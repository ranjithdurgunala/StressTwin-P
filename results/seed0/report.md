# StressTwin-P results (auto-generated; check the data source and the pilot setting in results.json before reading)

## held-out community: anxiety  (train authors 768)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.824 | 5.893 | 2.300 | 0.91 | 8.07 |
| twin[conf_rule] | 6.964 | 7.034 | 2.662 | 0.91 | 11.03 |
| twin[split_half] | 6.150 | 6.362 | 2.272 | 0.91 | 7.98 |
| twin[split_half/static] | 6.239 | 6.524 | 2.278 | 0.91 | 8.09 |
| twin[split_half/rw] | 6.239 | 6.523 | 2.278 | 0.91 | 8.09 |
| twin[split_half/nopool] | 7.009 | 7.055 | 2.335 | 0.91 | 8.45 |
| author_mean | 6.913 | 6.913 | 2.386 | 0.91 | 8.68 |
| last | 10.181 | 10.181 | 2.580 | 0.91 | 10.79 |
| ewma | 7.146 | 7.146 | 2.402 | 0.90 | 8.89 |
| gap_ewma | 6.899 | 6.899 | 2.385 | 0.91 | 8.68 |
| global_mean | 6.345 | 6.356 | 2.343 | 0.91 | 8.46 |
| shortcut | 4.843 | 4.898 | 2.208 | 0.91 | 7.41 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.91 / 8.07 | 0.91 / 8.10 | 0.90 / 7.98 |
| twin[conf_rule] | 0.91 / 11.03 | 0.91 / 10.81 | 0.90 / 10.81 |
| twin[split_half] | 0.91 / 7.98 | 0.91 / 7.96 | 0.90 / 7.87 |
| twin[split_half/static] | 0.91 / 8.09 | 0.91 / 7.99 | 0.90 / 7.89 |
| twin[split_half/rw] | 0.91 / 8.09 | 0.91 / 7.99 | 0.90 / 7.89 |
| twin[split_half/nopool] | 0.91 / 8.45 | 0.91 / 8.46 | 0.90 / 8.39 |

## held-out community: bipolar  (train authors 637)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.539 | 5.754 | 2.274 | 0.89 | 7.64 |
| twin[conf_rule] | 6.694 | 7.245 | 2.656 | 0.91 | 10.67 |
| twin[split_half] | 5.756 | 6.171 | 2.261 | 0.90 | 7.77 |
| twin[split_half/static] | 5.858 | 6.303 | 2.278 | 0.90 | 7.99 |
| twin[split_half/rw] | 5.856 | 6.299 | 2.278 | 0.90 | 7.99 |
| twin[split_half/nopool] | 6.230 | 6.244 | 2.298 | 0.90 | 8.03 |
| author_mean | 6.160 | 6.160 | 2.328 | 0.90 | 8.08 |
| last | 9.883 | 9.883 | 2.564 | 0.90 | 10.30 |
| ewma | 6.390 | 6.456 | 2.346 | 0.90 | 8.25 |
| gap_ewma | 6.153 | 6.153 | 2.328 | 0.90 | 8.07 |
| global_mean | 6.039 | 6.636 | 2.318 | 0.89 | 8.01 |
| shortcut | 4.761 | 4.794 | 2.199 | 0.90 | 7.16 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.89 / 7.64 | 0.90 / 7.68 | 0.90 / 7.88 |
| twin[conf_rule] | 0.91 / 10.67 | 0.91 / 10.47 | 0.90 / 10.60 |
| twin[split_half] | 0.90 / 7.77 | 0.90 / 7.64 | 0.90 / 7.86 |
| twin[split_half/static] | 0.90 / 7.99 | 0.89 / 7.80 | 0.90 / 8.09 |
| twin[split_half/rw] | 0.90 / 7.99 | 0.89 / 7.80 | 0.90 / 8.09 |
| twin[split_half/nopool] | 0.90 / 8.03 | 0.90 / 7.96 | 0.90 / 8.22 |

## held-out community: depression  (train authors 1500)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.782 | 5.755 | 2.296 | 0.90 | 7.89 |
| twin[conf_rule] | 7.019 | 7.032 | 2.712 | 0.91 | 10.97 |
| twin[split_half] | 6.153 | 6.024 | 2.277 | 0.90 | 7.91 |
| twin[split_half/static] | 6.349 | 6.179 | 2.293 | 0.90 | 8.17 |
| twin[split_half/rw] | 6.347 | 6.179 | 2.293 | 0.90 | 8.16 |
| twin[split_half/nopool] | 6.774 | 6.766 | 2.327 | 0.90 | 8.31 |
| author_mean | 6.667 | 6.667 | 2.368 | 0.90 | 8.42 |
| last | 9.951 | 9.951 | 2.568 | 0.90 | 10.32 |
| ewma | 6.856 | 6.856 | 2.381 | 0.90 | 8.57 |
| gap_ewma | 6.643 | 6.643 | 2.366 | 0.90 | 8.41 |
| global_mean | 6.563 | 6.639 | 2.360 | 0.90 | 8.34 |
| shortcut | 5.129 | 5.133 | 2.237 | 0.90 | 7.37 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 7.89 | 0.90 / 7.89 | 0.90 / 7.92 |
| twin[conf_rule] | 0.91 / 10.97 | 0.91 / 10.56 | 0.90 / 10.67 |
| twin[split_half] | 0.90 / 7.91 | 0.90 / 7.85 | 0.90 / 7.92 |
| twin[split_half/static] | 0.90 / 8.17 | 0.90 / 8.04 | 0.90 / 8.12 |
| twin[split_half/rw] | 0.90 / 8.16 | 0.90 / 8.03 | 0.90 / 8.12 |
| twin[split_half/nopool] | 0.90 / 8.31 | 0.90 / 8.26 | 0.90 / 8.37 |

## held-out community: suicidewatch  (train authors 613)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.928 | 5.865 | 2.309 | 0.89 | 7.78 |
| twin[conf_rule] | 7.579 | 7.480 | 2.728 | 0.91 | 11.28 |
| twin[split_half] | 6.301 | 6.099 | 2.300 | 0.89 | 7.88 |
| twin[split_half/static] | 6.452 | 6.192 | 2.314 | 0.89 | 8.04 |
| twin[split_half/rw] | 6.447 | 6.190 | 2.314 | 0.89 | 8.04 |
| twin[split_half/nopool] | 6.943 | 6.937 | 2.346 | 0.89 | 8.23 |
| author_mean | 6.810 | 6.810 | 2.380 | 0.89 | 8.26 |
| last | 10.029 | 10.029 | 2.572 | 0.89 | 10.20 |
| ewma | 7.054 | 7.054 | 2.397 | 0.89 | 8.41 |
| gap_ewma | 6.780 | 6.780 | 2.377 | 0.89 | 8.24 |
| global_mean | 6.451 | 6.468 | 2.352 | 0.89 | 8.08 |
| shortcut | 5.178 | 5.189 | 2.243 | 0.89 | 7.19 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.89 / 7.78 | 0.89 / 7.62 | 0.90 / 7.98 |
| twin[conf_rule] | 0.91 / 11.28 | 0.90 / 10.99 | 0.90 / 11.25 |
| twin[split_half] | 0.89 / 7.88 | 0.88 / 7.68 | 0.90 / 8.16 |
| twin[split_half/static] | 0.89 / 8.04 | 0.88 / 7.82 | 0.90 / 8.28 |
| twin[split_half/rw] | 0.89 / 8.04 | 0.88 / 7.82 | 0.90 / 8.28 |
| twin[split_half/nopool] | 0.89 / 8.23 | 0.89 / 8.15 | 0.90 / 8.40 |


## Twin vs baselines, paired difference with 95% author-bootstrap CI (negative = twin better)
| community | comparator | metric | diff | 95% CI | authors | min detectable (80% power) |
|---|---|---|---|---|---|---|
| anxiety | author_mean | se | -0.763 | [-0.886, -0.661] | 769 | 0.166 |
| anxiety | author_mean | nll | -0.113 | [-0.125, -0.104] | 769 | 0.015 |
| anxiety | ewma | se | -0.995 | [-1.139, -0.867] | 769 | 0.194 |
| anxiety | ewma | nll | -0.130 | [-0.142, -0.120] | 769 | 0.016 |
| anxiety | gap_ewma | se | -0.749 | [-0.869, -0.646] | 769 | 0.164 |
| anxiety | gap_ewma | nll | -0.112 | [-0.123, -0.103] | 769 | 0.015 |
| anxiety | last | se | -4.031 | [-4.358, -3.745] | 769 | 0.427 |
| anxiety | last | nll | -0.308 | [-0.322, -0.295] | 769 | 0.019 |
| anxiety | global_mean | se | -0.194 | [-0.326, -0.062] | 769 | 0.191 |
| anxiety | global_mean | nll | -0.071 | [-0.082, -0.060] | 769 | 0.016 |
| anxiety | shortcut | se | 1.308 | [1.143, 1.483] | 769 | 0.249 |
| anxiety | shortcut | nll | 0.064 | [0.050, 0.077] | 769 | 0.020 |
| anxiety | twin[fixed] | se | 0.327 | [0.281, 0.369] | 769 | 0.064 |
| anxiety | twin[fixed] | nll | -0.027 | [-0.034, -0.021] | 769 | 0.010 |
| anxiety | twin[conf_rule] | se | -0.814 | [-0.953, -0.686] | 769 | 0.191 |
| anxiety | twin[conf_rule] | nll | -0.390 | [-0.431, -0.352] | 769 | 0.055 |
| anxiety | twin[split_half/static] | se | -0.089 | [-0.132, -0.051] | 769 | 0.058 |
| anxiety | twin[split_half/static] | nll | -0.005 | [-0.008, -0.002] | 769 | 0.004 |
| anxiety | twin[split_half/rw] | se | -0.088 | [-0.131, -0.051] | 769 | 0.057 |
| anxiety | twin[split_half/rw] | nll | -0.005 | [-0.008, -0.002] | 769 | 0.004 |
| anxiety | twin[split_half/nopool] | se | -0.859 | [-0.986, -0.752] | 769 | 0.169 |
| anxiety | twin[split_half/nopool] | nll | -0.063 | [-0.070, -0.057] | 769 | 0.010 |
| bipolar | author_mean | se | -0.403 | [-0.487, -0.335] | 638 | 0.108 |
| bipolar | author_mean | nll | -0.067 | [-0.076, -0.059] | 638 | 0.011 |
| bipolar | ewma | se | -0.634 | [-0.736, -0.539] | 638 | 0.141 |
| bipolar | ewma | nll | -0.085 | [-0.095, -0.077] | 638 | 0.014 |
| bipolar | gap_ewma | se | -0.397 | [-0.479, -0.329] | 638 | 0.107 |
| bipolar | gap_ewma | nll | -0.067 | [-0.075, -0.059] | 638 | 0.011 |
| bipolar | last | se | -4.127 | [-4.325, -3.922] | 638 | 0.300 |
| bipolar | last | nll | -0.303 | [-0.313, -0.293] | 638 | 0.014 |
| bipolar | global_mean | se | -0.283 | [-0.446, -0.141] | 638 | 0.215 |
| bipolar | global_mean | nll | -0.057 | [-0.071, -0.045] | 638 | 0.019 |
| bipolar | shortcut | se | 0.995 | [0.858, 1.128] | 638 | 0.190 |
| bipolar | shortcut | nll | 0.062 | [0.050, 0.073] | 638 | 0.018 |
| bipolar | twin[fixed] | se | 0.217 | [0.184, 0.252] | 638 | 0.051 |
| bipolar | twin[fixed] | nll | -0.013 | [-0.018, -0.008] | 638 | 0.007 |
| bipolar | twin[conf_rule] | se | -0.938 | [-1.056, -0.827] | 638 | 0.161 |
| bipolar | twin[conf_rule] | nll | -0.395 | [-0.438, -0.357] | 638 | 0.061 |
| bipolar | twin[split_half/static] | se | -0.101 | [-0.142, -0.061] | 638 | 0.059 |
| bipolar | twin[split_half/static] | nll | -0.017 | [-0.021, -0.013] | 638 | 0.006 |
| bipolar | twin[split_half/rw] | se | -0.100 | [-0.141, -0.060] | 638 | 0.058 |
| bipolar | twin[split_half/rw] | nll | -0.017 | [-0.021, -0.013] | 638 | 0.006 |
| bipolar | twin[split_half/nopool] | se | -0.474 | [-0.554, -0.409] | 638 | 0.104 |
| bipolar | twin[split_half/nopool] | nll | -0.037 | [-0.043, -0.033] | 638 | 0.007 |
| depression | author_mean | se | -0.515 | [-0.583, -0.456] | 2172 | 0.092 |
| depression | author_mean | nll | -0.091 | [-0.097, -0.085] | 2172 | 0.008 |
| depression | ewma | se | -0.703 | [-0.775, -0.625] | 2172 | 0.110 |
| depression | ewma | nll | -0.104 | [-0.111, -0.098] | 2172 | 0.009 |
| depression | gap_ewma | se | -0.491 | [-0.558, -0.426] | 2172 | 0.092 |
| depression | gap_ewma | nll | -0.089 | [-0.095, -0.084] | 2172 | 0.008 |
| depression | last | se | -3.798 | [-3.967, -3.640] | 2172 | 0.241 |
| depression | last | nll | -0.291 | [-0.300, -0.282] | 2172 | 0.013 |
| depression | global_mean | se | -0.411 | [-0.577, -0.266] | 2172 | 0.223 |
| depression | global_mean | nll | -0.083 | [-0.096, -0.071] | 2172 | 0.018 |
| depression | shortcut | se | 1.024 | [0.914, 1.131] | 2172 | 0.155 |
| depression | shortcut | nll | 0.041 | [0.032, 0.049] | 2172 | 0.012 |
| depression | twin[fixed] | se | 0.371 | [0.335, 0.412] | 2172 | 0.054 |
| depression | twin[fixed] | nll | -0.019 | [-0.023, -0.015] | 2172 | 0.006 |
| depression | twin[conf_rule] | se | -0.866 | [-0.956, -0.777] | 2172 | 0.127 |
| depression | twin[conf_rule] | nll | -0.435 | [-0.487, -0.394] | 2172 | 0.067 |
| depression | twin[split_half/static] | se | -0.196 | [-0.274, -0.133] | 2172 | 0.102 |
| depression | twin[split_half/static] | nll | -0.016 | [-0.020, -0.013] | 2172 | 0.005 |
| depression | twin[split_half/rw] | se | -0.194 | [-0.271, -0.131] | 2172 | 0.100 |
| depression | twin[split_half/rw] | nll | -0.016 | [-0.020, -0.012] | 2172 | 0.005 |
| depression | twin[split_half/nopool] | se | -0.622 | [-0.681, -0.564] | 2172 | 0.083 |
| depression | twin[split_half/nopool] | nll | -0.050 | [-0.054, -0.047] | 2172 | 0.005 |
| suicidewatch | author_mean | se | -0.509 | [-0.638, -0.392] | 614 | 0.180 |
| suicidewatch | author_mean | nll | -0.080 | [-0.094, -0.065] | 614 | 0.021 |
| suicidewatch | ewma | se | -0.754 | [-0.881, -0.629] | 614 | 0.185 |
| suicidewatch | ewma | nll | -0.098 | [-0.111, -0.083] | 614 | 0.020 |
| suicidewatch | gap_ewma | se | -0.479 | [-0.611, -0.360] | 614 | 0.181 |
| suicidewatch | gap_ewma | nll | -0.078 | [-0.092, -0.063] | 614 | 0.021 |
| suicidewatch | last | se | -3.729 | [-3.970, -3.481] | 614 | 0.354 |
| suicidewatch | last | nll | -0.272 | [-0.285, -0.259] | 614 | 0.019 |
| suicidewatch | global_mean | se | -0.150 | [-0.325, 0.002] | 614 | 0.228 |
| suicidewatch | global_mean | nll | -0.052 | [-0.068, -0.040] | 614 | 0.020 |
| suicidewatch | shortcut | se | 1.123 | [0.945, 1.295] | 614 | 0.257 |
| suicidewatch | shortcut | nll | 0.057 | [0.040, 0.072] | 614 | 0.023 |
| suicidewatch | twin[fixed] | se | 0.373 | [0.328, 0.415] | 614 | 0.063 |
| suicidewatch | twin[fixed] | nll | -0.009 | [-0.018, -0.000] | 614 | 0.013 |
| suicidewatch | twin[conf_rule] | se | -1.278 | [-1.482, -1.070] | 614 | 0.304 |
| suicidewatch | twin[conf_rule] | nll | -0.428 | [-0.475, -0.384] | 614 | 0.064 |
| suicidewatch | twin[split_half/static] | se | -0.151 | [-0.207, -0.092] | 614 | 0.082 |
| suicidewatch | twin[split_half/static] | nll | -0.014 | [-0.019, -0.010] | 614 | 0.007 |
| suicidewatch | twin[split_half/rw] | se | -0.147 | [-0.200, -0.090] | 614 | 0.079 |
| suicidewatch | twin[split_half/rw] | nll | -0.014 | [-0.019, -0.009] | 614 | 0.007 |
| suicidewatch | twin[split_half/nopool] | se | -0.642 | [-0.765, -0.536] | 614 | 0.164 |
| suicidewatch | twin[split_half/nopool] | nll | -0.046 | [-0.054, -0.039] | 614 | 0.010 |

## E1 reply dose-response
beta=-0.1911 (p=5.47e-158); placebo beta=-0.0333; Gate A pass: True