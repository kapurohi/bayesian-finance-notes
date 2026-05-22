# Chapter 17 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 17.1 — Contamination Mixture | Explicit outlier-generating process | Earnings models that separate normal quarters from extraordinary-item quarters. Posterior over contamination fraction $\epsilon$ estimates how often the company reports non-recurring items. |
| 17.2 — Student-t Likelihood | Heavy-tailed likelihood robust to extreme observations | The default likelihood for return modeling and any financial series known to have heavy tails. Estimated $\nu$ provides a data-driven tail heaviness estimate rather than a fixed assumption. |
| 17.3 — Robust Regression | Regression with Student-t errors | Factor models and macro sensitivity regressions that include crisis periods. Down-weights extreme residuals without manual outlier removal. |

---

## Connection to Previous Chapters

The Student-t posterior from Chapter 3 Section 3.2 was the result of marginalizing over unknown variance in a Normal model. The Student-t likelihood in Section 17.2 is different — it is a deliberate modeling choice to handle heavy tails. The posterior predictive check procedure from Chapter 6 Section 6.3 is the tool that identifies when Normal is insufficient and Student-t is warranted.
