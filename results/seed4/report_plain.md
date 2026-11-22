# StressTwin-P results (auto-generated; check the data source and the pilot setting in results.json before reading)

## held-out community: anxiety  (train authors 768)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.430 | 8.533 | 2.485 | 0.90 | 9.57 |
| twin[conf_rule] | 10.423 | 10.444 | 3.099 | 0.90 | 13.99 |
| twin[split_half] | 8.822 | 9.116 | 2.445 | 0.91 | 9.42 |
| twin[split_half/static] | 8.942 | 9.322 | 2.450 | 0.91 | 9.53 |
| twin[split_half/rw] | 8.942 | 9.321 | 2.450 | 0.91 | 9.53 |
| twin[split_half/nopool] | 9.830 | 9.900 | 2.501 | 0.90 | 9.94 |
| author_mean | 9.780 | 9.780 | 2.559 | 0.90 | 10.39 |
| last | 15.032 | 15.032 | 2.774 | 0.90 | 12.76 |
| ewma | 10.204 | 10.204 | 2.580 | 0.90 | 10.61 |
| gap_ewma | 9.772 | 9.772 | 2.559 | 0.90 | 10.39 |
| global_mean | 9.245 | 9.308 | 2.531 | 0.90 | 10.06 |
| shortcut | 6.794 | 6.833 | 2.377 | 0.91 | 8.76 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.57 | 0.90 / 9.49 | 0.90 / 9.61 |
| twin[conf_rule] | 0.90 / 13.99 | 0.89 / 13.53 | 0.90 / 14.39 |
| twin[split_half] | 0.91 / 9.42 | 0.90 / 9.33 | 0.90 / 9.34 |
| twin[split_half/static] | 0.91 / 9.53 | 0.90 / 9.39 | 0.90 / 9.36 |
| twin[split_half/rw] | 0.91 / 9.53 | 0.90 / 9.39 | 0.90 / 9.35 |
| twin[split_half/nopool] | 0.90 / 9.94 | 0.90 / 9.84 | 0.90 / 9.96 |

## held-out community: bipolar  (train authors 637)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.031 | 8.309 | 2.460 | 0.90 | 9.25 |
| twin[conf_rule] | 9.906 | 10.379 | 3.043 | 0.91 | 13.70 |
| twin[split_half] | 8.386 | 8.849 | 2.438 | 0.90 | 9.39 |
| twin[split_half/static] | 8.567 | 9.043 | 2.453 | 0.91 | 9.70 |
| twin[split_half/rw] | 8.563 | 9.037 | 2.453 | 0.91 | 9.69 |
| twin[split_half/nopool] | 9.037 | 9.006 | 2.475 | 0.90 | 9.72 |
| author_mean | 8.924 | 8.924 | 2.513 | 0.90 | 9.77 |
| last | 14.220 | 14.220 | 2.746 | 0.90 | 12.53 |
| ewma | 9.194 | 9.280 | 2.528 | 0.90 | 10.02 |
| gap_ewma | 8.911 | 8.911 | 2.513 | 0.90 | 9.77 |
| global_mean | 8.743 | 9.725 | 2.503 | 0.90 | 9.71 |
| shortcut | 6.840 | 6.926 | 2.380 | 0.90 | 8.51 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.25 | 0.89 / 9.21 | 0.90 / 9.46 |
| twin[conf_rule] | 0.91 / 13.70 | 0.91 / 13.71 | 0.90 / 13.88 |
| twin[split_half] | 0.90 / 9.39 | 0.90 / 9.23 | 0.90 / 9.40 |
| twin[split_half/static] | 0.91 / 9.70 | 0.90 / 9.45 | 0.90 / 9.67 |
| twin[split_half/rw] | 0.91 / 9.69 | 0.90 / 9.46 | 0.90 / 9.66 |
| twin[split_half/nopool] | 0.90 / 9.72 | 0.90 / 9.64 | 0.90 / 9.77 |

## held-out community: depression  (train authors 1500)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.437 | 8.378 | 2.486 | 0.90 | 9.44 |
| twin[conf_rule] | 10.349 | 10.561 | 3.117 | 0.90 | 14.28 |
| twin[split_half] | 8.866 | 8.638 | 2.456 | 0.90 | 9.39 |
| twin[split_half/static] | 9.079 | 8.788 | 2.468 | 0.91 | 9.62 |
| twin[split_half/rw] | 9.074 | 8.784 | 2.468 | 0.91 | 9.61 |
| twin[split_half/nopool] | 9.730 | 9.683 | 2.505 | 0.90 | 9.84 |
| author_mean | 9.645 | 9.645 | 2.552 | 0.90 | 10.09 |
| last | 14.359 | 14.359 | 2.751 | 0.90 | 12.42 |
| ewma | 9.937 | 9.937 | 2.567 | 0.90 | 10.27 |
| gap_ewma | 9.613 | 9.613 | 2.551 | 0.90 | 10.08 |
| global_mean | 9.503 | 9.515 | 2.545 | 0.90 | 10.09 |
| shortcut | 7.318 | 7.322 | 2.414 | 0.90 | 8.81 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.44 | 0.90 / 9.36 | 0.90 / 9.53 |
| twin[conf_rule] | 0.90 / 14.28 | 0.89 / 13.65 | 0.90 / 14.75 |
| twin[split_half] | 0.90 / 9.39 | 0.90 / 9.33 | 0.90 / 9.42 |
| twin[split_half/static] | 0.91 / 9.62 | 0.90 / 9.45 | 0.90 / 9.54 |
| twin[split_half/rw] | 0.91 / 9.61 | 0.90 / 9.46 | 0.90 / 9.54 |
| twin[split_half/nopool] | 0.90 / 9.84 | 0.90 / 9.82 | 0.90 / 9.95 |

## held-out community: suicidewatch  (train authors 613)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.434 | 8.365 | 2.485 | 0.90 | 9.45 |
| twin[conf_rule] | 10.919 | 10.981 | 3.107 | 0.91 | 16.25 |
| twin[split_half] | 8.915 | 8.797 | 2.464 | 0.90 | 9.23 |
| twin[split_half/static] | 9.021 | 8.860 | 2.473 | 0.90 | 9.42 |
| twin[split_half/rw] | 9.020 | 8.858 | 2.473 | 0.90 | 9.41 |
| twin[split_half/nopool] | 9.807 | 9.895 | 2.512 | 0.89 | 9.63 |
| author_mean | 9.594 | 9.594 | 2.550 | 0.90 | 10.01 |
| last | 14.501 | 14.501 | 2.757 | 0.89 | 12.20 |
| ewma | 9.936 | 9.936 | 2.567 | 0.90 | 10.18 |
| gap_ewma | 9.571 | 9.561 | 2.549 | 0.90 | 9.98 |
| global_mean | 9.150 | 9.202 | 2.526 | 0.90 | 9.89 |
| shortcut | 7.239 | 7.207 | 2.409 | 0.90 | 8.76 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.45 | 0.90 / 9.29 | 0.90 / 9.42 |
| twin[conf_rule] | 0.91 / 16.25 | 0.90 / 15.99 | 0.90 / 16.35 |
| twin[split_half] | 0.90 / 9.23 | 0.89 / 9.04 | 0.90 / 9.48 |
| twin[split_half/static] | 0.90 / 9.42 | 0.89 / 9.20 | 0.90 / 9.66 |
| twin[split_half/rw] | 0.90 / 9.41 | 0.89 / 9.19 | 0.90 / 9.66 |
| twin[split_half/nopool] | 0.89 / 9.63 | 0.89 / 9.46 | 0.90 / 10.01 |


## Twin vs baselines, paired difference with 95% author-bootstrap CI (negative = twin better)
| community | comparator | metric | diff | 95% CI | authors | min detectable (80% power) |
|---|---|---|---|---|---|---|
| anxiety | author_mean | se | -0.958 | [-1.111, -0.794] | 769 | 0.226 |
| anxiety | author_mean | nll | -0.115 | [-0.125, -0.104] | 769 | 0.015 |
| anxiety | ewma | se | -1.383 | [-1.556, -1.203] | 769 | 0.248 |
| anxiety | ewma | nll | -0.136 | [-0.146, -0.125] | 769 | 0.015 |
| anxiety | gap_ewma | se | -0.950 | [-1.096, -0.787] | 769 | 0.221 |
| anxiety | gap_ewma | nll | -0.114 | [-0.124, -0.104] | 769 | 0.014 |
| anxiety | last | se | -6.211 | [-6.678, -5.773] | 769 | 0.645 |
| anxiety | last | nll | -0.329 | [-0.343, -0.315] | 769 | 0.020 |
| anxiety | global_mean | se | -0.423 | [-0.647, -0.198] | 769 | 0.309 |
| anxiety | global_mean | nll | -0.086 | [-0.099, -0.074] | 769 | 0.019 |
| anxiety | shortcut | se | 2.028 | [1.771, 2.313] | 769 | 0.382 |
| anxiety | shortcut | nll | 0.067 | [0.053, 0.083] | 769 | 0.022 |
| anxiety | twin[fixed] | se | 0.392 | [0.327, 0.456] | 769 | 0.094 |
| anxiety | twin[fixed] | nll | -0.040 | [-0.048, -0.032] | 769 | 0.011 |
| anxiety | twin[conf_rule] | se | -1.602 | [-1.868, -1.332] | 769 | 0.390 |
| anxiety | twin[conf_rule] | nll | -0.654 | [-0.746, -0.572] | 769 | 0.125 |
| anxiety | twin[split_half/static] | se | -0.120 | [-0.164, -0.076] | 769 | 0.062 |
| anxiety | twin[split_half/static] | nll | -0.005 | [-0.008, -0.003] | 769 | 0.004 |
| anxiety | twin[split_half/rw] | se | -0.120 | [-0.163, -0.076] | 769 | 0.061 |
| anxiety | twin[split_half/rw] | nll | -0.005 | [-0.008, -0.003] | 769 | 0.004 |
| anxiety | twin[split_half/nopool] | se | -1.008 | [-1.160, -0.858] | 769 | 0.208 |
| anxiety | twin[split_half/nopool] | nll | -0.056 | [-0.063, -0.049] | 769 | 0.010 |
| bipolar | author_mean | se | -0.538 | [-0.670, -0.413] | 638 | 0.180 |
| bipolar | author_mean | nll | -0.075 | [-0.084, -0.067] | 638 | 0.012 |
| bipolar | ewma | se | -0.808 | [-0.947, -0.669] | 638 | 0.206 |
| bipolar | ewma | nll | -0.090 | [-0.099, -0.081] | 638 | 0.013 |
| bipolar | gap_ewma | se | -0.525 | [-0.650, -0.401] | 638 | 0.178 |
| bipolar | gap_ewma | nll | -0.074 | [-0.083, -0.067] | 638 | 0.012 |
| bipolar | last | se | -5.835 | [-6.169, -5.509] | 638 | 0.484 |
| bipolar | last | nll | -0.308 | [-0.318, -0.297] | 638 | 0.015 |
| bipolar | global_mean | se | -0.358 | [-0.558, -0.178] | 638 | 0.265 |
| bipolar | global_mean | nll | -0.065 | [-0.077, -0.054] | 638 | 0.017 |
| bipolar | shortcut | se | 1.546 | [1.343, 1.742] | 638 | 0.289 |
| bipolar | shortcut | nll | 0.058 | [0.044, 0.071] | 638 | 0.020 |
| bipolar | twin[fixed] | se | 0.355 | [0.302, 0.406] | 638 | 0.074 |
| bipolar | twin[fixed] | nll | -0.022 | [-0.027, -0.016] | 638 | 0.008 |
| bipolar | twin[conf_rule] | se | -1.521 | [-1.710, -1.329] | 638 | 0.271 |
| bipolar | twin[conf_rule] | nll | -0.605 | [-0.694, -0.531] | 638 | 0.115 |
| bipolar | twin[split_half/static] | se | -0.181 | [-0.262, -0.109] | 638 | 0.106 |
| bipolar | twin[split_half/static] | nll | -0.015 | [-0.019, -0.011] | 638 | 0.005 |
| bipolar | twin[split_half/rw] | se | -0.177 | [-0.257, -0.104] | 638 | 0.105 |
| bipolar | twin[split_half/rw] | nll | -0.015 | [-0.019, -0.011] | 638 | 0.005 |
| bipolar | twin[split_half/nopool] | se | -0.652 | [-0.760, -0.553] | 638 | 0.154 |
| bipolar | twin[split_half/nopool] | nll | -0.037 | [-0.042, -0.032] | 638 | 0.007 |
| depression | author_mean | se | -0.779 | [-0.867, -0.691] | 2172 | 0.125 |
| depression | author_mean | nll | -0.096 | [-0.102, -0.090] | 2172 | 0.009 |
| depression | ewma | se | -1.071 | [-1.172, -0.962] | 2172 | 0.146 |
| depression | ewma | nll | -0.111 | [-0.117, -0.104] | 2172 | 0.009 |
| depression | gap_ewma | se | -0.747 | [-0.835, -0.658] | 2172 | 0.125 |
| depression | gap_ewma | nll | -0.094 | [-0.100, -0.088] | 2172 | 0.009 |
| depression | last | se | -5.493 | [-5.735, -5.253] | 2172 | 0.343 |
| depression | last | nll | -0.295 | [-0.303, -0.286] | 2172 | 0.012 |
| depression | global_mean | se | -0.637 | [-0.827, -0.476] | 2172 | 0.247 |
| depression | global_mean | nll | -0.088 | [-0.098, -0.079] | 2172 | 0.014 |
| depression | shortcut | se | 1.548 | [1.407, 1.679] | 2172 | 0.199 |
| depression | shortcut | nll | 0.042 | [0.034, 0.050] | 2172 | 0.011 |
| depression | twin[fixed] | se | 0.429 | [0.390, 0.467] | 2172 | 0.056 |
| depression | twin[fixed] | nll | -0.029 | [-0.033, -0.025] | 2172 | 0.006 |
| depression | twin[conf_rule] | se | -1.483 | [-1.618, -1.345] | 2172 | 0.193 |
| depression | twin[conf_rule] | nll | -0.660 | [-0.730, -0.598] | 2172 | 0.096 |
| depression | twin[split_half/static] | se | -0.213 | [-0.268, -0.161] | 2172 | 0.077 |
| depression | twin[split_half/static] | nll | -0.012 | [-0.014, -0.009] | 2172 | 0.004 |
| depression | twin[split_half/rw] | se | -0.208 | [-0.260, -0.157] | 2172 | 0.074 |
| depression | twin[split_half/rw] | nll | -0.011 | [-0.014, -0.008] | 2172 | 0.004 |
| depression | twin[split_half/nopool] | se | -0.864 | [-0.944, -0.782] | 2172 | 0.119 |
| depression | twin[split_half/nopool] | nll | -0.048 | [-0.052, -0.045] | 2172 | 0.005 |
| suicidewatch | author_mean | se | -0.680 | [-0.847, -0.528] | 614 | 0.228 |
| suicidewatch | author_mean | nll | -0.086 | [-0.099, -0.074] | 614 | 0.018 |
| suicidewatch | ewma | se | -1.021 | [-1.210, -0.852] | 614 | 0.259 |
| suicidewatch | ewma | nll | -0.103 | [-0.117, -0.090] | 614 | 0.019 |
| suicidewatch | gap_ewma | se | -0.657 | [-0.830, -0.499] | 614 | 0.238 |
| suicidewatch | gap_ewma | nll | -0.085 | [-0.098, -0.072] | 614 | 0.019 |
| suicidewatch | last | se | -5.586 | [-5.998, -5.211] | 614 | 0.568 |
| suicidewatch | last | nll | -0.293 | [-0.309, -0.277] | 614 | 0.022 |
| suicidewatch | global_mean | se | -0.235 | [-0.468, 0.003] | 614 | 0.325 |
| suicidewatch | global_mean | nll | -0.062 | [-0.075, -0.047] | 614 | 0.021 |
| suicidewatch | shortcut | se | 1.676 | [1.368, 1.994] | 614 | 0.436 |
| suicidewatch | shortcut | nll | 0.055 | [0.036, 0.075] | 614 | 0.027 |
| suicidewatch | twin[fixed] | se | 0.481 | [0.413, 0.550] | 614 | 0.097 |
| suicidewatch | twin[fixed] | nll | -0.021 | [-0.028, -0.013] | 614 | 0.011 |
| suicidewatch | twin[conf_rule] | se | -2.005 | [-2.317, -1.680] | 614 | 0.449 |
| suicidewatch | twin[conf_rule] | nll | -0.643 | [-0.718, -0.576] | 614 | 0.103 |
| suicidewatch | twin[split_half/static] | se | -0.107 | [-0.201, -0.017] | 614 | 0.132 |
| suicidewatch | twin[split_half/static] | nll | -0.009 | [-0.016, -0.002] | 614 | 0.009 |
| suicidewatch | twin[split_half/rw] | se | -0.105 | [-0.195, -0.019] | 614 | 0.127 |
| suicidewatch | twin[split_half/rw] | nll | -0.009 | [-0.015, -0.002] | 614 | 0.009 |
| suicidewatch | twin[split_half/nopool] | se | -0.892 | [-1.049, -0.748] | 614 | 0.220 |
| suicidewatch | twin[split_half/nopool] | nll | -0.048 | [-0.055, -0.041] | 614 | 0.011 |

## E1 reply dose-response
beta=-0.2350 (p=7.48e-173); placebo beta=-0.0423; Gate A pass: True