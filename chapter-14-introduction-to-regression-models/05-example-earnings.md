# 14.5 — Example: Earnings and Earnings Forecasts

## What this section is doing

Gelman works through a regression model of earnings on lagged earnings and analyst forecasts. The example demonstrates how Bayesian regression produces better-calibrated uncertainty estimates than OLS for this type of financial data.

---

## Key findings relevant to financial modeling

**Analyst forecasts are biased.** Historical data consistently shows that analyst earnings forecasts are optimistically biased. Encoding this as a prior on the analyst forecast coefficient produces more accurate earnings estimates than treating analyst forecasts as unbiased inputs.

**Uncertainty compounds.** The predictive uncertainty around an earnings estimate is larger than a frequentist model suggests, because the regression coefficients themselves are uncertain — especially with limited history. Bayesian regression captures this correctly.

**Prior shrinkage improves out-of-sample accuracy.** Ridge-style priors (Normal with mean zero) reduce overfitting for companies with short histories, producing better out-of-sample earnings predictions than OLS.

---

## See also
- Section 14.2 for the Bayesian regression model applied here
- Section 7.3 for leave-future-out cross-validation to validate earnings forecast accuracy
