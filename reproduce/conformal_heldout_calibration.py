"""Author-disjoint conformal calibration check, from the stored per-prediction records.

The released pipeline calibrates the static conformal quantile on the training authors' in-sample residuals.
This script instead calibrates on authors who were used neither to fit the state parameters nor to evaluate:
the held-out community's test authors are split at random into a calibration half and an evaluation half
(200 random splits per seed, community and condition). The split-conformal quantile q is the
ceil((n+1)(1-alpha))/n empirical quantile of |y - pred|/sqrt(var) over the calibration observations; coverage and
width are measured on the evaluation authors. For comparison, the Gaussian interval and the original in-sample
static quantile (results/seed*/results.json) are evaluated on the same evaluation halves.
Caveat: in the 'across' condition the calibration authors come from the target community, which is a different
(and more favourable) calibration set than the other-community authors used by the released pipeline.

Usage: python reproduce/conformal_heldout_calibration.py --records <dir with results_seed0..4> --out results/conformal_heldout.json
"""
import argparse, json
from pathlib import Path
import numpy as np, pandas as pd

C = ["anxiety", "bipolar", "depression", "suicidewatch"]; ALPHA = 0.10; Z = 1.6448536269514722
GAPS = [("<=1d", 0, 1), ("1-7d", 1, 7), (">7d", 7, 1e9)]


def one(r, q_insample, rng, n_splits):
    a = r.author.to_numpy(); ua = np.unique(a); idx = {x: np.flatnonzero(a == x) for x in ua}
    s = (r.y - r.pred).abs().to_numpy() / np.sqrt(r["var"].to_numpy()); gap = r.gap_days.to_numpy()
    out = {k: [] for k in ("cal_cov", "cal_w", "gauss_cov", "gauss_w", "ins_cov", "ins_w", "q")}; gp = {g[0]: [] for g in GAPS}
    sd = np.sqrt(r["var"].to_numpy())
    for _ in range(n_splits):
        perm = rng.permutation(ua); cal_a = set(perm[: len(ua) // 2])
        cm = np.isin(a, list(cal_a)); em = ~cm
        sc = np.sort(s[cm]); n = len(sc); k = int(np.ceil((n + 1) * (1 - ALPHA)))
        q = sc[min(k, n) - 1]
        w = lambda qq: float((2 * qq * sd[em]).mean())
        cov = lambda qq: float((s[em] <= qq).mean())
        out["cal_cov"].append(cov(q)); out["cal_w"].append(w(q)); out["gauss_cov"].append(cov(Z)); out["gauss_w"].append(w(Z))
        out["ins_cov"].append(cov(q_insample)); out["ins_w"].append(w(q_insample)); out["q"].append(float(q))
        for name, lo, hi in GAPS:
            m = em & (gap > lo) & (gap <= hi) if lo > 0 else em & (gap <= hi)
            gp[name].append((float((s[m] <= q).mean()) if m.sum() else np.nan, float((s[m] <= Z).mean()) if m.sum() else np.nan, float((s[m] <= q_insample).mean()) if m.sum() else np.nan))
    res = {k: float(np.mean(v)) for k, v in out.items()}
    res["cal_cov_sd_over_splits"] = float(np.std(out["cal_cov"]))
    res["by_gap"] = {g: {"heldout_cal": float(np.nanmean([x[0] for x in v])), "gaussian": float(np.nanmean([x[1] for x in v])), "insample_static": float(np.nanmean([x[2] for x in v]))} for g, v in gp.items()}
    res["q_insample"] = float(q_insample); res["n_obs"] = int(len(r)); res["n_authors"] = int(len(ua))
    return res


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--records", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--splits", type=int, default=200); a = ap.parse_args(); rng = np.random.default_rng(0)
    out = {"alpha": ALPHA, "n_splits": a.splits, "seeds": []}
    for s in range(5):
        d = Path(a.records) / f"results_seed{s}"; res = json.load(open(d / "results.json"))["communities"]
        rec = pd.read_csv(d / "records.csv.gz"); rec = rec[rec.model == "twin[split_half]"]
        o = {}
        for c in C:
            o[c] = {}
            for cond in ("within", "across"):
                q0 = res[c][cond]["conformal"]["twin[split_half]"]["static_conformal"]["q"]
                o[c][cond] = one(rec[(rec.community == c) & (rec.condition == cond)], q0, rng, a.splits)
        out["seeds"].append(o); print("seed", s, flush=True)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True); json.dump(out, open(a.out, "w"), indent=1)
