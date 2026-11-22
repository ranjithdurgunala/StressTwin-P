# StressTwin-P results (auto-generated; check the data source and the pilot setting in results.json before reading)

## held-out community: anxiety  (train authors 768)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.506 | 8.638 | 2.490 | 0.90 | 9.51 |
| twin[conf_rule] | 10.606 | 10.516 | 3.156 | 0.90 | 13.94 |
| twin[split_half] | 8.848 | 9.043 | 2.449 | 0.90 | 9.28 |
| twin[split_half/static] | 8.915 | 9.151 | 2.450 | 0.90 | 9.40 |
| twin[split_half/rw] | 8.915 | 9.151 | 2.450 | 0.90 | 9.40 |
| twin[split_half/nopool] | 10.034 | 10.002 | 2.510 | 0.90 | 9.81 |
| author_mean | 9.955 | 9.955 | 2.568 | 0.90 | 10.29 |
| last | 15.482 | 15.482 | 2.790 | 0.89 | 12.56 |
| ewma | 10.448 | 10.448 | 2.592 | 0.90 | 10.48 |
| gap_ewma | 9.951 | 9.951 | 2.568 | 0.90 | 10.29 |
| global_mean | 9.342 | 9.360 | 2.536 | 0.90 | 9.99 |
| shortcut | 6.903 | 6.960 | 2.385 | 0.90 | 8.69 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.51 | 0.90 / 9.47 | 0.90 / 9.66 |
| twin[conf_rule] | 0.90 / 13.94 | 0.91 / 14.15 | 0.90 / 13.95 |
| twin[split_half] | 0.90 / 9.28 | 0.90 / 9.24 | 0.90 / 9.29 |
| twin[split_half/static] | 0.90 / 9.40 | 0.90 / 9.29 | 0.90 / 9.37 |
| twin[split_half/rw] | 0.90 / 9.40 | 0.90 / 9.30 | 0.90 / 9.36 |
| twin[split_half/nopool] | 0.90 / 9.81 | 0.90 / 9.79 | 0.90 / 10.01 |

## held-out community: bipolar  (train authors 637)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.205 | 8.485 | 2.472 | 0.89 | 9.17 |
| twin[conf_rule] | 10.480 | 11.490 | 3.112 | 0.90 | 13.44 |
| twin[split_half] | 8.721 | 8.959 | 2.458 | 0.90 | 9.53 |
| twin[split_half/static] | 8.932 | 9.111 | 2.478 | 0.91 | 9.95 |
| twin[split_half/rw] | 8.909 | 9.085 | 2.477 | 0.91 | 9.95 |
| twin[split_half/nopool] | 9.392 | 9.209 | 2.494 | 0.90 | 9.81 |
| author_mean | 9.079 | 9.079 | 2.522 | 0.90 | 9.67 |
| last | 14.732 | 14.732 | 2.765 | 0.89 | 12.31 |
| ewma | 9.522 | 9.624 | 2.547 | 0.89 | 9.83 |
| gap_ewma | 9.062 | 9.062 | 2.522 | 0.90 | 9.67 |
| global_mean | 8.870 | 10.120 | 2.511 | 0.90 | 9.64 |
| shortcut | 6.964 | 7.202 | 2.390 | 0.89 | 8.41 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.89 / 9.17 | 0.89 / 9.16 | 0.90 / 9.48 |
| twin[conf_rule] | 0.90 / 13.44 | 0.89 / 12.77 | 0.90 / 14.45 |
| twin[split_half] | 0.90 / 9.53 | 0.90 / 9.37 | 0.90 / 9.53 |
| twin[split_half/static] | 0.91 / 9.95 | 0.90 / 9.72 | 0.90 / 9.89 |
| twin[split_half/rw] | 0.91 / 9.95 | 0.90 / 9.73 | 0.90 / 9.88 |
| twin[split_half/nopool] | 0.90 / 9.81 | 0.90 / 9.69 | 0.90 / 9.90 |

## held-out community: depression  (train authors 1500)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.503 | 8.454 | 2.490 | 0.90 | 9.36 |
| twin[conf_rule] | 10.471 | 10.689 | 3.084 | 0.91 | 14.77 |
| twin[split_half] | 8.926 | 8.846 | 2.457 | 0.90 | 9.30 |
| twin[split_half/static] | 9.095 | 8.995 | 2.464 | 0.90 | 9.54 |
| twin[split_half/rw] | 9.094 | 8.995 | 2.464 | 0.90 | 9.53 |
| twin[split_half/nopool] | 9.829 | 9.897 | 2.506 | 0.90 | 9.77 |
| author_mean | 9.738 | 9.738 | 2.558 | 0.89 | 9.97 |
| last | 14.719 | 14.719 | 2.765 | 0.89 | 12.14 |
| ewma | 10.066 | 10.066 | 2.575 | 0.89 | 10.11 |
| gap_ewma | 9.714 | 9.714 | 2.557 | 0.89 | 9.95 |
| global_mean | 9.495 | 9.557 | 2.544 | 0.90 | 10.05 |
| shortcut | 7.375 | 7.379 | 2.418 | 0.89 | 8.74 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 9.36 | 0.89 / 9.28 | 0.90 / 9.52 |
| twin[conf_rule] | 0.91 / 14.77 | 0.90 / 14.29 | 0.90 / 14.92 |
| twin[split_half] | 0.90 / 9.30 | 0.89 / 9.20 | 0.90 / 9.38 |
| twin[split_half/static] | 0.90 / 9.54 | 0.90 / 9.37 | 0.90 / 9.52 |
| twin[split_half/rw] | 0.90 / 9.53 | 0.90 / 9.37 | 0.90 / 9.50 |
| twin[split_half/nopool] | 0.90 / 9.77 | 0.90 / 9.73 | 0.90 / 9.97 |

## held-out community: suicidewatch  (train authors 613)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 8.147 | 8.104 | 2.467 | 0.91 | 9.48 |
| twin[conf_rule] | 10.674 | 10.761 | 3.120 | 0.90 | 15.08 |
| twin[split_half] | 8.643 | 8.427 | 2.458 | 0.91 | 9.73 |
| twin[split_half/static] | 8.820 | 8.552 | 2.474 | 0.91 | 10.01 |
| twin[split_half/rw] | 8.816 | 8.548 | 2.474 | 0.91 | 10.00 |
| twin[split_half/nopool] | 9.383 | 9.392 | 2.497 | 0.91 | 10.08 |
| author_mean | 9.184 | 9.184 | 2.528 | 0.91 | 10.25 |
| last | 13.886 | 13.886 | 2.735 | 0.91 | 12.49 |
| ewma | 9.505 | 9.505 | 2.546 | 0.91 | 10.43 |
| gap_ewma | 9.137 | 9.137 | 2.526 | 0.91 | 10.23 |
| global_mean | 9.125 | 9.050 | 2.524 | 0.90 | 9.96 |
| shortcut | 7.258 | 7.158 | 2.410 | 0.90 | 8.78 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.91 / 9.48 | 0.91 / 9.35 | 0.90 / 9.24 |
| twin[conf_rule] | 0.90 / 15.08 | 0.89 / 14.81 | 0.90 / 15.89 |
| twin[split_half] | 0.91 / 9.73 | 0.91 / 9.55 | 0.90 / 9.45 |
| twin[split_half/static] | 0.91 / 10.01 | 0.90 / 9.76 | 0.90 / 9.73 |
| twin[split_half/rw] | 0.91 / 10.00 | 0.90 / 9.75 | 0.90 / 9.73 |
| twin[split_half/nopool] | 0.91 / 10.08 | 0.91 / 9.97 | 0.90 / 9.88 |


## Twin vs baselines, paired difference with 95% author-bootstrap CI (negative = twin better)
| community | comparator | metric | diff | 95% CI | authors | min detectable (80% power) |
|---|---|---|---|---|---|---|
| anxiety | author_mean | se | -1.107 | [-1.280, -0.955] | 769 | 0.232 |
| anxiety | author_mean | nll | -0.119 | [-0.130, -0.108] | 769 | 0.015 |
| anxiety | ewma | se | -1.600 | [-1.789, -1.432] | 769 | 0.251 |
| anxiety | ewma | nll | -0.143 | [-0.154, -0.133] | 769 | 0.015 |
| anxiety | gap_ewma | se | -1.103 | [-1.272, -0.955] | 769 | 0.230 |
| anxiety | gap_ewma | nll | -0.118 | [-0.129, -0.108] | 769 | 0.015 |
| anxiety | last | se | -6.634 | [-7.108, -6.189] | 769 | 0.659 |
| anxiety | last | nll | -0.340 | [-0.355, -0.327] | 769 | 0.020 |
| anxiety | global_mean | se | -0.494 | [-0.702, -0.289] | 769 | 0.305 |
| anxiety | global_mean | nll | -0.087 | [-0.098, -0.075] | 769 | 0.017 |
| anxiety | shortcut | se | 1.945 | [1.692, 2.188] | 769 | 0.369 |
| anxiety | shortcut | nll | 0.065 | [0.048, 0.077] | 769 | 0.021 |
| anxiety | twin[fixed] | se | 0.342 | [0.282, 0.410] | 769 | 0.091 |
| anxiety | twin[fixed] | nll | -0.040 | [-0.047, -0.034] | 769 | 0.009 |
| anxiety | twin[conf_rule] | se | -1.758 | [-2.027, -1.499] | 769 | 0.376 |
| anxiety | twin[conf_rule] | nll | -0.706 | [-0.868, -0.580] | 769 | 0.206 |
| anxiety | twin[split_half/static] | se | -0.067 | [-0.126, -0.009] | 769 | 0.085 |
| anxiety | twin[split_half/static] | nll | -0.001 | [-0.004, 0.003] | 769 | 0.005 |
| anxiety | twin[split_half/rw] | se | -0.067 | [-0.124, -0.009] | 769 | 0.083 |
| anxiety | twin[split_half/rw] | nll | -0.001 | [-0.004, 0.003] | 769 | 0.004 |
| anxiety | twin[split_half/nopool] | se | -1.186 | [-1.354, -1.039] | 769 | 0.221 |
| anxiety | twin[split_half/nopool] | nll | -0.061 | [-0.068, -0.054] | 769 | 0.010 |
| bipolar | author_mean | se | -0.358 | [-0.642, -0.057] | 638 | 0.450 |
| bipolar | author_mean | nll | -0.065 | [-0.084, -0.046] | 638 | 0.029 |
| bipolar | ewma | se | -0.802 | [-1.065, -0.574] | 638 | 0.354 |
| bipolar | ewma | nll | -0.089 | [-0.106, -0.074] | 638 | 0.024 |
| bipolar | gap_ewma | se | -0.341 | [-0.628, -0.042] | 638 | 0.456 |
| bipolar | gap_ewma | nll | -0.064 | [-0.083, -0.045] | 638 | 0.030 |
| bipolar | last | se | -6.011 | [-6.492, -5.534] | 638 | 0.686 |
| bipolar | last | nll | -0.307 | [-0.319, -0.293] | 638 | 0.018 |
| bipolar | global_mean | se | -0.149 | [-0.438, 0.098] | 638 | 0.366 |
| bipolar | global_mean | nll | -0.053 | [-0.068, -0.038] | 638 | 0.021 |
| bipolar | shortcut | se | 1.757 | [1.355, 2.135] | 638 | 0.574 |
| bipolar | shortcut | nll | 0.067 | [0.042, 0.092] | 638 | 0.037 |
| bipolar | twin[fixed] | se | 0.515 | [0.410, 0.624] | 638 | 0.158 |
| bipolar | twin[fixed] | nll | -0.014 | [-0.022, -0.007] | 638 | 0.011 |
| bipolar | twin[conf_rule] | se | -1.759 | [-2.246, -1.321] | 638 | 0.734 |
| bipolar | twin[conf_rule] | nll | -0.654 | [-0.759, -0.543] | 638 | 0.160 |
| bipolar | twin[split_half/static] | se | -0.211 | [-0.271, -0.150] | 638 | 0.090 |
| bipolar | twin[split_half/static] | nll | -0.020 | [-0.029, -0.012] | 638 | 0.012 |
| bipolar | twin[split_half/rw] | se | -0.188 | [-0.260, -0.130] | 638 | 0.096 |
| bipolar | twin[split_half/rw] | nll | -0.019 | [-0.028, -0.011] | 638 | 0.012 |
| bipolar | twin[split_half/nopool] | se | -0.671 | [-0.838, -0.527] | 638 | 0.230 |
| bipolar | twin[split_half/nopool] | nll | -0.036 | [-0.044, -0.029] | 638 | 0.011 |
| depression | author_mean | se | -0.811 | [-0.901, -0.721] | 2172 | 0.132 |
| depression | author_mean | nll | -0.101 | [-0.107, -0.095] | 2172 | 0.009 |
| depression | ewma | se | -1.140 | [-1.236, -1.043] | 2172 | 0.140 |
| depression | ewma | nll | -0.118 | [-0.124, -0.112] | 2172 | 0.009 |
| depression | gap_ewma | se | -0.788 | [-0.877, -0.695] | 2172 | 0.131 |
| depression | gap_ewma | nll | -0.100 | [-0.106, -0.094] | 2172 | 0.009 |
| depression | last | se | -5.793 | [-6.047, -5.535] | 2172 | 0.359 |
| depression | last | nll | -0.308 | [-0.316, -0.299] | 2172 | 0.013 |
| depression | global_mean | se | -0.568 | [-0.756, -0.410] | 2172 | 0.249 |
| depression | global_mean | nll | -0.088 | [-0.098, -0.078] | 2172 | 0.014 |
| depression | shortcut | se | 1.551 | [1.400, 1.711] | 2172 | 0.216 |
| depression | shortcut | nll | 0.038 | [0.030, 0.047] | 2172 | 0.012 |
| depression | twin[fixed] | se | 0.424 | [0.387, 0.462] | 2172 | 0.054 |
| depression | twin[fixed] | nll | -0.033 | [-0.037, -0.029] | 2172 | 0.006 |
| depression | twin[conf_rule] | se | -1.545 | [-1.684, -1.412] | 2172 | 0.196 |
| depression | twin[conf_rule] | nll | -0.627 | [-0.684, -0.576] | 2172 | 0.078 |
| depression | twin[split_half/static] | se | -0.169 | [-0.225, -0.117] | 2172 | 0.077 |
| depression | twin[split_half/static] | nll | -0.008 | [-0.011, -0.005] | 2172 | 0.004 |
| depression | twin[split_half/rw] | se | -0.168 | [-0.222, -0.116] | 2172 | 0.076 |
| depression | twin[split_half/rw] | nll | -0.008 | [-0.011, -0.005] | 2172 | 0.004 |
| depression | twin[split_half/nopool] | se | -0.902 | [-0.985, -0.814] | 2172 | 0.119 |
| depression | twin[split_half/nopool] | nll | -0.050 | [-0.053, -0.046] | 2172 | 0.005 |
| suicidewatch | author_mean | se | -0.542 | [-0.725, -0.387] | 614 | 0.247 |
| suicidewatch | author_mean | nll | -0.070 | [-0.087, -0.053] | 614 | 0.026 |
| suicidewatch | ewma | se | -0.862 | [-1.034, -0.700] | 614 | 0.249 |
| suicidewatch | ewma | nll | -0.087 | [-0.103, -0.072] | 614 | 0.023 |
| suicidewatch | gap_ewma | se | -0.494 | [-0.671, -0.340] | 614 | 0.242 |
| suicidewatch | gap_ewma | nll | -0.067 | [-0.085, -0.050] | 614 | 0.025 |
| suicidewatch | last | se | -5.243 | [-5.570, -4.917] | 614 | 0.458 |
| suicidewatch | last | nll | -0.276 | [-0.291, -0.262] | 614 | 0.022 |
| suicidewatch | global_mean | se | -0.483 | [-0.835, -0.164] | 614 | 0.483 |
| suicidewatch | global_mean | nll | -0.066 | [-0.082, -0.052] | 614 | 0.021 |
| suicidewatch | shortcut | se | 1.385 | [1.090, 1.667] | 614 | 0.428 |
| suicidewatch | shortcut | nll | 0.048 | [0.025, 0.069] | 614 | 0.031 |
| suicidewatch | twin[fixed] | se | 0.496 | [0.417, 0.575] | 614 | 0.113 |
| suicidewatch | twin[fixed] | nll | -0.008 | [-0.021, 0.004] | 614 | 0.018 |
| suicidewatch | twin[conf_rule] | se | -2.031 | [-2.355, -1.725] | 614 | 0.459 |
| suicidewatch | twin[conf_rule] | nll | -0.661 | [-0.735, -0.590] | 614 | 0.105 |
| suicidewatch | twin[split_half/static] | se | -0.177 | [-0.266, -0.090] | 614 | 0.127 |
| suicidewatch | twin[split_half/static] | nll | -0.016 | [-0.021, -0.010] | 614 | 0.008 |
| suicidewatch | twin[split_half/rw] | se | -0.174 | [-0.260, -0.090] | 614 | 0.121 |
| suicidewatch | twin[split_half/rw] | nll | -0.015 | [-0.020, -0.010] | 614 | 0.007 |
| suicidewatch | twin[split_half/nopool] | se | -0.740 | [-0.919, -0.586] | 614 | 0.241 |
| suicidewatch | twin[split_half/nopool] | nll | -0.039 | [-0.047, -0.032] | 614 | 0.011 |

## E1 reply dose-response
beta=-0.2350 (p=7.48e-173); placebo beta=-0.0423; Gate A pass: True