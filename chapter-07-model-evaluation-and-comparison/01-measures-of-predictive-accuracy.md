## What this section is doing

Gelman introduces formal measures of how well a model predicts new data. The gold standard is **log predictive density** — how much probability the model assigns to the data it was not trained on. Higher is better.

---

## Simplification

You want to know if your revenue growth model is actually good, not just well-fit. A model that memorizes training data but predicts future quarters poorly is not useful. The measures in this section evaluate how well the model generalizes to new data.

---

## Key measures

**Log pointwise predictive density (lppd):**

$$\text{lppd} = \sum_{i=1}^n \log p(y_i \mid y_{-i})$$

The sum of log predictive densities for each observation, evaluated using the posterior fit to all other observations. Higher values indicate better predictive accuracy.

**Expected log predictive density (elpd):**

The expected lppd over new data drawn from the true data-generating distribution. This is what we want to maximize — predictive accuracy on genuinely new data.

---

## Financial application

A model that fits historical growth data well but assigns low probability to out-of-sample quarters is overfit. Predictive accuracy measures evaluate generalization, not just fit. This is particularly important for DCF models where the goal is forecasting future cash flows, not explaining historical ones.

---

## See also

- Section 7.2 for information criteria that approximate elpd
- Section 7.3 for cross-validation approaches