# Chapter 18 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 18.1 — Missing Data Mechanisms | MCAR/MAR/MNAR classification determines what can be inferred | MNAR is the common and dangerous case in finance — distressed companies withhold data, survivorship bias is MNAR by construction. Models must account for the missingness mechanism, not just ignore it. |
| 18.2 — Missing at Random | MAR data handled correctly by proper Bayesian modeling | Hierarchical models naturally handle unbalanced panels — companies with different numbers of quarters. No special treatment needed when missingness is not related to the missing values. |
| 18.3 — Multiple Imputation | Filling gaps with posterior predictive draws | Balance sheet gap filling. Cross-sectional panel completion. Uncertainty from imputed values correctly propagated into final parameter estimates through Rubin's rules. |

---

## Connection to Previous Chapters

The posterior predictive distribution used in imputation is the same $p(\tilde{y} \mid y)$ derived in Chapter 1 Section 1.3 and formalized in Chapter 3. Imputation is just posterior predictive simulation applied to the missing data problem. The hierarchical model from Chapter 5 handles MAR missing data automatically through marginalization.
