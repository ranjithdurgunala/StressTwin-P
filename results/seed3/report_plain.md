# StressTwin-P results (auto-generated; check the data source and the pilot setting in results.json before reading)

## held-out community: anxiety  (train authors 768)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.537 | 8.623 | 2.492 | 0.90 | 9.51 |
| twin[conf_rule] | 10.470 | 10.465 | 3.153 | 0.90 | 13.94 |
| twin[split_half] | 8.955 | 9.292 | 2.451 | 0.90 | 9.46 |
| twin[split_half/static] | 9.089 | 9.569 | 2.458 | 0.91 | 9.57 |
| twin[split_half/rw] | 9.087 | 9.569 | 2.458 | 0.91 | 9.56 |
| twin[split_half/nopool] | 9.981 | 10.062 | 2.507 | 0.90 | 9.96 |
| author_mean | 9.861 | 9.861 | 2.563 | 0.90 | 10.35 |
| last | 15.071 | 15.071 | 2.775 | 0.90 | 12.75 |
| ewma | 10.279 | 10.279 | 2.584 | 0.90 | 10.57 |
| gap_ewma | 9.843 | 9.843 | 2.562 | 0.90 | 10.35 |
| global_mean | 9.423 | 9.487 | 2.541 | 0.90 | 9.95 |
| shortcut | 6.933 | 6.984 | 2.387 | 0.90 | 8.66 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.51 | 0.90 / 9.44 | 0.90 / 9.69 |
| twin[conf_rule] | 0.90 / 13.94 | 0.90 / 13.63 | 0.90 / 14.67 |
| twin[split_half] | 0.90 / 9.46 | 0.90 / 9.32 | 0.90 / 9.43 |
| twin[split_half/static] | 0.91 / 9.57 | 0.90 / 9.35 | 0.90 / 9.51 |
| twin[split_half/rw] | 0.91 / 9.56 | 0.89 / 9.35 | 0.90 / 9.51 |
| twin[split_half/nopool] | 0.90 / 9.96 | 0.90 / 9.90 | 0.90 / 10.10 |

## held-out community: bipolar  (train authors 637)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.061 | 8.275 | 2.462 | 0.90 | 9.25 |
| twin[conf_rule] | 10.393 | 11.249 | 3.109 | 0.89 | 13.11 |
| twin[split_half] | 8.446 | 8.967 | 2.444 | 0.90 | 9.37 |
| twin[split_half/static] | 8.566 | 9.154 | 2.455 | 0.91 | 9.68 |
| twin[split_half/rw] | 8.544 | 9.125 | 2.454 | 0.91 | 9.67 |
| twin[split_half/nopool] | 8.996 | 9.085 | 2.475 | 0.90 | 9.65 |
| author_mean | 8.779 | 8.779 | 2.505 | 0.91 | 9.87 |
| last | 14.467 | 14.467 | 2.755 | 0.90 | 12.42 |
| ewma | 9.160 | 9.314 | 2.526 | 0.91 | 10.06 |
| gap_ewma | 8.772 | 8.772 | 2.505 | 0.91 | 9.86 |
| global_mean | 8.860 | 9.890 | 2.510 | 0.90 | 9.66 |
| shortcut | 6.735 | 6.797 | 2.373 | 0.91 | 8.61 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.25 | 0.90 / 9.24 | 0.90 / 9.38 |
| twin[conf_rule] | 0.89 / 13.11 | 0.89 / 12.70 | 0.90 / 14.44 |
| twin[split_half] | 0.90 / 9.37 | 0.90 / 9.18 | 0.90 / 9.30 |
| twin[split_half/static] | 0.91 / 9.68 | 0.90 / 9.48 | 0.90 / 9.50 |
| twin[split_half/rw] | 0.91 / 9.67 | 0.90 / 9.48 | 0.90 / 9.52 |
| twin[split_half/nopool] | 0.90 / 9.65 | 0.90 / 9.55 | 0.90 / 9.63 |

## held-out community: depression  (train authors 1500)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.343 | 8.298 | 2.480 | 0.90 | 9.45 |
| twin[conf_rule] | 10.343 | 10.471 | 3.058 | 0.91 | 14.90 |
| twin[split_half] | 8.852 | 8.670 | 2.449 | 0.91 | 9.51 |
| twin[split_half/static] | 9.085 | 8.861 | 2.462 | 0.91 | 9.79 |
| twin[split_half/rw] | 9.081 | 8.857 | 2.461 | 0.91 | 9.78 |
| twin[split_half/nopool] | 9.715 | 9.682 | 2.497 | 0.91 | 9.96 |
| author_mean | 9.531 | 9.531 | 2.546 | 0.90 | 10.15 |
| last | 14.341 | 14.341 | 2.751 | 0.90 | 12.34 |
| ewma | 9.844 | 9.844 | 2.562 | 0.90 | 10.28 |
| gap_ewma | 9.491 | 9.491 | 2.544 | 0.90 | 10.13 |
| global_mean | 9.521 | 9.610 | 2.546 | 0.90 | 10.02 |
| shortcut | 7.263 | 7.299 | 2.410 | 0.90 | 8.81 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.45 | 0.90 / 9.40 | 0.90 / 9.46 |
| twin[conf_rule] | 0.91 / 14.90 | 0.90 / 14.41 | 0.90 / 14.48 |
| twin[split_half] | 0.91 / 9.51 | 0.90 / 9.39 | 0.90 / 9.37 |
| twin[split_half/static] | 0.91 / 9.79 | 0.90 / 9.59 | 0.90 / 9.56 |
| twin[split_half/rw] | 0.91 / 9.78 | 0.90 / 9.58 | 0.90 / 9.58 |
| twin[split_half/nopool] | 0.91 / 9.96 | 0.90 / 9.90 | 0.90 / 9.88 |

## held-out community: suicidewatch  (train authors 613)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.100 | 8.040 | 2.464 | 0.91 | 9.52 |
| twin[conf_rule] | 10.359 | 10.541 | 3.022 | 0.92 | 17.29 |
| twin[split_half] | 8.800 | 8.335 | 2.464 | 0.91 | 9.86 |
| twin[split_half/static] | 8.972 | 8.402 | 2.484 | 0.91 | 10.29 |
| twin[split_half/rw] | 8.976 | 8.404 | 2.484 | 0.91 | 10.28 |
| twin[split_half/nopool] | 9.603 | 9.460 | 2.508 | 0.91 | 10.24 |
| author_mean | 9.282 | 9.282 | 2.533 | 0.91 | 10.17 |
| last | 13.664 | 13.664 | 2.727 | 0.91 | 12.55 |
| ewma | 9.603 | 9.603 | 2.550 | 0.91 | 10.34 |
| gap_ewma | 9.243 | 9.243 | 2.531 | 0.91 | 10.14 |
| global_mean | 9.036 | 9.037 | 2.520 | 0.90 | 9.98 |
| shortcut | 6.985 | 7.000 | 2.391 | 0.91 | 8.91 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.91 / 9.52 | 0.91 / 9.36 | 0.90 / 9.28 |
| twin[conf_rule] | 0.92 / 17.29 | 0.91 / 16.67 | 0.90 / 16.09 |
| twin[split_half] | 0.91 / 9.86 | 0.91 / 9.73 | 0.90 / 9.63 |
| twin[split_half/static] | 0.91 / 10.29 | 0.91 / 10.10 | 0.90 / 9.94 |
| twin[split_half/rw] | 0.91 / 10.28 | 0.91 / 10.09 | 0.90 / 9.93 |
| twin[split_half/nopool] | 0.91 / 10.24 | 0.91 / 10.17 | 0.90 / 10.03 |


## Twin vs baselines, paired difference with 95% author-bootstrap CI (negative = twin better)
| community | comparator | metric | diff | 95% CI | authors | min detectable (80% power) |
|---|---|---|---|---|---|---|
| anxiety | author_mean | se | -0.906 | [-1.062, -0.742] | 769 | 0.231 |
| anxiety | author_mean | nll | -0.112 | [-0.123, -0.101] | 769 | 0.016 |
| anxiety | ewma | se | -1.324 | [-1.495, -1.152] | 769 | 0.247 |
| anxiety | ewma | nll | -0.133 | [-0.143, -0.123] | 769 | 0.015 |
| anxiety | gap_ewma | se | -0.889 | [-1.048, -0.727] | 769 | 0.230 |
| anxiety | gap_ewma | nll | -0.111 | [-0.122, -0.100] | 769 | 0.016 |
| anxiety | last | se | -6.117 | [-6.554, -5.703] | 769 | 0.606 |
| anxiety | last | nll | -0.324 | [-0.338, -0.311] | 769 | 0.019 |
| anxiety | global_mean | se | -0.468 | [-0.701, -0.240] | 769 | 0.319 |
| anxiety | global_mean | nll | -0.089 | [-0.104, -0.076] | 769 | 0.020 |
| anxiety | shortcut | se | 2.022 | [1.721, 2.276] | 769 | 0.392 |
| anxiety | shortcut | nll | 0.064 | [0.048, 0.079] | 769 | 0.022 |
| anxiety | twin[fixed] | se | 0.418 | [0.349, 0.492] | 769 | 0.106 |
| anxiety | twin[fixed] | nll | -0.040 | [-0.048, -0.033] | 769 | 0.011 |
| anxiety | twin[conf_rule] | se | -1.515 | [-1.840, -1.245] | 769 | 0.422 |
| anxiety | twin[conf_rule] | nll | -0.702 | [-0.867, -0.581] | 769 | 0.206 |
| anxiety | twin[split_half/static] | se | -0.134 | [-0.193, -0.078] | 769 | 0.081 |
| anxiety | twin[split_half/static] | nll | -0.006 | [-0.009, -0.004] | 769 | 0.004 |
| anxiety | twin[split_half/rw] | se | -0.133 | [-0.192, -0.078] | 769 | 0.080 |
| anxiety | twin[split_half/rw] | nll | -0.006 | [-0.009, -0.003] | 769 | 0.004 |
| anxiety | twin[split_half/nopool] | se | -1.027 | [-1.176, -0.877] | 769 | 0.212 |
| anxiety | twin[split_half/nopool] | nll | -0.055 | [-0.062, -0.048] | 769 | 0.010 |
| bipolar | author_mean | se | -0.333 | [-0.564, -0.079] | 638 | 0.372 |
| bipolar | author_mean | nll | -0.062 | [-0.078, -0.045] | 638 | 0.025 |
| bipolar | ewma | se | -0.714 | [-0.905, -0.534] | 638 | 0.263 |
| bipolar | ewma | nll | -0.083 | [-0.096, -0.070] | 638 | 0.019 |
| bipolar | gap_ewma | se | -0.326 | [-0.557, -0.062] | 638 | 0.379 |
| bipolar | gap_ewma | nll | -0.061 | [-0.077, -0.044] | 638 | 0.025 |
| bipolar | last | se | -6.021 | [-6.518, -5.558] | 638 | 0.711 |
| bipolar | last | nll | -0.311 | [-0.322, -0.300] | 638 | 0.016 |
| bipolar | global_mean | se | -0.414 | [-0.661, -0.188] | 638 | 0.339 |
| bipolar | global_mean | nll | -0.066 | [-0.081, -0.052] | 638 | 0.021 |
| bipolar | shortcut | se | 1.710 | [1.448, 1.966] | 638 | 0.361 |
| bipolar | shortcut | nll | 0.071 | [0.055, 0.085] | 638 | 0.022 |
| bipolar | twin[fixed] | se | 0.385 | [0.310, 0.466] | 638 | 0.116 |
| bipolar | twin[fixed] | nll | -0.018 | [-0.025, -0.012] | 638 | 0.009 |
| bipolar | twin[conf_rule] | se | -1.947 | [-2.471, -1.522] | 638 | 0.748 |
| bipolar | twin[conf_rule] | nll | -0.665 | [-0.778, -0.560] | 638 | 0.164 |
| bipolar | twin[split_half/static] | se | -0.120 | [-0.178, -0.065] | 638 | 0.080 |
| bipolar | twin[split_half/static] | nll | -0.011 | [-0.018, -0.005] | 638 | 0.010 |
| bipolar | twin[split_half/rw] | se | -0.099 | [-0.166, -0.042] | 638 | 0.089 |
| bipolar | twin[split_half/rw] | nll | -0.011 | [-0.017, -0.004] | 638 | 0.010 |
| bipolar | twin[split_half/nopool] | se | -0.550 | [-0.692, -0.421] | 638 | 0.190 |
| bipolar | twin[split_half/nopool] | nll | -0.032 | [-0.039, -0.025] | 638 | 0.010 |
| depression | author_mean | se | -0.679 | [-0.778, -0.584] | 2172 | 0.140 |
| depression | author_mean | nll | -0.097 | [-0.103, -0.091] | 2172 | 0.009 |
| depression | ewma | se | -0.992 | [-1.114, -0.872] | 2172 | 0.170 |
| depression | ewma | nll | -0.113 | [-0.120, -0.106] | 2172 | 0.010 |
| depression | gap_ewma | se | -0.639 | [-0.742, -0.541] | 2172 | 0.143 |
| depression | gap_ewma | nll | -0.095 | [-0.101, -0.088] | 2172 | 0.009 |
| depression | last | se | -5.489 | [-5.734, -5.229] | 2172 | 0.364 |
| depression | last | nll | -0.301 | [-0.311, -0.291] | 2172 | 0.013 |
| depression | global_mean | se | -0.669 | [-0.978, -0.404] | 2172 | 0.433 |
| depression | global_mean | nll | -0.097 | [-0.113, -0.082] | 2172 | 0.024 |
| depression | shortcut | se | 1.589 | [1.419, 1.768] | 2172 | 0.249 |
| depression | shortcut | nll | 0.039 | [0.029, 0.049] | 2172 | 0.014 |
| depression | twin[fixed] | se | 0.509 | [0.452, 0.571] | 2172 | 0.085 |
| depression | twin[fixed] | nll | -0.030 | [-0.035, -0.025] | 2172 | 0.007 |
| depression | twin[conf_rule] | se | -1.490 | [-1.692, -1.302] | 2172 | 0.274 |
| depression | twin[conf_rule] | nll | -0.608 | [-0.673, -0.556] | 2172 | 0.085 |
| depression | twin[split_half/static] | se | -0.233 | [-0.344, -0.155] | 2172 | 0.133 |
| depression | twin[split_half/static] | nll | -0.012 | [-0.016, -0.009] | 2172 | 0.005 |
| depression | twin[split_half/rw] | se | -0.228 | [-0.336, -0.151] | 2172 | 0.130 |
| depression | twin[split_half/rw] | nll | -0.012 | [-0.016, -0.009] | 2172 | 0.005 |
| depression | twin[split_half/nopool] | se | -0.863 | [-0.948, -0.780] | 2172 | 0.119 |
| depression | twin[split_half/nopool] | nll | -0.048 | [-0.052, -0.044] | 2172 | 0.005 |
| suicidewatch | author_mean | se | -0.482 | [-0.666, -0.313] | 614 | 0.249 |
| suicidewatch | author_mean | nll | -0.069 | [-0.088, -0.047] | 614 | 0.029 |
| suicidewatch | ewma | se | -0.803 | [-0.979, -0.649] | 614 | 0.246 |
| suicidewatch | ewma | nll | -0.086 | [-0.104, -0.069] | 614 | 0.026 |
| suicidewatch | gap_ewma | se | -0.444 | [-0.620, -0.280] | 614 | 0.243 |
| suicidewatch | gap_ewma | nll | -0.067 | [-0.086, -0.045] | 614 | 0.029 |
| suicidewatch | last | se | -4.865 | [-5.199, -4.516] | 614 | 0.493 |
| suicidewatch | last | nll | -0.263 | [-0.279, -0.248] | 614 | 0.022 |
| suicidewatch | global_mean | se | -0.236 | [-0.604, 0.141] | 614 | 0.553 |
| suicidewatch | global_mean | nll | -0.056 | [-0.072, -0.041] | 614 | 0.022 |
| suicidewatch | shortcut | se | 1.814 | [1.568, 2.075] | 614 | 0.363 |
| suicidewatch | shortcut | nll | 0.073 | [0.055, 0.091] | 614 | 0.026 |
| suicidewatch | twin[fixed] | se | 0.700 | [0.599, 0.816] | 614 | 0.152 |
| suicidewatch | twin[fixed] | nll | 0.000 | [-0.013, 0.016] | 614 | 0.021 |
| suicidewatch | twin[conf_rule] | se | -1.559 | [-1.899, -1.224] | 614 | 0.494 |
| suicidewatch | twin[conf_rule] | nll | -0.558 | [-0.614, -0.502] | 614 | 0.080 |
| suicidewatch | twin[split_half/static] | se | -0.172 | [-0.270, -0.074] | 614 | 0.141 |
| suicidewatch | twin[split_half/static] | nll | -0.020 | [-0.028, -0.012] | 614 | 0.011 |
| suicidewatch | twin[split_half/rw] | se | -0.177 | [-0.274, -0.078] | 614 | 0.140 |
| suicidewatch | twin[split_half/rw] | nll | -0.020 | [-0.027, -0.012] | 614 | 0.011 |
| suicidewatch | twin[split_half/nopool] | se | -0.803 | [-1.009, -0.610] | 614 | 0.274 |
| suicidewatch | twin[split_half/nopool] | nll | -0.044 | [-0.053, -0.036] | 614 | 0.012 |

## E1 reply dose-response
beta=-0.2350 (p=7.48e-173); placebo beta=-0.0423; Gate A pass: True