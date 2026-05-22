"""
normal_normal_model.py
----------------------
Chapter 2 — Single-Parameter Models

What it does:
    Implements the Normal-Normal conjugate model for estimating a continuous
    unknown parameter from observed data. Two financial examples:
    - Revenue growth rate estimation from quarterly data
    - Operating margin estimation from quarterly income statements

    Demonstrates both the analytical closed-form posterior and the PyMC
    sampling version side by side so you can see they produce the same result.

Dependencies:
    pip install pymc arviz numpy matplotlib scipy
"""

import numpy as np
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from scipy import stats


# ---------------------------------------------------------------------------
# EXAMPLE 1 — Revenue Growth Rate Estimation
# ---------------------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 1: Revenue Growth Rate Estimation")
print("=" * 60)

# Observed quarterly YoY revenue growth rates
growth_data = np.array([0.082, 0.074, 0.091, 0.068, 0.055, 0.101, 0.079, 0.072])
n = len(growth_data)
y_bar = growth_data.mean()

# Prior hyperparameters — sector-level structural prior
mu_0 = 0.07     # sector median growth rate
tau_0 = 0.04    # prior standard deviation — fairly diffuse

# Assumed observation noise (known for now — relaxed in Chapter 3)
sigma = 0.025

# Analytical posterior (Normal-Normal conjugate)
prior_precision = 1 / tau_0**2
data_precision = n / sigma**2
post_precision = prior_precision + data_precision
tau_n = np.sqrt(1 / post_precision)

mu_n = (prior_precision * mu_0 + data_precision * y_bar) / post_precision

post_ci_low = stats.norm.ppf(0.025, mu_n, tau_n)
post_ci_high = stats.norm.ppf(0.975, mu_n, tau_n)
p_above_8pct = 1 - stats.norm.cdf(0.08, mu_n, tau_n)

print(f"\nPrior:               Normal({mu_0:.2%}, sigma={tau_0:.2%})")
print(f"Observed mean:       {y_bar:.2%}  (n={n} quarters)")
print(f"Posterior mean:      {mu_n:.2%}")
print(f"Posterior std:       {tau_n:.2%}")
print(f"95% credible int:    [{post_ci_low:.2%}, {post_ci_high:.2%}]")
print(f"P(growth > 8%):      {p_above_8pct:.1%}")

# Prior weight vs data weight
prior_weight = prior_precision / post_precision
data_weight = data_precision / post_precision
print(f"\nPrior weight:        {prior_weight:.1%}")
print(f"Data weight:         {data_weight:.1%}")


# ---------------------------------------------------------------------------
# EXAMPLE 2 — Operating Margin Estimation
# ---------------------------------------------------------------------------

print("\n" + "=" * 60)
print("EXAMPLE 2: Operating Margin Estimation")
print("=" * 60)

margin_data = np.array([0.183, 0.201, 0.195, 0.178, 0.212, 0.190])
n_m = len(margin_data)
y_bar_m = margin_data.mean()

# Prior: SaaS sector median margin ~20%, moderate confidence
mu_0_m = 0.20
tau_0_m = 0.05
sigma_m = 0.015

prior_prec_m = 1 / tau_0_m**2
data_prec_m = n_m / sigma_m**2
post_prec_m = prior_prec_m + data_prec_m
tau_n_m = np.sqrt(1 / post_prec_m)
mu_n_m = (prior_prec_m * mu_0_m + data_prec_m * y_bar_m) / post_prec_m

print(f"\nPrior:               Normal({mu_0_m:.2%}, sigma={tau_0_m:.2%})")
print(f"Observed mean:       {y_bar_m:.2%}  (n={n_m} quarters)")
print(f"Posterior mean:      {mu_n_m:.2%}")
print(f"95% credible int:    [{stats.norm.ppf(0.025, mu_n_m, tau_n_m):.2%}, "
      f"{stats.norm.ppf(0.975, mu_n_m, tau_n_m):.2%}]")


# ---------------------------------------------------------------------------
# PyMC version — growth rate model
# ---------------------------------------------------------------------------

with pm.Model() as growth_model:
    mu_growth = pm.Normal("mu_growth", mu=mu_0, sigma=tau_0)
    sigma_growth = pm.HalfNormal("sigma_growth", sigma=sigma)
    obs = pm.Normal("obs", mu=mu_growth, sigma=sigma_growth, observed=growth_data)
    trace = pm.sample(2000, tune=1000, target_accept=0.9,
                      return_inferencedata=True, progressbar=False)

pymc_samples = trace.posterior["mu_growth"].values.flatten()
print(f"\nPyMC posterior mean: {pymc_samples.mean():.2%}  (analytical: {mu_n:.2%})")


# ---------------------------------------------------------------------------
# PLOT
# ---------------------------------------------------------------------------

x = np.linspace(0.02, 0.14, 500)

fig, axes = plt.subplots(1, 2, figsize=(13, 4))

# Revenue growth
axes[0].plot(x, stats.norm.pdf(x, mu_0, tau_0), color='#6B8CCC',
             linewidth=2, linestyle='--', label=f'Prior: N({mu_0:.0%}, {tau_0:.0%})')
axes[0].plot(x, stats.norm.pdf(x, mu_n, tau_n), color='#1F3A7A',
             linewidth=2.5, label=f'Posterior: N({mu_n:.2%}, {tau_n:.2%})')
axes[0].hist(pymc_samples, bins=60, density=True, color='#1F3A7A',
             alpha=0.2, label='PyMC samples')
axes[0].axvline(mu_n, color='#C8960C', linewidth=2,
                label=f'Post. mean: {mu_n:.2%}')
axes[0].set_title('Revenue Growth Rate — Prior vs Posterior', fontweight='bold')
axes[0].set_xlabel('Growth Rate μ')
axes[0].xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
axes[0].legend(fontsize=9)

# Operating margin
x_m = np.linspace(0.10, 0.32, 500)
axes[1].plot(x_m, stats.norm.pdf(x_m, mu_0_m, tau_0_m), color='#6B8CCC',
             linewidth=2, linestyle='--', label=f'Prior: N({mu_0_m:.0%}, {tau_0_m:.0%})')
axes[1].plot(x_m, stats.norm.pdf(x_m, mu_n_m, tau_n_m), color='#2E7D32',
             linewidth=2.5, label=f'Posterior: N({mu_n_m:.2%}, {tau_n_m:.2%})')
axes[1].axvline(mu_n_m, color='#C8960C', linewidth=2,
                label=f'Post. mean: {mu_n_m:.2%}')
axes[1].set_title('Operating Margin — Prior vs Posterior', fontweight='bold')
axes[1].set_xlabel('Operating Margin μ')
axes[1].xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
axes[1].legend(fontsize=9)

plt.tight_layout()
plt.savefig("normal_normal_posteriors.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nPlot saved to normal_normal_posteriors.png")
