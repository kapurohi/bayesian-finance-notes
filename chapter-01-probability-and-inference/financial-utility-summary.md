# Chapter 1 — Financial Utility Summary

This is the end-of-chapter map. Every section connected to a specific use case for the platform.

---

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 1.1 — Three Steps | Prior → Likelihood → Posterior | The update loop that replaces static DCF assumptions. Every new earnings release triggers a posterior update instead of a manual model rebuild. |
| 1.2 — Notation | $y$, $\theta$, $\tilde{y}$, exchangeability | The data architecture. Observed financials are $y$. True growth/margin parameters are $\theta$. Forward forecasts are $\tilde{y}$. Exchangeability justifies data pooling across segments. |
| 1.3 — Bayes' Rule | $p(\theta \mid y) \propto p(\theta) \cdot p(y \mid \theta)$ | The core engine. Sequential updates mean today's posterior becomes tomorrow's prior — the model is always current without being rebuilt. |
| 1.4 — Discrete Examples | Base rate problem | Credit scoring, fraud detection, earnings surprise models. Prior probability of the event (base rate) must always be encoded — a high-sensitivity model with a low base rate produces mostly false alarms. |
| 1.5 — Probability as Uncertainty | Epistemic probability | The philosophical license for placing distributions over one-time financial events — a specific company's next-quarter revenue, a specific deal's closing probability. |
| 1.6 — Genetic Example | Structural priors, sequential updating | Industry-level margin and growth distributions serve as structural priors for companies with limited earnings history. Post-IPO companies get sector-constrained estimates before enough company data exists. |
| 1.7 — Spelling Correction | MAP vs. full posterior | The full posterior over intrinsic value is more useful than any point estimate. Clients receive probability distributions — "73% chance fair value exceeds current price" — not a single DCF output. |
| 1.8 — Probability Theory | Law of total probability, total expectation | Reference toolkit for the derivations in Chapters 2–3. Used in the normalizing constant computation and in expected value calculations under parameter uncertainty. |
| 1.9 — Computation | MCMC, HMC, NUTS, PyMC | The production backend. PyMC handles model specification, NUTS handles sampling, $\hat{R}$ handles convergence validation. The platform never needs to solve intractable integrals analytically. |
| 1.10 — Applied Statistics | Small-sample robustness, coherent uncertainty, posterior predictive checks | The five capabilities that make Bayesian models superior for production financial systems — especially for sparse data, forward forecasting, and model validation. |

---

## The Five Platform Capabilities Chapter 1 Unlocks

**1. Living DCF Model**

The three-step update loop (1.1, 1.3) replaces a static spreadsheet with a model that recalibrates automatically on every new earnings release. The prior encodes historical sector knowledge. The likelihood weights the new data. The posterior is the updated view.

**2. Probabilistic Output Layer**

Section 1.10 justifies replacing single-point DCF outputs with full posterior distributions over intrinsic value. The platform delivers probability statements — "there is an 81% probability that fair value exceeds the current share price" — that are directly actionable by investors.

**3. Small-Data Robustness**

Sections 1.4 and 1.10 show that Bayesian priors stabilize estimates when data is sparse. Critical for newly listed companies, emerging market equities, and any coverage universe with fewer than 8 quarters of history.

**4. Structural Prior Architecture**

Section 1.6 maps directly to using industry-level distributions as structural priors before company-specific data is sufficient. This is the architectural preview of the hierarchical model in Chapter 5 — the platform's solution to the new-company cold-start problem.

**5. Coherent Risk Propagation**

Section 1.10 establishes that parameter uncertainty — in WACC, growth rate, margin — automatically propagates into output uncertainty without manual scenario generation. One model run produces the full distribution over intrinsic value.

---

## Next Chapter

Chapter 2 — Single-Parameter Models — is where the engine from Chapter 1 gets put to work for the first time on real model structures:

- **Beta-Binomial model** — for default probabilities, win rates, conversion rates
- **Normal-Normal conjugate model** — for revenue growth rates and operating margins
- **Poisson-Gamma model** — for count-based financial metrics

These are the direct building blocks of the platform's first production models.
