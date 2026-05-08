# Changelog — p05_saas_churn_prediction

## 2026-05-07 — Initial project setup

### Added
- Created project folder structure for `p05_saas_churn_prediction`.
- Added project-specific `README.md`.
- Added `project_config.yaml` for SaaS churn prediction.
- Added synthetic SaaS churn dataset generator.
- Added project-specific descriptive plotting script.
- Added segmentation analysis script.
- Added relationship analysis script.
- Added predictive modeling script.
- Added executive HTML report generator.
- Added Streamlit dashboard script.

---

## Dataset generation

### Added
- Generated synthetic SaaS customer dataset with account-level churn behavior.
- Included customer structure fields:
  - region
  - industry
  - company size
  - plan tier
  - contract type
- Included commercial and lifecycle fields:
  - monthly recurring revenue
  - tenure months
  - renewal probability score
- Included product-usage fields:
  - weekly active users
  - feature adoption rate
  - login frequency
  - average session duration
  - days since last login
  - seat utilization
- Included support and account-health fields:
  - support ticket count
  - unresolved ticket count
  - support escalation flag
  - NPS score
  - account health score
- Included churn outcome:
  - `churned`

### Notes
- Dataset is synthetic and intentionally designed for portfolio, predictive modeling, and product analytics practice.
- Churn logic was designed to be realistic but not deterministic.
- Missingness was introduced for `nps_score` and `account_health_score`.

---

## Configuration

### Added
- Defined project metadata:
  - project name
  - domain
  - stage
  - raw and cleaned data paths
  - output paths
- Defined analytical variable groups:
  - ID columns
  - binary columns
  - categorical columns
  - continuous columns
- Added validation rules for numeric ranges.
- Added missing-value handling rules for:
  - `nps_score`
  - `account_health_score`
- Added governance metadata for synthetic-data and human-review requirements.

---

## Descriptive analysis

### Added
- Reused shared descriptive statistics pipeline.
- Generated cleaned analytical dataset.
- Generated descriptive statistical report.
- Logged cleaning and validation outputs.
- Preserved technical pipeline columns for validation review.

### Purpose
Establish a reliable baseline before segmentation, relationships, prediction, and reporting.

---

## Plotting

### Added
- Created descriptive plots for:
  - account health score
  - feature adoption rate
  - seat utilization
  - days since last login
  - monthly recurring revenue
  - churn distribution
  - health band distribution
  - usage band distribution
  - contract type distribution
  - plan tier distribution

### Purpose
Visually inspect churn-related distributions, skew, segment balance, and operational structure.

---

## Segmentation analysis

### Added
- Created segment-level comparison tables for:
  - health band
  - usage band
  - contract type
  - plan tier
  - login recency band
  - revenue band
- Created cross-segment tables:
  - health band × contract type
  - usage band × plan tier
  - health band × login recency band

### Purpose
Establish customer-group context before predictive modeling.

---

## Relationship analysis

### Added
- Created continuous-variable churn correlation table.
- Created binary-variable churn relationship table.
- Created churn relationship summaries for:
  - contract type
  - plan tier
  - health band

### Purpose
Identify candidate churn signals before modeling without treating relationships as causal.

---

## Predictive modeling

### Added
- Built logistic regression churn model.
- Used train/test split with stratified target sampling.
- Added preprocessing pipeline:
  - median imputation for numeric variables
  - standard scaling for numeric variables
  - one-hot encoding for categorical variables
- Added model evaluation outputs:
  - accuracy
  - precision
  - recall
  - F1 score
  - ROC AUC
- Added threshold comparison table.
- Added feature-importance table based on model coefficients.
- Added scored test-account output with predicted churn probabilities.

### Purpose
Create an interpretable predictive baseline for churn-risk decision support.

---

## Executive reporting

### Added
- Created `executive_report.py`.
- Generated branded HTML report:
  - executive summary
  - model performance
  - threshold tradeoffs
  - top feature signals
  - segmentation context
  - churn relationships
  - governance note

### Purpose
Create a stakeholder-facing analytical deliverable beyond raw CSV outputs.

---

## Dashboard

### Added
- Created `dashboard.py`.
- Added Streamlit dashboard structure:
  - model performance metrics
  - threshold controls
  - feature signal view
  - segmentation context
  - churn relationship table
  - scored account review table
  - governance warning

### Notes
- Dashboard requires Streamlit:
  ```bash
  pip install streamlit