# 2.9 — Weakly Informative Prior Distributions

## What this section is doing

Gelman introduces the concept that sits between fully informative and completely noninformative priors — the **weakly informative prior**. This is the most practically useful prior type for real-world modeling. It encodes just enough knowledge to rule out clearly impossible values while still letting the data drive the inference.

---

## Simplification

A fully informative prior says: "I am fairly confident the growth rate is between 6% and 10%."

A noninformative prior says: "Any growth rate from negative infinity to positive infinity is equally plausible."

A weakly informative prior says: "I don't think growth is going to be 500% or negative 200%, but beyond ruling out the absurd, I'm letting the data decide."

In practice, weakly informative priors are almost always the right choice. They prevent the model from producing nonsensical estimates while keeping the posterior genuinely responsive to the data.

---

## What makes a prior weakly informative

A weakly informative prior should:

1. **Rule out parameter values that are physically or economically impossible** — a probability cannot exceed 1, a standard deviation cannot be negative, revenue growth cannot be 10,000%
2. **Be wide enough that the data can easily override it** — the prior should not be so tight that it prevents the posterior from moving significantly
3. **Encode directional constraints when they exist** — if you know a parameter must be positive, use a distribution that only has support on positive values

---

## Common weakly informative priors in practice

| Parameter type | Weakly informative choice | Reasoning |
|---------------|--------------------------|-----------|
| Mean of a bounded quantity | $\text{Normal}(\mu_0, \text{large } \sigma)$ | Centered at a plausible value but very wide |
| Standard deviation | $\text{HalfNormal}(\sigma)$ | Constrained to be positive, but wide |
| Probability | $\text{Beta}(1, 1)$ or $\text{Beta}(2, 2)$ | Flat or mildly centered at 0.5 |
| Positive continuous quantity | $\text{LogNormal}$ or $\text{Gamma}$ with large variance | Constrained positive, diffuse |

---

## Financial application

**Revenue growth rate model:**

Instead of a tight informative prior centered at 7% with $\sigma = 2\%$, a weakly informative prior might be:

$$\mu_{\text{growth}} \sim \text{Normal}(0.07, 0.15)$$

This says: growth is probably somewhere near 7%, but I'm not ruling anything out between roughly -30% and +45%. The data from even a single year of earnings will dominate this prior completely.

**Volatility parameter:**

$$\sigma \sim \text{HalfNormal}(0.10)$$

This constrains volatility to be positive — which is required — but allows it to take any reasonable value. It prevents the model from fitting nonsensically small or large volatilities without genuinely constraining the estimate.

---

## The practical recommendation

For the platform's production models, weakly informative priors are the default starting point:

- Use sector medians to center the prior mean
- Use wide standard deviations so the data can move the posterior freely
- Use appropriate distribution families to enforce known constraints (positivity, boundedness)
- Tighten toward informative priors when historical sector data is robust and you want to leverage it

This approach gives you the stability benefits of a prior without the risk of forcing your conclusions.

---

## See also

- Section 2.4 for how to construct fully informative priors from domain knowledge
- Section 2.8 for noninformative priors and their limitations
- Section 1.6 for the structural prior concept — weakly informative priors are often built from the same sector-level data
