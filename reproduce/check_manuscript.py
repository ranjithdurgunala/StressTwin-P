"""Check that the numeric tables (1-7) of the manuscript equal the values recomputed from the result files.

    python reproduce/check_manuscript.py path/to/manuscript.docx

Reads results/values.json (written by reproduce/compute_values.py), results/funnel.json (written by
reproduce/funnel_counts.py) and results/seed*/results.json, and compares Tables 1-7 and 9-11 cell by cell.
"""
import json, statistics as st, sys
from pathlib import Path
from docx import Document

R = Path(__file__).resolve().parents[1] / "results"
V = json.load(open(R / "values.json"))["seeds"]
F = json.load(open(R / "funnel.json"))
C = ["anxiety", "bipolar", "depression", "suicidewatch"]
CN = {c: c.capitalize() for c in C}
M = "−"
sg = lambda x: (M if x < 0 else "+") + f"{abs(x):.3f}"
n0 = lambda x: f"{x:,}"
paired = lambda k, c: [s["comm"][c]["paired"][k]["diff"] for s in V]
cov = lambda m, c, key="coverage": [s["comm"][c]["conf_across"][m][key] for s in V]

def expected():
    A, o, p, sc, one = F["cohort_A"], F["own_narrative"], F["after_pilot"], F["scored"], F["one_community"]
    t1 = [["Step", "Observations", "Authors"],
          ["Own-narrative observations", n0(o["observations"]), n0(o["authors"])],
          ["Pilot slice removed", n0(p["observations"]), n0(p["authors"])],
          ["Scored (authors with ≥ 2 observations)", n0(sc["observations"]), n0(sc["authors"])],
          ["One community per author", n0(one["observations"]), n0(one["authors"])],
          ["Eligible: ≥ 5 observations over ≥ 14 days (cohort A)", n0(A["observations"]), n0(A["authors"])]]
    s0 = V[0]["comm"]
    t2 = [["Community", "Eligible", "Train used", "Test", "Test predictions"]]
    for c in C:
        t2.append([CN[c], n0(A["by_community_authors"][c]), n0(s0[c]["n_train"]), n0(s0[c]["n_test"]), n0(s0[c]["n_pred"])])
    t2.append(["Total", n0(A["authors"]), n0(sum(s0[c]["n_train"] for c in C)), n0(sum(s0[c]["n_test"] for c in C)), n0(sum(s0[c]["n_pred"] for c in C))])
    lab = [("Author mean", "author_mean"), ("EWMA", "ewma"), ("Gap-weighted EWMA", "gap_ewma"), ("Global mean (H1b)", "global_mean"),
           ("Static twin (H1b)", "twin[split_half/static]"), ("No-pooling twin", "twin[split_half/nopool]"), ("Shortcut (H1)", "shortcut")]
    t3 = [["Comparator"] + [CN[c] for c in C]]
    for n, k in lab:
        t3.append([n] + [f"{sg(st.mean(paired(k, c)))} ({st.stdev(paired(k, c)):.3f})" for c in C])
    t4cov = [["Method"] + [CN[c] for c in C]]
    for n, k in (("Gaussian", "gaussian"), ("Static conformal", "static_conformal"), ("Adaptive conformal", "aci")):
        t4cov.append([n] + [f"{st.mean(cov(k, c)):.3f} ({st.mean(cov(k, c, 'mean_width')):.2f})" for c in C])
    # Table 4: seed-0 estimate, 95% and Bonferroni intervals
    t4 = [["Comparator"] + [CN[c] for c in C]]
    for n, k in (("Author mean", "author_mean"), ("EWMA", "ewma"), ("Global mean", "global_mean"), ("Static twin", "twin[split_half/static]"),
                 ("No-pooling twin", "twin[split_half/nopool]"), ("Shortcut", "shortcut")):
        row = [n]
        for c in C:
            x = V[0]["comm"][c]["paired"][k]
            ng = lambda v: (M if v < 0 else "") + f"{abs(v):.3f}"
            row.append(f"{sg(x['diff'])}\n[{ng(x['ci95'][0])}, {ng(x['ci95'][1])}]\n[{ng(x['ci_bonf'][0])}, {ng(x['ci_bonf'][1])}]")
        t4.append(row)
    # Table 5: fitted parameters (within-community, mean over seeds)
    RES = [json.load(open(R / f"seed{i}" / "results.json"))["communities"] for i in range(5)]
    fit = lambda c, k: st.mean(r[c]["within"]["fits"]["split_half"][k] for r in RES)
    nm = lambda c, k: st.mean(r[c]["within"]["noise_model"][k] for r in RES)
    t5 = [["Community", "\u03c4", "\u03c3", "s", "a0", "a1", "a2"]]
    for c in C:
        t5.append([CN[c], f"{fit(c,'tau'):.2f}", f"{fit(c,'sigma'):.2f}", f"{fit(c,'noise_scale'):.2f}", f"{nm(c,'a0'):.2f}", f"{nm(c,'a1'):.0f}", f"{nm(c,'a2'):.2f}"])
    # Table 7: Gaussian / static conformal coverage by gap (from diagnostics.json)
    DG = json.load(open(R / "diagnostics.json"))["seeds"]
    gd = lambda c, g, k: st.mean(x["comm"][c]["across"]["gap"][g][k] for x in DG)
    t7 = [["Community", "\u2264 1 day", "1\u20137 days", "> 7 days"]]
    for c in C:
        t7.append([CN[c]] + [f"{gd(c,g,'gaussian_cov'):.3f} / {gd(c,g,'static_cov'):.3f}\n(n = {gd(c,g,'n'):,.0f})" for g in ("<=1d", "1-7d", ">7d")])
    # Table 9: variance validity by noise arm
    ng = lambda v: (M if v < 0 else "") + f"{abs(v):.2f}"
    dv = lambda m, k: [x["comm"][c]["across"]["variance"][m][k] for x in DG for c in C]
    dc = lambda m, k: st.mean(x["comm"][c]["across"]["calibration"][m][k] for x in DG for c in C)
    cl = lambda m, l: st.mean(x["comm"][c]["across"]["calibration"][m]["coverage"][l] for x in DG for c in C)
    t9 = [["Noise arm", "Spearman", "Mean z\u00b2", "Cov. 80%", "Cov. 90%", "Cov. 95%"]]
    for n, m in (("Fixed", "twin[fixed]"), ("Confidence rule", "twin[conf_rule]"), ("Split-half", "twin[split_half]")):
        sp = dv(m, "spearman")
        t9.append([n, f"{ng(st.mean(sp))} [{ng(min(sp))}, {ng(max(sp))}]", f"{dc(m,'z2_mean'):.3f}", f"{cl(m,'0.8'):.3f}", f"{cl(m,'0.9'):.3f}", f"{cl(m,'0.95'):.3f}"])
    # Table 10: first/second half, within-community
    t10 = [["Community", "Half", "Author mean", "EWMA", "Global mean", "Shortcut"]]
    for c in C:
        for h in ("first", "second"):
            t10.append([CN[c], h.capitalize()] + [sg(st.mean(x["comm"][c]["within"]["halves"][h][f"twin_minus_{b}"] for x in DG)) for b in ("author_mean", "ewma", "global_mean", "shortcut")])
    # Table 11: exploratory learned baselines (results/learned_baselines.json)
    LB = json.load(open(R / "learned_baselines.json"))["seeds"]
    t11 = [["Community", "Ridge + gap", "GBM + gap", "Ridge history", "GBM history"]]
    for c in C:
        row = [CN[c]]
        for m in ("ridge", "gbm", "ridge_nogap", "gbm_nogap"):
            d = st.mean(s[c][m]["twin_minus_model"] for s in LB)
            k = sum(1 for s in LB if s[c][m]["ci95"][0] > 0 or s[c][m]["ci95"][1] < 0)
            row.append(f"{sg(d)} ({k}/5)")
        t11.append(row)
    return [t1, t2, t3, t4, t5, t4cov, t7, None, t9, t10, t11]

def main(path):
    doc = Document(path)
    got = [[[c.text.strip() for c in r.cells] for r in t.rows] for t in doc.tables[:11]]
    bad = 0
    for i, (g, e) in enumerate(zip(got, expected()), 1):
        if e is None:   # Table 8 (hypotheses) is text, not recomputed
            continue
        for r, (gr, er) in enumerate(zip(g, e)):
            for c, (gc, ec) in enumerate(zip(gr, er)):
                if gc != ec:
                    bad += 1; print(f"Table {i} row {r} col {c}: manuscript '{gc}' != recomputed '{ec}'")
        if len(g) != len(e):
            bad += 1; print(f"Table {i}: row count {len(g)} != {len(e)}")
    print("OK: Tables 1-7 and 9-11 match the recomputed values" if not bad else f"{bad} mismatches")
    return bad

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
