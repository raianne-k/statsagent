# SaaS Customer Relationship Analysis Pipeline

**Project:** p03_saas_relationships  
**Domain:** SaaS / Product Analytics  
**Focus:** Descriptive profiling, segmentation, relationship analysis, account health patterns, and validation-aware analytics

---> **Dataset note:** This project uses a synthetic but intentionally realistic SaaS customer dataset built for portfolio and analytical practice. Certain behavioral and operational patterns may partly reflect simulation logic rather than naturally occurring production behavior. That distinction is flagged where relevant throughout.

---

## 01 Stage goals

Move from descriptive profiling into segmentation and relationship analysis.

Current focus:
- descriptive profiling
- SaaS account segmentation
- behavioral relationship analysis
- operational metric associations
- churn-related pattern analysis
- validation-aware analytical workflows

The goal is not to build predictive churn models yet, but to understand how SaaS account groups differ and which operational variables move together in meaningful ways.

---

## Analytical Goal

The purpose of this project is to answer:
> Which behavioral and operational patterns are associated with account health, engagement quality, renewal probability, and churn-related risk within a SaaS environment?

---

## Why This Matters

SaaS datasets combine:
- product usage behavior
- subscription economics
- engagement metrics
- customer-support activity
- account health indicators
- retention-related signals

These relationships are often easy to misinterpret.

Examples:
- High support-ticket volume may indicate either product friction or healthy platform usage
- High engagement does not always imply low churn risk
- Revenue concentration can distort account-level averages
- Account-health metrics may overlap operationally
- Correlation between variables does not imply causation
- Behavioral signals may reflect lifecycle stage rather than customer quality

This stage focuses on understanding both:
1. How customer groups differ
2. How operational variables relate to one another
before moving into statistical inference or predictive modeling.

---

## Pipeline Structure

The pipeline currently has five layers:

### 1. Profiling & Variable Classification
The analytical engine first identifies variable structure:
- continuous variables
- binary variables
- categorical variables
- behavioral metrics
- operational KPIs
- engagement indicators
- account-health metrics
- ID columns

This determines which analytical methods are appropriate for each field.

### 2. Cleaning & Validation
The cleaning layer applies conservative, logged transformations before analysis. Current rules include:
- preserving raw datasets separately from cleaned outputs
- validating binary churn-related variables
- flagging impossible operational values
- preserving missingness through explicit flags
- excluding identifiers from analysis
- logging all transformations

The goal is not to create “perfect” data, but to create a traceable and reviewable analytical dataset.

### 3. Segmentation & Comparative Analysis
This stage focuses on comparing SaaS customer groups responsibly. Examples include:
- health-band comparison
- usage-tier comparison
- revenue-tier segmentation
- churn-group comparison
- onboarding and engagement segmentation
- account lifecycle comparisons

The objective is not only to identify differences, but to determine whether those differences are operationally meaningful.

### 4. Relationship & Association Analysis
This stage evaluates how operational and behavioral variables move together. Examples include:
- engagement vs churn-related behavior
- feature adoption vs renewal probability
- support activity vs account health
- onboarding completion vs usage quality
- account health vs expansion revenue
- login recency vs churn-related indicators

The objective is not only to identify statistical relationships, but to determine whether those relationships are operationally meaningful and analytically defensible.

### 5. Validation & Governance Layer
The validation layer reviews analytical outputs before they are treated as trustworthy. Validation checks include:
- causal overclaims
- unsupported interpretations
- unresolved cleaning flags
- misleading correlations
- hidden imbalance issues
- suspicious distributions
- inappropriate statistical treatment

**Workflow:** Run, validate, fix, rerun.

---

## Expected Outputs
- validated descriptive report
- segmentation comparison tables
- relationship-analysis outputs
- correlation summaries
- validation log
- cleaning log
- analytical plots
- cleaned analytical dataset
- human-reviewed findings document

---

## Expected Analytical Themes
The project is designed to explore patterns such as:
- engagement patterns associated with account health
- behavioral signals associated with churn-related risk
- relationships between onboarding completion and product usage
- support-ticket behavior across account-health tiers
- operational indicators linked to renewal probability
- account patterns potentially relevant for retention workflows
- differences between healthy and at-risk customer segments

#### Account Health vs Feature Adoption

![Account Health vs Feature Adoption](outputs/plots/relationships/account_health_vs_feature_adoption.png)

#### Engagement and Churn-Risk Relationship Matrix

![Relationship Matrix](outputs/plots/relationships/relationship_matrix.png)

#### Customer Segment Comparison

![Customer Segment Comparison](outputs/plots/segmentation/customer_segment_comparison.png)
---

## Governance & Human Oversight
This project follows governance-oriented analytical principles including:
- transparency
- auditability
- traceability
- validation-aware reporting
- human oversight
- separation of observation from interpretation

Shared governance policies are maintained centrally at the repository level to ensure consistency across analytical projects and stages. The workflow is intentionally designed as **AI-assisted analysis with human validation** rather than fully autonomous operational decision-making.

---

## Stage Boundary

**This project does:**
- clean and validate SaaS operational data
- profile SaaS customer behavior
- compare customer segments
- evaluate behavioral relationships
- identify operational associations
- produce validation-aware analytical outputs
- support human-reviewed interpretation

**This project does not:**
- infer causality
- automate churn decisions
- replace customer-success review
- build production-grade retention models
- guarantee operational outcomes

---

## Repository Structure
```text
projects/p03_saas_relationships/
├── data/
│   ├── raw/
│   └── cleaned/
├── outputs/
│   ├── reports/
│   ├── plots/
│   ├── segmentation/
│   ├── relationships/
│   ├── validation/
│   ├── cleaning/
│   └── metadata/
├── configs/
│   └── project_config.yaml
├── README.md
├── changelog.md
└── findings.md
```
