# Chapter 8 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 8.1 — Sample Surveys | Poststratification corrects for non-random sampling | Survivorship bias correction in backtests. Coverage universe recalibration when model training data differs from the target application population. |
| 8.2 — Designed Experiments | Bayesian A/B testing | Fintech product testing — conversion rates, default rates, pricing sensitivity. Bayesian testing allows early stopping and direct probability statements about treatment superiority. |
| 8.3 — Observational Studies | Causal inference from non-experimental data | Factor attribution, counterfactual DCF analysis, identifying whether correlations are causal. Requires explicit assumptions about the data-generating mechanism. |
| 8.4 — Censoring and Truncation | Correct likelihood for incomplete observations | Credit duration models, time-to-IPO, recovery rate estimation. Every active loan is a censored observation — ignoring this systematically underestimates default rates. |

---

## Connection to Previous Chapters

The censored likelihood in Section 8.4 is a modification of the Binomial and survival likelihoods from Chapter 2. The fundamental prior-likelihood-posterior structure is unchanged — only the likelihood function changes to account for the incomplete observation.
