# 12.2 — Hamiltonian Monte Carlo

## What this section is doing

Gelman derives HMC — an MCMC algorithm that uses the gradient of the log-posterior to make large, efficient moves through the parameter space. Instead of random walks, HMC simulates the physics of a ball rolling on the (negative) posterior surface — using momentum to travel far before stopping to evaluate.

---

## The physics analogy

Augment the parameter space with a **momentum** variable $p$ (not probability — momentum in the physics sense). Define a **Hamiltonian**:

$$H(\theta, p) = -\log p(\theta \mid y) + \frac{1}{2}p^T M^{-1} p$$

The first term is potential energy (negative log-posterior). The second is kinetic energy. Simulate the dynamics of a particle rolling under this Hamiltonian for $L$ steps using leapfrog integration. The endpoint is the proposed next position.

Because Hamiltonian dynamics conserve energy, the acceptance probability of the proposed point is very high — often above 95%. The chain makes large moves and rarely wastes steps on rejected proposals.

---

## Advantages over random walk

- Moves proportional to $\sqrt{d}$ rather than $d^{-1/2}$ — vastly more efficient in high dimensions
- Exploits gradient information to move toward high-probability regions
- Avoids the random walk behavior that makes MH slow

---

## See also
- Section 12.3 for NUTS, which automatically tunes the trajectory length $L$
