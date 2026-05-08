"""
Segmentation analysis for P07.

Purpose:
- compare SaaS operational and revenue outcomes across strategic segments
- summarize retention, churn, health, usage, and revenue-at-risk by segment
- identify segments that may require executive attention
- support forecasting and scenario interpretation

Important:
Segment differences are observational. They should not be interpreted as causal effects.
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
    "projects/p07_saas_strategic_forecasting/outputs/segmentation"
)


SEGMENT_COLUMNS = [
    "health_band",
    "usage_band",
    "mrr_band",
    "login_recency_band",
    "plan_type",
    "company_size",
    "industry",
    "region",
    "acquisition_channel",
]


def load_data() -> pd.DataFrame:
    path = DATA_PATH if DATA_PATH.exists() else RAW_FALLBACK_PATH

    df = pd.read_csv(path)

    df["snapshot_month"] = pd.to_datetime(df["snapshot_month"])
    df["signup_month"] = pd.to_datetime(df["signup_month"])
    df["cohort_month"] = pd.to_datetime(df["cohort_month"])

    return df.sort_values(["account_id", "snapshot_month"]).reset_index(drop=True)


def save_table(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def summarize_by_segment(df: pd.DataFrame, segment_col: str) -> pd.DataFrame:
    grouped = df.groupby(segment_col, dropna=False)

    summary = grouped.agg(
        account_month_count=("account_id", "count"),
        unique_accounts=("account_id", "nunique"),
        churn_rate_percent=("churn_flag", lambda x: round(x.mean() * 100, 2)),
        downgrade_rate_percent=("downgrade_flag", lambda x: round(x.mean() * 100, 2)),
        median_product_health_score=("product_health_score", "median"),
        mean_product_health_score=("product_health_score", "mean"),
        median_rolling_health_3m=("rolling_health_3m", "median"),
        median_renewal_probability=("renewal_probability", "median"),
        mean_renewal_probability=("renewal_probability", "mean"),
        median_monthly_recurring_revenue=("monthly_recurring_revenue", "median"),
        mean_monthly_recurring_revenue=("monthly_recurring_revenue", "mean"),
        total_monthly_recurring_revenue=("monthly_recurring_revenue", "sum"),
        median_expansion_revenue=("expansion_revenue", "median"),
        total_expansion_revenue=("expansion_revenue", "sum"),
        median_revenue_at_risk=("revenue_at_risk", "median"),
        total_revenue_at_risk=("revenue_at_risk", "sum"),
        median_feature_adoption_rate=("feature_adoption_rate", "median"),
        mean_feature_adoption_rate=("feature_adoption_rate", "mean"),
        median_usage_frequency=("usage_frequency", "median"),
        mean_usage_frequency=("usage_frequency", "mean"),
        median_days_since_last_login=("days_since_last_login", "median"),
        mean_days_since_last_login=("days_since_last_login", "mean"),
        median_support_tickets=("support_tickets", "median"),
        mean_support_tickets=("support_tickets", "mean"),
        median_onboarding_completion=("onboarding_completion", "median"),
        mean_onboarding_completion=("onboarding_completion", "mean"),
    ).reset_index()

    summary["revenue_at_risk_rate"] = (
        summary["total_revenue_at_risk"] / summary["total_monthly_recurring_revenue"]
    ).replace([float("inf"), float("-inf")], pd.NA).fillna(0) * 100

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(2)

    return summary.sort_values("total_revenue_at_risk", ascending=False)


def summarize_cross_segment(
    df: pd.DataFrame,
    segment_cols: list[str],
) -> pd.DataFrame:
    grouped = df.groupby(segment_cols, dropna=False)

    summary = grouped.agg(
        account_month_count=("account_id", "count"),
        unique_accounts=("account_id", "nunique"),
        churn_rate_percent=("churn_flag", lambda x: round(x.mean() * 100, 2)),
        downgrade_rate_percent=("downgrade_flag", lambda x: round(x.mean() * 100, 2)),
        median_product_health_score=("product_health_score", "median"),
        median_renewal_probability=("renewal_probability", "median"),
        median_monthly_recurring_revenue=("monthly_recurring_revenue", "median"),
        total_monthly_recurring_revenue=("monthly_recurring_revenue", "sum"),
        total_revenue_at_risk=("revenue_at_risk", "sum"),
        median_feature_adoption_rate=("feature_adoption_rate", "median"),
        median_usage_frequency=("usage_frequency", "median"),
        median_days_since_last_login=("days_since_last_login", "median"),
        median_support_tickets=("support_tickets", "median"),
        median_onboarding_completion=("onboarding_completion", "median"),
    ).reset_index()

    summary["revenue_at_risk_rate"] = (
        summary["total_revenue_at_risk"] / summary["total_monthly_recurring_revenue"]
    ).replace([float("inf"), float("-inf")], pd.NA).fillna(0) * 100

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(2)

    return summary.sort_values("total_revenue_at_risk", ascending=False)


def summarize_latest_segment_position(df: pd.DataFrame) -> pd.DataFrame:
    latest_month = df["snapshot_month"].max()
    latest = df[df["snapshot_month"] == latest_month]

    summary = (
        latest.groupby(["health_band", "usage_band"], dropna=False)
        .agg(
            active_accounts=("account_id", "nunique"),
            total_mrr=("monthly_recurring_revenue", "sum"),
            total_revenue_at_risk=("revenue_at_risk", "sum"),
            avg_renewal_probability=("renewal_probability", "mean"),
            avg_product_health_score=("product_health_score", "mean"),
            avg_feature_adoption_rate=("feature_adoption_rate", "mean"),
            avg_usage_frequency=("usage_frequency", "mean"),
            avg_days_since_last_login=("days_since_last_login", "mean"),
            avg_support_tickets=("support_tickets", "mean"),
        )
        .reset_index()
    )

    summary["snapshot_month"] = latest_month

    summary["revenue_at_risk_rate"] = (
        summary["total_revenue_at_risk"] / summary["total_mrr"]
    ).replace([float("inf"), float("-inf")], pd.NA).fillna(0) * 100

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(2)

    return summary.sort_values("total_revenue_at_risk", ascending=False)


def summarize_segment_trajectory(
    df: pd.DataFrame,
    segment_col: str,
) -> pd.DataFrame:
    summary = (
        df.groupby(["snapshot_month", segment_col], dropna=False)
        .agg(
            active_accounts=("account_id", "nunique"),
            churned_accounts=("churn_flag", "sum"),
            total_mrr=("monthly_recurring_revenue", "sum"),
            total_revenue_at_risk=("revenue_at_risk", "sum"),
            avg_product_health_score=("product_health_score", "mean"),
            avg_feature_adoption_rate=("feature_adoption_rate", "mean"),
            avg_usage_frequency=("usage_frequency", "mean"),
            avg_days_since_last_login=("days_since_last_login", "mean"),
            avg_support_tickets=("support_tickets", "mean"),
            avg_renewal_probability=("renewal_probability", "mean"),
        )
        .reset_index()
        .sort_values(["snapshot_month", segment_col])
    )

    summary["monthly_churn_rate"] = (
        summary["churned_accounts"] / summary["active_accounts"]
    ).round(4)

    summary["revenue_at_risk_rate"] = (
        summary["total_revenue_at_risk"] / summary["total_mrr"]
    ).replace([float("inf"), float("-inf")], pd.NA).fillna(0).round(4)

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(3)

    return summary


def build_executive_segment_risk_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a compact table that highlights segment-level risk concentration.

    This is useful for executive reporting because it combines:
    - account concentration
    - MRR exposure
    - revenue-at-risk
    - operational health
    """

    grouped = df.groupby(["health_band", "mrr_band"], dropna=False)

    summary = grouped.agg(
        account_month_count=("account_id", "count"),
        unique_accounts=("account_id", "nunique"),
        total_mrr=("monthly_recurring_revenue", "sum"),
        total_revenue_at_risk=("revenue_at_risk", "sum"),
        avg_churn_rate=("churn_flag", "mean"),
        avg_renewal_probability=("renewal_probability", "mean"),
        avg_product_health_score=("product_health_score", "mean"),
        avg_days_since_last_login=("days_since_last_login", "mean"),
        avg_support_tickets=("support_tickets", "mean"),
    ).reset_index()

    summary["revenue_at_risk_rate"] = (
        summary["total_revenue_at_risk"] / summary["total_mrr"]
    ).replace([float("inf"), float("-inf")], pd.NA).fillna(0)

    summary["executive_attention_score"] = (
        summary["revenue_at_risk_rate"] * 0.45
        + summary["avg_churn_rate"] * 0.30
        + (1 - summary["avg_product_health_score"]) * 0.25
    )

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(3)

    return summary.sort_values(
        ["executive_attention_score", "total_revenue_at_risk"],
        ascending=[False, False],
    )


def main() -> None:
    df = load_data()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for segment_col in SEGMENT_COLUMNS:
        if segment_col not in df.columns:
            continue

        summary = summarize_by_segment(df, segment_col)

        save_table(
            summary,
            OUTPUT_DIR / f"{segment_col}_comparison.csv",
        )

        trajectory = summarize_segment_trajectory(df, segment_col)

        save_table(
            trajectory,
            OUTPUT_DIR / f"{segment_col}_trajectory.csv",
        )

        print(f"Saved {segment_col} comparison and trajectory")

    health_by_usage = summarize_cross_segment(
        df,
        ["health_band", "usage_band"],
    )

    save_table(
        health_by_usage,
        OUTPUT_DIR / "health_by_usage_comparison.csv",
    )

    health_by_mrr = summarize_cross_segment(
        df,
        ["health_band", "mrr_band"],
    )

    save_table(
        health_by_mrr,
        OUTPUT_DIR / "health_by_mrr_comparison.csv",
    )

    plan_by_company_size = summarize_cross_segment(
        df,
        ["plan_type", "company_size"],
    )

    save_table(
        plan_by_company_size,
        OUTPUT_DIR / "plan_by_company_size_comparison.csv",
    )

    latest_segment_position = summarize_latest_segment_position(df)

    save_table(
        latest_segment_position,
        OUTPUT_DIR / "latest_health_by_usage_position.csv",
    )

    executive_risk_table = build_executive_segment_risk_table(df)

    save_table(
        executive_risk_table,
        OUTPUT_DIR / "executive_segment_risk_table.csv",
    )

    print("Saved health by usage comparison")
    print("Saved health by MRR comparison")
    print("Saved plan by company-size comparison")
    print("Saved latest segment position")
    print("Saved executive segment risk table")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()