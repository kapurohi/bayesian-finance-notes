# Chapter 16 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 16.1 — GLM Framework | Distribution + linear predictor + link function | The architecture for all non-Normal financial models. Binary default, count events, and positive continuous losses all fit the same GLM structure with different distribution and link choices. |
| 16.2 — Logistic Regression | Binary outcome probability as logistic function of predictors | Bayesian credit scoring and PD estimation. Posterior coefficient distributions identify genuine default predictors. Posterior predictive PD accounts for coefficient uncertainty. |
| 16.3 — Poisson Regression | Count outcomes as exponential function of predictors | Event frequency modeling — covenant violations, downgrades, trades. Negative binomial extension handles overdispersion. |
| 16.4 — Probit and Other Links | Alternative link functions for specific tail behaviors | Structural model-consistent credit modeling (probit). Rare event modeling (cloglog). Link function choice guided by the data-generating process. |

---

## Connection to Previous Chapters

Logistic regression is the non-conjugate model introduced in Chapter 3 Section 3.7 (the bioassay example). That section showed the general pattern: specify a Binomial likelihood with a logistic link and Normal priors on coefficients; the posterior has no closed form; MCMC handles it. Chapter 16 applies that pattern systematically to financial classification problems.
