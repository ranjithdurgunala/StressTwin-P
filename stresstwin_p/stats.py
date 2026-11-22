"""Author-level inference for model comparisons.

Observations from one author are not independent, so every interval here resamples AUTHORS
(cluster bootstrap), never rows. Differences are paired: model A and model B are scored on the
same (author, observation) pairs.

  paired_diff(records, a, b, metric)   mean loss(A) - loss(B), 95% author-bootstrap CI.
                                       Negative = A better. metric: 'se' (squared error) or 'nll'.
  precision(records, a, b, metric)     the same CI plus the smallest true difference this sample could
                                       detect with ~80% power at two-sided 5% (about 2.8 x SE).
                                       Use it AFTER the data audit to decide whether the sample is big enough.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import baselines as B


def _loss(r: pd.DataFrame, metric: str) -> np.ndarray:
    if metric == "se":
        return ((r.y - r.pred) ** 2).to_numpy()
    if metric == "nll":
        return -B.gaussian_logscore(r.y.to_numpy(), r.pred.to_numpy(), r["var"].to_numpy())
    raise ValueError("metric must be 'se' or 'nll'")


def _paired(records: pd.DataFrame, a: str, b: str, metric: str, community=None, condition="within") -> pd.DataFrame:
    r = records[records.condition == condition]
    if community is not None:
        r = r[r.community == community]
    keys = ["community", "author", "i"]
    ra, rb = r[r.model == a].copy(), r[r.model == b].copy()
    ra["la"], rb["lb"] = _loss(ra, metric), _loss(rb, metric)
    m = ra[keys + ["la"]].merge(rb[keys + ["lb"]], on=keys, validate="1:1")
    m["d"] = m.la - m.lb
    return m


def paired_diff(records, a, b, metric="se", community=None, condition="within", n_boot=2000, seed=0, ci_level=0.95) -> dict:
    """ci_level: use 1 - 0.05/m (Bonferroni) for a family of m confirmatory comparisons."""
    m = _paired(records, a, b, metric, community, condition)
    if len(m) == 0:
        return {"n_obs": 0, "n_authors": 0}
    per_author = m.groupby("author")["d"].mean()
    w = m.groupby("author")["d"].size().loc[per_author.index].to_numpy().astype(float)
    d = per_author.to_numpy()
    rng = np.random.default_rng(seed)
    n = len(d)
    idx = rng.integers(0, n, size=(n_boot, n))
    boots = (d[idx] * w[idx]).sum(1) / w[idx].sum(1)          # observation-weighted mean over resampled authors
    est = float((d * w).sum() / w.sum())
    q = (1 - ci_level) / 2 * 100
    lo, hi = np.percentile(boots, [q, 100 - q])
    return {"n_obs": int(len(m)), "n_authors": int(n), "diff": est, "ci95": [float(lo), float(hi)], "ci_level": ci_level,
            "se": float(boots.std(ddof=1)), "excludes_zero": bool(lo > 0 or hi < 0)}


def precision(records, a, b, metric="se", community=None, condition="within", n_boot=2000, seed=0, ci_level=0.95) -> dict:
    r = paired_diff(records, a, b, metric, community, condition, n_boot, seed, ci_level)
    if r.get("n_authors", 0) > 1:
        r["min_detectable_diff_80pct_power"] = float(2.8 * r["se"])
    return r
