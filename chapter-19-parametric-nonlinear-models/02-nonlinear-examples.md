# 19.2 — Examples of Nonlinear Models

## What this section is doing

Gelman works through pharmacokinetics examples where the drug concentration follows a known compartment model. The financial analogues are well-specified growth and decay models.

---

## Financial application

**DCF as a nonlinear model:** The DCF formula itself is a nonlinear function of growth rate $g$, margin $m$, WACC $r$, and revenue $R$:

$$V = \sum_{t=1}^T \frac{m \cdot R(1+g)^t}{(1+r)^t} + \frac{m \cdot R(1+g)^T(1+g_T)}{(r-g_T)(1+r)^T}$$

This is a parametric nonlinear model. Given posterior samples of $(g, m, r, g_T)$ from Chapters 2-3, the posterior over $V$ is computed by evaluating this formula at each sample. No additional modeling required — the nonlinearity is handled automatically by posterior simulation.

**Mean-reversion model:**

$$\text{EBITDA}_t = \mu + \phi(\text{EBITDA}_{t-1} - \mu) + \epsilon_t$$

An autoregressive model for EBITDA margins: they mean-revert toward the long-run level $\mu$ at speed $1 - \phi$. The Bayesian posterior over $\phi$ tells you whether margins are strongly mean-reverting (small $\phi$) or persistent (large $\phi$).
