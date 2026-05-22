# Chapter 20 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 20.1 — Splines | Flexible nonlinear fitting with smoothness prior | Yield curve modeling, nonlinear factor-return relationships, earnings trajectory decomposition. Posterior distributions over the full curve shape, not just point estimates. |
| 20.2 — Regularization | Smoothness prior = ridge regularization on basis expansion | Unifies Bayesian smoothing with the regularization methods already used in quantitative finance. All spline-based financial models can be given Bayesian uncertainty quantification. |

---

## Connection to Previous Chapters

Bayesian splines are a specialization of the Bayesian regression framework from Chapter 14 — the same prior-likelihood-posterior structure, but with basis function transformations of the predictors. The smoothness prior is a structured version of the Normal prior on regression coefficients from Chapter 14 Section 14.2.
