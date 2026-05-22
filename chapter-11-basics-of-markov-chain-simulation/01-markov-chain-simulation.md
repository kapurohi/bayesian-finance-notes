# 11.1 — The Markov Chain Simulation Procedure

## What this section is doing

Gelman explains how a Markov chain — a sequence of random variables where each depends only on the previous — can be constructed so that its stationary distribution is the posterior. Drawing enough samples from the chain is equivalent to drawing from the posterior.

---

## The key insight

You don't need to compute $p(\theta \mid y)$ to sample from it. You only need to evaluate the unnormalized posterior $p(\theta) \cdot p(y \mid \theta)$ at any point. A Markov chain that uses only these evaluations — comparing the unnormalized posterior at two points — converges to the correct posterior as its stationary distribution.

The normalizing constant $p(y)$ cancels in the ratio. This is why MCMC makes Bayesian inference tractable for complex models.

---

## Burn-in and stationarity

The chain starts at an arbitrary initial value and takes some number of steps before reaching the stationary distribution. These initial steps — the **burn-in** period — are discarded. PyMC's `tune` parameter controls how many burn-in steps are run.

---

## See also
- Section 1.9 for the conceptual introduction to MCMC
- Section 11.4 for how to assess convergence
