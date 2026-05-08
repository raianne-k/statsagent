from pathlib import Path

import numpy as np
import pandas as pd


DATA_PATH = Path(
    "projects/p05_saas_churn_prediction/data/cleaned/saas_churn_prediction_cleaned.csv"
)

OUTPUT_DIR = Path(
    "projects/p05_saas_churn_prediction/outputs/relationships"
)


CONTINUOUS_COLUMNS = [
    "monthly_recurring_revenue",
    "tenure_months",
    "weekly_active_users",
    "feature_adoption_rate",
    "login_frequency_30d",
    "avg_session_duration_minutes",
    "support_ticket_count_90d",
    "unresolved_ticket_count",
    "nps_score",
    "account_health_score",
    "seat_utilization_percent",
    "days_since_last_login",
    "renewal_probability_score",
]


TARGET_COLUMN = "churned"


def save_table(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def build_correlation_table(df: pd.DataFrame) -> pd.DataFrame:
    correlations = []

    for column in CONTINUOUS_COLUMNS:
        temp_df = df[[column, TARGET_COLUMN]].dropna()

        correlation = temp_df[column].corr(temp_df[TARGET_COLUMN])

        correlations.append({
            "variable": column,
            "correlation_with_churn": round(correlation, 4),
            "absolute_correlation": round(abs(correlation), 4),
        })

    correlation_df = pd.DataFrame(correlations)

    correlation_df = correlation_df.sort_values(
        by="absolute_correlation",
        ascending=False,
    )

    return correlation_df


def build_binary_relationships(df: pd.DataFrame) -> pd.DataFrame:
    binary_columns = [
        "multi_product_adoption",
        "onboarding_completed",
        "support_escalation_flag",
        "renewal_meeting_completed",
        "discount_received",
    ]

    rows = []

    for column in binary_columns:
        grouped = df.groupby(column)["churned"].mean() * 100

        rows.append({
            "variable": column,
            "group_0_churn_rate_percent": round(grouped.get(0, np.nan), 2),
            "group_1_churn_rate_percent": round(grouped.get(1, np.nan), 2),
            "difference_percentage_points": round(
                grouped.get(1, np.nan) - grouped.get(0, np.nan),
                2,
            ),
        })

    return pd.DataFrame(rows)


def build_contract_churn_table(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby("contract_type")
        .agg(
            account_count=("account_id", "count"),
            churn_rate_percent=("churned", lambda x: round(x.mean() * 100, 2)),
            median_health_score=("account_health_score", "median"),
            median_feature_adoption=("feature_adoption_rate", "median"),
            median_days_since_login=("days_since_last_login", "median"),
        )
        .reset_index()
    )

    return grouped


def build_plan_tier_churn_table(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby("plan_tier")
        .agg(
            account_count=("account_id", "count"),
            churn_rate_percent=("churned", lambda x: round(x.mean() * 100, 2)),
            median_mrr=("monthly_recurring_revenue", "median"),
            median_health_score=("account_health_score", "median"),
            median_feature_adoption=("feature_adoption_rate", "median"),
        )
        .reset_index()
    )

    return grouped


def build_health_band_churn_table(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby("health_band")
        .agg(
            account_count=("account_id", "count"),
            churn_rate_percent=("churned", lambda x: round(x.mean() * 100, 2)),
            median_days_since_login=("days_since_last_login", "median"),
            median_nps=("nps_score", "median"),
            median_support_tickets=("support_ticket_count_90d", "median"),
        )
        .reset_index()
    )

    return grouped


def main():
    df = pd.read_csv(DATA_PATH)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    correlation_table = build_correlation_table(df)

    save_table(
        correlation_table,
        OUTPUT_DIR / "continuous_variable_correlations.csv",
    )

    print("Saved continuous variable correlations")

    binary_relationships = build_binary_relationships(df)

    save_table(
        binary_relationships,
        OUTPUT_DIR / "binary_variable_churn_relationships.csv",
    )

    print("Saved binary variable relationships")

    contract_churn = build_contract_churn_table(df)

    save_table(
        contract_churn,
        OUTPUT_DIR / "contract_type_churn_relationships.csv",
    )

    print("Saved contract type relationships")

    plan_tier_churn = build_plan_tier_churn_table(df)

    save_table(
        plan_tier_churn,
        OUTPUT_DIR / "plan_tier_churn_relationships.csv",
    )

    print("Saved plan tier relationships")

    health_band_churn = build_health_band_churn_table(df)

    save_table(
        health_band_churn,
        OUTPUT_DIR / "health_band_churn_relationships.csv",
    )

    print("Saved health band relationships")

    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()