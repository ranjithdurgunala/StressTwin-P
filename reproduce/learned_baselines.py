"""Exploratory history-only learned baselines (ridge, gradient boosting) vs the split-half twin.

Uses only the stored per-prediction records. Features of the prediction for observation i of an
author use information available before that observation, plus the time gap to it (which the twin also uses):
  last score, mean of past scores, number of past scores, previous gap, log gap to the target.
Models are fitted with author-grouped 5-fold cross-validation on the test authors of each held-out
community (a different protocol from the twin, which is fitted on separate training authors); the
predictive variance is the constant out-of-fold residual variance of the training folds.
Variants *_nogap drop the log gap to the target, leaving only information available before the target.
The result is exploratory and is not part of the confirmatory family.

Usage: python reproduce/learned_baselines.py --records <dir with results_seed0..4> --out results/learned_baselines.json
"""
import argparse, json
from pathlib import Path
import numpy as np, pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.linear_model import Ridge
from sklearn.model_selection import GroupKFold

C = ["anxiety", "bipolar", "depression", "suicidewatch"]


def nll(y, mu, v):
    return 0.5 * (np.log(2 * np.pi * v) + (y - mu) ** 2 / v)


def features(tw, last):
    """tw: split_half twin rows of one author (sorted by i); last: 'last' model rows (pred = previous score)."""
    d = tw.merge(last[["i", "pred"]].rename(columns={"pred": "prev"}), on="i").sort_values("i")
    y = d.y.to_numpy(); prev = d.prev.to_numpy()
    y0 = prev[0]
    hist = np.concatenate([[y0], y])
    n = len(d)
    mean_past = np.array([hist[: k + 1].mean() for k in range(n)])
    gap = d.gap_days.to_numpy()
    prev_gap = np.concatenate([[np.nan], gap[:-1]])
    X = np.column_stack([prev, mean_past, np.arange(1, n + 1), np.log1p(prev_gap * 24), np.log1p(gap * 24)])
    return d.assign(f_prev=X[:, 0], f_mean=X[:, 1], f_n=X[:, 2], f_pgap=X[:, 3], f_gap=X[:, 4])


def boot(d, B, rng):
    g = d.groupby("author")["d"].agg(["sum", "size"])
    s, n = g["sum"].to_numpy(), g["size"].to_numpy()
    idx = rng.integers(0, len(s), size=(B, len(s)))
    b = s[idx].sum(1) / n[idx].sum(1)
    return float(s.sum() / n.sum()), [float(x) for x in np.percentile(b, [2.5, 97.5])]


def one(rec, comm, rng, B):
    r = rec[(rec.community == comm) & (rec.condition == "within")]
    tw = r[r.model == "twin[split_half]"]; last = r[r.model == "last"]
    parts = []
    for a, g in tw.groupby("author"):
        parts.append(features(g, last[last.author == a]))
    D = pd.concat(parts, ignore_index=True)
    F = ["f_prev", "f_mean", "f_n", "f_pgap", "f_gap"]
    Xall = D[F].copy(); Xall["f_pgap"] = Xall["f_pgap"].fillna(Xall["f_pgap"].median())
    Xall = Xall.to_numpy(); y = D.y.to_numpy()
    out = {k: np.zeros(len(D)) for k in ("ridge", "gbm", "ridge_nogap", "gbm_nogap")}; var = {k: np.zeros(len(D)) for k in out}
    for tr, te in GroupKFold(5).split(Xall, y, D.author):
      for name, mdl in (("ridge", Ridge(alpha=1.0)),
                          ("gbm", HistGradientBoostingRegressor(max_depth=3, learning_rate=0.05, max_iter=150, random_state=0)),
                          ("ridge_nogap", Ridge(alpha=1.0)),
                          ("gbm_nogap", HistGradientBoostingRegressor(max_depth=3, learning_rate=0.05, max_iter=150, random_state=0))):
            X = Xall[:, :4] if name.endswith("nogap") else Xall   # nogap: drop the log gap to the target
            mu_, sd_ = X[tr].mean(0), X[tr].std(0) + 1e-9
            Xt, Xe = (X[tr] - mu_) / sd_, (X[te] - mu_) / sd_
            mdl.fit(Xt, y[tr])
            # predictive variance: variance of inner author-grouped 3-fold out-of-fold residuals within the training folds
            res = np.zeros(len(tr))
            for itr, ite in GroupKFold(3).split(Xt, y[tr], D.author.to_numpy()[tr]):
                m2 = type(mdl)(**mdl.get_params()); m2.fit(Xt[itr], y[tr][itr]); res[ite] = y[tr][ite] - m2.predict(Xt[ite])
            out[name][te] = mdl.predict(Xe); var[name][te] = res.var()
    res = {"n_obs": int(len(D)), "n_authors": int(D.author.nunique())}
    twin_nll = nll(y, D.pred.to_numpy(), D["var"].to_numpy())
    res["twin_nll"] = float(twin_nll.mean())
    for name in out:
        l = nll(y, out[name], var[name])
        d = pd.DataFrame({"author": D.author, "d": twin_nll - l})
        est, ci = boot(d, B, rng)
        res[name] = {"nll": float(l.mean()), "twin_minus_model": est, "ci95": ci, "mse": float(((y - out[name]) ** 2).mean())}
    res["twin_mse"] = float(((y - D.pred.to_numpy()) ** 2).mean())
    return res


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--records", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--seeds", type=int, default=5); ap.add_argument("--boot", type=int, default=1000)
    a = ap.parse_args(); rng = np.random.default_rng(0)
    out = {"note": "exploratory; history-only features; author-grouped 5-fold CV on test authors; constant residual variance", "seeds": []}
    for s in range(a.seeds):
        rec = pd.read_csv(Path(a.records) / f"results_seed{s}" / "records.csv.gz")
        out["seeds"].append({c: one(rec, c, rng, a.boot) for c in C})
        print("seed", s, "done", flush=True)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    json.dump(out, open(a.out, "w"), indent=1)
