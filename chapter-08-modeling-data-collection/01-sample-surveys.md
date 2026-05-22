# 8.1 — Sample Surveys and Poststratification

## What this section is doing

When data is collected from a non-random sample — certain companies, sectors, or time periods are over- or under-represented — naive estimates will be biased. Poststratification reweights estimates to match the population of interest.

---

## Simplification

If your training data for a default probability model has 80% large-cap companies and the portfolio you're scoring is 60% mid-cap, your model is calibrated for the wrong population. Poststratification reweights the estimates to match the actual portfolio composition.

---

## Financial application

**Backtest dataset bias:** Financial backtests often suffer from survivorship bias — only companies that survived appear in the historical dataset. Models trained on this data underestimate default rates and tail risks.

**Coverage universe mismatch:** A model trained on US large-cap earnings data applied to emerging market small-caps requires poststratification or recalibration.

The Bayesian version of poststratification uses the posterior to propagate uncertainty through the reweighting step — so the uncertainty in the final estimate correctly reflects both the model uncertainty and the reweighting uncertainty.

---

## See also
- Section 8.4 for censoring — a related data collection issue
