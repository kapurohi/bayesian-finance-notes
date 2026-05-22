# 5.3 — Bayesian Analysis of Conjugate Hierarchical Models

## What this section is doing

Gelman derives the posterior for the simplest hierarchical model — a Normal-Normal hierarchy — and shows how the posterior updates both the company-level parameters and the population-level hyperparameters simultaneously. The key result is the **partial pooling estimate** — a weighted average of the company's own data mean and the population mean, with the weight determined by how variable companies are relative to how noisy the data is.

---

## The partial pooling estimate

For the Normal-Normal hierarchical model, the posterior mean for company $j$ is:

$$\hat{\theta}_j = \frac{\frac{1}{\tau^2}}{\frac{1}{\tau^2} + \frac{1}{\sigma^2/n_j}} \cdot \mu + \frac{\frac{1}{\sigma^2/n_j}}{\frac{1}{\tau^2} + \frac{1}{\sigma^2/n_j}} \cdot \bar{y}_j$$

This is a precision-weighted average of:
- The population mean $\mu$ — weighted by the between-company precision $1/\tau^2$
- The company's own data mean $\bar{y}_j$ — weighted by its data precision $n_j/\sigma^2$

**When $\tau$ is small** (companies are similar): the population mean gets more weight. Strong pooling.

**When $\tau$ is large** (companies are very different): the company's own data gets more weight. Weak pooling.

**When $n_j$ is small** (limited data): the population mean gets more weight regardless of $\tau$. The company borrows heavily from the sector.

**When $n_j$ is large** (long history): the company's own data dominates. It contributes to the sector estimate but is largely self-determined.

---

## Financial application

A newly listed company with 3 quarters of history and a sector of 30 comparable companies: the partial pooling estimate pulls the new company's growth rate significantly toward the sector mean. As quarters accumulate, the weight shifts gradually toward the company's own history.

This is the formal mechanism behind what practitioners do informally when they say "use sector medians for new companies and company-specific data for mature ones." The hierarchical model makes the transition automatic and quantitatively justified.

---

## See also

- Section 5.4 for the full worked model
- Section 2.2 for the single-company version of this precision-weighted average
