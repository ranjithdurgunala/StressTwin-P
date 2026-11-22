"""Recompute every model-result number reported in the manuscript from the stage-2 outputs.

    python reproduce/compute_values.py --results results_dir --out values.json

results_dir holds results_seed0 ... results_seed4, each with results.json, results_plain.json and records.csv.gz
(the records files are large and are distributed separately, see docs/DATA.md).
Paired differences use stresstwin_p.stats.paired_diff (author-cluster bootstrap), as in run_all.
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from stresstwin_p import stats  # noqa: E402

COMMS = ["anxiety", "bipolar", "depression", "suicidewatch"]
TWIN = "twin[split_half]"
HIST = ["author_mean", "ewma", "gap_ewma", "global_mean", "twin[split_half/static]", "twin[split_half/nopool]", "shortcut"]
NOISE = ["twin[fixed]", "twin[conf_rule]"]
BONF = 1 - 0.05 / 24
Z90 = 1.6448536269514722


def gap_bucket(g):
    return np.where(g <= 1, "<=1d", np.where(g <= 7, "1-7d", ">7d"))


def one_seed(sd: Path, seed: int) -> dict:
    res = json.loads((sd / "results.json").read_text())
    resp = json.loads((sd / "results_plain.json").read_text())
    rec = pd.read_csv(sd / "records.csv.gz")
    out = {"seed": seed, "eligible": res["eligible_authors"], "settings": res["settings"], "e1": res["e1"],
           "e1_plain": resp["e1"], "comm": {}, "strata": res["strata"]}
    for c in COMMS:
        r = res["communities"][c]
        o = {"n_train": r["n_train_authors"], "n_test": r["n_test_authors"],
             "n_pred": r["within"]["summary"][TWIN]["n"], "kappa": {k: v["kappa"] for k, v in r["across"]["fits"].items()},
             "kappa_within": {k: v["kappa"] for k, v in r["within"]["fits"].items()},
             "within": {m: {"nll": s["nll"], "mse": s["mse"]} for m, s in r["within"]["summary"].items()},
             "across": {m: {"nll": s["nll"], "mse": s["mse"]} for m, s in r["across"]["summary"].items()},
             "conf_across": r["across"]["conformal"][TWIN], "conf_within": r["within"]["conformal"][TWIN],
             "paired": {}}
        for b in HIST + NOISE:
            p = stats.paired_diff(rec, TWIN, b, "nll", community=c, n_boot=2000)
            pb = stats.paired_diff(rec, TWIN, b, "nll", community=c, n_boot=2000, ci_level=BONF)
            o["paired"][b] = {"diff": p["diff"], "ci95": p["ci95"], "ci_bonf": pb["ci95"], "excl0": p["excludes_zero"],
                              "excl0_bonf": pb["excludes_zero"], "n_authors": p["n_authors"]}
        # Gaussian coverage by gap bucket, twin, both conditions
        sub = {}
        for cond in ("within", "across"):
            x = rec[(rec.model == TWIN) & (rec.community == c) & (rec.condition == cond)]
            hit = (np.abs(x.y - x.pred) <= Z90 * np.sqrt(x["var"])).to_numpy()
            gb = gap_bucket(x.gap_days.to_numpy())
            sub[cond] = {b: {"coverage": float(hit[gb == b].mean()), "n": int((gb == b).sum())} for b in ("<=1d", "1-7d", ">7d")}
        o["gauss_cov_by_gap"] = sub
        # plain-scorer twin: shortcut vs twin NLL
        pw = resp["communities"][c]["within"]["summary"]
        o["plain"] = {"twin_nll": pw[TWIN]["nll"], "shortcut_nll": pw["shortcut"]["nll"]}
        out["comm"][c] = o
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--seeds", default="0,1,2,3,4")
    a = ap.parse_args()
    seeds = [int(s) for s in a.seeds.split(",")]
    allv = [one_seed(Path(a.results) / f"results_seed{s}", s) for s in seeds]
    Path(a.out).write_text(json.dumps({"seeds": allv}, indent=1, default=float))
    print("wrote", a.out)


if __name__ == "__main__":
    main()
