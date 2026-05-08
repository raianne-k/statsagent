# Fintech Customer Segmentation Analysis
**Project:** p02_fintech_customer_segmentation  
**Stage:** S02A — Segmentation, Cohorts & Operational Comparison

---

> **Dataset note:** This project uses a synthetic but intentionally realistic fintech customer dataset built for portfolio purposes. Some segment distributions and customer behaviors may partly reflect simulation logic rather than naturally occurring production behavior.

---

## p02 Stage goals

Move from variable-level analysis into customer-group analysis.

This stage focuses on:
- comparing customer segments
- identifying structural differences between groups
- evaluating whether segmentation variables are analytically meaningful
- understanding where aggregate averages hide operational variation

The purpose of this stage is segmentation and comparison — not prediction or causal inference.

---

## Main Findings

### 1. Risk segmentation meaningfully separates financial behavior

`risk_band` is the clearest separating variable in the dataset.

Higher-risk customers consistently show:
- higher delinquency rates
- higher missed-payment counts
- larger loan burdens
- worse repayment behavior
- more payment lateness

The separation appears across multiple variables simultaneously rather than a single isolated metric.

| Pattern | Observation |
|---|---|
| Loan burden | Increases across higher-risk tiers |
| Repayment quality | Deteriorates in elevated-risk groups |
| Payment lateness | Higher in riskier segments |
| Delinquency | Concentrated in higher-risk customers |

`loan_to_income_ratio` and repayment-related variables appear to be the strongest segment-separating metrics in this stage.

---

### 2. Financial exposure remains highly concentrated inside groups

Even after segmentation, several financial variables remain strongly right-skewed.

Most visible in:
- `active_loan_amount`
- `installment_size`
- `savings_balance`

This means:
- averages overstate the “typical” customer
- medians remain operationally safer than means
- a minority of customers hold disproportionately large balances or obligations

The same structural issue identified during descriptive analysis persists at the segment level.

---

### 3. Engagement is not the same as financial health

Higher engagement groups are not automatically lower-risk groups.

Some engaged customers still show:
- elevated borrowing
- meaningful repayment stress
- active delinquency behavior

---

### 4. Product depth remains shallow across most customers

| Products Held | Approximate Share |
|---|---|
| 1 product | Majority |
| 2 products | Secondary group |
| 3+ products | Minority |

Most customers still hold only one product.

This suggests:
- relatively shallow customer relationships
- possible cross-sell opportunity
- concentration of deeper engagement within smaller user subsets

Product ownership may become more analytically meaningful in later relationship analysis.

---

### 5. Delinquency behaves like a concentrated subgroup phenomenon

Delinquency is not evenly distributed across the customer base.

It clusters alongside:
- higher loan exposure
- higher missed-payment counts
- worse repayment rates
- elevated average days late

This suggests delinquency is concentrated within specific financial profiles rather than broadly spread across the population.

---

### 6. Tenure cohorts reveal customer stabilization patterns

Customer behavior changes meaningfully across tenure cohorts.

| Cohort | Definition |
|---|---|
| `new_0_3m` | 0–3 months |
| `early_4_12m` | 4–12 months |
| `established_13_24m` | 13–24 months |
| `mature_25m_plus` | 25+ months |

Newer cohorts generally show:
- lower product depth
- lower balances
- shorter engagement history

More mature cohorts tend to show:
- larger financial exposure
- deeper product adoption
- more stable repayment behavior

This suggests customer financial profiles evolve materially with platform tenure.

> *Some cohort effects may partially reflect synthetic dataset generation logic.*

---

### 7. High-risk segment is statistically sparse

| Segment | Share |
|---|---|
| `high_risk` | Very small minority |
| `medium_risk` | Moderate minority |
| `low_risk` | Large majority |

The high-risk population is extremely small relative to the overall dataset.

This creates analytical constraints:
- subgroup instability
- sensitivity to outliers
- reduced reliability of comparisons

The segment may still be operationally important, but findings should remain cautious.

---

## Overall

The segmentation stage confirms that the customer base is structurally heterogeneous.

Key patterns moving forward:
- Risk segmentation meaningfully separates repayment behavior
- Medians remain safer than means across several financial variables
- Financial exposure is concentrated within smaller customer subsets
- Engagement alone is not a reliable proxy for financial health
- Product ownership remains relatively shallow
- Delinquency behaves as a concentrated subgroup issue rather than a broad population pattern
- Customer tenure meaningfully changes financial and behavioral structure

The dataset is suitable for deeper relationship analysis.

---

*AI-assisted workflow with human validation and review. Portfolio and exploratory use only.*