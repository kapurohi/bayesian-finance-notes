# 11.2 — The Metropolis-Hastings Algorithm

## What this section is doing

Metropolis-Hastings is the foundational MCMC algorithm. At each step, a candidate parameter value is proposed from a proposal distribution, and the candidate is accepted or rejected with a probability that ensures the chain converges to the correct posterior.

---

## The algorithm

1. Start at $\theta^{(t)}$
2. Propose a candidate: $\theta^* \sim q(\theta^* \mid \theta^{(t)})$
3. Compute the acceptance ratio:

$$r = \frac{p(\theta^* \mid y) / q(\theta^* \mid \theta^{(t)})}{p(\theta^{(t)} \mid y) / q(\theta^{(t)} \mid \theta^*)}$$

4. Accept $\theta^{(t+1)} = \theta^*$ with probability $\min(1, r)$; otherwise $\theta^{(t+1)} = \theta^{(t)}$

The acceptance ratio only requires the unnormalized posterior — $p(y)$ cancels in the ratio.

---

## The proposal matters

A proposal that moves too far: high rejection rate, slow mixing.
A proposal that moves too little: high acceptance rate, slow exploration.
Target acceptance rate is typically 23-44% for scalar parameters.

Modern algorithms (HMC, NUTS) automatically tune the proposal using gradient information — this is why they are far more efficient than basic Metropolis-Hastings.

---

## See also
- Section 11.4 for convergence assessment
- Chapter 12 for the HMC and NUTS algorithms that supersede this
