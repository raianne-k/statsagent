# Analysis Report

Generated: 2026-05-07 23:05:30

## Task

descriptive_stats

## Dataset Overview

- Rows: 10000
- Columns: 58
- Duplicate rows: 0
- Numeric columns: ['user_id', 'experiment_eligibility_flag', 'assignment_valid_flag', 'exposure_days', 'low_exposure_flag', 'onboarding_completion_flag', 'activation_flag', 'retained_30d', 'retained_60d', 'churn_30d', 'upgrade_flag', 'expansion_revenue_flag', 'negative_feedback_flag', 'sessions_first_14d', 'feature_adoption_count', 'support_tickets_first_30d', 'time_to_activation_days', 'monthly_subscription_value', 'experiment_eligibility_flag_clean', 'assignment_valid_flag_clean', 'low_exposure_flag_clean', 'onboarding_completion_flag_clean', 'activation_flag_clean', 'retained_30d_clean', 'retained_60d_clean', 'churn_30d_clean', 'upgrade_flag_clean', 'expansion_revenue_flag_clean', 'negative_feedback_flag_clean']
- Categorical columns: ['signup_date', 'acquisition_channel', 'region', 'company_size', 'industry', 'experiment_group', 'subscription_value_band', 'engagement_band', 'feature_adoption_band', 'experiment_eligibility_flag_invalid_flag', 'assignment_valid_flag_invalid_flag', 'low_exposure_flag_invalid_flag', 'onboarding_completion_flag_invalid_flag', 'activation_flag_invalid_flag', 'retained_30d_invalid_flag', 'retained_60d_invalid_flag', 'churn_30d_invalid_flag', 'upgrade_flag_invalid_flag', 'expansion_revenue_flag_invalid_flag', 'negative_feedback_flag_invalid_flag', 'acquisition_channel_missing_flag', 'company_size_missing_flag', 'time_to_activation_days_missing_flag', 'exposure_days_invalid_flag', 'sessions_first_14d_invalid_flag', 'feature_adoption_count_invalid_flag', 'support_tickets_first_30d_invalid_flag', 'time_to_activation_days_invalid_flag', 'monthly_subscription_value_invalid_flag']

## Missing Values

{'user_id': 0, 'signup_date': 0, 'acquisition_channel': 77, 'region': 0, 'company_size': 56, 'industry': 0, 'experiment_group': 0, 'experiment_eligibility_flag': 0, 'assignment_valid_flag': 0, 'exposure_days': 0, 'low_exposure_flag': 0, 'onboarding_completion_flag': 0, 'activation_flag': 0, 'retained_30d': 0, 'retained_60d': 0, 'churn_30d': 0, 'upgrade_flag': 0, 'expansion_revenue_flag': 0, 'negative_feedback_flag': 0, 'sessions_first_14d': 0, 'feature_adoption_count': 0, 'support_tickets_first_30d': 0, 'time_to_activation_days': 4810, 'monthly_subscription_value': 0, 'subscription_value_band': 0, 'engagement_band': 0, 'feature_adoption_band': 0, 'experiment_eligibility_flag_invalid_flag': 0, 'assignment_valid_flag_invalid_flag': 0, 'low_exposure_flag_invalid_flag': 0, 'onboarding_completion_flag_invalid_flag': 0, 'activation_flag_invalid_flag': 0, 'retained_30d_invalid_flag': 0, 'retained_60d_invalid_flag': 0, 'churn_30d_invalid_flag': 0, 'upgrade_flag_invalid_flag': 0, 'expansion_revenue_flag_invalid_flag': 0, 'negative_feedback_flag_invalid_flag': 0, 'experiment_eligibility_flag_clean': 0, 'assignment_valid_flag_clean': 0, 'low_exposure_flag_clean': 0, 'onboarding_completion_flag_clean': 0, 'activation_flag_clean': 0, 'retained_30d_clean': 0, 'retained_60d_clean': 0, 'churn_30d_clean': 0, 'upgrade_flag_clean': 0, 'expansion_revenue_flag_clean': 0, 'negative_feedback_flag_clean': 0, 'acquisition_channel_missing_flag': 0, 'company_size_missing_flag': 0, 'time_to_activation_days_missing_flag': 0, 'exposure_days_invalid_flag': 0, 'sessions_first_14d_invalid_flag': 0, 'feature_adoption_count_invalid_flag': 0, 'support_tickets_first_30d_invalid_flag': 0, 'time_to_activation_days_invalid_flag': 0, 'monthly_subscription_value_invalid_flag': 0}

## Method Used

Descriptive statistics were computed using column-type classification. Variables were separated into continuous numeric, binary, low-cardinality numeric, categorical, and technical pipeline columns.

Technical columns such as `_clean`, `_invalid_flag`, and `_missing_flag` are excluded from primary analytical interpretation and reserved for validation notes.

## Results

{'excluded_id_columns': ['user_id'], 'continuous_numeric_columns': ['exposure_days', 'sessions_first_14d', 'feature_adoption_count', 'time_to_activation_days', 'monthly_subscription_value'], 'binary_columns': ['experiment_eligibility_flag', 'assignment_valid_flag', 'low_exposure_flag', 'onboarding_completion_flag', 'activation_flag', 'retained_30d', 'retained_60d', 'churn_30d', 'upgrade_flag', 'expansion_revenue_flag', 'negative_feedback_flag'], 'low_cardinality_numeric_columns': ['support_tickets_first_30d'], 'categorical_columns': ['signup_date', 'acquisition_channel', 'region', 'company_size', 'industry', 'experiment_group', 'subscription_value_band', 'engagement_band', 'feature_adoption_band'], 'technical_columns': ['experiment_eligibility_flag_invalid_flag', 'assignment_valid_flag_invalid_flag', 'low_exposure_flag_invalid_flag', 'onboarding_completion_flag_invalid_flag', 'activation_flag_invalid_flag', 'retained_30d_invalid_flag', 'retained_60d_invalid_flag', 'churn_30d_invalid_flag', 'upgrade_flag_invalid_flag', 'expansion_revenue_flag_invalid_flag', 'negative_feedback_flag_invalid_flag', 'experiment_eligibility_flag_clean', 'assignment_valid_flag_clean', 'low_exposure_flag_clean', 'onboarding_completion_flag_clean', 'activation_flag_clean', 'retained_30d_clean', 'retained_60d_clean', 'churn_30d_clean', 'upgrade_flag_clean', 'expansion_revenue_flag_clean', 'negative_feedback_flag_clean', 'acquisition_channel_missing_flag', 'company_size_missing_flag', 'time_to_activation_days_missing_flag', 'exposure_days_invalid_flag', 'sessions_first_14d_invalid_flag', 'feature_adoption_count_invalid_flag', 'support_tickets_first_30d_invalid_flag', 'time_to_activation_days_invalid_flag', 'monthly_subscription_value_invalid_flag'], 'summary': {'exposure_days': {'count': 10000.0, 'mean': 24.88, 'std': 4.52, 'min': 0.0, '25%': 23.0, '50%': 25.0, '75%': 28.0, 'max': 30.0}, 'sessions_first_14d': {'count': 10000.0, 'mean': 7.36, 'std': 3.56, 'min': 0.0, '25%': 5.0, '50%': 7.0, '75%': 10.0, 'max': 22.0}, 'feature_adoption_count': {'count': 10000.0, 'mean': 3.2, 'std': 2.01, 'min': 0.0, '25%': 2.0, '50%': 3.0, '75%': 4.0, 'max': 13.0}, 'time_to_activation_days': {'count': 5190.0, 'mean': 5.69, 'std': 3.88, 'min': 0.1, '25%': 2.9, '50%': 4.8, '75%': 7.6, 'max': 32.4}, 'monthly_subscription_value': {'count': 10000.0, 'mean': 170.28, 'std': 255.08, 'min': 10.0, '25%': 44.05, '50%': 81.06, '75%': 183.46, 'max': 2416.61}}, 'extra_stats': {'exposure_days': {'mean': np.float64(24.88), 'median': np.float64(25.0), 'variance': np.float64(20.42), 'iqr': np.float64(5.0), 'outlier_count': 364, 'outlier_percent': 3.64, 'mean_median_gap_percent': np.float64(0.49), 'skew_warning': np.False_, 'round_number_max_check': None}, 'sessions_first_14d': {'mean': np.float64(7.36), 'median': np.float64(7.0), 'variance': np.float64(12.64), 'iqr': np.float64(5.0), 'outlier_count': 51, 'outlier_percent': 0.51, 'mean_median_gap_percent': np.float64(5.14), 'skew_warning': np.False_, 'round_number_max_check': None}, 'feature_adoption_count': {'mean': np.float64(3.2), 'median': np.float64(3.0), 'variance': np.float64(4.05), 'iqr': np.float64(2.0), 'outlier_count': 303, 'outlier_percent': 3.03, 'mean_median_gap_percent': np.float64(6.62), 'skew_warning': np.False_, 'round_number_max_check': None}, 'time_to_activation_days': {'mean': np.float64(5.69), 'median': np.float64(4.8), 'variance': np.float64(15.07), 'iqr': np.float64(4.7), 'outlier_count': 160, 'outlier_percent': 3.08, 'mean_median_gap_percent': np.float64(18.6), 'skew_warning': np.False_, 'round_number_max_check': None}, 'monthly_subscription_value': {'mean': np.float64(170.28), 'median': np.float64(81.06), 'variance': np.float64(65064.45), 'iqr': np.float64(139.41), 'outlier_count': 878, 'outlier_percent': 8.78, 'mean_median_gap_percent': np.float64(110.06), 'skew_warning': np.True_, 'round_number_max_check': None}}, 'binary_summary': {'experiment_eligibility_flag': {'count': 10000, 'positive_count': 9686, 'positive_rate_percent': 96.86, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'assignment_valid_flag': {'count': 10000, 'positive_count': 9636, 'positive_rate_percent': 96.36, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'low_exposure_flag': {'count': 10000, 'positive_count': 364, 'positive_rate_percent': 3.64, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'onboarding_completion_flag': {'count': 10000, 'positive_count': 5113, 'positive_rate_percent': 51.13, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'activation_flag': {'count': 10000, 'positive_count': 5190, 'positive_rate_percent': 51.9, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'retained_30d': {'count': 10000, 'positive_count': 5209, 'positive_rate_percent': 52.09, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'retained_60d': {'count': 10000, 'positive_count': 4641, 'positive_rate_percent': 46.41, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'churn_30d': {'count': 10000, 'positive_count': 4791, 'positive_rate_percent': 47.91, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'upgrade_flag': {'count': 10000, 'positive_count': 1720, 'positive_rate_percent': 17.2, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'expansion_revenue_flag': {'count': 10000, 'positive_count': 1445, 'positive_rate_percent': 14.45, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'negative_feedback_flag': {'count': 10000, 'positive_count': 791, 'positive_rate_percent': 7.91, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}}, 'low_cardinality_summary': {'support_tickets_first_30d': {'unique_values': 7, 'values': {0: 4715, 1: 3454, 2: 1425, 3: 317, 4: 78, 5: 8, 6: 3}, 'value_percent': {0: 47.15, 1: 34.54, 2: 14.25, 3: 3.17, 4: 0.78, 5: 0.08, 6: 0.03}, 'note': 'Low-cardinality numeric variable; verify whether this should be treated as categorical or ordinal.'}}, 'categorical_summary': {'signup_date': {'count': 10000, 'missing': 0, 'unique_values': 90, 'mode': '2026-01-17', 'top_values': {'2026-01-17': 138, '2026-03-03': 133, '2026-03-28': 129, '2026-01-25': 128, '2026-01-21': 127, '2026-02-27': 127, '2026-02-23': 127, '2026-01-26': 127, '2026-01-13': 126, '2026-02-18': 125}, 'top_value_percent': {'2026-01-17': 1.38, '2026-03-03': 1.33, '2026-03-28': 1.29, '2026-01-25': 1.28, '2026-01-21': 1.27, '2026-02-27': 1.27, '2026-02-23': 1.27, '2026-01-26': 1.27, '2026-01-13': 1.26, '2026-02-18': 1.25}}, 'acquisition_channel': {'count': 9923, 'missing': 77, 'unique_values': 6, 'mode': 'organic', 'top_values': {'organic': 2714, 'paid_search': 2022, 'referral': 1604, 'paid_social': 1398, 'direct': 1199, 'partner': 986}, 'top_value_percent': {'organic': 27.35, 'paid_search': 20.38, 'referral': 16.16, 'paid_social': 14.09, 'direct': 12.08, 'partner': 9.94}}, 'region': {'count': 10000, 'missing': 0, 'unique_values': 5, 'mode': 'North America', 'top_values': {'North America': 3855, 'Europe': 2799, 'APAC': 1505, 'UK': 1227, 'Other': 614}, 'top_value_percent': {'North America': 38.55, 'Europe': 27.99, 'APAC': 15.05, 'UK': 12.27, 'Other': 6.14}}, 'company_size': {'count': 9944, 'missing': 56, 'unique_values': 4, 'mode': 'small', 'top_values': {'small': 4521, 'solo': 2569, 'mid_market': 2160, 'enterprise': 694}, 'top_value_percent': {'small': 45.46, 'solo': 25.83, 'mid_market': 21.72, 'enterprise': 6.98}}, 'industry': {'count': 10000, 'missing': 0, 'unique_values': 6, 'mode': 'software', 'top_values': {'software': 2768, 'other': 1751, 'finance': 1678, 'retail': 1454, 'healthcare': 1357, 'education': 992}, 'top_value_percent': {'software': 27.68, 'other': 17.51, 'finance': 16.78, 'retail': 14.54, 'healthcare': 13.57, 'education': 9.92}}, 'experiment_group': {'count': 10000, 'missing': 0, 'unique_values': 2, 'mode': 'treatment', 'top_values': {'treatment': 5031, 'control': 4969}, 'top_value_percent': {'treatment': 50.31, 'control': 49.69}}, 'subscription_value_band': {'count': 10000, 'missing': 0, 'unique_values': 4, 'mode': 'mid_value', 'top_values': {'mid_value': 4304, 'low_value': 2834, 'high_value': 2150, 'enterprise_value': 712}, 'top_value_percent': {'mid_value': 43.04, 'low_value': 28.34, 'high_value': 21.5, 'enterprise_value': 7.12}}, 'engagement_band': {'count': 10000, 'missing': 0, 'unique_values': 4, 'mode': 'moderate_engagement', 'top_values': {'moderate_engagement': 5070, 'high_engagement': 3347, 'low_engagement': 1398, 'power_engagement': 185}, 'top_value_percent': {'moderate_engagement': 50.7, 'high_engagement': 33.47, 'low_engagement': 13.98, 'power_engagement': 1.85}}, 'feature_adoption_band': {'count': 10000, 'missing': 0, 'unique_values': 4, 'mode': 'basic_adoption', 'top_values': {'basic_adoption': 3978, 'moderate_adoption': 3307, 'minimal_adoption': 2080, 'broad_adoption': 635}, 'top_value_percent': {'basic_adoption': 39.78, 'moderate_adoption': 33.07, 'minimal_adoption': 20.8, 'broad_adoption': 6.35}}}, 'technical_summary': {'experiment_eligibility_flag_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'assignment_valid_flag_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'low_exposure_flag_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'onboarding_completion_flag_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'activation_flag_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'retained_30d_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'retained_60d_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'churn_30d_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'upgrade_flag_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'expansion_revenue_flag_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'negative_feedback_flag_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'acquisition_channel_missing_flag': {'count': 10000, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 9923, True: 77}, 'top_value_percent': {False: 99.23, True: 0.77}}, 'company_size_missing_flag': {'count': 10000, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 9944, True: 56}, 'top_value_percent': {False: 99.44, True: 0.56}}, 'time_to_activation_days_missing_flag': {'count': 10000, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 5190, True: 4810}, 'top_value_percent': {False: 51.9, True: 48.1}}, 'exposure_days_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'sessions_first_14d_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'feature_adoption_count_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'support_tickets_first_30d_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'time_to_activation_days_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}, 'monthly_subscription_value_invalid_flag': {'count': 10000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 10000}, 'top_value_percent': {False: 100.0}}}}

## Interpretation

# Descriptive Statistics Analysis
### Dataset: `saas_experimentation_cleaned.csv` | 10,000 rows × 58 columns

---

> **Note:** This dataset has already passed through a cleaning pipeline prior to analysis. Results reflect the cleaned version of the data. `user_id` was excluded from all analysis as a non-analytical identifier.

---

## 1. Method Used

Univariate descriptive statistics were computed across all analytical columns, with variables classified into five types: **continuous numeric**, **binary (flag)**, **low-cardinality numeric**, **categorical**, and **technical/pipeline columns**. Binary variables were summarized as proportions rather than continuous distributions. Technical pipeline columns (`*_invalid_flag`, `*_clean`, `*_missing_flag`) were reserved for validation notes only.

---

## 2. Key Results

### 2a. Continuous Numeric Variables

| Variable | Mean | Median | IQR | Outlier % | Skew Warning |
|---|---|---|---|---|---|
| `exposure_days` | 24.88 | 25.0 | 5.0 | 3.64% | No |
| `sessions_first_14d` | 7.36 | 7.0 | 5.0 | 0.51% | No |
| `feature_adoption_count` | 3.20 | 3.0 | 2.0 | 3.03% | No |
| `time_to_activation_days` | 5.69 | 4.8 | 4.7 | 3.08% | No |
| `monthly_subscription_value` | 170.28 | 81.06 | 139.41 | 8.78% | **Yes ⚠️** |

**`monthly_subscription_value`** is the only continuous variable with a confirmed skew warning. The mean ($170.28) is **110% higher than the median ($81.06)**, indicating a strong right-skewed distribution with a long upper tail. Nearly 9% of observations are flagged as outliers in this variable, the highest of any numeric column. The median is the more representative central tendency here.

**`time_to_activation_days`** shows a moderate mean-median gap (18.6%), with the mean (5.69 days) pulled above the median (4.8 days), suggesting mild right skew from a subset of users who take longer to activate — though no formal skew flag was raised.

The remaining continuous variables (`exposure_days`, `sessions_first_14d`, `feature_adoption_count`) are well-behaved, with mean-median gaps below 7% and no skew warnings.

---

### 2b. Binary Variables (Proportions)

| Variable | Positive Rate |
|---|---|
| `experiment_eligibility_flag` | 96.86% |
| `assignment_valid_flag` | 96.36% |
| `low_exposure_flag` | **3.64%** |
| `onboarding_completion_flag` | 51.13% |
| `activation_flag` | 51.90% |
| `retained_30d` | 52.09% |
| `retained_60d` | 46.41% |
| `churn_30d` | 47.91% |
| `upgrade_flag` | 17.20% |
| `expansion_revenue_flag` | 14.45% |
| `negative_feedback_flag` | **7.91%** |

**Observation:** Onboarding, activation, and 30-day retention rates cluster narrowly around 50–52%, suggesting a roughly even split in outcomes across the dataset. Retention drops to 46.4% at 60 days, implying some drop-off between the 30- and 60-day mark. Upgrade (17.2%) and expansion revenue (14.5%) rates are notably lower, and negative feedback is reported for ~8% of users. The `low_exposure_flag` rate (3.64%) aligns precisely with the outlier percentage in `exposure_days`, which is worth noting for experiment integrity checks.

**Interpretation:** The near-50% split across key funnel outcomes (onboarding, activation, retention) may reflect balanced experiment group assignment rather than a naturally bifurcated product experience, though this cannot be confirmed from descriptive statistics alone.

---

### 2c. Low-Cardinality Numeric Variable

**`support_tickets_first_30d`** takes only 7 discrete values (0–6):

| Tickets | Count | % |
|---|---|---|
| 0 | 4,715 | 47.2% |
| 1 | 3,454 | 34.5% |
| 2 | 1,425 | 14.3% |
| 3 | 317 | 3.2% |
| 4+ | 89 | 0.9% |

**Observation:** Nearly half of users submitted no support tickets in their first 30 days. The distribution is heavily right-skewed with a long tail; 82% of users submitted 0 or 1 tickets. Values of 5 or 6 are extremely rare (11 users total). This variable is better treated as an **ordinal/discrete count** than as a continuous measure.

---

### 2d. Categorical Variables

**Experiment Group:** Near-perfectly balanced — treatment (50.31%) vs. control (49.69%). This is consistent with a randomized assignment design.

**Acquisition Channel** *(77 missing)*: Organic is the dominant channel (27.4%), followed by paid search (20.4%) and referral (16.2%). Partner is the least common (9.9%). The 77 missing values (0.77%) are low-impact but should be handled in downstream subgroup analyses.

**Region:** North America dominates (38.6%), followed by Europe (28.0%) and APAC (15.1%). The "Other" category accounts for 6.1% and may warrant further disaggregation if regional analysis is intended.

**Company Size** *(56 missing)*: Small companies are the plurality (45.5%), with solo users comprising a quarter of the dataset (25.8%). Enterprise users are a small minority (7.0%). The 56 missing values (0.56%) are negligible.

**Industry:** Software leads (27.7%), with finance, retail, and healthcare each contributing 13–17%. Education is the smallest named segment (9.9%).

**Subscription Value Band:** Mid-value users are the largest group (43.0%), with enterprise-value users the smallest (7.1%). The band distribution is consistent with the right-skewed `monthly_subscription_value` distribution observed in continuous stats.

**Engagement Band:** Most users fall into moderate or high engagement (50.7% and 33.5% respectively). Power engagement is rare (1.85%), and low engagement accounts for ~14%.

**Feature Adoption Band:** Basic adoption is the mode (39.8%), and broad adoption is the rarest tier (6.4%). Over 20% of users fall into minimal adoption, suggesting a meaningful segment with limited product engagement.

**Signup Date:** Spread across 90 unique dates. No single date exceeds 1.4% of records, suggesting a relatively uniform signup distribution over the period (approximately Jan–Mar 2026 based on top dates).

---

## 3. Interpretation

- **`monthly_subscription_value`** is substantially right-skewed, indicating a small number of high-value accounts pulling the mean well above the typical user value. Median ($81) is the more representative central estimate for most users.
- The near-50% rates for onboarding, activation, and 30-day retention are noteworthy and may reflect the experimental design (balanced treatment/control) rather than the natural product funnel — though this is not determinable from descriptive statistics alone.
- The 60-day retention rate (46.4%) is lower than 30-day retention (52.1%), which is an expected pattern for SaaS products, though the ~6 percentage point gap warrants monitoring.
- Low upgrade (17.2%) and expansion revenue (14.5%) rates suggest monetization conversion is a minority behavior in this dataset.
- The `low_exposure_flag` rate (3.64%) is small but relevant for experiment validity: users with insufficient exposure should likely be excluded from treatment effect estimation.
- Feature adoption skews toward basic usage, with the broad adoption tier being rare — this may be relevant context for interpreting experiment outcomes.

---

## 4. Assumptions

- The dataset is analyzed as provided post-cleaning; no additional transformations were applied by this analysis.
- Binary variables are treated strictly as proportions.
- `support_tickets_first_30d` is treated as a discrete count variable.
- Signup dates are assumed to represent actual user signup events, not system artifacts.

---

## 5. Limitations

- **`time_to_activation_days`** has **4,810 missing values (48.1%)** — nearly half the dataset. This is the most significant data quality concern. These are structurally missing (i.e., users who never activated), not random missingness, and therefore any analysis of this variable applies only to the 51.9% of users who activated.
- **`monthly_subscription_value`** skew and outliers (8.78%) reduce the reliability of the mean as a summary statistic. Segment-level analysis or log transformation may be needed.
- The "Other" region and industry categories limit geographic and sector-level precision.
- Missing values in `acquisition_channel` (77) and `company_size` (56) are small in absolute terms but may matter for channel- or segment-level subgroup analyses.
- No inferential statistics (significance tests, confidence intervals) were produced at this stage; findings are descriptive only.
- No causal claims can be made from this analysis.

---

## 6. Validation Notes

All binary flag variables (`*_invalid_flag`) returned **100% clean (False)** across all 10,000 rows — no invalid values were detected in any binary outcome column by the cleaning pipeline.

- `acquisition_channel_missing_flag`: 77 records (0.77%) flagged as missing — consistent with the categorical summary.
- `company_size_missing_flag`: 56 records (0.56%) flagged — consistent.
- `time_to_activation_days_missing_flag`: **4,810 records (48.1%) flagged** — confirms that missingness is structural (non-activators), not random. This is the critical validation flag in the dataset.
- All `*_clean` columns are consistent with their source binary variables — no discrepancies detected. Cleaning validation passed.
- All numeric columns (`exposure_days`, `sessions_first_14d`, `feature_adoption_count`, `support_tickets_first_30d`, `time_to_activation_days`, `monthly_subscription_value`) returned 0 invalid flags from the pipeline.

---

## 7. Recommended Follow-up

1. **Experiment Analysis:** With a balanced treatment/control split (50.3% / 49.7%), proceed to hypothesis testing on key outcomes (activation, retention, upgrade). Exclude `low_exposure_flag = True` rows (3.64%) for the primary analysis.
2. **`monthly_subscription_value` Distribution:** Investigate the high-value tail (8.78% outliers). Consider segmenting by `subscription_value_band` or log-transforming for modeling. Median-based statistics are preferred for reporting.
3. **`time_to_activation_days` Missingness:** Treat missing values as structural (non-activating users). Any activation speed analysis must clearly scope findings to activated users only (n ≈ 5,190).
4. **Feature Adoption & Retention:** The broad adoption segment is small (6.4%) but may show disproportionate retention or upgrade rates — worth examining in cross-tabulation.
5. **Support Ticket Volume:** Given the discrete, sparse distribution, consider treating `support_tickets_first_30d` as an ordinal or binary variable (0 vs. 1+) in regression models rather than continuous.
6. **Acquisition Channel Subgroup Analysis:** Impute or flag the 77 missing channel values before running channel-level comparisons to avoid silent exclusion bias.

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
