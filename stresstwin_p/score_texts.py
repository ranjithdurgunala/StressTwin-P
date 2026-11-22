"""Stage 1 (GPU): score every observation text with the StressTwin-F ensemble.

Output columns per obs_id:
  z_mean   mean over seeds of the stress logit  (logit of P(stress) = l1 - l0)
  z_var    variance over seeds (epistemic spread), ddof=1
  n_chars  text length
  z_a, z_b mean-over-seeds logits of the two halves of a long text (split-half noise pairs)
  n_half   mean half length in characters

The scorer is injected so this file does not guess how YOUR StressTwin-F checkpoints are stored.
Provide a function  load_scorers() -> list[callable]  where each callable maps list[str] ->
np.ndarray of stress logits (one per text). One callable per seed. Then run

    python -m stresstwin_p.score_texts --texts texts.csv --out scores.csv --hook my_module:load_scorers

A generic HuggingFace sequence-classification loader is provided (hf_scorers) for checkpoints
saved with save_pretrained; label index 1 must be 'stress'.
"""
from __future__ import annotations

import argparse
import importlib
import re

import numpy as np
import pandas as pd

SENT = re.compile(r"(?<=[.!?])\s+|\n+")
MIN_HALF_CHARS = 200


def split_halves(text: str, min_half_chars: int = MIN_HALF_CHARS):
    """Cut at the sentence boundary closest to the middle. None if either half is too short."""
    parts = [p for p in SENT.split(text) if p and p.strip()]
    if len(parts) < 2:
        return None
    lens = np.cumsum([len(p) + 1 for p in parts])
    k = int(np.argmin(np.abs(lens - lens[-1] / 2)))
    k = min(max(k, 0), len(parts) - 2)
    a, b = " ".join(parts[: k + 1]), " ".join(parts[k + 1:])
    if len(a) < min_half_chars or len(b) < min_half_chars:
        return None
    return a, b


def score_table(texts: pd.DataFrame, scorers, batch_size: int = 64, progress=None) -> pd.DataFrame:
    if not scorers and not getattr(scorers, "multi", False):
        raise ValueError("no scorers supplied")
    ids = texts["obs_id"].tolist()
    body = texts["text"].astype(str).tolist()

    multi = getattr(scorers, "multi", False)          # an object with multi_logits(texts) -> (n_seeds, n)
    n_seeds = scorers.n_seeds if multi else len(scorers)

    def run(xs):
        if multi:
            out = np.empty((n_seeds, len(xs)))
            for i in range(0, len(xs), batch_size):
                out[:, i:i + batch_size] = scorers.multi_logits(xs[i:i + batch_size])
                if progress:
                    progress(0, i, len(xs))
            return out
        out = np.empty((len(scorers), len(xs)))
        for si, f in enumerate(scorers):
            for i in range(0, len(xs), batch_size):
                out[si, i:i + batch_size] = np.asarray(f(xs[i:i + batch_size]), float)
                if progress:
                    progress(si, i, len(xs))
        return out

    full = run(body)
    res = pd.DataFrame({
        "obs_id": ids,
        "z_mean": full.mean(0),
        "z_var": full.var(0, ddof=1) if n_seeds > 1 else np.zeros(len(ids)),
        "n_chars": [len(x) for x in body],
    })
    halves = [(i, split_halves(x)) for i, x in enumerate(body)]
    halves = [(i, h) for i, h in halves if h is not None]
    res["z_a"] = np.nan; res["z_b"] = np.nan; res["n_half"] = np.nan
    if halves:
        idx = [i for i, _ in halves]
        za = run([h[0] for _, h in halves]).mean(0)
        zb = run([h[1] for _, h in halves]).mean(0)
        res.loc[idx, "z_a"] = za
        res.loc[idx, "z_b"] = zb
        res.loc[idx, "n_half"] = [(len(h[0]) + len(h[1])) / 2 for _, h in halves]
    return res


def hf_scorers(checkpoint_dirs, device: str = "cuda", max_len: int = 256):
    """One scorer per checkpoint directory. Requires torch + transformers (present on Colab)."""
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer

    scorers = []
    for d in checkpoint_dirs:
        tok = AutoTokenizer.from_pretrained(d)
        model = AutoModelForSequenceClassification.from_pretrained(d).to(device).eval()

        def f(texts, tok=tok, model=model):
            enc = tok(texts, truncation=True, max_length=max_len, padding=True, return_tensors="pt").to(device)
            with torch.no_grad():
                lg = model(**enc).logits.float().cpu().numpy()
            return lg[:, 1] - lg[:, 0]
        scorers.append(f)
    return scorers


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--texts", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--hook", help="module:function returning a list of scorers")
    ap.add_argument("--checkpoints", nargs="*", help="HF checkpoint dirs (alternative to --hook)")
    ap.add_argument("--stf-backbone", help="StressTwin-F: frozen backbone folder (with --stf-ckpt-dir)")
    ap.add_argument("--stf-ckpt-dir", help="StressTwin-F: folder with stresstwin_f_s0..4.pt")
    ap.add_argument("--stf-name", default="stresstwin_f", help="checkpoint prefix; use plain_ft for the plain scorer")
    ap.add_argument("--batch-size", type=int, default=64)
    a = ap.parse_args()
    if a.stf_backbone:
        from .stf_scorer import load_ensemble
        scorers = load_ensemble(a.stf_backbone, a.stf_ckpt_dir, name=a.stf_name)
    elif a.hook:
        mod, fn = a.hook.split(":")
        scorers = getattr(importlib.import_module(mod), fn)()
    elif a.checkpoints:
        scorers = hf_scorers(a.checkpoints)
    else:
        raise SystemExit("give --stf-backbone/--stf-ckpt-dir, --hook or --checkpoints")
    t = pd.read_csv(a.texts)
    score_table(t, scorers, a.batch_size).to_csv(a.out, index=False)


if __name__ == "__main__":
    main()
