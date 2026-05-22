# 1.1 — The Three Steps of Bayesian Data Analysis

## What this section is doing

Gelman opens by saying that every Bayesian analysis — no matter how complex it gets later in the book — always runs the same three steps in the same order. This section defines those steps. Everything else in BDA3 is a specialization of this loop.

---

## The Analogy

Imagine you're a talent scout deciding whether to sign a 16-year-old footballer.

**Step 1 — Before you watch him play**, you already have a belief. You know which academy he trained at, you've heard from other scouts, you know his age and position. You haven't seen him touch a ball yet, but you're not completely in the dark either. This is your **prior** — your belief before you see new evidence.

**Step 2 — You watch him play 10 matches.** He scores 7 goals, makes good decisions under pressure, holds his position well. This is the data you actually observed. The question this data answers is: *how likely is this performance level, given that I think he's a particular quality of player?* That's the **likelihood** — a measure of how well your current belief explains the data.

**Step 3 — You combine your gut feeling with what you watched** and arrive at a sharper, updated opinion about whether to sign him. This updated opinion is your **posterior** — your belief after combining prior knowledge with observed evidence.

That's the entire framework. Every chapter in this book is just a more rigorous, more complex version of this same three-step loop.

---

## The Three Steps, Formally

**Step 1: Set up the prior distribution**

$$p(\theta)$$

This encodes what you believe about the unknown quantity $\theta$ before observing any data. In finance, $\theta$ might be a company's long-run revenue growth rate. You might say: *I believe it's probably somewhere between 3% and 15%, most likely around 7%.* That belief gets encoded as a probability distribution.

**Step 2: Construct the likelihood**

$$p(y \mid \theta)$$

This asks: *if $\theta$ were a specific value, how probable is the data $y$ that I actually observed?* You don't pick one value of $\theta$ — you evaluate this across all plausible values. In finance: *if the true growth rate were 7%, how likely is it that I'd observe this particular quarterly earnings report?*

**Step 3: Compute the posterior**

$$p(\theta \mid y) \propto p(\theta) \cdot p(y \mid \theta)$$

Multiply the prior by the likelihood. The result, once normalized, is the posterior — your updated belief about $\theta$ after seeing the data. The $\propto$ symbol means "proportional to," which is just saying the normalizing constant (the denominator in Bayes' rule) is being dropped for now because it doesn't change the shape of the distribution.

---

## Breaking down the posterior equation

$$p(\theta \mid y) \propto p(\theta) \cdot p(y \mid \theta)$$

Reading it left to right:

- **$p(\theta \mid y)$** — *posterior*. The probability distribution over $\theta$ given that we observed $y$. This is what we want.
- **$\propto$** — proportional to. The actual equality involves dividing by $p(y)$, but since $p(y)$ is just a constant (it doesn't depend on $\theta$), it only scales the distribution and doesn't affect its shape.
- **$p(\theta)$** — *prior*. What we believed before seeing data.
- **$p(y \mid \theta)$** — *likelihood*. How probable is the data, given a specific value of $\theta$.

The update is just multiplication. Prior belief times data evidence equals updated belief.

---

## Why this matters for financial modeling

A traditional DCF model hard-codes a single revenue growth rate — say 8% — and treats it as truth. When the next earnings report comes in at 3%, the model doesn't update. It has no mechanism to.

The three-step Bayesian loop gives a financial model a living architecture:

1. You encode a **prior** distribution over revenue growth — say, normally distributed around 7% with meaningful uncertainty
2. Each new earnings release is a **likelihood** signal
3. The **posterior** is the model's updated view — automatically recalibrated, never broken by a surprise

This is what separates a Bayesian financial platform from a Bloomberg Excel template.

---

## See also

- [Notation Reference](../resources/notation-reference.md) for definitions of $\theta$, $y$, $p(\theta)$, $p(y \mid \theta)$, $p(\theta \mid y)$
- Section 1.3 for the full derivation of Bayes' rule
