# 20.2 — Regularization and Bayesian Smoothing

## What this section is doing

Gelman shows that the smoothness-inducing prior on spline coefficients is equivalent to ridge regularization on the basis function expansion. This completes the connection between Bayesian priors and regularization methods.

---

## Financial application

**Term structure fitting:** A Bayesian spline fit to the yield curve with a smoothness prior produces Nelson-Siegel-like behavior — smooth, parsimonious yield curves — without explicitly imposing the Nelson-Siegel functional form. The posterior captures uncertainty in the curve shape.

**Earnings trajectory smoothing:** Smooth a company's historical earnings trajectory to separate the underlying trend from quarter-specific noise. The Bayesian smoother automatically determines how much smoothing is appropriate given the data.
