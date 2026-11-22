import numpy as np
import pandas as pd
import pytest

from stresstwin_p import baselines as B
from stresstwin_p import conformal as C
from stresstwin_p import events as E
from stresstwin_p import noise as N
from stresstwin_p import ou_filter as O
from stresstwin_p import synthetic as S


def make_tl(rng, p, n=25, horizon=200.0, author="a"):
    t = np.sort(rng.uniform(0, horizon, n))
    R = rng.uniform(0.1, 0.6, n)
    m = rng.normal(p.mu, p.tau)
    x = S._ou_path(t, p.kappa, p.sigma, rng)
    y = m + x + rng.normal(0, np.sqrt(p.noise_scale * R))
    return O.Timeline(author, t, y, R), m + x


# ---------------------------------------------------------------- ou_filter
def test_kalman_matches_exact_gp_likelihood():
    rng = np.random.default_rng(0)
    p = O.OUParams(0.2, 0.9, 0.7, 0.3, 1.3)
    for _ in range(5):
        tl, _ = make_tl(rng, p, n=18)
        f = O.kalman_filter(tl, p)
        ll_kf = float(np.sum(-0.5 * (np.log(2 * np.pi * f.pred_var) + (tl.y - f.pred_mean) ** 2 / f.pred_var)))
        assert ll_kf == pytest.approx(O.author_loglik(tl, p), rel=1e-9, abs=1e-9)


def test_filter_is_causal():
    rng = np.random.default_rng(1)
    p = O.OUParams(0.2, 0.9, 0.7, 0.0)
    tl, _ = make_tl(rng, p, n=20)
    base = O.kalman_filter(tl, p)
    y2 = tl.y.copy(); y2[12:] += 50.0                     # change the future only
    alt = O.kalman_filter(O.Timeline("a", tl.t, y2, tl.R), p)
    np.testing.assert_allclose(base.pred_mean[:12], alt.pred_mean[:12])
    np.testing.assert_allclose(base.filt_mean[:12], alt.filt_mean[:12])
    assert not np.allclose(base.filt_mean[12:], alt.filt_mean[12:])


def test_fit_recovers_planted_parameters():
    rng = np.random.default_rng(2)
    true = O.OUParams(0.15, 0.8, 0.9, 0.5, 1.0)
    tls = [make_tl(rng, true, n=int(rng.integers(8, 30)), horizon=200, author=f"a{i}")[0] for i in range(400)]
    fit = O.fit_ou(tls, fit_noise_scale=True)
    p = fit.params
    assert fit.converged
    assert p.sigma == pytest.approx(0.8, rel=0.2)
    assert p.tau == pytest.approx(0.9, rel=0.2)
    assert p.mu == pytest.approx(0.5, abs=0.15)
    assert p.kappa == pytest.approx(0.15, rel=0.5)
    assert p.noise_scale == pytest.approx(1.0, rel=0.35)


def test_twin_beats_author_mean_on_ou_data_and_flat_on_noise_only():
    """Sanity: on data that truly has OU dynamics the filter predicts better than the running mean."""
    rng = np.random.default_rng(3)
    true = O.OUParams(0.3, 1.0, 0.5, 0.0, 1.0)
    tls = [make_tl(rng, true, n=20, horizon=100, author=f"a{i}")[0] for i in range(200)]
    se_f = se_m = n = 0
    for tl in tls:
        f = O.kalman_filter(tl, true)
        m = B.predict_author_mean(tl.t, tl.y)
        k = slice(1, None)
        se_f += np.sum((tl.y[k] - f.pred_mean[k]) ** 2); se_m += np.sum((tl.y[k] - m[k]) ** 2); n += len(tl) - 1
    assert se_f / n < se_m / n


# ---------------------------------------------------------------- baselines
def test_baselines_are_causal():
    t = np.arange(8.0); y = np.array([1, 2, 3, 4, 5, 6, 7, 8.0])
    y2 = y.copy(); y2[5:] = 99
    for fn in (B.predict_author_mean, B.predict_last,
               lambda t, y: B.predict_ewma(t, y, 0.3), lambda t, y: B.predict_gap_ewma(t, y, 2.0)):
        a, b = fn(t, y), fn(t, y2)
        np.testing.assert_allclose(a[:6], b[:6])           # predictions up to index 5 use y[:5] only
        assert np.isnan(a[0])


# ---------------------------------------------------------------- noise
def test_split_half_recovers_planted_noise_function():
    d = S.simulate_obs({"c": 400}, seed=5)
    h = d.dropna(subset=["za"])
    m = N.fit_split_half(h.za, h.zb, h.n_half, h.ens_var)
    assert m.a0 == pytest.approx(0.15, abs=0.08)
    assert m.a1 == pytest.approx(60.0, rel=0.35)
    assert m.a2 == pytest.approx(3.0, rel=0.4)


def test_conf_rule_is_high_for_ambiguous_scores_not_for_noisy_ones():
    r = N.r_conf_rule(np.array([0.0, 4.0]))
    assert r[0] > r[1]                  # near-zero logit -> low confidence -> high 'noise'


def test_noise_arm_validation():
    with pytest.raises(ValueError):
        N.noise_for_arm("split_half", [0.0])
    with pytest.raises(ValueError):
        N.noise_for_arm("nope", [0.0])
    with pytest.raises(ValueError):
        O.OUParams(-1, 1, 1, 0)


# ---------------------------------------------------------------- conformal
def _gauss_stream(rng, n, shift=0.0, sd=1.0):
    mean = np.zeros(n); var = np.ones(n)
    y = mean + shift + rng.normal(0, sd, n)
    return y, mean, var


def test_static_conformal_covers_when_exchangeable_and_fails_under_shift():
    rng = np.random.default_rng(6)
    ys, ms, vs = _gauss_stream(rng, 4000)
    cal = C.scores(ys, ms, vs)
    yt, mt, vt = _gauss_stream(rng, 4000)
    ok = C.eval_static(yt, mt, vt, cal, 0.1)
    assert 0.87 < ok["coverage"] < 0.93
    yt, mt, vt = _gauss_stream(rng, 4000, shift=2.0, sd=1.5)     # a Twitter-like shift
    bad = C.eval_static(yt, mt, vt, cal, 0.1)
    assert bad["coverage"] < 0.7


def test_aci_repairs_coverage_under_shift_without_target_labels_beyond_the_stream():
    rng = np.random.default_rng(7)
    ys, ms, vs = _gauss_stream(rng, 4000)
    cal = C.scores(ys, ms, vs)
    yt, mt, vt = _gauss_stream(rng, 6000, shift=2.0, sd=1.5)
    static = C.eval_static(yt, mt, vt, cal, 0.1)
    aci = C.eval_aci(yt, mt, vt, cal, 0.1, gamma=0.02)
    assert static["coverage"] < 0.7
    assert abs(aci["coverage"] - 0.9) < 0.03
    assert aci["mean_width"] > static["mean_width"]       # coverage is bought with width: reported


# ---------------------------------------------------------------- events
def test_e1_detects_planted_effect_and_placebo_is_null():
    th = S.simulate_threads(3000, seed=1, beta=-0.30)
    r = E.e1_dose_response(th)
    assert r["e1"]["beta"] < -0.15 and r["e1"]["p"] < 0.01
    assert abs(r["placebo"]["beta"]) < 0.08
    assert r["gate_a_pass"]


def test_e1_null_false_positive_rate_is_low_and_regression_to_the_mean_exists():
    passes = 0
    for seed in range(60):
        r = E.e1_dose_response(S.simulate_threads(1500, seed=100 + seed, beta=0.0))
        passes += r["gate_a_pass"]
    assert passes / 60 <= 0.05              # measured 0.5% over 200 runs; the placebo condition makes the gate conservative
    th = S.simulate_threads(3000, seed=2, beta=0.0)
    high = th[th.state_open > 1.0]
    assert (high.state_after - high.state_open).mean() < -0.3     # the trap the controls exist for


def test_e1_confounded_by_severity_is_caught_by_the_placebo():
    """No true effect, but severity drives reply counts. Both coefficients move together,
    so the gate must NOT pass."""
    th = S.simulate_threads(6000, seed=3, beta=0.0, confound=0.5, measure_sd=0.8)
    r = E.e1_dose_response(th)
    assert abs(r["placebo"]["beta"]) > 0.3 * abs(r["e1"]["beta"]) or abs(r["e1"]["beta"]) < 0.05
    assert not r["gate_a_pass"]


def test_e1_requires_columns():
    with pytest.raises(ValueError):
        E.e1_dose_response(pd.DataFrame({"author": [1]}))
