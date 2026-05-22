# 8.4 — Censoring and Truncation

## What this section is doing

Censoring occurs when you know an event happened but not when. Truncation occurs when observations below (or above) a threshold are excluded entirely. Both introduce systematic bias if ignored. This section shows how to build likelihoods that correctly account for censored and truncated data.

---

## Simplification

You're modeling time-to-default for a loan portfolio. Many loans have not defaulted yet — they're still active. You know they haven't defaulted in 3 years, but you don't know if they'll default in year 4. Ignoring these observations loses information. Treating them as non-defaults biases the model toward lower default rates.

The correct treatment is **right-censoring**: each active loan contributes the probability of surviving at least this long to the likelihood, rather than the probability of defaulting at a specific time.

---

## The censored likelihood

For a right-censored observation at time $c$ (the loan is still active at time $c$):

$$p(\text{survival beyond } c \mid \theta) = S(c \mid \theta) = 1 - F(c \mid \theta)$$

Where $S$ is the survival function. This correctly uses the information that the loan survived to time $c$ without assuming it will survive forever.

---

## Financial applications

- **Credit duration modeling:** Active loans are right-censored
- **Time-to-IPO models:** Private companies that haven't gone public yet are right-censored
- **Recovery rate modeling:** Defaulted loans where recovery is still in process are censored
- **Options modeling:** Options that expire out of the money are truncated observations of the underlying process

---

## See also
- Section 2.1 for Binomial models — censoring is the continuous-time generalization
