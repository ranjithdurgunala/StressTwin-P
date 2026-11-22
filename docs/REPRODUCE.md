# Reproducing the paper

All commands are run from the repository root. Every number in the paper's tables and text is produced by the scripts below.

## 1. Tests

```bash
pip install -r requirements.txt && pip install -e .
pytest -q tests
```

## 2. Scorer (StressTwin-F)

`retrain_kit/03_train_eval.py` retrains the scorer and the plain fine-tuned model on Dreaddit (five seeds each; GPU). The retraining log is `results/scorer_retrain_log.txt`:

```bash
python reproduce/scorer_summary.py results/scorer_retrain_log.txt
# stresstwin_f  F1 0.768 (SD 0.007)  CC 0.869  ST 0.031
# plain_ft      F1 0.760 (SD 0.003)  CC 0.552  ST 0.041
```

## 3. Timelines, scores and the twin run

1. `notebooks/stage0_download_build.ipynb`: build `observations.csv` and `threads.csv` from the Zenodo files.
2. `notebooks/stage1_score_gpu.ipynb`: score every text with StressTwin-F (and `retrain_kit` for the plain scorer).
3. `notebooks/stage2_twin_loco_e1.ipynb` or `python -m stresstwin_p.run_all --obs observations.csv --scores scores.csv --threads threads.csv --out results/`: LOCO evaluation for each partition seed.

The five runs used in the paper are stored in `results/seed0` … `results/seed4`.

## 4. Tables and figures

```bash
python reproduce/funnel_counts.py --obs observations.csv --out results/funnel.json      # Tables 1-2, cohort A
python reproduce/compute_values.py --results <dir with results_seed0..4 and records> --out results/values.json
python reproduce/prediction_diagnostics.py --records <dir with results_seed0..4> --out results/diagnostics.json   # needs records.csv.gz
python reproduce/make_figures.py --values results/values.json --out figures
python reproduce/learned_baselines.py --records <dir with results_seed0..4> --out results/learned_baselines.json   # needs records.csv.gz; exploratory, Table 11
python reproduce/shrinkage_diagnostic.py --records <dir with results_seed0..4> --out results/shrinkage.json --fig figures/fig4_shrinkage.png   # Fig. 4
python reproduce/conformal_heldout_calibration.py --records <dir> --out results/conformal_heldout.json   # Section 6.3, author-disjoint calibration
PYTHONPATH=. python reproduce/kappa_profile.py --records <dir> --out results/kappa_profile.json --seed 0   # Section 6.1, kappa profile and five starts
python reproduce/check_manuscript.py manuscript.docx
```

`check_manuscript.py` reads Tables 1 to 7 and 9 to 11 of the manuscript and compares every cell with the recomputed values. The in-text numbers were taken from the same files (`values.json`, `funnel.json`, `seed*/results.json`).

## 5. Mapping from paper to files

| Paper element | Source |
|---|---|
| Tables 1, 2; cohort A statistics | `results/funnel.json` |
| Table 3 (NLL differences), Fig. 2, noise arms, pooling and dynamics ablations, kappa | `results/values.json` (`comm.*.paired`, `kappa`) |
| Table 4 (95% and Bonferroni intervals, seed 0) | `results/values.json` (`comm.*.paired.*.ci95`, `ci_bonf`) |
| Table 5 (fitted parameters, noise coefficients) | `results/seed*/results.json` (`communities.*.within.fits`, `noise_model`) |
| Table 6, Fig. 3 (coverage) | `results/values.json` (`conf_across`) |
| Table 7 (Gaussian and static conformal coverage by gap) | `results/diagnostics.json` (`comm.*.across.gap`) |
| Table 9 (predicted variance against realised error by noise arm), calibration at 50/80/90/95% | `results/diagnostics.json` (`variance`, `calibration`) |
| Table 10 (first and second half of the observation window) | `results/diagnostics.json` (`halves`) |
| Table 11 (exploratory learned baselines, ridge and gradient boosting) | `results/learned_baselines.json` |
| Fig. 4 (posterior shrinkage), Section 6.6 | `results/shrinkage.json` |
| Section 6.3 author-disjoint calibration | `results/conformal_heldout.json` |
| Section 6.1 kappa profile likelihood and multi-start check | `results/kappa_profile.json` |
| Identifiability comparison (full, near random walk, static NLL) | `results/seed*/results.json` (`within.summary`) |
| Section 6.4 strata | `results/values.json` (`strata`) |
| Section 6.5 (reply association, plain scorer) | `results/values.json` (`e1`, `e1_plain`, `comm.*.plain`) |
| Scorer F1, CC, ST | `results/scorer_retrain_log.txt` |

Conditions: `within` fits all parameters on training authors of the held-out community; `across` fits them on the same number of authors from the other three communities.

## Scope

The analyses reported in the paper are the ones listed above, including the exploratory learned-baseline comparison (Table 11). Table 12 of the paper (published work) is quoted from the cited sources and is not recomputed.
