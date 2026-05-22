# Chapter 3 — Introduction to Multiparameter Models

Chapters 1 and 2 dealt with a single unknown parameter. Real financial models almost always have multiple unknowns simultaneously — a revenue growth rate and a margin, a mean return and a volatility, a default probability and a recovery rate. This chapter extends the Bayesian framework to handle multiple parameters at once.

The key new idea is **marginalization** — the process of integrating out parameters you don't care about to get the distribution over the ones you do. This is how you handle nuisance parameters cleanly and how joint uncertainty over multiple quantities gets propagated into a single output distribution.

---

## Sections

| # | File | One-Line Summary |
|---|------|-----------------|
| 3.1 | [Averaging Over Nuisance Parameters](./01-nuisance-parameters.md) | How to eliminate parameters you don't care about by integrating them out |
| 3.2 | [Normal Data with Noninformative Prior](./02-normal-noninformative.md) | The Normal model with both mean and variance unknown — the realistic version |
| 3.3 | [Normal Data with Conjugate Prior](./03-normal-conjugate.md) | The Normal-InverseGamma conjugate model for joint mean and variance estimation |
| 3.4 | [Multinomial Model for Categorical Data](./04-multinomial.md) | Estimating probabilities across multiple categories simultaneously |
| 3.5 | [Multivariate Normal with Known Variance](./05-multivariate-normal-known.md) | Joint estimation of multiple means with a known covariance structure |
| 3.6 | [Multivariate Normal with Unknown Mean and Variance](./06-multivariate-normal-unknown.md) | The full joint model — the foundation for multi-driver financial models |
| 3.7 | [Example: Bioassay](./07-bioassay-example.md) | A non-conjugate model requiring numerical methods — the bridge to MCMC |
| 3.8 | [Summary of Elementary Modeling](./08-modeling-summary.md) | Recap of when to use which model and what comes next |

---

## End of Chapter

- [Financial Utility Summary](./financial-utility-summary.md) — every section mapped to a specific platform use case

---

## Code

| File | What it does |
|------|-------------|
| [joint_growth_margin_model.py](./code/joint_growth_margin_model.py) | Joint Bayesian model for revenue growth and operating margin estimated simultaneously |
| [chapter03_walkthrough.ipynb](./code/chapter03_walkthrough.ipynb) | Jupyter notebook walking through the multiparameter model with a DCF scenario application |
