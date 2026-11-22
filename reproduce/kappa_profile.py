"""Profile likelihood over the mean-reversion rate kappa, and a multi-start check of the optimiser.

Diagnostic of identifiability on real data, from the stored per-prediction records only. Timelines are rebuilt
from the held-out test authors' recorded scores (the first score of an author is recovered from the 'last'
baseline). Noise shape is fixed (R = 1; the fixed-noise arm), because the per-post noise inputs are not in the
records; s, sigma, tau and mu are optimised at every fixed kappa. This is therefore a diagnostic on test authors
with one noise arm, not a re-run of the confirmatory fits.

Usage: python reproduce/kappa_profile.py --records <dir with results_seed0..> --out results/kappa_profile.json [--seed 0]
"""
import argparse, json, time
from pathlib import Path
import numpy as np, pandas as pd
from stresstwin_p import ou_filter as O

C = ["anxiety", "bipolar", "depression", "suicidewatch"]
GRID = [0.001, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 5.0, 10.0, 30.0]
STARTS = [dict(kappa=0.001), dict(kappa=0.01), dict(kappa=0.1), dict(kappa=1.0), dict(kappa=5.0)]


def timelines(rec, comm):
    r = rec[(rec.community == comm) & (rec.condition == "within")]
    tw = r[r.model == "twin[split_half]"]; last = r[r.model == "last"]
    out = []
    for a, g in tw.groupby("author"):
        g = g.sort_values("i"); l = last[last.author == a].sort_values("i")
        y0 = l.pred.iloc[0]; t1 = g.t.iloc[0] - g.gap_days.iloc[0]
        t = np.concatenate([[t1], g.t.to_numpy()]); y = np.concatenate([[y0], g.y.to_numpy()])
        out.append(O.Timeline(str(a), t, y, np.ones(len(t))))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--records", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--seed", type=int, default=0); a = ap.parse_args()
    rec = pd.read_csv(Path(a.records) / f"results_seed{a.seed}" / "records.csv.gz")
    res = {"note": "fixed-noise arm (R = 1) on held-out test authors; other parameters optimised at each fixed kappa", "seed": a.seed, "communities": {}}
    for c in C:
        t0 = time.time(); tls = timelines(rec, c)
        free = O.fit_ou(tls, seed=0)
        prof = []
        for k in GRID:
            f = O.fit_ou(tls, seed=0, fixed={"kappa": k})
            prof.append({"kappa": k, "nll": float(f.neg_loglik), "sigma": f.params.sigma, "tau": f.params.tau, "s": f.params.noise_scale})
        ms = []
        for s0 in STARTS:
            sd = float(np.std(np.concatenate([t.y for t in tls])))
            init = O.OUParams(s0["kappa"], 0.3 * sd * (1 + s0["kappa"] % 3), 1.2 * sd / (1 + s0["kappa"] % 2), float(np.mean(np.concatenate([t.y for t in tls]))), 1.0)
            f = O.fit_ou(tls, seed=0, init=init)
            ms.append({"init_kappa": s0["kappa"], "kappa": f.params.kappa, "nll": float(f.neg_loglik), "at_bound": f.at_bound, "converged": f.converged})
        res["communities"][c] = {"n_authors": len(tls), "free_fit": {"kappa": free.params.kappa, "nll": float(free.neg_loglik), "at_bound": free.at_bound},
                                 "profile": prof, "multistart": ms}
        print(c, "done", round(time.time() - t0), "s", flush=True)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True); json.dump(res, open(a.out, "w"), indent=1, default=float)
