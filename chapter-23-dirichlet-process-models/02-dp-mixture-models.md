# 23.2 — Dirichlet Process Mixture Models

## What this section is doing

A DP mixture model uses a Dirichlet process as the prior over the mixing distribution. Each observation belongs to a cluster, and cluster membership can grow with the data. The posterior distribution over clusterings informs about the number and nature of subpopulations.

---

## The model

$$y_i \mid \theta_i \sim p(y_i \mid \theta_i)$$

$$\theta_i \mid G \sim G$$

$$G \sim \text{DP}(\alpha, G_0)$$

Where $G_0$ is the base distribution (the "average" cluster structure) and $\alpha$ controls the concentration.

---

## Financial application

**Nonparametric return clustering:** Fit a DP Gaussian mixture to equity returns. The posterior distribution over cluster assignments reveals the natural groupings in the data — without specifying in advance whether there are 2 regimes, 3, or 5. The posterior over the number of clusters quantifies uncertainty about the market structure.
