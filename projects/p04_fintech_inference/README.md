# Fintech Repayment Inference Pipeline

**Project:** p04_fintech_inference  
**Domain:** Fintech / Credit Risk  
**Focus:** Statistical reasoning, conditional probability, uncertainty interpretation, and validation-aware analytics

---

> **Dataset note:** This project uses a synthetic but intentionally realistic fintech repayment dataset built for portfolio and analytical practice. Some patterns may partly reflect simulation logic rather than naturally occurring production behavior.

---

## p04 Stage goals

Move from relationships into statistical reasoning.

Current focus:
- conditional probability
- confidence intervals
- repayment-risk signals
- intervention comparison
- uncertainty-aware interpretation
- validation-aware analytical workflows

The goal is not to predict delinquency yet, but to understand how confident we can be in observed repayment-risk differences.

---

## Analytical Goal

The purpose of this project is to answer:

> Which repayment-risk signals appear statistically meaningful, and how confident can we be in those observations?

---

## Why This Matters

Fintech repayment datasets combine:
- customer risk indicators
- repayment behavior
- intervention activity
- financial exposure
- operational follow-up signals

These are easy to overinterpret.

Examples:

```text
- intervention groups may look riskier because they were targeted
- small risky subgroups create wide uncertainty
- observed differences may be noise
- missed-payment signals update risk but do not prove future delinquency
- higher support contact may indicate distress or responsible engagement
```

This stage focuses on:
- distinguishing signal from noise
- reasoning about uncertainty
- interpreting repayment-risk evidence responsibly

before moving into predictive modeling.

---

## Pipeline Structure

The pipeline has four layers:

### 1. Profiling & Variable Classification

The shared engine identifies:
- continuous variables
- binary variables
- categorical variables
- repayment indicators
- intervention fields
- ID columns

---

### 2. Cleaning & Validation

Rules include:
- preserving raw data
- validating binary fields
- flagging impossible numeric values
- preserving missingness with flags
- excluding identifiers from analysis
- logging all transformations

---

### 3. Inference Analysis

This project evaluates:
- conditional probabilities
- confidence intervals
- repayment-risk differences
- small-group uncertainty
- Bayesian-style risk updates
- intervention-group comparisons

The objective is to reason about uncertainty, not to claim causality.

---

### 4. Validation & Governance

Outputs are reviewed for:
- causal overclaims
- unsupported conclusions
- unresolved cleaning flags
- small-sample risk
- misleading certainty
- overstated statistical interpretation

Workflow:

```text
Run, validate, fix, rerun
```

---

## Expected Outputs

- validated descriptive report
- inference-analysis outputs
- conditional probability summaries
- confidence interval summaries
- validation log
- cleaning log
- analytical plots
- cleaned analytical dataset
- human-reviewed findings document

---

## Expected Analytical Themes

The project is designed to explore patterns such as:
- delinquency probability after missed-payment events
- repayment-risk differences between intervention groups
- uncertainty around small high-risk segments
- repayment stability across income tiers
- operational follow-up patterns associated with repayment stress
- confidence differences between large and small repayment groups

The following outputs illustrate how repayment-risk signals and uncertainty measures are evaluated within the inference pipeline.

#### Repayment Risk Confidence Intervals

![Repayment Risk Confidence Intervals](outputs/plots/inference/repayment_risk_confidence_intervals.png)

#### Conditional Delinquency Probability by Customer Group

![Conditional Delinquency Probability](outputs/plots/inference/conditional_delinquency_probability.png)

#### Intervention Group Comparison

![Intervention Group Comparison](outputs/plots/inference/intervention_group_comparison.png)

---

## Governance & Human Oversight

This project follows governance-oriented analytical principles including:
- transparency
- auditability
- traceability
- uncertainty-aware reporting
- validation-aware analysis
- human oversight
- separation of observation from interpretation

The workflow is intentionally designed as:

> AI-assisted analysis with human validation

rather than fully autonomous operational decision-making.

---

## Stage Boundary

This project does:
- clean and validate repayment-risk datasets
- profile repayment behavior
- evaluate repayment-risk probabilities
- compare intervention-group outcomes
- quantify uncertainty around observed differences
- produce validation-aware analytical outputs

This project does not:
- infer causality
- automate lending decisions
- replace human risk review
- build predictive delinquency models
- guarantee operational outcomes

---

## Repository Structure

```text
projects/p04_fintech_inference/
├── data/
│   ├── raw/
│   └── cleaned/
├── outputs/
│   ├── reports/
│   ├── plots/
│   ├── inference/
│   ├── validation/
│   ├── cleaning/
│   └── metadata/
├── configs/
│   └── project_config.yaml
├── README.md
├── changelog.md
├── findings.md
├── create_plots.py
├── inference_analysis.py
└── run.sh
```

---

## Limitations

- Synthetic dataset
- Inference findings are observational only
- Confidence estimates depend on sample structure
- Correlation and conditional probability do not imply causation
- No predictive modeling at this stage
