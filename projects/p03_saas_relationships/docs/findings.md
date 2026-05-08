# SaaS Relationship & Operational Analysis
**Project:** p03_saas_relationships  
**Stage:** S03 — Segmentation, Relationship Analysis & Operational Patterns

---

> **Dataset note:** This project uses a synthetic but intentionally realistic SaaS dataset built for portfolio and analytical practice. Some relationships may partly reflect simulation structure rather than naturally occurring production behavior. That distinction is flagged where relevant throughout.

---

## 01 Stage goals

Move beyond descriptive profiling into:
- segmentation
- operational comparison
- relationship analysis
- behavioral pattern evaluation

The objective of this stage was not predictive modeling, but understanding:
- which SaaS account groups behave differently
- which operational variables move together
- which patterns appear operationally meaningful

---

## Main Findings

### 1. Account health is strongly tied to product adoption

The strongest relationships in the dataset consistently involve:
- feature adoption
- seat utilization
- onboarding completion

| Variable | Pearson correlation with `account_health_score` |
|---|---|
| `feature_adoption_rate` | 0.816 |
| `seats_used_percent` | 0.715 |
| `onboarding_completion_percent` | 0.627 |

The same pattern appears under Spearman correlation, suggesting the relationship is structurally consistent rather than driven only by outliers.

This is the clearest operational finding in the dataset:
- healthier accounts tend to adopt more features
- use a larger share of purchased seats
- complete onboarding more fully

---

### 2. Revenue is extremely concentrated

`monthly_recurring_revenue` is heavily right-skewed.

A relatively small number of accounts generate disproportionately large revenue values, while most accounts cluster at the lower end.

This means:
- averages overstate the “typical” SaaS account
- medians and percentiles are more reliable than means
- enterprise accounts materially distort aggregate reporting

> *This mirrors real SaaS revenue structures where a minority of accounts often generate the majority of revenue.*

---

### 3. Churn behavior is operationally weaker than expected

Churned accounts do differ operationally, but not dramatically.

| Metric | Non-churned | Churned |
|---|---|---|
| Median account health | 0.52 | 0.48 |
| Median renewal probability | 71.81 | 69.53 |
| Median feature adoption | 32.89 | 29.96 |
| Median MRR | 179.4 | 147.2 |

The differences are directionally consistent:
- lower adoption
- lower health
- lower revenue
- lower renewal likelihood

But the gaps are relatively moderate.

This suggests churn in the dataset is:
- not driven by a single dominant variable
- likely multi-factor
- operationally diffuse rather than binary

---

### 4. Product usage is concentrated at the low-to-mid range

The `usage_band` distribution is highly imbalanced.

Most accounts fall into:
- low usage
- medium usage

Very few accounts qualify as high usage.

This matters operationally because:
- “power users” are rare
- high-engagement behavior is not representative of the broader customer base
- aggregate engagement metrics are heavily shaped by lower-usage customers

---

### 5. Login inactivity has a strong long-tail pattern

`days_since_last_login` shows clear right skew.

Most accounts remain relatively active, but a smaller inactive tail extends far outward.

This creates a meaningful distinction between:
- regularly active accounts
- dormant or decaying accounts

Potentially useful later for:
- retention workflows
- lifecycle analysis
- churn modeling
- intervention triggers

---

### 6. Account health is more stable than revenue

Unlike MRR, `account_health_score` is relatively centered and approximately normal.

This suggests the health metric behaves more like a composite operational score than a pure financial metric.

Operationally, this is useful because:
- the metric is less distorted by outliers
- comparisons between account groups become more stable
- downstream modeling becomes easier

---

### 7. SaaS plan structure reflects expected funnel behavior

The dataset follows a typical SaaS commercial structure:

| Plan | Relative presence |
|---|---|
| Starter | Largest |
| Growth | Large |
| Business | Smaller |
| Enterprise | Smallest |

Enterprise remains a minority segment.

This reinforces the revenue-concentration pattern:
- a small subset of accounts likely contributes disproportionately to revenue outcomes

---

## Overall

Dataset is clean and suitable for continued analysis.

Main structural themes identified:
- strong relationship between adoption and account health
- heavy revenue concentration
- moderate but consistent churn-related differences
- engagement concentrated in lower-usage tiers
- clear inactivity tail behavior
- operational metrics more stable than financial metrics

---

## Operational interpretation

The strongest signal throughout the analysis is not revenue itself.

It is:
- adoption quality
- onboarding completion
- actual seat utilization

The dataset consistently suggests that:
- healthier SaaS accounts are behaviorally engaged
- operational usage patterns matter more than raw account size alone
- customer success indicators cluster together structurally

---

## Important analytical boundaries

This stage identifies:
- associations
- operational patterns
- segmentation differences

It does **not** establish:
- causality
- churn drivers
- retention mechanisms
- predictive certainty

---

*AI-assisted workflow with human validation and review. Portfolio and exploratory use only.*