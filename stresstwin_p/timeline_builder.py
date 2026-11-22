"""Build author timelines and thread tables from Reddit submissions + comments.

Written for the common Pushshift field names. Zenodo 4266616's inner key names are NOT verified,
so every field is looked up through aliases and a missing essential field raises SchemaError
listing the keys that were actually found. If you hit that, send the message back and the
alias list gets one more line.

An observation of an AUTHOR is only:
  1. the author's own submission (title + body), and
  2. the author's own comments inside THEIR OWN thread.
Comments on other people's threads are replies to other people's problems, not the author's
own state, and are excluded.

Privacy: author names are replaced by a salted HMAC hash at ingestion and never written out.
The salt must be at least 16 bytes and kept outside the repository. Text is written to a
separate file (texts.csv) used only for scoring; the analysis tables carry no text.
"""
from __future__ import annotations

import hashlib
import hmac
import re
from pathlib import Path

import numpy as np
import pandas as pd

from .safe_io import load_pickle

ALIASES = {
    "id": ["id", "post_id", "comment_id", "name"],
    "author": ["author", "user", "username"],
    "time": ["created_utc", "created", "timestamp"],
    "text": ["selftext", "body", "text", "content"],
    "title": ["title"],
    "community": ["subreddit", "community"],
    "thread": ["link_id", "post_id", "thread_id", "submission_id"],
}
MISSING_AUTHOR = {None, "", "[deleted]", "[removed]", "deleted"}
BOT = re.compile(r"(bot$|^automoderator$|moderator)", re.I)
BAD_TEXT = {"", "[removed]", "[deleted]"}


class SchemaError(ValueError):
    pass


def _get(row: dict, kind: str):
    for k in ALIASES[kind]:
        if k in row and row[k] is not None:
            return row[k]
    return None


def _strip_prefix(x):
    return re.sub(r"^t[1-6]_", "", str(x)) if x is not None else None


def _epoch(v):
    if isinstance(v, pd.Timestamp):                     # Zenodo 4266616 stores pandas Timestamps (naive, UTC by convention)
        if pd.isna(v):
            return None
        v = v.tz_localize("UTC") if v.tzinfo is None else v.tz_convert("UTC")
        return v.timestamp()
    try:
        x = float(v)
        return x / 1000.0 if x > 1e12 else x
    except (TypeError, ValueError):
        try:
            return pd.Timestamp(v, tz="UTC").timestamp()
        except Exception:
            return None


def _flatten(obj, key_name="_key"):
    if isinstance(obj, dict):
        rows = []
        for k, v in obj.items():
            if isinstance(v, dict):
                r = dict(v); r.setdefault(key_name, k); rows.append(r)
        return rows
    if isinstance(obj, (list, tuple)):
        return [dict(x) for x in obj if isinstance(x, dict)]
    return []


def _hash(author, salt: bytes) -> str:
    return hmac.new(salt, str(author).encode(), hashlib.sha256).hexdigest()[:20]


def build(posts_raw, comments_raw, salt: bytes, post2comments=None, min_text_chars: int = 20, drop_removed_body: bool = True):
    """Return (observations, texts, threads, stats). All inputs are lists of dict rows
    (or dict-of-dicts) in Reddit-API style."""
    if len(salt) < 16:
        raise ValueError("salt must be at least 16 bytes; keep it outside the repo")
    posts_raw, comments_raw = _flatten(posts_raw), _flatten(comments_raw)
    if not posts_raw:
        raise SchemaError("no post rows found")
    sample = posts_raw[0]
    for kind in ("author", "time"):
        if _get(sample, kind) is None:
            raise SchemaError(f"posts: no '{kind}' field. Keys seen: {sorted(sample)}")
    if _get(sample, "id") is None and "_key" not in sample:
        raise SchemaError(f"posts: no id field. Keys seen: {sorted(sample)}")

    stats = {"posts_in": len(posts_raw), "comments_in": len(comments_raw)}
    posts = {}
    for r in posts_raw:
        pid = _strip_prefix(_get(r, "id")) or _strip_prefix(r.get("_key"))
        au, t = _get(r, "author"), _epoch(_get(r, "time"))
        if au in MISSING_AUTHOR or BOT.search(str(au)) or t is None:
            continue
        body = str(_get(r, "text") or "").strip()
        if body in BAD_TEXT:
            # About a third of posts in Zenodo 4266616 have an empty or '[removed]' body. Scoring "title + [removed]" would feed the
            # placeholder to the scorer, and keeping title-only posts would over-represent posts whose body was taken down (selection).
            stats["posts_removed_or_empty_body"] = stats.get("posts_removed_or_empty_body", 0) + 1
            if drop_removed_body:
                continue
            body = ""
        text = ((_get(r, "title") or "") + "\n" + body).strip()
        posts[pid] = dict(author=au, t=t, text=text, community=str(_get(r, "community") or "unknown").lower())
    stats["posts_kept_author_time"] = len(posts)

    # link comments to threads
    cid_to_thread = {}
    if post2comments:
        for pid, cs in post2comments.items():
            pid = _strip_prefix(pid)
            if isinstance(cs, (list, tuple, set, np.ndarray)):
                for c in cs:
                    raw = _get(c, "id") if isinstance(c, dict) else c
                    if raw is None:
                        continue
                    cid_to_thread[_strip_prefix(raw)] = pid
    comments = []
    no_thread = 0
    if comments_raw:
        s = comments_raw[0]
        for kind in ("author", "time"):
            if _get(s, kind) is None:
                raise SchemaError(f"comments: no '{kind}' field. Keys seen: {sorted(s)}")
    for r in comments_raw:
        cid = _strip_prefix(_get(r, "id") or r.get("_key"))
        thread = _strip_prefix(_get(r, "thread")) or cid_to_thread.get(cid)
        if thread is None:
            no_thread += 1
            continue
        au, t = _get(r, "author"), _epoch(_get(r, "time"))
        if t is None:
            continue
        comments.append(dict(id=cid, thread=thread, author=au, t=t, text=str(_get(r, "text") or "").strip()))
    stats["comments_without_thread_link"] = no_thread
    if comments_raw and no_thread == len(comments_raw):
        raise SchemaError("no comment could be linked to a thread. Comment keys seen: "
                          f"{sorted(comments_raw[0])}. Need link_id/post_id or a post2comments map.")

    by_thread: dict[str, list] = {}
    for c in comments:
        by_thread.setdefault(c["thread"], []).append(c)

    obs, texts, threads = [], [], []
    for pid, p in posts.items():
        if p["text"] in BAD_TEXT or len(p["text"]) < min_text_chars:
            continue
        h = _hash(p["author"], salt)
        open_id = f"s:{pid}"
        obs.append((open_id, h, p["community"], p["t"] / 86400.0, "submission", len(p["text"])))
        texts.append((open_id, p["text"]))
        cs = sorted(by_thread.get(pid, []), key=lambda c: c["t"])
        own = [c for c in cs if c["author"] == p["author"] and c["text"] not in BAD_TEXT and len(c["text"]) >= min_text_chars]
        for c in own:
            oid = f"c:{c['id']}"
            obs.append((oid, h, p["community"], c["t"] / 86400.0, "own_comment", len(c["text"])))
            texts.append((oid, c["text"]))
        if own:
            last = own[-1]
            others = [c for c in cs if c["author"] != p["author"]]
            threads.append(dict(
                thread_id=pid, author=h, community=p["community"],
                obs_id_open=open_id, obs_id_after=f"c:{last['id']}",
                n_replies_before=sum(1 for c in others if c["t"] < last["t"]),
                n_replies_after=sum(1 for c in others if c["t"] > last["t"]),
                len_open=len(p["text"]),
                hours_since_open=max((last["t"] - p["t"]) / 3600.0, 0.0)))
    obs_df = pd.DataFrame(obs, columns=["obs_id", "author", "community", "t_days", "kind", "n_chars"])
    txt_df = pd.DataFrame(texts, columns=["obs_id", "text"])
    thr_df = pd.DataFrame(threads)
    stats.update(observations=len(obs_df), authors=int(obs_df.author.nunique()) if len(obs_df) else 0,
                 threads_with_own_comment=len(thr_df))
    return obs_df.sort_values(["author", "t_days"]).reset_index(drop=True), txt_df, thr_df, stats


def load_zenodo_4266616(folder, salt: bytes, community_from_filename: bool = True):
    """Zenodo 4266616 unzips to <subreddit>_post2data.pkl, <subreddit>_post2comments.pkl and
    <subreddit>_comment2data.pkl (file names verified from the record page; the keys INSIDE the pickles are not).
    Un-prefixed names (post2data.pkl) are also accepted. The subreddit is taken from the prefix."""
    folder = Path(folder)
    # The zip was made on macOS: it also holds a __MACOSX/ folder of 1 KB AppleDouble stubs named ._<file>.pkl. They are not
    # pickles and must be skipped, or they would be read as extra "communities" and fail.
    sets = sorted(p for p in folder.rglob("*post2data.pkl")
                  if "__MACOSX" not in p.parts and not p.name.startswith("._"))
    if not sets:
        raise FileNotFoundError(f"no *post2data.pkl under {folder}. Files found: "
                                f"{sorted(p.name for p in folder.rglob('*.pkl'))[:20]}")
    P, C, link = [], [], {}
    for p2d in sets:
        d = p2d.parent
        prefix = p2d.name[: -len("post2data.pkl")].rstrip("_")
        community = prefix or d.name
        posts = _flatten(load_pickle(p2d))
        if community_from_filename:
            for r in posts:
                r.setdefault("subreddit", community)
        P.extend(posts)
        stem = f"{prefix}_" if prefix else ""
        c2d, p2c = d / f"{stem}comment2data.pkl", d / f"{stem}post2comments.pkl"
        if c2d.exists():
            comments = _flatten(load_pickle(c2d))
            for r in comments:
                r.setdefault("subreddit", community)
            C.extend(comments)
        if p2c.exists():
            m = load_pickle(p2c)
            if isinstance(m, dict):
                link.update(m)
    return build(P, C, salt, post2comments=link or None)


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Build observation/text/thread tables from Zenodo 4266616")
    ap.add_argument("--folder", required=True)
    ap.add_argument("--salt-file", required=True, help="file with >=16 secret bytes; create once, keep OUT of any repo")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    salt = Path(a.salt_file).read_bytes().strip()
    obs, txt, thr, stats = load_zenodo_4266616(a.folder, salt)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    obs.to_csv(out / "observations.csv", index=False)
    txt.to_csv(out / "texts.csv", index=False)          # contains text: keep private, do not share or commit
    thr.to_csv(out / "threads.csv", index=False)
    print(stats)


if __name__ == "__main__":
    main()
