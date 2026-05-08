from pathlib import Path

import numpy as np
import pandas as pd


DATA_PATH = Path(
    "projects/p06_product_experimentation/data/cleaned/saas_experimentation_cleaned.csv"
)

OUTPUT_DIR = Path(
    "projects/p06_product_experimentation/outputs/segmentation"
)

GROUP_COLUMN = "experiment_group"
CONTROL_GROUP = "control"
TREATMENT_GROUP = "treatment"

SEGMENT_COLUMNS = [
    "company_size",
    "acquisition_channel",
    "region",
    "industry",
    "engagement_band",
    "feature_adoption_band",
    "subscription_value_band",
]

OUTCOME_COLUMNS = [
    "onboarding_completion_flag",
    "activation_flag",
    "retained_30d",
    "retained_60d",
    "churn_30d",
    "upgrade_flag",
]


def save_table(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def safe_rate(series: pd.Series) -> float:
    if len(series.dropna()) == 0:
        return np.nan
    return series.mean() * 100


def summarize_segment_effects(
    df: pd.DataFrame,
    segment_col: str,
) -> pd.DataFrame:
    rows = []

    for segment_value, segment_df in df.groupby(segment_col, dropna=False):
        control_df = segment_df[segment_df[GROUP_COLUMN] == CONTROL_GROUP]
        treatment_df = segment_df[segment_df[GROUP_COLUMN] == TREATMENT_GROUP]

        row = {
            "segment_column": segment_col,
            "segment_value": segment_value,
            "total_users": len(segment_df),
            "control_users": len(control_df),
            "treatment_users": len(treatment_df),
        }

        for outcome in OUTCOME_COLUMNS:
            control_rate = safe_rate(control_df[outcome])
            treatment_rate = safe_rate(treatment_df[outcome])
            lift_pp = treatment_rate - control_rate

            row[f"{outcome}_control_rate_percent"] = round(control_rate, 2)
            row[f"{outcome}_treatment_rate_percent"] = round(treatment_rate, 2)
            row[f"{outcome}_lift_percentage_points"] = round(lift_pp, 2)

        rows.append(row)

    result = pd.DataFrame(rows)

    return result.sort_values(
        by=["segment_column", "total_users"],
        ascending=[True, False],
    )


def summarize_core_segments(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for segment_col in SEGMENT_COLUMNS:
        grouped = (
            df.groupby(segment_col, dropna=False)
            .agg(
                user_count=("user_id", "count"),
                treatment_share_percent=(
                    GROUP_COLUMN,
                    lambda x: round((x == TREATMENT_GROUP).mean() * 100, 2),
                ),
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
                median_sessions_first_14d=("sessions_first_14d", "median"),
                median_feature_adoption_count=("feature_adoption_count", "median"),
                median_subscription_value=("monthly_subscription_value", "median"),
            )
            .reset_index()
        )

        grouped = grouped.rename(columns={segment_col: "segment_value"})
        grouped.insert(0, "segment_column", segment_col)

        rows.append(grouped)

    result = pd.concat(rows, ignore_index=True)

    numeric_cols = result.select_dtypes(include="number").columns
    result[numeric_cols] = result[numeric_cols].round(2)

    return result


def main():
    df = pd.read_csv(DATA_PATH)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    core_segments = summarize_core_segments(df)

    save_table(
        core_segments,
        OUTPUT_DIR / "segment_profile_summary.csv",
    )

    print("Saved segment profile summary")

    for segment_col in SEGMENT_COLUMNS:
        segment_effects = summarize_segment_effects(df, segment_col)

        save_table(
            segment_effects,
            OUTPUT_DIR / f"experiment_effects_by_{segment_col}.csv",
        )

        print(f"Saved experiment effects by {segment_col}")

    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()