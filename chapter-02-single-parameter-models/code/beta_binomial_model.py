"""
beta_binomial_model.py
----------------------
Chapter 2 — Single-Parameter Models

What it does:
    Implements the Beta-Binomial conjugate model for estimating a probability
    from count data. Two financial examples are included:
    - Default probability estimation from a bond portfolio
    - Sales conversion rate estimation from a deal pipeline

    The Beta-Binomial has a closed-form posterior so MCMC is not required,
    but PyMC is used here to demonstrate the modeling pattern and to enable
    extension to non-conjugate settings.

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
# EXAMPLE 1 — Default Probability Estimation
# ---------------------------------------------------------------------------

print("=" * 60)
print("EXAMPLE 1: Default Probability — Investment Grade Portfolio")
print("=" * 60)

# Observed data
n_bonds = 50        # total bonds in portfolio
y_defaults = 2      # observed defaults

# Prior hyperparameters — sector-level IG default history
# Historical IG default rate ~2%, encoded with effective sample size of 100
alpha_prior = 2.0
beta_prior = 98.0

# Analytical posterior (conjugate update — no MCMC needed)
alpha_post = alpha_prior + y_defaults
beta_post = beta_prior + (n_bonds - y_defaults)

prior_mean = alpha_prior / (alpha_prior + beta_prior)
post_mean = alpha_post / (alpha_post + beta_post)
post_ci_low = stats.beta.ppf(0.025, alpha_post, beta_post)
post_ci_high = stats.beta.ppf(0.975, alpha_post, beta_post)
p_above_5pct = 1 - stats.beta.cdf(0.05, alpha_post, beta_post)

print(f"\nPrior:               Beta({alpha_prior}, {beta_prior})")
print(f"Prior mean:          {prior_mean:.2%}")
print(f"Observed:            {y_defaults} defaults in {n_bonds} bonds")
print(f"Posterior:           Beta({alpha_post}, {beta_post})")
print(f"Posterior mean:      {post_mean:.2%}")
print(f"95% credible int:    [{post_ci_low:.2%}, {post_ci_high:.2%}]")
print(f"P(theta > 5%):       {p_above_5pct:.1%}")

# PyMC version — same model, demonstrates the modeling pattern
with pm.Model() as default_model:
    theta = pm.Beta("theta", alpha=alpha_prior, beta=beta_prior)
    obs = pm.Binomial("obs", n=n_bonds, p=theta, observed=y_defaults)
    trace_default = pm.sample(2000, tune=1000, target_accept=0.9,
                              return_inferencedata=True, progressbar=False)

theta_samples = trace_default.posterior["theta"].values.flatten()


# ---------------------------------------------------------------------------
# EXAMPLE 2 — Sales Conversion Rate
# ---------------------------------------------------------------------------

print("\n" + "=" * 60)
print("EXAMPLE 2: Sales Conversion Rate — Deal Pipeline")
print("=" * 60)

n_deals = 30        # deals in pipeline
y_closed = 8        # deals closed

# Prior: industry benchmark conversion ~25%, moderate confidence
alpha_sales = 3.0
beta_sales = 9.0

alpha_sales_post = alpha_sales + y_closed
beta_sales_post = beta_sales + (n_deals - y_closed)

sales_post_mean = alpha_sales_post / (alpha_sales_post + beta_sales_post)
sales_ci_low = stats.beta.ppf(0.025, alpha_sales_post, beta_sales_post)
sales_ci_high = stats.beta.ppf(0.975, alpha_sales_post, beta_sales_post)

print(f"\nPrior:               Beta({alpha_sales}, {beta_sales})")
print(f"Prior mean:          {alpha_sales/(alpha_sales+beta_sales):.2%}")
print(f"Observed:            {y_closed} closed in {n_deals} deals")
print(f"Posterior:           Beta({alpha_sales_post}, {beta_sales_post})")
print(f"Posterior mean:      {sales_post_mean:.2%}")
print(f"95% credible int:    [{sales_ci_low:.2%}, {sales_ci_high:.2%}]")


# ---------------------------------------------------------------------------
# PLOT
# ---------------------------------------------------------------------------

theta_range = np.linspace(0, 0.20, 500)

fig, axes = plt.subplots(1, 2, figsize=(13, 4))

# Default probability plot
prior_pdf = stats.beta.pdf(theta_range, alpha_prior, beta_prior)
post_pdf = stats.beta.pdf(theta_range, alpha_post, beta_post)

axes[0].plot(theta_range, prior_pdf, color='#6B8CCC', linewidth=2,
             linestyle='--', label=f'Prior: Beta({alpha_prior}, {beta_prior})')
axes[0].plot(theta_range, post_pdf, color='#1F3A7A', linewidth=2.5,
             label=f'Posterior: Beta({alpha_post}, {beta_post})')
axes[0].axvline(post_mean, color='#C8960C', linewidth=2,
                label=f'Post. mean: {post_mean:.2%}')
axes[0].fill_between(theta_range, post_pdf,
                     where=(theta_range >= post_ci_low) & (theta_range <= post_ci_high),
                     alpha=0.15, color='#1F3A7A')
axes[0].set_title('Default Probability — Prior vs Posterior', fontweight='bold')
axes[0].set_xlabel('Default Probability θ')
axes[0].xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
axes[0].legend(fontsize=9)

# Conversion rate plot
theta_range2 = np.linspace(0, 0.70, 500)
prior_pdf2 = stats.beta.pdf(theta_range2, alpha_sales, beta_sales)
post_pdf2 = stats.beta.pdf(theta_range2, alpha_sales_post, beta_sales_post)

axes[1].plot(theta_range2, prior_pdf2, color='#6B8CCC', linewidth=2,
             linestyle='--', label=f'Prior: Beta({alpha_sales}, {beta_sales})')
axes[1].plot(theta_range2, post_pdf2, color='#2E7D32', linewidth=2.5,
             label=f'Posterior: Beta({alpha_sales_post}, {beta_sales_post})')
axes[1].axvline(sales_post_mean, color='#C8960C', linewidth=2,
                label=f'Post. mean: {sales_post_mean:.2%}')
axes[1].set_title('Sales Conversion Rate — Prior vs Posterior', fontweight='bold')
axes[1].set_xlabel('Conversion Rate θ')
axes[1].xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
axes[1].legend(fontsize=9)

plt.tight_layout()
plt.savefig("beta_binomial_posteriors.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nPlot saved to beta_binomial_posteriors.png")
