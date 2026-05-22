# Chapter 2 — Single-Parameter Models

Chapter 1 installed the operating system. This chapter runs the first real programs on it.

Gelman works through the simplest possible Bayesian models — ones with a single unknown parameter — and shows how the three-step loop from Section 1.1 plays out in full detail. These are not toy examples. The Beta-Binomial and Normal-Normal models built here are direct building blocks for default probability estimation, revenue growth modeling, and margin forecasting.

The central concept introduced in this chapter is the **conjugate prior** — a prior distribution that, when combined with a specific likelihood, produces a posterior in the same distribution family. Conjugate models can be updated analytically without MCMC, which makes them fast and interpretable. They are the right starting point before moving to more complex models.

---

## Sections

| # | File | One-Line Summary |
|---|------|-----------------|
| 2.1 | [Estimating a Probability from Binomial Data](./01-binomial-probability.md) | The Beta-Binomial model — estimating a probability from counts |
| 2.2 | [Posterior as Compromise](./02-posterior-compromise.md) | How the posterior balances prior belief against data evidence |
| 2.3 | [Summarizing Posterior Inference](./03-summarizing-posterior.md) | Point estimates, credible intervals, and posterior probabilities |
| 2.4 | [Informative Prior Distributions](./04-informative-priors.md) | How to encode genuine prior knowledge formally |
| 2.5 | [Normal Distribution with Known Variance](./05-normal-known-variance.md) | The Normal-Normal conjugate model for continuous parameters |
| 2.6 | [Other Single-Parameter Models](./06-other-models.md) | Poisson-Gamma and other conjugate pairs |
| 2.7 | [Example: Cancer Rates](./07-cancer-rates-example.md) | Informative priors applied to a real estimation problem |
| 2.8 | [Noninformative Prior Distributions](./08-noninformative-priors.md) | What to do when you genuinely have no prior knowledge |
| 2.9 | [Weakly Informative Prior Distributions](./09-weakly-informative-priors.md) | The practical middle ground between informative and noninformative |

---

## End of Chapter

- [Financial Utility Summary](./financial-utility-summary.md) — every section mapped to a specific platform use case

---

## Code

| File | What it does |
|------|-------------|
| [beta_binomial_model.py](./code/beta_binomial_model.py) | Beta-Binomial model for default probability and win rate estimation |
| [normal_normal_model.py](./code/normal_normal_model.py) | Normal-Normal conjugate model for revenue growth and margin estimation |
| [chapter02_walkthrough.ipynb](./code/chapter02_walkthrough.ipynb) | Jupyter notebook walking through both models with financial examples |
