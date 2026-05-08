# Analysis Report

Generated: 2026-05-07 21:31:19

## Task

descriptive_stats

## Dataset Overview

- Rows: 8000
- Columns: 56
- Duplicate rows: 0
- Numeric columns: ['account_id', 'monthly_recurring_revenue', 'tenure_months', 'feature_adoption_rate', 'seat_utilization_percent', 'weekly_active_users', 'login_frequency_30d', 'avg_session_duration_minutes', 'days_since_last_login', 'support_ticket_count_90d', 'unresolved_ticket_count', 'support_escalation_flag', 'onboarding_completed', 'multi_product_adoption', 'renewal_meeting_completed', 'discount_received', 'nps_score', 'account_health_score', 'churned', 'renewal_probability_score', 'churned_clean', 'multi_product_adoption_clean', 'onboarding_completed_clean', 'support_escalation_flag_clean', 'renewal_meeting_completed_clean', 'discount_received_clean']
- Categorical columns: ['region', 'industry', 'company_size', 'contract_type', 'plan_tier', 'health_band', 'usage_band', 'login_recency_band', 'revenue_band', 'churned_invalid_flag', 'multi_product_adoption_invalid_flag', 'onboarding_completed_invalid_flag', 'support_escalation_flag_invalid_flag', 'renewal_meeting_completed_invalid_flag', 'discount_received_invalid_flag', 'nps_score_missing_flag', 'account_health_score_missing_flag', 'monthly_recurring_revenue_invalid_flag', 'tenure_months_invalid_flag', 'weekly_active_users_invalid_flag', 'feature_adoption_rate_invalid_flag', 'login_frequency_30d_invalid_flag', 'avg_session_duration_minutes_invalid_flag', 'support_ticket_count_90d_invalid_flag', 'unresolved_ticket_count_invalid_flag', 'nps_score_invalid_flag', 'account_health_score_invalid_flag', 'seat_utilization_percent_invalid_flag', 'days_since_last_login_invalid_flag', 'renewal_probability_score_invalid_flag']

## Missing Values

{'account_id': 0, 'region': 0, 'industry': 0, 'company_size': 0, 'contract_type': 0, 'plan_tier': 0, 'monthly_recurring_revenue': 0, 'tenure_months': 0, 'feature_adoption_rate': 0, 'seat_utilization_percent': 0, 'weekly_active_users': 0, 'login_frequency_30d': 0, 'avg_session_duration_minutes': 0, 'days_since_last_login': 0, 'support_ticket_count_90d': 0, 'unresolved_ticket_count': 0, 'support_escalation_flag': 0, 'onboarding_completed': 0, 'multi_product_adoption': 0, 'renewal_meeting_completed': 0, 'discount_received': 0, 'nps_score': 1177, 'account_health_score': 120, 'health_band': 120, 'churned': 0, 'renewal_probability_score': 0, 'usage_band': 0, 'login_recency_band': 0, 'revenue_band': 0, 'churned_invalid_flag': 0, 'multi_product_adoption_invalid_flag': 0, 'onboarding_completed_invalid_flag': 0, 'support_escalation_flag_invalid_flag': 0, 'renewal_meeting_completed_invalid_flag': 0, 'discount_received_invalid_flag': 0, 'churned_clean': 0, 'multi_product_adoption_clean': 0, 'onboarding_completed_clean': 0, 'support_escalation_flag_clean': 0, 'renewal_meeting_completed_clean': 0, 'discount_received_clean': 0, 'nps_score_missing_flag': 0, 'account_health_score_missing_flag': 0, 'monthly_recurring_revenue_invalid_flag': 0, 'tenure_months_invalid_flag': 0, 'weekly_active_users_invalid_flag': 0, 'feature_adoption_rate_invalid_flag': 0, 'login_frequency_30d_invalid_flag': 0, 'avg_session_duration_minutes_invalid_flag': 0, 'support_ticket_count_90d_invalid_flag': 0, 'unresolved_ticket_count_invalid_flag': 0, 'nps_score_invalid_flag': 0, 'account_health_score_invalid_flag': 0, 'seat_utilization_percent_invalid_flag': 0, 'days_since_last_login_invalid_flag': 0, 'renewal_probability_score_invalid_flag': 0}

## Method Used

Descriptive statistics were computed using column-type classification. Variables were separated into continuous numeric, binary, low-cardinality numeric, categorical, and technical pipeline columns.

Technical columns such as `_clean`, `_invalid_flag`, and `_missing_flag` are excluded from primary analytical interpretation and reserved for validation notes.

## Results

{'excluded_id_columns': ['account_id'], 'continuous_numeric_columns': ['monthly_recurring_revenue', 'tenure_months', 'feature_adoption_rate', 'seat_utilization_percent', 'weekly_active_users', 'login_frequency_30d', 'avg_session_duration_minutes', 'days_since_last_login', 'support_ticket_count_90d', 'nps_score', 'account_health_score', 'renewal_probability_score'], 'binary_columns': ['support_escalation_flag', 'onboarding_completed', 'multi_product_adoption', 'renewal_meeting_completed', 'discount_received', 'churned'], 'low_cardinality_numeric_columns': ['unresolved_ticket_count'], 'categorical_columns': ['region', 'industry', 'company_size', 'contract_type', 'plan_tier', 'health_band', 'usage_band', 'login_recency_band', 'revenue_band'], 'technical_columns': ['churned_invalid_flag', 'multi_product_adoption_invalid_flag', 'onboarding_completed_invalid_flag', 'support_escalation_flag_invalid_flag', 'renewal_meeting_completed_invalid_flag', 'discount_received_invalid_flag', 'churned_clean', 'multi_product_adoption_clean', 'onboarding_completed_clean', 'support_escalation_flag_clean', 'renewal_meeting_completed_clean', 'discount_received_clean', 'nps_score_missing_flag', 'account_health_score_missing_flag', 'monthly_recurring_revenue_invalid_flag', 'tenure_months_invalid_flag', 'weekly_active_users_invalid_flag', 'feature_adoption_rate_invalid_flag', 'login_frequency_30d_invalid_flag', 'avg_session_duration_minutes_invalid_flag', 'support_ticket_count_90d_invalid_flag', 'unresolved_ticket_count_invalid_flag', 'nps_score_invalid_flag', 'account_health_score_invalid_flag', 'seat_utilization_percent_invalid_flag', 'days_since_last_login_invalid_flag', 'renewal_probability_score_invalid_flag'], 'summary': {'monthly_recurring_revenue': {'count': 8000.0, 'mean': 775.99, 'std': 1592.41, 'min': 20.0, '25%': 64.42, '50%': 175.5, '75%': 592.19, 'max': 19280.68}, 'tenure_months': {'count': 8000.0, 'mean': 18.03, 'std': 17.43, 'min': 0.0, '25%': 5.0, '50%': 13.0, '75%': 25.0, 'max': 96.0}, 'feature_adoption_rate': {'count': 8000.0, 'mean': 39.13, 'std': 17.33, 'min': 0.0, '25%': 26.87, '50%': 38.72, '75%': 51.07, 'max': 100.0}, 'seat_utilization_percent': {'count': 8000.0, 'mean': 44.13, 'std': 15.83, 'min': 0.0, '25%': 32.85, '50%': 43.51, '75%': 55.02, 'max': 100.0}, 'weekly_active_users': {'count': 8000.0, 'mean': 6.36, 'std': 5.33, 'min': 0.0, '25%': 3.0, '50%': 5.0, '75%': 8.0, 'max': 58.0}, 'login_frequency_30d': {'count': 8000.0, 'mean': 7.89, 'std': 4.27, 'min': 0.0, '25%': 5.0, '50%': 7.0, '75%': 11.0, 'max': 29.0}, 'avg_session_duration_minutes': {'count': 8000.0, 'mean': 14.0, 'std': 6.97, 'min': 1.0, '25%': 9.11, '50%': 13.89, '75%': 18.61, 'max': 40.49}, 'days_since_last_login': {'count': 8000.0, 'mean': 17.98, 'std': 18.17, 'min': 0.0, '25%': 5.0, '50%': 12.0, '75%': 25.0, 'max': 180.0}, 'support_ticket_count_90d': {'count': 8000.0, 'mean': 2.43, 'std': 1.62, 'min': 0.0, '25%': 1.0, '50%': 2.0, '75%': 3.0, 'max': 11.0}, 'nps_score': {'count': 6823.0, 'mean': 9.73, 'std': 25.56, 'min': -76.0, '25%': -8.0, '50%': 10.0, '75%': 27.0, 'max': 96.0}, 'account_health_score': {'count': 7880.0, 'mean': 43.54, 'std': 16.78, 'min': 0.0, '25%': 31.06, '50%': 43.44, '75%': 55.39, 'max': 100.0}, 'renewal_probability_score': {'count': 8000.0, 'mean': 0.65, 'std': 0.12, 'min': 0.24, '25%': 0.56, '50%': 0.65, '75%': 0.74, 'max': 1.0}}, 'extra_stats': {'monthly_recurring_revenue': {'mean': np.float64(775.99), 'median': np.float64(175.5), 'variance': np.float64(2535762.52), 'iqr': np.float64(527.77), 'outlier_count': 1146, 'outlier_percent': 14.32, 'mean_median_gap_percent': np.float64(342.17), 'skew_warning': np.True_, 'round_number_max_check': None}, 'tenure_months': {'mean': np.float64(18.03), 'median': np.float64(13.0), 'variance': np.float64(303.64), 'iqr': np.float64(20.0), 'outlier_count': 374, 'outlier_percent': 4.67, 'mean_median_gap_percent': np.float64(38.71), 'skew_warning': np.True_, 'round_number_max_check': None}, 'feature_adoption_rate': {'mean': np.float64(39.13), 'median': np.float64(38.72), 'variance': np.float64(300.27), 'iqr': np.float64(24.2), 'outlier_count': 27, 'outlier_percent': 0.34, 'mean_median_gap_percent': np.float64(1.06), 'skew_warning': np.False_, 'round_number_max_check': {'max_value': 100.0, 'max_count': 1, 'possible_cap': False, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'seat_utilization_percent': {'mean': np.float64(44.13), 'median': np.float64(43.51), 'variance': np.float64(250.49), 'iqr': np.float64(22.17), 'outlier_count': 19, 'outlier_percent': 0.24, 'mean_median_gap_percent': np.float64(1.42), 'skew_warning': np.False_, 'round_number_max_check': {'max_value': 100.0, 'max_count': 2, 'possible_cap': True, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'weekly_active_users': {'mean': np.float64(6.36), 'median': np.float64(5.0), 'variance': np.float64(28.44), 'iqr': np.float64(5.0), 'outlier_count': 471, 'outlier_percent': 5.89, 'mean_median_gap_percent': np.float64(27.16), 'skew_warning': np.True_, 'round_number_max_check': None}, 'login_frequency_30d': {'mean': np.float64(7.89), 'median': np.float64(7.0), 'variance': np.float64(18.27), 'iqr': np.float64(6.0), 'outlier_count': 50, 'outlier_percent': 0.62, 'mean_median_gap_percent': np.float64(12.75), 'skew_warning': np.False_, 'round_number_max_check': None}, 'avg_session_duration_minutes': {'mean': np.float64(14.0), 'median': np.float64(13.89), 'variance': np.float64(48.56), 'iqr': np.float64(9.5), 'outlier_count': 44, 'outlier_percent': 0.55, 'mean_median_gap_percent': np.float64(0.8), 'skew_warning': np.False_, 'round_number_max_check': None}, 'days_since_last_login': {'mean': np.float64(17.98), 'median': np.float64(12.0), 'variance': np.float64(330.14), 'iqr': np.float64(20.0), 'outlier_count': 360, 'outlier_percent': 4.5, 'mean_median_gap_percent': np.float64(49.87), 'skew_warning': np.True_, 'round_number_max_check': None}, 'support_ticket_count_90d': {'mean': np.float64(2.43), 'median': np.float64(2.0), 'variance': np.float64(2.63), 'iqr': np.float64(2.0), 'outlier_count': 132, 'outlier_percent': 1.65, 'mean_median_gap_percent': np.float64(21.38), 'skew_warning': np.True_, 'round_number_max_check': None}, 'nps_score': {'mean': np.float64(9.73), 'median': np.float64(10.0), 'variance': np.float64(653.13), 'iqr': np.float64(35.0), 'outlier_count': 29, 'outlier_percent': 0.43, 'mean_median_gap_percent': np.float64(2.73), 'skew_warning': np.False_, 'round_number_max_check': None}, 'account_health_score': {'mean': np.float64(43.54), 'median': np.float64(43.44), 'variance': np.float64(281.42), 'iqr': np.float64(24.33), 'outlier_count': 8, 'outlier_percent': 0.1, 'mean_median_gap_percent': np.float64(0.24), 'skew_warning': np.False_, 'round_number_max_check': {'max_value': 100.0, 'max_count': 1, 'possible_cap': False, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'renewal_probability_score': {'mean': np.float64(0.65), 'median': np.float64(0.65), 'variance': np.float64(0.01), 'iqr': np.float64(0.18), 'outlier_count': 3, 'outlier_percent': 0.04, 'mean_median_gap_percent': np.float64(0.05), 'skew_warning': np.False_, 'round_number_max_check': None}}, 'binary_summary': {'support_escalation_flag': {'count': 8000, 'positive_count': 1603, 'positive_rate_percent': 20.04, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'onboarding_completed': {'count': 8000, 'positive_count': 4532, 'positive_rate_percent': 56.65, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'multi_product_adoption': {'count': 8000, 'positive_count': 1931, 'positive_rate_percent': 24.14, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'renewal_meeting_completed': {'count': 8000, 'positive_count': 1993, 'positive_rate_percent': 24.91, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'discount_received': {'count': 8000, 'positive_count': 2040, 'positive_rate_percent': 25.5, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'churned': {'count': 8000, 'positive_count': 2794, 'positive_rate_percent': 34.92, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}}, 'low_cardinality_summary': {'unresolved_ticket_count': {'unique_values': 8, 'values': {0: 3662, 1: 2735, 2: 1133, 3: 366, 4: 83, 5: 18, 6: 2, 7: 1}, 'value_percent': {0: 45.78, 1: 34.19, 2: 14.16, 3: 4.58, 4: 1.04, 5: 0.22, 6: 0.02, 7: 0.01}, 'note': 'Low-cardinality numeric variable; verify whether this should be treated as categorical or ordinal.'}}, 'categorical_summary': {'region': {'count': 8000, 'missing': 0, 'unique_values': 5, 'mode': 'North America', 'top_values': {'North America': 3092, 'Europe': 2435, 'APAC': 1108, 'UK': 884, 'Other': 481}, 'top_value_percent': {'North America': 38.65, 'Europe': 30.44, 'APAC': 13.85, 'UK': 11.05, 'Other': 6.01}}, 'industry': {'count': 8000, 'missing': 0, 'unique_values': 6, 'mode': 'software', 'top_values': {'software': 2261, 'finance': 1457, 'other': 1209, 'healthcare': 1142, 'retail': 1124, 'education': 807}, 'top_value_percent': {'software': 28.26, 'finance': 18.21, 'other': 15.11, 'healthcare': 14.27, 'retail': 14.05, 'education': 10.09}}, 'company_size': {'count': 8000, 'missing': 0, 'unique_values': 3, 'mode': 'small', 'top_values': {'small': 4500, 'mid_market': 2471, 'enterprise': 1029}, 'top_value_percent': {'small': 56.25, 'mid_market': 30.89, 'enterprise': 12.86}}, 'contract_type': {'count': 8000, 'missing': 0, 'unique_values': 2, 'mode': 'monthly', 'top_values': {'monthly': 5004, 'annual': 2996}, 'top_value_percent': {'monthly': 62.55, 'annual': 37.45}}, 'plan_tier': {'count': 8000, 'missing': 0, 'unique_values': 4, 'mode': 'starter', 'top_values': {'starter': 2967, 'growth': 2656, 'business': 1580, 'enterprise': 797}, 'top_value_percent': {'starter': 37.09, 'growth': 33.2, 'business': 19.75, 'enterprise': 9.96}}, 'health_band': {'count': 7880, 'missing': 120, 'unique_values': 3, 'mode': 'medium_health', 'top_values': {'medium_health': 4012, 'low_health': 3372, 'high_health': 496}, 'top_value_percent': {'medium_health': 50.91, 'low_health': 42.79, 'high_health': 6.29}}, 'usage_band': {'count': 8000, 'missing': 0, 'unique_values': 3, 'mode': 'medium_usage', 'top_values': {'medium_usage': 4347, 'low_usage': 3323, 'high_usage': 330}, 'top_value_percent': {'medium_usage': 54.34, 'low_usage': 41.54, 'high_usage': 4.12}}, 'login_recency_band': {'count': 8000, 'missing': 0, 'unique_values': 4, 'mode': 'warming_8_30d', 'top_values': {'warming_8_30d': 3834, 'active_0_7d': 2701, 'inactive_31_90d': 1406, 'dormant_90d_plus': 59}, 'top_value_percent': {'warming_8_30d': 47.92, 'active_0_7d': 33.76, 'inactive_31_90d': 17.58, 'dormant_90d_plus': 0.74}}, 'revenue_band': {'count': 8000, 'missing': 0, 'unique_values': 4, 'mode': 'mid_mrr', 'top_values': {'mid_mrr': 2956, 'low_mrr': 2843, 'high_mrr': 1117, 'enterprise_mrr': 1084}, 'top_value_percent': {'mid_mrr': 36.95, 'low_mrr': 35.54, 'high_mrr': 13.96, 'enterprise_mrr': 13.55}}}, 'technical_summary': {'churned_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'multi_product_adoption_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'onboarding_completed_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'support_escalation_flag_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'renewal_meeting_completed_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'discount_received_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'nps_score_missing_flag': {'count': 8000, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 6823, True: 1177}, 'top_value_percent': {False: 85.29, True: 14.71}}, 'account_health_score_missing_flag': {'count': 8000, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 7880, True: 120}, 'top_value_percent': {False: 98.5, True: 1.5}}, 'monthly_recurring_revenue_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'tenure_months_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'weekly_active_users_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'feature_adoption_rate_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'login_frequency_30d_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'avg_session_duration_minutes_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'support_ticket_count_90d_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'unresolved_ticket_count_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'nps_score_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'account_health_score_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'seat_utilization_percent_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'days_since_last_login_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}, 'renewal_probability_score_invalid_flag': {'count': 8000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 8000}, 'top_value_percent': {False: 100.0}}}}

## Interpretation

# Descriptive Statistics: SaaS Churn Prediction Dataset

---

## 1. Method Used

**Descriptive statistics** were computed on a pre-cleaned dataset (`saas_churn_prediction_cleaned.csv`), meaning data cleaning and validation steps were applied prior to this analysis. The pipeline classified variables into continuous numeric, binary, low-cardinality numeric, and categorical types, applying appropriate summary methods to each. The column `account_id` was excluded as a non-analytical identifier. Technical pipeline columns (`*_invalid_flag`, `*_missing_flag`, `*_clean`) were excluded from primary interpretation and reviewed only in Validation Notes.

---

## 2. Key Results

### 📊 Dataset Overview

| Property | Value |
|---|---|
| Rows | 8,000 |
| Columns | 56 (analytical) |
| Duplicate rows | 0 |
| Key missing fields | `nps_score` (1,177 missing, 14.7%), `account_health_score` (120 missing, 1.5%) |

---

### 📈 Continuous Variables — Highlights

| Variable | Mean | Median | Skew Warning | Outlier % | Notable |
|---|---|---|---|---|---|
| `monthly_recurring_revenue` | $775.99 | $175.50 | ✅ Yes | 14.32% | Extreme right skew; mean is 342% above median |
| `tenure_months` | 18.0 | 13.0 | ✅ Yes | 4.67% | Moderate right skew |
| `days_since_last_login` | 17.98 | 12.0 | ✅ Yes | 4.5% | Right-skewed; a subset of accounts significantly inactive |
| `weekly_active_users` | 6.36 | 5.0 | ✅ Yes | 5.89% | Moderate skew with notable high-end outliers |
| `support_ticket_count_90d` | 2.43 | 2.0 | ✅ Yes | 1.65% | Mild right skew |
| `feature_adoption_rate` | 39.1% | 38.7% | ❌ No | 0.34% | Well-distributed; near-symmetric |
| `seat_utilization_percent` | 44.1% | 43.5% | ❌ No | 0.24% | Well-distributed; max = 100 (see notes) |
| `avg_session_duration_minutes` | 14.0 | 13.9 | ❌ No | 0.55% | Very symmetric and clean |
| `account_health_score` | 43.5 | 43.4 | ❌ No | 0.1% | Extremely symmetric; max = 100 (see notes) |
| `renewal_probability_score` | 0.65 | 0.65 | ❌ No | 0.04% | Tight, symmetric distribution |
| `nps_score` | 9.73 | 10.0 | ❌ No | 0.43% | Wide IQR (35 pts) despite low mean/median gap; high missingness |
| `login_frequency_30d` | 7.89 | 7.0 | ❌ No | 0.62% | Slight right skew, mild |

**Most important continuous finding:** `monthly_recurring_revenue` is severely right-skewed, with a mean-to-median gap of 342%. This indicates a small number of high-revenue accounts pulling the mean far above the typical account value. Any revenue-based averages should be interpreted with caution.

---

### 🔘 Binary Variables — Proportions

| Variable | Positive Rate |
|---|---|
| `churned` | **34.92%** — roughly 1 in 3 accounts |
| `onboarding_completed` | 56.65% — slight majority |
| `discount_received` | 25.50% |
| `renewal_meeting_completed` | 24.91% |
| `multi_product_adoption` | 24.14% |
| `support_escalation_flag` | 20.04% |

**Most important binary finding:** The churn rate of **34.9%** is high for a SaaS context and represents 2,794 churned accounts out of 8,000. Nearly **43.4% of accounts have not completed onboarding**, and only about 1 in 4 accounts have adopted multiple products or completed a renewal meeting.

---

### 🔢 Low-Cardinality Numeric Variable

**`unresolved_ticket_count`** — 8 distinct integer values (0–7):

| Value | Count | % |
|---|---|---|
| 0 | 3,662 | 45.8% |
| 1 | 2,735 | 34.2% |
| 2 | 1,133 | 14.2% |
| 3+ | 470 | 5.8% |

The distribution is heavily concentrated at 0 and 1, with values of 4+ representing under 1.3% of accounts. This variable behaves more like a discrete ordinal count than a continuous measure.

---

### 🏷️ Categorical Variables — Key Distributions

| Variable | Modal Category | Concentration |
|---|---|---|
| `region` | North America (38.7%) | Europe second at 30.4%; APAC, UK, Other account for ~31% |
| `industry` | Software (28.3%) | Finance, Healthcare, Retail, Education each 10–18% |
| `company_size` | Small (56.3%) | Mid-market 30.9%; Enterprise 12.9% |
| `contract_type` | Monthly (62.6%) | Annual at 37.5% |
| `plan_tier` | Starter (37.1%) | Growth 33.2%; Business 19.8%; Enterprise 10.0% |
| `health_band` | Medium health (51%) | Low health 42.8%; High health only 6.3% (120 missing) |
| `usage_band` | Medium usage (54.3%) | Low usage 41.5%; High usage only 4.1% |
| `login_recency_band` | Warming 8–30d (47.9%) | Active 0–7d 33.8%; Inactive 31–90d 17.6%; Dormant 0.7% |
| `revenue_band` | Mid MRR (37.0%) | Low MRR 35.5%; High and Enterprise MRR ~27% combined |

**Most important categorical finding:** The customer base is dominated by small companies (56%) on monthly contracts (63%) at starter or growth plan tiers (70%). Only **6.3% of accounts fall into the high health band**, while **42.8% are in low health** — a concerning distribution. Similarly, only 4.1% of accounts are in the high usage band.

---

## 3. Interpretation

> *Observations below reflect patterns in the data. No causal relationships are claimed.*

- **Revenue distribution is highly unequal.** The MRR mean ($776) being 342% above the median ($176) strongly suggests the dataset contains a mix of SMB accounts with low MRR and a smaller tier of high-value enterprise accounts pulling the average up. Analysis involving average revenue should account for this.

- **The churn rate of ~35% is substantial.** In the context of a churn prediction dataset, this may represent a targeted or enriched sample (not necessarily the operational churn rate), but it warrants flagging as unusually high for a typical SaaS business.

- **Account health and usage distributions skew low.** Nearly 93% of accounts are in medium or low health bands, and 96% are in medium or low usage bands. This pattern may reflect the characteristics of an at-risk customer base or a segment deliberately sampled for churn analysis.

- **Engagement metrics are moderately healthy but variable.** Login frequency and session duration are near-symmetric and stable. However, `days_since_last_login` is right-skewed (mean ~18 days, median 12 days), indicating a tail of accounts with significant inactivity.

- **Onboarding completion is below majority** for approximately 43% of accounts. Combined with low multi-product adoption (~24%), this suggests a meaningful portion of the customer base may not be fully activated.

- **NPS scores show wide variability** (IQR = 35) despite a median near 10, suggesting diverse sentiment across the customer base. The high missingness (14.7%) reduces confidence in NPS-based conclusions.

---

## 4. Assumptions

- The dataset has already been cleaned; results reflect the post-cleaning distribution.
- Binary variables are treated as proportions; no distributional assumptions are applied.
- `unresolved_ticket_count` is treated as a discrete ordinal count, not a continuous variable.
- Missing values in `nps_score` and `account_health_score` are assumed to be missing at random for descriptive purposes (this has not been tested).

---

## 5. Limitations

- **MRR skew:** The mean is not a reliable central tendency measure for `monthly_recurring_revenue`. Segment-level medians or log-transformed values should be used in any modeling context.
- **NPS missingness (14.7%):** Any analysis involving NPS score covers only ~6,823 of 8,000 accounts. If missingness is non-random (e.g., churned accounts less likely to complete surveys), NPS-based findings could be biased.
- **Health band missingness (1.5%):** 120 accounts are missing `health_band` and `account_health_score`. The cause of missingness is unknown.
- **Possible data cap on `seat_utilization_percent`:** The pipeline flagged the maximum value of 100.0 as a possible cap (2 accounts). If accounts can exceed 100% utilization, data may be artificially bounded.
- **Churn rate may not represent operational reality:** A 34.9% churn rate is atypically high for most SaaS businesses; the dataset may be a stratified or enriched sample designed for predictive modeling, not a census of all accounts.
- **Descriptive statistics alone cannot establish relationships between variables.** No cross-variable or group-level analysis has been performed here.

---

## 6. Validation Notes

All binary variable `*_invalid_flag` columns returned 0 invalid values across all 8,000 rows — confirming that `churned`, `onboarding_completed`, `multi_product_adoption`, `renewal_meeting_completed`, `discount_received`, and `support_escalation_flag` passed binary validation cleanly.

All continuous variable `*_invalid_flag` columns also returned 0 invalid values, including MRR, tenure, session duration, login metrics, and support counts.

- **`nps_score_missing_flag`:** Confirms 1,177 records (14.71%) have missing NPS scores — consistent with the raw column count.
- **`account_health_score_missing_flag`:** Confirms 120 records (1.5%) have missing health scores — consistent with raw column count.
- **`*_clean` columns:** Were validated to match their source columns; no discrepancies flagged.

---

## 7. Recommended Follow-up

| Priority | Action |
|---|---|
| 🔴 High | Investigate whether NPS missingness is associated with churned accounts — could introduce bias in any downstream model using NPS |
| 🔴 High | Segment MRR analysis by `company_size` or `revenue_band`; avoid using mean MRR as a representative value |
| 🟡 Medium | Examine `seat_utilization_percent` max values to confirm whether 100% is a genuine cap or a data artifact |
| 🟡 Medium | Conduct churn rate analysis by `health_band`, `usage_band`, `plan_tier`, and `contract_type` to identify key subgroups |
| 🟡 Medium | Investigate whether the 34.9% churn rate reflects an enriched sample or the true operational churn rate |
| 🟢 Low | Treat `unresolved_ticket_count` as ordinal/categorical in downstream modeling rather than continuous |
| 🟢 Low | Assess whether `days_since_last_login` outliers (long-inactive accounts) warrant separate treatment in predictive models |

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
