# Chapter 13 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 13.1 — Laplace Approximation | Normal approximation at the posterior mode | Fast preliminary estimates for large-sample companies. Validated against MCMC before being trusted for production output. |
| 13.2 — Hierarchical Laplace | Hybrid approximation for hierarchical models | Speed optimization for large coverage universes. Individual-level Laplace approximation combined with accurate hyperparameter integration. |
| 13.3 — INLA | Accurate marginal posteriors for latent Gaussian models | Production option for time-series and GP models where MCMC is too slow. R-INLA implementation. |

---

## Connection to Previous Chapters

The Laplace approximation in Section 13.1 is the formal implementation of the asymptotic Normal posterior from Chapter 4 Section 4.1. Both are Normal approximations centered at the MAP estimate — Chapter 4 shows when this is asymptotically correct; Chapter 13 shows how to compute it in practice.
