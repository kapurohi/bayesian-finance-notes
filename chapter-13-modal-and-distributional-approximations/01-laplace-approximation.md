# 13.1 — Laplace's Method

## What this section is doing

The Laplace approximation fits a Normal distribution to the posterior by matching the mode and the curvature at the mode. It is a second-order Taylor expansion of the log-posterior around the MAP estimate.

---

## The approximation

$$\log p(\theta \mid y) \approx \log p(\hat{\theta} \mid y) - \frac{1}{2}(\theta - \hat{\theta})^T H (\theta - \hat{\theta})$$

Where $\hat{\theta}$ is the MAP estimate and $H$ is the negative Hessian of the log-posterior at $\hat{\theta}$.

This gives a Normal approximation:

$$p(\theta \mid y) \approx \text{Normal}(\hat{\theta}, H^{-1})$$

---

## When it works

Good when the posterior is unimodal and approximately symmetric — which the asymptotic theory (Chapter 4) says is true for large samples. Fails for multimodal posteriors, heavy-tailed posteriors, and posteriors with strong parameter correlations.

---

## Financial application

For mature companies with long earnings histories (large $n$), the Laplace approximation is often accurate enough for preliminary analysis and is significantly faster than MCMC. For newly listed companies or tail-risk scenarios, the approximation is unreliable and full MCMC is required.

---

## See also
- Section 4.1 for the asymptotic Normal posterior that motivates this approximation
