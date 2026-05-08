# Fintech Repayment Inference Findings
**Project:** p04_fintech_inference  
**Stage:** S04A — Repayment Risk Inference & Uncertainty Analysis

---

> **Dataset note:** This project uses a synthetic but intentionally realistic fintech repayment dataset built for portfolio and analytical practice. Some observed patterns may partly reflect simulation logic rather than naturally occurring production behavior. That distinction is flagged where relevant throughout.

---

## p04 Stage goals

Move from descriptive relationships into uncertainty-aware statistical reasoning.

This stage focused on:
- conditional probability
- confidence intervals
- repayment-risk updates
- intervention-group comparison
- uncertainty interpretation
- validation-aware inference workflows

The goal was not predictive modeling, but evaluating whether observed repayment-risk differences appear meaningful and how confident we can be in those observations.

---

# Main Findings

## 1. Missed recent payments materially increase delinquency risk

Customers with a missed payment in the last 30 days showed substantially higher delinquency rates.

| Group | Delinquency Rate |
|---|---|
| No missed payment | 13.92% |
| Missed payment | 26.34% |

Difference: **+12.4 percentage points**

This is one of the clearest repayment-risk signals in the dataset.

---

## 2. Prior delinquency remains an important risk signal

Historical repayment issues were also associated with meaningfully higher current delinquency risk.

| Group | Delinquency Rate |
|---|---|
| No prior delinquency | 14.26% |
| Prior delinquency | 25.13% |

Difference: **+10.9 percentage points**

This suggests repayment stress is persistent rather than randomly distributed across customers.

---

## 3. Risk tiers show meaningful delinquency separation

The synthetic risk scoring system produced progressively higher delinquency rates across tiers.

| Risk Tier | Delinquency Rate |
|---|---|
| Low risk | 13.24% |
| Medium risk | 19.93% |
| High risk | 24.31% |

The pattern aligns directionally with expectations:
higher modeled risk corresponds to higher observed delinquency.

However:
- the `high_risk` segment is small (~3.6% of the dataset)
- estimates for this group carry wider uncertainty intervals
- small-group volatility limits confidence precision

This becomes important when interpreting operational risk estimates.

---

## 4. Intervention outcomes should NOT be interpreted causally

Recovery rates differed across intervention groups.

| Intervention Group | Recovery Rate |
|---|---|
| SMS reminder | 59.50% |
| Repayment call | 58.50% |
| No intervention | 57.06% |
| Hardship outreach | 48.26% |

At first glance, hardship outreach appears least effective.

That interpretation would likely be incorrect.

Higher-risk customers were intentionally more likely to receive stronger interventions. This creates **selection bias**:
the intervention groups do not represent comparable populations.

This stage demonstrates an important inference principle:

> Observed outcome differences do not automatically represent treatment effectiveness.

---

## 5. Bayesian-style updates substantially changed baseline risk estimates

Baseline delinquency rate across the portfolio:

| Metric | Rate |
|---|---|
| Overall delinquency prior | 16.04% |

Observed evidence materially updated that estimate.

### After missed recent payment

| Condition | Updated Delinquency Risk |
|---|---|
| Missed payment present | 26.34% |
| Missed payment absent | 13.92% |

### After prior delinquency

| Condition | Updated Delinquency Risk |
|---|---|
| Prior delinquency present | 25.13% |
| Prior delinquency absent | 14.26% |

New repayment information changes estimated customer risk without requiring predictive modeling.

---

# Overall

The portfolio reflects:
- moderate overall repayment stress
- meaningful variation across risk segments
- observable repayment-risk signals
- measurable uncertainty differences between groups

Most important analytical outcomes from this stage:

- missed-payment behavior strongly updates delinquency risk
- prior delinquency remains operationally meaningful
- small high-risk segments produce wider uncertainty
- intervention comparisons are vulnerable to selection bias
- observational differences should not be interpreted causally

---

# Key Statistical Lessons

This stage reinforced several important inference concepts:

| Concept | Example |
|---|---|
| Conditional probability | Delinquency given missed payment |
| Uncertainty awareness | Wider confidence intervals in small groups |
| Selection bias | Higher-risk customers receiving interventions |
| Observational vs causal reasoning | Intervention outcomes do not prove effectiveness |
| Prior vs posterior risk | Bayesian-style repayment updates |

---

# Limitations

- Synthetic dataset
- No causal inference
- No randomized intervention assignment
- Intervention groups intentionally contain selection bias
- Confidence intervals are approximate
- High-risk subgroup remains relatively small
- Bayesian outputs are simplified operational examples, not formal Bayesian models

---

*AI-assisted workflow with human validation and review. Portfolio and exploratory use only.*