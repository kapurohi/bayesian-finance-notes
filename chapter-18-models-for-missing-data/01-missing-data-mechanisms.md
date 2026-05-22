# 18.1 — Missing Data Mechanisms

## What this section is doing

Gelman classifies missingness by whether the probability of data being missing depends on the missing value itself. This classification determines what can be inferred from incomplete data.

---

## The three mechanisms

**MCAR — Missing Completely At Random:** The probability of missingness doesn't depend on the data at all. A random data vendor outage causes some quarterly reports to be missing. MCAR data can be safely ignored without bias.

**MAR — Missing At Random:** The probability of missingness depends on observed data but not on the missing value itself. Small companies are less likely to report supplementary metrics — but once you condition on size, missingness is random. MAR data can be handled with proper imputation.

**MNAR — Missing Not At Random:** The probability of missingness depends on the missing value itself. Companies with bad earnings are more likely to delay or restate reports. MNAR creates bias that cannot be corrected without modeling the missingness process explicitly.

---

## Financial application

The MNAR case is common and dangerous in finance: distressed companies delay reporting, companies with covenant breaches may withhold metrics, and survivorship bias means failed companies have no data at all. Any backtest or model trained on available data is implicitly conditioning on survival — introducing MNAR bias.
