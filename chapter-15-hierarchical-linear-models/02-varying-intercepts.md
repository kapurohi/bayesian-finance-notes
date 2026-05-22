# 15.2 — Varying Intercept Models

## What this section is doing

The simplest hierarchical regression has a common slope but a company-specific intercept. Each company has its own baseline level, but all companies respond to predictors with the same coefficient. This is the **random effects model** in classical statistics.

---

## The model

$$y_{ij} = \alpha_j + \beta x_{ij} + \epsilon_{ij}$$

$$\alpha_j \sim \text{Normal}(\mu_\alpha, \tau_\alpha^2)$$

One slope $\beta$ shared across all companies. Each company has its own intercept $\alpha_j$ drawn from a Normal distribution with population mean $\mu_\alpha$ and variance $\tau_\alpha^2$.

---

## Financial application

A panel earnings regression where each company has a different base earnings level but a common response to macro factors. The varying intercept captures company-specific fixed characteristics (business model, competitive position) while the common slope captures the universal macro sensitivity.

---

## See also
- Section 15.3 for varying slopes — different macro sensitivities per company
