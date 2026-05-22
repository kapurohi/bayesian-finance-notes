## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 7.1 — Predictive Accuracy | Log predictive density measures generalization | The platform evaluates models by how well they predict future quarters, not how well they fit historical data. Overfitting to earnings history produces confident but wrong DCF forecasts. |
| 7.2 — WAIC | Bayesian information criterion accounting for effective parameter count | Model selection between Normal, Student-t, and regime-switching growth models. Lower WAIC wins. No hypothesis tests required. |
| 7.3 — Cross-Validation | LOO-CV as gold standard for predictive accuracy estimation | For financial time series: leave-future-out CV correctly measures forecasting accuracy. PSIS-LOO via ArviZ makes this computationally feasible. |
| 7.4 — Model Expansion | Systematic model improvement in response to identified failures | The production model improvement cycle: check → identify failure → expand → check again. No model is final; all models are iteratively improved as more data arrives and new failure modes are identified. |

---

## Connection to Previous Chapters

Model comparison using WAIC and LOO-CV is the complement to model checking from Chapter 6. Chapter 6 identifies *what* is wrong; Chapter 7 identifies *which model is less wrong* and provides the framework for improving it. The two chapters together form the complete model validation and iteration cycle.

The model expansion strategies in Section 7.4 — Student-t likelihoods, hierarchical structure, regime-switching — connect directly to Chapter 5 (hierarchical), Chapter 17 (robust), and Chapter 22 (mixture models).