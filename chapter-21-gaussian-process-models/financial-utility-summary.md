# Chapter 21 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 21.1 — GP Regression | Prior over functions — posterior is a distribution over curves | Yield curve fitting and interpolation. Returns a full distribution over the yield curve at every maturity, with uncertainty calibrated to data density. |
| 21.2 — Covariance Functions | Kernel choice encodes smoothness and structure priors | Volatility surface modeling with Matérn kernel. Seasonal financial series with periodic kernel. Kernel hyperparameters estimated from data. |
| 21.3 — GP Classification | Nonparametric binary classification | Flexible credit scoring where the relationship between financial ratios and default probability is not specified in advance. Posterior PD with uncertainty calibrated to training data density. |

---

## Connection to Previous Chapters

GP regression is the infinite-dimensional generalization of Bayesian linear regression from Chapter 14. As the number of basis functions in a spline model (Chapter 20) grows to infinity, the model converges to a GP with the kernel determined by the basis function family. The GP classification model is the GP extension of the logistic regression from Chapter 16 Section 16.2.
