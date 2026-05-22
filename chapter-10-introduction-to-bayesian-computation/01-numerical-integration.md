# 10.1 — Numerical Integration

## What this section is doing

For models where the posterior has no closed-form solution and MCMC is computationally expensive, deterministic numerical integration provides an alternative. Gelman covers grid approximation, quadrature methods, and their limitations for high-dimensional problems.

---

## Grid approximation

The simplest approach: evaluate the unnormalized posterior on a fine grid of parameter values, then normalize by dividing by the sum. This works well for models with 1-2 parameters but becomes computationally infeasible above 3-4 dimensions — the curse of dimensionality means the number of grid points grows exponentially with the number of parameters.

---

## Financial application

Grid approximation is practical for the single-parameter models in Chapter 2 (Beta-Binomial, Normal-Normal) and provides a useful teaching tool. For any model with more than 2 parameters — which includes most production financial models — MCMC or variational approximations are required.

---

## See also
- Chapter 11 for MCMC methods that scale to high dimensions
- Chapter 13 for variational approximations
