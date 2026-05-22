# 6.5 — Model Checking for the Educational Testing Example

## What this section is doing

Gelman works through a complete posterior predictive check for the classic eight-schools educational testing dataset — a hierarchical model. The check reveals that while the model fits the data well in most respects, it has specific failure modes that can be diagnosed and addressed.

---

## The financial parallel

The eight-schools example maps directly to an eight-company hierarchical earnings model. The posterior predictive checks reveal:

- Whether the hierarchical model is capturing between-company variation correctly
- Whether the shrinkage is appropriate — are estimates for low-data companies being pulled toward the sector mean by the right amount?
- Whether there are specific companies whose posteriors are systematically at odds with their observed data (outliers that may warrant their own treatment)

The methodological lesson is that model checking should be applied at both the individual-unit level (does this specific company's model fit its own data?) and the population level (does the sector-level distribution correctly describe the range of company behaviors?).

---

## See also

- Section 5.4 for the hierarchical Normal model these checks are applied to
- Section 6.3 for the formal posterior predictive check procedure