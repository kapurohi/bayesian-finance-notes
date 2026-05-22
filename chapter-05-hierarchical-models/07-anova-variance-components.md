# 5.7 — Analysis of Variance and the Variance Components Model

## What this section is doing

Gelman connects hierarchical models to classical ANOVA (Analysis of Variance). The variance components model decomposes total variation in data into within-group variation and between-group variation. In a Bayesian context, this decomposition is estimated probabilistically rather than as a fixed split — and the uncertainty about the split is captured in the posterior over $\tau$ (between-group standard deviation).

---

## Simplification

Total variation in quarterly earnings across a sector has two sources: variation within each company over time (some quarters are just better than others), and variation between companies (some companies are genuinely higher-growth than others).

The variance components model estimates both simultaneously. The within-company variation is $\sigma^2$. The between-company variation is $\tau^2$. Their ratio tells you how much of the total signal in the data is company-specific versus sector-wide.

---

## The intraclass correlation

The **intraclass correlation coefficient (ICC)** is:

$$\rho = \frac{\tau^2}{\tau^2 + \sigma^2}$$

$\rho$ measures the fraction of total variance that is attributable to between-company differences.

- $\rho$ close to 1: companies are very different from each other — each should be estimated mostly from its own data. Minimal pooling is appropriate.
- $\rho$ close to 0: within-company noise dominates — all companies look similar. Strong pooling is appropriate.

---

## Financial application

Estimating $\rho$ for a sector tells you how much a new company's estimate should borrow from the sector versus rely on its own data. A sector with $\rho = 0.8$ has highly heterogeneous companies — a new entrant's estimate should stay close to its own data quickly. A sector with $\rho = 0.2$ has homogeneous companies — a new entrant should rely heavily on the sector average for many quarters before its own data dominates.

---

## See also

- Section 5.3 for the partial pooling formula where $\tau$ and $\sigma$ appear explicitly
- Section 5.4 for the full hierarchical Normal model

