"""Draw the manuscript figures from values.json (output of compute_values.py).

    python reproduce/make_figures.py --values values.json --out figures/
"""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402
import numpy as np  # noqa: E402

COMMS = ["anxiety", "bipolar", "depression", "suicidewatch"]
LAB = {"anxiety": "Anxiety", "bipolar": "Bipolar", "depression": "Depression", "suicidewatch": "Suicidewatch"}
TWIN = "twin[split_half]"
plt.rcParams.update({"font.family": "serif", "font.serif": ["Times New Roman", "Liberation Serif", "DejaVu Serif"],
                     "font.size": 8, "axes.linewidth": 0.6, "pdf.fonttype": 42, "ps.fonttype": 42, "mathtext.fontset": "stix"})
COL = {"gauss": "#1f4e79", "static": "#b45f06", "aci": "#38761d"}


def fig_architecture(out: Path):
    fig, ax = plt.subplots(figsize=(3.45, 5.3))
    ax.set_xlim(0, 10); ax.set_ylim(0, 17.2); ax.axis("off")
    boxes = [
        ("L0  Timelines", "Reddit, 4 communities, 2017\nown posts and own-thread comments\nhashed author IDs; eligible authors:\nat least 5 observations over at least 14 days", "#dbe9f4"),
        ("L1  Scorer", "RoBERTa-base ensemble (5 seeds)\nmean logit y, seed variance v,\nhalf-text logits z1, z2", "#e8dff0"),
        ("L2  Observation noise", "R = a$_0$ + a$_1$/n + a$_2$v\nfitted without labels by\nnon-negative least squares", "#e8dff0"),
        ("L3  Person-level state", "x$_i$(t) = m$_i$ + u$_i$(t);  m$_i$ ~ N(μ, τ$^2$)\nOU fluctuation u$_i$; partial pooling\nexact marginal likelihood; Kalman filter", "#d9efe8"),
        ("L4  Intervals", "Gaussian, static conformal,\nadaptive conformal; 90% nominal", "#fbe9cc"),
        ("L5  Evaluation", "author-disjoint leave-one-community-out\nbaselines and pre-specified shortcut\nauthor-cluster bootstrap, 5 seeds", "#f6dcd6"),
    ]
    h = [2.9, 2.2, 2.0, 2.5, 1.8, 2.3]
    y = 16.9
    for (t, b, c), hh in zip(boxes, h):
        y0 = y - hh
        ax.add_patch(FancyBboxPatch((0.4, y0), 9.2, hh, boxstyle="round,pad=0.02,rounding_size=0.25", fc=c, ec="#333333", lw=0.7))
        ax.text(5, y - 0.42, t, ha="center", va="center", fontsize=8.4, fontweight="bold")
        ax.text(5, y0 + (hh - 0.8) / 2, b, ha="center", va="center", fontsize=6.9, linespacing=1.35)
        if y0 > 1.5:
            ax.annotate("", xy=(5, y0 - 0.58), xytext=(5, y0 - 0.03), arrowprops=dict(arrowstyle="-|>", lw=0.9, color="#333333", mutation_scale=9))
        y = y0 - 0.6
    fig.savefig(out / "fig1_architecture.png", dpi=300, bbox_inches="tight"); fig.savefig(out / "fig1_architecture.pdf", bbox_inches="tight"); plt.close(fig)


def fig_coverage(V, out: Path):
    fig, ax = plt.subplots(figsize=(3.45, 2.5))
    keys = [("gauss", "gaussian", "Gaussian"), ("static", "static_conformal", "Static conformal"), ("aci", "aci", "Adaptive conformal")]
    x = np.arange(len(COMMS))
    for j, (c, k, lab) in enumerate(keys):
        m = [np.mean([s["comm"][cm]["conf_across"][k]["coverage"] for s in V]) for cm in COMMS]
        lo = [min(s["comm"][cm]["conf_across"][k]["coverage"] for s in V) for cm in COMMS]
        hi = [max(s["comm"][cm]["conf_across"][k]["coverage"] for s in V) for cm in COMMS]
        ax.errorbar(x + (j - 1) * 0.2, m, yerr=[np.array(m) - lo, np.array(hi) - m], fmt="o", ms=3.5, capsize=2, lw=0.8, color=COL[c], label=lab)
    ax.axhline(0.90, color="#444444", lw=0.7, ls="--")
    ax.set_xticks(x); ax.set_xticklabels([LAB[c] for c in COMMS], fontsize=7)
    ax.set_ylabel("Coverage (nominal 0.90)"); ax.set_ylim(0.86, 0.93)
    ax.legend(fontsize=6.5, frameon=False, loc="lower right", ncol=1)
    fig.savefig(out / "fig3_coverage.png", dpi=300, bbox_inches="tight"); fig.savefig(out / "fig3_coverage.pdf", bbox_inches="tight"); plt.close(fig)


def fig_diffs(V, out: Path):
    comps = [("author_mean", "Author mean"), ("ewma", "EWMA"), ("gap_ewma", "Gap-weighted EWMA"), ("global_mean", "Global mean"),
             ("twin[split_half/static]", "Static twin"), ("twin[split_half/nopool]", "No-pooling twin"), ("shortcut", "Shortcut (target-available)")]
    fig, ax = plt.subplots(figsize=(3.45, 3.0))
    cols = ["#1f4e79", "#b45f06", "#38761d", "#7f2a7f"]
    for j, c in enumerate(COMMS):
        for i, (b, lab) in enumerate(comps):
            d = np.array([s["comm"][c]["paired"][b]["diff"] for s in V])
            ax.errorbar(d.mean(), i + (j - 1.5) * 0.15, xerr=d.std(ddof=1), fmt="o", ms=3, lw=0.7, capsize=1.5, color=cols[j], label=LAB[c] if i == 0 else None)
    ax.axvline(0, color="#444444", lw=0.7)
    ax.set_yticks(range(len(comps))); ax.set_yticklabels([l for _, l in comps], fontsize=6.8)
    ax.invert_yaxis(); ax.set_xlabel("NLL difference, twin minus comparator (nats)")
    ax.legend(fontsize=6.3, frameon=False, loc="upper center", bbox_to_anchor=(0.45, -0.17), ncol=4, columnspacing=0.8, handletextpad=0.2)
    fig.savefig(out / "fig2_nll_differences.png", dpi=300, bbox_inches="tight"); fig.savefig(out / "fig2_nll_differences.pdf", bbox_inches="tight"); plt.close(fig)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--values", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args(); out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    V = json.loads(Path(a.values).read_text())["seeds"]
    fig_architecture(out); fig_coverage(V, out); fig_diffs(V, out)
    print("figures written to", out)


if __name__ == "__main__":
    main()
