# 1.8 — Some Useful Results from Probability Theory

## What this section is doing

This section is a toolkit. Gelman collects the core probability identities that show up repeatedly in derivations throughout the book. None of these are new ideas — they are results from basic probability theory that you will keep reaching for as models get more complex in later chapters.

---

## The Law of Total Probability

If you want the marginal probability of $y$ but $\theta$ is unknown, you sum (or integrate) over every possible value of $\theta$, weighting each by how probable that value is:

$$p(y) = \int p(y \mid \theta) \cdot p(\theta) \, d\theta$$

Breaking it down:

- You can't directly compute $p(y)$ because you don't know $\theta$
- So you ask: for every possible value of $\theta$, how probable is $y$?
- You then average those probabilities, weighted by how likely each $\theta$ is

This is the normalizing constant from Section 1.3 — the denominator in Bayes' rule. It's why the posterior integral is usually intractable for complex models, and why MCMC exists.

**In finance:** the total probability of observing a specific earnings figure is the average of the conditional probabilities of that figure across all plausible growth rate scenarios, weighted by how probable each scenario is.

---

## The Law of Total Expectation

$$\mathbb{E}[y] = \mathbb{E}\left[\mathbb{E}[y \mid \theta]\right]$$

The overall expected value of $y$ equals the average, over all possible $\theta$ values, of the conditional expected value of $y$ given $\theta$.

In plain terms: if you don't know $\theta$ exactly, you compute the expected outcome for each possible $\theta$, then average those expectations weighted by how probable each $\theta$ is.

**In finance:** the expected revenue next quarter is not just the forecast conditional on one assumed growth rate — it is the average of conditional revenue forecasts across the full distribution of possible growth rates. This is what the posterior predictive distribution from Section 1.3 is computing.

---

## Conditional Independence

Two observations $y_1$ and $y_2$ are conditionally independent given $\theta$ if:

$$p(y_1, y_2 \mid \theta) = p(y_1 \mid \theta) \cdot p(y_2 \mid \theta)$$

This means: once you know $\theta$, learning $y_1$ tells you nothing additional about $y_2$.

**In finance:** quarterly revenue figures might be correlated with each other in general — a good Q1 tends to predict a good Q2. But conditional on the true underlying growth rate $\theta$, each quarter is an independent noisy draw. That conditional independence assumption is what makes the likelihood for the Normal model tractable, and it is worth knowing when it is and isn't reasonable.

---

## Change of Variables

When you transform a parameter — for example, modeling $\log(\theta)$ instead of $\theta$ directly — the probability density changes according to:

$$p_{\log\theta}(\log\theta) = p_\theta(\theta) \cdot \left|\frac{d\theta}{d\log\theta}\right|$$

The extra term is the Jacobian of the transformation. It accounts for the fact that stretching or compressing the parameter scale changes how probability mass is distributed.

**In finance:** financial ratios, returns, and growth rates are often log-transformed before modeling because they are bounded below by zero and tend to be right-skewed. When you transform parameters, the prior needs to be adjusted accordingly — PyMC handles this automatically when you use distributions like `pm.LogNormal`.

---

## When these show up

| Identity | Where it appears next |
|----------|-----------------------|
| Law of total probability | Chapter 2 normalizing constants, Chapter 3 marginal posteriors |
| Law of total expectation | Posterior predictive mean calculations throughout |
| Conditional independence | Likelihood factorization in every multi-observation model |
| Change of variables | Log-normal models, variance parameter transformations |
