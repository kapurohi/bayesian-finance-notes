# 14.4 — Variable Selection

## What this section is doing

With many potential predictors, you want to select only the relevant ones. Bayesian variable selection uses spike-and-slab priors — a mixture of a point mass at zero (variable excluded) and a diffuse Normal (variable included) — to simultaneously estimate which variables matter and what their coefficients are.

---

## Spike-and-slab prior

$$\beta_k \mid \gamma_k \sim (1-\gamma_k) \cdot \delta_0 + \gamma_k \cdot \text{Normal}(0, \tau^2)$$

$$\gamma_k \sim \text{Bernoulli}(p_0)$$

Where $\gamma_k = 1$ means variable $k$ is included and $\gamma_k = 0$ means it is excluded.

The posterior over $\gamma_k$ gives the **posterior inclusion probability** — the probability that each variable is genuinely relevant.

---

## Financial application

Factor model selection: given 20 candidate financial ratio predictors for earnings growth, the spike-and-slab model produces posterior inclusion probabilities for each factor. Factors with inclusion probability greater than 0.5 are likely genuine drivers. The model naturally handles correlated factors — it selects the most predictive non-redundant subset.

---

## See also
- Chapter 15 for hierarchical regularization as an alternative to explicit variable selection
