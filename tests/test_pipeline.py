import json
import pickle
import numpy as np
import pandas as pd
import pytest

from stresstwin_p import loco as L
from stresstwin_p import score_texts as ST
from stresstwin_p import synthetic as S
from stresstwin_p import timeline_builder as TB
from stresstwin_p.safe_io import load_pickle

SALT = b"0123456789abcdef0123456789abcdef"


# ---------------------------------------------------------------- timeline builder
def _fixture():
    base = 1_500_000_000
    long_text = "I feel really overwhelmed this week and cannot sleep. " * 3
    posts = {
        "p1": {"id": "p1", "author": "alice", "created_utc": base, "title": "help", "selftext": long_text, "subreddit": "Anxiety"},
        "p2": {"id": "p2", "author": "bob", "created_utc": base + 5000, "title": "hi", "selftext": long_text, "subreddit": "Anxiety"},
        "p3": {"id": "p3", "author": "[deleted]", "created_utc": base, "title": "x", "selftext": long_text, "subreddit": "Anxiety"},
        "p4": {"id": "p4", "author": "carol", "created_utc": base, "title": "x", "selftext": "[removed]", "subreddit": "Anxiety"},
    }
    def c(i, au, dt, thread, text=long_text):
        return {"id": i, "author": au, "created_utc": base + dt, "body": text, "link_id": "t3_" + thread, "subreddit": "Anxiety"}
    comments = {
        "c1": c("c1", "dan", 600, "p1"),                 # reply by someone else, before alice's comment
        "c2": c("c2", "erin", 1200, "p1"),               # another reply before
        "c3": c("c3", "alice", 3600, "p1"),              # alice's own comment (last own) at +1h
        "c4": c("c4", "dan", 7200, "p1"),                # reply AFTER alice's comment
        "c5": c("c5", "alice", 100, "p2"),               # alice commenting on bob's thread: must be excluded
        "c6": c("c6", "bob", 200, "p2", text="ok"),      # too short: excluded
    }
    return posts, comments


def test_builder_applies_own_narrative_rule_hashes_authors_and_counts_replies():
    posts, comments = _fixture()
    obs, txt, thr, stats = TB.build(posts, comments, SALT)
    assert set(obs.obs_id) == {"s:p1", "c:c3", "s:p2"}           # p3 deleted, p4 removed, c5 other thread, c6 short
    assert "alice" not in obs.author.astype(str).str.cat() and "alice" not in txt.text.str.cat()
    assert obs.author.nunique() == 2
    assert len(thr) == 1
    row = thr.iloc[0]
    assert (row.n_replies_before, row.n_replies_after) == (2, 1)
    assert row.hours_since_open == pytest.approx(1.0)
    assert row.obs_id_open == "s:p1" and row.obs_id_after == "c:c3"
    # same salt -> same hash; different salt -> different hash
    obs2, *_ = TB.build(posts, comments, SALT)
    assert (obs.author.values == obs2.author.values).all()
    obs3, *_ = TB.build(posts, comments, b"another-salt-another-salt-xyz")
    assert obs.author.iloc[0] != obs3.author.iloc[0]


def test_builder_links_comments_through_post2comments_when_link_id_is_missing():
    posts, comments = _fixture()
    for v in comments.values():
        v.pop("link_id")
    p2c = {"p1": ["c1", "c2", "c3", "c4"], "p2": ["c5", "c6"]}
    obs, txt, thr, stats = TB.build(posts, comments, SALT, post2comments=p2c)
    assert set(obs.obs_id) == {"s:p1", "c:c3", "s:p2"} and len(thr) == 1


def test_builder_fails_loudly_with_the_keys_it_saw():
    posts, comments = _fixture()
    bad = {k: {kk: vv for kk, vv in v.items() if kk != "author"} for k, v in posts.items()}
    with pytest.raises(TB.SchemaError) as e:
        TB.build(bad, comments, SALT)
    assert "author" in str(e.value) and "Keys seen" in str(e.value)
    for v in comments.values():
        v.pop("link_id")
    with pytest.raises(TB.SchemaError):
        TB.build(posts, comments, SALT)                          # no way to link comments to threads
    with pytest.raises(ValueError):
        TB.build(posts, comments, b"short")


def test_safe_loader_refuses_code_execution(tmp_path):
    import os
    marker = tmp_path / "pwned"
    class Evil:
        def __reduce__(self):
            return (os.system, (f"touch {marker}",))
    f = tmp_path / "evil.pkl"
    pickle.dump({"a": Evil()}, open(f, "wb"))
    with pytest.raises(pickle.UnpicklingError):
        load_pickle(f)
    assert not marker.exists()


# ---------------------------------------------------------------- scoring
def test_split_halves_and_score_table_with_injected_scorers():
    long = " ".join(f"This is sentence number {i} and it has some words in it to be long enough." for i in range(12))
    short = "too short"
    assert ST.split_halves(short) is None
    a, b = ST.split_halves(long)
    assert len(a) >= 200 and len(b) >= 200 and abs(len(a) - len(b)) < 120
    texts = pd.DataFrame({"obs_id": ["a", "b"], "text": [long, short]})
    scorers = [lambda xs, k=k: np.array([len(x) / 100.0 + k for x in xs]) for k in (0.0, 1.0, 2.0)]
    out = ST.score_table(texts, scorers, batch_size=1)
    assert out.loc[0, "z_var"] == pytest.approx(1.0)                  # seeds differ by 0,1,2 -> var 1 (ddof=1)
    assert np.isfinite(out.loc[0, "z_a"]) and np.isnan(out.loc[1, "z_a"])
    assert out.loc[0, "n_chars"] == len(long)
    with pytest.raises(ValueError):
        ST.score_table(texts, [])


# ---------------------------------------------------------------- LOCO end to end on synthetic data
@pytest.fixture(scope="module")
def loco_result():
    df = S.simulate_obs({"c0": 90, "c1": 90, "c2": 90}, seed=11, horizon_days=200,
                        community_bias={"c0": 0.0, "c1": 1.5, "c2": -1.0},
                        community_mu={"c0": 0.0, "c1": 0.8, "c2": -0.5})
    res, rec = L.run_loco(df, min_obs=5, min_days=14, min_authors=30, seed=3,
                          fit_kwargs=dict(max_authors=150, max_obs=60))
    return df, res, rec


def test_loco_runs_and_reports_every_model(loco_result):
    df, res, rec = loco_result
    assert set(res["communities"]) == {"c0", "c1", "c2"}
    s = res["communities"]["c0"]["within"]["summary"]
    for m in ("twin[fixed]", "twin[conf_rule]", "twin[split_half]", "author_mean", "last", "ewma", "gap_ewma", "global_mean"):
        assert m in s and s[m]["n"] > 100
    assert res["communities"]["c0"]["n_train_authors"] > 0
    json.dumps(res, default=float)                                    # serialisable


def test_training_free_models_have_exactly_zero_mse_degradation(loco_result):
    _, res, _ = loco_result
    for c in res["communities"].values():
        assert c["sensitivity"]["author_mean"]["abs_mse"] == 0.0
        assert c["sensitivity"]["last"]["abs_mse"] == 0.0


def test_matched_training_size(loco_result):
    _, res, _ = loco_result
    for c in res["communities"].values():
        w = c["within"]["fits"]["split_half"]["n_train_authors"]
        a = c["across"]["fits"]["split_half"]["n_train_authors"]
        assert w == a


def test_twin_with_split_half_noise_beats_the_running_mean_on_ou_data(loco_result):
    _, res, _ = loco_result
    for c in res["communities"].values():
        s = c["within"]["summary"]
        assert s["twin[split_half]"]["mse"] < s["author_mean"]["mse"]
        assert s["twin[split_half]"]["nll"] < s["author_mean"]["nll"]


def test_recovered_parameters_are_near_truth_and_split_half_noise_is_fitted(loco_result):
    _, res, _ = loco_result
    f = res["communities"]["c0"]["within"]["fits"]["split_half"]
    assert f["sigma"] == pytest.approx(0.8, rel=0.5) and f["tau"] == pytest.approx(0.9, rel=0.5)
    nm = res["communities"]["c0"]["within"]["noise_model"]
    assert nm["a1"] > 5                                               # length effect found (true 60)


def test_strata_and_pooled_sensitivity_present(loco_result):
    _, res, rec = loco_result
    assert set(res["strata"]) == {"len_bucket", "gap_bucket"}
    assert "twin[split_half]" in res["pooled_sensitivity"]
    assert len(rec) > 0


def test_skips_small_communities_instead_of_running_underpowered_tests():
    df = S.simulate_obs({"big": 80, "tiny": 6}, seed=4, horizon_days=200)
    res, _ = L.run_loco(df, min_authors=30, seed=1, fit_kwargs=dict(max_authors=60, max_obs=40))
    assert "tiny" in res["skipped"]
    # 'big' has only 'tiny' as another community -> too few matched training authors -> skipped, with a reason
    assert "big" in res["skipped"] and "matched training" in res["skipped"]["big"]
    assert res["communities"] == {}


def test_thread_states_feed_e1_end_to_end():
    from stresstwin_p import events as E
    df = S.simulate_obs({"c0": 60, "c1": 60}, seed=8, horizon_days=200)
    df["obs_id"] = [f"o{i}" for i in range(len(df))]
    # one thread per author: opening = first obs, comment = last obs; replies unrelated to anything
    rows = []
    rng = np.random.default_rng(0)
    for a, g in df.sort_values("t_days").groupby("author"):
        if len(g) < 3:
            continue
        rows.append(dict(thread_id=a, author=a, community=g.community.iloc[0], obs_id_open=g.obs_id.iloc[0],
                         obs_id_after=g.obs_id.iloc[-1], n_replies_before=int(rng.poisson(3)),
                         n_replies_after=int(rng.poisson(3)), len_open=float(g.n_chars.iloc[0]),
                         hours_since_open=float((g.t_days.iloc[-1] - g.t_days.iloc[0]) * 24)))
    thr = pd.DataFrame(rows)
    ts = L.thread_states(df, thr, fit_kwargs=dict(max_authors=80, max_obs=40))
    assert len(ts) > 50 and {"state_open", "state_after"} <= set(ts.columns)
    r = E.e1_dose_response(ts)
    assert abs(r["e1"]["beta"]) < 0.25                                # unrelated replies -> no effect


def test_run_all_cli_end_to_end(tmp_path):
    import subprocess, sys
    df = S.simulate_obs({"c0": 50, "c1": 50, "c2": 50}, seed=5, horizon_days=200)
    df["obs_id"] = [f"o{i}" for i in range(len(df))]
    df[["obs_id", "author", "community", "t_days", "n_chars"]].assign(kind="submission").to_csv(tmp_path / "o.csv", index=False)
    df.rename(columns={"y": "z_mean", "ens_var": "z_var", "za": "z_a", "zb": "z_b"})[
        ["obs_id", "z_mean", "z_var", "n_chars", "z_a", "z_b", "n_half"]].to_csv(tmp_path / "s.csv", index=False)
    r = subprocess.run([sys.executable, "-m", "stresstwin_p.run_all", "--obs", str(tmp_path / "o.csv"),
                        "--scores", str(tmp_path / "s.csv"), "--out", str(tmp_path / "out"), "--min-authors", "30"],
                       capture_output=True, text=True, cwd=str(__import__("pathlib").Path(__file__).parents[1]))
    assert r.returncode == 0, r.stderr[-800:]
    assert (tmp_path / "out" / "results.json").exists() and "held-out community" in (tmp_path / "out" / "report.md").read_text()


def test_loader_accepts_the_real_zenodo_file_names(tmp_path):
    import pickle
    posts, comments = _fixture()
    for v in comments.values():
        v.pop("link_id")
    p2c = {"p1": [comments[k] for k in ("c1", "c2", "c3", "c4")], "p2": ["c5", "c6"]}   # dict items AND id items
    d = tmp_path / "MentalHealthSubreddits2017"
    d.mkdir()
    pickle.dump(posts, open(d / "Anxiety_post2data.pkl", "wb"))
    pickle.dump(comments, open(d / "Anxiety_comment2data.pkl", "wb"))
    pickle.dump(p2c, open(d / "Anxiety_post2comments.pkl", "wb"))
    posts2 = {k + "x": {**{kk: vv for kk, vv in v.items() if kk not in ("subreddit",)}, "id": k + "x"} for k, v in posts.items()}
    pickle.dump(posts2, open(d / "Depression_post2data.pkl", "wb"))                       # no subreddit field: from prefix
    obs, txt, thr, stats = TB.load_zenodo_4266616(tmp_path, SALT)
    assert {"s:p1", "c:c3", "s:p2"} <= set(obs.obs_id) and set(obs.community) == {"anxiety", "depression"}
    assert set(obs[obs.obs_id.str.endswith("x")].community) == {"depression"}
    with pytest.raises(FileNotFoundError):
        TB.load_zenodo_4266616(tmp_path / "MentalHealthSubreddits2017" / "nothing", SALT)


def test_state_dynamics_ablations_run_and_are_labelled():
    df = S.simulate_obs({"c0": 60, "c1": 60}, seed=9, horizon_days=200)
    res, rec = L.run_loco(df, min_authors=30, seed=1, fit_kwargs=dict(max_authors=80, max_obs=40),
                          variants=("static", "rw", "nopool"))
    s = res["communities"]["c0"]["within"]["summary"]
    for m in ("twin[split_half]", "twin[split_half/static]", "twin[split_half/rw]", "twin[split_half/nopool]"):
        assert m in s and s[m]["n"] > 50
    f = res["communities"]["c0"]["within"]["fits"]
    assert f["split_half/static"]["sigma"] == pytest.approx(1e-3) and f["split_half/rw"]["kappa"] == pytest.approx(1e-4)
    assert s["twin[split_half]"]["nll"] < s["twin[split_half/static]"]["nll"]       # OU data: dynamics must help


def test_single_community_makes_loco_author_disjoint():
    df = S.simulate_obs({"c0": 30, "c1": 30}, seed=3, horizon_days=100)
    both = df[df.author == "c0_0"].copy(); both["community"] = "c1"          # same person also posts in c1 (fewer times)
    df = pd.concat([df, both.iloc[:3]], ignore_index=True)
    out = L.single_community(df)
    assert out.groupby("author").community.nunique().max() == 1
    assert out.attrs["multi_community_authors"] == 1 and out.attrs["obs_dropped_multi_community"] == 3


def test_loader_reads_real_zenodo_types_and_skips_macos_stubs(tmp_path):
    """Real files hold pandas Timestamps, numpy arrays of comment ids, a 'text' field, no subreddit, and a __MACOSX folder."""
    import pickle, numpy as np
    d = tmp_path / "MentalHealthSubreddits2017"; d.mkdir()
    ts = pd.Timestamp("2017-03-01 10:00:00")
    txt = "I have been struggling a lot with sleep and worry this month. " * 2
    posts = {"p1": {"author": "u1", "created_utc": ts, "text": txt, "title": "t", "pos": .1, "neg": .1, "neu": .8, "compound": 0.0}}
    comments = {"c1": {"author": "u1", "created_utc": ts + pd.Timedelta(hours=2), "text": txt, "link_id": "p1", "parent_id": "p1", "pos": 0, "neg": 0, "neu": 1, "compound": 0},
                "c2": {"author": "u2", "created_utc": ts + pd.Timedelta(hours=1), "text": txt, "link_id": "p1", "parent_id": "p1", "pos": 0, "neg": 0, "neu": 1, "compound": 0}}
    pickle.dump(posts, open(d / "Anxiety_post2data.pkl", "wb"))
    pickle.dump(comments, open(d / "Anxiety_comment2data.pkl", "wb"))
    pickle.dump({"p1": np.array(["c1", "c2"], dtype=object)}, open(d / "Anxiety_post2comments.pkl", "wb"))
    m = tmp_path / "__MACOSX" / "MentalHealthSubreddits2017"; m.mkdir(parents=True)
    (m / "._Anxiety_post2data.pkl").write_bytes(b"\x00\x05\x16\x07stub")
    obs, txtdf, thr, st = TB.load_zenodo_4266616(tmp_path, SALT)
    assert set(obs.community) == {"anxiety"} and len(obs) == 2 and len(thr) == 1
    assert thr.iloc[0].n_replies_before == 1 and obs.t_days.min() > 17000      # 2017 in days since epoch


def test_pilot_flag_partitions_authors_by_hash_prefix(tmp_path):
    import subprocess, sys, json
    df = S.simulate_obs({"c0": 60, "c1": 60}, seed=5, horizon_days=200)
    df["author"] = [("0" if hash(a) % 2 else "a") + a for a in df.author]          # '0...' = pilot, 'a...' = confirmatory
    df["obs_id"] = [f"o{i}" for i in range(len(df))]
    df[["obs_id", "author", "community", "t_days", "n_chars"]].assign(kind="submission").to_csv(tmp_path / "o.csv", index=False)
    df.rename(columns={"y": "z_mean", "ens_var": "z_var", "za": "z_a", "zb": "z_b"})[
        ["obs_id", "z_mean", "z_var", "n_chars", "z_a", "z_b", "n_half"]].to_csv(tmp_path / "s.csv", index=False)
    cwd = str(__import__("pathlib").Path(__file__).parents[1])
    n = {}
    for mode in ("only", "exclude"):
        r = subprocess.run([sys.executable, "-m", "stresstwin_p.run_all", "--obs", str(tmp_path / "o.csv"), "--scores", str(tmp_path / "s.csv"),
                            "--out", str(tmp_path / mode), "--min-authors", "10", "--pilot", mode], capture_output=True, text=True, cwd=cwd)
        assert r.returncode == 0, r.stderr[-600:]
        res = json.loads((tmp_path / mode / "results.json").read_text())
        assert res["settings"]["pilot"] == mode
        n[mode] = sum(res["eligible_authors"].values())
    assert n["only"] > 0 and n["exclude"] > 0
