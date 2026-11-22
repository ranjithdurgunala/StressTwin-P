# StressTwin-P results (auto-generated; check the data source and the pilot setting in results.json before reading)

## held-out community: anxiety  (train authors 768)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.958 | 6.016 | 2.311 | 0.90 | 7.97 |
| twin[conf_rule] | 7.139 | 7.209 | 2.714 | 0.91 | 10.82 |
| twin[split_half] | 6.257 | 6.507 | 2.283 | 0.91 | 7.96 |
| twin[split_half/static] | 6.361 | 6.732 | 2.291 | 0.91 | 8.05 |
| twin[split_half/rw] | 6.360 | 6.732 | 2.291 | 0.91 | 8.05 |
| twin[split_half/nopool] | 7.016 | 7.088 | 2.340 | 0.90 | 8.38 |
| author_mean | 6.919 | 6.919 | 2.386 | 0.90 | 8.67 |
| last | 10.494 | 10.494 | 2.594 | 0.90 | 10.64 |
| ewma | 7.213 | 7.213 | 2.407 | 0.90 | 8.86 |
| gap_ewma | 6.906 | 6.906 | 2.385 | 0.90 | 8.68 |
| global_mean | 6.553 | 6.599 | 2.359 | 0.89 | 8.31 |
| shortcut | 4.949 | 4.990 | 2.219 | 0.90 | 7.34 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 7.97 | 0.90 / 7.94 | 0.90 / 8.11 |
| twin[conf_rule] | 0.91 / 10.82 | 0.90 / 10.53 | 0.90 / 10.80 |
| twin[split_half] | 0.91 / 7.96 | 0.90 / 7.87 | 0.90 / 7.92 |
| twin[split_half/static] | 0.91 / 8.05 | 0.90 / 7.93 | 0.90 / 8.06 |
| twin[split_half/rw] | 0.91 / 8.05 | 0.90 / 7.93 | 0.90 / 8.06 |
| twin[split_half/nopool] | 0.90 / 8.38 | 0.90 / 8.35 | 0.90 / 8.47 |

## held-out community: bipolar  (train authors 637)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.513 | 5.675 | 2.272 | 0.90 | 7.67 |
| twin[conf_rule] | 6.886 | 7.348 | 2.714 | 0.90 | 10.41 |
| twin[split_half] | 5.806 | 6.189 | 2.265 | 0.90 | 7.85 |
| twin[split_half/static] | 5.903 | 6.250 | 2.279 | 0.91 | 8.16 |
| twin[split_half/rw] | 5.892 | 6.235 | 2.279 | 0.91 | 8.16 |
| twin[split_half/nopool] | 6.196 | 6.207 | 2.297 | 0.90 | 8.09 |
| author_mean | 6.026 | 6.026 | 2.317 | 0.91 | 8.18 |
| last | 9.849 | 9.849 | 2.563 | 0.90 | 10.32 |
| ewma | 6.284 | 6.378 | 2.338 | 0.91 | 8.33 |
| gap_ewma | 6.019 | 6.019 | 2.317 | 0.91 | 8.17 |
| global_mean | 6.077 | 6.860 | 2.321 | 0.89 | 8.00 |
| shortcut | 4.708 | 4.767 | 2.194 | 0.91 | 7.23 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 7.67 | 0.90 / 7.68 | 0.90 / 7.82 |
| twin[conf_rule] | 0.90 / 10.41 | 0.89 / 9.97 | 0.90 / 10.65 |
| twin[split_half] | 0.90 / 7.85 | 0.90 / 7.76 | 0.90 / 7.82 |
| twin[split_half/static] | 0.91 / 8.16 | 0.90 / 8.01 | 0.90 / 8.01 |
| twin[split_half/rw] | 0.91 / 8.16 | 0.91 / 8.02 | 0.90 / 8.01 |
| twin[split_half/nopool] | 0.90 / 8.09 | 0.90 / 8.07 | 0.90 / 8.11 |

## held-out community: depression  (train authors 1500)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.742 | 5.712 | 2.292 | 0.90 | 7.90 |
| twin[conf_rule] | 7.037 | 6.993 | 2.709 | 0.91 | 10.90 |
| twin[split_half] | 6.089 | 5.984 | 2.271 | 0.91 | 8.00 |
| twin[split_half/static] | 6.251 | 6.119 | 2.285 | 0.91 | 8.23 |
| twin[split_half/rw] | 6.248 | 6.117 | 2.285 | 0.91 | 8.23 |
| twin[split_half/nopool] | 6.718 | 6.716 | 2.320 | 0.91 | 8.38 |
| author_mean | 6.587 | 6.587 | 2.362 | 0.90 | 8.49 |
| last | 9.880 | 9.880 | 2.564 | 0.90 | 10.32 |
| ewma | 6.802 | 6.802 | 2.378 | 0.90 | 8.61 |
| gap_ewma | 6.558 | 6.558 | 2.359 | 0.91 | 8.48 |
| global_mean | 6.500 | 6.588 | 2.355 | 0.90 | 8.34 |
| shortcut | 5.071 | 5.094 | 2.231 | 0.90 | 7.41 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 7.90 | 0.90 / 7.93 | 0.90 / 7.92 |
| twin[conf_rule] | 0.91 / 10.90 | 0.91 / 10.48 | 0.90 / 10.59 |
| twin[split_half] | 0.91 / 8.00 | 0.91 / 7.97 | 0.90 / 7.85 |
| twin[split_half/static] | 0.91 / 8.23 | 0.91 / 8.16 | 0.90 / 8.02 |
| twin[split_half/rw] | 0.91 / 8.23 | 0.91 / 8.15 | 0.90 / 8.03 |
| twin[split_half/nopool] | 0.91 / 8.38 | 0.91 / 8.37 | 0.90 / 8.28 |

## held-out community: suicidewatch  (train authors 613)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.567 | 5.525 | 2.276 | 0.91 | 7.94 |
| twin[conf_rule] | 7.167 | 7.160 | 2.676 | 0.92 | 11.61 |
| twin[split_half] | 6.086 | 5.782 | 2.287 | 0.91 | 8.27 |
| twin[split_half/static] | 6.214 | 5.821 | 2.309 | 0.91 | 8.65 |
| twin[split_half/rw] | 6.217 | 5.823 | 2.309 | 0.91 | 8.65 |
| twin[split_half/nopool] | 6.677 | 6.598 | 2.332 | 0.91 | 8.60 |
| author_mean | 6.413 | 6.413 | 2.349 | 0.91 | 8.51 |
| last | 9.481 | 9.481 | 2.545 | 0.91 | 10.48 |
| ewma | 6.649 | 6.649 | 2.367 | 0.91 | 8.66 |
| gap_ewma | 6.390 | 6.390 | 2.347 | 0.91 | 8.48 |
| global_mean | 6.120 | 6.143 | 2.325 | 0.91 | 8.29 |
| shortcut | 4.843 | 4.852 | 2.208 | 0.91 | 7.44 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.91 / 7.94 | 0.91 / 7.85 | 0.90 / 7.78 |
| twin[conf_rule] | 0.92 / 11.61 | 0.91 / 11.23 | 0.90 / 11.02 |
| twin[split_half] | 0.91 / 8.27 | 0.91 / 8.21 | 0.90 / 8.04 |
| twin[split_half/static] | 0.91 / 8.65 | 0.91 / 8.49 | 0.90 / 8.39 |
| twin[split_half/rw] | 0.91 / 8.65 | 0.91 / 8.48 | 0.90 / 8.40 |
| twin[split_half/nopool] | 0.91 / 8.60 | 0.91 / 8.55 | 0.90 / 8.42 |


## Twin vs baselines, paired difference with 95% author-bootstrap CI (negative = twin better)
| community | comparator | metric | diff | 95% CI | authors | min detectable (80% power) |
|---|---|---|---|---|---|---|
| anxiety | author_mean | se | -0.662 | [-0.771, -0.545] | 769 | 0.163 |
| anxiety | author_mean | nll | -0.103 | [-0.114, -0.092] | 769 | 0.015 |
| anxiety | ewma | se | -0.956 | [-1.079, -0.830] | 769 | 0.176 |
| anxiety | ewma | nll | -0.124 | [-0.134, -0.114] | 769 | 0.015 |
| anxiety | gap_ewma | se | -0.649 | [-0.759, -0.537] | 769 | 0.161 |
| anxiety | gap_ewma | nll | -0.102 | [-0.112, -0.091] | 769 | 0.015 |
| anxiety | last | se | -4.237 | [-4.528, -3.944] | 769 | 0.415 |
| anxiety | last | nll | -0.311 | [-0.324, -0.299] | 769 | 0.018 |
| anxiety | global_mean | se | -0.296 | [-0.442, -0.145] | 769 | 0.211 |
| anxiety | global_mean | nll | -0.076 | [-0.089, -0.063] | 769 | 0.018 |
| anxiety | shortcut | se | 1.308 | [1.117, 1.475] | 769 | 0.251 |
| anxiety | shortcut | nll | 0.065 | [0.049, 0.079] | 769 | 0.020 |
| anxiety | twin[fixed] | se | 0.299 | [0.254, 0.346] | 769 | 0.067 |
| anxiety | twin[fixed] | nll | -0.028 | [-0.035, -0.021] | 769 | 0.010 |
| anxiety | twin[conf_rule] | se | -0.882 | [-1.051, -0.729] | 769 | 0.233 |
| anxiety | twin[conf_rule] | nll | -0.430 | [-0.502, -0.375] | 769 | 0.094 |
| anxiety | twin[split_half/static] | se | -0.104 | [-0.146, -0.063] | 769 | 0.059 |
| anxiety | twin[split_half/static] | nll | -0.007 | [-0.010, -0.005] | 769 | 0.004 |
| anxiety | twin[split_half/rw] | se | -0.103 | [-0.145, -0.063] | 769 | 0.059 |
| anxiety | twin[split_half/rw] | nll | -0.007 | [-0.010, -0.004] | 769 | 0.004 |
| anxiety | twin[split_half/nopool] | se | -0.758 | [-0.865, -0.651] | 769 | 0.156 |
| anxiety | twin[split_half/nopool] | nll | -0.057 | [-0.064, -0.050] | 769 | 0.010 |
| bipolar | author_mean | se | -0.220 | [-0.375, -0.053] | 638 | 0.248 |
| bipolar | author_mean | nll | -0.053 | [-0.068, -0.036] | 638 | 0.024 |
| bipolar | ewma | se | -0.477 | [-0.606, -0.356] | 638 | 0.181 |
| bipolar | ewma | nll | -0.073 | [-0.087, -0.061] | 638 | 0.019 |
| bipolar | gap_ewma | se | -0.213 | [-0.366, -0.041] | 638 | 0.250 |
| bipolar | gap_ewma | nll | -0.052 | [-0.068, -0.035] | 638 | 0.024 |
| bipolar | last | se | -4.042 | [-4.378, -3.708] | 638 | 0.485 |
| bipolar | last | nll | -0.298 | [-0.309, -0.287] | 638 | 0.016 |
| bipolar | global_mean | se | -0.270 | [-0.425, -0.132] | 638 | 0.206 |
| bipolar | global_mean | nll | -0.057 | [-0.071, -0.045] | 638 | 0.018 |
| bipolar | shortcut | se | 1.099 | [0.890, 1.316] | 638 | 0.313 |
| bipolar | shortcut | nll | 0.071 | [0.053, 0.090] | 638 | 0.028 |
| bipolar | twin[fixed] | se | 0.293 | [0.242, 0.346] | 638 | 0.077 |
| bipolar | twin[fixed] | nll | -0.007 | [-0.013, -0.001] | 638 | 0.009 |
| bipolar | twin[conf_rule] | se | -1.080 | [-1.397, -0.816] | 638 | 0.472 |
| bipolar | twin[conf_rule] | nll | -0.450 | [-0.519, -0.382] | 638 | 0.103 |
| bipolar | twin[split_half/static] | se | -0.096 | [-0.136, -0.056] | 638 | 0.056 |
| bipolar | twin[split_half/static] | nll | -0.015 | [-0.022, -0.008] | 638 | 0.010 |
| bipolar | twin[split_half/rw] | se | -0.085 | [-0.128, -0.047] | 638 | 0.057 |
| bipolar | twin[split_half/rw] | nll | -0.014 | [-0.021, -0.007] | 638 | 0.010 |
| bipolar | twin[split_half/nopool] | se | -0.390 | [-0.491, -0.299] | 638 | 0.136 |
| bipolar | twin[split_half/nopool] | nll | -0.032 | [-0.039, -0.026] | 638 | 0.010 |
| depression | author_mean | se | -0.499 | [-0.567, -0.432] | 2172 | 0.097 |
| depression | author_mean | nll | -0.090 | [-0.096, -0.084] | 2172 | 0.009 |
| depression | ewma | se | -0.714 | [-0.797, -0.633] | 2172 | 0.116 |
| depression | ewma | nll | -0.106 | [-0.114, -0.100] | 2172 | 0.010 |
| depression | gap_ewma | se | -0.469 | [-0.541, -0.402] | 2172 | 0.098 |
| depression | gap_ewma | nll | -0.088 | [-0.094, -0.082] | 2172 | 0.009 |
| depression | last | se | -3.791 | [-3.955, -3.616] | 2172 | 0.242 |
| depression | last | nll | -0.293 | [-0.302, -0.284] | 2172 | 0.013 |
| depression | global_mean | se | -0.412 | [-0.618, -0.239] | 2172 | 0.280 |
| depression | global_mean | nll | -0.084 | [-0.100, -0.070] | 2172 | 0.022 |
| depression | shortcut | se | 1.018 | [0.902, 1.142] | 2172 | 0.167 |
| depression | shortcut | nll | 0.040 | [0.031, 0.050] | 2172 | 0.014 |
| depression | twin[fixed] | se | 0.347 | [0.313, 0.387] | 2172 | 0.053 |
| depression | twin[fixed] | nll | -0.021 | [-0.026, -0.017] | 2172 | 0.006 |
| depression | twin[conf_rule] | se | -0.948 | [-1.037, -0.854] | 2172 | 0.131 |
| depression | twin[conf_rule] | nll | -0.438 | [-0.483, -0.399] | 2172 | 0.061 |
| depression | twin[split_half/static] | se | -0.162 | [-0.241, -0.107] | 2172 | 0.095 |
| depression | twin[split_half/static] | nll | -0.014 | [-0.018, -0.011] | 2172 | 0.005 |
| depression | twin[split_half/rw] | se | -0.159 | [-0.237, -0.104] | 2172 | 0.093 |
| depression | twin[split_half/rw] | nll | -0.014 | [-0.017, -0.011] | 2172 | 0.005 |
| depression | twin[split_half/nopool] | se | -0.629 | [-0.689, -0.570] | 2172 | 0.085 |
| depression | twin[split_half/nopool] | nll | -0.049 | [-0.053, -0.045] | 2172 | 0.005 |
| suicidewatch | author_mean | se | -0.327 | [-0.452, -0.215] | 614 | 0.170 |
| suicidewatch | author_mean | nll | -0.062 | [-0.080, -0.042] | 614 | 0.027 |
| suicidewatch | ewma | se | -0.563 | [-0.686, -0.455] | 614 | 0.169 |
| suicidewatch | ewma | nll | -0.080 | [-0.096, -0.064] | 614 | 0.024 |
| suicidewatch | gap_ewma | se | -0.304 | [-0.427, -0.195] | 614 | 0.166 |
| suicidewatch | gap_ewma | nll | -0.060 | [-0.078, -0.041] | 614 | 0.027 |
| suicidewatch | last | se | -3.396 | [-3.612, -3.158] | 614 | 0.333 |
| suicidewatch | last | nll | -0.258 | [-0.273, -0.244] | 614 | 0.021 |
| suicidewatch | global_mean | se | -0.034 | [-0.254, 0.194] | 614 | 0.320 |
| suicidewatch | global_mean | nll | -0.038 | [-0.055, -0.024] | 614 | 0.023 |
| suicidewatch | shortcut | se | 1.243 | [1.073, 1.428] | 614 | 0.254 |
| suicidewatch | shortcut | nll | 0.078 | [0.063, 0.092] | 614 | 0.021 |
| suicidewatch | twin[fixed] | se | 0.519 | [0.448, 0.606] | 614 | 0.113 |
| suicidewatch | twin[fixed] | nll | 0.011 | [-0.002, 0.024] | 614 | 0.018 |
| suicidewatch | twin[conf_rule] | se | -1.081 | [-1.299, -0.880] | 614 | 0.310 |
| suicidewatch | twin[conf_rule] | nll | -0.389 | [-0.430, -0.351] | 614 | 0.059 |
| suicidewatch | twin[split_half/static] | se | -0.128 | [-0.198, -0.058] | 614 | 0.100 |
| suicidewatch | twin[split_half/static] | nll | -0.023 | [-0.030, -0.015] | 614 | 0.011 |
| suicidewatch | twin[split_half/rw] | se | -0.131 | [-0.200, -0.063] | 614 | 0.099 |
| suicidewatch | twin[split_half/rw] | nll | -0.023 | [-0.030, -0.015] | 614 | 0.011 |
| suicidewatch | twin[split_half/nopool] | se | -0.592 | [-0.739, -0.458] | 614 | 0.194 |
| suicidewatch | twin[split_half/nopool] | nll | -0.046 | [-0.055, -0.037] | 614 | 0.012 |

## E1 reply dose-response
beta=-0.1911 (p=5.47e-158); placebo beta=-0.0333; Gate A pass: True