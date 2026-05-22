# 10.2 — Posterior Simulation and Summarization

## What this section is doing

Gelman covers how to use posterior samples — however they were obtained — to compute any quantity of interest. The key insight is that posterior simulation is a general-purpose tool: once you have samples from the posterior, you can estimate any function of the parameters by simply applying that function to each sample and averaging.

---

## The simulation-based workflow

Given $S$ posterior samples $\theta^{(1)}, \ldots, \theta^{(S)}$:

**Posterior mean:** $\frac{1}{S}\sum_s \theta^{(s)}$

**Posterior variance:** $\frac{1}{S-1}\sum_s (\theta^{(s)} - \bar{\theta})^2$

**Any quantile:** Sort the samples and read off the quantile directly.

**Any nonlinear function:** $\frac{1}{S}\sum_s f(\theta^{(s)})$ for any function $f$

---

## Financial application

DCF intrinsic value is a nonlinear function of growth rate, margin, and WACC. Given posterior samples of all three parameters, the posterior distribution over intrinsic value is just the collection of DCF outputs computed at each sample — no additional work required. This is how joint parameter uncertainty flows into output uncertainty automatically.

---

## See also
- Section 1.9 for the introduction to MCMC sampling
- Chapter 11 for the mechanics of obtaining the samples
