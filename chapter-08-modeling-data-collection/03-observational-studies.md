# 8.3 — Observational Studies

## What this section is doing

Most financial data is observational — companies make their own decisions about capital structure, investment, and reporting. Causal inference from observational data requires assumptions about the assignment mechanism. This section covers how to encode those assumptions in a Bayesian model.

---

## Simplification

You observe that companies with higher R&D spending have higher revenue growth. Is R&D causing the growth, or are high-growth companies choosing to invest more in R&D? Observational data alone cannot distinguish these without additional structure.

---

## Financial application

**Factor model causation:** Identifying whether a factor drives returns or simply correlates with the true driver requires assumptions about the data-generating process. Bayesian causal models encode these assumptions explicitly as priors over the causal structure.

**Counterfactual DCF analysis:** What would this company's revenue have been without the 2020 acquisition? Bayesian causal models can estimate counterfactuals with proper uncertainty — rather than a single deterministic adjustment.

---

## See also
- Chapter 14 for regression models that underlie causal analyses
