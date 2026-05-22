# 2.3 — Summarizing Posterior Inference

## What this section is doing

Once you have a posterior distribution, you need to communicate it. Gelman covers the standard tools for summarizing what a posterior says — point estimates, interval estimates, and direct probability statements. This section is about turning a distribution into something actionable.

---

## Simplification

The posterior is a full probability distribution — a curve showing how probable each value of $\theta$ is. That's powerful but also a lot of information. This section is about how to compress that curve into specific, useful statements without losing what matters.

---

## Point estimates

Sometimes you need a single number. There are three common choices:

**Posterior mean:**

$$\mathbb{E}[\theta \mid y] = \int \theta \cdot p(\theta \mid y) \, d\theta$$

The probability-weighted average of all possible $\theta$ values. Best choice when the posterior is roughly symmetric. This is what minimizes expected squared error.

**Posterior median:**

The value of $\theta$ where half the posterior probability sits below and half above. More robust than the mean when the posterior is skewed — for example, when estimating a probability that is close to 0 or 1.

**MAP (Maximum A Posteriori):**

$$\hat{\theta}_{MAP} = \arg\max_\theta \, p(\theta \mid y)$$

The single most probable value — the peak of the posterior. As noted in Section 1.7, the MAP throws away the shape of the distribution entirely. It is the least informative summary and should generally be avoided in favor of the full posterior.

---

## Credible intervals

A **credible interval** is a range of $\theta$ values that contains a specified probability of the posterior mass.

A 95% credible interval $[a, b]$ means:

$$p(a \leq \theta \leq b \mid y) = 0.95$$

There is a 95% probability that the true parameter lies in this interval. This is the statement most people think a frequentist confidence interval is making — but it isn't. The Bayesian credible interval actually says what it sounds like.

**Equal-tailed interval:** Cut 2.5% from each tail. Simple and standard.

**Highest Density Interval (HDI):** The shortest interval containing the required probability mass. More informative when the posterior is asymmetric.

---

## Direct probability statements

This is where the posterior is most powerful. You can directly compute the probability of any event involving $\theta$:

$$p(\theta > 0.05 \mid y) = \int_{0.05}^{1} p(\theta \mid y) \, d\theta$$

In financial terms:
- Probability that revenue growth exceeds 8% next quarter
- Probability that the default rate is below the covenant threshold
- Probability that operating margin expands year over year

These statements have no clean frequentist equivalent. They are natural outputs of a Bayesian model.

---

## Financial application

Returning to the default probability example from Section 2.1 — posterior $\text{Beta}(4, 146)$:

| Summary | Value |
|---------|-------|
| Posterior mean | $4/150 = 2.7\%$ |
| Posterior median | $\approx 2.6\%$ |
| 95% credible interval | $[0.7\%, 6.1\%]$ |
| $p(\theta > 5\%)$ | $\approx 7\%$ |
| $p(\theta < 1\%)$ | $\approx 12\%$ |

These are the numbers you serve to a credit risk manager. Not "the default rate is 2.7%" — but a full picture of the uncertainty around that estimate with direct probability statements about the scenarios that matter.

---

## See also

- Section 1.7 for the MAP vs full posterior discussion
- Section 2.1 for the Beta-Binomial model these summaries are computed from
- Section 1.5 for why Bayesian probability statements like $p(\theta > 5\%)$ are valid
