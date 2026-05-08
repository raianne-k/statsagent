from pathlib import Path

import pandas as pd


DATA_PATH = Path(
    "projects/p05_saas_churn_prediction/data/cleaned/saas_churn_prediction_cleaned.csv"
)

OUTPUT_DIR = Path(
    "projects/p05_saas_churn_prediction/outputs/segmentation"
)


SEGMENT_COLUMNS = [
    "health_band",
    "usage_band",
    "contract_type",
    "plan_tier",
    "login_recency_band",
    "revenue_band",
]


def summarize_by_segment(df: pd.DataFrame, segment_col: str) -> pd.DataFrame:
    grouped = df.groupby(segment_col, dropna=False)

    summary = grouped.agg(
        account_count=("account_id", "count"),
        churn_rate_percent=("churned", lambda x: round(x.mean() * 100, 2)),

        median_account_health_score=("account_health_score", "median"),
        median_renewal_probability_score=("renewal_probability_score", "median"),
        median_feature_adoption_rate=("feature_adoption_rate", "median"),
        median_seat_utilization_percent=("seat_utilization_percent", "median"),
        median_days_since_last_login=("days_since_last_login", "median"),
        median_support_ticket_count_90d=("support_ticket_count_90d", "median"),
        median_unresolved_ticket_count=("unresolved_ticket_count", "median"),
        median_monthly_recurring_revenue=("monthly_recurring_revenue", "median"),

        onboarding_completion_rate_percent=(
            "onboarding_completed",
            lambda x: round(x.mean() * 100, 2),
        ),
        support_escalation_rate_percent=(
            "support_escalation_flag",
            lambda x: round(x.mean() * 100, 2),
        ),
        renewal_meeting_rate_percent=(
            "renewal_meeting_completed",
            lambda x: round(x.mean() * 100, 2),
        ),
    ).reset_index()

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(2)

    return summary


def summarize_cross_segment(
    df: pd.DataFrame,
    segment_cols: list[str],
) -> pd.DataFrame:
    grouped = df.groupby(segment_cols, dropna=False)

    summary = grouped.agg(
        account_count=("account_id", "count"),
        churn_rate_percent=("churned", lambda x: round(x.mean() * 100, 2)),
        median_account_health_score=("account_health_score", "median"),
        median_feature_adoption_rate=("feature_adoption_rate", "median"),
        median_seat_utilization_percent=("seat_utilization_percent", "median"),
        median_days_since_last_login=("days_since_last_login", "median"),
        median_renewal_probability_score=("renewal_probability_score", "median"),
    ).reset_index()

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(2)

    return summary


def save_table(df: pd.DataFrame, output_path: Path) -> None:
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

    health_by_contract = summarize_cross_segment(
        df,
        ["health_band", "contract_type"],
    )

    save_table(
        health_by_contract,
        OUTPUT_DIR / "health_by_contract_comparison.csv",
    )

    print("Saved health by contract comparison")

    usage_by_plan = summarize_cross_segment(
        df,
        ["usage_band", "plan_tier"],
    )

    save_table(
        usage_by_plan,
        OUTPUT_DIR / "usage_by_plan_comparison.csv",
    )

    print("Saved usage by plan comparison")

    health_by_login_recency = summarize_cross_segment(
        df,
        ["health_band", "login_recency_band"],
    )

    save_table(
        health_by_login_recency,
        OUTPUT_DIR / "health_by_login_recency_comparison.csv",
    )

    print("Saved health by login recency comparison")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()