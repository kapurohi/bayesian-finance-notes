## What this section is doing

When a model fails a posterior predictive check or performs poorly on WAIC/LOO, the response is not to discard the model but to expand it. Gelman describes the systematic process of expanding a model to address specific identified failures.

---

## Simplification

A posterior predictive check reveals that your Normal growth model underestimates the frequency of large quarterly swings. The fix is to expand the model — replace the Normal likelihood with a Student-t, add a volatility regime component, or include a macro driver that explains the large swings. You don't start from scratch; you add structure to address the specific identified failure.

---

## Expansion strategies

**Likelihood expansion:** Replace Normal with Student-t to handle heavy tails. Add heteroscedasticity to handle time-varying volatility.

**Prior expansion:** Add a hierarchical level to share information across companies or time periods.

**Predictor expansion:** Add covariates (macro drivers, sector indicators) to explain systematic patterns in the residuals.

**Mixture expansion:** Add a mixture component to handle outlier-generating processes.

---

## Financial application

A model checking step reveals that a growth rate model systematically underestimates variance in periods following large macro shocks. The expansion adds a regime-switching component — a latent variable that distinguishes normal growth regimes from shock regimes — with different variance parameters in each regime. The expanded model is tested with new posterior predictive checks before deployment.

---

## See also

- Chapter 6 for the model checking diagnostics that motivate expansion
- Chapter 17 for robust models that handle heavy tails
- Chapter 22 for mixture models as an expansion strategy