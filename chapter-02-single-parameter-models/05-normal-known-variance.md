# 2.5 — Normal Distribution with Known Variance

## What this section is doing

Gelman introduces the second major conjugate model: the Normal-Normal model. The setup is that your observations are normally distributed around an unknown mean $\mu$, and your prior over $\mu$ is also normal. The result is a normal posterior — and the update rules are clean and intuitive. This is the model for estimating continuous financial quantities like revenue growth rates, margins, and returns.

---

## Simplification

The Beta-Binomial model from Section 2.1 was for probabilities — things bounded between 0 and 1. The Normal-Normal model is for continuous quantities that can take any value — growth rates, margins, returns, spreads.

The intuition is identical: you have a prior belief about a quantity, you observe data, and the posterior is a compromise between the two. The math just looks different because the distribution family is different.

---

## The model

**The likelihood — Normal with known variance:**

$$y_i \mid \mu \sim \text{Normal}(\mu, \sigma^2)$$

Each observation $y_i$ is drawn from a normal distribution centered on the true underlying mean $\mu$. The variance $\sigma^2$ is assumed known for now — Section 3.2 relaxes this.

**The prior — Normal:**

$$\mu \sim \text{Normal}(\mu_0, \tau_0^2)$$

- $\mu_0$ — your prior mean, what you believed the true value was before seeing data
- $\tau_0^2$ — your prior variance, how uncertain you were about $\mu_0$

**The posterior — Normal:**

$$\mu \mid y \sim \text{Normal}(\mu_n, \tau_n^2)$$

Where the updated parameters are:

$$\frac{1}{\tau_n^2} = \frac{1}{\tau_0^2} + \frac{n}{\sigma^2}$$

$$\mu_n = \frac{\frac{\mu_0}{\tau_0^2} + \frac{n\bar{y}}{\sigma^2}}{\frac{1}{\tau_0^2} + \frac{n}{\sigma^2}}$$

---

## Breaking down the update equations

The posterior precision $1/\tau_n^2$ is just the sum of the prior precision $1/\tau_0^2$ and the data precision $n/\sigma^2$.

**Precision** is the reciprocal of variance — a high-precision distribution is narrow and confident, a low-precision distribution is wide and uncertain. Adding precisions is how you combine two independent sources of information: prior knowledge and observed data.

The posterior mean $\mu_n$ is a precision-weighted average of the prior mean and the data mean $\bar{y}$:

- If the prior is very precise (small $\tau_0^2$), the posterior mean stays close to $\mu_0$
- If the data is very precise (large $n$, small $\sigma^2$), the posterior mean moves toward $\bar{y}$
- With equal precision, the posterior mean sits exactly halfway between the two

This is the same compromise structure from Section 2.2, now applied to continuous quantities.

---

## Financial application

**Revenue growth rate estimation:**

You are estimating the true underlying revenue growth rate $\mu$ for a technology company.

- Prior: sector benchmarks suggest $\mu_0 = 0.08$ (8%), with $\tau_0 = 0.04$ (fairly confident within a few percentage points)
- Observed data: 6 quarters with mean growth $\bar{y} = 0.11$ (11%), typical quarter-to-quarter noise $\sigma = 0.03$

Computing posterior precision:

$$\frac{1}{\tau_n^2} = \frac{1}{0.04^2} + \frac{6}{0.03^2} = 625 + 6{,}667 = 7{,}292$$

$$\tau_n = \sqrt{1/7292} \approx 0.012 \quad \text{(much tighter than the prior)}$$

Posterior mean:

$$\mu_n = \frac{625 \times 0.08 + 6667 \times 0.11}{7292} \approx 0.107$$

The posterior estimate of 10.7% sits between the prior (8%) and the data (11%), pulled toward the data because 6 quarters of observations outweigh the prior precision.

---

## See also

- Section 2.1 for the Beta-Binomial analogue for probabilities
- Section 2.2 for the prior-data compromise structure
- Section 3.2 for the extension to unknown variance — the more realistic model
