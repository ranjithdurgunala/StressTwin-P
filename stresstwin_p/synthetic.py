"""Synthetic timelines for testing the harness. NOT evidence about real people.

What a synthetic result can show: the code recovers planted parameters and detects planted
effects, and that a control that should fail does fail. What it cannot show: that any of this
holds on real posts. Noise here depends on text length and ensemble variance by construction,
so the split-half noise arm is favoured by design; the real-data check is in the notebook
(does the fitted noise track annotator agreement and length on Dreaddit?).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

DEFAULT_TRUE = dict(kappa=0.15, sigma=0.8, tau=0.9, mu=0.0, a0=0.15, a1=60.0, a2=3.0)


def _ou_path(t, kappa, sigma, rng):
    x = np.empty(len(t))
    x[0] = rng.normal(0, sigma)
    for i in range(1, len(t)):
        phi = np.exp(-kappa * (t[i] - t[i - 1]))
        x[i] = phi * x[i - 1] + rng.normal(0, sigma * np.sqrt(1 - phi ** 2))
    return x


def simulate_obs(authors_per_community: dict, seed: int = 0, horizon_days: float = 365.0,
                 community_bias: dict | None = None, community_mu: dict | None = None,
                 true: dict | None = None, min_obs: int = 3) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    tr = {**DEFAULT_TRUE, **(true or {})}
    community_bias = community_bias or {}
    community_mu = community_mu or {}
    rows = []
    for comm, n_auth in authors_per_community.items():
        b = community_bias.get(comm, 0.0)
        mu_c = tr["mu"] + community_mu.get(comm, 0.0)
        for a in range(n_auth):
            rate = np.exp(rng.normal(np.log(0.08), 0.8))        # posts per day, heterogeneous
            n = max(int(rng.poisson(rate * horizon_days)), 0)
            if n < min_obs:
                n = min_obs
            t = np.sort(rng.uniform(0, horizon_days, n))
            m = rng.normal(mu_c, tr["tau"])
            level = m + _ou_path(t, tr["kappa"], tr["sigma"], rng)
            n_chars = np.clip(np.exp(rng.normal(np.log(600), 0.9, n)), 40, 8000)
            v = rng.gamma(2.0, 0.05, n)
            R = tr["a0"] + tr["a1"] / n_chars + tr["a2"] * v
            y = level + b + rng.normal(0, np.sqrt(R))
            Rh = tr["a0"] + tr["a1"] / (n_chars / 2) + tr["a2"] * v
            za = level + b + rng.normal(0, np.sqrt(Rh))
            zb = level + b + rng.normal(0, np.sqrt(Rh))
            for i in range(n):
                rows.append((f"{comm}_{a}", comm, t[i], y[i], v[i], n_chars[i], level[i], R[i],
                             za[i] if n_chars[i] >= 400 else np.nan,
                             zb[i] if n_chars[i] >= 400 else np.nan, n_chars[i] / 2))
    return pd.DataFrame(rows, columns=["author", "community", "t_days", "y", "ens_var", "n_chars",
                                       "true_level", "R_true", "za", "zb", "n_half"])


def simulate_threads(n_threads: int, seed: int = 0, beta: float = 0.0, rho: float = 0.6,
                     measure_sd: float = 0.5, confound: float = 0.0,
                     communities=("c0", "c1")) -> pd.DataFrame:
    """beta: true effect of log(1+replies before) on the change in stress.
    confound: how strongly the person's severity drives BOTH reply counts (before and after)."""
    rng = np.random.default_rng(seed)
    a = rng.normal(0, 1, n_threads)                     # true opening level
    lam = np.exp(0.8 + confound * a)
    n_before = rng.poisson(lam)
    n_after = rng.poisson(lam)                           # independent draw, same driver
    b = rho * a + beta * np.log1p(n_before) + rng.normal(0, 0.4, n_threads)
    return pd.DataFrame({
        "author": [f"u{i // 2}" for i in range(n_threads)],   # about two threads per author
        "community": rng.choice(communities, n_threads),
        "state_open": a + rng.normal(0, measure_sd, n_threads),
        "state_after": b + rng.normal(0, measure_sd, n_threads),
        "n_replies_before": n_before, "n_replies_after": n_after,
        "len_open": np.exp(rng.normal(6, 0.7, n_threads)),
        "hours_since_open": np.exp(rng.normal(2.0, 1.0, n_threads)),
    })
