# 15.1 — Regression with Hierarchical Priors

## What this section is doing

Gelman combines the regression framework from Chapter 14 with the hierarchical structure from Chapter 5. Each group (company, sector, country) has its own regression coefficients, and those coefficients are drawn from a common population distribution whose parameters are estimated from the data.

---

## Simplification

You want to model how each company's revenue responds to GDP growth. Every company has its own GDP sensitivity. But you don't estimate each sensitivity from that company's data alone — you use a hierarchical model where all sensitivities are drawn from a sector-level distribution.

Companies with limited history get their sensitivity estimate pulled toward the sector average. Companies with long histories are mostly self-determining. The sector distribution is estimated from all companies simultaneously.

---

## The model

**Level 1 — Company-specific regression:**

$$y_{ij} = \alpha_j + \beta_j x_{ij} + \epsilon_{ij}$$

**Level 2 — Population distribution over coefficients:**

$$\begin{pmatrix}\alpha_j \\ \beta_j\end{pmatrix} \sim \text{Normal}(\mu_{\alpha\beta}, \Sigma)$$

The population covariance $\Sigma$ captures whether companies with high baseline growth tend to have higher or lower GDP sensitivity.

---

## Financial application

A macro sensitivity model for a coverage universe of 50 companies across 5 sectors: each company gets its own intercept and GDP coefficient, but both are drawn from a sector-level bivariate Normal distribution. Companies with only 4 quarters of history get sector-average sensitivities. Companies with 40 quarters mostly determine their own estimates.

---

## See also
- Chapter 5 for the scalar hierarchical model this extends
- Section 15.2 for the simpler varying-intercepts-only model
