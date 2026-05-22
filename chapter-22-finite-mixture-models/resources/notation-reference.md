# Notation Reference

This is my master glossary for every symbol that shows up across BDA3. I update this as new notation is introduced chapter by chapter.

Greek letters and math symbols are genuinely confusing the first time you see them. The goal here is simple: one place where every symbol is defined in plain English, with a financial example next to it.

---

## Core Symbols

| Symbol | Name | Plain English | Financial Example |
|--------|------|---------------|-------------------|
| $\theta$ | theta | The unknown quantity you're trying to estimate | Revenue growth rate, operating margin, default probability |
| $y$ | y | The data you actually observed | Reported quarterly earnings, historical revenue figures |
| $\tilde{y}$ | y-tilde | Future data you haven't observed yet | Next quarter's revenue, forecasted EPS |
| $p(\theta)$ | Prior | Your belief about $\theta$ before seeing any data | "I think revenue growth is probably between 3% and 12%" |
| $p(y \mid \theta)$ | Likelihood | How probable is the data $y$, if $\theta$ were true | How likely is this earnings report, given a true growth rate of 7%? |
| $p(\theta \mid y)$ | Posterior | Your updated belief about $\theta$ after seeing data | Updated growth rate distribution after this quarter's earnings |
| $p(y)$ | Marginal likelihood | Total probability of observing $y$ across all possible $\theta$ values | Normalizing constant — usually skipped in computation |
| $p(\tilde{y} \mid y)$ | Posterior predictive | Probability distribution over future outcomes | Distribution over next quarter's revenue, averaging over all plausible growth rates |

---

## Distribution Shorthand

| Symbol | Meaning |
|--------|---------|
| $\text{Normal}(\mu, \sigma^2)$ | Normal distribution with mean $\mu$ and variance $\sigma^2$ |
| $\text{Beta}(\alpha, \beta)$ | Beta distribution — used for probabilities between 0 and 1 |
| $\text{Binomial}(n, \theta)$ | Binomial distribution — counts of successes in $n$ trials |
| $\text{Gamma}(\alpha, \beta)$ | Gamma distribution — used for positive continuous quantities |
| $\text{HalfNormal}(\sigma)$ | Normal distribution truncated at zero — used for standard deviations |

---

## Operators and Notation

| Symbol | Meaning |
|--------|---------|
| $\propto$ | "Proportional to" — equals up to a constant. Used because the normalizing constant $p(y)$ is usually dropped |
| $\mathbb{E}[\theta]$ | Expected value of $\theta$ — the probability-weighted average |
| $\text{Var}(\theta)$ | Variance of $\theta$ — how spread out the distribution is |
| $\mid$ | "Given" or "conditional on" — $p(\theta \mid y)$ means "probability of $\theta$ given that we observed $y$" |
| $\sim$ | "Distributed as" — $\theta \sim \text{Normal}(0, 1)$ means $\theta$ follows a standard normal distribution |

---

*Updated as new symbols appear across chapters.*
