# 8.2 — Designed Experiments

## What this section is doing

When data comes from a controlled experiment — a randomized A/B test, a controlled pricing trial — the data collection design simplifies inference because treatment assignment is independent of potential outcomes. This section covers how to analyze experimental data within the Bayesian framework.

---

## Financial application

**A/B testing in fintech:** A pricing test for a lending product randomly assigns customers to different rate structures. The Bayesian analysis of the experiment produces posterior distributions over the treatment effect — the difference in conversion rates or default rates between rate structures.

The key advantage of Bayesian A/B testing over frequentist testing: you can compute the probability that Treatment A is better than Treatment B directly from the posterior, stop the test early when sufficient evidence accumulates, and incorporate prior information from previous tests.

---

## See also
- Section 2.1 for the Beta-Binomial model that underlies most A/B test analyses
