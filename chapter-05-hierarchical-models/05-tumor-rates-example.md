# 5.5 — Example: Estimating Tumor Rates in a Group of Rats

## What this section is doing

Gelman applies the Beta-Binomial hierarchical model to estimating tumor rates across a group of experimental rat populations — each population has a different sample size and observed tumor count. This is the direct analogue of estimating default rates or conversion rates across a coverage universe where some entities have more data than others.

---

## Simplification

You have 70 rat populations. Some have 20 rats, some have 5. In each population you observe how many developed tumors. You want to estimate the true tumor probability for each population.

Estimating each population separately produces wildly variable estimates — small populations drive extreme rates. Pooling everything together ignores real differences between populations. The hierarchical Beta-Binomial model finds the partial pooling solution: each population has its own probability, but all probabilities are drawn from a common Beta distribution whose parameters are estimated from all 70 populations simultaneously.

---

## Financial translation

Replace populations with companies, replace tumor rates with default probabilities. You have 70 companies in a credit portfolio. Each has a different amount of exposure history. The hierarchical Beta-Binomial model estimates each company's true default probability while sharing information across companies through the sector-level Beta hyperparameters.

The shrinkage is strongest for companies with the least exposure history. The model automatically adjusts how much each company borrows from the sector — no manual calibration required.

---

## See also

- Section 5.3 for the partial pooling formula
- Section 2.1 for the single-company Beta-Binomial model this extends
