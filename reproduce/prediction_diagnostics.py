"""Diagnostics computed from the per-prediction records only (no model refit).

    python reproduce/prediction_diagnostics.py --records <dir with results_seed0..4> --out results/diagnostics.json

Each records file has one row per scored test prediction: model, author (hashed), i, n_obs, t (days), gap_days,
y, pred, var, community, condition. The analyses are

  calibration    coverage of central Gaussian intervals at 50/80/90/95% and mean squared standardised residual
  variance       whether predicted variance tracks squared error, per noise arm (Spearman, slope, quintile table)
  gap            Gaussian and static-conformal coverage and width by gap since the previous post
  halves         first-half versus second-half of the observation window: NLL, coverage, twin-minus-baseline NLL
                 (the model is NOT refitted on the first half; this checks stability of held-out predictions in time)
Author-cluster bootstrap (B draws over authors) gives 95% intervals.
"""
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import norm, spearmanr

TWIN, FIX, CONF = "twin[split_half]", "twin[fixed]", "twin[conf_rule]"
BASE = ["author_mean", "ewma", "global_mean", "shortcut"]
COMMS = ["anxiety", "bipolar", "depression", "suicidewatch"]
LEVELS = [0.5, 0.8, 0.9, 0.95]
GAPS = [("<=1d", 0, 1), ("1-7d", 1, 7), (">7d", 7, 1e9)]
B = 400


def nll(y, m, v):
    v = np.maximum(v, 1e-12)
    return 0.5 * (np.log(2 * np.pi * v) + (y - m) ** 2 / v)


def cluster_ci(df, col, rng, fn=np.mean):
    """95% interval for the mean of `col`, resampling authors."""
    g = df.groupby("author")[col].agg(["sum", "count"])
    s, c = g["sum"].to_numpy(), g["count"].to_numpy()
    idx = rng.integers(0, len(s), (B, len(s)))
    est = s[idx].sum(1) / c[idx].sum(1)
    return [float(np.percentile(est, 2.5)), float(np.percentile(est, 97.5))]


def one_seed(sd: Path, seed: int) -> dict:
    rec = pd.read_csv(sd / "records.csv.gz")
    res = json.load(open(sd / "results.json"))["communities"]
    rng = np.random.default_rng(seed)
    out = {"seed": seed, "comm": {}}
    for c in COMMS:
        o = {}
        for cond in ("within", "across"):
            x = rec[(rec.community == c) & (rec.condition == cond)]
            piv = {m: x[x.model == m].set_index(["author", "i"]) for m in [TWIN, FIX, CONF] + BASE}
            t = piv[TWIN]
            r = {}
            # calibration
            d = {}
            for m in (TWIN, FIX, CONF):
                p = piv[m]; z = (p.y - p.pred) / np.sqrt(p["var"].clip(lower=1e-12))
                d[m] = {"z2_mean": float((z ** 2).mean()),
                        "coverage": {str(l): float((z.abs() <= norm.ppf(0.5 + l / 2)).mean()) for l in LEVELS}}
            r["calibration"] = d
            # variance validity
            v = {}
            for m in (TWIN, FIX, CONF):
                p = piv[m]; se = (p.y - p.pred) ** 2
                q = pd.qcut(p["var"], 5, labels=False, duplicates="drop")
                tab = pd.DataFrame({"v": p["var"], "se": se, "q": q}).groupby("q").mean()
                slope = float(np.polyfit(p["var"], se, 1)[0])
                v[m] = {"spearman": float(spearmanr(p["var"], se)[0]), "slope": slope,
                        "quintile_pred_var": tab.v.round(4).tolist(), "quintile_sq_err": tab.se.round(4).tolist()}
            r["variance"] = v
            # coverage / width by gap (Gaussian and static conformal at the stored quantile)
            q_static = res[c][cond]["conformal"][TWIN]["static_conformal"]["q"]
            g = {}
            sd_ = np.sqrt(t["var"].clip(lower=1e-12)); ae = (t.y - t.pred).abs()
            z90 = norm.ppf(0.95)
            for name, lo, hi in GAPS:
                mk = (t.gap_days > lo) & (t.gap_days <= hi) if lo > 0 else (t.gap_days <= hi)
                gg = {"n": int(mk.sum()),
                      "gaussian_cov": float((ae[mk] <= z90 * sd_[mk]).mean()), "gaussian_width": float(2 * z90 * sd_[mk].mean()),
                      "static_cov": float((ae[mk] <= q_static * sd_[mk]).mean()), "static_width": float(2 * q_static * sd_[mk].mean())}
                tmp = pd.DataFrame({"author": t.index.get_level_values(0)[mk.to_numpy()], "c": (ae[mk] <= z90 * sd_[mk]).astype(float).to_numpy()})
                gg["gaussian_cov_ci"] = cluster_ci(tmp, "c", rng)
                g[name] = gg
            r["gap"] = g
            # halves of the observation window
            med = t.t.median(); h = {}
            L = {m: nll(piv[m].y, piv[m].pred, piv[m]["var"]) for m in [TWIN] + BASE}
            for name, mk in (("first", t.t <= med), ("second", t.t > med)):
                hh = {"n": int(mk.sum()), "mean_y": float(t.y[mk].mean()),
                      "twin_nll": float(L[TWIN][mk].mean()),
                      "gaussian_cov": float((ae[mk] <= z90 * sd_[mk]).mean())}
                for b in BASE:
                    dif = (L[TWIN] - L[b])[mk]
                    tmp = pd.DataFrame({"author": dif.index.get_level_values(0), "d": dif.to_numpy()})
                    hh[f"twin_minus_{b}"] = float(dif.mean()); hh[f"twin_minus_{b}_ci"] = cluster_ci(tmp, "d", rng)
                h[name] = hh
            r["halves"] = h; r["median_t"] = float(med)
            o[cond] = r
        out["comm"][c] = o
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--records", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--seeds", default="0,1,2,3,4"); a = ap.parse_args()
    seeds = [int(s) for s in a.seeds.split(",")]
    allv = [one_seed(Path(a.records) / f"results_seed{s}", s) for s in seeds]
    Path(a.out).write_text(json.dumps({"seeds": allv}, indent=1, default=float)); print("written", a.out)


if __name__ == "__main__":
    main()
