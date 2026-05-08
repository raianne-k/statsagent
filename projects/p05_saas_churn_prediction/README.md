# SaaS Churn Prediction Pipeline

**Project:** p05_saas_churn_prediction  
**Domain:** SaaS / Product Analytics  
**Focus:** Predictive modeling, churn risk, retention analytics, operational decision support, and validation-aware analytics

---

> **Dataset note:** This project uses a synthetic but intentionally realistic SaaS customer dataset built for portfolio and analytical practice. Some behavioral and churn patterns may partly reflect simulation logic rather than naturally occurring production behavior.

---

## p05 Stage goals

Move from exploratory analytics into predictive modeling and operational decision support.

Current focus:
- churn prediction
- retention-risk scoring
- feature interpretation
- threshold analysis
- model evaluation
- operational tradeoffs
- dashboard and stakeholder reporting
- validation-aware predictive workflows

The goal is not to maximize model complexity, but to build interpretable predictive workflows that support product and customer-success decision-making.

---

## Analytical Goal

The purpose of this project is to answer:

> Which behavioral and operational patterns best predict SaaS customer churn risk?

---

## Why This Matters

SaaS churn datasets combine:
- product engagement
- customer lifecycle behavior
- subscription structure
- operational friction
- support activity
- commercial account value
- retention signals

without it:

```text
- high accuracy can still miss high-risk churn accounts
- feature importance does not imply causality
- prediction thresholds change operational workload
- false negatives may be more expensive than false positives
- data leakage can create misleadingly strong models
- strong statistical signals may still lack business usefulness
```

This project focuses on interpretable prediction and operational reasoning rather than black-box optimization.


## Pipeline Structure

The pipeline contains six analytical layers.

1. Profiling & Validation

The shared analytical engine identifies:

- continuous variables
- binary variables
- categorical variables
- missingness
- skewed distributions
- suspicious values
- cleaning requirements

This creates a validated baseline before predictive work begins.

2. Segmentation Analysis

Customer groups are compared across:

- health bands
- usage bands
- plan tiers
- contract structure
- login recency
- revenue bands

This establishes whether churn risk differs meaningfully across customer profiles.

3. Relationship Analysis

The relationship layer evaluates associations between:

- account health
- engagement behavior
- support activity
- onboarding completion
- contract structure
- retention signals
- churn outcome

This supports feature reasoning before modeling.

4. Predictive Modeling

The predictive layer trains an interpretable churn-classification model.

Current modeling focus:

- logistic regression
- train/test split
- churn probability scoring
- threshold comparison
- feature interpretation
- operational tradeoffs

5. Executive Reporting & Dashboarding

This project introduces stakeholder-facing deliverables including:

- executive analytical reporting
- operational churn summaries
- threshold tradeoff views
- churn-risk dashboards
- retention monitoring outputs

## Executive Deliverables

#### Churn-Risk Dashboard

![Churn Dashboard](outputs/dashboard/churn_dashboard_preview.png)

#### Executive Retention Report

![Executive Report](outputs/reports/executive_report_preview.png)

### Interactive Outputs

- [Executive HTML Report](outputs/reports/executive_report.html)
- [Interactive Churn Dashboard](outputs/dashboard/churn_dashboard.html)

6. Governance & Human Review

Outputs are reviewed for:

- leakage risk
- unsupported causal claims
- misleading accuracy interpretation
- threshold misuse
- poor operational framing
- missing validation context

Workflow:
Run, validate, review, rerun

#### Expected Outputs

- descriptive statistical report
- segmentation comparison tables
- relationship-analysis outputs
- predictive model metrics
- threshold comparison tables
- feature-importance summaries
- churn-risk scoring outputs
- executive HTML report
- dashboard outputs
- validation log
- cleaning log
- analytical plots
- cleaned analytical dataset
- human-reviewed findings document

#### Expected Analytical Themes

This project is designed to explore:

- which engagement signals predict churn
- how operational friction affects retention
- whether account health meaningfully separates churn outcomes
- how contract structure influences churn probability
- how thresholds affect intervention volume
- why recall and precision tradeoffs matter operationally
- why prediction does not imply causality

## Governance & Human Oversight

This project follows governance-oriented analytical principles including:

- transparency
- auditability
- validation-aware reporting
- human oversight
- interpretability
- separation of prediction from explanation
- separation of correlation from causality

The workflow is intentionally designed as:

AI-assisted analysis with human validation rather than autonomous customer-retention decision-making.

⸻

## Stage Boundary

This project does:

- clean and validate SaaS customer data
- profile churn-related behavior
- compare customer groups
- evaluate churn relationships
- build interpretable predictive models
- compare threshold tradeoffs
- generate stakeholder-facing analytical outputs
- support retention-focused operational reasoning

This project does not:

- infer causality
- deploy production ML systems
- automate retention decisions
- optimize deep-learning models
- guarantee churn reduction
- replace customer-success judgment

⸻

Repository Structure
projects/p05_saas_churn_prediction/
├── data/
│   ├── raw/
│   └── cleaned/
├── outputs/
│   ├── reports/
│   ├── plots/
│   ├── segmentation/
│   ├── relationships/
│   ├── prediction/
│   ├── validation/
│   ├── cleaning/
│   └── metadata/
├── configs/
│   └── project_config.yaml
├── README.md
├── changelog.md
├── findings.md
├── create_plots.py
├── segmentation_analysis.py
├── relationships.py
├── prediction_analysis.py
└── run.sh

Limitations

- Synthetic dataset
- Predictive outputs are for portfolio and learning purposes only
- No causal interpretation
- No production deployment
- Model performance depends partly on simulated signal structure
- Feature importance does not prove business drivers
- Threshold choices require business judgment
- Dashboard outputs are analytical decision-support tools, not autonomous systems