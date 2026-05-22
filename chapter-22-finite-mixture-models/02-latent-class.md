# 22.2 — Latent Class and Mixture of Experts

## What this section is doing

**Latent class models** apply mixture models to categorical outcomes — each observation belongs to an unobserved class, and the response distribution depends on the class.

**Mixture of experts** allows the mixture weights to depend on predictors — different covariate values activate different component models.

---

## Financial application

**Customer segmentation:** Classify customers into latent behavioral segments based on transaction history. Each segment has its own default probability and revenue trajectory. Segment membership is probabilistic — the model gives a posterior probability of each customer belonging to each segment.

**Regime-dependent factor models:** A mixture of experts where the active factor model depends on observable macro conditions (the "gating variable"). In a low-rate environment, one factor structure is active; in a high-rate environment, another. The model learns when each regime is active from the data.
