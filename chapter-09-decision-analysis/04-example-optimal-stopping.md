# 9.4 — Example: Optimal Stopping

## What this section is doing

Gelman works through a sequential decision problem where the question is when to stop collecting data and act. The Bayesian framework naturally handles this through the expected value of information — comparing the expected utility gain from acting now versus waiting for one more observation.

---

## Simplification

You are deciding whether to launch a product. Each additional month of market testing gives you better information about demand, but delays revenue. The optimal stopping rule says: stop testing and launch when the expected value of another month of data is less than the cost of waiting.

---

## Financial application

**Sequential portfolio construction:** When to stop analyzing a potential investment and either execute or pass. Each additional week of due diligence improves the posterior over intrinsic value but has an opportunity cost.

**Earnings release trading:** Should you act on preliminary earnings signals or wait for the full report? The Bayesian framework computes the expected value of waiting for more information versus acting on current posterior uncertainty.

---

## See also
- Section 9.1 for the expected utility framework underlying the stopping rule
