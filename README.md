# StressTwin-P

Code, tests and result files for **"StressTwin-P: Person-Level Forecasting and Interval Reliability of Text-Derived Stress Scores in Social Media"** (R. Durgunala and B. S. Kumar).

StressTwin-P is a person-level, digital-twin-inspired forecasting framework for text-derived stress scores: a person-specific latent state updated sequentially as posts arrive, with predictive intervals. It combines

* a latent Ornstein–Uhlenbeck state with partial pooling of person baselines,
* observation noise measured from split-half scorer disagreement, fitted without labels,
* exact marginal likelihood and an equivalent Kalman filter for one-step-ahead prediction,
* Gaussian, static split-conformal and adaptive conformal 90% intervals,
* author-disjoint leave-one-community-out (LOCO) evaluation on Reddit, five partition seeds and author-cluster bootstrap intervals.

Partial pooling is the main source of the forecasting gain; the dynamics are not identified at the available time resolution (see the paper). The prediction target is the score of the StressTwin-F scorer, not a clinical measure. Nothing in this repository supports a clinical, diagnostic or causal claim.

## Layout

| Path | Content |
|---|---|
| `stresstwin_p/` | Python package: timeline builder, scorer wrapper, noise model, OU filter, baselines, conformal methods, LOCO harness, statistics |
| `tests/` | Unit tests (filter vs marginal likelihood, leakage checks, statistics, scorer) |
| `notebooks/` | Notebooks for each stage (data build, scoring, twin and LOCO run) |
| `retrain_kit/` | Scripts that retrain the scorer on Dreaddit and verify the export |
| `reproduce/` | Scripts that regenerate every table value and figure of the paper from the result files |
| `results/` | Per-seed result files (`seed0` … `seed4`), recomputed values, funnel counts, scorer retraining log |
| `figures/` | The four figures of the paper (Fig. 4 is written by `reproduce/shrinkage_diagnostic.py`) |
| `docs/` | `DATA.md`, `REPRODUCE.md`, `PROTOCOL.md` |

## Quick start

```bash
pip install -r requirements.txt
pip install -e .
pytest -q tests
python reproduce/scorer_summary.py results/scorer_retrain_log.txt
python reproduce/make_figures.py --values results/values.json --out figures
python reproduce/check_manuscript.py path/to/manuscript.docx   # Tables 1-7 against results/
```

`docs/REPRODUCE.md` lists the full chain from the public Zenodo data to every number in the paper.

## Data and privacy

The Reddit timelines are public (doi:10.5281/zenodo.4266616). This repository contains no raw text, no author names and no pseudonymisation salt; only aggregate result files are included. See `docs/DATA.md`.

## Licence

MIT, see `LICENSE`.

## Citation

If you use this code, please cite the paper (reference to be added on publication).
