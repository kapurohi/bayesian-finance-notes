# Chapter 10 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 10.1 — Numerical Integration | Grid approximation — practical for 1-2 parameters only | Useful for single-parameter model visualization and debugging. Not scalable to production multi-driver models. |
| 10.2 — Posterior Simulation | Any posterior quantity computable from samples via averaging | The production output pipeline: sample the posterior → apply DCF function to each sample → histogram the results. No additional math required after sampling. |
| 10.3 — Factored Distributions | Conditional independence enables parallel sampling | Hierarchical company models: conditional on hyperparameters, each company's parameters can be updated in parallel. Large coverage universes become computationally tractable. |
| 10.4 — Expectation Propagation | Fast Gaussian approximation for large-scale models | Screening tool for large coverage universes: run EP quickly to identify companies worth full MCMC analysis. |

---

## Connection to Previous Chapters

Section 10.2 is the formal statement of what the code files in Chapters 1-3 implement: the PyMC `sample()` call produces the posterior samples, and then every summary — means, credible intervals, probability statements, DCF outputs — is computed by averaging functions over those samples. The posterior simulation workflow is the computational implementation of the three-step Bayesian loop from Chapter 1 Section 1.1.
