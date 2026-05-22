# 17.1 — Modeling Outliers with a Contamination Mixture

## What this section is doing

Gelman models outliers explicitly as a mixture: most observations come from the main distribution, but a small fraction come from a contaminating distribution with much larger variance. This "contamination mixture" is more interpretable than the Student-t because it explicitly represents the outlier-generating process.

---

## The model

$$y_i \sim (1-\epsilon) \cdot \text{Normal}(\mu, \sigma^2) + \epsilon \cdot \text{Normal}(\mu, k^2\sigma^2)$$

Where $\epsilon$ is the contamination fraction (typically small, 1-5%) and $k$ is the outlier scale multiplier (typically large, 5-10).

---

## Financial application

Quarterly earnings often have two modes: normal operating quarters and quarters with extraordinary items (write-downs, one-time charges, restructuring costs). The contamination mixture model explicitly separates these — the main Normal captures normal quarters, the contaminating Normal captures the extraordinary-item quarters. The posterior over $\epsilon$ estimates how often extraordinary items occur for this specific company.
