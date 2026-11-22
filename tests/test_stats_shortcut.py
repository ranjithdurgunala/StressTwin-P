import numpy as np
import pytest
from stresstwin_p import loco as L, stats as ST, synthetic as S


@pytest.fixture(scope="module")
def run():
    df = S.simulate_obs({"c0": 90, "c1": 90, "c2": 90}, seed=21, horizon_days=200)
    res, rec = L.run_loco(df, min_authors=30, seed=2, fit_kwargs=dict(max_authors=150, max_obs=60))
    return df, res, rec


def test_shortcut_baseline_is_reported_and_causal(run):
    _, res, rec = run
    assert "shortcut" in res["communities"]["c0"]["within"]["summary"]
    assert (rec[rec.model == "shortcut"].i >= 1).all()


def test_shortcut_catches_a_length_artefact():
    df = S.simulate_obs({"c0": 80, "c1": 80}, seed=5, horizon_days=200)
    df["y"] = df["y"] + 0.8 * np.log1p(df["n_chars"])        # planted style artefact unrelated to stress
    res, _ = L.run_loco(df, min_authors=30, seed=1, fit_kwargs=dict(max_authors=100, max_obs=50))
    s = res["communities"]["c0"]["within"]["summary"]
    assert s["shortcut"]["mse"] < s["author_mean"]["mse"]


def test_paired_bootstrap_detects_real_gap_and_zero_for_identical(run):
    _, res, rec = run
    d = ST.paired_diff(rec, "twin[split_half]", "author_mean", "se", community="c0")
    assert d["n_authors"] > 20 and d["diff"] < 0 and d["excludes_zero"]
    z = ST.paired_diff(rec, "author_mean", "author_mean", "se", community="c0")
    assert z["diff"] == 0.0 and not z["excludes_zero"]
    p = ST.precision(rec, "twin[split_half]", "author_mean", "nll", community="c0")
    assert p["min_detectable_diff_80pct_power"] > 0 and p["ci95"][0] <= p["diff"] <= p["ci95"][1]
    with pytest.raises(ValueError):
        ST.paired_diff(rec, "twin[split_half]", "author_mean", "bogus")


def test_ci_level_widens_interval(run):
    _, _, rec = run
    a = ST.paired_diff(rec, "twin[split_half]", "author_mean", "se", community="c0", ci_level=0.95)
    b = ST.paired_diff(rec, "twin[split_half]", "author_mean", "se", community="c0", ci_level=0.995)
    assert (b["ci95"][1] - b["ci95"][0]) > (a["ci95"][1] - a["ci95"][0]) and b["ci_level"] == 0.995
