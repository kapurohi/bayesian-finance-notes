# 18.3 — Bayesian Multiple Imputation

## What this section is doing

Multiple imputation fills in missing values by drawing from their posterior predictive distribution given the observed data, repeating this multiple times to produce a set of "completed" datasets. Analysis is run on each completed dataset and the results are combined.

---

## The procedure

1. Specify a model for the joint distribution of observed and missing data
2. Draw $M$ samples from $p(y_{\text{miss}} \mid y_{\text{obs}})$ — multiple imputations
3. Run the analysis on each of the $M$ completed datasets
4. Combine results using Rubin's rules: pool estimates and add between-imputation variance to within-imputation variance

---

## Financial application

**Balance sheet gap filling:** Quarterly financial statements sometimes have missing line items. Multiple imputation fills in missing values from the posterior predictive distribution conditional on all other available metrics and sector benchmarks.

**Panel data with gaps:** A coverage universe where different companies have data available for different time periods. Multiple imputation produces $M$ complete panels, the model is fit on each, and the results are combined — correctly propagating the uncertainty from the imputed values into the final estimates.
