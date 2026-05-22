# 3.3 — Normal Data with a Conjugate Prior Distribution

## What this section is doing

Section 3.2 used a noninformative prior and got the t-distribution result. This section uses a conjugate prior for both $\mu$ and $\sigma^2$ — the **Normal-Inverse-Gamma** family. This gives a closed-form posterior and allows genuine prior knowledge about both the mean and the variance to be encoded formally.

---

## The conjugate prior family

For the Normal likelihood with unknown mean and variance, the conjugate prior is:

$$\mu \mid \sigma^2 \sim \text{Normal}\!\left(\mu_0, \, \frac{\sigma^2}{\kappa_0}\right)$$

$$\sigma^2 \sim \text{Inverse-Gamma}\!\left(\frac{\nu_0}{2}, \, \frac{\nu_0 \sigma_0^2}{2}\right)$$

The four hyperparameters and what they encode:

| Hyperparameter | Meaning |
|---------------|---------|
| $\mu_0$ | Prior mean — your belief about the true center before data |
| $\kappa_0$ | Prior sample size for the mean — how many observations the prior is worth |
| $\nu_0$ | Prior degrees of freedom for the variance — how confident you are about $\sigma_0^2$ |
| $\sigma_0^2$ | Prior estimate of the variance — your belief about the noise level |

---

## The posterior update

After observing $n$ data points with sample mean $\bar{y}$ and sample variance $s^2$:

$$\kappa_n = \kappa_0 + n$$

$$\mu_n = \frac{\kappa_0 \mu_0 + n\bar{y}}{\kappa_0 + n}$$

$$\nu_n = \nu_0 + n$$

$$\nu_n \sigma_n^2 = \nu_0 \sigma_0^2 + (n-1)s^2 + \frac{\kappa_0 n}{\kappa_0 + n}(\bar{y} - \mu_0)^2$$

The last term captures the contribution to variance uncertainty from the discrepancy between the prior mean and the sample mean. If your prior was centered very differently from what the data shows, variance uncertainty increases.

---

## Financial application

**Joint growth rate and volatility model:**

Prior beliefs: growth is around 8% ($\mu_0 = 0.08$), with prior sample size $\kappa_0 = 5$. Quarterly noise is around 2% ($\sigma_0 = 0.02$), with $\nu_0 = 4$ prior observations.

After 8 quarters of data: $\bar{y} = 0.078$, $s = 0.014$.

Both the growth rate estimate and the noise estimate are updated jointly — and crucially, uncertainty about the noise level correctly propagates into uncertainty about the growth rate estimate through the marginal posterior.

---

## See also

- Section 3.2 for the noninformative version of this model
- Section 2.5 for the simpler Normal-Normal model with known variance
