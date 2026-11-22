"""Observation-noise models: how much should one scored text be trusted?

Three arms, all producing a per-observation variance R_i on the scorer's logit scale.
A global scale (OUParams.noise_scale) is then fitted by marginal likelihood for EVERY arm,
so arms differ only in the *shape* of the noise, not its overall size.

  fixed        R_i = 1
  conf_rule    R_i = max(1e-3, 1 - c_i), c_i = scorer softmax confidence.
               This is the AI YOU rule (R = 1 - confidence) applied to a classifier's own
               confidence. NOTE: AI YOU uses an LLM's *verbalised* confidence; a classifier's
               softmax confidence is a different quantity, so this arm is the closest
               analogue, not an exact replication.
  split_half   R_i = a0 + a1 / n_i + a2 * v_i, fitted without labels from split-half
               disagreement (a text is cut into two halves, each scored; E[(za-zb)^2 / 2] is
               the noise variance of a half-length text). n_i = text length, v_i = variance
               of the scorer's ensemble (seeds).

Split-half noise includes real within-text content variation, so it is a measure of how far
one text's score can sit from the person's level for reasons other than their level.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.optimize import nnls

R_FLOOR = 1e-3


def r_fixed(n: int) -> np.ndarray:
    return np.ones(n)


def r_conf_rule(logit: np.ndarray) -> np.ndarray:
    """c = softmax confidence of a binary classifier = sigmoid(|logit|)."""
    c = 1.0 / (1.0 + np.exp(-np.abs(np.asarray(logit, float))))
    return np.maximum(R_FLOOR, 1.0 - c)


@dataclass(frozen=True)
class SplitHalfNoise:
    a0: float
    a1: float
    a2: float
    n_pairs: int

    def predict(self, n_chars: np.ndarray, ens_var: np.ndarray) -> np.ndarray:
        n = np.maximum(np.asarray(n_chars, float), 1.0)
        v = np.maximum(np.asarray(ens_var, float), 0.0)
        return np.maximum(R_FLOOR, self.a0 + self.a1 / n + self.a2 * v)


def fit_split_half(za, zb, n_chars_half, ens_var_half) -> SplitHalfNoise:
    """Non-negative least squares of d = (za - zb)^2 / 2 on [1, 1/n, v]."""
    za, zb = np.asarray(za, float), np.asarray(zb, float)
    d = 0.5 * (za - zb) ** 2
    n = np.maximum(np.asarray(n_chars_half, float), 1.0)
    v = np.maximum(np.asarray(ens_var_half, float), 0.0)
    ok = np.isfinite(d) & np.isfinite(n) & np.isfinite(v)
    if ok.sum() < 30:
        raise ValueError(f"need >= 30 split-half pairs, got {int(ok.sum())}")
    X = np.column_stack([np.ones(ok.sum()), 1.0 / n[ok], v[ok]])
    # scale columns so NNLS is well conditioned
    scale = X.std(axis=0)
    scale[0] = 1.0
    scale[scale == 0] = 1.0
    coef, _ = nnls(X / scale, d[ok])
    coef = coef / scale
    return SplitHalfNoise(float(coef[0]), float(coef[1]), float(coef[2]), int(ok.sum()))


def noise_for_arm(arm: str, logit, n_chars=None, ens_var=None, model: SplitHalfNoise | None = None):
    logit = np.asarray(logit, float)
    if arm == "fixed":
        return r_fixed(len(logit))
    if arm == "conf_rule":
        return r_conf_rule(logit)
    if arm == "split_half":
        if model is None or n_chars is None or ens_var is None:
            raise ValueError("split_half arm needs a fitted model, n_chars and ens_var")
        return model.predict(n_chars, ens_var)
    raise ValueError(f"unknown noise arm: {arm}")


ARMS = ("fixed", "conf_rule", "split_half")
