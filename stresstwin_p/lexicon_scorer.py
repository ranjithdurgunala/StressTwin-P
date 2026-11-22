"""CPU-only lexicon scorer: negative-affect index from VADER (Hutto & Gilbert, 2014).

    y = -compound   (compound is in [-1, 1]; higher y = more negative affect)

This is NOT StressTwin-F and not a stress classifier. It serves three purposes:
  1. a pilot that exercises the whole twin pipeline on real timelines before the GPU scorer exists;
  2. a no-GPU comparison arm for the scorer ablation (does the twin's conclusion depend on the scorer?);
  3. the lexicon baseline that prior Reddit work on this corpus used as its label.
Its scale is bounded and not a logit, so never compare its raw errors with StressTwin-F's.
"""
from __future__ import annotations

import numpy as np


def vader_scorers():
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    an = SentimentIntensityAnalyzer()

    def f(texts):
        return np.array([-an.polarity_scores(t)["compound"] for t in texts], float)
    return [f]
