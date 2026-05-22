# 3.5 — Multivariate Normal Model with Known Variance

## What this section is doing

This is the multivariate generalization of Section 2.5. Instead of estimating a single unknown mean, you're estimating a vector of means simultaneously — with a known covariance structure. The key new element is that the parameters are correlated, and the posterior properly captures those correlations.

---

## Simplification

In Section 2.5, you estimated one number — a growth rate. Here you're estimating several numbers at once — say, revenue growth, operating margin, and capex intensity — where those quantities are correlated with each other. Higher growth companies tend to have different margin profiles. The multivariate normal model estimates all of them jointly, capturing those correlations in the posterior.

---

## The model

**The likelihood:**

$$y \mid \mu \sim \text{Normal}(\mu, \Sigma)$$

Where $y$ is a vector of observations, $\mu$ is the vector of unknown means, and $\Sigma$ is the known covariance matrix.

**The prior:**

$$\mu \sim \text{Normal}(\mu_0, \Lambda_0)$$

Where $\Lambda_0$ is the prior covariance matrix — encoding both uncertainty about each mean and prior beliefs about correlations between them.

**The posterior:**

$$\mu \mid y \sim \text{Normal}(\mu_n, \Lambda_n)$$

$$\Lambda_n^{-1} = \Lambda_0^{-1} + n\Sigma^{-1}$$

$$\mu_n = \Lambda_n\left(\Lambda_0^{-1}\mu_0 + n\Sigma^{-1}\bar{y}\right)$$

The structure is identical to Section 2.5 — precision matrices add, posterior mean is a precision-weighted average — but now operating on vectors and matrices instead of scalars.

---

## Financial application

**Joint estimation of growth and margin:**

Estimate revenue growth $\mu_1$ and operating margin $\mu_2$ simultaneously, with prior covariance encoding your belief that high-growth companies in this sector tend to have lower near-term margins.

The posterior covariance $\Lambda_n$ captures how information about one quantity updates your beliefs about the other. In a DCF, this correlation structure ensures that scenario analysis is internally consistent — you don't independently sample a high growth rate and a high margin if they are negatively correlated.

---

## See also

- Section 2.5 for the univariate version
- Section 3.6 for the extension to unknown covariance
