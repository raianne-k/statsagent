"""
Relationship analysis for P07.

Purpose:
- evaluate relationships among SaaS operational, engagement, health, and revenue metrics
- compare churned vs retained account-months
- analyze leading-indicator relationships with next-month outcomes
- support forecasting and scenario-modeling assumptions

Important:
Relationships are observational and should not be interpreted as causal effects.
"""

from pathlib import Path

import pandas as pd


DATA_PATH = Path(
    "projects/p07_saas_strategic_forecasting/data/cleaned/saas_account_monthly_cleaned.csv"
)

RAW_FALLBACK_PATH = Path(
    "projects/p07_saas_strategic_forecasting/data/raw/saas_account_monthly_forecasting.csv"
)

OUTPUT_DIR = Path(
    "projects/p07_saas_strategic_forecasting/outputs/relationships"
)


CORRELATION_COLUMNS = [
    "cohort_age_months",
    "active_users",
    "feature_adoption_rate",
    "usage_frequency",
    "support_tickets",
    "days_since_last_login",
    "onboarding_completion",
    "product_health_score",
    "rolling_health_3m",
    "rolling_usage_3m",
    "engagement_trend",
    "usage_trend",
    "monthly_recurring_revenue",
    "expansion_revenue",
    "revenue_trend",
    "renewal_probability",
    "revenue_at_risk",
]


TARGET_COLUMNS = [
    "product_health_score",
    "renewal_probability",
    "churn_flag",
    "monthly_recurring_revenue",
    "revenue_at_risk",
]


LEADING_INDICATOR_COLUMNS = [
    "onboarding_completion",
    "feature_adoption_rate",
    "usage_frequency",
    "active_users",
    "days_since_last_login",
    "support_tickets",
    "product_health_score",
    "rolling_health_3m",
    "rolling_usage_3m",
    "engagement_trend",
    "usage_trend",
]


NEXT_MONTH_TARGETS = [
    "next_month_churn_flag",
    "next_month_renewal_probability",
    "next_month_mrr",
    "next_month_revenue_at_risk",
    "next_month_product_health_score",
]


def save_table(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def load_data() -> pd.DataFrame:
    path = DATA_PATH if DATA_PATH.exists() else RAW_FALLBACK_PATH
    df = pd.read_csv(path)

    df["snapshot_month"] = pd.to_datetime(df["snapshot_month"])
    df["signup_month"] = pd.to_datetime(df["signup_month"])
    df["cohort_month"] = pd.to_datetime(df["cohort_month"])

    return df.sort_values(["account_id", "snapshot_month"]).reset_index(drop=True)


def compute_correlations(df: pd.DataFrame, method: str) -> pd.DataFrame:
    available_columns = [
        col for col in CORRELATION_COLUMNS
        if col in df.columns
    ]

    corr = df[available_columns].corr(method=method)

    return corr.reset_index().rename(columns={"index": "variable"})


def compute_target_relationships(df: pd.DataFrame, method: str) -> pd.DataFrame:
    available_columns = [
        col for col in CORRELATION_COLUMNS + TARGET_COLUMNS
        if col in df.columns
    ]

    rows = []

    for target in TARGET_COLUMNS:
        if target not in df.columns:
            continue

        for col in available_columns:
            if col == target:
                continue

            valid = df[[col, target]].dropna()

            if len(valid) < 50:
                continue

            corr_value = valid[col].corr(valid[target], method=method)

            rows.append({
                "target": target,
                "variable": col,
                "method": method,
                "correlation": round(corr_value, 3),
                "abs_correlation": round(abs(corr_value), 3),
                "n": len(valid),
                "interpretation_warning": (
                    "Same-month association only; not causal evidence."
                ),
            })

    result = pd.DataFrame(rows)

    if result.empty:
        return result

    return result.sort_values(
        ["target", "abs_correlation"],
        ascending=[True, False],
    )


def add_next_month_targets(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(["account_id", "snapshot_month"]).copy()

    df["next_month_churn_flag"] = (
        df.groupby("account_id")["churn_flag"].shift(-1)
    )

    df["next_month_renewal_probability"] = (
        df.groupby("account_id")["renewal_probability"].shift(-1)
    )

    df["next_month_mrr"] = (
        df.groupby("account_id")["monthly_recurring_revenue"].shift(-1)
    )

    df["next_month_revenue_at_risk"] = (
        df.groupby("account_id")["revenue_at_risk"].shift(-1)
    )

    df["next_month_product_health_score"] = (
        df.groupby("account_id")["product_health_score"].shift(-1)
    )

    return df


def compute_leading_indicator_relationships(df: pd.DataFrame, method: str) -> pd.DataFrame:
    df = add_next_month_targets(df)

    rows = []

    for target in NEXT_MONTH_TARGETS:
        if target not in df.columns:
            continue

        for indicator in LEADING_INDICATOR_COLUMNS:
            if indicator not in df.columns:
                continue

            valid = df[[indicator, target]].dropna()

            if len(valid) < 50:
                continue

            corr_value = valid[indicator].corr(valid[target], method=method)

            rows.append({
                "leading_indicator": indicator,
                "future_target": target,
                "method": method,
                "correlation": round(corr_value, 3),
                "abs_correlation": round(abs(corr_value), 3),
                "n": len(valid),
                "time_relationship": "current_month_indicator_to_next_month_target",
                "interpretation_warning": (
                    "Temporal ordering improves forecasting relevance but does not prove causality."
                ),
            })

    result = pd.DataFrame(rows)

    if result.empty:
        return result

    return result.sort_values(
        ["future_target", "abs_correlation"],
        ascending=[True, False],
    )


def compute_churn_group_comparison(df: pd.DataFrame) -> pd.DataFrame:
    grouped = df.groupby("churn_flag", dropna=False)

    summary = grouped.agg(
        account_month_count=("account_id", "count"),
        unique_accounts=("account_id", "nunique"),
        median_product_health_score=("product_health_score", "median"),
        median_rolling_health_3m=("rolling_health_3m", "median"),
        median_renewal_probability=("renewal_probability", "median"),
        median_feature_adoption_rate=("feature_adoption_rate", "median"),
        median_usage_frequency=("usage_frequency", "median"),
        median_days_since_last_login=("days_since_last_login", "median"),
        median_support_tickets=("support_tickets", "median"),
        median_monthly_recurring_revenue=("monthly_recurring_revenue", "median"),
        median_expansion_revenue=("expansion_revenue", "median"),
        median_revenue_at_risk=("revenue_at_risk", "median"),
        downgrade_rate=("downgrade_flag", "mean"),
    ).reset_index()

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(3)

    return summary


def compute_health_band_comparison(df: pd.DataFrame) -> pd.DataFrame:
    if "health_band" not in df.columns:
        return pd.DataFrame()

    summary = (
        df.groupby("health_band", dropna=False)
        .agg(
            account_month_count=("account_id", "count"),
            unique_accounts=("account_id", "nunique"),
            avg_churn_rate=("churn_flag", "mean"),
            avg_renewal_probability=("renewal_probability", "mean"),
            avg_monthly_recurring_revenue=("monthly_recurring_revenue", "mean"),
            avg_revenue_at_risk=("revenue_at_risk", "mean"),
            median_feature_adoption_rate=("feature_adoption_rate", "median"),
            median_usage_frequency=("usage_frequency", "median"),
            median_days_since_last_login=("days_since_last_login", "median"),
            median_support_tickets=("support_tickets", "median"),
            downgrade_rate=("downgrade_flag", "mean"),
        )
        .reset_index()
    )

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(3)

    return summary


def compute_indicator_direction_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize whether leading indicators move in the expected operational direction
    across churn outcomes.

    This is not a statistical test. It is a governance-friendly diagnostic table.
    """

    retained = df[df["churn_flag"] == 0]
    churned = df[df["churn_flag"] == 1]

    rows = []

    comparisons = [
        {
            "indicator": "product_health_score",
            "expected_risk_direction": "lower values indicate higher risk",
        },
        {
            "indicator": "rolling_health_3m",
            "expected_risk_direction": "lower values indicate higher risk",
        },
        {
            "indicator": "feature_adoption_rate",
            "expected_risk_direction": "lower values indicate higher risk",
        },
        {
            "indicator": "usage_frequency",
            "expected_risk_direction": "lower values indicate higher risk",
        },
        {
            "indicator": "days_since_last_login",
            "expected_risk_direction": "higher values indicate higher risk",
        },
        {
            "indicator": "support_tickets",
            "expected_risk_direction": "higher values may indicate higher risk",
        },
        {
            "indicator": "revenue_at_risk",
            "expected_risk_direction": "higher values indicate higher risk",
        },
    ]

    for item in comparisons:
        indicator = item["indicator"]

        if indicator not in df.columns:
            continue

        retained_median = retained[indicator].median()
        churned_median = churned[indicator].median()

        rows.append({
            "indicator": indicator,
            "retained_median": round(retained_median, 3),
            "churned_median": round(churned_median, 3),
            "difference_churned_minus_retained": round(churned_median - retained_median, 3),
            "expected_risk_direction": item["expected_risk_direction"],
            "interpretation_warning": (
                "Directional diagnostic only; not causal proof."
            ),
        })

    return pd.DataFrame(rows)


def main() -> None:
    df = load_data()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pearson_corr = compute_correlations(df, method="pearson")
    spearman_corr = compute_correlations(df, method="spearman")

    save_table(
        pearson_corr,
        OUTPUT_DIR / "pearson_correlation_matrix.csv",
    )

    save_table(
        spearman_corr,
        OUTPUT_DIR / "spearman_correlation_matrix.csv",
    )

    pearson_targets = compute_target_relationships(df, method="pearson")
    spearman_targets = compute_target_relationships(df, method="spearman")

    save_table(
        pearson_targets,
        OUTPUT_DIR / "pearson_target_relationships.csv",
    )

    save_table(
        spearman_targets,
        OUTPUT_DIR / "spearman_target_relationships.csv",
    )

    leading_pearson = compute_leading_indicator_relationships(
        df,
        method="pearson",
    )

    leading_spearman = compute_leading_indicator_relationships(
        df,
        method="spearman",
    )

    save_table(
        leading_pearson,
        OUTPUT_DIR / "pearson_leading_indicator_relationships.csv",
    )

    save_table(
        leading_spearman,
        OUTPUT_DIR / "spearman_leading_indicator_relationships.csv",
    )

    churn_comparison = compute_churn_group_comparison(df)
    save_table(
        churn_comparison,
        OUTPUT_DIR / "churn_group_comparison.csv",
    )

    health_band_comparison = compute_health_band_comparison(df)
    save_table(
        health_band_comparison,
        OUTPUT_DIR / "health_band_comparison.csv",
    )

    indicator_direction_summary = compute_indicator_direction_summary(df)
    save_table(
        indicator_direction_summary,
        OUTPUT_DIR / "indicator_direction_summary.csv",
    )

    print("Relationship analysis complete.")
    print("Saved Pearson and Spearman correlation matrices.")
    print("Saved target relationship rankings.")
    print("Saved leading-indicator relationship rankings.")
    print("Saved churn and health-band comparisons.")
    print("Saved indicator direction summary.")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()