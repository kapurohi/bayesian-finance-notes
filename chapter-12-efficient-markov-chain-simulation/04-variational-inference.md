# 12.4 — Variational Inference

## What this section is doing

Variational inference (VI) approximates the posterior with a simpler distribution — typically a product of Normals — by minimizing the KL divergence between the approximation and the true posterior. It is much faster than MCMC but less accurate, especially for posteriors with complex geometry or heavy tails.

---

## When to use VI

- **Large-scale screening:** Fit many models quickly to identify which ones are worth full MCMC analysis
- **Real-time applications:** When latency constraints prevent full MCMC sampling
- **Exploratory analysis:** Getting rough estimates quickly before committing to full inference

**Do not use VI for final production output** on models where tail probabilities matter — VI systematically underestimates posterior variance and can produce overconfident credible intervals.

---

## PyMC variational inference

```python
with model:
    approx = pm.fit(method='advi', n=100000)
    trace_vi = approx.sample(2000)
```

ADVI (Automatic Differentiation Variational Inference) is PyMC's default VI method.

---

## See also
- Chapter 13 for related approximation methods
