# Chapter 1 — Probability and Inference

This chapter is the foundation. Gelman isn't teaching you any specific model here — he's installing the operating system that every model in the rest of the book runs on.

The core idea is simple: before you see any data, you have some belief about the world. After you see data, you update that belief. The Bayesian framework is the mathematically rigorous way of doing that update — and it turns out this simple idea has enormous consequences for how you build financial models.

By the end of this chapter, the three-step Bayesian workflow should feel completely natural. Everything in Chapters 2 and beyond is just a more sophisticated version of the same loop.

---

## Sections

| # | File | One-Line Summary |
|---|------|-----------------|
| 1.1 | [The Three Steps](./01-three-steps.md) | The entire Bayesian framework in three moves: prior → likelihood → posterior |
| 1.2 | [General Notation](./02-notation.md) | The vocabulary Gelman uses for the rest of the book |
| 1.3 | [Bayesian Inference](./03-bayesian-inference.md) | The actual update equation — Bayes' rule derived and explained |
| 1.4 | [Discrete Examples](./04-discrete-examples.md) | Why base rates dominate — even accurate signals can mislead |
| 1.5 | [Probability as Uncertainty](./05-probability-as-uncertainty.md) | Why Bayesian probability can apply to one-time financial events |
| 1.6 | [Genetic Inference Example](./06-genetic-example.md) | Using structural knowledge as a prior before data is available |
| 1.7 | [Spelling Correction Example](./07-spelling-correction.md) | The cleanest proof that Bayes applies to any inference problem |
| 1.8 | [Probability Theory Results](./08-probability-theory-results.md) | Reference toolkit — law of total probability, total expectation |
| 1.9 | [Computation and Software](./09-computation-and-software.md) | How MCMC makes Bayesian inference practically computable |
| 1.10 | [Bayesian Inference in Applied Statistics](./10-applied-statistics.md) | Why Bayesian models outperform frequentist approaches for real-world finance |

---

## End of Chapter

- [Financial Utility Summary](./financial-utility-summary.md) — every section mapped to a specific platform use case

---

## Code

| File | What it does |
|------|-------------|
| [revenue_growth_model.py](./code/revenue_growth_model.py) | Standalone PyMC model implementing the full Chapter 1 Bayesian update loop on quarterly revenue data |
| [chapter01_walkthrough.ipynb](./code/chapter01_walkthrough.ipynb) | Jupyter notebook walking through the model step by step with inline explanations |
