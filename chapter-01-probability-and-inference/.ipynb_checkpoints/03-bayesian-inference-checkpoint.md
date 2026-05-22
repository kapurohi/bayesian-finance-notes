# 1.3 — Bayesian Inference

## What this section is doing

This is the mechanical heart of the chapter. Gelman derives Bayes' rule — the actual equation that performs the update from prior to posterior — and explains why the normalizing constant in the denominator is almost always dropped in practice. If you only deeply understand one thing from Chapter 1, make it this.

---

## The Analogy

You're a doctor trying to figure out how sick a patient is based on a single symptom — say, a fever.

You start with a general belief about how common a particular illness is in the general population. In Mumbai during monsoon season, maybe 1 in 50 people has a specific viral infection at any given time. That's your **prior** — background knowledge before you examine the patient.

You then observe that the patient has a fever of 102°F. You ask: *if this patient actually had that infection, how likely would it be for them to have a 102° fever?* That probability — fever given infection — is your **likelihood**.

You multiply those two things together: prior probability of infection times likelihood of this fever given infection. The result, once scaled so everything adds up to 100%, is your **posterior** — your updated belief about how sick this specific patient is, given this specific symptom.

The denominator in Bayes' rule — the total probability of seeing a 102° fever regardless of cause — is just the scaling factor that makes the probabilities sum to 1. In practice, modern sampling algorithms bypass computing it entirely.

---

## Bayes' Rule

Starting from the definition of conditional probability:

$$p(\theta \mid y) = \frac{p(\theta) \cdot p(y \mid \theta)}{p(y)}$$

Breaking this down piece by piece:

- **$p(\theta \mid y)$** — the posterior. What we want. The distribution over $\theta$ after seeing data $y$.
- **$p(\theta)$** — the prior. What we believed before seeing $y$.
- **$p(y \mid \theta)$** — the likelihood. How probable is data $y$ given a specific value of $\theta$.
- **$p(y)$** — the marginal likelihood or normalizing constant. The total probability of observing $y$ across all possible values of $\theta$.

The denominator $p(y)$ is computed as:

$$p(y) = \int p(\theta) \cdot p(y \mid \theta) \, d\theta$$

For continuous parameters, this integral is almost always analytically intractable — meaning you can't solve it with pen and paper. This is why MCMC exists (Section 1.9).

---

## The proportional form — why the denominator gets dropped

Since $p(y)$ doesn't depend on $\theta$ — it's just a constant — it doesn't affect the shape of the posterior distribution. So in practice, Gelman writes:

$$p(\theta \mid y) \propto p(\theta) \cdot p(y \mid \theta)$$

The $\propto$ symbol means "proportional to." The posterior is proportional to prior times likelihood. The normalizing constant just scales the whole thing so it integrates to 1, but it doesn't change which values of $\theta$ are more or less probable relative to each other.

This simplification is huge in practice. MCMC samplers (PyMC, Stan) only need the unnormalized posterior — they never compute $p(y)$ at all.

---

## Two important derived quantities

**The posterior predictive distribution:**

$$p(\tilde{y} \mid y) = \int p(\tilde{y} \mid \theta) \cdot p(\theta \mid y) \, d\theta$$

This is the distribution over future observations $\tilde{y}$, averaged over all plausible values of $\theta$ weighted by the posterior. In financial modeling, this is what you actually serve to clients — not a point estimate, but a full distribution over next quarter's revenue or next year's free cash flow.

**Conjugate priors:**

When the prior $p(\theta)$ and the likelihood $p(y \mid \theta)$ are chosen so that the posterior $p(\theta \mid y)$ belongs to the same distribution family as the prior, the prior is called **conjugate** to the likelihood.

For example: a Beta prior combined with a Binomial likelihood produces a Beta posterior. A Normal prior combined with a Normal likelihood produces a Normal posterior.

Conjugate priors are computationally convenient — the posterior can be computed analytically without MCMC. They're the first models you'll implement in Chapter 2.

---

## Why this matters for financial modeling

The posterior update equation is the engine your platform runs on.

Every time a new earnings report drops, you run:

$$p(\theta \mid y_{\text{new}}) \propto p(\theta \mid y_{\text{old}}) \cdot p(y_{\text{new}} \mid \theta)$$

Today's posterior becomes tomorrow's prior. The model never needs to be rebuilt from scratch — it just updates. This is sequential Bayesian updating, and it's what makes a Bayesian financial platform genuinely dynamic rather than a static snapshot.

The posterior predictive $p(\tilde{y} \mid y)$ is what turns parameter uncertainty into forecast uncertainty — and that forecast uncertainty is what gets displayed to clients as a distribution over intrinsic value, not a single number.

---

## See also

- [Notation Reference](../resources/notation-reference.md) for symbol definitions
- Section 1.9 for how MCMC computes the posterior without solving the integral
- Chapter 2 for conjugate models worked through in full
