# 6.4 — Graphical Posterior Predictive Checks

## What this section is doing

Gelman advocates for visual model checking — plotting the distribution of replicated data alongside the actual data — as a more informative diagnostic than summary statistics alone. Many forms of model misspecification are immediately visible in plots but would be missed by any single test statistic.

---

## Standard graphical checks

**Density overlay:** Plot the kernel density of the observed data alongside the densities of 50–100 replicated datasets. If the replicated densities cluster around the observed density, the model fits. If they are systematically shifted or shaped differently, the model is misspecified.

**Histogram comparison:** Overlay histograms of replicated data on the observed histogram. Systematic gaps between observed and replicated distributions indicate misspecification.

**Residual plots:** For regression models, plot residuals against fitted values and against predictors. Systematic patterns indicate a missing predictor or a misspecified functional form.

**Tail plots:** Focus specifically on the tails of the distribution. Many financial models fail not in the center but in the tails — they underestimate the frequency of large positive or negative outcomes.

---

## Financial application

After fitting a growth rate model, plot the distribution of simulated quarter-over-quarter growth rates against the actual historical distribution. If the model's simulated distribution is narrower than the observed distribution — missing the large upside and downside quarters — the likelihood variance is underestimated. This is a common failure mode for Normal models applied to financial returns.