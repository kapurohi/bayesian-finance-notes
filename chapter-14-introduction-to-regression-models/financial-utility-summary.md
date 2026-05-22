# Chapter 14 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 14.1 — Regression Basics | Bayesian linear regression with priors on coefficients | The foundation for all multi-driver financial models: revenue-GDP regression, earnings-factor regression, credit-ratio regression. |
| 14.2 — Conjugate Regression | Ridge regression as Bayesian inference with Normal prior | All regularized regression used in financial modeling has a Bayesian interpretation. Bayesian version adds uncertainty quantification on top of the regularized estimates. |
| 14.3 — Prediction | Posterior predictive accounts for coefficient uncertainty | Revenue and earnings forecasts with correct uncertainty — wider than OLS prediction intervals, reflecting genuine parameter uncertainty. |
| 14.4 — Variable Selection | Spike-and-slab priors for factor selection | Factor model construction: posterior inclusion probabilities identify genuine earnings drivers from a large candidate set without overfitting. |
| 14.5 — Earnings Example | Applied Bayesian regression for earnings forecasting | Analyst forecast bias encoded as prior information. Shrinkage priors improve out-of-sample accuracy for short-history companies. |

---

## Connection to Previous Chapters

Bayesian regression is the combination of the Normal-Normal model (Chapter 2 Section 2.5) extended to multiple predictors. The conjugate posterior structure in Section 14.2 is identical to the single-parameter Normal-Normal update — precision matrices add, posterior mean is precision-weighted — now applied to coefficient vectors and design matrices.

The Ridge = Bayesian result in Section 14.2 is the multivariate formalization of Section 4.5's statement that "OLS with a Normal prior gives Ridge regression."
