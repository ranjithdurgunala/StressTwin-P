"""Stage 2 (CPU): assemble observations + scores, run LOCO and E1, write results.json and a plain report.

    python -m stresstwin_p.run_all --obs observations.csv --scores scores.csv --threads threads.csv --out results/
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from . import events, loco, stats


VARIANTS = ("static", "rw", "nopool")     # state-dynamics ablations


def assemble(obs: pd.DataFrame, scores: pd.DataFrame) -> pd.DataFrame:
    """Merge on obs_id. y = z_mean; the columns the LOCO harness expects."""
    d = obs.merge(scores.drop(columns=["n_chars"], errors="ignore"), on="obs_id", how="inner", validate="1:1")
    lost = len(obs) - len(d)
    d = d.rename(columns={"z_mean": "y", "z_var": "ens_var", "z_a": "za", "z_b": "zb"})
    d = d.replace([np.inf, -np.inf], np.nan).dropna(subset=["y", "ens_var", "t_days"])
    d.attrs["dropped_unscored"] = int(lost)
    d = loco.single_community(d)          # author-disjoint LOCO needs one community per author (see loco.single_community)
    d.attrs["dropped_unscored"] = int(lost)
    return d.sort_values(["author", "t_days"]).reset_index(drop=True)


def paired_table(rec: pd.DataFrame, communities, ref="twin[split_half]") -> list:
    """Twin minus each baseline, 95% author-bootstrap CI. Negative = twin better. Includes the sample's minimum
    detectable difference so under-powered comparisons are visible."""
    L = ["\n## Twin vs baselines, paired difference with 95% author-bootstrap CI (negative = twin better)",
         "| community | comparator | metric | diff | 95% CI | authors | min detectable (80% power) |", "|---|---|---|---|---|---|---|"]
    for c in communities:
        for b in ("author_mean", "ewma", "gap_ewma", "last", "global_mean", "shortcut", "twin[fixed]", "twin[conf_rule]",
                  "twin[split_half/static]", "twin[split_half/rw]", "twin[split_half/nopool]"):
            for met in ("se", "nll"):
                r = stats.precision(rec, ref, b, met, community=c, n_boot=1000)
                if r.get("n_obs", 0) == 0:
                    continue
                L.append(f"| {c} | {b} | {met} | {r['diff']:.3f} | [{r['ci95'][0]:.3f}, {r['ci95'][1]:.3f}] | {r['n_authors']} | "
                         f"{r.get('min_detectable_diff_80pct_power', float('nan')):.3f} |")
    return L


def report(res: dict, e1: dict | None, rec: pd.DataFrame | None = None) -> str:
    L = ["# StressTwin-P results (auto-generated; check the data source and the pilot setting in results.json before reading)\n"]
    for c, r in res["communities"].items():
        w = r["within"]["summary"]; a = r["across"]["summary"]
        L.append(f"## held-out community: {c}  (train authors {r['n_train_authors']})")
        L.append("| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |")
        L.append("|---|---|---|---|---|---|")
        for m in w:
            L.append(f"| {m} | {w[m]['mse']:.3f} | {a.get(m, {}).get('mse', float('nan')):.3f} | "
                     f"{w[m]['nll']:.3f} | {w[m].get('gauss_cov', float('nan')):.2f} | {w[m].get('gauss_width', float('nan')):.2f} |")
        L.append("\nConformal / Gaussian intervals, held-out community, within-community training (target 90%):")
        L.append("| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |")
        L.append("|---|---|---|---|")
        for m, cf in r["within"]["conformal"].items():
            f = lambda k: f"{cf[k]['coverage']:.2f} / {cf[k]['mean_width']:.2f}"
            L.append(f"| {m} | {f('gaussian')} | {f('static_conformal')} | {f('aci')} |")
        L.append("")
    if rec is not None and len(rec):
        L.extend(paired_table(rec, list(res["communities"])))
    if res.get("skipped"):
        L.append("\nSkipped: " + json.dumps(res["skipped"]))
    if e1:
        L.append(f"\n## E1 reply dose-response\nbeta={e1['e1']['beta']:.4f} (p={e1['e1']['p']:.3g}); "
                 f"placebo beta={e1['placebo']['beta']:.4f}; Gate A pass: {e1['gate_a_pass']}")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--obs", required=True); ap.add_argument("--scores", required=True)
    ap.add_argument("--threads"); ap.add_argument("--out", required=True)
    ap.add_argument("--scores-plain", help="scores.csv from the PLAIN scorer: runs the same battery for the ablation (twin on plain vs on StressTwin-F)")
    ap.add_argument("--pilot", choices=["only", "exclude"], help="'only': run on the pilot slice (authors whose hash starts with 0 or 1, ~12.5%%), used to fix design choices; "
                    "'exclude': confirmatory run on all OTHER authors. A confirmatory result must use 'exclude' (or no pilot was ever looked at).")
    ap.add_argument("--min-authors", type=int, default=40)
    ap.add_argument("--min-obs", type=int, default=5); ap.add_argument("--min-days", type=float, default=14.0)
    ap.add_argument("--seed", type=int, default=0, help="author-partition seed; repeat with several seeds for the robustness table")
    ap.add_argument("--max-train-authors", type=int, default=1500)
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    obs0 = pd.read_csv(a.obs)
    if a.pilot:
        in_pilot = obs0.author.astype(str).str[0].isin(list("01"))
        obs0 = obs0[in_pilot if a.pilot == "only" else ~in_pilot]
    df = assemble(obs0, pd.read_csv(a.scores))
    res, rec = loco.run_loco(df, min_obs=a.min_obs, min_days=a.min_days, seed=a.seed, min_authors=a.min_authors, max_train_authors=a.max_train_authors, variants=VARIANTS)
    e1 = None
    if a.threads:
        ts = loco.thread_states(df, pd.read_csv(a.threads))
        e1 = events.e1_dose_response(ts) if len(ts) else None
    res["e1"] = e1
    res["settings"]["pilot"] = a.pilot
    res["settings"]["multi_community_authors"] = df.attrs.get("multi_community_authors")
    res["settings"]["obs_dropped_multi_community"] = df.attrs.get("obs_dropped_multi_community")
    (out / "results.json").write_text(json.dumps(res, indent=1, default=float))
    rec.to_csv(out / "records.csv.gz", index=False)
    (out / "report.md").write_text(report(res, e1, rec))
    if a.scores_plain:
        dp = assemble(obs0, pd.read_csv(a.scores_plain))
        resp, recp = loco.run_loco(dp, min_obs=a.min_obs, min_days=a.min_days, seed=a.seed, min_authors=a.min_authors, max_train_authors=a.max_train_authors, variants=VARIANTS)
        e1p = None
        if a.threads:
            tsp = loco.thread_states(dp, pd.read_csv(a.threads))
            e1p = events.e1_dose_response(tsp) if len(tsp) else None
        resp["e1"] = e1p
        (out / "results_plain.json").write_text(json.dumps(resp, indent=1, default=float))
        (out / "report_plain.md").write_text(report(resp, e1p, recp))
        # Scales differ between scorers, so compare on scale-free quantities only: Gaussian/conformal coverage,
        # and the E1 sign and placebo. Do NOT compare raw MSE between the two scorers.
    print((out / "report.md").read_text())


if __name__ == "__main__":
    main()
