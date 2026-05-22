# 2.2 — Posterior as Compromise Between Data and Prior

## What this section is doing

Gelman shows that the posterior is never purely the data and never purely the prior — it is always a weighted average of the two. The weight given to each depends on how much data you have relative to how strong your prior is. This section makes that trade-off precise and quantitative.

---

## Simplification

Imagine two people estimating the same thing. One is an experienced industry analyst who has spent 20 years studying this sector — she has strong prior beliefs. The other is a data scientist who only looks at the numbers from the last two quarters and ignores all background knowledge.

The Bayesian posterior is what you get when you force those two people to reconcile their views in a principled way. With very little data, the analyst dominates. With a lot of data, the numbers take over. The posterior tracks that trade-off exactly.

---

## The posterior mean as a weighted average

For the Beta-Binomial model from Section 2.1, the posterior mean can be written as:

$$\mathbb{E}[\theta \mid y] = \frac{\alpha + \beta}{\alpha + \beta + n} \cdot \frac{\alpha}{\alpha + \beta} + \frac{n}{\alpha + \beta + n} \cdot \frac{y}{n}$$

This looks complicated but it is just a weighted average of two quantities:

- **Prior mean:** $\frac{\alpha}{\alpha + \beta}$ — what you believed before seeing data
- **Data frequency:** $\frac{y}{n}$ — what the raw data says

The weights are:
- **Prior weight:** $\frac{\alpha + \beta}{\alpha + \beta + n}$ — how strong the prior is relative to the total information
- **Data weight:** $\frac{n}{\alpha + \beta + n}$ — how much data you have relative to the total information

The quantity $\alpha + \beta$ acts as the **effective sample size of the prior** — it represents how many pseudo-observations your prior beliefs are worth.

---

## What happens at the extremes

**When data is large ($n \gg \alpha + \beta$):**

The data weight approaches 1 and the prior weight approaches 0. The posterior mean converges to the raw data frequency $y/n$. The prior becomes irrelevant. This is the correct behavior — enough data should override any prior.

**When data is sparse ($n \ll \alpha + \beta$):**

The prior weight dominates. The posterior mean stays close to the prior mean. The data barely moves the estimate. This is also correct — with very little data, your background knowledge should carry most of the weight.

**When the prior is flat ($\alpha = \beta = 1$):**

The effective prior sample size is only 2. Even a small dataset will dominate. A flat prior is a way of saying "I have almost no prior knowledge — let the data speak."

---

## Financial application

**New company, limited earnings history:**

A company just listed with 3 quarters of earnings. Raw data says revenue growth is 15%. Sector prior says growth for this type of company is typically around 8%, encoded with an effective sample size of 8 quarters.

- Prior weight: $8 / (8 + 3) \approx 73\%$
- Data weight: $3 / (8 + 3) \approx 27\%$
- Posterior mean: $0.73 \times 8\% + 0.27 \times 15\% \approx 9.9\%$

The posterior estimate of 9.9% is more conservative than the raw 15% figure because three quarters is not enough history to fully trust.

**Mature company, long earnings history:**

Same sector prior, but now the company has 40 quarters of history averaging 12% growth.

- Prior weight: $8 / (8 + 40) \approx 17\%$
- Data weight: $40 / (8 + 40) \approx 83\%$
- Posterior mean: $0.17 \times 8\% + 0.83 \times 12\% \approx 11.3\%$

The posterior is now much closer to the data. With 40 quarters of history, the sector prior has minimal influence.

---

## See also

- Section 2.1 for the Beta-Binomial model this analysis is based on
- Section 2.4 for how to set the prior strength $\alpha + \beta$ from real domain knowledge
- Section 1.6 for the sequential updating structure that underlies this trade-off
