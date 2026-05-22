# 2.6 — Other Single-Parameter Models

## What this section is doing

Gelman extends the conjugate prior framework beyond the Beta-Binomial and Normal-Normal models. The key addition is the **Poisson-Gamma** model for count data, plus a general summary of conjugate pairs. Each model is the right tool for a different type of financial measurement.

---

## The Poisson-Gamma model

**When to use it:** When your data is a count of events over a fixed period — number of defaults in a portfolio per quarter, number of trades per day, number of earnings restatements per year.

**The likelihood — Poisson:**

$$p(y \mid \lambda) = \frac{\lambda^y e^{-\lambda}}{y!}$$

$\lambda$ is the true underlying rate — the expected number of events per period. $y$ is the observed count.

**The prior — Gamma:**

$$\lambda \sim \text{Gamma}(\alpha, \beta)$$

- Prior mean: $\alpha / \beta$
- Prior variance: $\alpha / \beta^2$

**The posterior — Gamma:**

$$\lambda \mid y_1, \ldots, y_n \sim \text{Gamma}\left(\alpha + \sum y_i, \; \beta + n\right)$$

The update is simple: add observed total counts to $\alpha$, add number of periods to $\beta$.

**Financial application:** Estimating the arrival rate of credit events in a portfolio. Prior encodes historical base rate. Each quarter of observed defaults updates the posterior rate.

---

## Conjugate prior summary table

| Likelihood | Conjugate Prior | Posterior Family | Typical Use Case |
|------------|----------------|-----------------|------------------|
| Binomial | Beta | Beta | Default rates, conversion rates, win rates |
| Normal (known $\sigma^2$) | Normal | Normal | Growth rates, margins, returns |
| Poisson | Gamma | Gamma | Event counts, default frequencies |
| Exponential | Gamma | Gamma | Time between events, duration models |
| Normal (known $\mu$) | Inverse-Gamma | Inverse-Gamma | Variance estimation, volatility |

---

## See also

- Section 2.1 for the Beta-Binomial model in full detail
- Section 2.5 for the Normal-Normal model in full detail
- Section 3.6 for the multivariate normal model that extends these to joint estimation
