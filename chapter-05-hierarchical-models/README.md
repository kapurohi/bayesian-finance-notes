# Chapter 5 — Hierarchical Models

This is the most directly important chapter in BDA3 for building a multi-company financial intelligence platform.

Every model in Chapters 2 and 3 estimated parameters for a single entity — one growth rate, one margin, one default probability — from that entity's own data alone. But in practice you have a coverage universe of dozens or hundreds of companies. Some have long histories. Some are newly listed. Some are in the same sector.

Hierarchical models are the framework for estimating all of them simultaneously, sharing information across entities through a common structure. A company with limited history borrows strength from the sector. A company with a long history contributes to the sector estimate while being mostly determined by its own data.

This is the formal architecture for what was introduced informally in Chapter 1 Section 1.6 — using industry-level knowledge as a structural prior.

---

## Sections

| # | File | One-Line Summary |
|---|------|-----------------|
| 5.1 | [Constructing a Hierarchical Model](./01-constructing-hierarchical-model.md) | The two-level structure — individual parameters drawn from a common population distribution |
| 5.2 | [Exchangeability](./02-exchangeability.md) | The formal justification for pooling information across units |
| 5.3 | [Bayesian Analysis of Conjugate Hierarchical Models](./03-conjugate-hierarchical.md) | Closed-form hierarchical updates — Normal-Normal and Beta-Binomial hierarchies |
| 5.4 | [Normal Model with Exchangeable Parameters](./04-normal-exchangeable.md) | The flagship hierarchical model — partial pooling across companies |
| 5.5 | [Example: Estimating Tumor Rates](./05-tumor-rates-example.md) | Full worked example showing partial pooling in action |
| 5.6 | [Hierarchical Modeling Applied to Regression](./06-hierarchical-regression.md) | Extending partial pooling to regression coefficient estimation |
| 5.7 | [Analysis of Variance and the Variance Components Model](./07-anova-variance-components.md) | Decomposing variation into within-group and between-group components |

---

## End of Chapter

- [Financial Utility Summary](./financial-utility-summary.md)

---

## Code

| File | What it does |
|------|-------------|
| [hierarchical_growth_model.py](./code/hierarchical_growth_model.py) | Hierarchical PyMC model estimating revenue growth rates across a coverage universe of companies simultaneously |
