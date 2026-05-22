# 2.8 — Noninformative Prior Distributions

## What this section is doing

Gelman addresses what to do when you genuinely have no prior knowledge — or when you want the data to speak for itself without any prior influence. A noninformative prior is an attempt to encode total ignorance about a parameter. This section explains what that means, why it is harder than it sounds, and when it is and isn't appropriate.

---

## Simplification

A flat prior sounds like the honest thing to do when you know nothing — just say every value is equally likely. But there is a problem. If you say every value of $\theta$ is equally likely, and then someone transforms $\theta$ to a different scale — say, $\log(\theta)$ — the transformed quantity is no longer flat. You can't be uniformly ignorant on every scale simultaneously.

This means "true noninformative" priors don't really exist. What we can do is choose priors that are as weakly informative as possible while still being mathematically valid.

---

## The uniform prior

The simplest attempt at a noninformative prior is a flat prior:

$$p(\theta) \propto 1$$

This assigns equal probability density to every value of $\theta$. For a parameter bounded between 0 and 1 — like a probability — this is the $\text{Beta}(1, 1)$ distribution.

The problem: a flat prior on $\theta$ is not flat on $\theta^2$, or $\log(\theta)$, or any other transformation. So "flat" is not a scale-invariant property.

---

## Jeffreys prior

Harold Jeffreys proposed a prior that is invariant under reparameterization — it produces the same inference regardless of how you write the model:

$$p(\theta) \propto \sqrt{I(\theta)}$$

Where $I(\theta)$ is the **Fisher information** — a measure of how much information the data provides about $\theta$ at a specific value.

For the Binomial model, the Jeffreys prior is $\text{Beta}(1/2, 1/2)$ — slightly U-shaped, putting more mass near 0 and 1 than the flat prior. For the Normal mean with known variance, it is simply the flat prior.

---

## When noninformative priors are appropriate

- You are in a genuinely novel domain with no historical comparables
- You want to demonstrate that your conclusions are driven entirely by the data
- You are performing a sensitivity analysis to see how much the prior matters

---

## When they are not appropriate

- When you have real domain knowledge — using a flat prior throws that away
- When data is sparse — a flat prior combined with limited data produces poorly calibrated posteriors
- When the parameter is bounded and the flat prior assigns probability to impossible values

For most financial modeling problems, some prior knowledge always exists. Sector benchmarks, historical base rates, and economic constraints should be encoded rather than discarded.

---

## See also

- Section 2.4 for how to build informative priors when knowledge exists
- Section 2.9 for the practical middle ground — weakly informative priors
- Section 1.5 for the philosophical basis for encoding prior knowledge formally
