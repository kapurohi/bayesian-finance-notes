# 16.2 — Logistic Regression

## What this section is doing

Logistic regression is the GLM for binary outcomes. The probability of a positive outcome is modeled as a logistic function of the linear predictor. This is the Bayesian treatment — adding priors on the coefficients, producing posterior distributions over probabilities rather than point estimates.

---

## The model

$$y_i \mid \theta_i \sim \text{Bernoulli}(\theta_i)$$

$$\text{logit}(\theta_i) = \log\frac{\theta_i}{1-\theta_i} = \alpha + \beta^T x_i$$

**Bayesian version:**

$$\alpha \sim \text{Normal}(0, 2.5), \qquad \beta_k \sim \text{Normal}(0, 2.5)$$

The prior $\text{Normal}(0, 2.5)$ on the log-odds scale is weakly informative — it corresponds to a roughly uniform prior on the probability scale for moderate predictor values.

---

## Financial application

**Credit scoring:** The probability of default as a function of leverage, interest coverage, cash flow, and sector. The Bayesian posterior over each coefficient gives the probability that each ratio is a genuine predictor of default — not just whether it is "statistically significant."

**Posterior probability of default:** For a specific borrower with predictors $x_*$, the posterior predictive probability of default is:

$$p(y^* = 1 \mid x^*, y) = \int \sigma(\alpha + \beta^T x^*) \cdot p(\alpha, \beta \mid y) \, d\alpha \, d\beta$$

This averages over coefficient uncertainty — producing a wider probability interval than a point-estimate logistic regression.
