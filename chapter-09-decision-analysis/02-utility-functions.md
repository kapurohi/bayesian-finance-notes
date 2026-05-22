# 9.2 — Utility Functions

## What this section is doing

Gelman discusses how to specify the utility function that translates outcomes into a common scale. The choice of utility function encodes risk preferences — a risk-neutral investor treats a 10% chance of $100 the same as a certain $10; a risk-averse investor prefers the certain $10.

---

## Common utility functions

**Linear utility (risk-neutral):** $U(x) = x$

The optimal decision maximizes expected monetary value. Used when stakes are small relative to total wealth.

**Logarithmic utility (risk-averse):** $U(x) = \log(x)$

Optimal for investors whose welfare depends on multiplicative returns — appropriate for long-horizon portfolio decisions.

**Quadratic utility:** $U(x) = x - \frac{b}{2}x^2$

Produces mean-variance optimization — the formal Bayesian foundation for Markowitz portfolio theory.

---

## Financial application

Risk-neutral utility is appropriate for single-transaction decisions with small stakes. For portfolio-level decisions involving capital allocation, logarithmic utility is more appropriate — it reflects the compounding nature of investment returns and naturally produces diversification as an optimal strategy.

---

## See also
- Section 9.1 for how utility functions feed into the expected utility calculation
