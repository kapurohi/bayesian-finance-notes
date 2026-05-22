# 16.1 — The GLM Framework

## What this section is doing

Gelman introduces the three components of a GLM: the distribution family (Normal, Binomial, Poisson), the linear predictor ($X\beta$), and the link function that connects them. The link function transforms the linear predictor to the scale of the outcome's mean.

---

## The three components

**Distribution:** The likelihood for the outcome $y$. For binary outcomes: Binomial. For counts: Poisson. For positive continuous: Gamma.

**Linear predictor:** $\eta_i = \alpha + \beta_1 x_{i1} + \cdots + \beta_K x_{iK}$

**Link function:** $g(\mu_i) = \eta_i$ — maps the mean $\mu_i$ to the linear predictor. For Binomial: logit. For Poisson: log. For Normal: identity.

---

## Financial application

The GLM framework covers almost every classification and count model used in finance:
- Binary default/no-default: Binomial + logit link
- Transaction count fraud model: Poisson + log link
- Loss given default: Gamma + log link
- Recovery rate: Beta regression

All of these fit within the same Bayesian GLM framework with prior distributions on the coefficients.
