"""
joint_growth_margin_model.py
----------------------------
Chapter 3 — Introduction to Multiparameter Models

What it does:
    Implements a joint Bayesian model for simultaneous estimation of revenue
    growth rate and operating margin using the multivariate Normal framework
    from Section 3.6. Both parameters are estimated together with a full
    posterior covariance structure — capturing the correlation between them.

    The posterior samples are then used to generate a distribution over
    DCF terminal value, demonstrating how correlated parameter uncertainty
    flows into the valuation output.

Dependencies:
    pip install pymc arviz numpy matplotlib scipy
"""

import numpy as np
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


# ---------------------------------------------------------------------------
# DATA
# Observed quarterly (growth rate, operating margin) pairs
# ---------------------------------------------------------------------------

# Each row: [revenue_growth, operating_margin] for one quarter
observed_data = np.array([
    [0.082, 0.191],   # Q1 2022
    [0.074, 0.183],   # Q2 2022
    [0.091, 0.201],   # Q3 2022
    [0.068, 0.178],   # Q4 2022
    [0.055, 0.172],   # Q1 2023
    [0.101, 0.212],   # Q2 2023
    [0.079, 0.195],   # Q3 2023
    [0.072, 0.188],   # Q4 2023
])

n = len(observed_data)
y_bar = observed_data.mean(axis=0)
print(f"Sample mean growth:  {y_bar[0]:.2%}")
print(f"Sample mean margin:  {y_bar[1]:.2%}")
print(f"Sample correlation:  {np.corrcoef(observed_data.T)[0,1]:.3f}")


# ---------------------------------------------------------------------------
# MODEL
# Joint Bayesian model for growth rate and operating margin
# Section 3.6 — Normal with unknown mean and covariance
# ---------------------------------------------------------------------------

with pm.Model() as joint_model:

    # --- PRIORS ---
    # Revenue growth: sector median ~7%, weakly informative
    mu_growth = pm.Normal("mu_growth", mu=0.07, sigma=0.04)

    # Operating margin: SaaS sector median ~20%, weakly informative
    mu_margin = pm.Normal("mu_margin", mu=0.20, sigma=0.05)

    # Correlation between growth and margin
    # Using LKJ prior — the standard prior for correlation matrices in PyMC
    # eta=2 gives a mild regularization toward independence
    corr_matrix, stds = pm.LKJCholeskyCov(
        "chol", n=2, eta=2.0, sd_dist=pm.HalfNormal.dist(sigma=0.03)
    )
    cov_matrix = pm.Deterministic("cov", corr_matrix.dot(corr_matrix.T))

    # --- LIKELIHOOD ---
    # Joint normal — both parameters estimated simultaneously
    mu_vec = pm.math.stack([mu_growth, mu_margin])
    obs = pm.MvNormal("obs", mu=mu_vec, chol=corr_matrix, observed=observed_data)

    # --- POSTERIOR ---
    trace = pm.sample(2000, tune=1000, target_accept=0.9,
                      return_inferencedata=True, progressbar=True)


# ---------------------------------------------------------------------------
# DIAGNOSTICS
# ---------------------------------------------------------------------------

print("\n--- Convergence Diagnostics ---")
print(az.summary(trace, var_names=["mu_growth", "mu_margin"]))


# ---------------------------------------------------------------------------
# RESULTS
# ---------------------------------------------------------------------------

post_growth = trace.posterior["mu_growth"].values.flatten()
post_margin = trace.posterior["mu_margin"].values.flatten()
post_corr = trace.posterior["cov"].values.reshape(-1, 2, 2)[:, 0, 1] / (
    np.sqrt(trace.posterior["cov"].values.reshape(-1, 2, 2)[:, 0, 0]) *
    np.sqrt(trace.posterior["cov"].values.reshape(-1, 2, 2)[:, 1, 1])
)

print(f"\n--- Posterior: Revenue Growth Rate ---")
print(f"  Mean:     {post_growth.mean():.2%}")
print(f"  95% CI:   [{np.percentile(post_growth, 2.5):.2%}, {np.percentile(post_growth, 97.5):.2%}]")

print(f"\n--- Posterior: Operating Margin ---")
print(f"  Mean:     {post_margin.mean():.2%}")
print(f"  95% CI:   [{np.percentile(post_margin, 2.5):.2%}, {np.percentile(post_margin, 97.5):.2%}]")

print(f"\n--- Posterior: Growth-Margin Correlation ---")
print(f"  Mean:     {post_corr.mean():.3f}")
print(f"  95% CI:   [{np.percentile(post_corr, 2.5):.3f}, {np.percentile(post_corr, 97.5):.3f}]")


# ---------------------------------------------------------------------------
# DCF TERMINAL VALUE DISTRIBUTION
# Using posterior samples to generate intrinsic value distribution
# Simplified DCF: TV = (Margin * Revenue * (1 + growth)) / (WACC - growth)
# ---------------------------------------------------------------------------

BASE_REVENUE = 500      # $500M base revenue
WACC = 0.10             # fixed WACC for this example

# Generate terminal value distribution from correlated posterior samples
tv_samples = (post_margin * BASE_REVENUE * (1 + post_growth)) / (WACC - post_growth)

# Filter out scenarios where growth >= WACC (terminal value undefined)
valid = tv_samples[post_growth < WACC]

print(f"\n--- DCF Terminal Value Distribution (base revenue = ${BASE_REVENUE}M) ---")
print(f"  Median TV:      ${np.median(valid):.0f}M")
print(f"  Mean TV:        ${np.mean(valid):.0f}M")
print(f"  90% CI:         [${np.percentile(valid, 5):.0f}M, ${np.percentile(valid, 95):.0f}M]")
print(f"  P(TV > $2000M): {(valid > 2000).mean():.1%}")
print(f"  P(TV < $1000M): {(valid < 1000).mean():.1%}")


# ---------------------------------------------------------------------------
# PLOT
# ---------------------------------------------------------------------------

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Growth vs Margin scatter — joint posterior
axes[0].scatter(post_growth[::10], post_margin[::10], alpha=0.15,
                s=8, color='#1F3A7A')
axes[0].set_title('Joint Posterior:\nGrowth vs. Margin', fontweight='bold')
axes[0].set_xlabel('Revenue Growth Rate')
axes[0].set_ylabel('Operating Margin')
axes[0].xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
axes[0].yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
corr_text = f"Post. correlation: {post_corr.mean():.2f}"
axes[0].text(0.05, 0.95, corr_text, transform=axes[0].transAxes,
             fontsize=9, verticalalignment='top', color='#C8960C', fontweight='bold')

# Marginal posteriors
axes[1].hist(post_growth, bins=60, color='#1F3A7A', alpha=0.8, density=True)
axes[1].axvline(post_growth.mean(), color='#C8960C', linewidth=2,
                label=f'Mean: {post_growth.mean():.2%}')
axes[1].set_title('Marginal Posterior:\nRevenue Growth Rate', fontweight='bold')
axes[1].set_xlabel('Growth Rate')
axes[1].xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
axes[1].legend(fontsize=9)

# Terminal value distribution
axes[2].hist(valid, bins=80, color='#2E7D32', alpha=0.8, edgecolor='white', linewidth=0.2)
axes[2].axvline(np.median(valid), color='#C8960C', linewidth=2,
                label=f'Median: ${np.median(valid):.0f}M')
axes[2].axvline(np.percentile(valid, 5), color='gray', linewidth=1.5,
                linestyle='--', label='90% CI')
axes[2].axvline(np.percentile(valid, 95), color='gray', linewidth=1.5, linestyle='--')
axes[2].set_title('DCF Terminal Value\nDistribution', fontweight='bold')
axes[2].set_xlabel('Terminal Value ($M)')
axes[2].legend(fontsize=9)

plt.tight_layout()
plt.savefig("joint_dcf_model.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nPlot saved to joint_dcf_model.png")
