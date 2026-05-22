# 6.3 — Posterior Predictive Checking

## What this section is doing

This is the central model checking tool in BDA3. Gelman formalizes the procedure for comparing model-generated data to real data. You draw samples from the posterior predictive distribution and compare them to the observed data using a **test statistic** — a summary of the data that you expect the model to replicate correctly.

---

## The procedure

**Step 1:** Fit the model and obtain posterior samples $\theta^{(1)}, \ldots, \theta^{(S)}$.

**Step 2:** For each posterior sample $\theta^{(s)}$, simulate a replicated dataset:

$$y^{\text{rep}(s)} \sim p(y \mid \theta^{(s)})$$

**Step 3:** Choose a test statistic $T(y)$ — a summary of the data you care about. Examples: the mean, the variance, the maximum, the proportion of values above a threshold, the autocorrelation.

**Step 4:** Compare $T(y^{\text{rep}})$ — the distribution of the test statistic across replicated datasets — to $T(y)$ — the test statistic on the actual data.

**Step 5:** Compute the **posterior predictive p-value**:

$$p_B = P\!\left(T(y^{\text{rep}}) \geq T(y) \mid y\right)$$

Values near 0 or 1 indicate the model is failing to replicate that aspect of the data. Values near 0.5 indicate a good fit for that test statistic.

---

## Choosing the right test statistic

The posterior predictive check is only as good as the test statistic. You should check:

- **Mean** — does the model get the center right?
- **Variance / standard deviation** — does the model get the spread right?
- **Skewness** — does the model capture asymmetry?
- **Tail behavior** — does the model produce the right frequency of extreme observations?
- **Autocorrelation** — for time-series data, does the model capture temporal dependence?

---

## Financial application

After fitting a Normal-Normal revenue growth model:

- Check the mean: simulated growth means should cluster around the observed mean
- Check the variance: if the model consistently underestimates spread, the likelihood variance is too small
- Check tail behavior: if the model never generates the large quarterly swings actually observed, the Normal likelihood may be too thin-tailed — a Student-t likelihood may be more appropriate
- Check autocorrelation: if real growth rates are serially correlated (a good year tends to follow a good year) but the model assumes i.i.d. observations, the autocorrelation check will fail