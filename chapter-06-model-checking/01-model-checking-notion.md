# 6.1 — The Notion of Model Checking

## What this section is doing

Gelman establishes what it means to check a model. A Bayesian model is a joint probability distribution over data and parameters. Model checking asks: is this distribution a plausible description of how the data was actually generated? If the model is badly wrong, the posterior summaries it produces cannot be trusted regardless of how elegantly the math works out.

---

## Simplification

Building a model is like building a map. A map is useful if it represents the terrain well enough for the purpose at hand. But if the map shows roads that don't exist and misses ones that do, the directions it gives you are wrong — no matter how beautifully it was drawn.

Model checking is how you test whether your map matches the territory. You use the model to predict what data should look like, then compare those predictions to the data you actually have.

---

## Two types of model failure

**Misspecified likelihood:** The assumed data-generating distribution doesn't match reality. For example, assuming Normal errors when the actual errors are heavy-tailed.

**Misspecified prior:** The prior places probability mass in regions that are inconsistent with the data. For example, a prior on growth rates that allows negative values that are economically impossible in the specific context.

Both types of failure produce posteriors that do not correctly reflect the uncertainty about the true parameters.

---

## See also

- Section 6.3 for the formal posterior predictive check procedure
- Section 1.10 for why posterior predictive checks are a key advantage of Bayesian methods
