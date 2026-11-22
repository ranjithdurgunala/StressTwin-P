"""Baselines for one-step-ahead prediction of an author's next score.

Every predictor is CAUSAL: the prediction for observation i uses observations 0..i-1 only.
Observation 0 has no history, so scoring always starts at i = 1.

  author_mean   expanding mean of the author's previous scores       (uses no training data)
  last          the previous score                                    (uses no training data)
  ewma          exponentially weighted by observation count, alpha tuned on training authors
  gap_ewma      exponentially weighted by elapsed days, half-life tuned on training authors
  global_mean   the training-set mean score for everyone
"""
from __future__ import annotations

import numpy as np

HALFLIFE_GRID_DAYS = (0.5, 1, 2, 4, 7, 14, 30, 60, 120)
ALPHA_GRID = (0.1, 0.2, 0.3, 0.5, 0.7, 0.9)


def predict_author_mean(t, y):
    y = np.asarray(y, float)
    out = np.full(len(y), np.nan)
    if len(y) > 1:
        out[1:] = np.cumsum(y)[:-1] / np.arange(1, len(y))
    return out


def predict_last(t, y):
    y = np.asarray(y, float)
    out = np.full(len(y), np.nan)
    out[1:] = y[:-1]
    return out


def predict_ewma(t, y, alpha):
    y = np.asarray(y, float)
    out = np.full(len(y), np.nan)
    if len(y) == 0:
        return out
    s = y[0]
    for i in range(1, len(y)):
        out[i] = s
        s = alpha * y[i] + (1 - alpha) * s
    return out


def predict_gap_ewma(t, y, halflife_days):
    """Kernel-weighted mean of the author's PREVIOUS scores, weight 0.5**(age/halflife).

    age is measured from the time of the observation being predicted, so a long gap
    since the last post shrinks every weight equally (the mean is unchanged) while a
    short half-life emphasises the most recent posts.
    """
    t = np.asarray(t, float); y = np.asarray(y, float)
    out = np.full(len(y), np.nan)
    for i in range(1, len(y)):
        w = 0.5 ** (np.maximum(t[i] - t[:i], 0.0) / halflife_days)
        out[i] = float(np.sum(w * y[:i]) / np.sum(w))
    return out


def predict_global_mean(t, y, mean):
    out = np.full(len(y), float(mean))
    if len(out):
        out[0] = np.nan
    return out


def _mse(timelines, fn):
    se, n = 0.0, 0
    for tl in timelines:
        p = fn(tl.t, tl.y)
        m = ~np.isnan(p)
        se += float(np.sum((tl.y[m] - p[m]) ** 2)); n += int(m.sum())
    return se / n if n else np.inf


def tune_ewma(timelines):
    best = min(ALPHA_GRID, key=lambda a: _mse(timelines, lambda t, y: predict_ewma(t, y, a)))
    return best


def tune_gap_ewma(timelines):
    best = min(HALFLIFE_GRID_DAYS, key=lambda h: _mse(timelines, lambda t, y: predict_gap_ewma(t, y, h)))
    return best


def residual_variance(timelines, fn) -> float:
    """Constant predictive variance for a point-predictor, from training residuals."""
    res = []
    for tl in timelines:
        p = fn(tl.t, tl.y)
        m = ~np.isnan(p)
        res.append(tl.y[m] - p[m])
    r = np.concatenate(res) if res else np.array([])
    return float(np.mean(r ** 2)) if len(r) else np.nan


def gaussian_logscore(y, mean, var):
    var = np.maximum(var, 1e-9)
    return -0.5 * (np.log(2 * np.pi * var) + (y - mean) ** 2 / var)


# ---------------------------------------------------------------- shortcut (nuisance-feature) baseline
def shortcut_features(t, n_chars):
    """Features available at prediction time that are NOT stress: text length, gap since previous post,
    how many posts the author already has. If the twin cannot beat a model that sees only these, the 'state'
    may be tracking style or activity."""
    t = np.asarray(t, float); n = np.asarray(n_chars, float)
    gap = np.r_[0.0, np.diff(t)]
    k = np.arange(len(t))
    return np.column_stack([np.ones(len(t)), np.log1p(n), np.log1p(np.maximum(gap, 0)), np.log1p(k)])


def fit_shortcut(timelines_with_nchars):
    """timelines_with_nchars: iterable of (t, y, n_chars). OLS of (y_i - author running mean) on shortcut features."""
    X, Y = [], []
    for t, y, n in timelines_with_nchars:
        if len(y) < 2:
            continue
        base = predict_author_mean(t, y)
        F = shortcut_features(t, n)
        X.append(F[1:]); Y.append(np.asarray(y, float)[1:] - base[1:])
    if not X:
        return np.zeros(4)
    X, Y = np.vstack(X), np.concatenate(Y)
    return np.linalg.lstsq(X, Y, rcond=None)[0]


def predict_shortcut(t, y, n_chars, coef):
    base = predict_author_mean(t, y)
    out = base + shortcut_features(t, n_chars) @ coef
    out[0] = np.nan
    return out
