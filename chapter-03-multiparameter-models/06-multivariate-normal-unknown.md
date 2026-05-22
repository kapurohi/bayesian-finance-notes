# 3.6 — Multivariate Normal with Unknown Mean and Variance

## What this section is doing

This is the most realistic and most important model in Chapter 3. Both the mean vector $\mu$ and the covariance matrix $\Sigma$ are treated as unknown. The conjugate prior is the **Normal-Inverse-Wishart** family. This is the foundational model for joint financial parameter estimation — estimating multiple drivers simultaneously with fully propagated uncertainty.

---

## Simplification

In Section 3.5, you knew how the financial metrics were correlated with each other — you fixed the covariance matrix. In practice you don't know this. You have to estimate the correlations from the same data you use to estimate the means.

Estimating the covariance structure from data introduces additional uncertainty, which again flows into the posterior over the means. The Normal-Inverse-Wishart model handles this jointly and correctly.

---

## The conjugate prior

**For the mean, conditional on covariance:**

$$\mu \mid \Sigma \sim \text{Normal}\!\left(\mu_0, \frac{\Sigma}{\kappa_0}\right)$$

**For the covariance matrix:**

$$\Sigma \sim \text{Inverse-Wishart}(\Lambda_0, \nu_0)$$

The Inverse-Wishart is the matrix generalization of the Inverse-Gamma distribution. It places a prior over the full covariance structure — the variances of each parameter and the correlations between them.

Hyperparameters:
- $\mu_0$ — prior mean vector
- $\kappa_0$ — prior strength on the mean
- $\Lambda_0$ — prior scale matrix, encodes your belief about the covariance structure
- $\nu_0$ — prior degrees of freedom, how confident you are in $\Lambda_0$

---

## The posterior update

After observing $n$ data vectors:

$$\kappa_n = \kappa_0 + n, \qquad \nu_n = \nu_0 + n$$

$$\mu_n = \frac{\kappa_0 \mu_0 + n\bar{y}}{\kappa_0 + n}$$

$$\Lambda_n = \Lambda_0 + S + \frac{\kappa_0 n}{\kappa_0 + n}(\bar{y} - \mu_0)(\bar{y} - \mu_0)^T$$

Where $S = \sum_{i=1}^n (y_i - \bar{y})(y_i - \bar{y})^T$ is the scatter matrix of the data.

The marginal posterior over $\mu$ — integrating out $\Sigma$ — is a multivariate Student-t distribution, generalizing the result from Section 3.2.

---

## Financial application

**Multi-driver DCF parameter model:**

Estimate the joint distribution over three DCF drivers simultaneously:
- $\mu_1$: revenue growth rate
- $\mu_2$: EBITDA margin
- $\mu_3$: capex as a percentage of revenue

The prior covariance $\Lambda_0$ encodes sector-level beliefs about how these quantities co-move. The posterior covariance $\Sigma_n$ is updated by the company's own historical data.

When you sample from the joint posterior $p(\mu_1, \mu_2, \mu_3, \Sigma \mid y)$ and use those samples to simulate DCF scenarios, the resulting distribution over intrinsic value properly reflects:

1. Uncertainty about each individual driver
2. The correlation structure between drivers
3. Uncertainty about the correlation structure itself

This is fundamentally different from a Monte Carlo DCF that independently samples each driver — and it produces materially different, more realistic output distributions.

---

## Why this model matters for the platform

A standard sensitivity table in a DCF independently moves one variable at a time. A standard Monte Carlo DCF samples each variable independently. Both ignore correlations.

The Normal-Inverse-Wishart posterior samples the full joint distribution. High growth and compressed margins arrive as correlated draws. The output distribution over intrinsic value reflects the actual covariance structure of the business, not an artificial independence assumption.

---

## See also

- Section 3.5 for the known-covariance version
- Section 3.2 for the scalar version (Normal with unknown mean and variance)
- Section 3.3 for the Normal-Inverse-Gamma conjugate — the univariate analogue of this model
