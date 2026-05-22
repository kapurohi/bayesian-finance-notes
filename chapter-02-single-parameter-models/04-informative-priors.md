# 2.4 — Informative Prior Distributions

## What this section is doing

Gelman addresses the practical question of how to actually construct a prior when you have genuine domain knowledge. An informative prior is not a guess — it is a formal encoding of real information that exists before the data is collected. This section gives the tools to do that rigorously.

---

## Simplification

Saying "I have no idea" when you actually do have relevant knowledge is not being objective — it is throwing away information. If you know that investment-grade default rates have historically averaged around 1–3%, encoding that as a flat prior from 0% to 100% is dishonest and produces worse estimates than using what you know.

An informative prior is just being honest about what you already know before the data arrives.

---

## How to construct an informative prior

**Method 1 — Prior predictive matching**

Simulate data from your prior and ask: does this look like plausible data for this problem?

If your prior over a default probability produces simulated default rates of 40% for investment-grade bonds, the prior is wrong. Adjust the hyperparameters until the simulated data looks like what you would actually expect to observe.

**Method 2 — Moment matching**

If you have beliefs about the mean and variance of $\theta$, you can solve for the hyperparameters that produce a distribution with those moments.

For the Beta distribution:

$$\alpha = \mu \left(\frac{\mu(1-\mu)}{\sigma^2} - 1\right), \qquad \beta = (1-\mu)\left(\frac{\mu(1-\mu)}{\sigma^2} - 1\right)$$

Where $\mu$ is your prior mean and $\sigma^2$ is your prior variance. You plug in what you believe about the center and spread of $\theta$, and the formula gives you $\alpha$ and $\beta$.

**Method 3 — Effective sample size**

As shown in Section 2.2, the sum $\alpha + \beta$ is the effective sample size of a Beta prior — how many pseudo-observations your prior is worth. If you believe your prior is roughly as reliable as 10 historical observations, set $\alpha + \beta = 10$.

---

## Prior elicitation from data

When historical data is available for similar problems — same sector, comparable companies, historical base rates — you can fit a distribution directly to that data and use it as the prior for the new problem.

For example: collect default rates across 200 investment-grade issuers over 10 years. Fit a Beta distribution to those rates. Use the fitted Beta as the prior for estimating the default probability of a new issuer entering the portfolio.

This is called **empirical Bayes** — using data to set the prior. It is a practical and widely used approach, though Gelman notes it slightly underestimates uncertainty because it treats the prior as known rather than estimated.

---

## Financial application

**Setting a prior for operating margin:**

You are building a model for a SaaS company. You know from sector benchmarks that mature SaaS operating margins cluster around 15–25%, with a median around 20% and most companies falling within a 10 percentage point band.

- Prior mean $\mu = 0.20$
- Prior standard deviation $\sigma = 0.05$

Using moment matching:

$$\frac{\mu(1-\mu)}{\sigma^2} - 1 = \frac{0.20 \times 0.80}{0.0025} - 1 = 63$$

So $\alpha = 0.20 \times 63 = 12.6$ and $\beta = 0.80 \times 63 = 50.4$.

Prior: $\text{Beta}(12.6, 50.4)$ — centered at 20%, with 95% of prior mass between roughly 10% and 32%.

This prior encodes real sector knowledge, not a guess. As company-specific margin data arrives, the posterior moves away from the sector benchmark toward the company's actual performance.

---

## See also

- Section 2.2 for how the prior strength interacts with data to determine the posterior
- Section 2.8 and 2.9 for the alternative approaches when prior knowledge is limited
- Section 1.6 for the structural prior concept that motivates this approach
