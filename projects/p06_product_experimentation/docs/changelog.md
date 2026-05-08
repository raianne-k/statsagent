# Changelog — p06_product_experimentation

## 2026-05-07 — Initial project setup

### Added
- Created project folder structure for `p06_product_experimentation`.
- Added project-specific `README.md`.
- Added `project_config.yaml` for SaaS product experimentation.
- Added synthetic SaaS onboarding experiment dataset generator.
- Added project-specific descriptive plotting script.
- Added core experiment analysis script.
- Added segmentation support script.
- Added relationship support script.

---

## Dataset generation

### Added
- Generated synthetic SaaS onboarding experiment dataset.
- Included user/account structure fields:
  - user ID
  - signup date
  - acquisition channel
  - region
  - company size
  - industry
- Included experiment structure fields:
  - experiment group
  - experiment eligibility flag
  - assignment validity flag
  - exposure days
  - low exposure flag
- Included product behavior fields:
  - onboarding completion
  - activation
  - sessions in first 14 days
  - feature adoption count
  - support tickets in first 30 days
  - time to activation
- Included retention and monetization outcomes:
  - 30-day retention
  - 60-day retention
  - 30-day churn
  - upgrade flag
  - expansion revenue flag
  - monthly subscription value
- Included guardrail metric:
  - negative feedback flag

### Notes
- Dataset is synthetic and intentionally designed for portfolio, experimentation, and product analytics practice.
- Treatment effect is intentionally modest rather than unrealistically large.
- The strongest expected treatment effect is on onboarding and activation.
- Retention and revenue effects are intentionally noisier.
- Small assignment-quality and exposure-window issues were included for validation practice.

---

## Configuration

### Added
- Defined project metadata:
  - project ID
  - project name
  - domain
  - description
- Defined dataset paths and output paths.
- Defined experiment structure:
  - experiment group column
  - control group
  - treatment group
  - primary metrics
  - secondary metrics
  - confidence level
  - significance level
- Added cleaning rules for:
  - binary validation
  - non-negative numeric columns
- Added validation rules for:
  - group balance
  - assignment validity
  - experiment governance
- Added reporting configuration for:
  - confidence intervals
  - lift analysis
  - significance testing
  - governance notes

---

## Descriptive plotting

### Added
- Created descriptive plots for:
  - experiment group distribution
  - assignment validity
  - low exposure rate
  - activation distribution
  - 30-day retention distribution
  - 60-day retention distribution
  - 30-day churn distribution
  - sessions in first 14 days
  - feature adoption count
  - support tickets in first 30 days
  - monthly subscription value
  - time to activation
  - acquisition channel distribution
  - company size distribution
  - engagement band distribution

### Purpose
Establish experiment structure, outcome distributions, and diagnostic checks before formal experiment interpretation.

---

## Experiment analysis

### Added
- Created experiment integrity review.
- Created binary metric experiment comparison table.
- Created continuous metric experiment comparison table.
- Created randomization balance check.

### Outputs
- `experiment_integrity_review.csv`
- `binary_metric_experiment_results.csv`
- `continuous_metric_experiment_results.csv`
- `randomization_balance_check.csv`

### Purpose
Evaluate whether the treatment group differs from the control group across activation, retention, churn, monetization, and engagement outcomes.

---

## Segmentation support

### Added
- Created segment-level experiment summaries by:
  - company size
  - acquisition channel
  - region
  - industry
  - engagement band
  - feature adoption band
  - subscription value band
- Created segment-level treatment lift summaries for key outcomes:
  - onboarding completion
  - activation
  - 30-day retention
  - 60-day retention
  - 30-day churn
  - upgrade

### Purpose
Use segmentation as an experiment-support layer to identify whether treatment effects vary across customer groups.

---

## Relationship support

### Added
- Created overall metric-outcome correlation table.
- Created experiment-group-specific metric-outcome correlation table.
- Created binary context-outcome relationship table.
- Created engagement-retention relationship table.

### Purpose
Use relationship analysis as experiment context, not as the primary project identity.

Relationship outputs support:
- engagement interpretation
- retention context
- treatment-effect explanation
- guardrail review
- Simpson’s-paradox awareness

---

## Governance and interpretation

### Added
- Explicitly framed experiment outputs as decision-support evidence.
- Added warning that statistical significance does not automatically imply business significance.
- Added human-review requirement.
- Added no-causal-overclaim framing despite randomized assignment.
- Added emphasis on experiment validity, assignment quality, exposure window, and rollout caution.

---

## Current status

Project setup is partially complete.

Completed:
- README
- project configuration
- dataset generator
- descriptive plotting script
- experiment analysis script
- segmentation support script
- relationship support script
- changelog
