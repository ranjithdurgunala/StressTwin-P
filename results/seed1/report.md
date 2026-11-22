# StressTwin-P results (auto-generated; check the data source and the pilot setting in results.json before reading)

## held-out community: anxiety  (train authors 768)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.939 | 6.010 | 2.309 | 0.90 | 7.99 |
| twin[conf_rule] | 7.263 | 7.339 | 2.747 | 0.90 | 10.60 |
| twin[split_half] | 6.279 | 6.501 | 2.281 | 0.91 | 7.99 |
| twin[split_half/static] | 6.397 | 6.711 | 2.289 | 0.91 | 8.12 |
| twin[split_half/rw] | 6.397 | 6.713 | 2.288 | 0.91 | 8.12 |
| twin[split_half/nopool] | 7.045 | 7.098 | 2.338 | 0.91 | 8.45 |
| author_mean | 6.957 | 6.957 | 2.389 | 0.90 | 8.65 |
| last | 10.487 | 10.487 | 2.594 | 0.90 | 10.65 |
| ewma | 7.253 | 7.253 | 2.410 | 0.90 | 8.83 |
| gap_ewma | 6.956 | 6.956 | 2.389 | 0.90 | 8.64 |
| global_mean | 6.565 | 6.572 | 2.360 | 0.90 | 8.33 |
| shortcut | 4.996 | 5.005 | 2.223 | 0.90 | 7.30 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 7.99 | 0.90 / 7.95 | 0.90 / 8.11 |
| twin[conf_rule] | 0.90 / 10.60 | 0.90 / 10.43 | 0.90 / 10.93 |
| twin[split_half] | 0.91 / 7.99 | 0.90 / 7.91 | 0.90 / 7.95 |
| twin[split_half/static] | 0.91 / 8.12 | 0.90 / 7.98 | 0.90 / 8.01 |
| twin[split_half/rw] | 0.91 / 8.12 | 0.90 / 7.98 | 0.90 / 8.00 |
| twin[split_half/nopool] | 0.91 / 8.45 | 0.90 / 8.40 | 0.90 / 8.45 |

## held-out community: bipolar  (train authors 637)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.523 | 5.727 | 2.273 | 0.90 | 7.64 |
| twin[conf_rule] | 6.872 | 7.389 | 2.727 | 0.90 | 10.28 |
| twin[split_half] | 5.854 | 6.148 | 2.268 | 0.90 | 7.90 |
| twin[split_half/static] | 5.987 | 6.282 | 2.288 | 0.91 | 8.26 |
| twin[split_half/rw] | 5.976 | 6.269 | 2.287 | 0.91 | 8.25 |
| twin[split_half/nopool] | 6.282 | 6.215 | 2.302 | 0.90 | 8.14 |
| author_mean | 6.088 | 6.088 | 2.322 | 0.90 | 8.12 |
| last | 9.884 | 9.884 | 2.564 | 0.90 | 10.29 |
| ewma | 6.347 | 6.421 | 2.343 | 0.90 | 8.28 |
| gap_ewma | 6.081 | 6.081 | 2.322 | 0.90 | 8.12 |
| global_mean | 6.021 | 6.890 | 2.317 | 0.90 | 8.05 |
| shortcut | 4.753 | 5.097 | 2.198 | 0.90 | 7.17 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 7.64 | 0.90 / 7.71 | 0.90 / 7.79 |
| twin[conf_rule] | 0.90 / 10.28 | 0.89 / 9.99 | 0.90 / 10.70 |
| twin[split_half] | 0.90 / 7.90 | 0.90 / 7.80 | 0.90 / 7.85 |
| twin[split_half/static] | 0.91 / 8.26 | 0.90 / 8.06 | 0.90 / 8.11 |
| twin[split_half/rw] | 0.91 / 8.25 | 0.90 / 8.06 | 0.90 / 8.12 |
| twin[split_half/nopool] | 0.90 / 8.14 | 0.90 / 8.07 | 0.90 / 8.14 |

## held-out community: depression  (train authors 1500)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.752 | 5.722 | 2.293 | 0.90 | 7.86 |
| twin[conf_rule] | 7.006 | 6.990 | 2.693 | 0.91 | 10.71 |
| twin[split_half] | 6.119 | 5.969 | 2.277 | 0.90 | 7.94 |
| twin[split_half/static] | 6.331 | 6.132 | 2.295 | 0.90 | 8.19 |
| twin[split_half/rw] | 6.328 | 6.131 | 2.295 | 0.90 | 8.19 |
| twin[split_half/nopool] | 6.742 | 6.702 | 2.325 | 0.90 | 8.29 |
| author_mean | 6.637 | 6.637 | 2.365 | 0.90 | 8.45 |
| last | 9.836 | 9.836 | 2.562 | 0.90 | 10.34 |
| ewma | 6.832 | 6.832 | 2.380 | 0.90 | 8.58 |
| gap_ewma | 6.608 | 6.608 | 2.363 | 0.90 | 8.44 |
| global_mean | 6.587 | 6.583 | 2.362 | 0.90 | 8.36 |
| shortcut | 5.062 | 5.069 | 2.230 | 0.90 | 7.39 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 7.86 | 0.90 / 7.88 | 0.90 / 7.93 |
| twin[conf_rule] | 0.91 / 10.71 | 0.90 / 10.18 | 0.90 / 10.69 |
| twin[split_half] | 0.90 / 7.94 | 0.90 / 7.88 | 0.90 / 7.93 |
| twin[split_half/static] | 0.90 / 8.19 | 0.90 / 8.06 | 0.90 / 8.18 |
| twin[split_half/rw] | 0.90 / 8.19 | 0.90 / 8.06 | 0.90 / 8.18 |
| twin[split_half/nopool] | 0.90 / 8.29 | 0.90 / 8.27 | 0.90 / 8.35 |

## held-out community: suicidewatch  (train authors 613)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.686 | 5.647 | 2.287 | 0.91 | 7.88 |
| twin[conf_rule] | 7.398 | 7.308 | 2.717 | 0.90 | 11.22 |
| twin[split_half] | 6.165 | 6.014 | 2.288 | 0.90 | 8.12 |
| twin[split_half/static] | 6.371 | 6.143 | 2.309 | 0.90 | 8.40 |
| twin[split_half/rw] | 6.368 | 6.143 | 2.309 | 0.90 | 8.39 |
| twin[split_half/nopool] | 6.728 | 6.735 | 2.330 | 0.90 | 8.42 |
| author_mean | 6.483 | 6.483 | 2.354 | 0.91 | 8.47 |
| last | 9.757 | 9.757 | 2.558 | 0.90 | 10.34 |
| ewma | 6.687 | 6.687 | 2.369 | 0.91 | 8.64 |
| gap_ewma | 6.447 | 6.447 | 2.351 | 0.91 | 8.45 |
| global_mean | 6.226 | 6.207 | 2.333 | 0.90 | 8.25 |
| shortcut | 4.943 | 4.933 | 2.218 | 0.90 | 7.38 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.91 / 7.88 | 0.90 / 7.73 | 0.90 / 7.82 |
| twin[conf_rule] | 0.90 / 11.22 | 0.89 / 10.61 | 0.90 / 11.41 |
| twin[split_half] | 0.90 / 8.12 | 0.90 / 7.99 | 0.90 / 8.14 |
| twin[split_half/static] | 0.90 / 8.40 | 0.89 / 8.19 | 0.90 / 8.37 |
| twin[split_half/rw] | 0.90 / 8.39 | 0.89 / 8.19 | 0.90 / 8.37 |
| twin[split_half/nopool] | 0.90 / 8.42 | 0.90 / 8.38 | 0.90 / 8.46 |


## Twin vs baselines, paired difference with 95% author-bootstrap CI (negative = twin better)
| community | comparator | metric | diff | 95% CI | authors | min detectable (80% power) |
|---|---|---|---|---|---|---|
| anxiety | author_mean | se | -0.677 | [-0.794, -0.545] | 769 | 0.182 |
| anxiety | author_mean | nll | -0.107 | [-0.119, -0.096] | 769 | 0.016 |
| anxiety | ewma | se | -0.974 | [-1.097, -0.832] | 769 | 0.197 |
| anxiety | ewma | nll | -0.128 | [-0.139, -0.117] | 769 | 0.016 |
| anxiety | gap_ewma | se | -0.677 | [-0.795, -0.548] | 769 | 0.181 |
| anxiety | gap_ewma | nll | -0.107 | [-0.118, -0.096] | 769 | 0.016 |
| anxiety | last | se | -4.208 | [-4.560, -3.879] | 769 | 0.499 |
| anxiety | last | nll | -0.313 | [-0.328, -0.297] | 769 | 0.022 |
| anxiety | global_mean | se | -0.285 | [-0.438, -0.146] | 769 | 0.208 |
| anxiety | global_mean | nll | -0.079 | [-0.091, -0.067] | 769 | 0.017 |
| anxiety | shortcut | se | 1.283 | [1.100, 1.468] | 769 | 0.259 |
| anxiety | shortcut | nll | 0.058 | [0.043, 0.072] | 769 | 0.021 |
| anxiety | twin[fixed] | se | 0.340 | [0.288, 0.400] | 769 | 0.078 |
| anxiety | twin[fixed] | nll | -0.028 | [-0.034, -0.021] | 769 | 0.009 |
| anxiety | twin[conf_rule] | se | -0.984 | [-1.169, -0.804] | 769 | 0.260 |
| anxiety | twin[conf_rule] | nll | -0.466 | [-0.541, -0.402] | 769 | 0.103 |
| anxiety | twin[split_half/static] | se | -0.118 | [-0.174, -0.068] | 769 | 0.075 |
| anxiety | twin[split_half/static] | nll | -0.007 | [-0.011, -0.004] | 769 | 0.005 |
| anxiety | twin[split_half/rw] | se | -0.118 | [-0.173, -0.069] | 769 | 0.075 |
| anxiety | twin[split_half/rw] | nll | -0.007 | [-0.011, -0.004] | 769 | 0.005 |
| anxiety | twin[split_half/nopool] | se | -0.765 | [-0.888, -0.643] | 769 | 0.177 |
| anxiety | twin[split_half/nopool] | nll | -0.057 | [-0.064, -0.049] | 769 | 0.011 |
| bipolar | author_mean | se | -0.235 | [-0.415, -0.045] | 638 | 0.283 |
| bipolar | author_mean | nll | -0.055 | [-0.071, -0.036] | 638 | 0.026 |
| bipolar | ewma | se | -0.494 | [-0.646, -0.358] | 638 | 0.213 |
| bipolar | ewma | nll | -0.075 | [-0.090, -0.062] | 638 | 0.020 |
| bipolar | gap_ewma | se | -0.227 | [-0.408, -0.037] | 638 | 0.284 |
| bipolar | gap_ewma | nll | -0.054 | [-0.071, -0.035] | 638 | 0.026 |
| bipolar | last | se | -4.030 | [-4.354, -3.711] | 638 | 0.485 |
| bipolar | last | nll | -0.297 | [-0.308, -0.285] | 638 | 0.016 |
| bipolar | global_mean | se | -0.167 | [-0.313, -0.034] | 638 | 0.196 |
| bipolar | global_mean | nll | -0.049 | [-0.063, -0.037] | 638 | 0.018 |
| bipolar | shortcut | se | 1.101 | [0.865, 1.353] | 638 | 0.359 |
| bipolar | shortcut | nll | 0.069 | [0.047, 0.091] | 638 | 0.032 |
| bipolar | twin[fixed] | se | 0.331 | [0.266, 0.400] | 638 | 0.098 |
| bipolar | twin[fixed] | nll | -0.005 | [-0.012, 0.001] | 638 | 0.009 |
| bipolar | twin[conf_rule] | se | -1.018 | [-1.350, -0.755] | 638 | 0.462 |
| bipolar | twin[conf_rule] | nll | -0.460 | [-0.534, -0.387] | 638 | 0.110 |
| bipolar | twin[split_half/static] | se | -0.134 | [-0.179, -0.088] | 638 | 0.065 |
| bipolar | twin[split_half/static] | nll | -0.020 | [-0.027, -0.013] | 638 | 0.011 |
| bipolar | twin[split_half/rw] | se | -0.123 | [-0.170, -0.081] | 638 | 0.064 |
| bipolar | twin[split_half/rw] | nll | -0.019 | [-0.027, -0.012] | 638 | 0.011 |
| bipolar | twin[split_half/nopool] | se | -0.429 | [-0.536, -0.332] | 638 | 0.151 |
| bipolar | twin[split_half/nopool] | nll | -0.034 | [-0.042, -0.027] | 638 | 0.011 |
| depression | author_mean | se | -0.518 | [-0.587, -0.454] | 2172 | 0.096 |
| depression | author_mean | nll | -0.089 | [-0.095, -0.083] | 2172 | 0.009 |
| depression | ewma | se | -0.713 | [-0.791, -0.630] | 2172 | 0.116 |
| depression | ewma | nll | -0.103 | [-0.110, -0.096] | 2172 | 0.010 |
| depression | gap_ewma | se | -0.489 | [-0.558, -0.424] | 2172 | 0.097 |
| depression | gap_ewma | nll | -0.087 | [-0.093, -0.080] | 2172 | 0.009 |
| depression | last | se | -3.717 | [-3.886, -3.548] | 2172 | 0.240 |
| depression | last | nll | -0.285 | [-0.294, -0.277] | 2172 | 0.012 |
| depression | global_mean | se | -0.468 | [-0.712, -0.287] | 2172 | 0.300 |
| depression | global_mean | nll | -0.085 | [-0.103, -0.071] | 2172 | 0.024 |
| depression | shortcut | se | 1.057 | [0.943, 1.161] | 2172 | 0.161 |
| depression | shortcut | nll | 0.047 | [0.038, 0.056] | 2172 | 0.013 |
| depression | twin[fixed] | se | 0.367 | [0.330, 0.402] | 2172 | 0.052 |
| depression | twin[fixed] | nll | -0.016 | [-0.020, -0.012] | 2172 | 0.006 |
| depression | twin[conf_rule] | se | -0.887 | [-0.984, -0.794] | 2172 | 0.134 |
| depression | twin[conf_rule] | nll | -0.417 | [-0.445, -0.389] | 2172 | 0.041 |
| depression | twin[split_half/static] | se | -0.212 | [-0.287, -0.152] | 2172 | 0.096 |
| depression | twin[split_half/static] | nll | -0.018 | [-0.022, -0.015] | 2172 | 0.005 |
| depression | twin[split_half/rw] | se | -0.209 | [-0.281, -0.150] | 2172 | 0.094 |
| depression | twin[split_half/rw] | nll | -0.018 | [-0.022, -0.015] | 2172 | 0.005 |
| depression | twin[split_half/nopool] | se | -0.623 | [-0.682, -0.562] | 2172 | 0.087 |
| depression | twin[split_half/nopool] | nll | -0.049 | [-0.052, -0.045] | 2172 | 0.006 |
| suicidewatch | author_mean | se | -0.317 | [-0.434, -0.212] | 614 | 0.161 |
| suicidewatch | author_mean | nll | -0.066 | [-0.084, -0.048] | 614 | 0.025 |
| suicidewatch | ewma | se | -0.521 | [-0.647, -0.419] | 614 | 0.162 |
| suicidewatch | ewma | nll | -0.082 | [-0.098, -0.068] | 614 | 0.022 |
| suicidewatch | gap_ewma | se | -0.282 | [-0.397, -0.182] | 614 | 0.158 |
| suicidewatch | gap_ewma | nll | -0.063 | [-0.081, -0.046] | 614 | 0.025 |
| suicidewatch | last | se | -3.592 | [-3.842, -3.337] | 614 | 0.353 |
| suicidewatch | last | nll | -0.270 | [-0.287, -0.255] | 614 | 0.022 |
| suicidewatch | global_mean | se | -0.060 | [-0.238, 0.136] | 614 | 0.275 |
| suicidewatch | global_mean | nll | -0.046 | [-0.058, -0.034] | 614 | 0.018 |
| suicidewatch | shortcut | se | 1.222 | [1.042, 1.438] | 614 | 0.290 |
| suicidewatch | shortcut | nll | 0.070 | [0.053, 0.087] | 614 | 0.024 |
| suicidewatch | twin[fixed] | se | 0.480 | [0.413, 0.553] | 614 | 0.101 |
| suicidewatch | twin[fixed] | nll | 0.001 | [-0.011, 0.012] | 614 | 0.017 |
| suicidewatch | twin[conf_rule] | se | -1.233 | [-1.466, -1.009] | 614 | 0.324 |
| suicidewatch | twin[conf_rule] | nll | -0.429 | [-0.473, -0.382] | 614 | 0.066 |
| suicidewatch | twin[split_half/static] | se | -0.205 | [-0.282, -0.132] | 614 | 0.108 |
| suicidewatch | twin[split_half/static] | nll | -0.022 | [-0.027, -0.015] | 614 | 0.009 |
| suicidewatch | twin[split_half/rw] | se | -0.203 | [-0.273, -0.132] | 614 | 0.103 |
| suicidewatch | twin[split_half/rw] | nll | -0.021 | [-0.027, -0.015] | 614 | 0.008 |
| suicidewatch | twin[split_half/nopool] | se | -0.563 | [-0.689, -0.454] | 614 | 0.167 |
| suicidewatch | twin[split_half/nopool] | nll | -0.043 | [-0.051, -0.036] | 614 | 0.011 |

## E1 reply dose-response
beta=-0.1911 (p=5.47e-158); placebo beta=-0.0333; Gate A pass: True