# 15.5 — Meta-Analysis

## What this section is doing

Meta-analysis is the statistical combination of results from multiple independent studies. In the Bayesian framework, it is exactly a hierarchical model — each study estimates the same underlying effect with its own noise level, and the hierarchical prior pools information across studies to produce a combined estimate.

---

## Financial application

**Combining analyst estimates:** Multiple sell-side analysts each publish earnings estimates with different track records (noise levels). A Bayesian meta-analysis model combines them hierarchically — analysts with better historical accuracy get more weight, and the combined posterior estimate has less uncertainty than any individual estimate.

**Aggregating signals:** Combining multiple alpha signals (momentum, value, quality) where each signal has a different historical Sharpe ratio. The hierarchical model correctly weights each signal by its estimated precision and produces a combined signal with calibrated uncertainty.

---

## See also
- Chapter 5 Section 5.5 for the hierarchical Beta-Binomial model — the discrete analogue of meta-analysis
