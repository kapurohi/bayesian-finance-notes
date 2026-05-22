# Chapter 9 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 9.1 — Decision Theory | Expected utility maximization over the posterior | The formal bridge from posterior distributions to investment recommendations. Buy when the posterior-expected return exceeds the hurdle rate and the upside probability justifies the risk. |
| 9.2 — Utility Functions | Risk preferences encoded as utility functions | Different client mandates require different utility functions. The same posterior distribution produces different optimal decisions for a risk-neutral hedge fund and a risk-averse pension fund. |
| 9.3 — Unknown Utilities | Sensitivity analysis over utility parameters | Robustness testing: compute optimal actions across a range of utility functions to identify decisions that are good across all plausible client preferences. |
| 9.4 — Optimal Stopping | When to stop gathering information and act | The formal framework for sequential analysis decisions — when to stop due diligence, when to execute a trade, when additional data collection stops adding value relative to its cost. |

---

## Connection to Previous Chapters

Chapter 9 is the output layer of the entire framework. Chapters 1-8 build the posterior distribution. Chapter 9 converts that distribution into an action. The posterior predictive distribution from Chapter 1 Section 1.3 — $p(\tilde{y} \mid y)$ — is the direct input to the expected utility calculation: you integrate the utility of each future outcome weighted by its posterior predictive probability.
