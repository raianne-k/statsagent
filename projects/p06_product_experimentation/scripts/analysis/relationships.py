from pathlib import Path

import numpy as np
import pandas as pd


DATA_PATH = Path(
    "projects/p06_product_experimentation/data/cleaned/saas_experimentation_cleaned.csv"
)

OUTPUT_DIR = Path(
    "projects/p06_product_experimentation/outputs/relationships"
)

GROUP_COLUMN = "experiment_group"

CONTINUOUS_COLUMNS = [
    "sessions_first_14d",
    "feature_adoption_count",
    "support_tickets_first_30d",
    "time_to_activation_days",
    "monthly_subscription_value",
    "exposure_days",
]

OUTCOME_COLUMNS = [
    "activation_flag",
    "retained_30d",
    "retained_60d",
    "churn_30d",
    "upgrade_flag",
    "negative_feedback_flag",
]


def save_table(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def build_overall_correlations(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for continuous_col in CONTINUOUS_COLUMNS:
        for outcome_col in OUTCOME_COLUMNS:
            temp = df[[continuous_col, outcome_col]].dropna()

            if len(temp) < 2 or temp[continuous_col].nunique() <= 1:
                correlation = np.nan
            else:
                correlation = temp[continuous_col].corr(temp[outcome_col])

            rows.append(
                {
                    "continuous_variable": continuous_col,
                    "outcome_variable": outcome_col,
                    "correlation": round(correlation, 4)
                    if pd.notna(correlation)
                    else np.nan,
                    "absolute_correlation": round(abs(correlation), 4)
                    if pd.notna(correlation)
                    else np.nan,
                    "n": len(temp),
                }
            )

    result = pd.DataFrame(rows)

    return result.sort_values(
        by="absolute_correlation",
        ascending=False,
        na_position="last",
    )


def build_group_correlations(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for group_value, group_df in df.groupby(GROUP_COLUMN):
        for continuous_col in CONTINUOUS_COLUMNS:
            for outcome_col in OUTCOME_COLUMNS:
                temp = group_df[[continuous_col, outcome_col]].dropna()

                if len(temp) < 2 or temp[continuous_col].nunique() <= 1:
                    correlation = np.nan
                else:
                    correlation = temp[continuous_col].corr(temp[outcome_col])

                rows.append(
                    {
                        "experiment_group": group_value,
                        "continuous_variable": continuous_col,
                        "outcome_variable": outcome_col,
                        "correlation": round(correlation, 4)
                        if pd.notna(correlation)
                        else np.nan,
                        "absolute_correlation": round(abs(correlation), 4)
                        if pd.notna(correlation)
                        else np.nan,
                        "n": len(temp),
                    }
                )

    result = pd.DataFrame(rows)

    return result.sort_values(
        by=["outcome_variable", "absolute_correlation"],
        ascending=[True, False],
        na_position="last",
    )


def build_binary_relationships(df: pd.DataFrame) -> pd.DataFrame:
    binary_context_columns = [
        "onboarding_completion_flag",
        "activation_flag",
        "experiment_eligibility_flag",
        "assignment_valid_flag",
        "low_exposure_flag",
    ]

    rows = []

    for context_col in binary_context_columns:
        for outcome_col in OUTCOME_COLUMNS:
            if context_col == outcome_col:
                continue

            grouped = df.groupby(context_col, dropna=False)[outcome_col].mean() * 100

            rows.append(
                {
                    "context_variable": context_col,
                    "outcome_variable": outcome_col,
                    "group_0_rate_percent": round(grouped.get(0, np.nan), 2),
                    "group_1_rate_percent": round(grouped.get(1, np.nan), 2),
                    "difference_percentage_points": round(
                        grouped.get(1, np.nan) - grouped.get(0, np.nan),
                        2,
                    ),
                }
            )

    return pd.DataFrame(rows)


def build_engagement_retention_summary(df: pd.DataFrame) -> pd.DataFrame:
    engagement_cols = [
        "engagement_band",
        "feature_adoption_band",
    ]

    rows = []

    for col in engagement_cols:
        summary = (
            df.groupby([col, GROUP_COLUMN], dropna=False)
            .agg(
                user_count=("user_id", "count"),
                activation_rate_percent=(
                    "activation_flag",
                    lambda x: round(x.mean() * 100, 2),
                ),
                retained_30d_rate_percent=(
                    "retained_30d",
                    lambda x: round(x.mean() * 100, 2),
                ),
                retained_60d_rate_percent=(
                    "retained_60d",
                    lambda x: round(x.mean() * 100, 2),
                ),
                churn_30d_rate_percent=(
                    "churn_30d",
                    lambda x: round(x.mean() * 100, 2),
                ),
                upgrade_rate_percent=(
                    "upgrade_flag",
                    lambda x: round(x.mean() * 100, 2),
                ),
            )
            .reset_index()
        )

        summary = summary.rename(columns={col: "engagement_segment"})
        summary.insert(0, "segment_type", col)

        rows.append(summary)

    result = pd.concat(rows, ignore_index=True)

    return result


def main():
    df = pd.read_csv(DATA_PATH)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    overall_correlations = build_overall_correlations(df)
    group_correlations = build_group_correlations(df)
    binary_relationships = build_binary_relationships(df)
    engagement_retention = build_engagement_retention_summary(df)

    save_table(
        overall_correlations,
        OUTPUT_DIR / "overall_metric_outcome_correlations.csv",
    )

    save_table(
        group_correlations,
        OUTPUT_DIR / "experiment_group_metric_outcome_correlations.csv",
    )

    save_table(
        binary_relationships,
        OUTPUT_DIR / "binary_context_outcome_relationships.csv",
    )

    save_table(
        engagement_retention,
        OUTPUT_DIR / "engagement_retention_relationships.csv",
    )

    print("Saved overall metric-outcome correlations")
    print("Saved experiment-group metric-outcome correlations")
    print("Saved binary context-outcome relationships")
    print("Saved engagement-retention relationships")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()