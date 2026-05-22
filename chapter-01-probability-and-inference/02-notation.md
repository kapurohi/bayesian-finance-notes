# 1.2 — General Notation for Statistical Inference

## What this section is doing

Gelman establishes the vocabulary for the rest of the book. Before any model can be built, you need a shared language for the things you can observe, the things you can't, and the things you want to predict. This section introduces that three-way distinction and it shows up on every page from here on.

---

## The Analogy

Think of a football match report.

The **scoreline** is observable — it happened, it's recorded, you can look it up. That's your data $y$.

The **manager's tactical intent** is unobservable — you can see the formation and the substitutions, but the actual reasoning behind the decisions lives in his head. You can only infer it from what happened on the pitch. That's your parameter $\theta$.

The **result of next week's match** hasn't happened yet, but you can forecast it using everything you know about both teams. That's your future data $\tilde{y}$.

Bayesian inference is the formal machinery for reasoning about all three of these things together.

---

## The Three Types of Quantities

**Observable data: $y$**

The data you've actually collected. Historical financial statements, reported quarterly earnings, market prices, macro indicators. These are fixed — they happened.

**Unobservable parameters: $\theta$**

The unknown quantities driving the data. The true underlying growth rate of a business. The actual long-run default probability of a borrower. The real operating leverage in a cost structure. You never observe $\theta$ directly — you infer it from $y$.

**Future/potentially observable data: $\tilde{y}$**

Quantities you haven't observed yet but could observe in the future. Next quarter's revenue. Forecasted EPS. The terminal value of a business in year 10. This is ultimately what your platform is trying to estimate — and Bayesian inference provides a full probability distribution over $\tilde{y}$, not just a point estimate.

---

## The Joint Distribution

Gelman introduces the idea of a **joint probability model**:

$$p(y, \theta)$$

This is a single distribution that captures both the data and the parameters together. It can be factored two ways:

$$p(y, \theta) = p(\theta) \cdot p(y \mid \theta)$$

Which reads as: the joint probability of the data and the parameters equals the prior over parameters times the likelihood of the data given those parameters.

This factorization is the formal setup for Bayes' rule, which comes in Section 1.3.

---

## Exchangeability

Gelman introduces a concept here that sounds technical but has a very practical implication: **exchangeability**.

A set of observations is exchangeable if the order they were collected in doesn't matter for what you're trying to infer. Formally, $y_1, y_2, \ldots, y_n$ are exchangeable if the joint distribution $p(y_1, \ldots, y_n)$ is the same under any permutation of the indices.

**Why this matters in finance:**

Exchangeability is the mathematical justification for pooling data across business units, time periods, or companies in the same sector when building priors. If you're willing to say that Q1 2022 revenue growth and Q3 2023 revenue growth are exchangeable — i.e., both are draws from the same underlying growth process — then you're justified in using all of that history together to estimate a single growth rate distribution.

This is the conceptual foundation for hierarchical models (Chapter 5), where you pool data across companies in the same sector while still allowing each company to have its own parameters.

---

## Breaking down the notation you'll see constantly

| Expression | How to read it | What it means |
|------------|---------------|---------------|
| $p(\theta)$ | "p of theta" | Prior distribution over the unknown parameter |
| $p(y \mid \theta)$ | "p of y given theta" | Likelihood — probability of the data, given a specific value of the parameter |
| $p(\theta \mid y)$ | "p of theta given y" | Posterior — updated belief about the parameter after seeing data |
| $p(\tilde{y} \mid y)$ | "p of y-tilde given y" | Posterior predictive — distribution over future observations |
| $p(y, \theta)$ | "p of y and theta" | Joint distribution over both data and parameters |

---

## See also

- [Notation Reference](../resources/notation-reference.md) for the complete symbol glossary
- Section 1.3 for how the joint distribution $p(y, \theta)$ leads directly to Bayes' rule
