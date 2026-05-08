# Analysis Report

Generated: 2026-05-07 20:27:38

## Task

descriptive_stats

## Dataset Overview

- Rows: 7000
- Columns: 48
- Duplicate rows: 0
- Numeric columns: ['customer_id', 'monthly_income', 'loan_balance', 'monthly_payment', 'loan_to_income_ratio', 'credit_utilization_percent', 'risk_score', 'missed_payments_last_6m', 'days_late_average', 'missed_payment_last_30d', 'prior_delinquency_flag', 'current_delinquency_flag', 'autopay_enabled', 'support_contact_last_30d', 'hardship_program_enrolled', 'payment_recovery_flag', 'repayment_probability_score', 'autopay_enabled_clean', 'missed_payment_last_30d_clean', 'prior_delinquency_flag_clean', 'current_delinquency_flag_clean', 'hardship_program_enrolled_clean', 'payment_recovery_flag_clean', 'support_contact_last_30d_clean']
- Categorical columns: ['region', 'income_band', 'employment_type', 'risk_tier', 'intervention_group', 'repayment_plan_type', 'autopay_enabled_invalid_flag', 'missed_payment_last_30d_invalid_flag', 'prior_delinquency_flag_invalid_flag', 'current_delinquency_flag_invalid_flag', 'hardship_program_enrolled_invalid_flag', 'payment_recovery_flag_invalid_flag', 'support_contact_last_30d_invalid_flag', 'employment_type_missing_flag', 'monthly_income_missing_flag', 'monthly_income_invalid_flag', 'loan_balance_invalid_flag', 'monthly_payment_invalid_flag', 'loan_to_income_ratio_invalid_flag', 'credit_utilization_percent_invalid_flag', 'missed_payments_last_6m_invalid_flag', 'days_late_average_invalid_flag', 'risk_score_invalid_flag', 'repayment_probability_score_invalid_flag']

## Missing Values

{'customer_id': 0, 'region': 0, 'income_band': 0, 'employment_type': 126, 'monthly_income': 178, 'loan_balance': 0, 'monthly_payment': 0, 'loan_to_income_ratio': 0, 'credit_utilization_percent': 0, 'risk_score': 0, 'risk_tier': 0, 'missed_payments_last_6m': 0, 'days_late_average': 0, 'missed_payment_last_30d': 0, 'prior_delinquency_flag': 0, 'current_delinquency_flag': 0, 'autopay_enabled': 0, 'support_contact_last_30d': 0, 'hardship_program_enrolled': 0, 'intervention_group': 0, 'repayment_plan_type': 0, 'payment_recovery_flag': 0, 'repayment_probability_score': 0, 'autopay_enabled_invalid_flag': 0, 'missed_payment_last_30d_invalid_flag': 0, 'prior_delinquency_flag_invalid_flag': 0, 'current_delinquency_flag_invalid_flag': 0, 'hardship_program_enrolled_invalid_flag': 0, 'payment_recovery_flag_invalid_flag': 0, 'support_contact_last_30d_invalid_flag': 0, 'autopay_enabled_clean': 0, 'missed_payment_last_30d_clean': 0, 'prior_delinquency_flag_clean': 0, 'current_delinquency_flag_clean': 0, 'hardship_program_enrolled_clean': 0, 'payment_recovery_flag_clean': 0, 'support_contact_last_30d_clean': 0, 'employment_type_missing_flag': 0, 'monthly_income_missing_flag': 0, 'monthly_income_invalid_flag': 0, 'loan_balance_invalid_flag': 0, 'monthly_payment_invalid_flag': 0, 'loan_to_income_ratio_invalid_flag': 0, 'credit_utilization_percent_invalid_flag': 0, 'missed_payments_last_6m_invalid_flag': 0, 'days_late_average_invalid_flag': 0, 'risk_score_invalid_flag': 0, 'repayment_probability_score_invalid_flag': 0}

## Method Used

Descriptive statistics were computed using column-type classification. Variables were separated into continuous numeric, binary, low-cardinality numeric, categorical, and technical pipeline columns.

Technical columns such as `_clean`, `_invalid_flag`, and `_missing_flag` are excluded from primary analytical interpretation and reserved for validation notes.

## Results

{'excluded_id_columns': ['customer_id'], 'continuous_numeric_columns': ['monthly_income', 'loan_balance', 'monthly_payment', 'loan_to_income_ratio', 'credit_utilization_percent', 'risk_score', 'days_late_average', 'repayment_probability_score'], 'binary_columns': ['missed_payment_last_30d', 'prior_delinquency_flag', 'current_delinquency_flag', 'autopay_enabled', 'support_contact_last_30d', 'hardship_program_enrolled', 'payment_recovery_flag'], 'low_cardinality_numeric_columns': ['missed_payments_last_6m'], 'categorical_columns': ['region', 'income_band', 'employment_type', 'risk_tier', 'intervention_group', 'repayment_plan_type'], 'technical_columns': ['autopay_enabled_invalid_flag', 'missed_payment_last_30d_invalid_flag', 'prior_delinquency_flag_invalid_flag', 'current_delinquency_flag_invalid_flag', 'hardship_program_enrolled_invalid_flag', 'payment_recovery_flag_invalid_flag', 'support_contact_last_30d_invalid_flag', 'autopay_enabled_clean', 'missed_payment_last_30d_clean', 'prior_delinquency_flag_clean', 'current_delinquency_flag_clean', 'hardship_program_enrolled_clean', 'payment_recovery_flag_clean', 'support_contact_last_30d_clean', 'employment_type_missing_flag', 'monthly_income_missing_flag', 'monthly_income_invalid_flag', 'loan_balance_invalid_flag', 'monthly_payment_invalid_flag', 'loan_to_income_ratio_invalid_flag', 'credit_utilization_percent_invalid_flag', 'missed_payments_last_6m_invalid_flag', 'days_late_average_invalid_flag', 'risk_score_invalid_flag', 'repayment_probability_score_invalid_flag'], 'summary': {'monthly_income': {'count': 6822.0, 'mean': 2020.05, 'std': 1185.18, 'min': 400.0, '25%': 1204.26, '50%': 1711.42, '75%': 2502.37, 'max': 9500.0}, 'loan_balance': {'count': 7000.0, 'mean': 5511.11, 'std': 4644.2, 'min': 300.0, '25%': 2533.79, '50%': 4226.42, '75%': 6959.55, 'max': 45000.0}, 'monthly_payment': {'count': 7000.0, 'mean': 392.7, 'std': 434.07, 'min': 8.82, '25%': 145.56, '50%': 263.65, '75%': 474.95, 'max': 7387.06}, 'loan_to_income_ratio': {'count': 7000.0, 'mean': 3.63, 'std': 3.92, 'min': 0.07, '25%': 1.31, '50%': 2.43, '75%': 4.5, 'max': 50.56}, 'credit_utilization_percent': {'count': 7000.0, 'mean': 43.01, 'std': 19.26, 'min': 0.68, '25%': 28.23, '50%': 42.24, '75%': 57.06, 'max': 97.63}, 'risk_score': {'count': 7000.0, 'mean': 0.42, 'std': 0.13, 'min': 0.0, '25%': 0.33, '50%': 0.41, '75%': 0.51, 'max': 1.0}, 'days_late_average': {'count': 7000.0, 'mean': 5.59, 'std': 3.69, 'min': 0.1, '25%': 2.9, '50%': 4.8, '75%': 7.6, 'max': 34.4}, 'repayment_probability_score': {'count': 7000.0, 'mean': 0.69, 'std': 0.1, 'min': 0.25, '25%': 0.63, '50%': 0.71, '75%': 0.77, 'max': 0.94}}, 'extra_stats': {'monthly_income': {'mean': np.float64(2020.05), 'median': np.float64(1711.42), 'variance': np.float64(1404661.59), 'iqr': np.float64(1298.11), 'outlier_count': 315, 'outlier_percent': 4.62, 'mean_median_gap_percent': np.float64(18.03), 'skew_warning': np.False_, 'round_number_max_check': {'max_value': 9500.0, 'max_count': 3, 'possible_cap': True, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'loan_balance': {'mean': np.float64(5511.11), 'median': np.float64(4226.42), 'variance': np.float64(21568589.75), 'iqr': np.float64(4425.76), 'outlier_count': 402, 'outlier_percent': 5.74, 'mean_median_gap_percent': np.float64(30.4), 'skew_warning': np.True_, 'round_number_max_check': {'max_value': 45000.0, 'max_count': 5, 'possible_cap': True, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'monthly_payment': {'mean': np.float64(392.7), 'median': np.float64(263.65), 'variance': np.float64(188418.01), 'iqr': np.float64(329.39), 'outlier_count': 519, 'outlier_percent': 7.41, 'mean_median_gap_percent': np.float64(48.95), 'skew_warning': np.True_, 'round_number_max_check': None}, 'loan_to_income_ratio': {'mean': np.float64(3.63), 'median': np.float64(2.43), 'variance': np.float64(15.37), 'iqr': np.float64(3.19), 'outlier_count': 479, 'outlier_percent': 6.84, 'mean_median_gap_percent': np.float64(49.24), 'skew_warning': np.True_, 'round_number_max_check': None}, 'credit_utilization_percent': {'mean': np.float64(43.01), 'median': np.float64(42.24), 'variance': np.float64(370.97), 'iqr': np.float64(28.83), 'outlier_count': 0, 'outlier_percent': 0.0, 'mean_median_gap_percent': np.float64(1.82), 'skew_warning': np.False_, 'round_number_max_check': None}, 'risk_score': {'mean': np.float64(0.42), 'median': np.float64(0.41), 'variance': np.float64(0.02), 'iqr': np.float64(0.18), 'outlier_count': 46, 'outlier_percent': 0.66, 'mean_median_gap_percent': np.float64(2.39), 'skew_warning': np.False_, 'round_number_max_check': None}, 'days_late_average': {'mean': np.float64(5.59), 'median': np.float64(4.8), 'variance': np.float64(13.64), 'iqr': np.float64(4.7), 'outlier_count': 162, 'outlier_percent': 2.31, 'mean_median_gap_percent': np.float64(16.54), 'skew_warning': np.False_, 'round_number_max_check': None}, 'repayment_probability_score': {'mean': np.float64(0.69), 'median': np.float64(0.71), 'variance': np.float64(0.01), 'iqr': np.float64(0.14), 'outlier_count': 122, 'outlier_percent': 1.74, 'mean_median_gap_percent': np.float64(2.56), 'skew_warning': np.False_, 'round_number_max_check': None}}, 'binary_summary': {'missed_payment_last_30d': {'count': 7000, 'positive_count': 1196, 'positive_rate_percent': 17.09, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'prior_delinquency_flag': {'count': 7000, 'positive_count': 1146, 'positive_rate_percent': 16.37, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'current_delinquency_flag': {'count': 7000, 'positive_count': 1123, 'positive_rate_percent': 16.04, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'autopay_enabled': {'count': 7000, 'positive_count': 4425, 'positive_rate_percent': 63.21, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'support_contact_last_30d': {'count': 7000, 'positive_count': 1411, 'positive_rate_percent': 20.16, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'hardship_program_enrolled': {'count': 7000, 'positive_count': 632, 'positive_rate_percent': 9.03, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'payment_recovery_flag': {'count': 7000, 'positive_count': 4044, 'positive_rate_percent': 57.77, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}}, 'low_cardinality_summary': {'missed_payments_last_6m': {'unique_values': 8, 'values': {0: 1645, 1: 2260, 2: 1684, 3: 880, 4: 369, 5: 116, 6: 36, 7: 10}, 'value_percent': {0: 23.5, 1: 32.29, 2: 24.06, 3: 12.57, 4: 5.27, 5: 1.66, 6: 0.51, 7: 0.14}, 'note': 'Low-cardinality numeric variable; verify whether this should be treated as categorical or ordinal.'}}, 'categorical_summary': {'region': {'count': 7000, 'missing': 0, 'unique_values': 5, 'mode': 'Tallinn', 'top_values': {'Tallinn': 2995, 'Tartu': 1517, 'Other': 973, 'Narva': 815, 'Pärnu': 700}, 'top_value_percent': {'Tallinn': 42.79, 'Tartu': 21.67, 'Other': 13.9, 'Narva': 11.64, 'Pärnu': 10.0}}, 'income_band': {'count': 7000, 'missing': 0, 'unique_values': 5, 'mode': 'mid', 'top_values': {'mid': 2319, 'lower_mid': 2309, 'low': 1257, 'upper_mid': 917, 'high': 198}, 'top_value_percent': {'mid': 33.13, 'lower_mid': 32.99, 'low': 17.96, 'upper_mid': 13.1, 'high': 2.83}}, 'employment_type': {'count': 6874, 'missing': 126, 'unique_values': 5, 'mode': 'salaried', 'top_values': {'salaried': 3966, 'self_employed': 1101, 'gig_worker': 737, 'student': 567, 'unemployed': 503}, 'top_value_percent': {'salaried': 57.7, 'self_employed': 16.02, 'gig_worker': 10.72, 'student': 8.25, 'unemployed': 7.32}}, 'risk_tier': {'count': 7000, 'missing': 0, 'unique_values': 3, 'mode': 'low_risk', 'top_values': {'low_risk': 4236, 'medium_risk': 2509, 'high_risk': 255}, 'top_value_percent': {'low_risk': 60.51, 'medium_risk': 35.84, 'high_risk': 3.64}}, 'intervention_group': {'count': 7000, 'missing': 0, 'unique_values': 4, 'mode': 'none', 'top_values': {'none': 3605, 'sms_reminder': 2141, 'repayment_call': 1053, 'hardship_outreach': 201}, 'top_value_percent': {'none': 51.5, 'sms_reminder': 30.59, 'repayment_call': 15.04, 'hardship_outreach': 2.87}}, 'repayment_plan_type': {'count': 7000, 'missing': 0, 'unique_values': 3, 'mode': 'standard', 'top_values': {'standard': 5214, 'restructured': 1275, 'grace_period': 511}, 'top_value_percent': {'standard': 74.49, 'restructured': 18.21, 'grace_period': 7.3}}}, 'technical_summary': {'autopay_enabled_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'missed_payment_last_30d_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'prior_delinquency_flag_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'current_delinquency_flag_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'hardship_program_enrolled_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'payment_recovery_flag_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'support_contact_last_30d_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'employment_type_missing_flag': {'count': 7000, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 6874, True: 126}, 'top_value_percent': {False: 98.2, True: 1.8}}, 'monthly_income_missing_flag': {'count': 7000, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 6822, True: 178}, 'top_value_percent': {False: 97.46, True: 2.54}}, 'monthly_income_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'loan_balance_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'monthly_payment_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'loan_to_income_ratio_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'credit_utilization_percent_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'missed_payments_last_6m_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'days_late_average_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'risk_score_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}, 'repayment_probability_score_invalid_flag': {'count': 7000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 7000}, 'top_value_percent': {False: 100.0}}}}

## Interpretation

# Descriptive Statistics Report
### Dataset: `fintech_repayment_inference_cleaned.csv`
### Rows: 7,000 | Columns: 48 | Duplicates: 0

---

> **Note:** This dataset was loaded from the `/cleaned/` path, indicating that a data cleaning pipeline was applied prior to this analysis. Results reflect the post-cleaning state of the data.

---

## 1. Method Used

Descriptive statistics were computed across all 48 columns. Columns were classified into: continuous numeric, binary, low-cardinality numeric, categorical, and technical/pipeline columns. The `customer_id` column was excluded from analysis as an identifier. Binary variables were summarized as proportions. Technical cleaning columns (`*_invalid_flag`, `*_missing_flag`, `*_clean`) were reserved for validation notes only.

---

## 2. Key Results

### 🔢 Continuous Numeric Variables

| Variable | Mean | Median | Mean–Median Gap | Outlier % | Skew Warning |
|---|---|---|---|---|---|
| `monthly_income` | 2,020 | 1,711 | +18.0% | 4.62% | No |
| `loan_balance` | 5,511 | 4,226 | +30.4% | 5.74% | ⚠️ Yes |
| `monthly_payment` | 393 | 264 | +49.0% | 7.41% | ⚠️ Yes |
| `loan_to_income_ratio` | 3.63 | 2.43 | +49.2% | 6.84% | ⚠️ Yes |
| `credit_utilization_percent` | 43.0 | 42.2 | +1.8% | 0.0% | No |
| `risk_score` | 0.42 | 0.41 | +2.4% | 0.66% | No |
| `days_late_average` | 5.59 | 4.80 | +16.5% | 2.31% | No |
| `repayment_probability_score` | 0.69 | 0.71 | −2.6% | 1.74% | No |

**Key observations:**
- `monthly_payment`, `loan_to_income_ratio`, and `loan_balance` show the largest mean–median divergence (30–49%), consistent with right-skewed distributions driven by a subset of high-value borrowers.
- `credit_utilization_percent`, `risk_score`, and `repayment_probability_score` are well-centred with minimal skew.
- `repayment_probability_score` has a mean of 0.69 and median of 0.71, suggesting the portfolio skews toward moderate-to-higher repayment probability.

---

### 🔵 Binary Variables (Proportions)

| Variable | Positive Rate |
|---|---|
| `autopay_enabled` | **63.2%** |
| `payment_recovery_flag` | **57.8%** |
| `support_contact_last_30d` | 20.2% |
| `missed_payment_last_30d` | 17.1% |
| `prior_delinquency_flag` | 16.4% |
| `current_delinquency_flag` | 16.0% |
| `hardship_program_enrolled` | 9.0% |

**Key observations:**
- Nearly two-thirds of customers have autopay enabled (63.2%).
- Over half the portfolio has a `payment_recovery_flag` set (57.8%) — this is notably high and warrants verification of the flag's definition before interpretation.
- Delinquency indicators (`missed_payment_last_30d`, `prior_delinquency_flag`, `current_delinquency_flag`) are tightly clustered between 16–17%, suggesting consistent overlap in the at-risk population.
- Hardship program enrollment is low at 9.0%, notably lower than the ~16–17% delinquency rate.

---

### 🔢 Low-Cardinality Numeric: `missed_payments_last_6m`

| Value | Count | % |
|---|---|---|
| 0 | 1,645 | 23.5% |
| 1 | 2,260 | 32.3% |
| 2 | 1,684 | 24.1% |
| 3 | 880 | 12.6% |
| 4 | 369 | 5.3% |
| 5 | 116 | 1.7% |
| 6 | 36 | 0.5% |
| 7 | 10 | 0.1% |

**Observation:** This variable behaves as an ordinal discrete count (0–7) rather than a continuous measure. Nearly 80% of customers have 0–2 missed payments. The distribution drops sharply beyond 3. It is best treated as ordinal or categorical in downstream modelling.

---

### 🏷️ Categorical Variables

**`region`** — 5 categories; heavily skewed toward Tallinn (42.8%), with Tartu second at 21.7%. The remaining three regions (Other, Narva, Pärnu) together account for ~35.5%.

**`income_band`** — 5 tiers; concentrated in the lower-to-middle range: `mid` (33.1%) and `lower_mid` (33.0%) together represent two-thirds of the portfolio. The `high` band is very sparse at only 198 customers (2.8%).

**`employment_type`** — 126 missing records (1.8%). Among known values, `salaried` dominates at 57.7%, followed by `self_employed` (16.0%) and `gig_worker` (10.7%).

**`risk_tier`** — Majority classified as `low_risk` (60.5%), with `medium_risk` at 35.8% and `high_risk` a small minority at 3.6%. Note that the `high_risk` segment, while small in count (255), may be disproportionately important for portfolio risk analysis.

**`intervention_group`** — Over half the population (51.5%) received no intervention. `sms_reminder` is the most common active intervention (30.6%), followed by `repayment_call` (15.0%). `hardship_outreach` is rare (2.9%).

**`repayment_plan_type`** — Predominantly `standard` (74.5%). `restructured` plans account for 18.2%, and `grace_period` for 7.3%.

---

## 3. Interpretation

- **Skewed financial variables:** The right-skewed distributions of `loan_balance`, `monthly_payment`, and `loan_to_income_ratio` indicate a minority of customers carry substantially higher financial exposure than the median borrower. Analyses using means for these variables may overstate typical values.
- **Mild delinquency concentration:** With ~16–17% flagged across three delinquency indicators, a consistent subgroup appears to be financially stressed. However, hardship program enrollment at 9% trails this rate, suggesting a potential gap in support coverage — though this cannot be interpreted causally from descriptive data alone.
- **High autopay adoption:** At 63.2%, a majority have autopay enabled, which may be relevant for repayment behaviour studies.
- **Portfolio composition:** The strong concentration of `low_risk` borrowers (60.5%) and standard repayment plans (74.5%) reflects a portfolio that is predominantly lower-risk, but the tail segments (high_risk, restructured, grace_period) merit targeted analysis.
- **Repayment probability:** A median score of 0.71 suggests a generally optimistic repayment outlook across the portfolio, though the distribution width (IQR ≈ 0.14) indicates meaningful variation.

---

## 4. Assumptions

- Column classifications (binary, continuous, categorical) are based on automated type detection and have been validated against actual value ranges.
- The `payment_recovery_flag` is assumed to be a binary indicator — its high positive rate (57.8%) should be verified against its business definition before use.
- `missed_payments_last_6m` is treated as an ordinal count variable.
- Missing values in `employment_type` (126) and `monthly_income` (178) are assumed to be missing at random pending further investigation.

---

## 5. Limitations

- **No causal claims are made.** Associations between variables (e.g., delinquency rates and hardship enrollment) cannot be attributed to any directional relationship from descriptive statistics alone.
- **Possible caps detected:** `monthly_income` has a round-number maximum of 9,500 (count: 3) and `loan_balance` has a round-number maximum of 45,000 (count: 5). These may reflect genuine values or data entry/system caps — this cannot be determined from this analysis.
- **Regional imbalance:** Tallinn represents 42.8% of the dataset. Findings may not generalise equally across all regions.
- **High-risk minority:** The `high_risk` tier (n=255, 3.6%) is small enough that subgroup analyses may lack statistical power.
- **Income band sparsity:** The `high` income band (n=198) is very thin and should be treated cautiously in any segmented analysis.
- **Missing employment and income data** affect a small but non-trivial number of records (1.8%–2.5%) and could introduce bias if not missing at random.

---

## 6. Validation Notes

All binary variables passed invalid-flag checks (0 invalid records across all 7 binary flags). No format or range violations were detected for continuous variables including `monthly_income`, `loan_balance`, `monthly_payment`, `loan_to_income_ratio`, `credit_utilization_percent`, `risk_score`, `days_late_average`, or `repayment_probability_score`. The `*_clean` binary columns match their originals, confirming cleaning did not alter core values. Missing data is correctly captured by `employment_type_missing_flag` (126 records, 1.8%) and `monthly_income_missing_flag` (178 records, 2.54%) — both consistent with the raw missing counts. Overall, data quality is considered **good**, with the only notable concerns being the potential round-number caps on `monthly_income` and `loan_balance`, and the two fields with minor missingness.

---

## 7. Recommended Follow-up

1. **Verify `payment_recovery_flag` definition** — a 57.8% positive rate is unusually high and its business meaning should be confirmed before using it as an outcome variable.
2. **Investigate round-number caps** on `monthly_income` (max = 9,500) and `loan_balance` (max = 45,000) to determine whether these are true values or system-imposed limits.
3. **Analyse missing data patterns** for `employment_type` and `monthly_income` — test whether missingness correlates with risk tier, region, or delinquency status.
4. **Treat `missed_payments_last_6m` as ordinal** in modelling; consider grouping values ≥ 4 due to sparse tail counts.
5. **Subgroup analysis** of the `high_risk` tier and `high` income band should be approached cautiously given small sample sizes.
6. **Skewed variables** (`loan_balance`, `monthly_payment`, `loan_to_income_ratio`) may benefit from log transformation or winsorisation prior to regression or inference modelling.
7. **Delinquency-to-hardship gap** (16–17% delinquency vs. 9% hardship enrollment) is a pattern worth investigating through inferential analysis.

## Validation

Status: `pass`

Warnings:
[]

Issues:
[]

## Governance Note

This report was generated by StatsAgent as an AI-assisted analytical output.

The report is intended for analytical support and validation purposes. Outputs should be reviewed by a human analyst before operational, financial, customer-impacting, or business-critical use.

Raw row-level data is not required for interpretation; the LLM interpretation layer should receive compact statistical summaries where possible.
