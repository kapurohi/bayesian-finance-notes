# 11.4 — Convergence of Markov Chains

## What this section is doing

Gelman establishes the theoretical conditions under which MCMC chains converge to the correct posterior — and more practically, how to know when they have converged in a specific run.

---

## Theoretical conditions

A Markov chain converges to the correct stationary distribution if it is:
- **Irreducible:** It can reach any region of the parameter space from any starting point
- **Aperiodic:** It doesn't cycle through states in a fixed pattern
- **Positive recurrent:** It returns to any region of the space in finite expected time

The Metropolis-Hastings algorithm satisfies these conditions under mild regularity conditions on the posterior and proposal.

---

## Practical implications

Convergence is guaranteed asymptotically — given infinite samples. In practice you run a finite chain and assess whether convergence has been achieved sufficiently. This is the job of the diagnostics in Section 11.5.

---

## See also
- Section 11.5 for the diagnostics that assess practical convergence
