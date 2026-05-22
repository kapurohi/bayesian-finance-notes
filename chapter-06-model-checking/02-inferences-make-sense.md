# 6.2 — Do the Inferences Make Sense?

## What this section is doing

Before running any formal diagnostic, Gelman recommends a simple qualitative check: look at the posterior summaries and ask whether they make sense given domain knowledge. Implausible estimates — a negative growth rate for a company with 20% revenue CAGR, or a default probability above 50% for an investment-grade issuer — signal model problems immediately.

---

## The qualitative checklist

- Do posterior means sit in the range of plausible values for this parameter?
- Are posterior credible intervals neither impossibly narrow nor impossibly wide?
- Does the posterior predictive mean match the observed data mean approximately?
- Are the hyperparameter estimates (in a hierarchical model) consistent with sector knowledge?

These checks cost nothing and catch obvious errors before more sophisticated diagnostics are run.

---

## Financial application

After fitting a revenue growth model, the first check is simply: does the posterior mean growth rate look like what you'd expect for this company in this sector? If the model returns a 35% posterior mean growth rate for a mature utility company, something is wrong with the likelihood, the prior, or the data itself. Fix the obvious problems before running formal posterior predictive checks.