# 1.7 — Example: Spelling Correction

## What this section is doing

Gelman uses a natural language spelling correction problem to show that Bayes' rule is not just a statistics technique — it's a general inference engine that applies to any domain where you're reasoning from noisy observations back to the true underlying state. This example is the cleanest proof that the framework is universal.

---

## The Analogy

You type "recieve" into a document. The spell-checker needs to figure out what you meant.

It has two inputs:

1. **Prior:** some words appear far more often than others in normal writing. "Receive" is common. "Recieve" is not a real word.
2. **Likelihood:** some typos are more probable than others given a specific intended word. Swapping "ie" and "ei" is a very common mistake — so the probability of typing "recieve" given that you meant "receive" is relatively high.

The spell-checker multiplies prior word frequency by the probability of this specific typo, and it picks the word with the highest posterior probability. It outputs "receive."

That's Bayes' rule applied to language. The exact same structure applies to financial signals.

---

## The financial translation

Your platform receives a noisy earnings signal. Revenue came in at $412M. The model needs to infer what this says about the company's true underlying growth trajectory.

- **Prior:** distribution over possible true growth rates based on sector history and prior quarters
- **Likelihood:** probability of observing $412M in revenue given a specific true growth rate
- **Posterior:** updated distribution over the true growth rate, incorporating this quarter's data

The noisy observation is the "misspelling." The true growth rate is the "intended word." Bayes' rule is the spell-checker.

---

## MAP vs. full posterior

This example also introduces the **MAP estimate** — Maximum A Posteriori. It's the single value of $\theta$ that maximizes the posterior:

$$\hat{\theta}_{MAP} = \arg\max_{\theta} \, p(\theta \mid y)$$

The MAP is the Bayesian equivalent of a point estimate. It tells you the single most probable value of $\theta$ given the data and prior.

But the MAP throws away most of what the posterior tells you. It gives you the peak of the distribution without telling you anything about its shape, width, or tails.

For a financial platform, the full posterior is almost always more valuable than the MAP:

- The MAP says: *the most likely growth rate is 7.2%*
- The full posterior says: *there's a 68% probability that growth is between 5.1% and 9.3%, a 12% probability it's below 3%, and a 4% probability it exceeds 14%*

The second statement is actionable risk intelligence. The first is just a number.

---

## See also

- Section 1.3 for Bayes' rule derivation
- Section 1.9 for how MCMC samples the full posterior rather than just finding the MAP
- Chapter 2 for worked models where MAP and full posterior are computed and compared
