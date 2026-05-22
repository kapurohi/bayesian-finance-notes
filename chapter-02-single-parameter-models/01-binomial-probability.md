# 2.1 — Estimating a Probability from Binomial Data

## What this section is doing

This is the first full worked Bayesian model in the book. Gelman takes the simplest possible setup — you observe some number of successes out of some number of trials, and you want to estimate the underlying probability of success — and walks through the entire prior-likelihood-posterior loop analytically. The model is called the **Beta-Binomial** model, and it is the foundation for estimating any probability from count data.

---

## Simplification

You flip a coin 10 times and get 7 heads. What is the probability this coin lands heads?

You could just say 7/10 = 70%. But that ignores everything you knew before flipping — your prior belief that most coins are roughly fair. The Beta-Binomial model combines your prior belief with the observed flips to produce a posterior distribution over the true heads probability.

The same structure applies to any problem where you're estimating a probability from a count of successes and failures — default rates, conversion rates, win rates, fraud rates.

---

## The model

**The unknown parameter:**

$$\theta \in [0, 1]$$

$\theta$ is the true underlying probability of success. It is unknown. We want to estimate it.

**The likelihood — Binomial:**

If you run $n$ independent trials and observe $y$ successes, the probability of that outcome given $\theta$ is:

$$p(y \mid \theta) = \binom{n}{y} \theta^y (1 - \theta)^{n-y}$$

Breaking it down:
- $\binom{n}{y}$ — the number of ways to arrange $y$ successes in $n$ trials. This is a constant that doesn't depend on $\theta$, so it drops out when we compute the posterior
- $\theta^y$ — the probability of getting exactly $y$ successes
- $(1 - \theta)^{n-y}$ — the probability of getting exactly $n - y$ failures

**The prior — Beta:**

We need a prior over $\theta$ that lives between 0 and 1. The Beta distribution is the natural choice:

$$p(\theta) = \text{Beta}(\alpha, \beta) \propto \theta^{\alpha - 1}(1 - \theta)^{\beta - 1}$$

The parameters $\alpha$ and $\beta$ are called **hyperparameters** — they control the shape of the prior, not the data. You choose them to reflect your prior belief:

- $\alpha = \beta = 1$ — completely flat prior, all probabilities equally likely
- $\alpha = 10, \beta = 10$ — prior centered at 0.5 with moderate confidence
- $\alpha = 2, \beta = 8$ — prior centered around 0.2, reflecting belief in a low success rate

**The posterior — also Beta:**

Multiply the prior by the likelihood and simplify:

$$p(\theta \mid y) \propto \theta^{\alpha - 1}(1-\theta)^{\beta-1} \cdot \theta^y(1-\theta)^{n-y}$$

$$= \theta^{(\alpha + y) - 1}(1-\theta)^{(\beta + n - y) - 1}$$

$$= \text{Beta}(\alpha + y, \; \beta + n - y)$$

This is what makes it conjugate. The posterior is a Beta distribution with updated parameters. No MCMC needed — the update is just addition.

---

## The update rule in plain English

| Quantity | Before data | After observing $y$ successes in $n$ trials |
|----------|-------------|----------------------------------------------|
| Prior successes | $\alpha$ | $\alpha + y$ |
| Prior failures | $\beta$ | $\beta + (n - y)$ |

Your prior pseudo-counts $\alpha$ and $\beta$ get augmented by the actual observed counts. The posterior mean is:

$$\mathbb{E}[\theta \mid y] = \frac{\alpha + y}{\alpha + \beta + n}$$

As $n$ grows large, the data dominates and the posterior mean converges to $y/n$ — the simple frequency. With small $n$, the prior pulls the estimate toward $\alpha / (\alpha + \beta)$.

---

## Financial application

**Default probability estimation:**

You have a portfolio of 50 investment-grade bonds. 2 have defaulted. You want to estimate the true underlying default probability $\theta$.

- Prior: historical IG default rates suggest $\theta$ is around 1–3%. Encode as $\text{Beta}(2, 98)$ — prior mean of 2%
- Observed data: $y = 2$ defaults in $n = 50$ bonds
- Posterior: $\text{Beta}(2 + 2, \; 98 + 48) = \text{Beta}(4, 146)$
- Posterior mean: $4 / 150 \approx 2.7\%$

The posterior mean sits between the prior mean (2%) and the raw data frequency (4%), pulled toward the prior because $n = 50$ is not large enough to fully override it.

**Win rate / conversion rate:**

The same model applies to sales conversion rates, deal close rates, or any other probability estimated from a count of successes and failures.

---

## See also

- Section 1.1 for the three-step loop this model instantiates
- Section 2.2 for how the posterior sits between prior and data
- Section 2.4 for how to set $\alpha$ and $\beta$ from genuine prior knowledge
