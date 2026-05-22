# 21.1 — Gaussian Process Regression

## What this section is doing

A Gaussian process defines a prior over functions such that any finite collection of function values follows a multivariate Normal distribution. Given observations, the posterior is also a GP — a posterior distribution over functions, not just parameters.

---

## Simplification

Instead of saying "the yield curve is described by these 3 Nelson-Siegel parameters," a GP says "the yield curve is some smooth function — and after observing the market yields at these maturities, here is my posterior distribution over what the full yield curve looks like."

The posterior GP gives you a distribution over the curve at every point — not just at the observed maturities.

---

## The model

$$f \sim \mathcal{GP}(m(x), k(x, x'))$$

Where $m(x)$ is the mean function (often zero) and $k(x, x')$ is the **covariance function** (or kernel) — it defines how similar function values are at different input points.

Given observations $y = f(X) + \epsilon$ with $\epsilon \sim \text{Normal}(0, \sigma^2 I)$:

$$f^* \mid y \sim \text{Normal}(\mu^*, \Sigma^*)$$

Where $\mu^*$ and $\Sigma^*$ are the posterior mean and covariance at prediction points $X^*$ — computed analytically using the kernel matrix.

---

## Financial application

**Yield curve interpolation:** Given yields at observed maturities (3m, 6m, 1y, 2y, 5y, 10y, 30y), the GP posterior gives a distribution over the yield at every maturity. Posterior uncertainty is largest where observations are sparse (between 10y and 30y) and smallest where observations are dense.
