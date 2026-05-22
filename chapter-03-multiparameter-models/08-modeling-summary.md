# 3.8 — Summary of Elementary Modeling and Computation

## What this section is doing

Gelman closes Chapter 3 with a recap of the modeling decisions covered across Chapters 2 and 3 — when to use which model, what the general workflow looks like, and what the limits of elementary models are. It is a consolidation section that also points toward the more advanced methods in the rest of the book.

---

## The general workflow

Every Bayesian model built so far follows the same sequence:

1. **Identify the unknown parameters** — what are you trying to estimate?
2. **Choose a likelihood** — what is the data-generating process?
3. **Choose a prior** — what do you know before seeing the data?
4. **Compute or sample the posterior** — analytically if conjugate, via MCMC otherwise
5. **Summarize and check** — credible intervals, probability statements, posterior predictive checks

This workflow does not change as models get more complex. The likelihood and prior get more sophisticated, but the five steps are invariant.

---

## Model selection guide from Chapters 2 and 3

| Data type | Unknown | Model |
|-----------|---------|-------|
| Count of successes / failures | Single probability $\theta$ | Beta-Binomial (Section 2.1) |
| Continuous measurements, known noise | Mean $\mu$ | Normal-Normal (Section 2.5) |
| Continuous measurements, unknown noise | Mean $\mu$ | Normal with t marginal (Section 3.2) |
| Continuous measurements, joint mean and variance | $\mu$ and $\sigma^2$ | Normal-Inverse-Gamma (Section 3.3) |
| Count of events per period | Rate $\lambda$ | Poisson-Gamma (Section 2.6) |
| Counts across multiple categories | Probability vector $\theta$ | Dirichlet-Multinomial (Section 3.4) |
| Multiple continuous outcomes, known covariance | Mean vector $\mu$ | Multivariate Normal-Normal (Section 3.5) |
| Multiple continuous outcomes, unknown covariance | $\mu$ and $\Sigma$ | Normal-Inverse-Wishart (Section 3.6) |
| Binary outcomes from regression | Coefficients $\alpha, \beta$ | Logistic regression with Normal prior (Section 3.7) |

---

## Where the limits are

The models in Chapters 2 and 3 are single-level — they estimate parameters directly from observed data. They do not share information across multiple units (multiple companies, multiple sectors) or model variation in parameters across groups.

That structure comes in Chapter 5 — hierarchical models. Hierarchical models are the direct extension of everything here: instead of estimating one growth rate for one company, you estimate growth rates for 50 companies simultaneously, sharing information across them through a common prior that is itself estimated from the data.

---

## See also

- Section 2.9 for the weakly informative prior recommendation that applies across all of these models
- Section 1.9 for the MCMC computational solution for non-conjugate models
- Chapters 11–12 for the full MCMC treatment
