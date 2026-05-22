# 4.4 — Frequency Evaluations of Bayesian Inferences

## What this section is doing

Gelman examines how Bayesian credible intervals perform from a frequentist perspective — across many repeated experiments. The key finding is that Bayesian credible intervals with noninformative or weakly informative priors have approximately correct frequentist coverage. This means Bayesian intervals are defensible not just philosophically but empirically.

---

## Simplification

A frequentist confidence interval is designed so that 95% of intervals constructed this way, across repeated experiments, contain the true parameter. A Bayesian 95% credible interval says there's a 95% posterior probability the true parameter is in this range.

They sound different. But in practice, for large samples and weakly informative priors, they produce nearly identical intervals. This section shows that the Bayesian interval achieves the correct frequentist coverage too — so you get both the philosophical clarity of the Bayesian statement and the empirical calibration of the frequentist guarantee.

---

## Financial application

When presenting Bayesian uncertainty estimates to clients or regulators who are accustomed to frequentist statistics, this result matters. A 95% credible interval around a default probability or a growth rate estimate is not just philosophically coherent — it is also approximately a 95% confidence interval in the frequentist sense, for large samples with weakly informative priors.

---

## See also

- Section 2.3 for how credible intervals are constructed
- Section 1.5 for the Bayesian interpretation of probability that distinguishes credible intervals from confidence intervals
