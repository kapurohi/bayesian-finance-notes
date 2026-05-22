## What this section is doing

Gelman derives the **Widely Applicable Information Criterion (WAIC)** — a fully Bayesian information criterion that estimates out-of-sample predictive accuracy using the full posterior rather than a point estimate. WAIC replaces AIC and DIC for comparing Bayesian models.

---

## Simplification

AIC penalizes model complexity by subtracting 2 times the number of parameters from the log-likelihood. But in a Bayesian model, the "effective number of parameters" is not simply the count of parameters — it depends on how much the data actually constrains each one. A parameter that the data knows nothing about behaves like a free parameter. One that is tightly constrained by a strong prior barely counts.

WAIC computes the effective number of parameters directly from the posterior and uses it to produce a bias-corrected estimate of predictive accuracy.

---

## The formula

$$\text{WAIC} = -2\left(\text{lppd} - p_{\text{WAIC}}\right)$$

Where:
- $\text{lppd}$ is the log pointwise predictive density
- $p_{\text{WAIC}} = \sum_i \text{Var}_{\theta \mid y}(\log p(y_i \mid \theta))$ is the effective number of parameters

Lower WAIC indicates better out-of-sample predictive accuracy.

---

## Financial application

Comparing a Normal-Normal revenue growth model to a Student-t growth model for the same company: compute WAIC for both and choose the model with lower WAIC. No need for a hypothesis test — the information criterion directly estimates which model will predict future quarters more accurately.

---

## See also

- Section 7.3 for LOO-CV, which WAIC approximates
- Chapter 6 for posterior predictive checks that diagnose *why* a model is failing