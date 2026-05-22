# 12.1 — The Challenge of Efficient Sampling

## What this section is doing

Gelman explains why basic Metropolis-Hastings is slow for high-dimensional posteriors. The core problem is the **random walk** nature of the proposals — the chain moves randomly and slowly, spending many steps in low-probability regions and making many rejected proposals.

---

## The curse of dimensionality in MCMC

In $d$ dimensions, a random walk proposal needs a step size proportional to $d^{-1/2}$ to maintain a reasonable acceptance rate. This means the chain moves a distance of only $1/\sqrt{d}$ per accepted step. For a 50-parameter financial model, effective exploration requires an exponentially large number of steps.

---

## Financial application

A multi-company hierarchical model with 50 companies, each having 3 parameters, plus 6 hyperparameters, has 156 parameters. Random walk Metropolis-Hastings is completely impractical at this scale. HMC and NUTS solve this by using gradient information to make large, directed moves through the parameter space.

---

## See also
- Section 12.2 for the HMC solution
