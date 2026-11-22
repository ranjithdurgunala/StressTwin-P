import numpy as np
import pandas as pd
from stresstwin_p import annotation as A


def _data(n_auth=60, per=6, seed=0):
    rng = np.random.default_rng(seed)
    rows, texts, val = [], [], {}
    for a in range(n_auth):
        for k in range(per):
            oid = f"a{a}_{k}"
            rows.append((oid, f"u{a}", "c", k * 5.0 + rng.random()))
            texts.append((oid, f"text {oid}"))
            val[oid] = rng.normal()
    return (pd.DataFrame(rows, columns=["obs_id", "author", "community", "t_days"]),
            pd.DataFrame(texts, columns=["obs_id", "text"]), pd.Series(val))


def test_sheet_is_blind_one_pair_per_author_and_order_randomised():
    obs, txt, val = _data()
    sheet, key = A.sample_pairs(obs, txt, val, n_pairs=40, seed=1)
    assert list(sheet.columns) == ["pair_id", "text_a", "text_b"]            # no scores, dates, authors, communities
    assert len(sheet) == 40 and key.obs_a.str.split("_").str[0].nunique() == 40
    earlier_first = np.mean([obs.set_index("obs_id").t_days[a] < obs.set_index("obs_id").t_days[b]
                             for a, b in zip(key.obs_a, key.obs_b)])
    assert 0.25 < earlier_first < 0.75


def test_agreement_detects_a_model_that_matches_humans_and_one_that_does_not():
    obs, txt, val = _data()
    _, key = A.sample_pairs(obs, txt, val, n_pairs=120, seed=2)
    good = pd.DataFrame({"pair_id": key.pair_id, "label": np.where(key.value_a > key.value_b, "A", "B")})
    assert A.agreement(key, good)["accuracy"] == 1.0
    rng = np.random.default_rng(0)
    rand = pd.DataFrame({"pair_id": key.pair_id, "label": rng.choice(["A", "B"], len(key))})
    r = A.agreement(key, rand)
    assert 0.35 < r["accuracy"] < 0.65 and not r["beats_chance"]
    assert A.cohen_kappa(["A", "B", "A"], ["A", "B", "A"]) == 1.0
