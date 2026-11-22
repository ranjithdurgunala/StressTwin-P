# Pre-specified protocol

Written before the confirmatory run. The study was not publicly registered, so these are pre-specified hypotheses, not a registration.

* **Pilot discipline.** Authors whose hash starts with 0 or 1 (about 12.5%) are a design pilot and are excluded from every reported analysis.
* **Eligibility.** At least 5 observations spanning at least 14 days; one community per author (the community with most observations).
* **Primary outcome.** One-step-ahead negative log-likelihood of the next score; MSE secondary. Differences are twin minus comparator (negative favours the twin). 95% author-cluster bootstrap intervals; Bonferroni adjustment over 24 comparisons.
* **H1.** Twin NLL is below the author mean, EWMA and the shortcut in at least 2 of 4 communities with an adjusted interval excluding zero.
* **H1b.** Comparison with the global mean and the static twin, reported either way.
* **H2.** Measured split-half noise beats fixed and confidence-rule noise on NLL.
* **H3.** Adaptive conformal coverage lies within 0.90 ± 0.03, reported with width.
* **H4.** The reply association is negative with a smaller placebo (gate: placebo magnitude below half the main coefficient).
* **H5.** The fidelity-based twin is at least as good as a plain-scorer twin.
* **Seeds.** Five author-partition seeds (0 to 4).

## Partition and leakage rules (as implemented)

* Every author has one role per fold: test author, within-community training author, or across-community training author. Test authors are a random half of the held-out community's eligible authors; within-community training authors come from the other half; across-community training authors come from the other three communities. Authors who wrote in several communities are assigned to one community before any split.
* On training authors only, per fold and per seed: state parameters (kappa, sigma, tau, mu, s), split-half noise coefficients (a0, a1, a2; non-negative least squares), the global mean and the conformal quantile.
* A test author's earlier scores enter only that author's causal filter. No target score is used for a prediction except by the shortcut, which is labelled target-available.
* Known departure: no separate set of calibration authors is held out. Conformal scores are in-sample standardised residuals of the training authors, computed with parameters fitted on the same authors; the intervals are residual-calibrated and carry no formal conformal guarantee. `reproduce/conformal_heldout_calibration.py` repeats the static interval with calibration on held-out authors.
* Optimiser: L-BFGS-B on log kappa, log sigma, log tau, log s and mu, single start, bounds kappa in [0.001, 5] per day, sigma and tau in [0.02, 10], s in [0.05, 20], mu in [min, max] of the training scores; at most 3,000 authors and 200 observations per author per fit. Fits with a parameter at a bound are flagged in `results/seed*/results.json` (`at_bound`).
* Reply association: OLS of the change in filtered level between an opening post and the author's last own comment on log(1 + replies before), the opening level, log(1 + opening length), log(1 + hours) and community effects, with author-clustered (CR1) errors; the placebo uses replies after the comment. The model is fitted once on all eligible authors pooled, so this is an association check, not a transfer test.
