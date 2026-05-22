# 13.3 — Integrated Nested Laplace Approximation (INLA)

## What this section is doing

INLA is a systematic method for computing accurate marginal posterior approximations for a large class of latent Gaussian models. It is implemented in the R-INLA package and can handle models that would take hours in MCMC in seconds.

---

## Financial application

Gaussian process models (Chapter 21), spatial models, and time-series models with latent Gaussian structure all fall within the INLA framework. For production financial models where speed is critical and the model structure fits INLA's assumptions, it provides MCMC-level accuracy at a fraction of the computational cost.

---

## See also
- Chapter 21 for Gaussian process models that fit the INLA framework
