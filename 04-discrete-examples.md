# 1.4 — Discrete Probability Examples

## What this section is doing

Gelman works through concrete examples with discrete outcomes — most famously a medical diagnostic test — to show how prior probabilities reshape posterior conclusions in ways that are deeply counterintuitive. The lesson: even a highly accurate signal can produce mostly false positives when the prior probability of the event is very low. This is called the base rate problem, and it shows up constantly in financial modeling.

---

## The Analogy

Imagine a COVID test that is 99% accurate — meaning if you have COVID, it correctly identifies you 99% of the time, and if you don't have COVID, it correctly clears you 99% of the time.

Now imagine the city you're in has a very low prevalence — only 1 in 1,000 people actually has COVID right now.

You test positive. What's the probability you actually have COVID?

Most people guess somewhere around 99%. The correct answer is roughly **9%**.

Here's why: out of every 1,000 people tested, only 1 actually has COVID. That 1 person almost certainly tests positive (99% accuracy). But the other 999 people without COVID — 1% of them will also test positive. That's about 10 false positives. So out of roughly 11 positive tests, only 1 is a true positive. The prior probability (1 in 1,000) is so low that it dominates even a highly accurate test.

The prior pulled the posterior down hard. Base rates matter enormously.

---

## The Math

Let's define:

- $\theta = 1$ means the person has the disease; $\theta = 0$ means they don't
- $y = 1$ means the test is positive; $y = 0$ means the test is negative
- Prior: $p(\theta = 1) = 0.001$ (1 in 1,000 prevalence)
- Sensitivity: $p(y = 1 \mid \theta = 1) = 0.99$ (true positive rate)
- False positive rate: $p(y = 1 \mid \theta = 0) = 0.01$

Applying Bayes' rule:

$$p(\theta = 1 \mid y = 1) = \frac{p(\theta = 1) \cdot p(y = 1 \mid \theta = 1)}{p(y = 1)}$$

The denominator uses the law of total probability:

$$p(y = 1) = p(\theta = 1) \cdot p(y = 1 \mid \theta = 1) + p(\theta = 0) \cdot p(y = 1 \mid \theta = 0)$$

$$= 0.001 \times 0.99 + 0.999 \times 0.01 = 0.00099 + 0.00999 = 0.01098$$

So the posterior:

$$p(\theta = 1 \mid y = 1) = \frac{0.001 \times 0.99}{0.01098} \approx 0.090$$

About 9%. Despite a 99% accurate test.

---

## Why this matters for financial modeling

**Credit scoring and default probability:**

If the historical default rate in an investment-grade bond portfolio is 0.2% per year, then even a model that flags potential defaults with 95% accuracy will produce a large number of false alarms. Before acting on a model signal, you need to weight it against the base rate.

**Earnings surprise detection:**

If large negative earnings surprises occur in only 5% of quarters for a stable-growth company, an anomaly detection model with high sensitivity will still produce many false positives. The prior probability of the event shapes how much you should trust any individual signal.

**Fraud detection:**

In a low-fraud transaction portfolio, even a highly accurate fraud model will flag mostly legitimate transactions. The prior fraud rate is the most important input — not the model's sensitivity.

The general lesson: **always ask what the base rate is before trusting a model signal.** A Bayesian framework forces this question explicitly, because the prior must be specified before you can compute the posterior.

---

## The broader principle: prior sensitivity

The degree to which conclusions change when you shift the prior is called **prior sensitivity**. When the prior is very strong (very low base rate, or very high prior confidence), it takes a large amount of data to override it.

This is not a flaw. It's the correct behavior. If you genuinely believe a company's default probability is 0.01%, a single quarter of cash flow weakness shouldn't push that estimate to 40%. The data needs to be both strong and consistent to move a well-calibrated prior.

---

## See also

- Section 1.3 for Bayes' rule derivation
- Section 1.8 for the law of total probability used in the denominator here
- Chapter 2 for the Beta-Binomial model, which generalizes this to continuous probability estimation
