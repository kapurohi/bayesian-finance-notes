# 1.6 — Example: Inference About a Genetic Probability

## What this section is doing

Gelman works through a hereditary disease example where structural knowledge about a family tree serves as the prior, and observed test results update that prior. The reason this section matters isn't the genetics — it's the demonstration that non-data domain knowledge can be rigorously encoded as a prior, and that sequential data collection naturally sharpens the posterior step by step.

---

## The Analogy

Imagine a family where a hereditary condition appears in roughly half of all siblings across multiple generations. A new child is born. What's the probability they'll develop it?

You don't wait to find out. You use the family pattern as your prior: roughly 50% chance. As the child grows, you observe more signals — a preliminary genetic marker test comes back borderline, they show some early indicators. Each observation updates the posterior. The prior based on family structure prevents you from overreacting to a single ambiguous test result.

In this example, the prior doesn't come from a dataset of this specific person — it comes from structural knowledge about how the disease works. That's a **structural prior**.

---

## The financial translation

This maps directly to how you build priors for companies with limited history.

A company just completed its IPO. You have two quarters of earnings. That's not enough data to estimate a stable growth rate. But you do know:

- What sector it operates in
- What the median revenue growth rate distribution looks like for comparable public companies in that sector
- What the typical margin trajectory looks like in years 2–5 post-IPO

You encode all of that as a structural prior — built from industry data, not from this company's own history. As quarterly earnings arrive, those observations update the prior toward a company-specific posterior.

This is the direct architectural preview of **hierarchical Bayesian models** (Chapter 5). The industry distribution is the top level of the hierarchy. The company-specific estimate is the bottom level, constrained by and pulled toward the industry prior, especially when company-specific data is sparse.

---

## Sequential updating

One of the most powerful demonstrations in this section is showing how updating works sequentially:

$$p(\theta \mid y_1, y_2) \propto p(\theta) \cdot p(y_1 \mid \theta) \cdot p(y_2 \mid \theta)$$

Which is equivalent to:

$$p(\theta \mid y_1, y_2) \propto p(\theta \mid y_1) \cdot p(y_2 \mid \theta)$$

Today's posterior is tomorrow's prior. The order in which data arrives doesn't matter — the final posterior is the same whether you update once with all the data or sequentially one observation at a time.

For a live financial platform ingesting quarterly earnings, this means the model can update every time new data arrives without rebuilding from scratch.

---

## See also

- Section 1.3 for the sequential update derivation
- Chapter 5 for hierarchical models that formalize the industry-to-company prior structure
