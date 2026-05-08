# Analysis Report

Generated: 2026-05-07 14:37:11

## Task

descriptive_stats

## Dataset Overview

- Rows: 6000
- Columns: 46
- Duplicate rows: 0
- Numeric columns: ['account_id', 'account_age_months', 'monthly_recurring_revenue', 'seat_count', 'seats_used_percent', 'weekly_active_users', 'feature_adoption_rate', 'avg_session_minutes', 'admin_logins_last_30d', 'onboarding_completion_percent', 'days_since_last_login', 'support_tickets_last_90d', 'nps_score', 'account_health_score', 'churn_flag', 'renewal_probability', 'expansion_revenue', 'churn_flag_clean']
- Categorical columns: ['industry', 'company_size', 'region', 'contract_type', 'subscription_plan', 'nps_band', 'health_band', 'usage_band', 'revenue_band', 'login_recency_band', 'churn_flag_invalid_flag', 'nps_score_missing_flag', 'industry_missing_flag', 'account_age_months_invalid_flag', 'monthly_recurring_revenue_invalid_flag', 'seat_count_invalid_flag', 'seats_used_percent_invalid_flag', 'weekly_active_users_invalid_flag', 'feature_adoption_rate_invalid_flag', 'avg_session_minutes_invalid_flag', 'admin_logins_last_30d_invalid_flag', 'onboarding_completion_percent_invalid_flag', 'days_since_last_login_invalid_flag', 'support_tickets_last_90d_invalid_flag', 'nps_score_invalid_flag', 'account_health_score_invalid_flag', 'renewal_probability_invalid_flag', 'expansion_revenue_invalid_flag']

## Missing Values

{'account_id': 0, 'industry': 208, 'company_size': 0, 'region': 0, 'contract_type': 0, 'subscription_plan': 0, 'account_age_months': 0, 'monthly_recurring_revenue': 0, 'seat_count': 0, 'seats_used_percent': 0, 'weekly_active_users': 0, 'feature_adoption_rate': 0, 'avg_session_minutes': 0, 'admin_logins_last_30d': 0, 'onboarding_completion_percent': 0, 'days_since_last_login': 0, 'support_tickets_last_90d': 0, 'nps_score': 1018, 'nps_band': 1018, 'account_health_score': 0, 'health_band': 0, 'churn_flag': 0, 'renewal_probability': 0, 'expansion_revenue': 0, 'usage_band': 0, 'revenue_band': 0, 'login_recency_band': 0, 'churn_flag_invalid_flag': 0, 'churn_flag_clean': 0, 'nps_score_missing_flag': 0, 'industry_missing_flag': 0, 'account_age_months_invalid_flag': 0, 'monthly_recurring_revenue_invalid_flag': 0, 'seat_count_invalid_flag': 0, 'seats_used_percent_invalid_flag': 0, 'weekly_active_users_invalid_flag': 0, 'feature_adoption_rate_invalid_flag': 0, 'avg_session_minutes_invalid_flag': 0, 'admin_logins_last_30d_invalid_flag': 0, 'onboarding_completion_percent_invalid_flag': 0, 'days_since_last_login_invalid_flag': 0, 'support_tickets_last_90d_invalid_flag': 0, 'nps_score_invalid_flag': 0, 'account_health_score_invalid_flag': 0, 'renewal_probability_invalid_flag': 0, 'expansion_revenue_invalid_flag': 0}

## Method Used

Descriptive statistics were computed using column-type classification. Variables were separated into continuous numeric, binary, low-cardinality numeric, categorical, and technical pipeline columns.

Technical columns such as `_clean`, `_invalid_flag`, and `_missing_flag` are excluded from primary analytical interpretation and reserved for validation notes.

## Results

{'excluded_id_columns': ['account_id'], 'continuous_numeric_columns': ['account_age_months', 'monthly_recurring_revenue', 'seat_count', 'seats_used_percent', 'weekly_active_users', 'feature_adoption_rate', 'avg_session_minutes', 'admin_logins_last_30d', 'onboarding_completion_percent', 'days_since_last_login', 'support_tickets_last_90d', 'nps_score', 'account_health_score', 'renewal_probability', 'expansion_revenue'], 'binary_columns': ['churn_flag'], 'low_cardinality_numeric_columns': [], 'categorical_columns': ['industry', 'company_size', 'region', 'contract_type', 'subscription_plan', 'nps_band', 'health_band', 'usage_band', 'revenue_band', 'login_recency_band'], 'technical_columns': ['churn_flag_invalid_flag', 'churn_flag_clean', 'nps_score_missing_flag', 'industry_missing_flag', 'account_age_months_invalid_flag', 'monthly_recurring_revenue_invalid_flag', 'seat_count_invalid_flag', 'seats_used_percent_invalid_flag', 'weekly_active_users_invalid_flag', 'feature_adoption_rate_invalid_flag', 'avg_session_minutes_invalid_flag', 'admin_logins_last_30d_invalid_flag', 'onboarding_completion_percent_invalid_flag', 'days_since_last_login_invalid_flag', 'support_tickets_last_90d_invalid_flag', 'nps_score_invalid_flag', 'account_health_score_invalid_flag', 'renewal_probability_invalid_flag', 'expansion_revenue_invalid_flag'], 'summary': {'account_age_months': {'count': 6000.0, 'mean': 17.77, 'std': 17.2, 'min': 0.0, '25%': 5.0, '50%': 13.0, '75%': 25.0, 'max': 84.0}, 'monthly_recurring_revenue': {'count': 6000.0, 'mean': 718.2, 'std': 1515.61, 'min': 20.0, '25%': 62.17, '50%': 169.06, '75%': 534.62, 'max': 14318.05}, 'seat_count': {'count': 6000.0, 'mean': 24.97, 'std': 32.04, 'min': 1.0, '25%': 7.0, '50%': 14.0, '75%': 30.0, 'max': 153.0}, 'seats_used_percent': {'count': 6000.0, 'mean': 66.93, 'std': 17.75, 'min': 9.33, '25%': 54.73, '50%': 68.74, '75%': 80.7, 'max': 99.66}, 'weekly_active_users': {'count': 6000.0, 'mean': 7.27, 'std': 11.71, 'min': 0.0, '25%': 1.0, '50%': 3.0, '75%': 7.0, 'max': 86.0}, 'feature_adoption_rate': {'count': 6000.0, 'mean': 32.24, 'std': 15.4, 'min': 0.0, '25%': 21.7, '50%': 31.94, '75%': 42.54, 'max': 86.43}, 'avg_session_minutes': {'count': 6000.0, 'mean': 17.38, 'std': 6.43, 'min': 1.0, '25%': 12.91, '50%': 17.26, '75%': 21.8, 'max': 43.53}, 'admin_logins_last_30d': {'count': 6000.0, 'mean': 3.46, 'std': 2.11, 'min': 0.0, '25%': 2.0, '50%': 3.0, '75%': 5.0, 'max': 14.0}, 'onboarding_completion_percent': {'count': 6000.0, 'mean': 53.07, 'std': 14.16, 'min': 0.0, '25%': 43.77, '50%': 53.12, '75%': 62.52, 'max': 100.0}, 'days_since_last_login': {'count': 6000.0, 'mean': 15.87, 'std': 16.03, 'min': 0.0, '25%': 5.0, '50%': 11.0, '75%': 22.0, 'max': 157.0}, 'support_tickets_last_90d': {'count': 6000.0, 'mean': 1.77, 'std': 1.37, 'min': 0.0, '25%': 1.0, '50%': 2.0, '75%': 3.0, 'max': 9.0}, 'nps_score': {'count': 4982.0, 'mean': 31.6, 'std': 17.13, 'min': -31.0, '25%': 20.0, '50%': 32.0, '75%': 44.0, 'max': 95.0}, 'account_health_score': {'count': 6000.0, 'mean': 0.51, 'std': 0.14, 'min': 0.0, '25%': 0.42, '50%': 0.51, '75%': 0.6, 'max': 1.0}, 'renewal_probability': {'count': 6000.0, 'mean': 71.15, 'std': 10.56, 'min': 32.26, '25%': 63.82, '50%': 71.22, '75%': 78.42, 'max': 100.0}, 'expansion_revenue': {'count': 6000.0, 'mean': 142.38, 'std': 403.25, 'min': 0.0, '25%': 6.32, '50%': 21.94, '75%': 89.57, 'max': 5879.09}}, 'extra_stats': {'account_age_months': {'mean': np.float64(17.77), 'median': np.float64(13.0), 'variance': np.float64(295.88), 'iqr': np.float64(20.0), 'outlier_count': 260, 'outlier_percent': 4.33, 'mean_median_gap_percent': np.float64(36.7), 'skew_warning': np.True_, 'round_number_max_check': None}, 'monthly_recurring_revenue': {'mean': np.float64(718.2), 'median': np.float64(169.06), 'variance': np.float64(2297078.75), 'iqr': np.float64(472.46), 'outlier_count': 829, 'outlier_percent': 13.82, 'mean_median_gap_percent': np.float64(324.81), 'skew_warning': np.True_, 'round_number_max_check': None}, 'seat_count': {'mean': np.float64(24.97), 'median': np.float64(14.0), 'variance': np.float64(1026.34), 'iqr': np.float64(23.0), 'outlier_count': 525, 'outlier_percent': 8.75, 'mean_median_gap_percent': np.float64(78.38), 'skew_warning': np.True_, 'round_number_max_check': None}, 'seats_used_percent': {'mean': np.float64(66.93), 'median': np.float64(68.74), 'variance': np.float64(315.03), 'iqr': np.float64(25.98), 'outlier_count': 14, 'outlier_percent': 0.23, 'mean_median_gap_percent': np.float64(2.64), 'skew_warning': np.False_, 'round_number_max_check': None}, 'weekly_active_users': {'mean': np.float64(7.27), 'median': np.float64(3.0), 'variance': np.float64(137.17), 'iqr': np.float64(6.0), 'outlier_count': 634, 'outlier_percent': 10.57, 'mean_median_gap_percent': np.float64(142.17), 'skew_warning': np.True_, 'round_number_max_check': None}, 'feature_adoption_rate': {'mean': np.float64(32.24), 'median': np.float64(31.94), 'variance': np.float64(237.07), 'iqr': np.float64(20.84), 'outlier_count': 33, 'outlier_percent': 0.55, 'mean_median_gap_percent': np.float64(0.93), 'skew_warning': np.False_, 'round_number_max_check': None}, 'avg_session_minutes': {'mean': np.float64(17.38), 'median': np.float64(17.26), 'variance': np.float64(41.38), 'iqr': np.float64(8.89), 'outlier_count': 17, 'outlier_percent': 0.28, 'mean_median_gap_percent': np.float64(0.68), 'skew_warning': np.False_, 'round_number_max_check': None}, 'admin_logins_last_30d': {'mean': np.float64(3.46), 'median': np.float64(3.0), 'variance': np.float64(4.46), 'iqr': np.float64(3.0), 'outlier_count': 50, 'outlier_percent': 0.83, 'mean_median_gap_percent': np.float64(15.34), 'skew_warning': np.False_, 'round_number_max_check': None}, 'onboarding_completion_percent': {'mean': np.float64(53.07), 'median': np.float64(53.12), 'variance': np.float64(200.62), 'iqr': np.float64(18.76), 'outlier_count': 50, 'outlier_percent': 0.83, 'mean_median_gap_percent': np.float64(0.09), 'skew_warning': np.False_, 'round_number_max_check': {'max_value': 100.0, 'max_count': 1, 'possible_cap': False, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'days_since_last_login': {'mean': np.float64(15.87), 'median': np.float64(11.0), 'variance': np.float64(257.03), 'iqr': np.float64(17.0), 'outlier_count': 292, 'outlier_percent': 4.87, 'mean_median_gap_percent': np.float64(44.26), 'skew_warning': np.True_, 'round_number_max_check': None}, 'support_tickets_last_90d': {'mean': np.float64(1.77), 'median': np.float64(2.0), 'variance': np.float64(1.89), 'iqr': np.float64(2.0), 'outlier_count': 16, 'outlier_percent': 0.27, 'mean_median_gap_percent': np.float64(11.42), 'skew_warning': np.False_, 'round_number_max_check': None}, 'nps_score': {'mean': np.float64(31.6), 'median': np.float64(32.0), 'variance': np.float64(293.58), 'iqr': np.float64(24.0), 'outlier_count': 19, 'outlier_percent': 0.38, 'mean_median_gap_percent': np.float64(1.26), 'skew_warning': np.False_, 'round_number_max_check': None}, 'account_health_score': {'mean': np.float64(0.51), 'median': np.float64(0.51), 'variance': np.float64(0.02), 'iqr': np.float64(0.19), 'outlier_count': 17, 'outlier_percent': 0.28, 'mean_median_gap_percent': np.float64(0.53), 'skew_warning': np.False_, 'round_number_max_check': None}, 'renewal_probability': {'mean': np.float64(71.15), 'median': np.float64(71.22), 'variance': np.float64(111.51), 'iqr': np.float64(14.6), 'outlier_count': 17, 'outlier_percent': 0.28, 'mean_median_gap_percent': np.float64(0.1), 'skew_warning': np.False_, 'round_number_max_check': {'max_value': 100.0, 'max_count': 16, 'possible_cap': True, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'expansion_revenue': {'mean': np.float64(142.38), 'median': np.float64(21.94), 'variance': np.float64(162607.6), 'iqr': np.float64(83.25), 'outlier_count': 802, 'outlier_percent': 13.37, 'mean_median_gap_percent': np.float64(548.94), 'skew_warning': np.True_, 'round_number_max_check': None}}, 'binary_summary': {'churn_flag': {'count': 6000, 'positive_count': 1760, 'positive_rate_percent': 29.33, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}}, 'low_cardinality_summary': {}, 'categorical_summary': {'industry': {'count': 5792, 'missing': 208, 'unique_values': 6, 'mode': 'software', 'top_values': {'software': 1655, 'finance': 1044, 'retail': 880, 'other': 851, 'healthcare': 782, 'education': 580}, 'top_value_percent': {'software': 28.57, 'finance': 18.02, 'retail': 15.19, 'other': 14.69, 'healthcare': 13.5, 'education': 10.01}}, 'company_size': {'count': 6000, 'missing': 0, 'unique_values': 3, 'mode': 'small', 'top_values': {'small': 3573, 'mid_market': 1729, 'enterprise': 698}, 'top_value_percent': {'small': 59.55, 'mid_market': 28.82, 'enterprise': 11.63}}, 'region': {'count': 6000, 'missing': 0, 'unique_values': 5, 'mode': 'North America', 'top_values': {'North America': 2255, 'Europe': 1825, 'APAC': 828, 'UK': 727, 'Other': 365}, 'top_value_percent': {'North America': 37.58, 'Europe': 30.42, 'APAC': 13.8, 'UK': 12.12, 'Other': 6.08}}, 'contract_type': {'count': 6000, 'missing': 0, 'unique_values': 2, 'mode': 'monthly', 'top_values': {'monthly': 3606, 'annual': 2394}, 'top_value_percent': {'monthly': 60.1, 'annual': 39.9}}, 'subscription_plan': {'count': 6000, 'missing': 0, 'unique_values': 4, 'mode': 'starter', 'top_values': {'starter': 2292, 'growth': 2022, 'business': 1161, 'enterprise': 525}, 'top_value_percent': {'starter': 38.2, 'growth': 33.7, 'business': 19.35, 'enterprise': 8.75}}, 'nps_band': {'count': 4982, 'missing': 1018, 'unique_values': 3, 'mode': 'passive', 'top_values': {'passive': 4137, 'promoter': 677, 'detractor': 168}, 'top_value_percent': {'passive': 83.04, 'promoter': 13.59, 'detractor': 3.37}}, 'health_band': {'count': 6000, 'missing': 0, 'unique_values': 3, 'mode': 'medium_health', 'top_values': {'medium_health': 4595, 'high_health': 813, 'low_health': 592}, 'top_value_percent': {'medium_health': 76.58, 'high_health': 13.55, 'low_health': 9.87}}, 'usage_band': {'count': 6000, 'missing': 0, 'unique_values': 3, 'mode': 'low_usage', 'top_values': {'low_usage': 3505, 'medium_usage': 2447, 'high_usage': 48}, 'top_value_percent': {'low_usage': 58.42, 'medium_usage': 40.78, 'high_usage': 0.8}}, 'revenue_band': {'count': 6000, 'missing': 0, 'unique_values': 4, 'mode': 'mid_mrr', 'top_values': {'mid_mrr': 2240, 'low_mrr': 2206, 'high_mrr': 844, 'enterprise_mrr': 710}, 'top_value_percent': {'mid_mrr': 37.33, 'low_mrr': 36.77, 'high_mrr': 14.07, 'enterprise_mrr': 11.83}}, 'login_recency_band': {'count': 6000, 'missing': 0, 'unique_values': 4, 'mode': 'warming_8_30d', 'top_values': {'warming_8_30d': 2853, 'active_0_7d': 2265, 'inactive_31_90d': 859, 'dormant_90d_plus': 23}, 'top_value_percent': {'warming_8_30d': 47.55, 'active_0_7d': 37.75, 'inactive_31_90d': 14.32, 'dormant_90d_plus': 0.38}}}, 'technical_summary': {'churn_flag_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'nps_score_missing_flag': {'count': 6000, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 4982, True: 1018}, 'top_value_percent': {False: 83.03, True: 16.97}}, 'industry_missing_flag': {'count': 6000, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 5792, True: 208}, 'top_value_percent': {False: 96.53, True: 3.47}}, 'account_age_months_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'monthly_recurring_revenue_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'seat_count_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'seats_used_percent_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'weekly_active_users_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'feature_adoption_rate_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'avg_session_minutes_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'admin_logins_last_30d_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'onboarding_completion_percent_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'days_since_last_login_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'support_tickets_last_90d_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'nps_score_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'account_health_score_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'renewal_probability_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}, 'expansion_revenue_invalid_flag': {'count': 6000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 6000}, 'top_value_percent': {False: 100.0}}}}

## Interpretation

# Descriptive Statistics Report
## SaaS Account Dataset — `saas_account_cleaned.csv`

---

### Preliminary Note

This analysis was performed on a **pre-cleaned dataset**. Data cleaning and validation pipelines were applied prior to this descriptive pass. The `account_id` column was excluded from all analysis as a non-analytical identifier.

---

## 1. Method Used

Univariate descriptive statistics were computed across all 46 columns of a 6,000-row SaaS account dataset. Variables were classified into continuous numeric, binary, categorical, and technical pipeline columns. Summary statistics include mean, median, IQR, outlier percentage, skew warnings, and round-number cap checks for continuous variables; proportions for binary variables; and frequency distributions for categorical variables. Technical cleaning columns were reserved for validation review only.

---

## 2. Key Results

### 2a. Dataset Overview

| Attribute | Value |
|---|---|
| Rows | 6,000 |
| Columns | 46 |
| Duplicate rows | 0 |
| Columns with missing values | 2 (analytical) |

---

### 2b. Continuous Variables — Summary Table

| Variable | Mean | Median | IQR | Outlier % | Skew Warning |
|---|---|---|---|---|---|
| account_age_months | 17.77 | 13.0 | 20.0 | 4.33% | ⚠️ Yes |
| monthly_recurring_revenue | 718.20 | 169.06 | 472.46 | 13.82% | ⚠️ Yes |
| seat_count | 24.97 | 14.0 | 23.0 | 8.75% | ⚠️ Yes |
| seats_used_percent | 66.93 | 68.74 | 25.98 | 0.23% | ✅ No |
| weekly_active_users | 7.27 | 3.0 | 6.0 | 10.57% | ⚠️ Yes |
| feature_adoption_rate | 32.24 | 31.94 | 20.84 | 0.55% | ✅ No |
| avg_session_minutes | 17.38 | 17.26 | 8.89 | 0.28% | ✅ No |
| admin_logins_last_30d | 3.46 | 3.0 | 3.0 | 0.83% | ✅ No |
| onboarding_completion_percent | 53.07 | 53.12 | 18.76 | 0.83% | ✅ No |
| days_since_last_login | 15.87 | 11.0 | 17.0 | 4.87% | ⚠️ Yes |
| support_tickets_last_90d | 1.77 | 2.0 | 2.0 | 0.27% | ✅ No |
| nps_score | 31.60 | 32.0 | 24.0 | 0.38% | ✅ No |
| account_health_score | 0.51 | 0.51 | 0.19 | 0.28% | ✅ No |
| renewal_probability | 71.15 | 71.22 | 14.60 | 0.28% | ✅ No ⚠️ Cap? |
| expansion_revenue | 142.38 | 21.94 | 83.25 | 13.37% | ⚠️ Yes |

---

### 2c. Binary Variable

| Variable | Count | Positive (Churned) | Churn Rate |
|---|---|---|---|
| churn_flag | 6,000 | 1,760 | **29.33%** |

---

### 2d. Categorical Variables — Highlights

**Industry** *(208 missing, 3.47%)*
- Software dominates at 28.6%, followed by Finance (18.0%), Retail (15.2%), Other (14.7%), Healthcare (13.5%), Education (10.0%).

**Company Size**
- Heavily skewed toward small accounts: Small (59.6%), Mid-market (28.8%), Enterprise (11.6%).

**Region**
- North America (37.6%), Europe (30.4%), APAC (13.8%), UK (12.1%), Other (6.1%).

**Contract Type**
- Monthly contracts predominate (60.1%) vs. Annual (39.9%).

**Subscription Plan**
- Starter (38.2%), Growth (33.7%), Business (19.4%), Enterprise (8.8%) — a long tail from entry-level to enterprise tier.

**NPS Band** *(1,018 missing, 17.0%)*
- Of accounts with a score: Passive (83.0%), Promoter (13.6%), Detractor (3.4%).

**Health Band**
- Medium health (76.6%), High health (13.6%), Low health (9.9%).

**Usage Band**
- Low usage dominates strongly: Low (58.4%), Medium (40.8%), High (0.8%).

**Revenue Band**
- Mid MRR (37.3%) and Low MRR (36.8%) together represent ~74% of accounts.

**Login Recency Band**
- Warming/8–30d (47.6%), Active/0–7d (37.8%), Inactive/31–90d (14.3%), Dormant/90d+ (0.4%).

---

## 3. Interpretation

### Revenue is highly right-skewed with significant outliers
**Observation:** MRR has a mean of $718 against a median of $169 — a mean/median gap of 325%. Outliers account for 13.8% of records. Expansion revenue is even more extreme, with a mean of $142 vs. a median of $22 (gap of 549%), and 13.4% outliers.

**Interpretation:** A small subset of accounts likely contributes disproportionately to total revenue. Summary statistics based on means alone would substantially misrepresent the typical account. These distributions are not suitable for parametric analysis without transformation.

---

### Engagement metrics show a two-speed account base
**Observation:** Weekly active users has a mean of 7.3 but a median of just 3.0 (142% gap, 10.6% outliers). Meanwhile, `seats_used_percent` (mean 66.9%, median 68.7%) and `feature_adoption_rate` (mean 32.2%, median 31.9%) are symmetrically distributed with minimal outliers.

**Interpretation:** The seat utilization and feature adoption distributions appear broadly consistent across accounts. However, weekly active user counts are concentrated at the low end, with a smaller group of highly active accounts pulling the mean upward. This may warrant separate treatment of high-activity accounts in downstream analysis.

---

### Churn rate is materially elevated
**Observation:** 29.3% of accounts (1,760 of 6,000) carry a positive churn flag.

**Interpretation:** This is a relatively high churn signal for a SaaS portfolio. It is worth noting whether this figure reflects actual historical churn events or a forward-looking prediction label, as the interpretation differs substantially. No causal claims can be made from this proportion alone.

---

### Accounts are predominantly small, entry-level, and on monthly contracts
**Observation:** 59.6% of accounts are small companies; 38.2% are on the Starter plan; 60.1% are on monthly (not annual) contracts. Only 8.75% are on Enterprise plans.

**Interpretation:** The account base is dominated by lower-commitment customer segments. This composition may be associated with higher volatility in revenue and retention metrics, though no directional claims can be established from descriptive data alone.

---

### NPS skews heavily passive — with a large missing data caveat
**Observation:** Of the 4,982 accounts with a valid NPS score, 83.0% are classified as Passive, 13.6% as Promoter, and only 3.4% as Detractor. However, 1,018 accounts (17.0%) have no NPS score.

**Interpretation:** The near-absence of Detractors is notable and could reflect genuine satisfaction patterns or may be influenced by the non-random nature of NPS non-response (e.g., disengaged customers may be less likely to respond). Conclusions about overall NPS sentiment should be treated cautiously given the 17% missing rate.

---

### Usage is concentrated at the low end
**Observation:** 58.4% of accounts fall in the "low usage" band; only 0.8% in "high usage."

**Interpretation:** The predominance of low-usage accounts — combined with the skewed weekly active user distribution — suggests a usage concentration pattern that may warrant further segmentation. The "high usage" category represents a very small but potentially distinct group.

---

### Account maturity is right-skewed
**Observation:** Account age has a mean of 17.8 months vs. a median of 13.0 months (37% gap), with 4.3% outliers.

**Interpretation:** The account base is relatively young on average, with a subset of longer-tenured accounts pulling the mean upward. This skew means median account age is the more representative central tendency measure.

---

### Renewal probability appears tightly distributed — with a potential cap flag
**Observation:** Mean and median are nearly identical (71.15 vs. 71.22), with a narrow IQR of 14.6 points. However, 16 records sit exactly at 100.0, triggering a possible-cap warning.

**Interpretation:** The distribution is well-behaved overall, suggesting this is a model-generated or calculated score. The 16 records at exactly 100 warrant confirmation that this represents a genuine score ceiling rather than a data entry or capping artifact.

---

## 4. Assumptions

- The cleaned dataset reflects accurate source data after validation; no additional imputation is assumed.
- Binary `churn_flag` is treated as a proportion (0/1 label), not a continuous variable.
- Categorical bands (`health_band`, `usage_band`, etc.) are treated as ordinal-adjacent labels derived from underlying numeric fields.
- `nps_band` is derived from `nps_score` and shares its 1,018-record missing subset.

---

## 5. Limitations

- **Missing NPS data (17.0%)** reduces confidence in sentiment-level findings. The missing mechanism is unknown — if non-random, NPS summaries are likely biased.
- **Missing industry data (3.47%)** is modest but may affect any industry-level segmentation analysis.
- **Right-skewed revenue and usage variables** mean that mean-based summaries overstate typical account values. Medians and segment-level breakdowns are more appropriate.
- **No temporal data** is available in this snapshot — trends over time cannot be assessed.
- **Causal relationships cannot be established** from descriptive statistics. Associations between churn, usage, plan tier, or contract type require inferential analysis.
- The **"high usage" band contains only 48 accounts (0.8%)**, making that segment analytically fragile in isolation.

---

## 6. Validation Notes

All 19 technical pipeline columns (`*_invalid_flag`, `*_clean`, `*_missing_flag`) were excluded from primary analysis and reviewed here for data quality confirmation only:

| Check | Result |
|---|---|
| `churn_flag_invalid_flag` | 0 invalid records — all values passed validation |
| All other `*_invalid_flag` columns (14 fields) | 0 invalid records each — full pass across all numeric fields |
| `nps_score_missing_flag` | 1,018 flagged as missing (16.97%) — consistent with `nps_score` null count |
| `industry_missing_flag` | 208 flagged as missing (3.47%) — consistent with `industry` null count |
| `renewal_probability` max cap check | 16 records at exactly 100.0 — flagged as **possible cap**; warrants source-level verification |
| `onboarding_completion_percent` max check | 1 record at 100.0 — flagged but `possible_cap: False`; consistent with a genuine completion value |

**Overall data quality assessment: Good.** No invalid numeric records were detected post-cleaning. Missing data is concentrated in two fields (NPS and Industry) and is within manageable bounds for most analyses, though the NPS gap is material enough to require careful handling.

---

## 7. Recommended Follow-up

| Priority | Action |
|---|---|
| 🔴 High | Investigate the mechanism behind NPS non-response (17%). If non-random, consider whether imputation or sensitivity analysis is appropriate before using NPS in downstream models. |
| 🔴 High | Confirm whether `renewal_probability = 100.0` (16 records) represents a genuine maximum score or a system cap — this affects model calibration if the field is used as a target or feature. |
| 🟠 Medium | Segment revenue and expansion revenue analysis by revenue band or company size — mean-based summaries are misleading given extreme right skew. |
| 🟠 Medium | Examine churn rate (29.3%) across key segments (plan tier, contract type, health band, login recency) to identify whether churn concentration varies by account profile. |
| 🟡 Low | Validate the 48 "high usage" accounts as a distinct analytical group before drawing conclusions — the segment is too small for robust standalone comparisons. |
| 🟡 Low | Clarify the `churn_flag` definition (historical event vs. predictive label) — this materially affects how the 29.3% figure should be communicated to stakeholders. |

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
