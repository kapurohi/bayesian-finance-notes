# Chapter 19 — Financial Utility Summary

## Section-by-Section Map

| Section | Core Concept | Platform Application |
|---------|-------------|----------------------|
| 19.1 — Nonlinear Regression | Any known functional form can be the mean function | Exponential growth models, S-curve adoption models, mean-reversion models. MCMC handles nonlinearity automatically. |
| 19.2 — Nonlinear Examples | DCF as a parametric nonlinear model | The DCF formula is a nonlinear function of parameters — evaluated at posterior samples to produce a posterior distribution over intrinsic value. No additional modeling needed beyond the parameter posteriors from earlier chapters. |

---

## Connection to Previous Chapters

The posterior simulation approach from Chapter 10 Section 10.2 makes nonlinear models tractable: given posterior samples of the parameters, evaluate any nonlinear function (including the DCF formula) at each sample. The collection of outputs is the posterior distribution over that function. This is the computational implementation of coherent uncertainty propagation discussed in Chapter 1 Section 1.10.
