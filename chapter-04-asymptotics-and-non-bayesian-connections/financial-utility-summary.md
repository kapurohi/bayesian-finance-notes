# Chapter 4 — Financial Utility Summary

---

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 4.1 — Normal Approximation | Posterior becomes Normal as $n$ grows | For mature companies with long earnings histories, the Normal approximation is computationally cheap and accurate. For sparse-data companies, full MCMC is still required — the approximation is not reliable below roughly 20 observations. |
| 4.2 — Large-Sample Theory | Posterior consistency and efficiency | Validates using Bayesian models on large transaction datasets, long equity return series, and full credit history panels — the posteriors will converge correctly and achieve minimum-variance estimates. |
| 4.3 — Counterexamples | Unidentified models, growing parameters, heavy tails | Three production failure modes to design around: collinear factors (unidentification), per-company fixed effects with few data points (growing parameters), and tail-risk modeling (heavy-tailed likelihoods that require robust models from Chapter 17). |
| 4.4 — Frequency Evaluations | Bayesian intervals have correct frequentist coverage | Bayesian credible intervals are defensible to clients and regulators who expect frequentist confidence intervals. For large samples and weakly informative priors, they are numerically equivalent. |
| 4.5 — Classical Connections | MLE, OLS, Ridge as Bayesian special cases | All existing financial regression models are flat-prior Bayesian models. Upgrading them to full Bayesian involves adding a proper prior — not replacing the model. Factor models, scoring models, and earnings forecasting models all fit this pattern. |

---

## Connection to Previous Chapters

The Normal approximation in Section 4.1 is the large-sample limit of the exact Student-t marginal posterior derived in Chapter 3 Section 3.2. As $n$ grows, the Student-t degrees of freedom increase and the distribution converges to Normal — Section 4.1 is the formal statement of what Section 3.2 approaches asymptotically.

The MLE-as-flat-prior result in Section 4.5 connects directly to Chapter 2 Section 2.8. A noninformative prior produces a posterior centered at the MLE — this chapter makes precise the conditions under which that is a reasonable approximation.
