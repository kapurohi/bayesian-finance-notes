# 5.6 — Hierarchical Modeling Applied to Regression

## What this section is doing

Gelman extends the hierarchical framework from estimating scalar parameters to estimating regression coefficients. Instead of each unit having its own mean, each unit has its own set of regression coefficients — and those coefficients are drawn from a common population distribution. This is the framework for building multi-company financial models where each company has its own response to common drivers.

---

## The model

**Level 1 — Company-specific regression:**

$$y_{ij} = \alpha_j + \beta_j x_{ij} + \epsilon_{ij}, \qquad \epsilon_{ij} \sim \text{Normal}(0, \sigma^2)$$

Each company $j$ has its own intercept $\alpha_j$ and slope $\beta_j$.

**Level 2 — Population distribution over coefficients:**

$$\begin{pmatrix} \alpha_j \\ \beta_j \end{pmatrix} \sim \text{Normal}\!\left(\begin{pmatrix} \mu_\alpha \\ \mu_\beta \end{pmatrix}, \Sigma\right)$$

All companies' coefficients are drawn from a joint Normal distribution with population mean vector and covariance matrix $\Sigma$.

---

## Financial application

A revenue forecasting model where revenue growth depends on GDP growth. Each company has its own sensitivity to GDP — some are cyclical, some are defensive — but all sensitivities are drawn from a sector-level distribution.

Companies with limited earnings history get GDP sensitivity estimates pulled toward the sector-average sensitivity. Companies with long histories are mostly self-determined. The sector-level covariance $\Sigma$ captures whether high-GDP-sensitivity companies also tend to have higher baseline growth rates.

---

## See also

- Section 5.4 for the simpler scalar hierarchical model
- Chapter 15 for the full hierarchical linear model treatment
