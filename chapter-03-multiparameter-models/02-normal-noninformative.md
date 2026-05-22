# 3.2 — Normal Data with a Noninformative Prior Distribution

## What this section is doing

Section 2.5 assumed the observation variance $\sigma^2$ was known. That is rarely true in practice. This section treats both the mean $\mu$ and variance $\sigma^2$ as unknown simultaneously, using a noninformative prior for both. The result is a joint posterior where you need to marginalize over $\sigma^2$ to get the posterior over $\mu$ — and that marginal posterior turns out to be a Student-t distribution.

---

## Simplification

You have quarterly revenue growth data. You want to estimate the true underlying growth rate. But you also don't know how noisy the quarterly figures are — that's a second unknown you have to estimate from the same data.

When both the level and the noise are unknown, there's more total uncertainty than when one of them is fixed. The resulting posterior over the growth rate is wider and heavier-tailed than a Normal distribution — it puts more probability on extreme values, because you're not sure how noisy the data is.

That wider, heavier-tailed distribution is a Student-t distribution. It is the honest result when you've estimated both parameters from the same data.

---

## The model

**Noninformative prior:**

$$p(\mu, \sigma^2) \propto \frac{1}{\sigma^2}$$

This is the Jeffreys prior for the location-scale family. It is flat on $\mu$ and flat on $\log(\sigma)$ — encoding ignorance about both the mean and the scale.

**Joint posterior:**

$$p(\mu, \sigma^2 \mid y) \propto \sigma^{-n-2} \exp\left(-\frac{1}{2\sigma^2}\left[(n-1)s^2 + n(\bar{y} - \mu)^2\right]\right)$$

Where $\bar{y}$ is the sample mean and $s^2$ is the sample variance.

**Marginal posterior over $\mu$ — the key result:**

After integrating out $\sigma^2$:

$$p(\mu \mid y) \propto \left[1 + \frac{n(\mu - \bar{y})^2}{(n-1)s^2}\right]^{-n/2}$$

This is a **Student-t distribution** with $n - 1$ degrees of freedom, centered at $\bar{y}$, with scale $s/\sqrt{n}$:

$$\mu \mid y \sim t_{n-1}\!\left(\bar{y}, \, \frac{s^2}{n}\right)$$

---

## Why Student-t and not Normal

The Student-t distribution has heavier tails than the Normal. With small $n$, the tails are very heavy — the distribution is saying "there's meaningful probability that the true mean is quite far from the sample mean, because we don't have much data."

As $n \to \infty$, the Student-t converges to a Normal. With a lot of data, the two become indistinguishable — which is the correct behavior.

This is the Bayesian justification for why frequentist t-tests use the t-distribution. The t-distribution is the honest posterior over the mean when variance is unknown and estimated from the same data.

---

## Financial application

**Revenue growth with unknown noise:**

8 quarters of revenue growth data: mean $\bar{y} = 7.8\%$, sample std $s = 1.4\%$.

With noninformative prior, the marginal posterior over the true growth rate is:

$$\mu \mid y \sim t_7\!\left(0.078, \, \frac{0.014^2}{8}\right)$$

The 95% credible interval from the t-distribution is slightly wider than what a Normal posterior would give — correctly reflecting that you estimated the noise from the same 8 data points you used to estimate the mean.

For a DCF model, this means the uncertainty band around your growth rate estimate is properly wider when you have less data and haven't externally verified the noise level. The model is being honest.

---

## See also

- Section 2.5 for the Normal-Normal model where $\sigma^2$ was assumed known
- Section 3.1 for the marginalization operation that produces the t-distribution result
- Section 3.3 for the conjugate prior version of this model
