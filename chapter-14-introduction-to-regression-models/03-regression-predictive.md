# 14.3 — Prediction

## What this section is doing

The Bayesian regression model produces a full predictive distribution over new outcomes — not just a point forecast and standard error. Gelman derives the posterior predictive distribution for new observations and shows how it correctly accounts for both parameter uncertainty and observation noise.

---

## The posterior predictive for regression

For a new observation with predictors $x_{\text{new}}$:

$$\tilde{y} \mid x_{\text{new}}, y \sim \int p(\tilde{y} \mid x_{\text{new}}, \beta) \cdot p(\beta \mid y) \, d\beta$$

This integrates over the posterior uncertainty in $\beta$ — so the predictive interval is wider than a frequentist confidence interval, correctly reflecting that $\beta$ is uncertain.

The result is a Student-t distribution (when $\sigma^2$ is also unknown) wider than the Normal approximation that ignores coefficient uncertainty.

---

## Financial application

A DCF revenue forecast: given a posterior distribution over the GDP sensitivity coefficient and a forecast distribution over GDP growth, the posterior predictive distribution over next-quarter revenue properly accounts for both coefficient uncertainty and GDP forecast uncertainty. The resulting uncertainty band is wider than what a point-estimate OLS model would produce — and correctly so.

---

## See also
- Section 1.3 for the posterior predictive concept
- Section 3.2 for the Student-t result when variance is unknown
