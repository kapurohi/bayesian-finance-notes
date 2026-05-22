# 14.2 — Bayesian Regression with Conjugate Priors

## What this section is doing

With a Normal prior on the regression coefficients and known variance, the posterior over the coefficients is Normal — another conjugate model. Gelman derives the posterior mean, which turns out to be a weighted combination of the OLS estimate and the prior mean.

---

## The posterior

For the multivariate regression $y = X\beta + \epsilon$ with $\epsilon \sim \text{Normal}(0, \sigma^2 I)$ and prior $\beta \sim \text{Normal}(\beta_0, \Sigma_0)$:

$$\beta \mid y \sim \text{Normal}(\beta_n, \Sigma_n)$$

$$\Sigma_n^{-1} = \Sigma_0^{-1} + \frac{1}{\sigma^2}X^T X$$

$$\beta_n = \Sigma_n\left(\Sigma_0^{-1}\beta_0 + \frac{1}{\sigma^2}X^T y\right)$$

This is the same precision-weighted average structure as the Normal-Normal model — prior precision plus data precision, posterior mean is a precision-weighted combination.

---

## Ridge regression as a special case

With a spherical Normal prior $\beta \sim \text{Normal}(0, \lambda^{-1}I)$, the posterior mean is identical to the ridge regression estimate:

$$\beta_n = (X^T X + \lambda I)^{-1} X^T y$$

Ridge regularization is Bayesian regression with a zero-mean Normal prior. The regularization strength $\lambda$ is the prior precision.

---

## Financial application

A multi-factor earnings model: regress earnings growth on GDP growth, sector momentum, and balance sheet quality. The Bayesian version automatically regularizes the factor loadings through the prior, preventing overfitting on limited earnings history. The posterior mean factor loadings are shrunk toward zero relative to OLS estimates — appropriate when the model has many factors relative to the number of earnings observations.

---

## See also
- Chapter 15 for the hierarchical extension where the prior itself is estimated from data
