## What this section is doing

Gelman covers leave-one-out cross-validation (LOO-CV) as the gold standard for Bayesian model comparison. LOO-CV directly estimates out-of-sample predictive accuracy by iteratively holding out one observation, fitting the model on the rest, and evaluating the held-out prediction.

---

## Simplification

You have 20 quarters of revenue data. To estimate how well your model predicts new data, hold out Q1 2022, fit the model on the other 19 quarters, and record how much probability the fitted model assigns to Q1 2022. Repeat for every quarter. The sum of those log-probabilities is the LOO estimate of predictive accuracy.

---

## Pareto-Smoothed Importance Sampling (PSIS-LOO)

Full LOO-CV requires fitting the model $n$ times. For large datasets this is computationally expensive. **PSIS-LOO** approximates this using a single posterior fit and importance weights — it is exact when the approximation is accurate, and it flags when the approximation breaks down (via high Pareto-$k$ diagnostic values).

ArviZ implements PSIS-LOO directly: `az.loo(trace)`.

---

## Financial application

For time-series financial data, standard LOO-CV can be misleading because observations are temporally correlated — a model that knows Q1 and Q3 effectively knows Q2. Use **leave-future-out cross-validation** instead: train on all quarters before $t$, predict quarter $t$, repeat across all $t$. This correctly evaluates forecasting accuracy rather than interpolation accuracy.

---

## See also

- Section 7.2 for WAIC, which approximates LOO-CV
- Section 7.4 for model expansion when comparison reveals a gap