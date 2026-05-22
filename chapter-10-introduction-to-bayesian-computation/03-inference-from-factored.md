# 10.3 — Inference from Factored Distributions

## What this section is doing

When the joint posterior factors into independent components — or nearly independent components — you can sample from each factor separately and combine. This section covers how to identify and exploit factorization structure to make sampling more efficient.

---

## Financial application

In a hierarchical model, the company-level parameters $\theta_j$ are conditionally independent given the hyperparameters $\mu$ and $\tau$. This factorization can be exploited in Gibbs sampling: alternate between sampling the hyperparameters and sampling each company parameter independently in parallel.

For a coverage universe of 100 companies, conditional independence means the company-level sampling step is embarrassingly parallelizable — each company's posterior can be updated simultaneously given the current hyperparameter values.

---

## See also
- Chapter 11 for Gibbs sampling that exploits conditional independence
