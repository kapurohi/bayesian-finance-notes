# 4.5 — Bayesian Interpretations of Classical Statistics

## What this section is doing

Gelman shows that many classical statistical methods — maximum likelihood estimation, ordinary least squares regression, t-tests, AIC model selection — are either special cases of Bayesian inference or can be derived as Bayesian procedures under specific prior choices. This reframes classical statistics as a subset of the Bayesian framework rather than an alternative to it.

---

## The key connections

**Maximum likelihood estimation (MLE):**

MLE is equivalent to Bayesian inference with a flat (uniform) prior. The MLE is the MAP estimate under a noninformative prior. With large samples, the posterior concentrates at the MLE regardless of the prior — so MLE and Bayesian estimation converge.

**Ordinary least squares (OLS):**

OLS regression is equivalent to Bayesian linear regression with a flat prior on the coefficients and a known error variance. The OLS coefficient estimates are the posterior means under these conditions.

**Ridge regression:**

Ridge regression — OLS with an L2 penalty on coefficients — is equivalent to Bayesian linear regression with a Normal prior on the coefficients. The ridge penalty parameter controls the prior precision. This means every regularized regression method has a Bayesian interpretation.

**AIC model selection:**

The Akaike Information Criterion (AIC) approximates leave-one-out cross-validation and has a Bayesian interpretation as a penalized log-likelihood. It is related to but less principled than the Bayesian information criteria discussed in Chapter 7.

---

## Financial application

Every regression model used in financial analysis — factor models, earnings prediction models, credit scoring models — can be reframed as a Bayesian model. The OLS version is the special case with a flat prior. The regularized version (Ridge, Lasso) is the special case with a Normal or Laplace prior. The full Bayesian version adds proper uncertainty quantification and sequential updating.

This means existing financial models don't need to be thrown away — they need to be extended with priors and posterior inference.

---

## See also

- Section 2.8 for the noninformative priors that make Bayesian inference equivalent to MLE
- Chapter 14 for the full Bayesian regression treatment
