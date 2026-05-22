# 20.1 — Splines and Smoothing

## What this section is doing

Splines are piecewise polynomial functions that provide flexible smooth fits to data. Bayesian spline models place priors on the spline coefficients that encourage smoothness — preventing overfitting while allowing the fit to follow genuine nonlinear patterns in the data.

---

## The model

Divide the predictor range into $K$ knot points. Between each pair of knots, fit a polynomial. Constrain the polynomials to be continuous and smooth at the knots. The result is a flexible curve that can capture any smooth relationship.

The Bayesian prior on spline coefficients is a **random walk prior** — adjacent coefficients are penalized for being too different. This is equivalent to penalized spline regression (P-splines) in the frequentist setting.

---

## Financial application

**Yield curve modeling:** Fit the yield curve (interest rates as a function of maturity) with a Bayesian spline. The smooth prior prevents overfitting to specific maturities. The posterior gives a distribution over the entire yield curve shape — including uncertainty in the short end, long end, and any inversion features.

**Nonlinear factor effects:** A stock's return may have a nonlinear relationship with its valuation ratio — cheap stocks outperform, but extremely cheap stocks may be value traps. A Bayesian spline captures this curvature with proper uncertainty.
