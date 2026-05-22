# 12.3 — The No-U-Turn Sampler (NUTS)

## What this section is doing

HMC requires choosing a trajectory length $L$ — how far to roll before stopping. Too short and HMC reduces to random walk behavior. Too long and the trajectory doubles back on itself, wasting computation. NUTS automatically finds the optimal trajectory length by stopping when the trajectory would start doubling back (when it takes a U-turn).

---

## Why this matters

NUTS eliminates the most important tuning parameter in HMC. Combined with the dual-averaging step-size adaptation in the warm-up phase, NUTS requires virtually no manual tuning. This is why PyMC uses NUTS as its default sampler — you specify the model, and NUTS handles the rest.

---

## NUTS in PyMC

```python
with pm.Model() as model:
    # ... prior and likelihood ...
    trace = pm.sample(
        draws=2000,
        tune=1000,          # warm-up for step size adaptation
        target_accept=0.9,  # target acceptance rate (higher = smaller steps)
        return_inferencedata=True
    )
```

`target_accept=0.9` is a good default for most financial models. Increase to 0.95 for models with difficult geometries (funnel shapes, strong correlations between parameters).

---

## Divergences

NUTS reports **divergences** — trajectory steps where the numerical integration becomes inaccurate, indicating the sampler is exploring a region of the posterior it is not handling correctly. Divergences are a warning sign.

Common causes in financial models:
- Strong prior-likelihood conflict
- Hierarchical models where the group-level variance $\tau$ is near zero
- Highly correlated parameters

The fix is usually reparameterization — a non-centered parameterization for hierarchical models typically eliminates divergences.

---

## See also
- Section 11.5 for convergence diagnostics to run after sampling
- Chapter 5 for hierarchical models where non-centered parameterization matters
