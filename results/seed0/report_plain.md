# StressTwin-P results (auto-generated; check the data source and the pilot setting in results.json before reading)

## held-out community: anxiety  (train authors 768)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.388 | 8.482 | 2.482 | 0.91 | 9.61 |
| twin[conf_rule] | 10.180 | 10.187 | 3.030 | 0.91 | 14.84 |
| twin[split_half] | 8.730 | 9.184 | 2.445 | 0.91 | 9.42 |
| twin[split_half/static] | 8.836 | 9.413 | 2.449 | 0.91 | 9.52 |
| twin[split_half/rw] | 8.835 | 9.413 | 2.449 | 0.91 | 9.52 |
| twin[split_half/nopool] | 9.928 | 10.106 | 2.508 | 0.90 | 9.99 |
| author_mean | 9.902 | 9.902 | 2.565 | 0.90 | 10.32 |
| last | 14.780 | 14.780 | 2.766 | 0.90 | 12.86 |
| ewma | 10.254 | 10.254 | 2.583 | 0.90 | 10.58 |
| gap_ewma | 9.888 | 9.888 | 2.565 | 0.90 | 10.32 |
| global_mean | 9.155 | 9.157 | 2.526 | 0.91 | 10.12 |
| shortcut | 6.791 | 6.862 | 2.377 | 0.91 | 8.75 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.91 / 9.61 | 0.91 / 9.63 | 0.90 / 9.53 |
| twin[conf_rule] | 0.91 / 14.84 | 0.90 / 14.18 | 0.90 / 14.40 |
| twin[split_half] | 0.91 / 9.42 | 0.91 / 9.38 | 0.90 / 9.30 |
| twin[split_half/static] | 0.91 / 9.52 | 0.91 / 9.47 | 0.90 / 9.34 |
| twin[split_half/rw] | 0.91 / 9.52 | 0.91 / 9.48 | 0.90 / 9.34 |
| twin[split_half/nopool] | 0.90 / 9.99 | 0.90 / 10.02 | 0.90 / 10.01 |

## held-out community: bipolar  (train authors 637)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.082 | 8.384 | 2.463 | 0.90 | 9.22 |
| twin[conf_rule] | 10.028 | 10.574 | 3.027 | 0.91 | 14.06 |
| twin[split_half] | 8.357 | 8.976 | 2.441 | 0.90 | 9.30 |
| twin[split_half/static] | 8.490 | 9.164 | 2.455 | 0.90 | 9.54 |
| twin[split_half/rw] | 8.489 | 9.160 | 2.455 | 0.90 | 9.54 |
| twin[split_half/nopool] | 9.033 | 9.098 | 2.478 | 0.90 | 9.61 |
| author_mean | 8.967 | 8.967 | 2.516 | 0.89 | 9.75 |
| last | 14.453 | 14.453 | 2.754 | 0.90 | 12.44 |
| ewma | 9.316 | 9.417 | 2.535 | 0.90 | 9.96 |
| gap_ewma | 8.961 | 8.961 | 2.515 | 0.89 | 9.74 |
| global_mean | 8.806 | 9.611 | 2.507 | 0.90 | 9.67 |
| shortcut | 6.780 | 6.794 | 2.376 | 0.90 | 8.55 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.22 | 0.90 / 9.22 | 0.90 / 9.42 |
| twin[conf_rule] | 0.91 / 14.06 | 0.91 / 13.96 | 0.90 / 13.88 |
| twin[split_half] | 0.90 / 9.30 | 0.90 / 9.24 | 0.90 / 9.35 |
| twin[split_half/static] | 0.90 / 9.54 | 0.90 / 9.35 | 0.90 / 9.60 |
| twin[split_half/rw] | 0.90 / 9.54 | 0.90 / 9.35 | 0.90 / 9.58 |
| twin[split_half/nopool] | 0.90 / 9.61 | 0.90 / 9.60 | 0.90 / 9.70 |

## held-out community: depression  (train authors 1500)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.347 | 8.306 | 2.480 | 0.90 | 9.51 |
| twin[conf_rule] | 10.252 | 10.524 | 3.055 | 0.91 | 15.35 |
| twin[split_half] | 8.846 | 8.703 | 2.452 | 0.90 | 9.44 |
| twin[split_half/static] | 9.102 | 8.830 | 2.465 | 0.91 | 9.70 |
| twin[split_half/rw] | 9.098 | 8.829 | 2.465 | 0.91 | 9.69 |
| twin[split_half/nopool] | 9.713 | 9.672 | 2.502 | 0.90 | 9.90 |
| author_mean | 9.584 | 9.584 | 2.549 | 0.90 | 10.14 |
| last | 14.358 | 14.358 | 2.751 | 0.90 | 12.42 |
| ewma | 9.868 | 9.868 | 2.564 | 0.90 | 10.31 |
| gap_ewma | 9.551 | 9.551 | 2.547 | 0.90 | 10.12 |
| global_mean | 9.505 | 9.600 | 2.545 | 0.90 | 10.11 |
| shortcut | 7.294 | 7.300 | 2.413 | 0.90 | 8.84 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.51 | 0.90 / 9.43 | 0.90 / 9.45 |
| twin[conf_rule] | 0.91 / 15.35 | 0.91 / 14.94 | 0.90 / 14.83 |
| twin[split_half] | 0.90 / 9.44 | 0.90 / 9.33 | 0.90 / 9.36 |
| twin[split_half/static] | 0.91 / 9.70 | 0.90 / 9.52 | 0.90 / 9.57 |
| twin[split_half/rw] | 0.91 / 9.69 | 0.90 / 9.51 | 0.90 / 9.57 |
| twin[split_half/nopool] | 0.90 / 9.90 | 0.90 / 9.88 | 0.90 / 9.85 |

## held-out community: suicidewatch  (train authors 613)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.596 | 8.511 | 2.495 | 0.90 | 9.33 |
| twin[conf_rule] | 10.992 | 11.097 | 3.108 | 0.91 | 16.51 |
| twin[split_half] | 9.009 | 8.854 | 2.477 | 0.90 | 9.35 |
| twin[split_half/static] | 9.180 | 8.982 | 2.488 | 0.89 | 9.50 |
| twin[split_half/rw] | 9.174 | 8.978 | 2.488 | 0.89 | 9.50 |
| twin[split_half/nopool] | 9.910 | 10.003 | 2.522 | 0.90 | 9.76 |
| author_mean | 9.807 | 9.807 | 2.562 | 0.89 | 9.89 |
| last | 14.512 | 14.512 | 2.757 | 0.89 | 12.19 |
| ewma | 10.145 | 10.145 | 2.579 | 0.89 | 10.06 |
| gap_ewma | 9.764 | 9.764 | 2.560 | 0.89 | 9.87 |
| global_mean | 9.425 | 9.468 | 2.542 | 0.89 | 9.76 |
| shortcut | 7.488 | 7.496 | 2.428 | 0.89 | 8.60 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.33 | 0.89 / 9.12 | 0.90 / 9.55 |
| twin[conf_rule] | 0.91 / 16.51 | 0.90 / 15.92 | 0.90 / 16.02 |
| twin[split_half] | 0.90 / 9.35 | 0.89 / 9.13 | 0.90 / 9.55 |
| twin[split_half/static] | 0.89 / 9.50 | 0.88 / 9.25 | 0.90 / 9.77 |
| twin[split_half/rw] | 0.89 / 9.50 | 0.88 / 9.26 | 0.90 / 9.76 |
| twin[split_half/nopool] | 0.90 / 9.76 | 0.89 / 9.69 | 0.90 / 10.01 |


## Twin vs baselines, paired difference with 95% author-bootstrap CI (negative = twin better)
| community | comparator | metric | diff | 95% CI | authors | min detectable (80% power) |
|---|---|---|---|---|---|---|
| anxiety | author_mean | se | -1.172 | [-1.347, -1.024] | 769 | 0.233 |
| anxiety | author_mean | nll | -0.120 | [-0.131, -0.111] | 769 | 0.015 |
| anxiety | ewma | se | -1.524 | [-1.718, -1.351] | 769 | 0.270 |
| anxiety | ewma | nll | -0.138 | [-0.149, -0.128] | 769 | 0.016 |
| anxiety | gap_ewma | se | -1.158 | [-1.326, -1.010] | 769 | 0.231 |
| anxiety | gap_ewma | nll | -0.120 | [-0.130, -0.110] | 769 | 0.015 |
| anxiety | last | se | -6.050 | [-6.522, -5.613] | 769 | 0.630 |
| anxiety | last | nll | -0.321 | [-0.334, -0.307] | 769 | 0.019 |
| anxiety | global_mean | se | -0.425 | [-0.607, -0.246] | 769 | 0.267 |
| anxiety | global_mean | nll | -0.081 | [-0.092, -0.070] | 769 | 0.016 |
| anxiety | shortcut | se | 1.939 | [1.677, 2.197] | 769 | 0.366 |
| anxiety | shortcut | nll | 0.068 | [0.053, 0.082] | 769 | 0.021 |
| anxiety | twin[fixed] | se | 0.341 | [0.285, 0.396] | 769 | 0.079 |
| anxiety | twin[fixed] | nll | -0.037 | [-0.044, -0.031] | 769 | 0.010 |
| anxiety | twin[conf_rule] | se | -1.450 | [-1.672, -1.227] | 769 | 0.318 |
| anxiety | twin[conf_rule] | nll | -0.585 | [-0.656, -0.517] | 769 | 0.102 |
| anxiety | twin[split_half/static] | se | -0.106 | [-0.157, -0.059] | 769 | 0.072 |
| anxiety | twin[split_half/static] | nll | -0.004 | [-0.006, -0.001] | 769 | 0.004 |
| anxiety | twin[split_half/rw] | se | -0.105 | [-0.155, -0.059] | 769 | 0.071 |
| anxiety | twin[split_half/rw] | nll | -0.004 | [-0.006, -0.001] | 769 | 0.004 |
| anxiety | twin[split_half/nopool] | se | -1.199 | [-1.366, -1.049] | 769 | 0.230 |
| anxiety | twin[split_half/nopool] | nll | -0.062 | [-0.069, -0.056] | 769 | 0.009 |
| bipolar | author_mean | se | -0.610 | [-0.733, -0.510] | 638 | 0.158 |
| bipolar | author_mean | nll | -0.075 | [-0.084, -0.068] | 638 | 0.011 |
| bipolar | ewma | se | -0.958 | [-1.103, -0.828] | 638 | 0.197 |
| bipolar | ewma | nll | -0.094 | [-0.104, -0.086] | 638 | 0.013 |
| bipolar | gap_ewma | se | -0.604 | [-0.721, -0.505] | 638 | 0.156 |
| bipolar | gap_ewma | nll | -0.075 | [-0.084, -0.068] | 638 | 0.011 |
| bipolar | last | se | -6.096 | [-6.401, -5.801] | 638 | 0.435 |
| bipolar | last | nll | -0.314 | [-0.324, -0.304] | 638 | 0.015 |
| bipolar | global_mean | se | -0.449 | [-0.664, -0.256] | 638 | 0.301 |
| bipolar | global_mean | nll | -0.066 | [-0.079, -0.055] | 638 | 0.018 |
| bipolar | shortcut | se | 1.577 | [1.371, 1.773] | 638 | 0.293 |
| bipolar | shortcut | nll | 0.065 | [0.052, 0.077] | 638 | 0.019 |
| bipolar | twin[fixed] | se | 0.275 | [0.229, 0.326] | 638 | 0.070 |
| bipolar | twin[fixed] | nll | -0.022 | [-0.028, -0.017] | 638 | 0.007 |
| bipolar | twin[conf_rule] | se | -1.671 | [-1.847, -1.488] | 638 | 0.258 |
| bipolar | twin[conf_rule] | nll | -0.587 | [-0.660, -0.526] | 638 | 0.098 |
| bipolar | twin[split_half/static] | se | -0.133 | [-0.188, -0.075] | 638 | 0.081 |
| bipolar | twin[split_half/static] | nll | -0.015 | [-0.019, -0.011] | 638 | 0.006 |
| bipolar | twin[split_half/rw] | se | -0.132 | [-0.185, -0.074] | 638 | 0.080 |
| bipolar | twin[split_half/rw] | nll | -0.014 | [-0.018, -0.011] | 638 | 0.006 |
| bipolar | twin[split_half/nopool] | se | -0.676 | [-0.796, -0.584] | 638 | 0.147 |
| bipolar | twin[split_half/nopool] | nll | -0.037 | [-0.042, -0.033] | 638 | 0.006 |
| depression | author_mean | se | -0.738 | [-0.834, -0.653] | 2172 | 0.131 |
| depression | author_mean | nll | -0.097 | [-0.103, -0.091] | 2172 | 0.008 |
| depression | ewma | se | -1.023 | [-1.129, -0.906] | 2172 | 0.160 |
| depression | ewma | nll | -0.112 | [-0.118, -0.105] | 2172 | 0.009 |
| depression | gap_ewma | se | -0.705 | [-0.801, -0.615] | 2172 | 0.133 |
| depression | gap_ewma | nll | -0.095 | [-0.102, -0.090] | 2172 | 0.008 |
| depression | last | se | -5.512 | [-5.768, -5.275] | 2172 | 0.357 |
| depression | last | nll | -0.299 | [-0.308, -0.291] | 2172 | 0.013 |
| depression | global_mean | se | -0.660 | [-0.895, -0.452] | 2172 | 0.316 |
| depression | global_mean | nll | -0.093 | [-0.106, -0.082] | 2172 | 0.018 |
| depression | shortcut | se | 1.551 | [1.400, 1.709] | 2172 | 0.225 |
| depression | shortcut | nll | 0.039 | [0.031, 0.048] | 2172 | 0.012 |
| depression | twin[fixed] | se | 0.498 | [0.444, 0.559] | 2172 | 0.082 |
| depression | twin[fixed] | nll | -0.028 | [-0.032, -0.024] | 2172 | 0.006 |
| depression | twin[conf_rule] | se | -1.406 | [-1.548, -1.253] | 2172 | 0.209 |
| depression | twin[conf_rule] | nll | -0.603 | [-0.669, -0.548] | 2172 | 0.085 |
| depression | twin[split_half/static] | se | -0.256 | [-0.357, -0.171] | 2172 | 0.133 |
| depression | twin[split_half/static] | nll | -0.013 | [-0.016, -0.010] | 2172 | 0.005 |
| depression | twin[split_half/rw] | se | -0.252 | [-0.352, -0.169] | 2172 | 0.131 |
| depression | twin[split_half/rw] | nll | -0.013 | [-0.016, -0.010] | 2172 | 0.005 |
| depression | twin[split_half/nopool] | se | -0.867 | [-0.951, -0.786] | 2172 | 0.118 |
| depression | twin[split_half/nopool] | nll | -0.050 | [-0.054, -0.046] | 2172 | 0.005 |
| suicidewatch | author_mean | se | -0.798 | [-0.970, -0.637] | 614 | 0.250 |
| suicidewatch | author_mean | nll | -0.085 | [-0.099, -0.072] | 614 | 0.020 |
| suicidewatch | ewma | se | -1.136 | [-1.322, -0.961] | 614 | 0.261 |
| suicidewatch | ewma | nll | -0.102 | [-0.116, -0.088] | 614 | 0.020 |
| suicidewatch | gap_ewma | se | -0.754 | [-0.927, -0.591] | 614 | 0.252 |
| suicidewatch | gap_ewma | nll | -0.083 | [-0.097, -0.069] | 614 | 0.020 |
| suicidewatch | last | se | -5.503 | [-5.872, -5.142] | 614 | 0.530 |
| suicidewatch | last | nll | -0.280 | [-0.293, -0.267] | 614 | 0.020 |
| suicidewatch | global_mean | se | -0.416 | [-0.676, -0.183] | 614 | 0.349 |
| suicidewatch | global_mean | nll | -0.065 | [-0.080, -0.052] | 614 | 0.021 |
| suicidewatch | shortcut | se | 1.521 | [1.246, 1.791] | 614 | 0.395 |
| suicidewatch | shortcut | nll | 0.049 | [0.032, 0.065] | 614 | 0.024 |
| suicidewatch | twin[fixed] | se | 0.413 | [0.353, 0.469] | 614 | 0.083 |
| suicidewatch | twin[fixed] | nll | -0.018 | [-0.028, -0.010] | 614 | 0.013 |
| suicidewatch | twin[conf_rule] | se | -1.982 | [-2.283, -1.664] | 614 | 0.444 |
| suicidewatch | twin[conf_rule] | nll | -0.631 | [-0.705, -0.568] | 614 | 0.099 |
| suicidewatch | twin[split_half/static] | se | -0.171 | [-0.250, -0.088] | 614 | 0.112 |
| suicidewatch | twin[split_half/static] | nll | -0.011 | [-0.016, -0.007] | 614 | 0.007 |
| suicidewatch | twin[split_half/rw] | se | -0.165 | [-0.239, -0.086] | 614 | 0.107 |
| suicidewatch | twin[split_half/rw] | nll | -0.011 | [-0.016, -0.006] | 614 | 0.007 |
| suicidewatch | twin[split_half/nopool] | se | -0.900 | [-1.068, -0.751] | 614 | 0.230 |
| suicidewatch | twin[split_half/nopool] | nll | -0.045 | [-0.053, -0.038] | 614 | 0.010 |

## E1 reply dose-response
beta=-0.2350 (p=7.48e-173); placebo beta=-0.0423; Gate A pass: True