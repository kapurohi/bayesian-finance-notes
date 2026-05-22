# 5.4 — Normal Model with Exchangeable Parameters

## What this section is doing

This is the flagship hierarchical model. Gelman works through the full Normal-Normal hierarchy — estimating both company-level growth rates and the sector-level hyperparameters simultaneously — with all details of the posterior derivation. This is the model you implement in production.

---

## The full model

**Level 1 — Observations:**

$$y_{ij} \mid \theta_j, \sigma^2 \sim \text{Normal}(\theta_j, \sigma^2)$$

Quarter $i$ for company $j$ is normally distributed around company $j$'s true growth rate.

**Level 2 — Company parameters:**

$$\theta_j \mid \mu, \tau^2 \sim \text{Normal}(\mu, \tau^2)$$

Each company's true growth rate is drawn from a sector-level Normal distribution.

**Hyperpriors:**

$$\mu \sim \text{Normal}(\mu_{\text{prior}}, \sigma_\mu^2), \qquad \tau \sim \text{HalfNormal}(\sigma_\tau)$$

Weakly informative priors on the sector mean and the between-company spread.

---

## The posterior structure

The joint posterior is:

$$p(\theta_1, \ldots, \theta_J, \mu, \tau \mid y) \propto p(\mu, \tau) \cdot \prod_{j=1}^J \left[p(\theta_j \mid \mu, \tau) \cdot \prod_i p(y_{ij} \mid \theta_j)\right]$$

This has no closed-form solution in general — MCMC is required. But the structure is clear: the company-level parameters $\theta_j$ are connected through the shared hyperparameters $\mu$ and $\tau$. Observing data from any company updates the hyperparameters, which in turn affects every other company's posterior.

---

## Shrinkage

The hierarchical model produces **shrinkage** — company estimates are pulled toward the population mean relative to their raw data means. Companies with extreme observed means get pulled back more than companies near the center.

This shrinkage is not a bug. It reflects the genuine information that extreme observations are more likely to be noisy outliers than truly extreme underlying values. It is the formal version of "regression to the mean."

In finance: a company that reports 40% growth in one quarter gets a posterior growth rate estimate well below 40%, because the hierarchical model correctly discounts that extreme observation in the context of a sector where 40% is unusual.

---

## See also

- Section 5.3 for the closed-form special case
- Section 5.5 for a complete worked example
- Chapter 15 for extending this to hierarchical regression
