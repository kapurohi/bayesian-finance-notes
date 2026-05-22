# 11.3 — Gibbs Sampling

## What this section is doing

Gibbs sampling is a special case of Metropolis-Hastings that is applicable when you can sample directly from the **full conditional distributions** — the distribution of each parameter given all other parameters and the data. It accepts every proposal (acceptance rate = 100%) and is highly efficient when the conditionals are tractable.

---

## The algorithm

For a model with parameters $(\theta_1, \theta_2, \ldots, \theta_K)$:

1. Initialize all parameters
2. At each step, cycle through parameters:
   - Sample $\theta_1^{(t+1)} \sim p(\theta_1 \mid \theta_2^{(t)}, \ldots, \theta_K^{(t)}, y)$
   - Sample $\theta_2^{(t+1)} \sim p(\theta_2 \mid \theta_1^{(t+1)}, \theta_3^{(t)}, \ldots, y)$
   - Continue for all parameters
3. Repeat

---

## Financial application

Hierarchical models often have tractable full conditionals. The company-level parameters have Normal full conditionals given the hyperparameters; the hyperparameters have tractable conditionals given the company parameters. This Gibbs structure makes hierarchical model inference efficient — PyMC automatically identifies and exploits it.

---

## See also
- Section 10.3 for factored distributions that enable efficient Gibbs sampling
