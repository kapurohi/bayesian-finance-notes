# Chapter 6 — Model Checking

Before trusting any model output, you need to know whether the model is a good description of reality. This chapter covers the tools for diagnosing whether a Bayesian model is correctly specified — whether the likelihood and prior are appropriate for the data at hand.

The core tool is the **posterior predictive check**: simulate data from the fitted model and compare it to the actual observed data. If the simulated data looks systematically different from the real data, something is wrong with the model.

---

## Sections

| # | File | One-Line Summary |
|---|------|-----------------|
| 6.1 | [The Notion of Model Checking](./01-model-checking-notion.md) | Why model checking matters and what it means for a model to fit |
| 6.2 | [Do the Inferences Make Sense?](./02-inferences-make-sense.md) | Qualitative checks — do the posterior estimates look reasonable? |
| 6.3 | [Posterior Predictive Checking](./03-posterior-predictive-checking.md) | The main quantitative tool — simulate from the model and compare to data |
| 6.4 | [Graphical Posterior Predictive Checks](./04-graphical-checks.md) | Visual diagnostics for model misspecification |
| 6.5 | [Model Checking for the Educational Testing Example](./05-educational-testing.md) | Full worked example of posterior predictive checking |

---

## End of Chapter

- [Financial Utility Summary](./financial-utility-summary.md)
