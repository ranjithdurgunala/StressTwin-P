"""Human pairwise validation of within-person change (optional objective O6b; needs ethics approval for
annotator access to text, and the same privacy controls as the main data).

Why: every other test compares the model with the model. This is the one test that compares it with people.
Annotators see two posts by the SAME author (never any score, state, date, community or order cue) and
answer: which post expresses more stress?  A / B / SAME.  The direction of the model's state (or raw score)
between the two posts is then compared with the human answer.

  sample_pairs(obs, texts, value, n_pairs, ...)  -> (sheet, key)
        sheet: pair_id, text_a, text_b          (give to annotators)
        key:   pair_id, obs_a, obs_b, value_a, value_b   (keep private; order was randomised)
  agreement(key, labels, ...)                    -> accuracy vs the model direction (ties excluded) with author-free
                                                    bootstrap CI (one pair per author, so pairs are independent)
  cohen_kappa(l1, l2)                            -> inter-annotator agreement; report it before the model comparison
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def sample_pairs(obs: pd.DataFrame, texts: pd.DataFrame, value: pd.Series, n_pairs: int = 200,
                 min_gap_days: float = 3.0, min_abs_diff: float = 0.0, seed: int = 0):
    """One pair per author. value: Series indexed by obs_id (model state or score). A larger min_abs_diff makes the
    task easier for the model; keep 0 for the headline analysis and report a stratified version as secondary."""
    rng = np.random.default_rng(seed)
    t = texts.set_index("obs_id")["text"]
    rows = []
    for a, g in obs.sort_values("t_days").groupby("author", sort=False):
        g = g[g.obs_id.isin(t.index) & g.obs_id.isin(value.index)]
        if len(g) < 2:
            continue
        ids, ts = g.obs_id.to_numpy(), g.t_days.to_numpy()
        cand = [(i, j) for i in range(len(g)) for j in range(i + 1, len(g))
                if ts[j] - ts[i] >= min_gap_days and abs(value[ids[j]] - value[ids[i]]) >= min_abs_diff]
        if not cand:
            continue
        i, j = cand[rng.integers(len(cand))]
        if rng.random() < 0.5:                       # randomise display order so time order is not a cue
            i, j = j, i
        rows.append((str(a), ids[i], ids[j]))
    rng.shuffle(rows)
    rows = rows[:n_pairs]
    key = pd.DataFrame([(f"p{k:04d}", a, b, float(value[a]), float(value[b])) for k, (_, a, b) in enumerate(rows)],
                       columns=["pair_id", "obs_a", "obs_b", "value_a", "value_b"])
    sheet = pd.DataFrame({"pair_id": key.pair_id, "text_a": [t[x] for x in key.obs_a], "text_b": [t[x] for x in key.obs_b]})
    return sheet, key


def cohen_kappa(l1, l2) -> float:
    l1, l2 = np.asarray(l1), np.asarray(l2)
    cats = sorted(set(l1) | set(l2))
    po = float(np.mean(l1 == l2))
    pe = sum(float(np.mean(l1 == c)) * float(np.mean(l2 == c)) for c in cats)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def agreement(key: pd.DataFrame, labels: pd.DataFrame, n_boot: int = 2000, seed: int = 0) -> dict:
    """labels: pair_id, label in {'A','B','SAME'} (consensus of annotators). Ties are excluded from accuracy and
    their share is reported. Chance is 0.5."""
    m = key.merge(labels, on="pair_id", validate="1:1")
    m = m[m.label.isin(["A", "B", "SAME"])]
    n_same = int((m.label == "SAME").sum())
    d = m[m.label != "SAME"].copy()
    if len(d) == 0:
        return {"n": 0, "n_same": n_same}
    model_says_a = (d.value_a > d.value_b).to_numpy()
    human_says_a = (d.label == "A").to_numpy()
    hit = (model_says_a == human_says_a).astype(float)
    rng = np.random.default_rng(seed)
    boots = hit[rng.integers(0, len(hit), size=(n_boot, len(hit)))].mean(1)
    lo, hi = np.percentile(boots, [2.5, 97.5])
    return {"n": int(len(d)), "n_same": n_same, "share_same": n_same / max(len(m), 1),
            "accuracy": float(hit.mean()), "ci95": [float(lo), float(hi)], "beats_chance": bool(lo > 0.5)}
