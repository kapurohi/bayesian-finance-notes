# 5.2 — Exchangeability and Its Role in Hierarchical Models

## What this section is doing

Gelman formalizes the assumption that makes hierarchical models valid: **exchangeability**. This was introduced briefly in Section 1.2. Here it gets its full treatment as the foundational justification for pooling information across units.

---

## Simplification

Exchangeability means: before you look at the data, you have no reason to believe any one unit is systematically different from the others. You might believe they are all different — but you don't believe unit 7 is special in a way you could have predicted before seeing the data.

If that's true, then observing data from unit 7 gives you information about all the other units too — because they're all drawn from the same population distribution. That information sharing is exactly what hierarchical models implement.

---

## Formal definition

A sequence of random variables $\theta_1, \ldots, \theta_J$ is **exchangeable** if their joint distribution is invariant to permutation:

$$p(\theta_1, \ldots, \theta_J) = p(\theta_{\pi(1)}, \ldots, \theta_{\pi(J)})$$

for any permutation $\pi$.

**De Finetti's theorem** states that any exchangeable sequence can be represented as a mixture of independent and identically distributed (i.i.d.) draws from some population distribution. This theorem is the mathematical foundation of hierarchical models — it says that assuming exchangeability is equivalent to assuming the hierarchical structure.

---

## When exchangeability is reasonable in finance

Exchangeability across companies is reasonable when:
- Companies are in the same sector and business model class
- You have no specific prior reason to rank them before seeing the data
- The goal is to estimate population-level patterns as well as individual company parameters

Exchangeability is **not** reasonable when:
- Companies differ by a known, observable characteristic you want to model explicitly (size, geography, age) — in this case, you should condition on those characteristics in the model
- You have strong prior information that distinguishes specific companies

When exchangeability doesn't hold unconditionally, it often holds conditionally — companies may not be exchangeable across sectors, but within the same sector they may be. This leads to nested hierarchical models.

---

## See also

- Section 1.2 for the first introduction of exchangeability
- Section 5.1 for the hierarchical structure that exchangeability justifies
- Section 5.7 for variance components models that decompose the exchangeability structure
