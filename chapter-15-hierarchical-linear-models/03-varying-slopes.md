# 15.3 — Varying Slope Models

## What this section is doing

Gelman extends to models where both the intercept and the slope vary across groups. This is the full random-effects regression — each company has its own baseline and its own response to predictors.

---

## Financial application

**Cyclicality heterogeneity:** Some companies are highly cyclical (high GDP sensitivity), others are defensive (low GDP sensitivity). A varying-slope model estimates both the company-specific sensitivity and the sector-level distribution of sensitivities simultaneously.

**Portfolio construction:** The posterior distribution over each company's GDP sensitivity feeds directly into portfolio construction — overweight defensive companies heading into a recession (low posterior $\beta_j$), overweight cyclicals in expansion (high $\beta_j$), with uncertainty in the sensitivities appropriately reflected.

---

## See also
- Section 15.1 for the full joint model
