# Analysis Report

Generated: 2026-05-07 12:44:08

## Task

descriptive_stats

## Dataset Overview

- Rows: 8000
- Columns: 33
- Duplicate rows: 0
- Numeric columns: ['customer_id', 'customer_tenure_months', 'monthly_income', 'credit_utilization_percent', 'debt_to_income_ratio', 'savings_balance', 'active_loan_amount', 'loan_term_months', 'installment_size', 'loan_to_income_ratio', 'financial_stress_score', 'app_sessions_per_week', 'avg_session_minutes', 'days_since_last_login', 'support_tickets_last_90d', 'autopay_enabled', 'number_of_products', 'promo_usage_rate', 'delinquency_flag', 'missed_payments_last_12m', 'avg_days_late', 'repayment_rate_percent']
- Categorical columns: ['region', 'acquisition_channel', 'employment_type', 'device_type', 'income_band', 'risk_band', 'engagement_band', 'utilization_band', 'savings_balance_missing_flag', 'monthly_income_invalid_flag', 'savings_balance_invalid_flag']

## Missing Values

{'customer_id': 0, 'region': 0, 'acquisition_channel': 0, 'employment_type': 225, 'device_type': 0, 'customer_tenure_months': 0, 'monthly_income': 0, 'income_band': 0, 'credit_utilization_percent': 0, 'debt_to_income_ratio': 0, 'savings_balance': 656, 'active_loan_amount': 0, 'loan_term_months': 0, 'installment_size': 0, 'loan_to_income_ratio': 0, 'financial_stress_score': 0, 'app_sessions_per_week': 0, 'avg_session_minutes': 0, 'days_since_last_login': 0, 'support_tickets_last_90d': 0, 'autopay_enabled': 0, 'number_of_products': 0, 'promo_usage_rate': 0, 'delinquency_flag': 0, 'missed_payments_last_12m': 0, 'avg_days_late': 0, 'repayment_rate_percent': 0, 'risk_band': 0, 'engagement_band': 0, 'utilization_band': 0, 'savings_balance_missing_flag': 0, 'monthly_income_invalid_flag': 0, 'savings_balance_invalid_flag': 0}

## Method Used

Descriptive statistics were computed using column-type classification. Variables were separated into continuous numeric, binary, low-cardinality numeric, categorical, and technical pipeline columns.

Technical columns such as `_clean`, `_invalid_flag`, and `_missing_flag` are excluded from primary analytical interpretation and reserved for validation notes.

## Results

{'excluded_id_columns': ['customer_id'], 'continuous_numeric_columns': ['customer_tenure_months', 'monthly_income', 'credit_utilization_percent', 'debt_to_income_ratio', 'savings_balance', 'active_loan_amount', 'installment_size', 'loan_to_income_ratio', 'financial_stress_score', 'app_sessions_per_week', 'avg_session_minutes', 'days_since_last_login', 'promo_usage_rate', 'avg_days_late', 'repayment_rate_percent'], 'binary_columns': ['autopay_enabled', 'delinquency_flag'], 'low_cardinality_numeric_columns': ['loan_term_months', 'support_tickets_last_90d', 'number_of_products', 'missed_payments_last_12m'], 'categorical_columns': ['region', 'acquisition_channel', 'employment_type', 'device_type', 'income_band', 'risk_band', 'engagement_band', 'utilization_band'], 'technical_columns': ['savings_balance_missing_flag', 'monthly_income_invalid_flag', 'savings_balance_invalid_flag'], 'summary': {'customer_tenure_months': {'count': 8000.0, 'mean': 13.75, 'std': 13.42, 'min': 0.0, '25%': 4.0, '50%': 10.0, '75%': 19.0, 'max': 72.0}, 'monthly_income': {'count': 8000.0, 'mean': 1847.36, 'std': 878.07, 'min': 350.0, '25%': 1201.36, '50%': 1751.03, '75%': 2356.32, 'max': 7409.65}, 'credit_utilization_percent': {'count': 8000.0, 'mean': 31.62, 'std': 18.02, 'min': 0.0, '25%': 18.24, '50%': 29.98, '75%': 43.43, 'max': 96.74}, 'debt_to_income_ratio': {'count': 8000.0, 'mean': 0.32, 'std': 0.13, 'min': 0.02, '25%': 0.23, '50%': 0.32, '75%': 0.41, 'max': 0.82}, 'savings_balance': {'count': 7344.0, 'mean': 1289.49, 'std': 1409.6, 'min': 24.14, '25%': 451.85, '50%': 865.08, '75%': 1593.7, 'max': 25000.0}, 'active_loan_amount': {'count': 8000.0, 'mean': 1876.2, 'std': 1738.11, 'min': 100.0, '25%': 739.84, '50%': 1367.0, '75%': 2414.68, 'max': 15000.0}, 'installment_size': {'count': 8000.0, 'mean': 230.21, 'std': 300.49, 'min': 4.17, '25%': 67.23, '50%': 136.97, '75%': 271.12, 'max': 4040.17}, 'loan_to_income_ratio': {'count': 8000.0, 'mean': 1.02, 'std': 0.75, 'min': 0.08, '25%': 0.5, '50%': 0.82, '75%': 1.31, 'max': 8.43}, 'financial_stress_score': {'count': 8000.0, 'mean': 0.22, 'std': 0.1, 'min': 0.0, '25%': 0.15, '50%': 0.21, '75%': 0.28, 'max': 1.0}, 'app_sessions_per_week': {'count': 8000.0, 'mean': 4.18, 'std': 2.14, 'min': 0.0, '25%': 3.0, '50%': 4.0, '75%': 5.0, 'max': 18.0}, 'avg_session_minutes': {'count': 8000.0, 'mean': 5.93, 'std': 2.21, 'min': 0.5, '25%': 4.41, '50%': 5.9, '75%': 7.39, 'max': 14.66}, 'days_since_last_login': {'count': 8000.0, 'mean': 8.8, 'std': 8.92, 'min': 0.0, '25%': 2.0, '50%': 6.0, '75%': 12.0, 'max': 90.0}, 'promo_usage_rate': {'count': 8000.0, 'mean': 28.06, 'std': 16.15, 'min': 0.02, '25%': 15.34, '50%': 25.9, '75%': 38.73, 'max': 85.77}, 'avg_days_late': {'count': 8000.0, 'mean': 3.74, 'std': 4.32, 'min': 0.0, '25%': 0.1, '50%': 2.5, '75%': 5.6, 'max': 37.6}, 'repayment_rate_percent': {'count': 8000.0, 'mean': 92.5, 'std': 7.82, 'min': 41.37, '25%': 89.79, '50%': 93.72, '75%': 99.0, 'max': 100.0}}, 'extra_stats': {'customer_tenure_months': {'mean': np.float64(13.75), 'median': np.float64(10.0), 'variance': np.float64(180.0), 'iqr': np.float64(15.0), 'outlier_count': 388, 'outlier_percent': 4.85, 'mean_median_gap_percent': np.float64(37.51), 'skew_warning': np.True_, 'round_number_max_check': None}, 'monthly_income': {'mean': np.float64(1847.36), 'median': np.float64(1751.03), 'variance': np.float64(771014.47), 'iqr': np.float64(1154.96), 'outlier_count': 143, 'outlier_percent': 1.79, 'mean_median_gap_percent': np.float64(5.5), 'skew_warning': np.False_, 'round_number_max_check': None}, 'credit_utilization_percent': {'mean': np.float64(31.62), 'median': np.float64(29.98), 'variance': np.float64(324.58), 'iqr': np.float64(25.19), 'outlier_count': 49, 'outlier_percent': 0.61, 'mean_median_gap_percent': np.float64(5.5), 'skew_warning': np.False_, 'round_number_max_check': None}, 'debt_to_income_ratio': {'mean': np.float64(0.32), 'median': np.float64(0.32), 'variance': np.float64(0.02), 'iqr': np.float64(0.18), 'outlier_count': 37, 'outlier_percent': 0.46, 'mean_median_gap_percent': np.float64(1.4), 'skew_warning': np.False_, 'round_number_max_check': None}, 'savings_balance': {'mean': np.float64(1289.49), 'median': np.float64(865.08), 'variance': np.float64(1986971.35), 'iqr': np.float64(1141.84), 'outlier_count': 499, 'outlier_percent': 6.79, 'mean_median_gap_percent': np.float64(49.06), 'skew_warning': np.True_, 'round_number_max_check': {'max_value': 25000.0, 'max_count': 1, 'possible_cap': False, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'active_loan_amount': {'mean': np.float64(1876.2), 'median': np.float64(1367.0), 'variance': np.float64(3021009.58), 'iqr': np.float64(1674.85), 'outlier_count': 454, 'outlier_percent': 5.67, 'mean_median_gap_percent': np.float64(37.25), 'skew_warning': np.True_, 'round_number_max_check': {'max_value': 15000.0, 'max_count': 6, 'possible_cap': True, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'installment_size': {'mean': np.float64(230.21), 'median': np.float64(136.97), 'variance': np.float64(90292.87), 'iqr': np.float64(203.89), 'outlier_count': 663, 'outlier_percent': 8.29, 'mean_median_gap_percent': np.float64(68.07), 'skew_warning': np.True_, 'round_number_max_check': None}, 'loan_to_income_ratio': {'mean': np.float64(1.02), 'median': np.float64(0.82), 'variance': np.float64(0.57), 'iqr': np.float64(0.81), 'outlier_count': 367, 'outlier_percent': 4.59, 'mean_median_gap_percent': np.float64(24.23), 'skew_warning': np.True_, 'round_number_max_check': None}, 'financial_stress_score': {'mean': np.float64(0.22), 'median': np.float64(0.21), 'variance': np.float64(0.01), 'iqr': np.float64(0.13), 'outlier_count': 210, 'outlier_percent': 2.62, 'mean_median_gap_percent': np.float64(7.84), 'skew_warning': np.False_, 'round_number_max_check': None}, 'app_sessions_per_week': {'mean': np.float64(4.18), 'median': np.float64(4.0), 'variance': np.float64(4.58), 'iqr': np.float64(2.0), 'outlier_count': 253, 'outlier_percent': 3.16, 'mean_median_gap_percent': np.float64(4.42), 'skew_warning': np.False_, 'round_number_max_check': None}, 'avg_session_minutes': {'mean': np.float64(5.93), 'median': np.float64(5.9), 'variance': np.float64(4.86), 'iqr': np.float64(2.98), 'outlier_count': 25, 'outlier_percent': 0.31, 'mean_median_gap_percent': np.float64(0.34), 'skew_warning': np.False_, 'round_number_max_check': None}, 'days_since_last_login': {'mean': np.float64(8.8), 'median': np.float64(6.0), 'variance': np.float64(79.56), 'iqr': np.float64(10.0), 'outlier_count': 346, 'outlier_percent': 4.32, 'mean_median_gap_percent': np.float64(46.69), 'skew_warning': np.True_, 'round_number_max_check': None}, 'promo_usage_rate': {'mean': np.float64(28.06), 'median': np.float64(25.9), 'variance': np.float64(260.74), 'iqr': np.float64(23.39), 'outlier_count': 42, 'outlier_percent': 0.53, 'mean_median_gap_percent': np.float64(8.31), 'skew_warning': np.False_, 'round_number_max_check': None}, 'avg_days_late': {'mean': np.float64(3.74), 'median': np.float64(2.5), 'variance': np.float64(18.68), 'iqr': np.float64(5.5), 'outlier_count': 287, 'outlier_percent': 3.59, 'mean_median_gap_percent': np.float64(49.57), 'skew_warning': np.True_, 'round_number_max_check': None}, 'repayment_rate_percent': {'mean': np.float64(92.5), 'median': np.float64(93.72), 'variance': np.float64(61.22), 'iqr': np.float64(9.21), 'outlier_count': 368, 'outlier_percent': 4.6, 'mean_median_gap_percent': np.float64(1.3), 'skew_warning': np.False_, 'round_number_max_check': {'max_value': 100.0, 'max_count': 1, 'possible_cap': False, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}}, 'binary_summary': {'autopay_enabled': {'count': 8000, 'positive_count': 5217, 'positive_rate_percent': 65.21, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'delinquency_flag': {'count': 8000, 'positive_count': 1187, 'positive_rate_percent': 14.84, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}}, 'low_cardinality_summary': {'loan_term_months': {'unique_values': 6, 'values': {3: 769, 6: 1695, 9: 1463, 12: 2284, 18: 966, 24: 823}, 'value_percent': {3: 9.61, 6: 21.19, 9: 18.29, 12: 28.55, 18: 12.08, 24: 10.29}, 'note': 'Low-cardinality numeric variable; verify whether this should be treated as categorical or ordinal.'}, 'support_tickets_last_90d': {'unique_values': 7, 'values': {0: 3739, 1: 2749, 2: 1097, 3: 312, 4: 78, 5: 22, 6: 3}, 'value_percent': {0: 46.74, 1: 34.36, 2: 13.71, 3: 3.9, 4: 0.98, 5: 0.27, 6: 0.04}, 'note': 'Low-cardinality numeric variable; verify whether this should be treated as categorical or ordinal.'}, 'number_of_products': {'unique_values': 4, 'values': {1: 4589, 2: 2156, 3: 908, 4: 347}, 'value_percent': {1: 57.36, 2: 26.95, 3: 11.35, 4: 4.34}, 'note': 'Low-cardinality numeric variable; verify whether this should be treated as categorical or ordinal.'}, 'missed_payments_last_12m': {'unique_values': 9, 'values': {0: 3374, 1: 2612, 2: 1248, 3: 469, 4: 201, 5: 73, 6: 16, 7: 4, 8: 3}, 'value_percent': {0: 42.18, 1: 32.65, 2: 15.6, 3: 5.86, 4: 2.51, 5: 0.91, 6: 0.2, 7: 0.05, 8: 0.04}, 'note': 'Low-cardinality numeric variable; verify whether this should be treated as categorical or ordinal.'}}, 'categorical_summary': {'region': {'count': 8000, 'missing': 0, 'unique_values': 5, 'mode': 'Tallinn', 'top_values': {'Tallinn': 3428, 'Tartu': 1753, 'Other': 1177, 'Narva': 847, 'Pärnu': 795}, 'top_value_percent': {'Tallinn': 42.85, 'Tartu': 21.91, 'Other': 14.71, 'Narva': 10.59, 'Pärnu': 9.94}}, 'acquisition_channel': {'count': 8000, 'missing': 0, 'unique_values': 5, 'mode': 'organic', 'top_values': {'organic': 2742, 'paid_search': 1957, 'referral': 1216, 'partner': 1142, 'social': 943}, 'top_value_percent': {'organic': 34.28, 'paid_search': 24.46, 'referral': 15.2, 'partner': 14.27, 'social': 11.79}}, 'employment_type': {'count': 7775, 'missing': 225, 'unique_values': 5, 'mode': 'salaried', 'top_values': {'salaried': 4314, 'self_employed': 1262, 'gig_worker': 898, 'student': 719, 'unemployed': 582}, 'top_value_percent': {'salaried': 55.49, 'self_employed': 16.23, 'gig_worker': 11.55, 'student': 9.25, 'unemployed': 7.49}}, 'device_type': {'count': 8000, 'missing': 0, 'unique_values': 3, 'mode': 'android', 'top_values': {'android': 4157, 'ios': 3072, 'web': 771}, 'top_value_percent': {'android': 51.96, 'ios': 38.4, 'web': 9.64}}, 'income_band': {'count': 8000, 'missing': 0, 'unique_values': 5, 'mode': 'mid', 'top_values': {'mid': 3039, 'lower_mid': 2776, 'low': 1404, 'upper_mid': 749, 'high': 32}, 'top_value_percent': {'mid': 37.99, 'lower_mid': 34.7, 'low': 17.55, 'upper_mid': 9.36, 'high': 0.4}}, 'risk_band': {'count': 8000, 'missing': 0, 'unique_values': 3, 'mode': 'low_risk', 'top_values': {'low_risk': 6897, 'medium_risk': 1078, 'high_risk': 25}, 'top_value_percent': {'low_risk': 86.21, 'medium_risk': 13.48, 'high_risk': 0.31}}, 'engagement_band': {'count': 8000, 'missing': 0, 'unique_values': 3, 'mode': 'medium_engagement', 'top_values': {'medium_engagement': 5144, 'low_engagement': 1778, 'high_engagement': 1078}, 'top_value_percent': {'medium_engagement': 64.3, 'low_engagement': 22.22, 'high_engagement': 13.48}}, 'utilization_band': {'count': 8000, 'missing': 0, 'unique_values': 3, 'mode': 'low_utilization', 'top_values': {'low_utilization': 4003, 'medium_utilization': 3782, 'high_utilization': 215}, 'top_value_percent': {'low_utilization': 50.04, 'medium_utilization': 47.28, 'high_utilization': 2.69}}}, 'technical_summary': {'savings_balance_missing_flag': {'count': 8000, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 7344, True: 656}, 'top_value_percent': {False: 91.8, True: 8.2}}, 'monthly_income_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'savings_balance_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}}}

## Interpretation

# Descriptive Statistics Report
### Dataset: `fintech_customer_cleaned.csv` — Fintech Customer Segmentation

---

> **Note:** This dataset has already passed through a cleaning pipeline. Results reflect post-cleaning distributions. The `customer_id` column was excluded from all analysis as a non-analytical identifier.

---

## 1. Method Used

Standard descriptive statistics were computed across 8,000 rows and 33 columns. Columns were classified into: continuous numeric, binary, low-cardinality numeric (discrete tiers), categorical, and technical/pipeline columns. Continuous variables were assessed for skew via mean-median gap percentage and outlier flags. Binary variables were summarized as proportions. Low-cardinality numeric columns were treated as discrete ordinal tiers. Technical pipeline columns (`*_missing_flag`, `*_invalid_flag`) are reported separately in Validation Notes only.

---

## 2. Key Results

### 📊 Dataset Overview

| Property | Value |
|---|---|
| Rows | 8,000 |
| Columns | 33 |
| Duplicate rows | 0 |
| Columns with missing values | 2 (`employment_type`: 225 missing; `savings_balance`: 656 missing) |

---

### 📈 Continuous Variables

#### Stable, Approximately Symmetric Distributions
These variables showed no skew warning and modest mean-median gaps:

| Variable | Mean | Median | IQR | Outlier % |
|---|---|---|---|---|
| `monthly_income` | 1,847 | 1,751 | 1,155 | 1.79% |
| `credit_utilization_percent` | 31.6% | 30.0% | 25.2 | 0.61% |
| `debt_to_income_ratio` | 0.32 | 0.32 | 0.18 | 0.46% |
| `financial_stress_score` | 0.22 | 0.21 | 0.13 | 2.62% |
| `app_sessions_per_week` | 4.18 | 4.0 | 2.0 | 3.16% |
| `avg_session_minutes` | 5.93 | 5.90 | 2.98 | 0.31% |
| `promo_usage_rate` | 28.1% | 25.9% | 23.4 | 0.53% |
| `repayment_rate_percent` | 92.5% | 93.7% | 9.2 | 4.6% |

**Observation:** These variables are well-behaved with low outlier rates and small mean-median gaps. `repayment_rate_percent` is slightly left-skewed (mean below median), clustering near the upper end of the scale — most customers are repaying at high rates.

---

#### ⚠️ Right-Skewed Distributions (Notable Mean-Median Gaps)

| Variable | Mean | Median | Gap % | Outlier % | Flag |
|---|---|---|---|---|---|
| `customer_tenure_months` | 13.75 | 10.0 | 37.5% | 4.85% | Skewed |
| `savings_balance` | 1,289 | 865 | 49.1% | 6.79% | Skewed + Round max |
| `active_loan_amount` | 1,876 | 1,367 | 37.3% | 5.67% | Skewed + Possible cap |
| `installment_size` | 230 | 137 | 68.1% | 8.29% | Skewed |
| `loan_to_income_ratio` | 1.02 | 0.82 | 24.2% | 4.59% | Skewed |
| `days_since_last_login` | 8.8 | 6.0 | 46.7% | 4.32% | Skewed |
| `avg_days_late` | 3.74 | 2.5 | 49.6% | 3.59% | Skewed |

**Observation:** A meaningful subset of continuous variables exhibit right skew, where a long upper tail pulls the mean above the median. This is most pronounced in `installment_size` (68% gap), `savings_balance` (49%), and `avg_days_late` (50%). The median is the more representative central tendency for these variables.

---

### 🔵 Binary Variables (Proportions)

| Variable | Positive Rate |
|---|---|
| `autopay_enabled` | **65.2%** (5,217 of 8,000) |
| `delinquency_flag` | **14.8%** (1,187 of 8,000) |

**Observation:** Nearly two-thirds of customers have autopay enabled. One in approximately seven customers (14.8%) has a delinquency flag active.

---

### 🔢 Low-Cardinality Numeric Variables (Discrete Tiers)

These variables have a small number of distinct integer values and are better interpreted as ordered tiers than continuous distributions.

**`loan_term_months`** — 6 discrete tiers:
- 12-month terms dominate (28.6%), followed by 6-month (21.2%) and 9-month (18.3%). Longer terms of 18 and 24 months are less common (~22% combined).

**`support_tickets_last_90d`** — Heavily concentrated at low counts:
- 46.7% of customers opened zero tickets; 34.4% opened one. Only ~5.2% opened 3 or more.

**`number_of_products`** — Strong single-product skew:
- 57.4% hold only 1 product; 27.0% hold 2. Just 4.3% hold all 4 products.

**`missed_payments_last_12m`** — Most customers have few or no missed payments:
- 42.2% had zero missed payments; 32.7% had one. Only ~3.7% had 4 or more.

---

### 🏷️ Categorical Variables

**Region:**
- Tallinn is the dominant region at 42.9% of customers. Tartu follows at 21.9%. Narva, Pärnu, and "Other" account for the remainder. The dataset has a pronounced Tallinn concentration.

**Acquisition Channel:**
- Organic acquisition leads at 34.3%, followed by paid search (24.5%). Referral, partner, and social channels each contribute between 12–15%.

**Employment Type** *(225 missing values — 2.8% of records)*:
- Among those recorded, salaried employees are the majority (55.5%). Self-employed (16.2%), gig workers (11.6%), students (9.3%), and unemployed (7.5%) make up the rest.

**Device Type:**
- Android users are the largest group (52.0%), followed by iOS (38.4%). Web users are a small minority (9.6%).

**Income Band:**
- The customer base is concentrated in mid and lower-mid income bands (37.9% and 34.7%, respectively). High-income customers are notably scarce — only 32 customers (0.4%).

**Risk Band:**
- The vast majority are classified as low risk (86.2%). Medium risk accounts for 13.5%, and high risk is near-absent (0.3%, 25 customers).

**Engagement Band:**
- Medium engagement is the modal category (64.3%). High engagement customers represent 13.5% — the same share as the medium-risk band, which may be a coincidence worth verifying in segmentation modeling.

**Utilization Band:**
- Low and medium utilization are roughly split (~50% and ~47%). High utilization customers are rare at 2.7%.

---

## 3. Interpretation

The customer base appears to be a relatively **young-tenure, low-to-mid income fintech population**, most of whom are performing adequately on loan obligations. A few notable patterns emerge:

- **Loan and savings distributions are right-skewed**, suggesting that a minority of customers hold disproportionately large loan amounts or savings balances. Median values are more representative for these variables.
- **Repayment behavior is broadly positive**: median repayment rate is 93.7%, 42% of customers had no missed payments in the past year, and only 14.8% carry a delinquency flag.
- **Product depth is shallow** — more than half of customers hold only one product, which may be relevant for cross-sell analysis.
- **Engagement is predominantly medium**, with high-engagement customers forming a smaller, potentially high-value subset.
- **The high-income and high-risk tiers are extremely sparse** (0.4% and 0.3% respectively), which will limit the statistical reliability of any segment-level analysis for those groups.
- **`days_since_last_login`** shows right skew (median: 6 days, mean: 8.8 days), suggesting most customers are relatively active but a tail of inactive customers pulls the average upward.

> ⚠️ **No causal claims are made.** These patterns describe the distribution of variables and should not be interpreted as explanations of customer behavior or business outcomes.

---

## 4. Assumptions

- Post-cleaning data is assumed to reflect intentional transformations applied upstream; original distributions prior to cleaning are not available for comparison.
- `savings_balance` missing values (656 records, 8.2%) were handled during the cleaning pipeline; imputation or exclusion logic is not confirmed in this analysis.
- Low-cardinality numeric columns (`loan_term_months`, `support_tickets_last_90d`, etc.) are treated as discrete ordinal tiers, not continuous variables.
- Binary variables are evaluated as proportions only.

---

## 5. Limitations

- **Missing data:** `employment_type` (225 missing, 2.8%) and `savings_balance` (656 missing, 8.2%) reduce completeness for any segment-level analysis involving these fields. If missingness is non-random, affected estimates may be biased.
- **Sparse high-end tiers:** The `high` income band (32 customers), `high_risk` risk band (25 customers), and `high_utilization` band (215 customers) are too small for reliable sub-group analysis without aggregation or resampling strategies.
- **`active_loan_amount` possible cap at 15,000:** Six customers share this exact maximum value. This may reflect a genuine product limit or a data cap — it cannot be determined from descriptive statistics alone.
- **Right-skewed variables:** Mean-based summaries for `installment_size`, `savings_balance`, `avg_days_late`, and `customer_tenure_months` overstate the typical customer value. Median and IQR are preferred for these variables.
- **Regional concentration:** With 42.9% of records from Tallinn, regional breakdowns will be underpowered for smaller regions (particularly Pärnu and Narva).
- Causality **cannot** be inferred from any of these distributions.

---

## 6. Validation Notes

| Check | Result |
|---|---|
| `monthly_income_invalid_flag` | 0 invalid records — all 8,000 monthly income values passed validation |
| `savings_balance_invalid_flag` | 0 invalid records — all non-missing savings balance values passed validation |
| `savings_balance_missing_flag` | 656 records flagged as missing (8.2%) — consistent with the raw missing count reported in the dataset overview |
| `savings_balance` round-number max (25,000) | 1 occurrence — `possible_cap: False`; flagged for manual verification but low probability of systematic cap |
| `active_loan_amount` round-number max (15,000) | 6 occurrences — `possible_cap: True`; **warrants confirmation** with the data source whether this is a product limit or encoding artifact |
| `repayment_rate_percent` max = 100.0 | 1 occurrence — natural ceiling for a percentage; no concern |
| Duplicate rows | None detected |

---

## 7. Recommended Follow-up

1. **Confirm the `active_loan_amount` cap at 15,000** with the source system or product team. If it is a hard product limit, it should be documented; if it is a data truncation artifact, affected records should be flagged.
2. **Investigate missingness in `employment_type` and `savings_balance`** — assess whether missing records cluster in any region, acquisition channel, or income band, which could indicate non-random missingness.
3. **Apply log-transformation or robust scaling** to right-skewed variables (`installment_size`, `savings_balance`, `active_loan_amount`, `avg_days_late`) before using them in any clustering or predictive model.
4. **Treat `loan_term_months` as ordinal/categorical** rather than continuous in downstream modeling, given its six discrete tiers.
5. **Evaluate the high-income and high-risk micro-segments** (32 and 25 customers respectively) — consider whether they are meaningful segments or should be merged with adjacent tiers for modeling stability.
6. **Cross-tabulate `delinquency_flag` with `missed_payments_last_12m` and `avg_days_late`** to assess internal consistency of credit risk indicators before using them jointly as segmentation features.

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
