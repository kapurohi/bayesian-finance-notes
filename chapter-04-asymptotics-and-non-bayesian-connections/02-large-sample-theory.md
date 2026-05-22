# 4.2 — Large-Sample Theory

## What this section is doing

Gelman formalizes the asymptotic behavior of Bayesian posteriors. Two key results: **posterior consistency** (the posterior concentrates on the true parameter value as $n \to \infty$) and **asymptotic efficiency** (the posterior variance achieves the Cramér-Rao lower bound — no estimator can do better with that amount of data).

---

## Simplification

As you collect more and more data, two things happen to your posterior:

1. It gets narrower and narrower — you become more and more certain about the true value
2. It converges to the right answer — the center of the posterior moves toward the true parameter

These are called consistency and efficiency. They tell you that Bayesian inference is working correctly in the long run — it learns from data and converges to the truth.

---

## Key results

**Posterior consistency:**

For a well-specified model with a proper prior, as $n \to \infty$:

$$p(\theta \mid y_1, \ldots, y_n) \to \delta(\theta_{\text{true}})$$

The posterior collapses to a point mass at the true value.

**Asymptotic efficiency:**

The posterior variance satisfies:

$$\text{Var}(\theta \mid y) \approx \frac{1}{n \cdot I(\theta_{\text{true}})}$$

Where $I(\theta_{\text{true}})$ is the Fisher information at the true parameter. This is the theoretical minimum variance achievable by any unbiased estimator — the Cramér-Rao bound.

---

## Financial application

These results justify using Bayesian models on large financial datasets — equity return series, transaction data, credit histories — with confidence that the posteriors will converge to the correct estimates. With large $n$, the choice of prior becomes irrelevant and the posterior variance shrinks predictably.

---

## See also

- Section 4.1 for the Normal approximation that follows from these results
- Section 4.3 for the cases where these results break down
