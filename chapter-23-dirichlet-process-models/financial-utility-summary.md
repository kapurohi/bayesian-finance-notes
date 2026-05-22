# Chapter 23 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 23.1 — Dirichlet Process | Prior over distributions — number of clusters grows with data | Portfolio segmentation without prespecifying the number of risk segments. The model learns the appropriate number of distinct subpopulations from the data. |
| 23.2 — DP Mixture Models | Nonparametric mixture with data-driven number of components | Return regime detection without fixing the number of regimes in advance. Posterior distribution over number of regimes quantifies structural uncertainty. |
| 23.3 — HDP Applications | Hierarchical DP for shared cluster structure across groups | Cross-sector portfolio segmentation. NLP applications on earnings transcripts (LDA topic models). Shared cluster types across related groups without forced identical structure. |

---

## Connection to Previous Chapters

The Dirichlet process is the infinite-dimensional generalization of the Dirichlet distribution from Chapter 3 Section 3.4. Where the Dirichlet distribution is a prior over $K$ fixed probability categories, the DP is a prior over a countably infinite number of categories. The finite mixture model in Chapter 22 is the DP mixture model with $K$ fixed — removing that constraint gives the DP.
