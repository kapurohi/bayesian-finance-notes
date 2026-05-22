# Chapter 11 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 11.1 — Markov Chain Procedure | MCMC samples the posterior using only unnormalized evaluations | Eliminates the intractable normalizing constant $p(y)$ — the computational bottleneck that made complex Bayesian models infeasible before MCMC. Enables arbitrary-complexity financial models. |
| 11.2 — Metropolis-Hastings | The foundational MCMC algorithm | Understanding MH is essential for debugging MCMC failures. Modern algorithms (HMC, NUTS) are vastly more efficient but reduce to MH conceptually. |
| 11.3 — Gibbs Sampling | Efficient sampling via full conditionals | Hierarchical financial models often have Gibbs-tractable full conditionals. PyMC identifies and exploits this automatically, making multi-company hierarchical models computationally feasible. |
| 11.4 — Convergence Theory | Conditions for MCMC convergence | Understanding why convergence is guaranteed under mild conditions — and what those conditions mean in practice — informs model specification choices that avoid convergence failures. |
| 11.5 — Convergence Diagnostics | $\hat{R}$ and ESS as production gatekeepers | Non-negotiable checks before serving any model output. $\hat{R} < 1.01$ and ESS greater than 400 for every parameter. Implemented in ArviZ. |

---

## Connection to Previous Chapters

Section 11.5 formalizes the $\hat{R}$ diagnostic introduced in Chapter 1 Section 1.9. What Chapter 1 presented as a rule of thumb — "R-hat less than 1.01 means converged" — is now derived from first principles as a ratio of between-chain to within-chain variance. The full conditional distributions in Section 11.3 are the same factorizations introduced in Chapter 3 Section 3.1 and Chapter 10 Section 10.3.
