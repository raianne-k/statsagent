from pathlib import Path

import pandas as pd


DATA_PATH = Path(
    "projects/p03_saas_relationships/data/cleaned/saas_account_cleaned.csv"
)

OUTPUT_DIR = Path(
    "projects/p03_saas_relationships/outputs/segmentation"
)


SEGMENT_COLUMNS = [
    "health_band",
    "usage_band",
    "revenue_band",
    "login_recency_band",
    "subscription_plan",
    "contract_type",
]


def summarize_by_segment(df: pd.DataFrame, segment_col: str) -> pd.DataFrame:
    """Create segment-level comparison table for one SaaS grouping variable."""

    grouped = df.groupby(segment_col, dropna=False)

    summary = grouped.agg(
        account_count=("account_id", "count"),
        churn_rate_percent=("churn_flag", lambda x: round(x.mean() * 100, 2)),

        median_account_health_score=("account_health_score", "median"),
        mean_account_health_score=("account_health_score", "mean"),

        median_renewal_probability=("renewal_probability", "median"),
        mean_renewal_probability=("renewal_probability", "mean"),

        median_monthly_recurring_revenue=("monthly_recurring_revenue", "median"),
        mean_monthly_recurring_revenue=("monthly_recurring_revenue", "mean"),

        median_expansion_revenue=("expansion_revenue", "median"),
        mean_expansion_revenue=("expansion_revenue", "mean"),

        median_feature_adoption_rate=("feature_adoption_rate", "median"),
        mean_feature_adoption_rate=("feature_adoption_rate", "mean"),

        median_onboarding_completion_percent=("onboarding_completion_percent", "median"),
        mean_onboarding_completion_percent=("onboarding_completion_percent", "mean"),

        median_seats_used_percent=("seats_used_percent", "median"),
        mean_seats_used_percent=("seats_used_percent", "mean"),

        median_days_since_last_login=("days_since_last_login", "median"),
        mean_days_since_last_login=("days_since_last_login", "mean"),

        median_support_tickets_last_90d=("support_tickets_last_90d", "median"),
        mean_support_tickets_last_90d=("support_tickets_last_90d", "mean"),

        median_nps_score=("nps_score", "median"),
        mean_nps_score=("nps_score", "mean"),
    ).reset_index()

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(2)

    return summary


def summarize_cross_segment(
    df: pd.DataFrame,
    segment_cols: list[str],
) -> pd.DataFrame:
    """Create comparison table across two SaaS segmentation dimensions."""

    grouped = df.groupby(segment_cols, dropna=False)

    summary = grouped.agg(
        account_count=("account_id", "count"),
        churn_rate_percent=("churn_flag", lambda x: round(x.mean() * 100, 2)),

        median_account_health_score=("account_health_score", "median"),
        median_renewal_probability=("renewal_probability", "median"),
        median_monthly_recurring_revenue=("monthly_recurring_revenue", "median"),
        median_feature_adoption_rate=("feature_adoption_rate", "median"),
        median_onboarding_completion_percent=("onboarding_completion_percent", "median"),
        median_days_since_last_login=("days_since_last_login", "median"),
        median_support_tickets_last_90d=("support_tickets_last_90d", "median"),
    ).reset_index()

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(2)

    return summary


def summarize_operational_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """Create operational KPI table across health and usage segments."""

    grouped = df.groupby(
        ["health_band", "usage_band"],
        dropna=False,
    )

    summary = grouped.agg(
        account_count=("account_id", "count"),
        churn_rate_percent=("churn_flag", lambda x: round(x.mean() * 100, 2)),
        median_renewal_probability=("renewal_probability", "median"),
        median_monthly_recurring_revenue=("monthly_recurring_revenue", "median"),
        median_expansion_revenue=("expansion_revenue", "median"),
        median_feature_adoption_rate=("feature_adoption_rate", "median"),
        median_onboarding_completion_percent=("onboarding_completion_percent", "median"),
        median_seats_used_percent=("seats_used_percent", "median"),
        median_days_since_last_login=("days_since_last_login", "median"),
        median_support_tickets_last_90d=("support_tickets_last_90d", "median"),
        median_nps_score=("nps_score", "median"),
    ).reset_index()

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(2)

    return summary


def save_table(df: pd.DataFrame, output_path: Path) -> None:
    """Save one comparison table."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def main():
    df = pd.read_csv(DATA_PATH)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for segment_col in SEGMENT_COLUMNS:
        summary = summarize_by_segment(df, segment_col)

        save_table(
            summary,
            OUTPUT_DIR / f"{segment_col}_comparison.csv",
        )

        print(f"Saved {segment_col} comparison")

    health_by_usage = summarize_cross_segment(
        df,
        ["health_band", "usage_band"],
    )

    save_table(
        health_by_usage,
        OUTPUT_DIR / "health_by_usage_comparison.csv",
    )

    print("Saved health by usage comparison")

    health_by_revenue = summarize_cross_segment(
        df,
        ["health_band", "revenue_band"],
    )

    save_table(
        health_by_revenue,
        OUTPUT_DIR / "health_by_revenue_comparison.csv",
    )

    print("Saved health by revenue comparison")

    operational_kpis = summarize_operational_kpis(df)

    save_table(
        operational_kpis,
        OUTPUT_DIR / "health_by_usage_operational_kpis.csv",
    )

    print("Saved health by usage operational KPIs")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()