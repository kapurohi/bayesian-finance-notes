# 4.3 — Counterexamples to the Asymptotic Theory

## What this section is doing

Gelman presents cases where the large-sample Normal approximation fails — where posteriors don't converge normally, or converge to the wrong place. Understanding these failure modes is important for knowing when you need exact posterior computation rather than approximations.

---

## When large-sample theory breaks down

**1. Unidentified parameters**

If two different parameter values produce the same likelihood for all possible data — the model is unidentified — the posterior never concentrates. You can collect infinite data and still not distinguish between the two values.

In finance: a factor model where two factors are perfectly collinear. Adding more data doesn't help identify the separate factor loadings.

**2. The number of parameters grows with the data**

If you add more parameters as you collect more data — for example, adding a new fixed effect for each new company in a panel — the asymptotic results fail. Each parameter is estimated from a fixed (small) number of observations regardless of how large $n$ grows overall.

In finance: a model that estimates a separate intercept for every company in a coverage universe, with only a few quarters of data per company. The parameters don't concentrate because the per-company sample size stays small.

**3. Heavy-tailed likelihoods**

If the likelihood has very heavy tails — the Cauchy distribution is the standard example — the MLE and the posterior mean can both be poorly behaved, and the Normal approximation fails.

In finance: modeling extreme tail events like financial crises requires likelihoods with heavier tails than Normal. Student-t or stable distributions are more appropriate, and their posteriors are not well-approximated by the Normal asymptotic.

---

## See also

- Section 4.2 for the positive results that these counterexamples bound
- Section 17.1 for robust models that handle heavy-tailed data correctly
