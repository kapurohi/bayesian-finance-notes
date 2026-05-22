# 3.7 — Example: Analysis of a Bioassay Experiment

## What this section is doing

Gelman works through a non-conjugate model — a logistic regression applied to dose-response data — to show what happens when the posterior has no closed-form solution. This is the bridge to MCMC. The bioassay example introduces the general pattern of building models where you specify the likelihood and prior, accept that the posterior cannot be computed analytically, and rely on numerical methods to explore it.

---

## Simplification

A pharmaceutical company is testing a drug at different doses and measuring how many subjects respond. They want to estimate the dose-response curve — how the probability of a response changes with dose. This is a regression problem where the unknown parameters are the intercept and slope of a logistic curve.

The logistic regression likelihood combined with a Normal prior on the coefficients does not produce a conjugate posterior. There is no clean formula for $p(\alpha, \beta \mid y)$. You have to sample it numerically.

This is the normal state of affairs for most real models. Conjugate models are the exception. MCMC is the general solution.

---

## The model

**Likelihood — Binomial with logistic link:**

$$p(y_i \mid \alpha, \beta) = \text{Binomial}\!\left(n_i, \, \text{logit}^{-1}(\alpha + \beta x_i)\right)$$

Where $x_i$ is the log-dose at experiment $i$, $y_i$ is the number of responses, and $\text{logit}^{-1}(u) = 1/(1 + e^{-u})$ converts a linear predictor into a probability.

**Prior:**

$$\alpha \sim \text{Normal}(0, 4), \qquad \beta \sim \text{Normal}(0, 4)$$

Weakly informative — consistent with Section 2.9.

**Posterior:** No closed form. Gelman uses a grid approximation in the text. In practice this is a job for PyMC.

---

## Financial translation

The bioassay structure maps directly to any financial model where a probability depends on a continuous predictor:

- **Credit scoring:** probability of default as a function of leverage, coverage ratio, and sector — logistic regression with Bayesian priors on coefficients
- **Earnings surprise model:** probability of a positive earnings surprise as a function of analyst consensus revision, short interest, and momentum
- **Deal close probability:** probability a transaction closes as a function of deal size, buyer type, and market conditions

In all of these, the likelihood is Binomial (or Bernoulli) with a logistic link, the parameters are regression coefficients, and the posterior has no closed form. This is exactly the bioassay structure — and the solution is exactly the same: sample the posterior with MCMC.

---

## The key insight

This section is Gelman demonstrating that once you leave the conjugate world, the modeling workflow does not change — you still write down a prior and a likelihood — but the computation changes. You can no longer solve for the posterior analytically. MCMC (Chapters 11–12) handles it.

For the platform, this means the Beta-Binomial and Normal-Normal models from Chapter 2 can be extended to richer, more realistic specifications — logistic regression for default probability, hierarchical structures for multi-company estimation — without changing the fundamental Bayesian architecture.

---

## See also

- Section 2.1 for the conjugate Binomial model this extends
- Section 2.9 for the weakly informative prior choices used here
- Section 1.9 for the introduction to MCMC as the computational solution
