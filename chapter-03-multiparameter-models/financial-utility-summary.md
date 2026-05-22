# Chapter 3 — Financial Utility Summary

This is the end-of-chapter map connecting every section to a specific use case for the platform.

---

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 3.1 — Nuisance Parameters | Marginalization — integrating out parameters you don't need | MCMC gives marginalization for free. Sample the joint posterior over all parameters, report only the ones that matter. Uncertainty in noise, volatility, and correlation parameters all propagate into the output distribution automatically. |
| 3.2 — Normal, Noninformative Prior | Unknown mean and variance → Student-t marginal posterior | Revenue growth estimation with unknown quarterly noise. The t-distribution posterior is wider than Normal — correctly reflecting that noise level was estimated from the same data. More honest uncertainty bounds in the DCF. |
| 3.3 — Normal-Inverse-Gamma | Conjugate joint model for mean and variance | Joint estimation of growth rate and volatility with encoded sector priors on both. Closed-form posterior — fast enough for real-time recalibration on earnings release. |
| 3.4 — Dirichlet-Multinomial | Probability vectors that sum to 1 | Credit rating transition matrices. Revenue segment mix estimation. Any problem where you're estimating a full distribution over categories from count data. Posterior is Dirichlet — same clean conjugate update as Beta-Binomial. |
| 3.5 — Multivariate Normal, Known Covariance | Joint mean vector estimation | Simultaneous estimation of multiple DCF drivers with known correlation structure. Posterior captures co-movement between growth, margin, and capex — sampling produces internally consistent scenarios. |
| 3.6 — Normal-Inverse-Wishart | Full joint model — unknown mean vector and covariance | The flagship multiparameter model. Estimates growth rate, margin, and capex jointly with an unknown correlation structure estimated from data. The direct replacement for a standard Monte Carlo DCF that incorrectly assumes independence across drivers. |
| 3.7 — Bioassay Example | Non-conjugate model — MCMC required | The template for Bayesian logistic regression. Maps directly to credit scoring (PD as a function of financial ratios), earnings surprise models, and deal close probability estimation. Same prior-likelihood structure, MCMC posterior. |
| 3.8 — Modeling Summary | Model selection guide | Decision tree for choosing the right model by data type and unknown parameter structure. Consolidates Chapters 2 and 3 into a single reference. |

---

## The Platform Architecture Chapter 3 Enables

**From single-driver to multi-driver DCF:**

Chapters 1 and 2 built the single-parameter models — one growth rate, one margin, one default probability. Chapter 3 connects those into a joint model. The Normal-Inverse-Wishart posterior from Section 3.6 is the direct implementation of a multi-driver Bayesian DCF where all parameters are estimated simultaneously with full covariance structure.

**From point estimates to correlated scenarios:**

A standard DCF Monte Carlo samples growth, margin, and WACC independently. A Section 3.6 posterior samples them from their joint distribution — high growth with compressed near-term margins, not high growth with high margins, because that is what the historical data and sector priors actually imply. The output distribution over intrinsic value is materially different and more defensible.

**Non-conjugate extension via MCMC:**

Section 3.7 removes the last constraint. Once you accept MCMC as the computational engine — as Section 1.9 introduced — any likelihood can be combined with any prior. The platform is not limited to conjugate models. Logistic regression for default probability, Student-t likelihoods for robust estimation, and time-series likelihoods for sequential updating all become available within the same modeling framework.

---

## Connection to Chapters 1 and 2

The marginalization principle in Section 3.1 is the formal version of the coherent uncertainty propagation described in Chapter 1 Section 1.10. What Chapter 1 stated as a qualitative advantage — "parameter uncertainty flows into forecast uncertainty automatically" — is now a specific mathematical operation: integrating out nuisance parameters from the joint posterior.

The prior-data compromise structure from Chapter 2 Section 2.2 generalizes exactly to the multivariate setting in Section 3.5 and 3.6 — posterior precision matrices add just as scalar precisions did, and posterior mean vectors are precision-weighted averages of prior and data means. The intuition is identical; the algebra is matrix-valued.
