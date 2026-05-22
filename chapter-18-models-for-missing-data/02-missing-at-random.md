# 18.2 — Missing at Random

## What this section is doing

Under MAR, the missing data mechanism can be ignored when the parameters of the data model and the missingness model are independent. Gelman shows when this condition holds and how to check it.

---

## Financial application

In a hierarchical company model, a company missing 2 quarters of data (due to a reporting delay, not distress) satisfies MAR — the missingness is not related to what the missing quarters would have shown. The hierarchical model handles this naturally: the missing quarters are marginalized out, and the posterior for that company's parameters is based on the available quarters plus the sector-level prior.

This is a significant advantage of the Bayesian hierarchical framework — it handles unbalanced panel data (different numbers of observations per company) without any special treatment.
