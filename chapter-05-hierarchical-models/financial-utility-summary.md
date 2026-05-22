# Chapter 5 — Financial Utility Summary

---

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 5.1 — Hierarchical Structure | Two-level model: company parameters drawn from sector distribution | The architecture for a multi-company coverage platform. Each company has its own parameters; all parameters are connected through the sector-level distribution. |
| 5.2 — Exchangeability | Formal justification for pooling information across companies | Within a well-defined sector and business model class, companies are exchangeable — observing one company's data informs all others. This is the assumption that makes the platform defensible. |
| 5.3 — Conjugate Hierarchy | Partial pooling estimate as precision-weighted average | The exact formula governing how much each company borrows from the sector. New companies: high sector weight. Mature companies: high own-data weight. The model calibrates this automatically. |
| 5.4 — Normal Exchangeable | Full hierarchical Normal model with shrinkage | The flagship production model for growth rate and margin estimation across a coverage universe. Requires MCMC. Extreme observations get shrunk toward the sector mean. |
| 5.5 — Tumor Rates Example | Hierarchical Beta-Binomial with varying sample sizes | The template for hierarchical default probability estimation across a credit portfolio. Small-exposure entities borrow heavily from the population. |
| 5.6 — Hierarchical Regression | Company-specific regression coefficients drawn from a population | Revenue sensitivity to macro drivers estimated per company while sharing information across the sector. Limited-history companies get sector-average sensitivities until their own data accumulates. |
| 5.7 — Variance Components | ICC decomposes total variance into within vs between-company | $\rho$ tells you how aggressively to pool within a sector. Estimated from the data — no manual calibration required. |

---

## Connection to Previous Chapters

The hierarchical model is the formal implementation of the structural prior introduced informally in Chapter 1 Section 1.6. What Chapter 1 described as "using industry-level distributions as a structural prior before company data is sufficient" is now fully specified: the sector distribution is Level 2 of the hierarchy, estimated from the data rather than fixed externally.

The partial pooling estimate in Section 5.3 is a generalization of the single-company posterior compromise from Chapter 2 Section 2.2. The precision-weighted average structure is identical — but now the population mean $\mu$ is itself a parameter estimated from all companies simultaneously rather than a fixed hyperparameter.
