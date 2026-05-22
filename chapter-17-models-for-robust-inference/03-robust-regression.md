# 17.3 — Robust Regression

## What this section is doing

Replacing the Normal error distribution in regression with a Student-t produces **robust regression** — regression that is not dominated by a small number of extreme residuals. The coefficient estimates are less sensitive to outlying data points.

---

## Financial application

A factor regression with Student-t errors is more stable than OLS when a few quarters have extreme outcomes — crisis quarters, acquisition-driven spikes, regulatory charges. The robust regression down-weights those extreme residuals automatically without requiring manual outlier removal.

The posterior predictive check from Chapter 6 will flag whether the Normal or Student-t likelihood is more appropriate: if the Normal model's simulated data never produces the large residuals observed in the actual data, switch to Student-t.
