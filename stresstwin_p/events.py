"""Event-anchored fidelity tests that need no ground-truth trajectories.

E1  reply dose-response (Zenodo 4266616 style data)
    For an author's own thread, delta = state at the author's later comment - state at the
    opening post. Regress delta on log(1 + replies received BEFORE that comment), controlling
    for the opening state, text length, hours since opening, and community.
    Predicted sign: negative (more replies -> larger fall in stress).
    Negative control: the same regression with replies received AFTER the comment. Later
    replies cannot cause an earlier change, so a large placebo coefficient means the
    association comes from something else (thread popularity, severity, regression to the
    mean) and the E1 result must not be read as an effect.

    Limits you must state in the paper: (1) controlling for a *measured* opening state does
    not remove regression to the mean completely, because that measurement is noisy;
    (2) replies are not 'support': they include any response. The placebo guards against
    both only partly.

Standard errors are clustered by author (CR1).
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import t as student_t


def ols_cluster(X: np.ndarray, y: np.ndarray, groups) -> dict:
    X = np.asarray(X, float); y = np.asarray(y, float)
    n, k = X.shape
    XtX_inv = np.linalg.pinv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    u = y - X @ beta
    g = pd.factorize(np.asarray(groups))[0]
    G = int(g.max()) + 1
    meat = np.zeros((k, k))
    for gi in range(G):
        idx = g == gi
        s = X[idx].T @ u[idx]
        meat += np.outer(s, s)
    adj = (G / max(G - 1, 1)) * ((n - 1) / max(n - k, 1))
    V = adj * XtX_inv @ meat @ XtX_inv
    se = np.sqrt(np.maximum(np.diag(V), 0.0))
    tstat = np.divide(beta, se, out=np.zeros_like(beta), where=se > 0)
    p = 2 * student_t.sf(np.abs(tstat), df=max(G - 1, 1))
    return {"beta": beta, "se": se, "t": tstat, "p": p, "n": n, "n_clusters": G}


def _design(df: pd.DataFrame, predictor: str):
    cols = {"dose": df[predictor].to_numpy(float),
            "state_open": df["state_open"].to_numpy(float),
            "log_len": np.log1p(df["len_open"].to_numpy(float)),
            "log_hours": np.log1p(df["hours_since_open"].to_numpy(float))}
    X = [np.ones(len(df))] + list(cols.values())
    names = ["const"] + list(cols)
    dummies = pd.get_dummies(df["community"], drop_first=True, dtype=float)
    for c in dummies.columns:
        X.append(dummies[c].to_numpy()); names.append(f"comm_{c}")
    return np.column_stack(X), names


def e1_dose_response(threads: pd.DataFrame) -> dict:
    """threads columns: author, community, state_open, state_after, n_replies_before,
    n_replies_after, len_open, hours_since_open."""
    need = {"author", "community", "state_open", "state_after", "n_replies_before",
            "n_replies_after", "len_open", "hours_since_open"}
    missing = need - set(threads.columns)
    if missing:
        raise ValueError(f"threads table is missing columns: {sorted(missing)}")
    df = threads.dropna(subset=list(need)).copy()
    df["delta"] = df["state_after"] - df["state_open"]
    df["dose_before"] = np.log1p(df["n_replies_before"])
    df["dose_after"] = np.log1p(df["n_replies_after"])
    out = {"n_threads": int(len(df)), "naive_mean_delta": float(df["delta"].mean())}
    for label, col in (("e1", "dose_before"), ("placebo", "dose_after")):
        X, names = _design(df, col)
        r = ols_cluster(X, df["delta"].to_numpy(), df["author"].to_numpy())
        i = names.index("dose")
        out[label] = {"beta": float(r["beta"][i]), "se": float(r["se"][i]),
                      "t": float(r["t"][i]), "p": float(r["p"][i]),
                      "n_clusters": r["n_clusters"]}
    e, p = out["e1"], out["placebo"]
    out["gate_a_pass"] = bool(e["beta"] < 0 and e["p"] < 0.05 and abs(p["beta"]) < 0.5 * abs(e["beta"]))
    out["gate_a_rule"] = ("E1 beta < 0 with p < 0.05 AND |placebo beta| < 0.5 * |E1 beta|. "
                          "The 0.5 is a proposed threshold; fix your own before any real-data run.")
    return out
