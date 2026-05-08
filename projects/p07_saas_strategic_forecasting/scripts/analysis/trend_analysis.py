"""
Operational trend analysis for P07.

Purpose:
- summarize monthly SaaS operating trends
- identify leading-indicator movement
- create trend outputs for forecasting, scenarios, reporting, and dashboarding

Important:
This script tracks directional operational movement. It does not claim that
observed trends causally determine future outcomes.
"""

from pathlib import Path

import pandas as pd
import yaml


CONFIG_PATH = Path("projects/p07_saas_strategic_forecasting/configs/project_config.yaml")


def load_config(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def ensure_output_dirs(config: dict) -> None:
    output_paths = config["outputs"]["trends"]

    for path in output_paths.values():
        Path(path).parent.mkdir(parents=True, exist_ok=True)


def load_data(config: dict) -> pd.DataFrame:
    cleaned_path = Path(config["data"]["cleaned_path"])
    raw_path = Path(config["data"]["raw_path"])

    path = cleaned_path if cleaned_path.exists() else raw_path

    df = pd.read_csv(path)

    df["snapshot_month"] = pd.to_datetime(df["snapshot_month"])
    df["signup_month"] = pd.to_datetime(df["signup_month"])
    df["cohort_month"] = pd.to_datetime(df["cohort_month"])

    return df


def build_operational_trends(df: pd.DataFrame) -> pd.DataFrame:
    monthly = (
        df.groupby("snapshot_month")
        .agg(
            active_accounts=("account_id", "nunique"),
            churned_accounts=("churn_flag", "sum"),
            total_mrr=("monthly_recurring_revenue", "sum"),
            avg_mrr=("monthly_recurring_revenue", "mean"),
            expansion_revenue=("expansion_revenue", "sum"),
            revenue_at_risk=("revenue_at_risk", "sum"),
            avg_renewal_probability=("renewal_probability", "mean"),
            avg_product_health=("product_health_score", "mean"),
            avg_rolling_health_3m=("rolling_health_3m", "mean"),
            avg_usage_frequency=("usage_frequency", "mean"),
            avg_rolling_usage_3m=("rolling_usage_3m", "mean"),
            avg_feature_adoption=("feature_adoption_rate", "mean"),
            avg_days_since_last_login=("days_since_last_login", "mean"),
            avg_support_tickets=("support_tickets", "mean"),
            avg_onboarding_completion=("onboarding_completion", "mean"),
            downgrade_rate=("downgrade_flag", "mean"),
        )
        .reset_index()
        .sort_values("snapshot_month")
    )

    monthly["monthly_churn_rate"] = (
        monthly["churned_accounts"] / monthly["active_accounts"]
    ).round(4)

    monthly["mrr_growth_rate"] = (
        monthly["total_mrr"].pct_change()
    ).replace([float("inf"), float("-inf")], pd.NA).fillna(0).round(4)

    monthly["revenue_at_risk_rate"] = (
        monthly["revenue_at_risk"] / monthly["total_mrr"]
    ).replace([float("inf"), float("-inf")], pd.NA).fillna(0).round(4)

    monthly["health_trend_3m"] = (
        monthly["avg_product_health"].rolling(window=3, min_periods=1).mean()
    ).round(3)

    monthly["usage_trend_3m"] = (
        monthly["avg_usage_frequency"].rolling(window=3, min_periods=1).mean()
    ).round(2)

    monthly["adoption_trend_3m"] = (
        monthly["avg_feature_adoption"].rolling(window=3, min_periods=1).mean()
    ).round(2)

    monthly["inactivity_trend_3m"] = (
        monthly["avg_days_since_last_login"].rolling(window=3, min_periods=1).mean()
    ).round(2)

    monthly["support_trend_3m"] = (
        monthly["avg_support_tickets"].rolling(window=3, min_periods=1).mean()
    ).round(2)

    monthly["mrr_trend_3m"] = (
        monthly["total_mrr"].rolling(window=3, min_periods=1).mean()
    ).round(2)

    return monthly


def build_leading_indicators(df: pd.DataFrame) -> pd.DataFrame:
    indicator_summary = (
        df.groupby("snapshot_month")
        .agg(
            active_accounts=("account_id", "nunique"),
            low_health_accounts=("product_health_score", lambda s: (s < 0.35).sum()),
            declining_engagement_accounts=("engagement_trend", lambda s: (s < -0.05).sum()),
            low_adoption_accounts=("feature_adoption_rate", lambda s: (s < 35).sum()),
            inactive_accounts=("days_since_last_login", lambda s: (s > 45).sum()),
            high_support_accounts=("support_tickets", lambda s: (s >= 6).sum()),
            downgrade_accounts=("downgrade_flag", "sum"),
            churned_accounts=("churn_flag", "sum"),
            revenue_at_risk=("revenue_at_risk", "sum"),
            total_mrr=("monthly_recurring_revenue", "sum"),
        )
        .reset_index()
        .sort_values("snapshot_month")
    )

    denominator = indicator_summary["active_accounts"]

    indicator_summary["low_health_rate"] = (
        indicator_summary["low_health_accounts"] / denominator
    ).round(4)

    indicator_summary["declining_engagement_rate"] = (
        indicator_summary["declining_engagement_accounts"] / denominator
    ).round(4)

    indicator_summary["low_adoption_rate"] = (
        indicator_summary["low_adoption_accounts"] / denominator
    ).round(4)

    indicator_summary["inactive_account_rate"] = (
        indicator_summary["inactive_accounts"] / denominator
    ).round(4)

    indicator_summary["high_support_rate"] = (
        indicator_summary["high_support_accounts"] / denominator
    ).round(4)

    indicator_summary["downgrade_rate"] = (
        indicator_summary["downgrade_accounts"] / denominator
    ).round(4)

    indicator_summary["churn_rate"] = (
        indicator_summary["churned_accounts"] / denominator
    ).round(4)

    indicator_summary["revenue_at_risk_rate"] = (
        indicator_summary["revenue_at_risk"] / indicator_summary["total_mrr"]
    ).replace([float("inf"), float("-inf")], pd.NA).fillna(0).round(4)

    return indicator_summary


def main() -> None:
    config = load_config(CONFIG_PATH)
    ensure_output_dirs(config)

    df = load_data(config)

    operational_trends = build_operational_trends(df)
    leading_indicators = build_leading_indicators(df)

    operational_trends_path = Path(config["outputs"]["trends"]["operational_trends"])
    leading_indicators_path = Path(config["outputs"]["trends"]["leading_indicators"])

    operational_trends.to_csv(operational_trends_path, index=False)
    leading_indicators.to_csv(leading_indicators_path, index=False)

    print("Trend analysis complete.")
    print(f"Saved operational trends: {operational_trends_path}")
    print(f"Saved leading indicators: {leading_indicators_path}")
    print(f"Months analyzed: {operational_trends['snapshot_month'].nunique()}")


if __name__ == "__main__":
    main()