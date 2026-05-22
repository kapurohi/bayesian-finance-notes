# 13.2 — Laplace Approximation for Hierarchical Models

## What this section is doing

Applying Laplace approximation to hierarchical models requires marginalizing over the group-level parameters. Gelman shows how to combine Laplace approximation at the individual level with a more accurate integration at the population level.

---

## Financial application

For a hierarchical model with 100 companies: use Laplace approximation for each company's individual parameters (fast) while integrating the hyperparameters more accurately. This hybrid approach is significantly faster than full MCMC while maintaining reasonable accuracy for the population-level estimates.

---

## See also
- Chapter 5 for hierarchical models this approximation is applied to
