# 1.9 — Computation and Software

## What this section is doing

Gelman acknowledges the computational revolution that made Bayesian methods practically usable. For most of the history of Bayesian statistics, the math was theoretically sound but computationally impossible for anything beyond the simplest models. MCMC changed that completely.

---

## The problem MCMC solves

To compute the posterior exactly, you need to evaluate this integral:

$$p(y) = \int p(\theta) \cdot p(y \mid \theta) \, d\theta$$

For a model with one parameter, this might be doable analytically. For a model with five parameters — say, growth rate, margin, WACC, terminal multiple, and volatility — this becomes a five-dimensional integral that has no closed-form solution.

MCMC sidesteps the problem entirely. Instead of computing the posterior analytically, it draws samples from it directly.

---

## How MCMC works

The core idea is a random walker exploring the parameter space.

The walker moves according to rules that make it visit regions of the space proportionally to how probable they are under the posterior. High-probability regions get visited more. Low-probability regions get visited less. Run the walker long enough, and the collection of positions it visited is the posterior distribution — not a formula you solved for, but a set of samples drawn from it.

This works because the walker only needs to evaluate the ratio of probabilities at two points — its current position and a proposed next position. The normalizing constant $p(y)$ cancels out in that ratio, so it never needs to be computed.

---

## HMC and NUTS

The basic random walker (Metropolis-Hastings) works but is slow — it takes small random steps and explores the parameter space inefficiently.

**Hamiltonian Monte Carlo (HMC)** improves on this by using gradient information — the slope of the posterior surface — to take larger, more purposeful steps. It moves like a ball rolling across a curved landscape, using momentum to travel farther before stopping to evaluate.

**NUTS (No-U-Turn Sampler)** is an extension of HMC that automatically decides how far to roll before stopping, removing the need to manually tune step size. This is what PyMC uses by default.

In practice you almost never need to think about any of this. PyMC handles it automatically.

---

## PyMC

PyMC is the Python library that handles the full pipeline:

1. You specify the model — prior distributions and likelihood
2. PyMC builds the computation graph
3. NUTS runs and draws posterior samples
4. Samples are returned as an `InferenceData` object you can query directly

```python
import pymc as pm

with pm.Model() as model:
    theta = pm.Normal("theta", mu=0.07, sigma=0.03)   # prior
    sigma = pm.HalfNormal("sigma", sigma=0.02)          # prior on noise
    obs   = pm.Normal("obs", mu=theta, sigma=sigma,
                      observed=data)                    # likelihood
    trace = pm.sample(2000, return_inferencedata=True)  # posterior
```

---

## Convergence diagnostics

After sampling you need to verify that the chains actually converged to the true posterior. The key diagnostic is $\hat{R}$ (R-hat).

$\hat{R}$ compares variance within each chain to variance across chains. If all chains converged to the same distribution, these should be equal and $\hat{R}$ should be close to 1.

- $\hat{R}$ less than 1.01 — converged, results are trustworthy
- $\hat{R}$ between 1.01 and 1.1 — borderline, run more samples
- $\hat{R}$ greater than 1.1 — not converged, do not use the output

```python
import arviz as az
print(az.summary(trace, var_names=["theta", "sigma"]))
```

Always check this before interpreting any model output.

---

## Software landscape

| Tool | Language | Notes |
|------|----------|-------|
| PyMC | Python | Primary tool for this repo. Clean API, NUTS by default, ArviZ integration. |
| Stan | R / Python (via CmdStanPy) | More flexible for complex custom models. Steeper learning curve. |
| Bambi | Python | High-level wrapper over PyMC. Good for regression-style models. |
| NumPyro | Python | JAX-based, very fast. Worth exploring for production scale. |
