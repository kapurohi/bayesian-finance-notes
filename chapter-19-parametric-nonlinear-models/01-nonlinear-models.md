# 19.1 — Nonlinear Regression

## What this section is doing

Gelman covers regression where the mean function is nonlinear in the parameters. Unlike linear regression where the predictors appear linearly, nonlinear regression requires specifying the functional form explicitly.

---

## The model

$$y_i = f(x_i, \theta) + \epsilon_i, \qquad \epsilon_i \sim \text{Normal}(0, \sigma^2)$$

Where $f$ is a known nonlinear function and $\theta$ are the parameters to be estimated. The Bayesian version adds priors on $\theta$.

MCMC handles nonlinear models naturally — you only need to evaluate $f(x_i, \theta)$ at each MCMC step. No linearity assumption is required.

---

## Financial application

**Exponential growth model:**

$$y_t = A \cdot e^{\beta t} + \epsilon_t$$

Revenue modeled as exponential growth with parameters $A$ (initial level) and $\beta$ (growth rate). The Bayesian posterior over $\beta$ gives a distribution over the compound annual growth rate — not a point estimate.

**S-curve adoption model:**

$$y_t = \frac{K}{1 + e^{-r(t-t_0)}}$$

Technology adoption or market penetration modeled as a logistic growth curve with carrying capacity $K$, growth rate $r$, and inflection point $t_0$. All three parameters are estimated with posterior uncertainty.
