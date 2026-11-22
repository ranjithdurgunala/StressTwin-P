# StressTwin-P results (auto-generated; check the data source and the pilot setting in results.json before reading)

## held-out community: anxiety  (train authors 768)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.532 | 8.616 | 2.491 | 0.90 | 9.53 |
| twin[conf_rule] | 10.633 | 10.635 | 3.210 | 0.89 | 13.22 |
| twin[split_half] | 8.879 | 9.281 | 2.455 | 0.90 | 9.42 |
| twin[split_half/static] | 9.009 | 9.547 | 2.460 | 0.90 | 9.52 |
| twin[split_half/rw] | 9.008 | 9.549 | 2.460 | 0.90 | 9.52 |
| twin[split_half/nopool] | 9.938 | 10.085 | 2.510 | 0.90 | 9.99 |
| author_mean | 9.911 | 9.911 | 2.566 | 0.90 | 10.32 |
| last | 15.094 | 15.094 | 2.776 | 0.90 | 12.74 |
| ewma | 10.346 | 10.346 | 2.587 | 0.90 | 10.53 |
| gap_ewma | 9.913 | 9.913 | 2.566 | 0.90 | 10.31 |
| global_mean | 9.464 | 9.452 | 2.543 | 0.90 | 9.97 |
| shortcut | 6.996 | 7.004 | 2.392 | 0.90 | 8.63 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.53 | 0.90 / 9.47 | 0.90 / 9.66 |
| twin[conf_rule] | 0.89 / 13.22 | 0.89 / 13.13 | 0.90 / 14.79 |
| twin[split_half] | 0.90 / 9.42 | 0.90 / 9.37 | 0.90 / 9.34 |
| twin[split_half/static] | 0.90 / 9.52 | 0.90 / 9.42 | 0.90 / 9.43 |
| twin[split_half/rw] | 0.90 / 9.52 | 0.90 / 9.43 | 0.90 / 9.43 |
| twin[split_half/nopool] | 0.90 / 9.99 | 0.90 / 10.03 | 0.90 / 10.04 |

## held-out community: bipolar  (train authors 637)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.106 | 8.375 | 2.465 | 0.90 | 9.19 |
| twin[conf_rule] | 10.311 | 11.313 | 3.122 | 0.89 | 12.85 |
| twin[split_half] | 8.493 | 8.926 | 2.446 | 0.90 | 9.33 |
| twin[split_half/static] | 8.644 | 9.098 | 2.460 | 0.90 | 9.63 |
| twin[split_half/rw] | 8.622 | 9.073 | 2.459 | 0.91 | 9.62 |
| twin[split_half/nopool] | 9.106 | 9.076 | 2.480 | 0.90 | 9.62 |
| author_mean | 8.914 | 8.914 | 2.513 | 0.90 | 9.77 |
| last | 14.508 | 14.508 | 2.756 | 0.90 | 12.40 |
| ewma | 9.305 | 9.423 | 2.534 | 0.90 | 9.95 |
| gap_ewma | 8.903 | 8.903 | 2.512 | 0.90 | 9.76 |
| global_mean | 8.808 | 9.993 | 2.507 | 0.90 | 9.69 |
| shortcut | 6.829 | 7.378 | 2.380 | 0.90 | 8.51 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.19 | 0.90 / 9.21 | 0.90 / 9.37 |
| twin[conf_rule] | 0.89 / 12.85 | 0.88 / 12.50 | 0.90 / 14.28 |
| twin[split_half] | 0.90 / 9.33 | 0.90 / 9.28 | 0.90 / 9.34 |
| twin[split_half/static] | 0.90 / 9.63 | 0.90 / 9.48 | 0.90 / 9.62 |
| twin[split_half/rw] | 0.91 / 9.62 | 0.90 / 9.49 | 0.90 / 9.61 |
| twin[split_half/nopool] | 0.90 / 9.62 | 0.90 / 9.56 | 0.90 / 9.76 |

## held-out community: depression  (train authors 1500)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.339 | 8.292 | 2.479 | 0.90 | 9.46 |
| twin[conf_rule] | 10.315 | 10.462 | 3.047 | 0.90 | 14.35 |
| twin[split_half] | 8.797 | 8.607 | 2.452 | 0.90 | 9.43 |
| twin[split_half/static] | 9.062 | 8.830 | 2.466 | 0.91 | 9.65 |
| twin[split_half/rw] | 9.056 | 8.825 | 2.466 | 0.91 | 9.65 |
| twin[split_half/nopool] | 9.668 | 9.621 | 2.500 | 0.90 | 9.85 |
| author_mean | 9.575 | 9.575 | 2.549 | 0.90 | 10.15 |
| last | 14.210 | 14.210 | 2.746 | 0.90 | 12.45 |
| ewma | 9.853 | 9.853 | 2.563 | 0.90 | 10.31 |
| gap_ewma | 9.533 | 9.533 | 2.546 | 0.90 | 10.14 |
| global_mean | 9.623 | 9.592 | 2.551 | 0.90 | 10.10 |
| shortcut | 7.230 | 7.238 | 2.408 | 0.90 | 8.83 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.46 | 0.90 / 9.44 | 0.90 / 9.48 |
| twin[conf_rule] | 0.90 / 14.35 | 0.90 / 13.99 | 0.90 / 14.76 |
| twin[split_half] | 0.90 / 9.43 | 0.90 / 9.33 | 0.90 / 9.41 |
| twin[split_half/static] | 0.91 / 9.65 | 0.90 / 9.44 | 0.90 / 9.62 |
| twin[split_half/rw] | 0.91 / 9.65 | 0.90 / 9.44 | 0.90 / 9.61 |
| twin[split_half/nopool] | 0.90 / 9.85 | 0.90 / 9.78 | 0.90 / 9.93 |

## held-out community: suicidewatch  (train authors 613)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.278 | 8.213 | 2.475 | 0.91 | 9.44 |
| twin[conf_rule] | 10.738 | 10.805 | 3.074 | 0.90 | 16.08 |
| twin[split_half] | 8.900 | 8.687 | 2.469 | 0.91 | 9.63 |
| twin[split_half/static] | 9.154 | 8.854 | 2.488 | 0.90 | 9.93 |
| twin[split_half/rw] | 9.150 | 8.852 | 2.488 | 0.90 | 9.92 |
| twin[split_half/nopool] | 9.636 | 9.659 | 2.510 | 0.90 | 9.97 |
| author_mean | 9.362 | 9.362 | 2.537 | 0.90 | 10.13 |
| last | 14.102 | 14.102 | 2.742 | 0.90 | 12.36 |
| ewma | 9.627 | 9.627 | 2.551 | 0.91 | 10.34 |
| gap_ewma | 9.308 | 9.308 | 2.534 | 0.90 | 10.11 |
| global_mean | 9.209 | 9.155 | 2.529 | 0.90 | 9.92 |
| shortcut | 7.159 | 7.149 | 2.403 | 0.90 | 8.81 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.91 / 9.44 | 0.90 / 9.24 | 0.90 / 9.35 |
| twin[conf_rule] | 0.90 / 16.08 | 0.89 / 14.97 | 0.90 / 16.55 |
| twin[split_half] | 0.91 / 9.63 | 0.90 / 9.48 | 0.90 / 9.55 |
| twin[split_half/static] | 0.90 / 9.93 | 0.89 / 9.68 | 0.90 / 9.88 |
| twin[split_half/rw] | 0.90 / 9.92 | 0.89 / 9.67 | 0.90 / 9.84 |
| twin[split_half/nopool] | 0.90 / 9.97 | 0.90 / 9.88 | 0.90 / 9.97 |


## Twin vs baselines, paired difference with 95% author-bootstrap CI (negative = twin better)
| community | comparator | metric | diff | 95% CI | authors | min detectable (80% power) |
|---|---|---|---|---|---|---|
| anxiety | author_mean | se | -1.032 | [-1.196, -0.851] | 769 | 0.250 |
| anxiety | author_mean | nll | -0.111 | [-0.122, -0.100] | 769 | 0.015 |
| anxiety | ewma | se | -1.467 | [-1.641, -1.268] | 769 | 0.269 |
| anxiety | ewma | nll | -0.133 | [-0.142, -0.122] | 769 | 0.015 |
| anxiety | gap_ewma | se | -1.034 | [-1.195, -0.852] | 769 | 0.249 |
| anxiety | gap_ewma | nll | -0.111 | [-0.122, -0.101] | 769 | 0.015 |
| anxiety | last | se | -6.215 | [-6.705, -5.731] | 769 | 0.691 |
| anxiety | last | nll | -0.322 | [-0.337, -0.307] | 769 | 0.022 |
| anxiety | global_mean | se | -0.585 | [-0.802, -0.381] | 769 | 0.302 |
| anxiety | global_mean | nll | -0.088 | [-0.101, -0.076] | 769 | 0.018 |
| anxiety | shortcut | se | 1.883 | [1.629, 2.150] | 769 | 0.378 |
| anxiety | shortcut | nll | 0.063 | [0.048, 0.077] | 769 | 0.022 |
| anxiety | twin[fixed] | se | 0.347 | [0.282, 0.420] | 769 | 0.097 |
| anxiety | twin[fixed] | nll | -0.037 | [-0.043, -0.030] | 769 | 0.009 |
| anxiety | twin[conf_rule] | se | -1.754 | [-2.083, -1.458] | 769 | 0.441 |
| anxiety | twin[conf_rule] | nll | -0.755 | [-0.927, -0.620] | 769 | 0.220 |
| anxiety | twin[split_half/static] | se | -0.130 | [-0.193, -0.075] | 769 | 0.084 |
| anxiety | twin[split_half/static] | nll | -0.005 | [-0.008, -0.002] | 769 | 0.004 |
| anxiety | twin[split_half/rw] | se | -0.129 | [-0.191, -0.074] | 769 | 0.084 |
| anxiety | twin[split_half/rw] | nll | -0.005 | [-0.008, -0.002] | 769 | 0.004 |
| anxiety | twin[split_half/nopool] | se | -1.059 | [-1.220, -0.889] | 769 | 0.239 |
| anxiety | twin[split_half/nopool] | nll | -0.055 | [-0.062, -0.048] | 769 | 0.010 |
| bipolar | author_mean | se | -0.422 | [-0.674, -0.139] | 638 | 0.404 |
| bipolar | author_mean | nll | -0.067 | [-0.083, -0.048] | 638 | 0.026 |
| bipolar | ewma | se | -0.813 | [-1.028, -0.617] | 638 | 0.299 |
| bipolar | ewma | nll | -0.088 | [-0.102, -0.075] | 638 | 0.020 |
| bipolar | gap_ewma | se | -0.411 | [-0.668, -0.128] | 638 | 0.410 |
| bipolar | gap_ewma | nll | -0.066 | [-0.083, -0.048] | 638 | 0.026 |
| bipolar | last | se | -6.015 | [-6.511, -5.530] | 638 | 0.742 |
| bipolar | last | nll | -0.310 | [-0.322, -0.298] | 638 | 0.017 |
| bipolar | global_mean | se | -0.316 | [-0.538, -0.102] | 638 | 0.305 |
| bipolar | global_mean | nll | -0.061 | [-0.074, -0.048] | 638 | 0.019 |
| bipolar | shortcut | se | 1.663 | [1.379, 1.950] | 638 | 0.411 |
| bipolar | shortcut | nll | 0.067 | [0.048, 0.084] | 638 | 0.026 |
| bipolar | twin[fixed] | se | 0.386 | [0.302, 0.477] | 638 | 0.130 |
| bipolar | twin[fixed] | nll | -0.019 | [-0.025, -0.013] | 638 | 0.009 |
| bipolar | twin[conf_rule] | se | -1.818 | [-2.334, -1.399] | 638 | 0.736 |
| bipolar | twin[conf_rule] | nll | -0.676 | [-0.796, -0.560] | 638 | 0.179 |
| bipolar | twin[split_half/static] | se | -0.151 | [-0.210, -0.100] | 638 | 0.080 |
| bipolar | twin[split_half/static] | nll | -0.014 | [-0.020, -0.007] | 638 | 0.009 |
| bipolar | twin[split_half/rw] | se | -0.129 | [-0.199, -0.068] | 638 | 0.089 |
| bipolar | twin[split_half/rw] | nll | -0.013 | [-0.019, -0.007] | 638 | 0.009 |
| bipolar | twin[split_half/nopool] | se | -0.614 | [-0.764, -0.472] | 638 | 0.209 |
| bipolar | twin[split_half/nopool] | nll | -0.034 | [-0.041, -0.027] | 638 | 0.010 |
| depression | author_mean | se | -0.778 | [-0.874, -0.685] | 2172 | 0.137 |
| depression | author_mean | nll | -0.096 | [-0.103, -0.090] | 2172 | 0.009 |
| depression | ewma | se | -1.056 | [-1.176, -0.936] | 2172 | 0.170 |
| depression | ewma | nll | -0.111 | [-0.118, -0.103] | 2172 | 0.010 |
| depression | gap_ewma | se | -0.736 | [-0.834, -0.640] | 2172 | 0.139 |
| depression | gap_ewma | nll | -0.094 | [-0.101, -0.088] | 2172 | 0.009 |
| depression | last | se | -5.413 | [-5.665, -5.160] | 2172 | 0.356 |
| depression | last | nll | -0.294 | [-0.302, -0.285] | 2172 | 0.012 |
| depression | global_mean | se | -0.826 | [-1.207, -0.543] | 2172 | 0.459 |
| depression | global_mean | nll | -0.099 | [-0.118, -0.084] | 2172 | 0.025 |
| depression | shortcut | se | 1.568 | [1.396, 1.720] | 2172 | 0.232 |
| depression | shortcut | nll | 0.044 | [0.036, 0.053] | 2172 | 0.013 |
| depression | twin[fixed] | se | 0.458 | [0.407, 0.510] | 2172 | 0.075 |
| depression | twin[fixed] | nll | -0.027 | [-0.031, -0.022] | 2172 | 0.006 |
| depression | twin[conf_rule] | se | -1.518 | [-1.741, -1.334] | 2172 | 0.283 |
| depression | twin[conf_rule] | nll | -0.595 | [-0.644, -0.550] | 2172 | 0.068 |
| depression | twin[split_half/static] | se | -0.265 | [-0.356, -0.190] | 2172 | 0.118 |
| depression | twin[split_half/static] | nll | -0.014 | [-0.017, -0.011] | 2172 | 0.005 |
| depression | twin[split_half/rw] | se | -0.259 | [-0.349, -0.187] | 2172 | 0.115 |
| depression | twin[split_half/rw] | nll | -0.014 | [-0.017, -0.011] | 2172 | 0.004 |
| depression | twin[split_half/nopool] | se | -0.871 | [-0.957, -0.788] | 2172 | 0.123 |
| depression | twin[split_half/nopool] | nll | -0.048 | [-0.052, -0.044] | 2172 | 0.006 |
| suicidewatch | author_mean | se | -0.462 | [-0.622, -0.319] | 614 | 0.222 |
| suicidewatch | author_mean | nll | -0.068 | [-0.086, -0.050] | 614 | 0.026 |
| suicidewatch | ewma | se | -0.726 | [-0.896, -0.583] | 614 | 0.223 |
| suicidewatch | ewma | nll | -0.082 | [-0.099, -0.067] | 614 | 0.023 |
| suicidewatch | gap_ewma | se | -0.408 | [-0.565, -0.270] | 614 | 0.217 |
| suicidewatch | gap_ewma | nll | -0.065 | [-0.083, -0.048] | 614 | 0.025 |
| suicidewatch | last | se | -5.202 | [-5.530, -4.877] | 614 | 0.470 |
| suicidewatch | last | nll | -0.273 | [-0.289, -0.258] | 614 | 0.022 |
| suicidewatch | global_mean | se | -0.308 | [-0.659, 0.051] | 614 | 0.519 |
| suicidewatch | global_mean | nll | -0.060 | [-0.073, -0.045] | 614 | 0.020 |
| suicidewatch | shortcut | se | 1.741 | [1.470, 2.069] | 614 | 0.426 |
| suicidewatch | shortcut | nll | 0.066 | [0.045, 0.087] | 614 | 0.028 |
| suicidewatch | twin[fixed] | se | 0.622 | [0.537, 0.725] | 614 | 0.132 |
| suicidewatch | twin[fixed] | nll | -0.006 | [-0.018, 0.008] | 614 | 0.018 |
| suicidewatch | twin[conf_rule] | se | -1.838 | [-2.173, -1.506] | 614 | 0.468 |
| suicidewatch | twin[conf_rule] | nll | -0.605 | [-0.677, -0.545] | 614 | 0.098 |
| suicidewatch | twin[split_half/static] | se | -0.254 | [-0.363, -0.156] | 614 | 0.148 |
| suicidewatch | twin[split_half/static] | nll | -0.019 | [-0.025, -0.012] | 614 | 0.009 |
| suicidewatch | twin[split_half/rw] | se | -0.250 | [-0.353, -0.158] | 614 | 0.141 |
| suicidewatch | twin[split_half/rw] | nll | -0.018 | [-0.024, -0.012] | 614 | 0.009 |
| suicidewatch | twin[split_half/nopool] | se | -0.735 | [-0.903, -0.585] | 614 | 0.223 |
| suicidewatch | twin[split_half/nopool] | nll | -0.041 | [-0.049, -0.034] | 614 | 0.011 |

## E1 reply dose-response
beta=-0.2350 (p=7.48e-173); placebo beta=-0.0423; Gate A pass: True