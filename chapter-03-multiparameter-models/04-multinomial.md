# 3.4 — Multinomial Model for Categorical Data

## What this section is doing

The Binomial model from Section 2.1 handled two outcomes — success or failure, default or no default. The **Multinomial model** extends this to more than two categories. The conjugate prior is the **Dirichlet distribution**, which generalizes the Beta distribution to multiple probabilities that must sum to 1.

---

## Simplification

Instead of estimating one probability (heads vs tails), you're estimating a full set of probabilities that all add up to 100%. For example: the probability a borrower falls into each of five credit rating categories, or the probability a deal closes in each of four revenue size buckets.

The Dirichlet-Multinomial model is the Beta-Binomial model extended to any number of categories.

---

## The model

**The likelihood — Multinomial:**

$$p(y \mid \theta) \propto \prod_{k=1}^{K} \theta_k^{y_k}$$

Where $y_k$ is the observed count in category $k$ and $\theta_k$ is the true probability of category $k$, with $\sum_k \theta_k = 1$.

**The prior — Dirichlet:**

$$p(\theta) = \text{Dirichlet}(\alpha_1, \ldots, \alpha_K) \propto \prod_{k=1}^{K} \theta_k^{\alpha_k - 1}$$

Each $\alpha_k$ is a pseudo-count for category $k$ — how many prior observations you're encoding for that category.

**The posterior — Dirichlet:**

$$\theta \mid y \sim \text{Dirichlet}(\alpha_1 + y_1, \ldots, \alpha_K + y_K)$$

The update is identical to the Beta-Binomial: add observed counts to prior pseudo-counts, one per category.

---

## Financial application

**Revenue mix estimation:**

A company reports revenue across four segments. You want to estimate the true probability that each segment grows faster than 10% next quarter.

- Prior: encode historical segment growth patterns as Dirichlet pseudo-counts
- Data: observed segment revenue fractions over the past 8 quarters
- Posterior: updated Dirichlet over segment probability vector

The posterior captures not just the estimate for each segment but the correlation structure across segments — if segment A does well, what does that imply about segment B?

**Credit rating transition matrix:**

Each row of a credit rating transition matrix — the probability of moving from rating A to ratings AAA, AA, A, BBB, BB, B, CCC, Default — is a Dirichlet-Multinomial estimation problem. The Dirichlet prior encodes historical transition rates, and each observed transition updates the posterior over the full row of probabilities.

---

## See also

- Section 2.1 for the Binomial-Beta model — the two-category special case
- Section 2.3 for posterior summarization tools that apply to each marginal of the Dirichlet
