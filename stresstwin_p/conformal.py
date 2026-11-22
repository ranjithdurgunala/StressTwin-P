"""Conformal intervals for the NEXT OBSERVED SCORE, with and without online adaptation.

What is covered. The target is the next observed scorer output y_i (a measurement), not the
person's true stress. That is a deliberate limit: no ground-truth state exists in this data.

Why the label is free. The 'label' for the interval at observation i is y_i itself, which
arrives with the next post. So online methods (ACI) need no human labels in this setting.

  split_q        finite-sample split-conformal quantile of source-community scores
  eval_static    fixed quantile from the SOURCE communities, applied to the target
  eval_aci       Adaptive Conformal Inference (Gibbs & Candes 2021): alpha_t is nudged by the
                 observed miscoverage, so coverage is repaired under shift and drift
  eval_gaussian  the model's own Gaussian interval, no conformal step (z * predictive sd)

Scores are standardised absolute residuals |y - mean| / sd, so intervals widen where the
model says it is unsure. Width is reported next to coverage because coverage alone can be
bought with very wide intervals.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import norm


def scores(y, mean, var):
    return np.abs(np.asarray(y, float) - np.asarray(mean, float)) / np.sqrt(np.maximum(var, 1e-12))


def split_q(cal_scores, alpha: float) -> float:
    s = np.sort(np.asarray(cal_scores, float))
    n = len(s)
    if n == 0:
        return np.inf
    k = int(np.ceil((n + 1) * (1 - alpha)))
    return float(s[min(k, n) - 1]) if k <= n else np.inf


def _summ(covered, halfwidth):
    hw = np.asarray(halfwidth, float)
    finite = np.isfinite(hw)
    return {
        "coverage": float(np.mean(covered)),
        "mean_width": float(2 * np.mean(hw[finite])) if finite.any() else float("inf"),
        "frac_infinite": float(1 - finite.mean()),
        "n": int(len(hw)),
    }


def eval_gaussian(y, mean, var, alpha: float):
    z = norm.ppf(1 - alpha / 2)
    sd = np.sqrt(np.maximum(var, 1e-12))
    return _summ(np.abs(np.asarray(y) - mean) <= z * sd, z * sd)


def eval_static(y, mean, var, cal_scores, alpha: float):
    q = split_q(cal_scores, alpha)
    sd = np.sqrt(np.maximum(var, 1e-12))
    return _summ(np.abs(np.asarray(y) - mean) <= q * sd, q * sd) | {"q": q}


def eval_aci(y, mean, var, cal_scores, alpha: float, gamma: float = 0.02):
    """y, mean, var must already be ordered by time (a pooled stream within one community)."""
    cal = np.sort(np.asarray(cal_scores, float))
    sd = np.sqrt(np.maximum(var, 1e-12))
    a = alpha
    covered = np.empty(len(y), bool)
    hw = np.empty(len(y))
    for i in range(len(y)):
        if a <= 0:
            q = np.inf
        elif a >= 1:
            q = 0.0
        else:
            q = split_q(cal, a)
        hw[i] = q * sd[i]
        covered[i] = abs(y[i] - mean[i]) <= hw[i]
        a = a + gamma * (alpha - (0.0 if covered[i] else 1.0))
    return _summ(covered, hw) | {"final_alpha": float(a)}
