# 21.2 — Covariance Functions

## What this section is doing

The covariance function (kernel) encodes the prior beliefs about the function's smoothness, periodicity, and length scale. Choosing the right kernel is the key modeling decision in GP regression.

---

## Common kernels

**Squared exponential (RBF):** $k(x, x') = \sigma^2 \exp\left(-\frac{(x-x')^2}{2l^2}\right)$

Produces infinitely smooth functions. The length scale $l$ controls how quickly the function can vary.

**Matérn kernel:** Less smooth than RBF — the smoothness parameter $\nu$ controls how many times the function is differentiable. Matérn-5/2 is a common choice for financial time series.

**Periodic kernel:** Captures repeating patterns. Appropriate for seasonal financial data.

---

## Financial application

**Return volatility surface:** Model implied volatility as a function of strike and maturity using a GP. The Matérn kernel captures the observed roughness of the volatility surface more accurately than the smooth RBF kernel. The posterior provides a distribution over the full volatility surface — including interpolated and extrapolated values with correct uncertainty.

