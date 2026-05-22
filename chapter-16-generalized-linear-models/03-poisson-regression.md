# 16.3 — Poisson Regression

## What this section is doing

Poisson regression models count outcomes as a function of predictors. The expected count is modeled as an exponential function of the linear predictor, ensuring it is always positive.

---

## The model

$$y_i \mid \lambda_i \sim \text{Poisson}(\lambda_i)$$

$$\log(\lambda_i) = \alpha + \beta^T x_i$$

---

## Financial application

**Event frequency modeling:** Number of analyst downgrades per quarter as a function of earnings surprise and balance sheet stress. Number of covenant violations per year as a function of leverage and macro conditions. Number of trades per day as a function of volatility and spread.

**Overdispersion:** Real financial count data is often overdispersed — the variance exceeds the mean, violating the Poisson assumption. The negative binomial model (Poisson with a Gamma-distributed rate) handles overdispersion and should be used when the posterior predictive check reveals underdispersion in the simulated counts.
