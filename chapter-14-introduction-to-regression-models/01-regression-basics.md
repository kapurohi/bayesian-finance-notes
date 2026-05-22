# 14.1 — Introduction to Regression Models

## What this section is doing

Gelman sets up the linear regression framework: a continuous outcome is modeled as a linear function of predictors plus Normal noise. The Bayesian version adds a prior over the regression coefficients, converting OLS into a proper probability model.

---

## The model

$$y_i = \alpha + \beta x_i + \epsilon_i, \qquad \epsilon_i \sim \text{Normal}(0, \sigma^2)$$

Equivalently:

$$y_i \mid \alpha, \beta, \sigma^2 \sim \text{Normal}(\alpha + \beta x_i, \sigma^2)$$

**Bayesian version adds priors:**

$$\alpha \sim \text{Normal}(0, \tau_\alpha^2), \qquad \beta \sim \text{Normal}(0, \tau_\beta^2), \qquad \sigma \sim \text{HalfNormal}(\sigma_0)$$

---

## Financial application

**Revenue-to-GDP regression:** Model quarterly revenue growth as a linear function of GDP growth. The Bayesian version produces:
- A posterior distribution over the GDP sensitivity coefficient $\beta$
- A posterior predictive distribution over next-quarter revenue given a GDP forecast
- Automatic regularization through the prior — preventing overfitting on limited data

---

## See also
- Section 4.5 for OLS as the flat-prior special case
- Chapter 15 for hierarchical regression
