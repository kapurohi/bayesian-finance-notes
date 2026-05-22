# 4.1 — Normal Approximation to the Posterior

## What this section is doing

Gelman shows that as the number of observations grows, any well-behaved posterior distribution becomes approximately Normal — regardless of what prior you used. This result, called the **Bernstein-von Mises theorem**, is the asymptotic justification for why Bayesian and frequentist methods converge with large data.

---

## Simplification

No matter what shape your prior started with — skewed, wide, multimodal — pour enough data into a Bayesian model and the posterior will eventually look like a bell curve. The data overwhelms the prior and the posterior concentrates around the true parameter value.

This is reassuring: with a lot of data, your choice of prior stops mattering. The posterior is driven almost entirely by the likelihood.

---

## The math

The posterior can be approximated as:

$$p(\theta \mid y) \approx \text{Normal}\!\left(\hat{\theta}, \, [I(\hat{\theta})]^{-1}\right)$$

Where:
- $\hat{\theta}$ is the **maximum likelihood estimate (MLE)** — the value of $\theta$ that maximizes $p(y \mid \theta)$
- $I(\hat{\theta})$ is the **observed Fisher information** — the curvature of the log-likelihood at the MLE. Higher curvature means a narrower, more certain posterior.

The approximation improves as $n$ grows. For small $n$, it may be poor — especially if the posterior is skewed or the prior is informative.

---

## Financial application

For a mature company with 40+ quarters of earnings history, the Normal approximation to the growth rate posterior is typically very good. The data dominates, the prior is irrelevant, and the posterior is well-approximated by a Normal centered at the sample mean.

For a recently listed company with 4 quarters of history, the approximation may be poor — the posterior can be skewed and the prior still has meaningful influence. This is exactly where full MCMC sampling (Chapters 11–12) is worth the computational cost.

---

## See also

- Section 3.2 for the exact Student-t posterior that the Normal approximation is replacing
- Section 4.2 for the formal large-sample theory underlying this result
