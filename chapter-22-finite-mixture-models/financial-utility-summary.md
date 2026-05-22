# Chapter 22 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 22.1 — Mixture Models | Heterogeneous populations as weighted component distributions | Return distribution with heavy tails modeled as Normal mixture. Credit portfolio segmentation into subpopulations with different default processes. |
| 22.2 — Latent Class | Unobserved categorical membership | Customer behavioral segmentation. Regime-dependent factor models where active factor structure depends on macro conditions. |
| 22.3 — Regime Switching | Temporal mixture with Markov regime evolution | The flagship financial application: recession probability monitoring, regime-conditional growth and volatility estimation, DCF scenario analysis conditioned on current regime probability. |

---

## Connection to Previous Chapters

The contamination mixture from Chapter 17 Section 17.1 is a two-component mixture model with one large-variance component. Chapter 22 generalizes this to $K$ components with temporal structure. The Dirichlet prior on mixture weights is the same Dirichlet-Multinomial model from Chapter 3 Section 3.4.
