# 23.1 — The Dirichlet Process

## What this section is doing

Gelman introduces the Dirichlet process — a probability distribution over probability distributions. Drawing from a DP produces a random discrete distribution (almost surely). This is the prior used in DP mixture models.

---

## Simplification

A finite mixture model requires you to decide in advance how many groups exist — is it 2 regimes or 3? The Dirichlet process removes this constraint. You specify a concentration parameter $\alpha$ that controls how quickly new groups form. The model estimates how many distinct groups the data is consistent with, rather than requiring you to specify it.

---

## The Chinese restaurant process

An intuitive representation: customers (observations) enter a restaurant and sit at tables (clusters). The first customer sits alone. Each subsequent customer either:
- Joins an existing table with probability proportional to the number of customers already there
- Starts a new table with probability proportional to $\alpha$

Large $\alpha$: many small tables — many distinct clusters.
Small $\alpha$: a few large tables — a few dominant clusters.

---

## Financial application

**Unknown number of credit risk segments:** In a large portfolio, you don't know how many distinct risk subpopulations exist. A DP mixture estimates the number of segments from the data — it might find 3 or it might find 8, depending on the heterogeneity in the portfolio.
