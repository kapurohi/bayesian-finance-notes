# Chapter 12 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 12.1 — Efficiency Challenge | Random walk MH is impractical for high-dimensional models | Production financial models with 50+ parameters require HMC or NUTS — basic MCMC is not computationally viable at this scale. |
| 12.2 — HMC | Gradient-guided large moves through parameter space | The algorithmic foundation of PyMC's sampler. Understanding it helps diagnose sampling failures and choose reparameterizations. |
| 12.3 — NUTS | Automatic trajectory tuning — the PyMC default | The production sampler. Set `target_accept=0.9`, check for divergences, monitor $\hat{R}$ and ESS. Non-centered parameterization fixes most divergence issues in hierarchical models. |
| 12.4 — Variational Inference | Fast approximate posterior — good for screening, not final output | Screening tool for large coverage universes. Flag companies for full MCMC when VI ESS or $\hat{R}$ is poor. Never serve VI output as final valuation uncertainty. |

---

## Connection to Previous Chapters

NUTS is the algorithm that makes every PyMC model in Chapters 1-5 actually run. Section 12.3 provides the full picture of what happens when you call `pm.sample()`. The divergence diagnostics in Section 12.3 are the production-level extension of the $\hat{R}$ and ESS diagnostics introduced in Chapter 11 Section 11.5.
