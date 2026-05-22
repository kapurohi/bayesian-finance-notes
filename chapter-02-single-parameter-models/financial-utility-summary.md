# Chapter 2 — Financial Utility Summary

This is the end-of-chapter map connecting every section to a specific use case for the platform.

---

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 2.1 — Beta-Binomial | Estimating a probability from count data | Default probability, conversion rates, win rates. The posterior is $\text{Beta}(\alpha + y, \beta + n - y)$ — a direct closed-form update with no MCMC needed. |
| 2.2 — Posterior Compromise | Posterior as precision-weighted average of prior and data | Governs how aggressively new earnings data overrides sector priors. Few quarters: prior dominates. Long history: data dominates. Quantifies exactly how much weight each source gets. |
| 2.3 — Summarizing Posteriors | Mean, median, credible intervals, direct probability statements | The output layer of the platform. Clients receive 95% credible intervals and probability statements — "73% chance growth exceeds 8%" — not point estimates. |
| 2.4 — Informative Priors | Moment matching and effective sample size for prior construction | Sector-level benchmarks get formally encoded as Beta or Normal priors via moment matching. Prior strength is set by choosing $\alpha + \beta$ or $\tau_0^2$ to match the reliability of the historical benchmark data. |
| 2.5 — Normal-Normal | Conjugate model for continuous quantities | The core model for revenue growth rates, operating margins, and return estimation. Posterior mean and variance have closed-form solutions — fast, interpretable, production-ready. |
| 2.6 — Poisson-Gamma | Count data and event rate estimation | Default event frequency, earnings restatement rates, credit event arrival rates. The Gamma posterior updates by adding observed counts and periods — another closed-form conjugate update. |
| 2.7 — Cancer Rates Example | Small-area estimation — prior stabilizes noisy small-sample estimates | Post-IPO and small-cap coverage universe. Companies with limited earnings history get prior-stabilized estimates. The same stabilization mechanism Gelman demonstrates across US counties applies directly to cross-sectional company coverage. |
| 2.8 — Noninformative Priors | Flat and Jeffreys priors — encoding ignorance | Used for sensitivity analysis and for demonstrating that model conclusions are data-driven. Not the default for production models where sector knowledge exists. |
| 2.9 — Weakly Informative Priors | Prior that constrains without dominating | Default prior choice for production models. Sector median centers the prior. Wide variance lets data move the posterior. Distribution family enforces physical constraints (positivity, boundedness). |

---

## The Three Production Models Chapter 2 Delivers

**Model 1 — Default Probability (Beta-Binomial)**

Sections 2.1, 2.2, 2.4

$$\theta \sim \text{Beta}(\alpha, \beta) \qquad y \mid \theta \sim \text{Binomial}(n, \theta)$$
$$\theta \mid y \sim \text{Beta}(\alpha + y, \; \beta + n - y)$$

Use for: default probability, fraud rate, conversion rate, any probability estimated from counts.

**Model 2 — Growth Rate / Margin (Normal-Normal)**

Sections 2.5, 2.4, 2.9

$$\mu \sim \text{Normal}(\mu_0, \tau_0^2) \qquad y_i \mid \mu \sim \text{Normal}(\mu, \sigma^2)$$
$$\mu \mid y \sim \text{Normal}(\mu_n, \tau_n^2)$$

Use for: revenue growth rate, operating margin, return estimation, any continuous financial metric.

**Model 3 — Event Rate (Poisson-Gamma)**

Section 2.6

$$\lambda \sim \text{Gamma}(\alpha, \beta) \qquad y \mid \lambda \sim \text{Poisson}(\lambda)$$
$$\lambda \mid y \sim \text{Gamma}\!\left(\alpha + \textstyle\sum y_i, \; \beta + n\right)$$

Use for: credit event frequency, default arrival rates, earnings restatement rates.

---

## Connection to Chapter 1

The three-step loop from Chapter 1 Section 1.1 is now instantiated in three concrete models. The philosophical framework from Chapter 1 — prior encodes existing knowledge, likelihood weights the data, posterior is the update — maps directly to the $\alpha$, $\beta$ hyperparameter choices and the closed-form update equations derived here.

The small-sample robustness discussed in Chapter 1 Section 1.10 is now quantified precisely through the effective sample size of the prior ($\alpha + \beta$ for Beta, $1/\tau_0^2$ for Normal). The prior stabilization mechanism from the cancer rates example in Section 2.7 is the Chapter 1 small-sample argument made concrete and computable.
