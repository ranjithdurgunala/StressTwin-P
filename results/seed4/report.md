# StressTwin-P results (auto-generated; check the data source and the pilot setting in results.json before reading)

## held-out community: anxiety  (train authors 768)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.879 | 5.957 | 2.304 | 0.90 | 8.02 |
| twin[conf_rule] | 7.158 | 7.242 | 2.701 | 0.90 | 10.80 |
| twin[split_half] | 6.251 | 6.371 | 2.275 | 0.91 | 8.03 |
| twin[split_half/static] | 6.373 | 6.534 | 2.284 | 0.91 | 8.18 |
| twin[split_half/rw] | 6.373 | 6.534 | 2.284 | 0.91 | 8.18 |
| twin[split_half/nopool] | 6.972 | 6.944 | 2.330 | 0.91 | 8.46 |
| author_mean | 6.858 | 6.858 | 2.382 | 0.90 | 8.71 |
| last | 10.434 | 10.434 | 2.591 | 0.90 | 10.68 |
| ewma | 7.138 | 7.138 | 2.402 | 0.90 | 8.91 |
| gap_ewma | 6.849 | 6.849 | 2.381 | 0.90 | 8.71 |
| global_mean | 6.448 | 6.510 | 2.351 | 0.90 | 8.38 |
| shortcut | 4.852 | 4.883 | 2.209 | 0.91 | 7.41 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 8.02 | 0.90 / 8.01 | 0.90 / 8.00 |
| twin[conf_rule] | 0.90 / 10.80 | 0.90 / 10.36 | 0.90 / 10.86 |
| twin[split_half] | 0.91 / 8.03 | 0.91 / 7.92 | 0.90 / 7.86 |
| twin[split_half/static] | 0.91 / 8.18 | 0.90 / 8.04 | 0.90 / 7.96 |
| twin[split_half/rw] | 0.91 / 8.18 | 0.90 / 8.05 | 0.90 / 7.96 |
| twin[split_half/nopool] | 0.91 / 8.46 | 0.91 / 8.43 | 0.90 / 8.33 |

## held-out community: bipolar  (train authors 637)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.474 | 5.675 | 2.268 | 0.90 | 7.68 |
| twin[conf_rule] | 6.594 | 6.944 | 2.648 | 0.91 | 10.69 |
| twin[split_half] | 5.746 | 6.028 | 2.257 | 0.91 | 7.87 |
| twin[split_half/static] | 5.884 | 6.171 | 2.276 | 0.91 | 8.19 |
| twin[split_half/rw] | 5.882 | 6.167 | 2.276 | 0.91 | 8.18 |
| twin[split_half/nopool] | 6.209 | 6.143 | 2.295 | 0.91 | 8.16 |
| author_mean | 6.101 | 6.101 | 2.323 | 0.90 | 8.12 |
| last | 9.699 | 9.699 | 2.555 | 0.90 | 10.39 |
| ewma | 6.278 | 6.332 | 2.338 | 0.90 | 8.32 |
| gap_ewma | 6.090 | 6.090 | 2.322 | 0.90 | 8.11 |
| global_mean | 5.943 | 6.676 | 2.310 | 0.90 | 8.07 |
| shortcut | 4.787 | 4.858 | 2.202 | 0.90 | 7.14 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 7.68 | 0.90 / 7.72 | 0.90 / 7.86 |
| twin[conf_rule] | 0.91 / 10.69 | 0.90 / 10.38 | 0.90 / 10.54 |
| twin[split_half] | 0.91 / 7.87 | 0.90 / 7.79 | 0.90 / 7.81 |
| twin[split_half/static] | 0.91 / 8.19 | 0.90 / 7.96 | 0.90 / 8.04 |
| twin[split_half/rw] | 0.91 / 8.18 | 0.90 / 7.97 | 0.90 / 8.03 |
| twin[split_half/nopool] | 0.91 / 8.16 | 0.90 / 8.11 | 0.90 / 8.12 |

## held-out community: depression  (train authors 1500)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.798 | 5.757 | 2.297 | 0.90 | 7.87 |
| twin[conf_rule] | 7.067 | 7.049 | 2.734 | 0.91 | 10.82 |
| twin[split_half] | 6.169 | 5.957 | 2.277 | 0.90 | 7.92 |
| twin[split_half/static] | 6.351 | 6.073 | 2.293 | 0.90 | 8.17 |
| twin[split_half/rw] | 6.347 | 6.070 | 2.293 | 0.90 | 8.17 |
| twin[split_half/nopool] | 6.775 | 6.709 | 2.326 | 0.90 | 8.30 |
| author_mean | 6.662 | 6.662 | 2.367 | 0.90 | 8.42 |
| last | 9.865 | 9.865 | 2.563 | 0.90 | 10.37 |
| ewma | 6.857 | 6.857 | 2.382 | 0.90 | 8.57 |
| gap_ewma | 6.637 | 6.637 | 2.365 | 0.90 | 8.41 |
| global_mean | 6.528 | 6.536 | 2.357 | 0.90 | 8.36 |
| shortcut | 5.102 | 5.104 | 2.234 | 0.90 | 7.39 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 7.87 | 0.90 / 7.82 | 0.90 / 7.95 |
| twin[conf_rule] | 0.91 / 10.82 | 0.90 / 10.18 | 0.90 / 10.79 |
| twin[split_half] | 0.90 / 7.92 | 0.90 / 7.86 | 0.90 / 7.95 |
| twin[split_half/static] | 0.90 / 8.17 | 0.90 / 8.06 | 0.90 / 8.13 |
| twin[split_half/rw] | 0.90 / 8.17 | 0.90 / 8.06 | 0.90 / 8.12 |
| twin[split_half/nopool] | 0.90 / 8.30 | 0.90 / 8.27 | 0.90 / 8.33 |

## held-out community: suicidewatch  (train authors 613)
| model | MSE within | MSE across | NLL within | Gaussian cov90 within | Gaussian width within |
|---|---|---|---|---|---|
| twin[fixed] | 5.786 | 5.737 | 2.296 | 0.90 | 7.89 |
| twin[conf_rule] | 7.531 | 7.439 | 2.735 | 0.91 | 11.35 |
| twin[split_half] | 6.229 | 6.107 | 2.283 | 0.90 | 7.81 |
| twin[split_half/static] | 6.329 | 6.162 | 2.296 | 0.90 | 8.02 |
| twin[split_half/rw] | 6.329 | 6.161 | 2.295 | 0.90 | 8.02 |
| twin[split_half/nopool] | 6.854 | 6.899 | 2.331 | 0.90 | 8.15 |
| author_mean | 6.613 | 6.613 | 2.364 | 0.90 | 8.38 |
| last | 10.006 | 10.006 | 2.571 | 0.89 | 10.21 |
| ewma | 6.874 | 6.874 | 2.383 | 0.90 | 8.52 |
| gap_ewma | 6.598 | 6.591 | 2.362 | 0.90 | 8.36 |
| global_mean | 6.252 | 6.294 | 2.335 | 0.90 | 8.19 |
| shortcut | 4.986 | 4.971 | 2.222 | 0.90 | 7.34 |

Conformal / Gaussian intervals, held-out community, within-community training (target 90%):
| model | Gaussian cov/width | static conformal cov/width | ACI cov/width |
|---|---|---|---|
| twin[fixed] | 0.90 / 7.89 | 0.90 / 7.74 | 0.90 / 7.89 |
| twin[conf_rule] | 0.91 / 11.35 | 0.90 / 10.97 | 0.90 / 11.49 |
| twin[split_half] | 0.90 / 7.81 | 0.89 / 7.69 | 0.90 / 7.95 |
| twin[split_half/static] | 0.90 / 8.02 | 0.89 / 7.87 | 0.90 / 8.11 |
| twin[split_half/rw] | 0.90 / 8.02 | 0.89 / 7.87 | 0.90 / 8.13 |
| twin[split_half/nopool] | 0.90 / 8.15 | 0.89 / 8.07 | 0.90 / 8.33 |


## Twin vs baselines, paired difference with 95% author-bootstrap CI (negative = twin better)
| community | comparator | metric | diff | 95% CI | authors | min detectable (80% power) |
|---|---|---|---|---|---|---|
| anxiety | author_mean | se | -0.607 | [-0.718, -0.494] | 769 | 0.162 |
| anxiety | author_mean | nll | -0.107 | [-0.118, -0.096] | 769 | 0.015 |
| anxiety | ewma | se | -0.888 | [-1.013, -0.760] | 769 | 0.178 |
| anxiety | ewma | nll | -0.127 | [-0.138, -0.116] | 769 | 0.016 |
| anxiety | gap_ewma | se | -0.598 | [-0.706, -0.488] | 769 | 0.157 |
| anxiety | gap_ewma | nll | -0.106 | [-0.117, -0.096] | 769 | 0.015 |
| anxiety | last | se | -4.183 | [-4.537, -3.865] | 769 | 0.465 |
| anxiety | last | nll | -0.317 | [-0.332, -0.302] | 769 | 0.021 |
| anxiety | global_mean | se | -0.197 | [-0.340, -0.051] | 769 | 0.210 |
| anxiety | global_mean | nll | -0.076 | [-0.089, -0.063] | 769 | 0.018 |
| anxiety | shortcut | se | 1.399 | [1.220, 1.590] | 769 | 0.265 |
| anxiety | shortcut | nll | 0.066 | [0.052, 0.080] | 769 | 0.021 |
| anxiety | twin[fixed] | se | 0.371 | [0.319, 0.424] | 769 | 0.076 |
| anxiety | twin[fixed] | nll | -0.029 | [-0.038, -0.021] | 769 | 0.011 |
| anxiety | twin[conf_rule] | se | -0.907 | [-1.067, -0.743] | 769 | 0.227 |
| anxiety | twin[conf_rule] | nll | -0.426 | [-0.478, -0.380] | 769 | 0.070 |
| anxiety | twin[split_half/static] | se | -0.122 | [-0.165, -0.079] | 769 | 0.060 |
| anxiety | twin[split_half/static] | nll | -0.009 | [-0.013, -0.005] | 769 | 0.005 |
| anxiety | twin[split_half/rw] | se | -0.122 | [-0.164, -0.079] | 769 | 0.059 |
| anxiety | twin[split_half/rw] | nll | -0.009 | [-0.012, -0.005] | 769 | 0.005 |
| anxiety | twin[split_half/nopool] | se | -0.721 | [-0.828, -0.615] | 769 | 0.149 |
| anxiety | twin[split_half/nopool] | nll | -0.055 | [-0.062, -0.049] | 769 | 0.010 |
| bipolar | author_mean | se | -0.355 | [-0.443, -0.267] | 638 | 0.125 |
| bipolar | author_mean | nll | -0.066 | [-0.075, -0.057] | 638 | 0.013 |
| bipolar | ewma | se | -0.532 | [-0.628, -0.426] | 638 | 0.145 |
| bipolar | ewma | nll | -0.080 | [-0.090, -0.071] | 638 | 0.014 |
| bipolar | gap_ewma | se | -0.344 | [-0.430, -0.259] | 638 | 0.123 |
| bipolar | gap_ewma | nll | -0.065 | [-0.074, -0.056] | 638 | 0.013 |
| bipolar | last | se | -3.953 | [-4.194, -3.726] | 638 | 0.334 |
| bipolar | last | nll | -0.298 | [-0.308, -0.288] | 638 | 0.015 |
| bipolar | global_mean | se | -0.197 | [-0.327, -0.073] | 638 | 0.178 |
| bipolar | global_mean | nll | -0.053 | [-0.065, -0.041] | 638 | 0.016 |
| bipolar | shortcut | se | 0.959 | [0.823, 1.094] | 638 | 0.194 |
| bipolar | shortcut | nll | 0.055 | [0.042, 0.068] | 638 | 0.019 |
| bipolar | twin[fixed] | se | 0.272 | [0.237, 0.309] | 638 | 0.051 |
| bipolar | twin[fixed] | nll | -0.011 | [-0.017, -0.005] | 638 | 0.008 |
| bipolar | twin[conf_rule] | se | -0.848 | [-0.960, -0.732] | 638 | 0.172 |
| bipolar | twin[conf_rule] | nll | -0.391 | [-0.439, -0.352] | 638 | 0.063 |
| bipolar | twin[split_half/static] | se | -0.138 | [-0.196, -0.085] | 638 | 0.077 |
| bipolar | twin[split_half/static] | nll | -0.019 | [-0.023, -0.015] | 638 | 0.006 |
| bipolar | twin[split_half/rw] | se | -0.136 | [-0.194, -0.084] | 638 | 0.076 |
| bipolar | twin[split_half/rw] | nll | -0.019 | [-0.023, -0.015] | 638 | 0.006 |
| bipolar | twin[split_half/nopool] | se | -0.463 | [-0.543, -0.391] | 638 | 0.110 |
| bipolar | twin[split_half/nopool] | nll | -0.037 | [-0.042, -0.032] | 638 | 0.007 |
| depression | author_mean | se | -0.494 | [-0.557, -0.432] | 2172 | 0.089 |
| depression | author_mean | nll | -0.090 | [-0.096, -0.083] | 2172 | 0.009 |
| depression | ewma | se | -0.688 | [-0.761, -0.617] | 2172 | 0.103 |
| depression | ewma | nll | -0.104 | [-0.111, -0.098] | 2172 | 0.010 |
| depression | gap_ewma | se | -0.469 | [-0.530, -0.405] | 2172 | 0.089 |
| depression | gap_ewma | nll | -0.088 | [-0.094, -0.082] | 2172 | 0.009 |
| depression | last | se | -3.696 | [-3.865, -3.530] | 2172 | 0.237 |
| depression | last | nll | -0.286 | [-0.295, -0.278] | 2172 | 0.012 |
| depression | global_mean | se | -0.360 | [-0.486, -0.244] | 2172 | 0.178 |
| depression | global_mean | nll | -0.080 | [-0.089, -0.071] | 2172 | 0.014 |
| depression | shortcut | se | 1.067 | [0.971, 1.160] | 2172 | 0.137 |
| depression | shortcut | nll | 0.044 | [0.035, 0.051] | 2172 | 0.011 |
| depression | twin[fixed] | se | 0.371 | [0.342, 0.400] | 2172 | 0.043 |
| depression | twin[fixed] | nll | -0.020 | [-0.024, -0.016] | 2172 | 0.006 |
| depression | twin[conf_rule] | se | -0.898 | [-0.985, -0.819] | 2172 | 0.118 |
| depression | twin[conf_rule] | nll | -0.457 | [-0.507, -0.416] | 2172 | 0.065 |
| depression | twin[split_half/static] | se | -0.182 | [-0.226, -0.141] | 2172 | 0.060 |
| depression | twin[split_half/static] | nll | -0.016 | [-0.019, -0.013] | 2172 | 0.005 |
| depression | twin[split_half/rw] | se | -0.178 | [-0.222, -0.138] | 2172 | 0.059 |
| depression | twin[split_half/rw] | nll | -0.016 | [-0.019, -0.013] | 2172 | 0.005 |
| depression | twin[split_half/nopool] | se | -0.607 | [-0.663, -0.546] | 2172 | 0.087 |
| depression | twin[split_half/nopool] | nll | -0.049 | [-0.052, -0.045] | 2172 | 0.005 |
| suicidewatch | author_mean | se | -0.384 | [-0.501, -0.270] | 614 | 0.165 |
| suicidewatch | author_mean | nll | -0.080 | [-0.094, -0.067] | 614 | 0.019 |
| suicidewatch | ewma | se | -0.645 | [-0.780, -0.525] | 614 | 0.185 |
| suicidewatch | ewma | nll | -0.099 | [-0.114, -0.085] | 614 | 0.021 |
| suicidewatch | gap_ewma | se | -0.369 | [-0.493, -0.253] | 614 | 0.171 |
| suicidewatch | gap_ewma | nll | -0.079 | [-0.093, -0.066] | 614 | 0.020 |
| suicidewatch | last | se | -3.777 | [-4.066, -3.501] | 614 | 0.405 |
| suicidewatch | last | nll | -0.287 | [-0.304, -0.272] | 614 | 0.023 |
| suicidewatch | global_mean | se | -0.023 | [-0.183, 0.141] | 614 | 0.224 |
| suicidewatch | global_mean | nll | -0.052 | [-0.066, -0.038] | 614 | 0.021 |
| suicidewatch | shortcut | se | 1.244 | [1.035, 1.458] | 614 | 0.293 |
| suicidewatch | shortcut | nll | 0.061 | [0.042, 0.079] | 614 | 0.025 |
| suicidewatch | twin[fixed] | se | 0.443 | [0.389, 0.501] | 614 | 0.081 |
| suicidewatch | twin[fixed] | nll | -0.012 | [-0.021, -0.004] | 614 | 0.012 |
| suicidewatch | twin[conf_rule] | se | -1.302 | [-1.515, -1.096] | 614 | 0.297 |
| suicidewatch | twin[conf_rule] | nll | -0.451 | [-0.502, -0.405] | 614 | 0.071 |
| suicidewatch | twin[split_half/static] | se | -0.100 | [-0.170, -0.029] | 614 | 0.101 |
| suicidewatch | twin[split_half/static] | nll | -0.012 | [-0.019, -0.005] | 614 | 0.010 |
| suicidewatch | twin[split_half/rw] | se | -0.099 | [-0.168, -0.031] | 614 | 0.098 |
| suicidewatch | twin[split_half/rw] | nll | -0.012 | [-0.018, -0.005] | 614 | 0.010 |
| suicidewatch | twin[split_half/nopool] | se | -0.625 | [-0.742, -0.522] | 614 | 0.159 |
| suicidewatch | twin[split_half/nopool] | nll | -0.048 | [-0.056, -0.041] | 614 | 0.011 |

## E1 reply dose-response
beta=-0.1911 (p=5.47e-158); placebo beta=-0.0333; Gate A pass: True