# 22.3 — Regime-Switching Models

## What this section is doing

Regime-switching models are temporal mixture models where the latent state (regime) evolves over time according to a Markov process. This is the Hamilton (1989) regime-switching model, which has been enormously influential in macroeconomics and finance.

---

## The Hidden Markov Model structure

$$z_t \mid z_{t-1} \sim \text{Categorical}(P_{z_{t-1}})$$

$$y_t \mid z_t \sim p(y_t \mid \theta_{z_t})$$

The latent regime $z_t$ follows a Markov chain with transition matrix $P$. The observed return or growth rate is drawn from the regime-specific distribution.

---

## Financial application

**Two-regime revenue growth model:** One regime has mean growth 8% and low volatility (normal expansion). The other has mean growth -2% and high volatility (recession/crisis). The Bayesian posterior over:
- The transition probabilities: how long each regime tends to last
- The current regime probability: what is the probability we are currently in a recession?
- The regime-conditional parameters: what do growth and volatility look like in each state?

This directly supports recession-probability monitoring and regime-conditional scenario analysis for DCF models.
