# StressTwin-P results (auto-generated; check the data source and the pilot setting in results.json before reading)

## held-out community: anxiety  (train authors 768)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.911 | 5.998 | 2.307 | 0.90 | 7.99 |
| twin[conf_rule] | 7.196 | 7.210 | 2.724 | 0.91 | 10.77 |
| twin[split_half] | 6.220 | 6.358 | 2.278 | 0.90 | 7.88 |
| twin[split_half/static] | 6.278 | 6.453 | 2.280 | 0.91 | 8.02 |
| twin[split_half/rw] | 6.279 | 6.453 | 2.280 | 0.91 | 8.02 |
| twin[split_half/nopool] | 7.070 | 7.041 | 2.339 | 0.90 | 8.32 |
| author_mean | 6.945 | 6.945 | 2.388 | 0.90 | 8.66 |
| last | 10.703 | 10.703 | 2.605 | 0.89 | 10.54 |
| ewma | 7.281 | 7.281 | 2.412 | 0.90 | 8.81 |
| gap_ewma | 6.943 | 6.943 | 2.388 | 0.90 | 8.65 |
| global_mean | 6.488 | 6.504 | 2.354 | 0.90 | 8.35 |
| shortcut | 4.901 | 4.942 | 2.214 | 0.90 | 7.38 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 7.99 | 0.90 / 8.01 | 0.90 / 8.04 |
| twin[conf_rule] | 0.91 / 10.77 | 0.90 / 10.67 | 0.90 / 10.85 |
| twin[split_half] | 0.90 / 7.88 | 0.90 / 7.84 | 0.90 / 7.86 |
| twin[split_half/static] | 0.91 / 8.02 | 0.90 / 7.92 | 0.90 / 7.94 |
| twin[split_half/rw] | 0.91 / 8.02 | 0.90 / 7.92 | 0.90 / 7.94 |
| twin[split_half/nopool] | 0.90 / 8.32 | 0.90 / 8.30 | 0.90 / 8.44 |

## held-out community: bipolar  (train authors 637)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.640 | 5.844 | 2.284 | 0.89 | 7.58 |
| twin[conf_rule] | 7.023 | 7.543 | 2.715 | 0.90 | 10.45 |
| twin[split_half] | 5.999 | 6.270 | 2.280 | 0.90 | 7.94 |
| twin[split_half/static] | 6.154 | 6.404 | 2.303 | 0.91 | 8.33 |
| twin[split_half/rw] | 6.143 | 6.391 | 2.303 | 0.91 | 8.33 |
| twin[split_half/nopool] | 6.479 | 6.397 | 2.317 | 0.90 | 8.18 |
| author_mean | 6.255 | 6.255 | 2.336 | 0.90 | 8.00 |
| last | 10.105 | 10.105 | 2.576 | 0.89 | 10.17 |
| ewma | 6.564 | 6.626 | 2.361 | 0.89 | 8.13 |
| gap_ewma | 6.246 | 6.246 | 2.336 | 0.90 | 8.00 |
| global_mean | 6.119 | 7.035 | 2.325 | 0.89 | 7.96 |
| shortcut | 4.880 | 5.057 | 2.212 | 0.89 | 7.05 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.89 / 7.58 | 0.89 / 7.59 | 0.90 / 7.90 |
| twin[conf_rule] | 0.90 / 10.45 | 0.89 / 9.89 | 0.90 / 10.91 |
| twin[split_half] | 0.90 / 7.94 | 0.90 / 7.86 | 0.90 / 7.96 |
| twin[split_half/static] | 0.91 / 8.33 | 0.90 / 8.12 | 0.90 / 8.27 |
| twin[split_half/rw] | 0.91 / 8.33 | 0.90 / 8.12 | 0.90 / 8.26 |
| twin[split_half/nopool] | 0.90 / 8.18 | 0.90 / 8.11 | 0.90 / 8.26 |

## held-out community: depression  (train authors 1500)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.886 | 5.853 | 2.306 | 0.89 | 7.78 |
| twin[conf_rule] | 7.187 | 7.207 | 2.742 | 0.90 | 10.72 |
| twin[split_half] | 6.220 | 6.160 | 2.282 | 0.90 | 7.80 |
| twin[split_half/static] | 6.348 | 6.271 | 2.292 | 0.90 | 8.03 |
| twin[split_half/rw] | 6.347 | 6.271 | 2.292 | 0.90 | 8.03 |
| twin[split_half/nopool] | 6.877 | 6.929 | 2.333 | 0.90 | 8.19 |
| author_mean | 6.784 | 6.784 | 2.377 | 0.89 | 8.29 |
| last | 10.216 | 10.216 | 2.583 | 0.89 | 10.10 |
| ewma | 7.008 | 7.008 | 2.394 | 0.89 | 8.41 |
| gap_ewma | 6.766 | 6.766 | 2.376 | 0.89 | 8.27 |
| global_mean | 6.536 | 6.587 | 2.358 | 0.90 | 8.32 |
| shortcut | 5.191 | 5.193 | 2.243 | 0.89 | 7.29 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.89 / 7.78 | 0.89 / 7.77 | 0.90 / 7.99 |
| twin[conf_rule] | 0.90 / 10.72 | 0.89 / 10.13 | 0.90 / 10.92 |
| twin[split_half] | 0.90 / 7.80 | 0.89 / 7.72 | 0.90 / 7.93 |
| twin[split_half/static] | 0.90 / 8.03 | 0.89 / 7.91 | 0.90 / 8.12 |
| twin[split_half/rw] | 0.90 / 8.03 | 0.89 / 7.91 | 0.90 / 8.11 |
| twin[split_half/nopool] | 0.90 / 8.19 | 0.89 / 8.16 | 0.90 / 8.40 |

## held-out community: suicidewatch  (train authors 613)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.616 | 5.582 | 2.280 | 0.91 | 7.90 |
| twin[conf_rule] | 7.389 | 7.329 | 2.744 | 0.90 | 11.07 |
| twin[split_half] | 5.977 | 5.835 | 2.279 | 0.91 | 8.15 |
| twin[split_half/static] | 6.095 | 5.918 | 2.295 | 0.91 | 8.43 |
| twin[split_half/rw] | 6.093 | 5.916 | 2.295 | 0.91 | 8.43 |
| twin[split_half/nopool] | 6.536 | 6.558 | 2.320 | 0.91 | 8.46 |
| author_mean | 6.363 | 6.363 | 2.345 | 0.91 | 8.57 |
| last | 9.639 | 9.639 | 2.552 | 0.91 | 10.42 |
| ewma | 6.604 | 6.604 | 2.364 | 0.91 | 8.72 |
| gap_ewma | 6.333 | 6.333 | 2.343 | 0.91 | 8.55 |
| global_mean | 6.189 | 6.155 | 2.330 | 0.90 | 8.27 |
| shortcut | 5.020 | 4.959 | 2.226 | 0.90 | 7.34 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.91 / 7.90 | 0.91 / 7.80 | 0.90 / 7.77 |
| twin[conf_rule] | 0.90 / 11.07 | 0.90 / 10.66 | 0.90 / 11.17 |
| twin[split_half] | 0.91 / 8.15 | 0.91 / 8.07 | 0.90 / 7.94 |
| twin[split_half/static] | 0.91 / 8.43 | 0.91 / 8.28 | 0.90 / 8.15 |
| twin[split_half/rw] | 0.91 / 8.43 | 0.91 / 8.29 | 0.90 / 8.14 |
| twin[split_half/nopool] | 0.91 / 8.46 | 0.91 / 8.39 | 0.90 / 8.26 |


## Twin vs baselines, paired difference with 95% author-bootstrap CI (negative = twin better)
| community | comparator | metric | diff | 95% CI | authors | min detectable (80% power) |
|---|---|---|---|---|---|---|
| anxiety | author_mean | se | -0.724 | [-0.861, -0.612] | 769 | 0.171 |
| anxiety | author_mean | nll | -0.110 | [-0.122, -0.100] | 769 | 0.016 |
| anxiety | ewma | se | -1.061 | [-1.203, -0.938] | 769 | 0.187 |
| anxiety | ewma | nll | -0.134 | [-0.145, -0.124] | 769 | 0.016 |
| anxiety | gap_ewma | se | -0.723 | [-0.858, -0.613] | 769 | 0.169 |
| anxiety | gap_ewma | nll | -0.110 | [-0.122, -0.100] | 769 | 0.016 |
| anxiety | last | se | -4.483 | [-4.803, -4.165] | 769 | 0.456 |
| anxiety | last | nll | -0.327 | [-0.341, -0.313] | 769 | 0.020 |
| anxiety | global_mean | se | -0.268 | [-0.420, -0.123] | 769 | 0.206 |
| anxiety | global_mean | nll | -0.076 | [-0.088, -0.064] | 769 | 0.017 |
| anxiety | shortcut | se | 1.319 | [1.138, 1.485] | 769 | 0.257 |
| anxiety | shortcut | nll | 0.064 | [0.049, 0.077] | 769 | 0.021 |
| anxiety | twin[fixed] | se | 0.309 | [0.264, 0.360] | 769 | 0.070 |
| anxiety | twin[fixed] | nll | -0.029 | [-0.036, -0.023] | 769 | 0.009 |
| anxiety | twin[conf_rule] | se | -0.976 | [-1.131, -0.834] | 769 | 0.209 |
| anxiety | twin[conf_rule] | nll | -0.446 | [-0.524, -0.387] | 769 | 0.101 |
| anxiety | twin[split_half/static] | se | -0.058 | [-0.107, -0.009] | 769 | 0.072 |
| anxiety | twin[split_half/static] | nll | -0.002 | [-0.006, 0.002] | 769 | 0.005 |
| anxiety | twin[split_half/rw] | se | -0.058 | [-0.107, -0.009] | 769 | 0.071 |
| anxiety | twin[split_half/rw] | nll | -0.002 | [-0.006, 0.002] | 769 | 0.005 |
| anxiety | twin[split_half/nopool] | se | -0.850 | [-0.978, -0.740] | 769 | 0.165 |
| anxiety | twin[split_half/nopool] | nll | -0.061 | [-0.069, -0.055] | 769 | 0.010 |
| bipolar | author_mean | se | -0.256 | [-0.446, -0.057] | 638 | 0.300 |
| bipolar | author_mean | nll | -0.056 | [-0.075, -0.038] | 638 | 0.028 |
| bipolar | ewma | se | -0.564 | [-0.745, -0.408] | 638 | 0.246 |
| bipolar | ewma | nll | -0.081 | [-0.098, -0.065] | 638 | 0.025 |
| bipolar | gap_ewma | se | -0.247 | [-0.438, -0.050] | 638 | 0.302 |
| bipolar | gap_ewma | nll | -0.055 | [-0.075, -0.037] | 638 | 0.029 |
| bipolar | last | se | -4.106 | [-4.430, -3.786] | 638 | 0.457 |
| bipolar | last | nll | -0.296 | [-0.307, -0.283] | 638 | 0.017 |
| bipolar | global_mean | se | -0.119 | [-0.302, 0.022] | 638 | 0.223 |
| bipolar | global_mean | nll | -0.045 | [-0.060, -0.032] | 638 | 0.019 |
| bipolar | shortcut | se | 1.120 | [0.829, 1.418] | 638 | 0.446 |
| bipolar | shortcut | nll | 0.068 | [0.040, 0.095] | 638 | 0.042 |
| bipolar | twin[fixed] | se | 0.359 | [0.291, 0.428] | 638 | 0.100 |
| bipolar | twin[fixed] | nll | -0.004 | [-0.012, 0.003] | 638 | 0.011 |
| bipolar | twin[conf_rule] | se | -1.024 | [-1.341, -0.742] | 638 | 0.471 |
| bipolar | twin[conf_rule] | nll | -0.435 | [-0.502, -0.369] | 638 | 0.101 |
| bipolar | twin[split_half/static] | se | -0.155 | [-0.196, -0.109] | 638 | 0.064 |
| bipolar | twin[split_half/static] | nll | -0.023 | [-0.031, -0.015] | 638 | 0.012 |
| bipolar | twin[split_half/rw] | se | -0.144 | [-0.186, -0.102] | 638 | 0.062 |
| bipolar | twin[split_half/rw] | nll | -0.023 | [-0.031, -0.014] | 638 | 0.012 |
| bipolar | twin[split_half/nopool] | se | -0.480 | [-0.599, -0.376] | 638 | 0.165 |
| bipolar | twin[split_half/nopool] | nll | -0.037 | [-0.045, -0.029] | 638 | 0.011 |
| depression | author_mean | se | -0.563 | [-0.628, -0.500] | 2172 | 0.093 |
| depression | author_mean | nll | -0.095 | [-0.101, -0.089] | 2172 | 0.009 |
| depression | ewma | se | -0.788 | [-0.853, -0.722] | 2172 | 0.098 |
| depression | ewma | nll | -0.112 | [-0.118, -0.105] | 2172 | 0.009 |
| depression | gap_ewma | se | -0.546 | [-0.609, -0.484] | 2172 | 0.091 |
| depression | gap_ewma | nll | -0.094 | [-0.100, -0.088] | 2172 | 0.009 |
| depression | last | se | -3.996 | [-4.164, -3.816] | 2172 | 0.245 |
| depression | last | nll | -0.300 | [-0.309, -0.292] | 2172 | 0.012 |
| depression | global_mean | se | -0.316 | [-0.438, -0.206] | 2172 | 0.166 |
| depression | global_mean | nll | -0.076 | [-0.086, -0.066] | 2172 | 0.014 |
| depression | shortcut | se | 1.029 | [0.923, 1.133] | 2172 | 0.147 |
| depression | shortcut | nll | 0.039 | [0.030, 0.047] | 2172 | 0.012 |
| depression | twin[fixed] | se | 0.334 | [0.308, 0.360] | 2172 | 0.038 |
| depression | twin[fixed] | nll | -0.023 | [-0.027, -0.019] | 2172 | 0.006 |
| depression | twin[conf_rule] | se | -0.967 | [-1.051, -0.887] | 2172 | 0.120 |
| depression | twin[conf_rule] | nll | -0.460 | [-0.494, -0.427] | 2172 | 0.050 |
| depression | twin[split_half/static] | se | -0.128 | [-0.170, -0.089] | 2172 | 0.058 |
| depression | twin[split_half/static] | nll | -0.010 | [-0.014, -0.007] | 2172 | 0.005 |
| depression | twin[split_half/rw] | se | -0.127 | [-0.167, -0.088] | 2172 | 0.057 |
| depression | twin[split_half/rw] | nll | -0.010 | [-0.013, -0.007] | 2172 | 0.005 |
| depression | twin[split_half/nopool] | se | -0.657 | [-0.717, -0.597] | 2172 | 0.085 |
| depression | twin[split_half/nopool] | nll | -0.051 | [-0.055, -0.047] | 2172 | 0.005 |
| suicidewatch | author_mean | se | -0.386 | [-0.512, -0.274] | 614 | 0.175 |
| suicidewatch | author_mean | nll | -0.066 | [-0.083, -0.050] | 614 | 0.024 |
| suicidewatch | ewma | se | -0.627 | [-0.746, -0.513] | 614 | 0.173 |
| suicidewatch | ewma | nll | -0.085 | [-0.100, -0.070] | 614 | 0.022 |
| suicidewatch | gap_ewma | se | -0.356 | [-0.483, -0.249] | 614 | 0.171 |
| suicidewatch | gap_ewma | nll | -0.064 | [-0.081, -0.047] | 614 | 0.024 |
| suicidewatch | last | se | -3.663 | [-3.894, -3.431] | 614 | 0.330 |
| suicidewatch | last | nll | -0.273 | [-0.287, -0.260] | 614 | 0.020 |
| suicidewatch | global_mean | se | -0.212 | [-0.405, -0.029] | 614 | 0.272 |
| suicidewatch | global_mean | nll | -0.051 | [-0.066, -0.038] | 614 | 0.020 |
| suicidewatch | shortcut | se | 0.956 | [0.765, 1.148] | 614 | 0.281 |
| suicidewatch | shortcut | nll | 0.053 | [0.033, 0.071] | 614 | 0.027 |
| suicidewatch | twin[fixed] | se | 0.361 | [0.306, 0.418] | 614 | 0.081 |
| suicidewatch | twin[fixed] | nll | -0.001 | [-0.012, 0.009] | 614 | 0.016 |
| suicidewatch | twin[conf_rule] | se | -1.412 | [-1.617, -1.209] | 614 | 0.305 |
| suicidewatch | twin[conf_rule] | nll | -0.465 | [-0.515, -0.412] | 614 | 0.074 |
| suicidewatch | twin[split_half/static] | se | -0.118 | [-0.181, -0.053] | 614 | 0.090 |
| suicidewatch | twin[split_half/static] | nll | -0.016 | [-0.021, -0.011] | 614 | 0.008 |
| suicidewatch | twin[split_half/rw] | se | -0.116 | [-0.178, -0.056] | 614 | 0.086 |
| suicidewatch | twin[split_half/rw] | nll | -0.016 | [-0.021, -0.010] | 614 | 0.008 |
| suicidewatch | twin[split_half/nopool] | se | -0.560 | [-0.691, -0.446] | 614 | 0.176 |
| suicidewatch | twin[split_half/nopool] | nll | -0.041 | [-0.049, -0.034] | 614 | 0.011 |

## E1 reply dose-response
beta=-0.1911 (p=5.47e-158); placebo beta=-0.0333; Gate A pass: True