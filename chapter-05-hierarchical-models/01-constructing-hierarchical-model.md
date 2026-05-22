# 5.1 — Constructing a Hierarchical Model

## What this section is doing

Gelman introduces the two-level hierarchical structure. At the bottom level, each unit (company, patient, school) has its own parameter. At the top level, all those parameters are drawn from a common population distribution — whose parameters are themselves estimated from the data. This top-level distribution is what enables information sharing across units.

---

## Simplification

Imagine you're estimating revenue growth rates for 50 technology companies. You could estimate each company's growth rate separately — using only that company's own earnings history. Or you could assume all companies have the same growth rate — using every company's data for every estimate.

Both extremes are wrong. The first ignores the fact that tech companies in the same sector are similar. The second ignores the fact that each company is genuinely different.

Hierarchical models find the middle ground. Each company has its own growth rate. But all growth rates are drawn from a common sector-level distribution. Companies with limited data get pulled toward the sector average. Companies with long histories stay close to their own estimates. The model figures out how much pooling is appropriate from the data itself.

This middle ground is called **partial pooling**.

---

## The two-level structure

**Level 1 — Company-specific parameters:**

$$y_{ij} \mid \theta_j \sim p(y_{ij} \mid \theta_j)$$

Each observation $y_{ij}$ (quarter $i$ for company $j$) is drawn from a distribution parameterized by that company's own parameter $\theta_j$.

**Level 2 — Population distribution:**

$$\theta_j \mid \mu, \tau \sim \text{Normal}(\mu, \tau^2)$$

Each company's parameter $\theta_j$ is itself drawn from a Normal population distribution with mean $\mu$ and standard deviation $\tau$. These **hyperparameters** $\mu$ and $\tau$ are estimated from the full dataset.

**Hyperprior:**

$$\mu \sim p(\mu), \qquad \tau \sim p(\tau)$$

Weakly informative priors on the hyperparameters complete the model.

---

## The three quantities to interpret

| Quantity | Meaning | Estimated from |
|----------|---------|----------------|
| $\theta_j$ | Company $j$'s true growth rate | Company $j$'s data + sector information |
| $\mu$ | Sector-average growth rate | All companies' data jointly |
| $\tau$ | Between-company variation | How different companies are from each other |

$\tau$ is the most important hyperparameter. If $\tau$ is small, companies are similar and strong pooling is appropriate. If $\tau$ is large, companies are very different from each other and each should be estimated largely from its own data.

---

## See also

- Section 5.2 for the exchangeability assumption that justifies this structure
- Section 5.4 for the full worked model with Normal observations
- Section 1.6 for the informal version of this idea introduced in Chapter 1
