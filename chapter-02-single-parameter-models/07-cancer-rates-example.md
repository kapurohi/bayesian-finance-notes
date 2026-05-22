# 2.7 — Example: Informative Prior Distribution for Cancer Rates

## What this section is doing

Gelman works through a real applied example — estimating kidney cancer death rates across US counties — to show how informative priors work in practice when data varies dramatically in quality and quantity across units. Small counties have very few observations and wildly unstable raw rates. The prior stabilizes them.

---

## Simplification

Imagine you're trying to estimate the default rate for every county-level bank in the US. Some banks are large with decades of data. Some are tiny community banks with only a handful of loans ever made.

For the large banks, the data speaks for itself. For the tiny banks, even a single default makes the raw rate look catastrophically high, and zero defaults makes it look impossibly safe. Neither extreme is trustworthy.

The Bayesian approach puts a prior on all banks based on their overall historical context — and the prior pulls the extreme estimates back toward something reasonable, proportionally more for the banks with less data and less for the ones with lots of data.

That is exactly what Gelman does with the cancer rate example.

---

## The key insight: small samples produce extreme estimates

This is sometimes called the **small-area estimation problem**. When $n$ is tiny:

- A raw rate of $y/n$ is very noisy
- Extreme values dominate just by chance
- Both the highest and lowest rates in a dataset are disproportionately populated by small-sample units

If you ranked US counties by kidney cancer rate and looked at the top 10 and bottom 10, you would find they are almost entirely rural, sparsely populated counties. This is not because rural life is both the healthiest and most dangerous — it is because small $n$ produces extreme estimates in both directions.

A Bayesian model with an informative prior corrects for this automatically. The posterior for a small-county estimate gets pulled hard toward the prior. The posterior for a large-county estimate barely moves.

---

## Financial translation

**Credit rating across borrowers of different sizes:**

Large corporate borrowers have long credit histories — 20+ years of financials, multiple debt issuances, well-established default experience. The data dominates.

Small private companies or recent IPOs have limited history — 2–3 years of financials, possibly no prior debt. Raw estimates are noisy and extreme.

A Bayesian model with a sector-level informative prior stabilizes the small-company estimates. The posterior for a company with 3 quarters of history gets pulled significantly toward the sector prior. The posterior for a company with 30 quarters of history is almost entirely determined by its own data.

This is the same mechanism Gelman demonstrates with counties and cancer rates — and it is directly applicable to any financial modeling problem where data volume varies dramatically across the units being estimated.

---

## See also

- Section 2.2 for the prior-data compromise that drives this stabilization
- Section 2.4 for how to construct the informative prior used in this kind of model
- Section 1.4 for the base rate problem — the same small-sample intuition from a different angle
