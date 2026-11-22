"""Dataset-construction counts (Table 2 of the manuscript) from the observation table.

    python reproduce/funnel_counts.py --obs observations.csv --out funnel.json

The observation table has columns obs_id, author, community, t_days, kind, n_chars (see docs/DATA.md).
Steps follow the manuscript: own-narrative observations -> pilot slice removed -> authors with at least two
observations (the only ones that can be scored) -> one community per author -> eligible (>=5 observations over >=14 days).
"""
import argparse
import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from stresstwin_p import loco  # noqa: E402


def funnel(obs: pd.DataFrame) -> dict:
    out = {"own_narrative": {"observations": int(len(obs)), "authors": int(obs.author.nunique())}}
    out["by_community"] = {
        c: {"observations": int(len(g)), "authors": int(g.author.nunique()),
            "submissions": int((g.kind == "submission").sum()), "own_comments": int((g.kind != "submission").sum()),
            "median_chars": float(g.n_chars.median())}
        for c, g in obs.groupby("community")}
    out["submissions"] = int((obs.kind == "submission").sum())
    out["own_comments"] = int((obs.kind != "submission").sum())
    in_pilot = obs.author.astype(str).str[0].isin(list("01"))
    pilot_authors = int(obs[in_pilot].author.nunique())
    out["pilot"] = {"authors": pilot_authors, "observations": int(in_pilot.sum()),
                    "share_of_authors": pilot_authors / obs.author.nunique()}
    d = obs[~in_pilot]
    out["after_pilot"] = {"observations": int(len(d)), "authors": int(d.author.nunique())}
    cnt = d.groupby("author").size()
    multi = cnt[cnt >= 2].index
    scored = d[d.author.isin(multi)].rename(columns={})
    out["scored"] = {"observations": int(len(scored)), "authors": int(scored.author.nunique()),
                     "single_observation_texts_not_scored": int((cnt == 1).sum())}
    one = loco.single_community(scored.assign(y=0.0))
    out["one_community"] = {"observations": int(len(one)), "authors": int(one.author.nunique()),
                            "multi_community_authors": one.attrs["multi_community_authors"],
                            "observations_dropped": one.attrs["obs_dropped_multi_community"]}
    el = loco.eligible(one)
    A = one[one.author.isin(el)]
    out["cohort_A"] = {"observations": int(len(A)), "authors": int(A.author.nunique()),
                       "submissions": int((A.kind == "submission").sum()), "own_comments": int((A.kind != "submission").sum()),
                       "by_community_authors": {c: int(g.author.nunique()) for c, g in A.groupby("community")}}
    g = A.sort_values(["author", "t_days"]).groupby("author")["t_days"]
    n_per = g.size()
    gaps = A.sort_values(["author", "t_days"]).groupby("author")["t_days"].diff().dropna()
    out["cohort_A"].update({
        "obs_per_author_median": float(n_per.median()), "obs_per_author_q25": float(n_per.quantile(.25)),
        "obs_per_author_q75": float(n_per.quantile(.75)), "obs_per_author_max": int(n_per.max()),
        "span_days_median": float((g.max() - g.min()).median()), "span_days_mean": float((g.max() - g.min()).mean()),
        "gap_days_median": float(gaps.median()), "gap_days_q25": float(gaps.quantile(.25)), "gap_days_q75": float(gaps.quantile(.75)),
        "share_gaps_le_1d": float((gaps <= 1).mean()), "share_gaps_gt_7d": float((gaps > 7).mean()),
        "chars_median": float(A.n_chars.median())})
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--obs", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    res = funnel(pd.read_csv(a.obs))
    Path(a.out).write_text(json.dumps(res, indent=1))
    print(json.dumps(res, indent=1))
