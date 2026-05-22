# 10.4 — Expectation Propagation

## What this section is doing

Expectation Propagation (EP) is an approximation method that represents each factor in the posterior as a Gaussian, propagates those approximations through the model, and iterates until convergence. It is faster than MCMC and more accurate than simple Laplace approximation for models where the posterior is not too far from Normal.

---

## Financial application

For large-scale financial models — estimating parameters for thousands of companies simultaneously — MCMC may be computationally prohibitive. EP provides a scalable approximation that is often accurate enough for production use.

Stan's variational inference (ADVI) and PyMC's `fit` method implement related approximation methods. These are appropriate for large-scale exploratory analysis before committing to full MCMC for final inference.

---

## See also
- Chapter 13 for related approximation methods
- Chapter 12 for efficient MCMC that may be preferable when accuracy matters
