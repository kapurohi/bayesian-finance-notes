# 21.3 — Gaussian Process Classification

## What this section is doing

GP classification applies a GP prior to the latent function in a logistic or probit regression. The posterior over the latent function is no longer Gaussian (due to the non-Gaussian likelihood), but can be approximated using Laplace approximation or MCMC.

---

## Financial application

**Nonparametric credit scoring:** Model the probability of default as a flexible nonparametric function of financial ratios using a GP. The GP classifier captures nonlinear and interaction effects between ratios without specifying them in advance — the data determines the functional form. The posterior provides not just a default probability but uncertainty about that probability, wider in regions of the covariate space with fewer training examples.
