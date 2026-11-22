"""Person-level state-space twin: Ornstein-Uhlenbeck fluctuation around a person baseline.

Model (time in days, observations irregularly spaced):

    level_i  = m + x(t_i)                    latent stress level of the person at time t_i
    x        ~ OU(kappa, sigma)              stationary, mean 0, sd sigma, correlation exp(-kappa*|dt|)
    m        ~ N(mu, tau^2)                  person baseline (partial pooling: shrinks to mu)
    y_i      = level_i + e_i,  e_i ~ N(0, s * R_i)

R_i is the observation-noise variance from the observation model (see noise.py); s is one
global scale. This is a Gaussian process with covariance

    Cov(y_i, y_j) = tau^2 + sigma^2 * exp(-kappa*|t_i - t_j|) + s*R_i*[i == j]

so the exact marginal likelihood is a multivariate normal (used for fitting), and the same
model has an equivalent 2-state Kalman filter (used for causal one-step-ahead prediction).
tests/test_ou_filter.py checks the two agree to numerical precision.
"""
from __future__ import annotations

from dataclasses import dataclass, replace

import numpy as np
from scipy.linalg import cho_factor, cho_solve
from scipy.optimize import minimize

LOG2PI = np.log(2.0 * np.pi)


@dataclass(frozen=True)
class OUParams:
    kappa: float          # mean-reversion rate, per day
    sigma: float          # stationary sd of within-person fluctuation
    tau: float            # sd of person baselines around mu
    mu: float             # population mean level
    noise_scale: float = 1.0   # multiplies R_i

    def __post_init__(self):
        for name in ("kappa", "sigma", "tau", "noise_scale"):
            v = getattr(self, name)
            if not np.isfinite(v) or v <= 0:
                raise ValueError(f"{name} must be positive and finite, got {v}")
        if not np.isfinite(self.mu):
            raise ValueError("mu must be finite")


@dataclass
class Timeline:
    """One author's observations. t is in days, strictly non-decreasing."""
    author: str
    t: np.ndarray
    y: np.ndarray
    R: np.ndarray          # observation-noise variance per observation (before noise_scale)

    def __post_init__(self):
        self.t = np.asarray(self.t, float)
        self.y = np.asarray(self.y, float)
        self.R = np.asarray(self.R, float)
        if not (len(self.t) == len(self.y) == len(self.R)):
            raise ValueError("t, y, R must have equal length")
        if len(self.t) and np.any(np.diff(self.t) < 0):
            raise ValueError("timeline must be sorted by time")
        if np.any(self.R <= 0):
            raise ValueError("R must be positive")

    def __len__(self):
        return len(self.t)


def author_loglik(tl: Timeline, p: OUParams, max_obs: int | None = None) -> float:
    t, y, R = tl.t, tl.y, tl.R
    if max_obs is not None and len(t) > max_obs:
        t, y, R = t[-max_obs:], y[-max_obs:], R[-max_obs:]
    n = len(t)
    if n == 0:
        return 0.0
    dt = np.abs(t[:, None] - t[None, :])
    S = p.tau ** 2 + p.sigma ** 2 * np.exp(-p.kappa * dt)
    S[np.diag_indices(n)] += p.noise_scale * R
    try:
        c = cho_factor(S, lower=True)
    except np.linalg.LinAlgError:
        S[np.diag_indices(n)] += 1e-8
        c = cho_factor(S, lower=True)
    r = y - p.mu
    a = cho_solve(c, r)
    logdet = 2.0 * np.log(np.diag(c[0])).sum()
    return float(-0.5 * (r @ a + logdet + n * LOG2PI))


def total_loglik(timelines, p: OUParams, max_obs: int | None = None) -> float:
    return float(sum(author_loglik(tl, p, max_obs) for tl in timelines))


@dataclass
class FilterOutput:
    pred_mean: np.ndarray    # E[y_i | y_<i]   (nan-free; for i=0 uses the prior)
    pred_var: np.ndarray     # Var[y_i | y_<i], includes observation noise
    filt_mean: np.ndarray    # E[level_i | y_<=i]
    filt_var: np.ndarray     # Var[level_i | y_<=i]


def kalman_filter(tl: Timeline, p: OUParams) -> FilterOutput:
    """Causal filter. State s = [x, m]. Output at i uses observations 0..i only."""
    n = len(tl)
    pm = np.empty(n); pv = np.empty(n); fm = np.empty(n); fv = np.empty(n)
    s = np.array([0.0, p.mu])
    P = np.array([[p.sigma ** 2, 0.0], [0.0, p.tau ** 2]])
    H = np.array([1.0, 1.0])
    for i in range(n):
        if i > 0:
            dt = max(tl.t[i] - tl.t[i - 1], 0.0)
            phi = np.exp(-p.kappa * dt)
            F = np.array([[phi, 0.0], [0.0, 1.0]])
            Q = np.array([[p.sigma ** 2 * (1.0 - phi ** 2), 0.0], [0.0, 0.0]])
            s = F @ s
            P = F @ P @ F.T + Q
        yhat = H @ s
        Ph = P @ H
        S = H @ Ph + p.noise_scale * tl.R[i]
        pm[i], pv[i] = yhat, S
        K = Ph / S
        s = s + K * (tl.y[i] - yhat)
        P = P - np.outer(K, Ph)
        P = 0.5 * (P + P.T)
        fm[i] = H @ s
        fv[i] = H @ P @ H
    return FilterOutput(pm, pv, fm, fv)


# ---------------------------------------------------------------- fitting

_BOUNDS = {  # on log scale, except mu
    "log_kappa": (np.log(1e-3), np.log(5.0)),
    "log_sigma": (np.log(0.02), np.log(10.0)),
    "log_tau": (np.log(0.02), np.log(10.0)),
    "log_scale": (np.log(0.05), np.log(20.0)),
}


@dataclass
class FitResult:
    params: OUParams
    neg_loglik: float
    n_authors: int
    n_obs: int
    converged: bool
    at_bound: list


def fit_ou(timelines, fit_noise_scale: bool = True, max_authors: int | None = 3000,
           max_obs: int | None = 200, seed: int = 0, init: OUParams | None = None,
           fixed: dict | None = None) -> FitResult:
    """fixed: optional {'kappa'|'sigma'|'tau': value} held constant (used for the state-dynamics ablations)."""
    fixed = fixed or {}
    tls = [tl for tl in timelines if len(tl) >= 2]
    if len(tls) < 5:
        raise ValueError(f"need at least 5 timelines with >= 2 observations, got {len(tls)}")
    if max_authors is not None and len(tls) > max_authors:
        idx = np.random.default_rng(seed).choice(len(tls), max_authors, replace=False)
        tls = [tls[i] for i in sorted(idx)]
    ally = np.concatenate([tl.y for tl in tls])
    sd = float(np.std(ally)) or 1.0
    if init is None:
        init = OUParams(kappa=0.1, sigma=0.7 * sd, tau=0.7 * sd, mu=float(np.mean(ally)))

    def unpack(th):
        return OUParams(np.exp(th[0]), np.exp(th[1]), np.exp(th[2]), th[3],
                        np.exp(th[4]) if fit_noise_scale else init.noise_scale)

    def nll(th):
        try:
            return -total_loglik(tls, unpack(th), max_obs)
        except (np.linalg.LinAlgError, ValueError):
            return 1e12

    init = OUParams(fixed.get("kappa", init.kappa), fixed.get("sigma", init.sigma), fixed.get("tau", init.tau),
                    init.mu, init.noise_scale)
    th0 = np.array([np.log(init.kappa), np.log(init.sigma), np.log(init.tau), init.mu, np.log(init.noise_scale)])
    bnds = [_BOUNDS["log_kappa"], _BOUNDS["log_sigma"], _BOUNDS["log_tau"],
            (float(ally.min()), float(ally.max())),
            _BOUNDS["log_scale"] if fit_noise_scale else (th0[4], th0[4])]
    for k, name in enumerate(("kappa", "sigma", "tau")):
        if name in fixed:
            bnds[k] = (th0[k], th0[k])
    res = minimize(nll, th0, method="L-BFGS-B", bounds=bnds)
    p = unpack(res.x)
    at_bound = []
    for name, v, (lo, hi) in zip(["kappa", "sigma", "tau", "mu", "noise_scale"], res.x, bnds):
        if hi > lo and (abs(v - lo) < 1e-6 or abs(v - hi) < 1e-6):
            at_bound.append(name)
    return FitResult(p, float(res.fun), len(tls), int(sum(len(t) for t in tls)), bool(res.success), at_bound)


def filter_all(timelines, p: OUParams) -> dict:
    return {tl.author: kalman_filter(tl, p) for tl in timelines}
