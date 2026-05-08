# Analysis Report

Generated: 2026-05-07 23:58:06

## Task

descriptive_stats

## Dataset Overview

- Rows: 22382
- Columns: 54
- Duplicate rows: 0
- Numeric columns: ['account_id', 'cohort_age_months', 'active_users', 'feature_adoption_rate', 'usage_frequency', 'support_tickets', 'days_since_last_login', 'onboarding_completion', 'product_health_score', 'rolling_health_3m', 'rolling_usage_3m', 'engagement_trend', 'usage_trend', 'monthly_recurring_revenue', 'expansion_revenue', 'revenue_trend', 'downgrade_flag', 'renewal_probability', 'churn_flag', 'revenue_at_risk', 'downgrade_flag_clean', 'churn_flag_clean']
- Categorical columns: ['snapshot_month', 'signup_month', 'cohort_month', 'plan_type', 'company_size', 'industry', 'region', 'acquisition_channel', 'health_band', 'usage_band', 'login_recency_band', 'mrr_band', 'downgrade_flag_invalid_flag', 'churn_flag_invalid_flag', 'feature_adoption_rate_missing_flag', 'usage_band_missing_flag', 'support_tickets_missing_flag', 'industry_missing_flag', 'cohort_age_months_invalid_flag', 'active_users_invalid_flag', 'feature_adoption_rate_invalid_flag', 'usage_frequency_invalid_flag', 'support_tickets_invalid_flag', 'days_since_last_login_invalid_flag', 'onboarding_completion_invalid_flag', 'product_health_score_invalid_flag', 'rolling_health_3m_invalid_flag', 'rolling_usage_3m_invalid_flag', 'monthly_recurring_revenue_invalid_flag', 'expansion_revenue_invalid_flag', 'renewal_probability_invalid_flag', 'revenue_at_risk_invalid_flag']

## Missing Values

{'account_id': 0, 'snapshot_month': 0, 'signup_month': 0, 'cohort_month': 0, 'cohort_age_months': 0, 'plan_type': 0, 'company_size': 0, 'industry': 291, 'region': 0, 'acquisition_channel': 0, 'active_users': 0, 'feature_adoption_rate': 466, 'usage_frequency': 0, 'support_tickets': 262, 'days_since_last_login': 0, 'onboarding_completion': 0, 'product_health_score': 0, 'rolling_health_3m': 0, 'rolling_usage_3m': 0, 'engagement_trend': 0, 'usage_trend': 0, 'monthly_recurring_revenue': 0, 'expansion_revenue': 0, 'revenue_trend': 0, 'downgrade_flag': 0, 'renewal_probability': 0, 'churn_flag': 0, 'revenue_at_risk': 0, 'health_band': 0, 'usage_band': 466, 'login_recency_band': 0, 'mrr_band': 0, 'downgrade_flag_invalid_flag': 0, 'churn_flag_invalid_flag': 0, 'downgrade_flag_clean': 0, 'churn_flag_clean': 0, 'feature_adoption_rate_missing_flag': 0, 'usage_band_missing_flag': 0, 'support_tickets_missing_flag': 0, 'industry_missing_flag': 0, 'cohort_age_months_invalid_flag': 0, 'active_users_invalid_flag': 0, 'feature_adoption_rate_invalid_flag': 0, 'usage_frequency_invalid_flag': 0, 'support_tickets_invalid_flag': 0, 'days_since_last_login_invalid_flag': 0, 'onboarding_completion_invalid_flag': 0, 'product_health_score_invalid_flag': 0, 'rolling_health_3m_invalid_flag': 0, 'rolling_usage_3m_invalid_flag': 0, 'monthly_recurring_revenue_invalid_flag': 0, 'expansion_revenue_invalid_flag': 0, 'renewal_probability_invalid_flag': 0, 'revenue_at_risk_invalid_flag': 0}

## Method Used

Descriptive statistics were computed using column-type classification. Variables were separated into continuous numeric, binary, low-cardinality numeric, categorical, and technical pipeline columns.

Technical columns such as `_clean`, `_invalid_flag`, and `_missing_flag` are excluded from primary analytical interpretation and reserved for validation notes.

## Results

{'excluded_id_columns': ['account_id'], 'continuous_numeric_columns': ['cohort_age_months', 'active_users', 'feature_adoption_rate', 'usage_frequency', 'support_tickets', 'days_since_last_login', 'onboarding_completion', 'product_health_score', 'rolling_health_3m', 'rolling_usage_3m', 'engagement_trend', 'usage_trend', 'monthly_recurring_revenue', 'expansion_revenue', 'revenue_trend', 'renewal_probability', 'revenue_at_risk'], 'binary_columns': ['downgrade_flag', 'churn_flag'], 'low_cardinality_numeric_columns': [], 'categorical_columns': ['snapshot_month', 'signup_month', 'cohort_month', 'plan_type', 'company_size', 'industry', 'region', 'acquisition_channel', 'health_band', 'usage_band', 'login_recency_band', 'mrr_band'], 'technical_columns': ['downgrade_flag_invalid_flag', 'churn_flag_invalid_flag', 'downgrade_flag_clean', 'churn_flag_clean', 'feature_adoption_rate_missing_flag', 'usage_band_missing_flag', 'support_tickets_missing_flag', 'industry_missing_flag', 'cohort_age_months_invalid_flag', 'active_users_invalid_flag', 'feature_adoption_rate_invalid_flag', 'usage_frequency_invalid_flag', 'support_tickets_invalid_flag', 'days_since_last_login_invalid_flag', 'onboarding_completion_invalid_flag', 'product_health_score_invalid_flag', 'rolling_health_3m_invalid_flag', 'rolling_usage_3m_invalid_flag', 'monthly_recurring_revenue_invalid_flag', 'expansion_revenue_invalid_flag', 'renewal_probability_invalid_flag', 'revenue_at_risk_invalid_flag'], 'summary': {'cohort_age_months': {'count': 22382.0, 'mean': 8.87, 'std': 7.34, 'min': 0.0, '25%': 3.0, '50%': 7.0, '75%': 13.0, 'max': 35.0}, 'active_users': {'count': 22382.0, 'mean': 23.47, 'std': 33.08, 'min': 0.0, '25%': 5.0, '50%': 11.0, '75%': 27.0, 'max': 221.0}, 'feature_adoption_rate': {'count': 21916.0, 'mean': 67.67, 'std': 15.58, 'min': 0.0, '25%': 57.1, '50%': 68.06, '75%': 78.74, 'max': 100.0}, 'usage_frequency': {'count': 22382.0, 'mean': 17.36, 'std': 4.4, 'min': 0.0, '25%': 14.34, '50%': 17.42, '75%': 20.43, 'max': 31.0}, 'support_tickets': {'count': 22120.0, 'mean': 1.29, 'std': 1.22, 'min': 0.0, '25%': 0.0, '50%': 1.0, '75%': 2.0, 'max': 12.0}, 'days_since_last_login': {'count': 22382.0, 'mean': 13.64, 'std': 15.25, 'min': 0.0, '25%': 3.0, '50%': 9.0, '75%': 19.0, 'max': 158.0}, 'onboarding_completion': {'count': 22382.0, 'mean': 75.37, 'std': 13.61, 'min': 29.78, '25%': 66.61, '50%': 75.36, '75%': 84.95, 'max': 100.0}, 'product_health_score': {'count': 22382.0, 'mean': 0.62, 'std': 0.13, 'min': 0.06, '25%': 0.53, '50%': 0.62, '75%': 0.71, 'max': 0.96}, 'rolling_health_3m': {'count': 22382.0, 'mean': 0.61, 'std': 0.12, 'min': 0.1, '25%': 0.53, '50%': 0.61, '75%': 0.7, 'max': 0.9}, 'rolling_usage_3m': {'count': 22382.0, 'mean': 17.1, 'std': 3.67, 'min': 0.9, '25%': 14.64, '50%': 17.18, '75%': 19.73, 'max': 27.52}, 'engagement_trend': {'count': 22382.0, 'mean': 0.01, 'std': 0.08, 'min': -0.36, '25%': -0.04, '50%': 0.0, '75%': 0.06, 'max': 0.36}, 'usage_trend': {'count': 22382.0, 'mean': 0.28, 'std': 4.32, 'min': -18.18, '25%': -2.45, '50%': 0.0, '75%': 3.04, 'max': 18.59}, 'monthly_recurring_revenue': {'count': 22382.0, 'mean': 1700.12, 'std': 3820.47, 'min': 31.17, '25%': 119.98, '50%': 360.33, '75%': 1216.94, 'max': 44519.76}, 'expansion_revenue': {'count': 22382.0, 'mean': 23.09, 'std': 178.65, 'min': 0.0, '25%': 0.0, '50%': 0.0, '75%': 0.0, 'max': 5665.01}, 'revenue_trend': {'count': 22382.0, 'mean': 0.01, 'std': 0.04, 'min': -0.16, '25%': 0.0, '50%': 0.0, '75%': 0.0, 'max': 0.22}, 'renewal_probability': {'count': 22382.0, 'mean': 98.32, 'std': 3.06, 'min': 72.44, '25%': 97.64, '50%': 100.0, '75%': 100.0, 'max': 100.0}, 'revenue_at_risk': {'count': 22382.0, 'mean': 24.63, 'std': 125.66, 'min': 0.0, '25%': 0.0, '50%': 0.0, '75%': 5.45, 'max': 3126.31}}, 'extra_stats': {'cohort_age_months': {'mean': np.float64(8.87), 'median': np.float64(7.0), 'variance': np.float64(53.82), 'iqr': np.float64(10.0), 'outlier_count': 286, 'outlier_percent': 1.28, 'mean_median_gap_percent': np.float64(26.73), 'skew_warning': np.True_, 'round_number_max_check': None}, 'active_users': {'mean': np.float64(23.47), 'median': np.float64(11.0), 'variance': np.float64(1094.07), 'iqr': np.float64(22.0), 'outlier_count': 2074, 'outlier_percent': 9.27, 'mean_median_gap_percent': np.float64(113.36), 'skew_warning': np.True_, 'round_number_max_check': None}, 'feature_adoption_rate': {'mean': np.float64(67.67), 'median': np.float64(68.06), 'variance': np.float64(242.74), 'iqr': np.float64(21.64), 'outlier_count': 100, 'outlier_percent': 0.46, 'mean_median_gap_percent': np.float64(0.56), 'skew_warning': np.False_, 'round_number_max_check': {'max_value': 100.0, 'max_count': 237, 'possible_cap': True, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'usage_frequency': {'mean': np.float64(17.36), 'median': np.float64(17.42), 'variance': np.float64(19.35), 'iqr': np.float64(6.09), 'outlier_count': 104, 'outlier_percent': 0.46, 'mean_median_gap_percent': np.float64(0.34), 'skew_warning': np.False_, 'round_number_max_check': None}, 'support_tickets': {'mean': np.float64(1.29), 'median': np.float64(1.0), 'variance': np.float64(1.49), 'iqr': np.float64(2.0), 'outlier_count': 116, 'outlier_percent': 0.52, 'mean_median_gap_percent': np.float64(29.35), 'skew_warning': np.True_, 'round_number_max_check': None}, 'days_since_last_login': {'mean': np.float64(13.64), 'median': np.float64(9.0), 'variance': np.float64(232.56), 'iqr': np.float64(16.0), 'outlier_count': 1106, 'outlier_percent': 4.94, 'mean_median_gap_percent': np.float64(51.6), 'skew_warning': np.True_, 'round_number_max_check': None}, 'onboarding_completion': {'mean': np.float64(75.37), 'median': np.float64(75.36), 'variance': np.float64(185.32), 'iqr': np.float64(18.34), 'outlier_count': 75, 'outlier_percent': 0.34, 'mean_median_gap_percent': np.float64(0.01), 'skew_warning': np.False_, 'round_number_max_check': {'max_value': 100.0, 'max_count': 887, 'possible_cap': True, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'product_health_score': {'mean': np.float64(0.62), 'median': np.float64(0.62), 'variance': np.float64(0.02), 'iqr': np.float64(0.18), 'outlier_count': 95, 'outlier_percent': 0.42, 'mean_median_gap_percent': np.float64(0.53), 'skew_warning': np.False_, 'round_number_max_check': None}, 'rolling_health_3m': {'mean': np.float64(0.61), 'median': np.float64(0.61), 'variance': np.float64(0.01), 'iqr': np.float64(0.17), 'outlier_count': 73, 'outlier_percent': 0.33, 'mean_median_gap_percent': np.float64(0.32), 'skew_warning': np.False_, 'round_number_max_check': None}, 'rolling_usage_3m': {'mean': np.float64(17.1), 'median': np.float64(17.18), 'variance': np.float64(13.45), 'iqr': np.float64(5.09), 'outlier_count': 111, 'outlier_percent': 0.5, 'mean_median_gap_percent': np.float64(0.48), 'skew_warning': np.False_, 'round_number_max_check': None}, 'engagement_trend': {'mean': np.float64(0.01), 'median': np.float64(0.0), 'variance': np.float64(0.01), 'iqr': np.float64(0.1), 'outlier_count': 363, 'outlier_percent': 1.62, 'mean_median_gap_percent': None, 'skew_warning': False, 'round_number_max_check': None}, 'usage_trend': {'mean': np.float64(0.28), 'median': np.float64(0.0), 'variance': np.float64(18.67), 'iqr': np.float64(5.49), 'outlier_count': 298, 'outlier_percent': 1.33, 'mean_median_gap_percent': None, 'skew_warning': False, 'round_number_max_check': None}, 'monthly_recurring_revenue': {'mean': np.float64(1700.12), 'median': np.float64(360.33), 'variance': np.float64(14596018.61), 'iqr': np.float64(1096.96), 'outlier_count': 3204, 'outlier_percent': 14.32, 'mean_median_gap_percent': np.float64(371.82), 'skew_warning': np.True_, 'round_number_max_check': None}, 'expansion_revenue': {'mean': np.float64(23.09), 'median': np.float64(0.0), 'variance': np.float64(31915.37), 'iqr': np.float64(0.0), 'outlier_count': 2465, 'outlier_percent': 11.01, 'mean_median_gap_percent': None, 'skew_warning': False, 'round_number_max_check': None}, 'revenue_trend': {'mean': np.float64(0.01), 'median': np.float64(0.0), 'variance': np.float64(0.0), 'iqr': np.float64(0.0), 'outlier_count': 3599, 'outlier_percent': 16.08, 'mean_median_gap_percent': None, 'skew_warning': False, 'round_number_max_check': None}, 'renewal_probability': {'mean': np.float64(98.32), 'median': np.float64(100.0), 'variance': np.float64(9.34), 'iqr': np.float64(2.36), 'outlier_count': 2218, 'outlier_percent': 9.91, 'mean_median_gap_percent': np.float64(1.68), 'skew_warning': np.False_, 'round_number_max_check': {'max_value': 100.0, 'max_count': 13383, 'possible_cap': True, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'revenue_at_risk': {'mean': np.float64(24.63), 'median': np.float64(0.0), 'variance': np.float64(15789.86), 'iqr': np.float64(5.45), 'outlier_count': 3772, 'outlier_percent': 16.85, 'mean_median_gap_percent': None, 'skew_warning': False, 'round_number_max_check': None}}, 'binary_summary': {'downgrade_flag': {'count': 22382, 'positive_count': 831, 'positive_rate_percent': 3.71, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'churn_flag': {'count': 22382, 'positive_count': 875, 'positive_rate_percent': 3.91, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}}, 'low_cardinality_summary': {}, 'categorical_summary': {'snapshot_month': {'count': 22382, 'missing': 0, 'unique_values': 36, 'mode': '2024-12-01', 'top_values': {'2024-12-01': 965, '2024-10-01': 951, '2024-11-01': 950, '2024-09-01': 941, '2024-06-01': 940, '2024-08-01': 938, '2024-07-01': 928, '2024-05-01': 912, '2024-04-01': 895, '2024-03-01': 880}, 'top_value_percent': {'2024-12-01': 4.31, '2024-10-01': 4.25, '2024-11-01': 4.24, '2024-09-01': 4.2, '2024-06-01': 4.2, '2024-08-01': 4.19, '2024-07-01': 4.15, '2024-05-01': 4.07, '2024-04-01': 4.0, '2024-03-01': 3.93}}, 'signup_month': {'count': 22382, 'missing': 0, 'unique_values': 36, 'mode': '2023-01-01', 'top_values': {'2023-01-01': 1083, '2022-05-01': 1073, '2023-02-01': 1018, '2022-08-01': 977, '2023-05-01': 934, '2022-09-01': 927, '2022-02-01': 902, '2022-06-01': 888, '2022-04-01': 864, '2023-04-01': 808}, 'top_value_percent': {'2023-01-01': 4.84, '2022-05-01': 4.79, '2023-02-01': 4.55, '2022-08-01': 4.37, '2023-05-01': 4.17, '2022-09-01': 4.14, '2022-02-01': 4.03, '2022-06-01': 3.97, '2022-04-01': 3.86, '2023-04-01': 3.61}}, 'cohort_month': {'count': 22382, 'missing': 0, 'unique_values': 36, 'mode': '2023-01-01', 'top_values': {'2023-01-01': 1083, '2022-05-01': 1073, '2023-02-01': 1018, '2022-08-01': 977, '2023-05-01': 934, '2022-09-01': 927, '2022-02-01': 902, '2022-06-01': 888, '2022-04-01': 864, '2023-04-01': 808}, 'top_value_percent': {'2023-01-01': 4.84, '2022-05-01': 4.79, '2023-02-01': 4.55, '2022-08-01': 4.37, '2023-05-01': 4.17, '2022-09-01': 4.14, '2022-02-01': 4.03, '2022-06-01': 3.97, '2022-04-01': 3.86, '2023-04-01': 3.61}}, 'plan_type': {'count': 22382, 'missing': 0, 'unique_values': 4, 'mode': 'starter', 'top_values': {'starter': 8018, 'growth': 7840, 'business': 4411, 'enterprise': 2113}, 'top_value_percent': {'starter': 35.82, 'growth': 35.03, 'business': 19.71, 'enterprise': 9.44}}, 'company_size': {'count': 22382, 'missing': 0, 'unique_values': 3, 'mode': 'small', 'top_values': {'small': 11767, 'mid_market': 7782, 'enterprise': 2833}, 'top_value_percent': {'small': 52.57, 'mid_market': 34.77, 'enterprise': 12.66}}, 'industry': {'count': 22091, 'missing': 291, 'unique_values': 6, 'mode': 'software', 'top_values': {'software': 6629, 'finance': 3591, 'other': 3577, 'retail': 3300, 'healthcare': 2943, 'education': 2051}, 'top_value_percent': {'software': 30.01, 'finance': 16.26, 'other': 16.19, 'retail': 14.94, 'healthcare': 13.32, 'education': 9.28}}, 'region': {'count': 22382, 'missing': 0, 'unique_values': 5, 'mode': 'North America', 'top_values': {'North America': 8752, 'Europe': 6546, 'APAC': 3382, 'UK': 2507, 'Other': 1195}, 'top_value_percent': {'North America': 39.1, 'Europe': 29.25, 'APAC': 15.11, 'UK': 11.2, 'Other': 5.34}}, 'acquisition_channel': {'count': 22382, 'missing': 0, 'unique_values': 5, 'mode': 'organic', 'top_values': {'organic': 7664, 'paid_search': 5325, 'sales_outbound': 3451, 'partner': 3260, 'referral': 2682}, 'top_value_percent': {'organic': 34.24, 'paid_search': 23.79, 'sales_outbound': 15.42, 'partner': 14.57, 'referral': 11.98}}, 'health_band': {'count': 22382, 'missing': 0, 'unique_values': 3, 'mode': 'medium_health', 'top_values': {'medium_health': 12785, 'high_health': 9117, 'low_health': 480}, 'top_value_percent': {'medium_health': 57.12, 'high_health': 40.73, 'low_health': 2.14}}, 'usage_band': {'count': 21916, 'missing': 466, 'unique_values': 3, 'mode': 'medium_usage', 'top_values': {'medium_usage': 11584, 'high_usage': 9859, 'low_usage': 473}, 'top_value_percent': {'medium_usage': 52.86, 'high_usage': 44.99, 'low_usage': 2.16}}, 'login_recency_band': {'count': 22382, 'missing': 0, 'unique_values': 4, 'mode': 'active_0_7d', 'top_values': {'active_0_7d': 10083, 'warming_8_30d': 9804, 'inactive_31_90d': 2415, 'dormant_90d_plus': 80}, 'top_value_percent': {'active_0_7d': 45.05, 'warming_8_30d': 43.8, 'inactive_31_90d': 10.79, 'dormant_90d_plus': 0.36}}, 'mrr_band': {'count': 22382, 'missing': 0, 'unique_values': 4, 'mode': 'low_mrr', 'top_values': {'low_mrr': 9230, 'mid_mrr': 6798, 'high_mrr': 4344, 'enterprise_mrr': 2010}, 'top_value_percent': {'low_mrr': 41.24, 'mid_mrr': 30.37, 'high_mrr': 19.41, 'enterprise_mrr': 8.98}}}, 'technical_summary': {'downgrade_flag_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'churn_flag_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'feature_adoption_rate_missing_flag': {'count': 22382, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 21916, True: 466}, 'top_value_percent': {False: 97.92, True: 2.08}}, 'usage_band_missing_flag': {'count': 22382, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 21916, True: 466}, 'top_value_percent': {False: 97.92, True: 2.08}}, 'support_tickets_missing_flag': {'count': 22382, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 22120, True: 262}, 'top_value_percent': {False: 98.83, True: 1.17}}, 'industry_missing_flag': {'count': 22382, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 22091, True: 291}, 'top_value_percent': {False: 98.7, True: 1.3}}, 'cohort_age_months_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'active_users_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'feature_adoption_rate_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'usage_frequency_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'support_tickets_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'days_since_last_login_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'onboarding_completion_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'product_health_score_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'rolling_health_3m_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'rolling_usage_3m_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'monthly_recurring_revenue_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'expansion_revenue_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'renewal_probability_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}, 'revenue_at_risk_invalid_flag': {'count': 22382, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 22382}, 'top_value_percent': {False: 100.0}}}}

## Interpretation

# Descriptive Statistics Analysis
## SaaS Account Monthly Dataset — `saas_account_monthly_cleaned.csv`

> **Note:** This dataset has already passed through a cleaning pipeline prior to analysis. Results reflect the cleaned version of the data. The `account_id` column was excluded from all analysis as a non-analytical identifier.

---

## 1. Method Used

Full descriptive statistics were computed across 22,382 rows and 54 columns. Columns were classified into continuous numeric, binary, categorical, and technical cleaning categories. Continuous variables were assessed for mean/median divergence, skew, outlier prevalence, and suspicious cap values. Binary variables were summarized as proportions. Categorical variables were summarized by mode and top-value frequency distributions. Technical pipeline columns were excluded from primary analysis and reviewed separately in Validation Notes.

---

## 2. Key Results

### Dataset Overview

| Attribute | Value |
|---|---|
| Total rows | 22,382 |
| Total columns | 54 |
| Duplicate rows | 0 |
| Columns with missing data | 4 (industry, feature_adoption_rate, support_tickets, usage_band) |

---

### Continuous Variables — Highlights

#### 🔴 High-Priority Distributional Concerns

**`monthly_recurring_revenue` (MRR)**
- Mean: **$1,700**, Median: **$360** — a mean/median gap of **372%**
- IQR: $1,097 | Outlier rate: **14.32%**
- **Observation:** The distribution is strongly right-skewed with a substantial high-revenue tail.
- **Interpretation:** A minority of accounts likely represent disproportionately large revenue values. Median is a more representative central tendency measure for most accounts. This skew warrants careful treatment in any revenue forecasting model.

**`active_users`**
- Mean: **23.5**, Median: **11.0** — mean/median gap of **113%**
- Outlier rate: **9.27%**
- **Observation:** Heavily right-skewed. Most accounts have relatively few active users, but a notable upper tail exists.
- **Interpretation:** May reflect the presence of enterprise or large business accounts alongside a majority of smaller accounts.

**`days_since_last_login`**
- Mean: **13.6 days**, Median: **9.0 days** — gap of **52%**
- Outlier rate: **4.94%**
- **Observation:** Right-skewed, suggesting a smaller subset of accounts with very long login gaps pulling the mean upward.
- **Interpretation:** The modal user base is reasonably active (median 9 days), but a tail of dormant or at-risk accounts inflates the average.

**`cohort_age_months`**
- Mean: **8.9 months**, Median: **7.0** — gap of **27%**
- Outlier rate: **1.28%**
- **Observation:** Mild right skew; the cohort base is younger on average, with a smaller set of older accounts.

**`support_tickets`**
- Mean: **1.29**, Median: **1.0** — gap of **29%**
- Outlier rate: **0.52%**
- **Observation:** Low-magnitude skew; most accounts generate 1 or fewer tickets per month.

---

#### 🟡 Well-Behaved Distributions (Low Skew)

| Variable | Mean | Median | Notes |
|---|---|---|---|
| `feature_adoption_rate` | 67.7% | 68.1% | Near-symmetric; max cap flag (see below) |
| `usage_frequency` | 17.4 | 17.4 | Very tightly distributed |
| `onboarding_completion` | 75.4% | 75.4% | Near-symmetric; max cap flag (see below) |
| `product_health_score` | 0.62 | 0.62 | Symmetric, tight IQR (0.18) |
| `rolling_health_3m` | 0.61 | 0.61 | Mirrors product_health_score closely |
| `rolling_usage_3m` | 17.1 | 17.2 | Consistent with usage_frequency |

---

#### 🟡 Zero-Median / Sparse Variables

**`expansion_revenue`**
- Mean: **$23.09**, Median: **$0**, IQR: **$0**, Outlier rate: **11.01%**
- **Observation:** The overwhelming majority of account-months show zero expansion revenue. Positive values are confined to a distinct minority.

**`revenue_at_risk`**
- Mean: **$24.63**, Median: **$0**, Outlier rate: **16.85%**
- **Observation:** Similarly zero-inflated. Risk is concentrated in a subset of accounts.

**`revenue_trend`** and **`engagement_trend`** and **`usage_trend`**
- All have median of **$0.0** with small means near zero and relatively high outlier rates (16.1%, 1.6%, 1.3% respectively).
- **Observation:** These trend variables are near-flat for the majority of accounts, with deviations present in a minority subset.

**`renewal_probability`**
- Mean: **98.3%**, Median: **100%**, IQR: **2.36%**, Outlier rate: **9.91%**
- **Observation:** Highly right-concentrated — most accounts are flagged at 100% renewal probability. A 9.91% outlier tail exists below this ceiling.
- ⚠️ **Round-number cap detected:** 13,383 records (59.8% of the dataset) carry exactly 100.0. This warrants verification — it may reflect a model output cap, a default fill value, or genuinely high confidence scores.

---

#### ⚠️ Potential Cap Values (Round-Number Maximum Check)

| Variable | Max Value | Count at Max | % of Total |
|---|---|---|---|
| `feature_adoption_rate` | 100.0 | 237 | 1.1% |
| `onboarding_completion` | 100.0 | 887 | 4.0% |
| `renewal_probability` | 100.0 | 13,383 | **59.8%** |

The `renewal_probability` concentration at 100.0 is particularly notable and should be validated. The other two are plausible as genuine completion values but warrant confirmation.

---

### Binary Variables

| Variable | Positive Count | Positive Rate |
|---|---|---|
| `churn_flag` | 875 | **3.91%** |
| `downgrade_flag` | 831 | **3.71%** |

- **Observation:** Both churn and downgrade events are relatively rare in this dataset (~4% each), consistent with a reasonably healthy SaaS portfolio at a point in time.
- These are treated as proportions, not continuous distributions.

---

### Categorical Variables — Key Highlights

**Plan Type Distribution**
- Starter (35.8%) and Growth (35.0%) dominate; Business (19.7%) and Enterprise (9.4%) are smaller segments.
- The customer base is predominantly SMB-oriented.

**Company Size**
- Small (52.6%), Mid-Market (34.8%), Enterprise (12.7%)
- Consistent with the plan-type skew toward smaller accounts.

**Health and Usage Bands**
- `health_band`: 57.1% medium_health, 40.7% high_health, only **2.1% low_health**
- `usage_band`: 52.9% medium_usage, 45.0% high_usage, only **2.2% low_usage**
- **Observation:** The population is broadly healthy and engaged. Low-health/low-usage accounts are a small but potentially important minority.

**Login Recency Band**
- Active (0–7 days): **45.1%** | Warming (8–30 days): **43.8%** | Inactive (31–90 days): **10.8%** | Dormant (90+ days): **0.4%**
- **Observation:** Nearly 89% of accounts logged in within the past 30 days. Truly dormant accounts are rare (<1%).

**MRR Band**
- Low MRR: 41.2% | Mid MRR: 30.4% | High MRR: 19.4% | Enterprise MRR: 9.0%
- Aligns with the company size and plan-type distributions.

**Acquisition Channel**
- Organic (34.2%) is the leading channel, followed by Paid Search (23.8%), Sales Outbound (15.4%), Partner (14.6%), and Referral (12.0%).

**Region**
- North America (39.1%) > Europe (29.3%) > APAC (15.1%) > UK (11.2%) > Other (5.3%)

**Industry** *(291 missing values — 1.3% of records)*
- Software (30.0%), Finance (16.3%), Other (16.2%), Retail (14.9%), Healthcare (13.3%), Education (9.3%)

**Snapshot Coverage**
- 36 monthly snapshots represented. Distribution is relatively even across months (each ~4%), with slight growth toward late 2024 (Dec 2024 mode at 4.3%).

---

## 3. Interpretation

The dataset describes a SaaS account base that is, in aggregate, **predominantly healthy and active**. The majority of accounts fall in medium-to-high health and usage bands, with strong login recency and renewal probabilities concentrated near 100%. Churn and downgrade rates are low (~4% each).

However, **revenue is significantly concentrated in a small number of high-value accounts** — the MRR distribution is severely right-skewed with a 372% mean/median gap. This means aggregate revenue metrics will be driven by a minority of enterprise or high-value accounts, and any revenue analysis should segment by MRR band to avoid misleading averages.

**Expansion revenue and revenue at risk are largely zero-state variables**, with positive values occurring only in a minority of account-months. Analysis of these variables should focus on the non-zero subset rather than portfolio-wide averages.

The near-universal 100% renewal probability scores, combined with very low churn and downgrade rates, may suggest that the renewal model outputs skew optimistic — or that the dataset snapshot captures a generally healthy period.

---

## 4. Assumptions

- Each row represents one account-month observation (panel/longitudinal structure).
- The cleaned dataset has already had invalid values addressed; no further imputation is assumed here.
- Missing values in `industry`, `feature_adoption_rate`, `support_tickets`, and `usage_band` are assumed to be missing at random unless further analysis suggests systematic gaps.
- Binary flags are treated as event indicators, not continuous scores.

---

## 5. Limitations

- **Missing data** is present in four fields: `industry` (1.3%), `feature_adoption_rate` (2.1%), `usage_band` (2.1%), `support_tickets` (1.2%). These are modest but could introduce bias if missingness is systematic (e.g., concentrated in specific industries or plan types).
- **Causal inference is not possible** from descriptive statistics alone. No associations between variables are established here.
- The **renewal_probability cap at 100.0** (59.8% of records) raises data quality questions that could affect any churn prediction or health scoring model using this field.
- The **snapshot coverage is not perfectly even** across months; earlier cohort months have fewer records, which could affect longitudinal comparisons without cohort-adjustment.
- The **zero-inflated nature** of expansion_revenue, revenue_at_risk, and revenue_trend means standard distributional summaries are not informative for those variables without separating zero and non-zero populations.

---

## 6. Validation Notes

All technical pipeline columns (`*_invalid_flag`, `*_clean`, `*_missing_flag`) were excluded from primary analysis. Their outputs confirm:

- **Zero invalid records** were found across all validated numeric fields (cohort_age_months, active_users, feature_adoption_rate, usage_frequency, support_tickets, days_since_last_login, onboarding_completion, product_health_score, rolling_health_3m, rolling_usage_3m, monthly_recurring_revenue, expansion_revenue, renewal_probability, revenue_at_risk). All invalid flags are uniformly `False` (100%).
- **`downgrade_flag_clean` and `churn_flag_clean`** are consistent with their source columns — no cleaning discrepancies detected.
- **Missing flags** for `feature_adoption_rate` and `usage_band` each cover 466 records (2.08%), `support_tickets` covers 262 records (1.17%), and `industry` covers 291 records (1.30%). These are aligned with the raw missing counts reported in the dataset overview, confirming internal consistency.
- The cleaning pipeline appears to have been applied correctly with no residual invalid values.

---

## 7. Recommended Follow-up

| Priority | Action |
|---|---|
| 🔴 High | **Validate `renewal_probability` = 100.0** for 59.8% of records — confirm whether this is a genuine model output, a default, or a capping artifact. This materially affects any churn risk analysis. |
| 🔴 High | **Segment MRR analysis by MRR band or company size** — portfolio-level MRR averages are heavily distorted by the right-skewed tail. |
| 🟡 Medium | **Investigate missingness patterns** in `industry`, `feature_adoption_rate`, and `usage_band` — check whether missing values cluster within specific plan types, regions, or cohorts. |
| 🟡 Medium | **Analyze expansion revenue and revenue at risk as binary + conditional distributions** — separate zero vs. non-zero populations before computing any summaries or models. |
| 🟡 Medium | **Examine the active_users outlier tail** — given the 9.27% outlier rate and 113% mean/median gap, confirm whether high-user accounts are enterprise accounts or data anomalies. |
| 🟢 Lower | **Validate `feature_adoption_rate` and `onboarding_completion` at max=100** — confirm these represent genuine 100% completion rather than capped values. |
| 🟢 Lower | **Cohort-adjusted analysis** — since snapshot rows increase over time (slightly), trend analysis should control for cohort composition changes across the 36-month window. |

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
