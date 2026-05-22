# 11.5 — Inference and Monitoring Convergence

## What this section is doing

Gelman covers the practical tools for assessing whether MCMC chains have converged — the most important being the $\hat{R}$ (R-hat) statistic introduced in Section 1.9 and effective sample size (ESS).

---

## $\hat{R}$ — The convergence diagnostic

Run multiple chains starting from different random initial values. $\hat{R}$ compares variance within chains to variance across chains:

$$\hat{R} = \sqrt{\frac{\hat{V}}{W}}$$

Where $\hat{V}$ is the pooled variance estimator and $W$ is the within-chain variance. If all chains have converged to the same distribution, $\hat{R} \approx 1$.

**Rule:** $\hat{R} < 1.01$ for all parameters before trusting any output.

---

## Effective Sample Size (ESS)

MCMC samples are correlated — adjacent samples are similar because the chain moves gradually. The **effective sample size** is the number of independent samples that would give the same precision as the $S$ correlated MCMC samples:

$$\text{ESS} = \frac{S}{1 + 2\sum_{k=1}^\infty \rho_k}$$

Where $\rho_k$ is the autocorrelation at lag $k$. Low ESS relative to total samples indicates high autocorrelation and poor mixing — the chain is moving slowly through the parameter space.

**Rule:** ESS greater than 400 for stable posterior summaries. ESS greater than 1000 for accurate tail quantiles.

---

## Financial application

After fitting any production model, always check:
- $\hat{R} < 1.01$ for every parameter
- ESS greater than 400 for every parameter
- Trace plots show the chains mixing freely (no stuck regions, no trends)

ArviZ implements all of these: `az.summary(trace)` reports both $\hat{R}$ and ESS for every parameter.

---

## See also
- Section 1.9 for the first introduction of $\hat{R}$
- Chapter 12 for sampling algorithms that produce better ESS per compute step
