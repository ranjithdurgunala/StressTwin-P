"""Leave-one-community-out (LOCO) evaluation: RQ0 (noise arms), RQ2 (value over history),
RQ3 (coverage under shift) and the absolute-sensitivity statistic (the pre-registered H1 amendment).

Input table (one row per observation), columns:
    author, community, t_days, y (scorer logit), ens_var, n_chars, [za, zb, n_half], [obs_id, kind]

Protocol, per held-out community c with enough eligible authors:
  1. Split c's eligible authors, author-disjoint, into A (train-within) and B (test).
  2. 'within'  : fit everything on A.
     'across'  : fit everything on the SAME NUMBER of authors drawn from the other communities.
     Both are scored on B. Matching the training size is essential: without it, 'across' has
     more data and the comparison measures sample size, not community shift.
  3. Score one-step-ahead prediction of each author's next observation (i >= 1), causally.
  4. Sensitivity of a model = |score_across - score_within|. Models that use no training
     data (author_mean, last) must show exactly 0 MSE degradation; that is a built-in check
     that the harness measures training-source effects and nothing else.

What is predicted is the next OBSERVED SCORE (a measurement), so RQ2 is partly self-referential.
Do not present it as accuracy against true stress.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import baselines as B
from . import conformal as C
from . import noise as N
from . import ou_filter as O


# ---------------------------------------------------------------- helpers
def single_community(df: pd.DataFrame) -> pd.DataFrame:
    """Give every author exactly one community: the one where they have most observations (ties: the community of their
    earliest observation). Their observations elsewhere are dropped.

    Why: in Zenodo 4266616 about 8% of authors post in more than one community. Leave-one-community-out is only
    author-disjoint if no person is in both the held-out community and the training data. Dropping the minority-community
    observations is the simplest rule that guarantees it; the number dropped is stored in df.attrs and must be reported."""
    cnt = df.groupby(["author", "community"]).agg(n=("t_days", "size"), first=("t_days", "min")).reset_index()
    cnt = cnt.sort_values(["author", "n", "first"], ascending=[True, False, True])
    home = cnt.drop_duplicates("author").set_index("author")["community"]
    keep = df["community"].values == df["author"].map(home).values
    out = df[keep].copy()
    out.attrs.update(df.attrs)
    out.attrs["multi_community_authors"] = int((cnt.groupby("author").size() > 1).sum())
    out.attrs["obs_dropped_multi_community"] = int((~keep).sum())
    return out


def eligible(df: pd.DataFrame, min_obs: int = 5, min_days: float = 14.0) -> list:
    g = df.groupby("author")["t_days"].agg(["count", "min", "max"])
    ok = g[(g["count"] >= min_obs) & ((g["max"] - g["min"]) >= min_days)]
    return ok.index.tolist()


def _timelines(df: pd.DataFrame, rcol: str):
    out = []
    for a, g in df.sort_values(["author", "t_days"]).groupby("author", sort=False):
        out.append(O.Timeline(str(a), g["t_days"].to_numpy(), g["y"].to_numpy(), g[rcol].to_numpy()))
    return out


def _add_noise(df: pd.DataFrame, arm: str, model) -> pd.DataFrame:
    d = df.copy()
    d["R"] = N.noise_for_arm(arm, d["y"].to_numpy(), d["n_chars"].to_numpy(), d["ens_var"].to_numpy(), model)
    return d


def _records(tls, preds: dict, model: str) -> pd.DataFrame:
    rows = []
    for tl in tls:
        pm, pv = preds[tl.author]
        for i in range(1, len(tl)):
            if np.isnan(pm[i]):
                continue
            rows.append((model, tl.author, i, len(tl), tl.t[i], tl.t[i] - tl.t[i - 1], tl.y[i], pm[i], pv[i]))
    return pd.DataFrame(rows, columns=["model", "author", "i", "n_obs", "t", "gap_days", "y", "pred", "var"])


def _summ(r: pd.DataFrame, alpha: float) -> dict:
    if len(r) == 0:
        return {"n": 0}
    se = (r.y - r.pred) ** 2
    ls = B.gaussian_logscore(r.y.to_numpy(), r.pred.to_numpy(), r["var"].to_numpy())
    sd = np.sqrt(np.maximum(r["var"].to_numpy(), 1e-12))
    from scipy.stats import norm
    z = norm.ppf(1 - alpha / 2)
    return {"n": int(len(r)), "mse": float(se.mean()), "nll": float(-ls.mean()),
            "gauss_cov": float(np.mean(np.abs(r.y - r.pred) <= z * sd)),
            "gauss_width": float(np.mean(2 * z * sd))}


# ---------------------------------------------------------------- one train/test condition
# State-dynamics ablations, all run with the measured (split_half) noise so only the dynamics change:
#   static  : no fluctuation (sigma ~ 0)  -> shrunken personal baseline, i.e. the twin without dynamics
#   rw      : kappa ~ 0                   -> near random walk, i.e. no mean reversion
#   nopool  : tau large                   -> no partial pooling of personal baselines across authors
VARIANTS = {"static": {"sigma": 1e-3}, "rw": {"kappa": 1e-4}, "nopool": {"tau": 100.0}}


def evaluate_condition(train: pd.DataFrame, test: pd.DataFrame, arms=N.ARMS, alpha: float = 0.10,
                       fit_kwargs: dict | None = None, variants=()) -> dict:
    fit_kwargs = fit_kwargs or {}
    recs, summaries, fits, conf = [], {}, {}, {}
    half = train.dropna(subset=["za", "zb"]) if {"za", "zb"} <= set(train.columns) else train.iloc[0:0]
    sh_model = None
    if len(half) >= 30:
        sh_model = N.fit_split_half(half["za"], half["zb"], half["n_half"], half["ens_var"])

    pairs = [(arm, "ou") for arm in arms] + [("split_half", v) for v in variants]
    for arm, var_name in pairs:
        if arm == "split_half" and sh_model is None:
            summaries[f"twin[{arm}]"] = {"skipped": "fewer than 30 split-half pairs in training data"}
            continue
        tr, te = _add_noise(train, arm, sh_model), _add_noise(test, arm, sh_model)
        tr_tl, te_tl = _timelines(tr, "R"), _timelines(te, "R")
        fit = O.fit_ou(tr_tl, **{**fit_kwargs, **({"fixed": VARIANTS[var_name]} if var_name != "ou" else {})})
        label = arm if var_name == "ou" else f"{arm}/{var_name}"
        fits[label] = {"kappa": fit.params.kappa, "sigma": fit.params.sigma, "tau": fit.params.tau,
                     "mu": fit.params.mu, "noise_scale": fit.params.noise_scale,
                     "converged": fit.converged, "at_bound": fit.at_bound,
                     "n_train_authors": fit.n_authors}
        f_te = {tl.author: O.kalman_filter(tl, fit.params) for tl in te_tl}
        f_tr = {tl.author: O.kalman_filter(tl, fit.params) for tl in tr_tl}
        name = f"twin[{label}]"
        r = _records(te_tl, {a: (f.pred_mean, f.pred_var) for a, f in f_te.items()}, name)
        rtr = _records(tr_tl, {a: (f.pred_mean, f.pred_var) for a, f in f_tr.items()}, name)
        recs.append(r)
        summaries[name] = _summ(r, alpha)
        if len(r) and len(rtr):
            cal = C.scores(rtr.y, rtr.pred, rtr["var"])
            r2 = r.sort_values("t")
            conf[name] = {
                "gaussian": C.eval_gaussian(r2.y.to_numpy(), r2.pred.to_numpy(), r2["var"].to_numpy(), alpha),
                "static_conformal": C.eval_static(r2.y.to_numpy(), r2.pred.to_numpy(), r2["var"].to_numpy(), cal, alpha),
                "aci": C.eval_aci(r2.y.to_numpy(), r2.pred.to_numpy(), r2["var"].to_numpy(), cal, alpha)}

    # baselines on the raw scorer logit
    te_tl = _timelines(test.assign(R=1.0), "R")
    tr_tl = _timelines(train.assign(R=1.0), "R")
    a_star = B.tune_ewma(tr_tl)
    h_star = B.tune_gap_ewma(tr_tl)
    gmean = float(np.mean(np.concatenate([tl.y for tl in tr_tl])))
    fns = {
        "author_mean": B.predict_author_mean,
        "last": B.predict_last,
        "ewma": lambda t, y: B.predict_ewma(t, y, a_star),
        "gap_ewma": lambda t, y: B.predict_gap_ewma(t, y, h_star),
        "global_mean": lambda t, y: B.predict_global_mean(t, y, gmean),
    }
    for name, fn in fns.items():
        var = B.residual_variance(tr_tl, fn)
        preds = {tl.author: (fn(tl.t, tl.y), np.full(len(tl), var)) for tl in te_tl}
        r = _records(te_tl, preds, name)
        recs.append(r)
        summaries[name] = _summ(r, alpha)
    # shortcut baseline: author running mean + (length, gap, activity) only. A twin that cannot beat this is not
    # showing anything beyond style / posting behaviour.
    def _tn(df):
        return [(g["t_days"].to_numpy(), g["y"].to_numpy(), g["n_chars"].to_numpy(), str(a))
                for a, g in df.sort_values(["author", "t_days"]).groupby("author", sort=False)]
    coef = B.fit_shortcut([(t, y, n) for t, y, n, _ in _tn(train)])
    def predict_sc(tup):
        t, y, n, _ = tup
        return B.predict_shortcut(t, y, n, coef)
    tr_res = np.concatenate([(y - predict_sc((t, y, n, a)))[1:] for t, y, n, a in _tn(train) if len(y) > 1] or [np.array([1.0])])
    sc_var = float(np.mean(tr_res ** 2))
    te_by = {a: (t, y, n) for t, y, n, a in _tn(test)}
    preds = {tl.author: (B.predict_shortcut(*[te_by[tl.author][0], te_by[tl.author][1], te_by[tl.author][2]], coef),
                         np.full(len(tl), sc_var)) for tl in te_tl}
    r = _records(te_tl, preds, "shortcut")
    recs.append(r)
    summaries["shortcut"] = _summ(r, alpha)
    return {"summary": summaries, "fits": fits, "conformal": conf, "tuned": {"ewma_alpha": a_star, "gap_ewma_halflife_days": h_star},
            "noise_model": None if sh_model is None else vars(sh_model),
            "records": pd.concat(recs, ignore_index=True) if recs else pd.DataFrame()}


# ---------------------------------------------------------------- LOCO driver
def run_loco(df: pd.DataFrame, min_obs: int = 5, min_days: float = 14.0, min_authors: int = 40,
             max_train_authors: int = 1500, alpha: float = 0.10, seed: int = 0, arms=N.ARMS,
             fit_kwargs: dict | None = None, variants=()) -> dict:
    rng = np.random.default_rng(seed)
    elig = set(eligible(df, min_obs, min_days))
    d = df[df.author.isin(elig)]
    comms = sorted(d.community.unique())
    out = {"settings": dict(min_obs=min_obs, min_days=min_days, min_authors=min_authors, alpha=alpha, seed=seed,
                            max_train_authors=max_train_authors),
           "eligible_authors": {c: int(d[d.community == c].author.nunique()) for c in comms},
           "communities": {}, "skipped": {}}
    all_rec = []
    for c in comms:
        a_c = np.array(sorted(d[d.community == c].author.unique()))
        a_other = np.array(sorted(d[d.community != c].author.unique()))
        if len(a_c) < min_authors:
            out["skipped"][c] = f"only {len(a_c)} eligible authors (< {min_authors})"; continue
        perm = rng.permutation(a_c)
        A, Bt = perm[: len(perm) // 2], perm[len(perm) // 2:]
        n_train = min(len(A), max_train_authors, len(a_other))
        if n_train < 20:
            out["skipped"][c] = f"only {n_train} matched training authors"; continue
        within_ids = rng.permutation(A)[:n_train]
        across_ids = rng.permutation(a_other)[:n_train]
        test = d[d.author.isin(Bt)]
        res = {}
        for cond, ids in (("within", within_ids), ("across", across_ids)):
            res[cond] = evaluate_condition(d[d.author.isin(ids)], test, arms, alpha, fit_kwargs, variants)
        sens = {}
        for m in res["within"]["summary"]:
            sw, sa = res["within"]["summary"][m], res["across"]["summary"].get(m, {})
            if "mse" in sw and "mse" in sa:
                sens[m] = {"mse_degradation": sa["mse"] - sw["mse"], "nll_degradation": sa["nll"] - sw["nll"],
                           "abs_mse": abs(sa["mse"] - sw["mse"]), "abs_nll": abs(sa["nll"] - sw["nll"])}
        out["communities"][c] = {
            "n_train_authors": int(n_train), "n_test_authors": int(len(Bt)),
            "within": {k: v for k, v in res["within"].items() if k != "records"},
            "across": {k: v for k, v in res["across"].items() if k != "records"},
            "sensitivity": sens}
        for cond in ("within", "across"):
            r = res[cond]["records"].copy(); r["community"] = c; r["condition"] = cond; all_rec.append(r)

    # pooled sensitivity: mean absolute degradation across held-out communities (pre-registered statistic)
    pooled = {}
    models = set().union(*[set(v["sensitivity"]) for v in out["communities"].values()]) if out["communities"] else set()
    for m in sorted(models):
        vals = [v["sensitivity"][m] for v in out["communities"].values() if m in v["sensitivity"]]
        pooled[m] = {"mean_abs_nll_degradation": float(np.mean([x["abs_nll"] for x in vals])),
                     "mean_abs_mse_degradation": float(np.mean([x["abs_mse"] for x in vals])),
                     "n_communities": len(vals)}
    ref = next((k for k in pooled if k.startswith("twin[split_half]")), None) or next((k for k in pooled if k.startswith("twin[")), None)
    if ref and pooled[ref]["mean_abs_nll_degradation"] > 0:
        for m in pooled:
            pooled[m]["nll_sensitivity_ratio_vs_" + ref] = pooled[m]["mean_abs_nll_degradation"] / pooled[ref]["mean_abs_nll_degradation"]
    out["pooled_sensitivity"] = pooled
    records = pd.concat(all_rec, ignore_index=True) if all_rec else pd.DataFrame()
    out["strata"] = strata(records) if len(records) else {}
    return out, records


def strata(records: pd.DataFrame) -> dict:
    """MSE of twin vs the strongest baselines, by timeline length and by gap since previous post.
    Descriptive only (length buckets use the author's total count)."""
    r = records[records.condition == "within"].copy()
    r["se"] = (r.y - r.pred) ** 2
    r["len_bucket"] = pd.cut(r.n_obs, [0, 9, 19, 10 ** 6], labels=["5-9", "10-19", "20+"])
    r["gap_bucket"] = pd.cut(r.gap_days, [-1e-9, 1, 7, 1e9], labels=["<=1d", "1-7d", ">7d"])
    out = {}
    for key in ("len_bucket", "gap_bucket"):
        g = r.groupby([key, "model"], observed=True)["se"].agg(mse="mean", n="count").reset_index()
        out[key] = {str(k): {row.model: {"mse": float(row.mse), "n": int(row.n)}
                             for row in g[g[key] == k].itertuples()} for k in g[key].unique()}
    return out


# ---------------------------------------------------------------- thread states for E1
def thread_states(df: pd.DataFrame, threads: pd.DataFrame, arm: str = "split_half", min_obs: int = 5,
                  min_days: float = 14.0, fit_kwargs: dict | None = None) -> pd.DataFrame:
    """Fit the twin on eligible authors (pooled; E1 is not a transfer test), filter ALL authors in
    `threads` causally, and attach the filtered level at the opening post and at the later comment."""
    elig = df[df.author.isin(eligible(df, min_obs, min_days))]
    half = elig.dropna(subset=["za", "zb"]) if "za" in elig else elig.iloc[0:0]
    model = N.fit_split_half(half["za"], half["zb"], half["n_half"], half["ens_var"]) if len(half) >= 30 else None
    if arm == "split_half" and model is None:
        raise ValueError("split_half arm needs >= 30 split-half pairs among eligible authors")
    fit = O.fit_ou(_timelines(_add_noise(elig, arm, model), "R"), **(fit_kwargs or {}))
    need = df[df.author.isin(threads.author.unique())]
    tls = _timelines(_add_noise(need, arm, model), "R")
    ids = need.sort_values(["author", "t_days"]).groupby("author", sort=False)["obs_id"].apply(list).to_dict()
    level = {}
    for tl in tls:
        f = O.kalman_filter(tl, fit.params)
        for oid, m in zip(ids[tl.author], f.filt_mean):
            level[oid] = m
    t = threads.copy()
    t["state_open"] = t.obs_id_open.map(level)
    t["state_after"] = t.obs_id_after.map(level)
    return t.dropna(subset=["state_open", "state_after"])
