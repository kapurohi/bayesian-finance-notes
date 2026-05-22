# 9.1 — Bayesian Decision Theory

## What this section is doing

Gelman connects the posterior distribution to formal decision-making. Given a posterior over unknown parameters and a utility function that quantifies how good each outcome is, the optimal decision is the one that maximizes **expected utility** — the posterior-weighted average of utilities across all possible states of the world.

---

## Simplification

You have a posterior distribution over a company's intrinsic value. You need to decide whether to buy the stock. The decision framework says: for each possible intrinsic value, how good is the outcome of buying versus not buying? Weight those outcomes by the posterior probability of each intrinsic value. The action with the highest weighted average outcome is optimal.

---

## The formal framework

An action $a$ has utility $U(a, \theta)$ when the true state is $\theta$. The **expected utility** of action $a$ is:

$$\mathbb{E}[U(a, \theta) \mid y] = \int U(a, \theta) \cdot p(\theta \mid y) \, d\theta$$

The optimal action is:

$$a^* = \arg\max_a \mathbb{E}[U(a, \theta) \mid y]$$

---

## Financial application

**Investment decision:**
- Action $a_1$: buy the stock
- Action $a_2$: do not buy
- Utility $U(a_1, \theta) = \theta - P$ (profit when intrinsic value is $\theta$ and current price is $P$)
- Buy when $\mathbb{E}[\theta \mid y] > P$ and the posterior distribution over $\theta - P$ has sufficient upside probability

This framework produces buy/sell/hold recommendations that are directly grounded in the posterior uncertainty — not in a single point estimate.

---

## See also
- Section 9.2 for how to specify the utility function
