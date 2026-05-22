# 22.1 — Finite Mixture Models

## What this section is doing

A finite mixture model represents the overall distribution as a weighted sum of $K$ component distributions. Each observation belongs to one component — but which one is unknown and is modeled as a latent variable.

---

## The model

$$p(y_i \mid \theta, \pi) = \sum_{k=1}^K \pi_k \cdot p(y_i \mid \theta_k)$$

Where:
- $\pi_k$ are the mixture weights (they sum to 1)
- $\theta_k$ are the component-specific parameters
- The latent variable $z_i \in \{1, \ldots, K\}$ indicates which component observation $i$ comes from

**Prior on weights:** Dirichlet($\alpha, \ldots, \alpha$)

---

## Financial application

**Return distribution modeling:** Equity returns may be drawn from a mixture of Normal distributions — a low-volatility normal-market component and a high-volatility crisis component. The mixture model estimates both components and their weights simultaneously. The posterior over $\pi_k$ gives the probability of being in each regime at any given time.

**Credit quality segmentation:** A portfolio of borrowers may contain subpopulations with genuinely different default processes — prime and subprime, for example. A mixture model identifies these subpopulations from the data without requiring external labels.
