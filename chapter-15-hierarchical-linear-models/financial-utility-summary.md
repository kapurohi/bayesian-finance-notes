# Chapter 15 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 15.1 — Hierarchical Regression | Company-specific coefficients drawn from a population distribution | The production multi-company macro sensitivity model. Every company gets its own GDP, rate, and inflation sensitivities — estimated jointly across the coverage universe. |
| 15.2 — Varying Intercepts | Common slope, company-specific baseline | Panel earnings model with company fixed effects and a common macro factor loading. Computationally simpler than full varying slopes. |
| 15.3 — Varying Slopes | Company-specific macro sensitivities | Cyclicality modeling. The full distribution of GDP sensitivities across the coverage universe informs sector rotation and portfolio construction. |
| 15.4 — Non-Nested Models | Crossed groupings — sector AND country simultaneously | Global equity models where both sector and country effects matter independently. Non-nested structure estimates both dimensions simultaneously. |
| 15.5 — Meta-Analysis | Combining estimates from multiple independent sources | Analyst estimate aggregation. Signal combination for multi-factor models. Each source weighted by its historical accuracy, combined posterior is better than any individual source. |

---

## Connection to Previous Chapters

Chapter 15 is the intersection of Chapter 5 (hierarchical scalar models) and Chapter 14 (regression). The varying-intercepts model in Section 15.2 is exactly the Chapter 5 Normal hierarchical model applied to regression intercepts. The meta-analysis in Section 15.5 is the same partial pooling mechanism from Chapter 5 Section 5.3 — precision-weighted averaging of independent estimates.
