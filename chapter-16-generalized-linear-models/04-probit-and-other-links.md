# 16.4 — Probit and Other Link Functions

## What this section is doing

The logit link is the most common for binary outcomes but not the only option. The probit link uses the Normal CDF instead of the logistic function. The two produce nearly identical results in most applications but differ in the tails.

---

## Financial application

**Probit in credit modeling:** Some structural credit models (Merton-type) produce Normal CDF default probabilities naturally — the probit link is the correct link function in these cases, producing results consistent with the structural model's assumptions.

**Complementary log-log link:** Appropriate for rare events where the probability is very small — extreme tail default rates, catastrophic loss events. The cloglog link is asymmetric and puts more mass on small probabilities than the logit or probit.
