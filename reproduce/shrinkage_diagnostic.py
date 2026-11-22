"""Posterior-shrinkage diagnostic from stored records (no refit).

For each prediction, the twin forecast is a weighted average of the global mean and the author's running mean:
w = (twin - global) / (author_mean - global). The empirical weight in each bin of the number of past scores n
is the least-squares slope through the origin of (twin - global) on (author_mean - global). With a static
person baseline and noise variance v, theory gives w(n) = n*tau2 / (n*tau2 + v); v is fitted to the empirical
weights for each community (tau2 taken from the fitted model). Writes results/shrinkage.json and figures/fig4_shrinkage.png.
"""
import argparse, json
from pathlib import Path
import numpy as np, pandas as pd
from scipy.optimize import minimize_scalar

C = ["anxiety", "bipolar", "depression", "suicidewatch"]
BINS = [(1, 1), (2, 2), (3, 4), (5, 8), (9, 16), (17, 10**6)]
LAB = ["1", "2", "3-4", "5-8", "9-16", "17+"]

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--records", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--fig", default=None); a = ap.parse_args()
    emp = {c: {l: [] for l in LAB} for c in C}; tau2 = {c: [] for c in C}; nmid = {}
    for s in range(5):
        d = Path(a.records) / f"results_seed{s}"
        res = json.load(open(d / "results.json"))["communities"]
        rec = pd.read_csv(d / "records.csv.gz"); rec = rec[(rec.condition == "within")]
        for c in C:
            tau2[c].append(res[c]["within"]["fits"]["split_half"]["tau"] ** 2)
            r = rec[rec.community == c]
            piv = {m: r[r.model == m].set_index(["author", "i"]) for m in ("twin[split_half]", "author_mean", "global_mean")}
            j = piv["twin[split_half]"][["pred"]].join(piv["author_mean"][["pred"]], rsuffix="_a").join(piv["global_mean"][["pred"]], rsuffix="_g").reset_index()
            j["u"] = j.pred_a - j.pred_g; j["w"] = j.pred - j.pred_g
            for (lo, hi), l in zip(BINS, LAB):
                b = j[(j.i >= lo) & (j.i <= hi)]
                emp[c][l].append(float((b.u * b.w).sum() / (b.u ** 2).sum()))
                nmid.setdefault(l, float(b.i.mean()))
    out = {"bins": LAB, "mean_n_in_bin": nmid, "communities": {}}
    for c in C:
        t2 = float(np.mean(tau2[c])); e = [float(np.mean(emp[c][l])) for l in LAB]
        n = np.array([nmid[l] for l in LAB])
        f = lambda lv: ((n * t2 / (n * t2 + np.exp(lv)) - np.array(e)) ** 2).sum()
        v = float(np.exp(minimize_scalar(f, bounds=(-6, 6), method="bounded").x))
        out["communities"][c] = {"tau2": t2, "v_fitted": v, "empirical_weight": e,
                                 "theory_weight": [float(x) for x in n * t2 / (n * t2 + v)]}
    Path(a.out).parent.mkdir(parents=True, exist_ok=True); json.dump(out, open(a.out, "w"), indent=1)
    if a.fig:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt; plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "Liberation Serif", "DejaVu Serif"], "pdf.fonttype": 42})
        fig, ax = plt.subplots(figsize=(3.4, 2.5), dpi=300)
        cols = ["#0072B2", "#D55E00", "#009E73", "#CC79A7"]; mk = ["o", "s", "^", "D"]
        xs = np.arange(len(LAB))
        for c, col, m in zip(C, cols, mk):
            o = out["communities"][c]
            ax.plot(xs, o["empirical_weight"], marker=m, color=col, lw=1, ms=3, label=c.capitalize())
            ax.plot(xs, o["theory_weight"], ls="--", color=col, lw=0.8)
        ax.set_xticks(xs); ax.set_xticklabels(LAB, fontsize=6.5); ax.tick_params(axis="y", labelsize=6.5)
        ax.set_xlabel("Number of past scores of the author", fontsize=7); ax.set_ylabel("Weight on the author's own mean", fontsize=7)
        ax.set_ylim(0, 1.05); ax.legend(fontsize=6, frameon=False, loc="lower right"); ax.grid(alpha=.25, lw=.4)
        for s in ("top", "right"): ax.spines[s].set_visible(False)
        fig.tight_layout(); Path(a.fig).parent.mkdir(parents=True, exist_ok=True); fig.savefig(a.fig); fig.savefig(str(Path(a.fig).with_suffix(".pdf")))
