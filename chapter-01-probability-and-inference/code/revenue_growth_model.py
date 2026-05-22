"""
revenue_growth_model.py
-----------------------
Chapter 1 — Bayesian Data Analysis (BDA3)

This is the Chapter 1 production model implementation.

What it does:
    Estimates a company's true underlying revenue growth rate as a posterior
    distribution, given a structural sector-level prior and observed quarterly
    revenue growth data. Implements the full three-step Bayesian loop from
    Section 1.1 and the sequential update architecture from Section 1.6.

Dependencies:
    pip install pymc arviz numpy matplotlib
"""

import numpy as np
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# DATA
# Observed quarterly revenue growth rates — replace with real data
# These are year-over-year growth rates per quarter
# ---------------------------------------------------------------------------

COMPANY_TICKER = "EXAMPLE_CO"

revenue_growth_observed = np.array([
    0.082,  # Q1 2022
    0.074,  # Q2 2022
    0.091,  # Q3 2022
    0.068,  # Q4 2022
    0.055,  # Q1 2023
    0.101,  # Q2 2023
    0.079,  # Q3 2023
    0.072,  # Q4 2023
])


# ---------------------------------------------------------------------------
# PRIOR HYPERPARAMETERS
# These encode the structural sector-level prior (Section 1.6)
# Change these to reflect the specific sector you're modeling
# ---------------------------------------------------------------------------

SECTOR_MEDIAN_GROWTH = 0.07     # 7% — sector median revenue growth
SECTOR_GROWTH_SPREAD = 0.03     # 3% — how wide the sector distribution is
SECTOR_VOL_PRIOR     = 0.02     # 2% — prior belief on idiosyncratic noise


# ---------------------------------------------------------------------------
# MODEL
# ---------------------------------------------------------------------------

with pm.Model() as revenue_growth_model:

    # STEP 1: Prior — structural belief from sector data (Section 1.6)
    # mu_growth is the unknown true underlying growth rate
    # We believe it is normally distributed around the sector median
    mu_growth = pm.Normal(
        "mu_growth",
        mu=SECTOR_MEDIAN_GROWTH,
        sigma=SECTOR_GROWTH_SPREAD,
    )

    # sigma_growth is the idiosyncratic quarter-to-quarter noise
    # HalfNormal because standard deviations must be positive
    sigma_growth = pm.HalfNormal(
        "sigma_growth",
        sigma=SECTOR_VOL_PRIOR,
    )

    # STEP 2: Likelihood — how probable are the observed quarterly figures
    # given the latent true growth rate? (Section 1.3)
    observed = pm.Normal(
        "observed",
        mu=mu_growth,
        sigma=sigma_growth,
        observed=revenue_growth_observed,
    )

    # STEP 3: Posterior — sample the full updated belief distribution
    # NUTS runs automatically. target_accept=0.9 reduces divergences.
    trace = pm.sample(
        draws=2000,
        tune=1000,
        target_accept=0.9,
        return_inferencedata=True,
        progressbar=True,
    )

    # Posterior predictive — generate forward revenue scenarios (Section 1.10)
    # This is the direct input to the DCF terminal value distribution
    posterior_predictive = pm.sample_posterior_predictive(trace)


# ---------------------------------------------------------------------------
# DIAGNOSTICS
# Always check convergence before trusting any output (Section 1.9)
# R-hat should be less than 1.01 for all parameters
# ---------------------------------------------------------------------------

print("\n--- Convergence Diagnostics ---")
print(az.summary(trace, var_names=["mu_growth", "sigma_growth"]))

# Check R-hat explicitly
rhat = az.rhat(trace)
print(f"\nR-hat mu_growth:    {float(rhat['mu_growth'].values):.4f}  (should be < 1.01)")
print(f"R-hat sigma_growth: {float(rhat['sigma_growth'].values):.4f}  (should be < 1.01)")


# ---------------------------------------------------------------------------
# RESULTS
# ---------------------------------------------------------------------------

posterior_mu = trace.posterior["mu_growth"].values.flatten()

print(f"\n--- Posterior: True Revenue Growth Rate for {COMPANY_TICKER} ---")
print(f"  Posterior mean:         {posterior_mu.mean():.2%}")
print(f"  Posterior median:       {np.median(posterior_mu):.2%}")
print(f"  90% credible interval:  [{np.percentile(posterior_mu, 5):.2%}, {np.percentile(posterior_mu, 95):.2%}]")
print(f"  P(growth > 8%):         {(posterior_mu > 0.08).mean():.1%}")
print(f"  P(growth > 5%):         {(posterior_mu > 0.05).mean():.1%}")
print(f"  P(growth < 3%):         {(posterior_mu < 0.03).mean():.1%}")


# ---------------------------------------------------------------------------
# PLOT
# ---------------------------------------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Posterior distribution
axes[0].hist(posterior_mu, bins=60, color="#1F3A7A", alpha=0.8, edgecolor="white", linewidth=0.3)
axes[0].axvline(posterior_mu.mean(), color="#C8960C", linewidth=2, label=f"Mean: {posterior_mu.mean():.2%}")
axes[0].axvline(np.percentile(posterior_mu, 5), color="gray", linewidth=1.5, linestyle="--", label="90% CI")
axes[0].axvline(np.percentile(posterior_mu, 95), color="gray", linewidth=1.5, linestyle="--")
axes[0].set_title(f"Posterior: True Growth Rate — {COMPANY_TICKER}", fontweight="bold")
axes[0].set_xlabel("Revenue Growth Rate")
axes[0].set_ylabel("Frequency")
axes[0].legend()
axes[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.0%}"))

# Posterior predictive — next quarter scenarios
ppc_samples = posterior_predictive.posterior_predictive["observed"].values.flatten()
axes[1].hist(ppc_samples, bins=60, color="#2E7D32", alpha=0.8, edgecolor="white", linewidth=0.3)
axes[1].axvline(np.median(ppc_samples), color="#C8960C", linewidth=2, label=f"Median: {np.median(ppc_samples):.2%}")
axes[1].set_title("Posterior Predictive: Next Quarter Revenue Growth", fontweight="bold")
axes[1].set_xlabel("Forecasted Growth Rate")
axes[1].set_ylabel("Frequency")
axes[1].legend()
axes[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.0%}"))

plt.tight_layout()
plt.savefig("revenue_growth_posterior.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nPlot saved to revenue_growth_posterior.png")
