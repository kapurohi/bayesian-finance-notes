# Chapter 6 — Financial Utility Summary

---

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 6.1 — Model Checking Notion | A model must be tested against reality before its outputs are trusted | Every production model on the platform requires a formal checking step before output is served. A well-computed posterior from a misspecified model is worse than useless — it is confidently wrong. |
| 6.2 — Qualitative Checks | Look at posterior summaries and ask whether they make sense | First-pass validation for every new model or new company added to coverage. Implausible estimates signal data or prior problems before formal diagnostics are needed. |
| 6.3 — Posterior Predictive Checking | Simulate data from the fitted model and compare to actual data | The formal validation protocol. Test statistics: mean, variance, skewness, tail behavior, autocorrelation. Posterior predictive p-values near 0 or 1 flag model failures. |
| 6.4 — Graphical Checks | Visual comparison of simulated vs observed data distributions | Standard diagnostic plots: density overlay, histogram comparison, tail plots. Visual checks catch systematic misspecification — especially tail failures — that summary statistics miss. |
| 6.5 — Educational Testing | Full worked example of hierarchical model checking | Template for checking hierarchical company models. Check at both the individual-company level (does this company's model fit its own data?) and the sector level (does the population distribution fit the observed range of company behaviors?). |

---

## Connection to Previous Chapters

Posterior predictive checking was first mentioned in Chapter 1 Section 1.10 as one of the five practical advantages of Bayesian methods. This chapter delivers the full implementation. The posterior predictive distribution $p(\tilde{y} \mid y)$ introduced in Chapter 1 Section 1.3 is the same object used here for checking — you simulate replicated data from it and compare to the original observations.

The specific failure modes in Section 6.3 — tail underestimation, variance misspecification — connect directly to the choice between Normal and Student-t likelihoods discussed in Chapter 3 Section 3.2 and Chapter 17.