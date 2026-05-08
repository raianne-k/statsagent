import argparse
import sys
from pathlib import Path

import pandas as pd


# Allow imports from repo root when running project scripts directly.
sys.path.append(str(Path(__file__).resolve().parents[4]))

from src.visualization.visualization import (
    ensure_output_dir,
    save_histogram,
    save_bar_chart,
)


def create_experiment_plots(data_path: str, output_dir: str) -> None:
    df = pd.read_csv(data_path)

    output_path = ensure_output_dir(output_dir)

    # Experiment structure
    save_bar_chart(
        df["experiment_group"].value_counts(),
        output_path / "experiment_group_distribution.png",
        title="Experiment group distribution",
        xlabel="Experiment group",
    )

    save_bar_chart(
        df["assignment_valid_flag"].value_counts().sort_index(),
        output_path / "assignment_valid_flag_distribution.png",
        title="Assignment validity distribution",
        xlabel="Assignment valid flag",
    )

    save_bar_chart(
        df["low_exposure_flag"].value_counts().sort_index(),
        output_path / "low_exposure_flag_distribution.png",
        title="Low exposure flag distribution",
        xlabel="Low exposure flag",
    )

    # Core outcomes
    save_bar_chart(
        df["activation_flag"].value_counts().sort_index(),
        output_path / "activation_flag_distribution.png",
        title="Activation flag distribution",
        xlabel="Activation flag",
    )

    save_bar_chart(
        df["retained_30d"].value_counts().sort_index(),
        output_path / "retained_30d_distribution.png",
        title="30-day retention distribution",
        xlabel="Retained 30d",
    )

    save_bar_chart(
        df["retained_60d"].value_counts().sort_index(),
        output_path / "retained_60d_distribution.png",
        title="60-day retention distribution",
        xlabel="Retained 60d",
    )

    save_bar_chart(
        df["churn_30d"].value_counts().sort_index(),
        output_path / "churn_30d_distribution.png",
        title="30-day churn distribution",
        xlabel="Churn 30d",
    )

    # Engagement distributions
    save_histogram(
        df,
        "sessions_first_14d",
        output_path / "sessions_first_14d_distribution.png",
        title="Sessions in first 14 days distribution",
    )

    save_histogram(
        df,
        "feature_adoption_count",
        output_path / "feature_adoption_count_distribution.png",
        title="Feature adoption count distribution",
    )

    save_histogram(
        df,
        "support_tickets_first_30d",
        output_path / "support_tickets_first_30d_distribution.png",
        title="Support tickets in first 30 days distribution",
    )

    save_histogram(
        df,
        "monthly_subscription_value",
        output_path / "monthly_subscription_value_distribution.png",
        title="Monthly subscription value distribution",
    )

    save_histogram(
        df,
        "time_to_activation_days",
        output_path / "time_to_activation_days_distribution.png",
        title="Time to activation distribution",
    )

    # Segmentation fields
    save_bar_chart(
        df["acquisition_channel"].value_counts(dropna=False),
        output_path / "acquisition_channel_distribution.png",
        title="Acquisition channel distribution",
        xlabel="Acquisition channel",
    )

    save_bar_chart(
        df["company_size"].value_counts(dropna=False),
        output_path / "company_size_distribution.png",
        title="Company size distribution",
        xlabel="Company size",
    )

    save_bar_chart(
        df["engagement_band"].value_counts(dropna=False),
        output_path / "engagement_band_distribution.png",
        title="Engagement band distribution",
        xlabel="Engagement band",
    )

    print(f"Saved plots to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Create product experimentation descriptive plots."
    )

    parser.add_argument("--data", required=True)

    parser.add_argument(
        "--output-dir",
        default="projects/p06_product_experimentation/outputs/plots",
    )

    args = parser.parse_args()

    create_experiment_plots(
        data_path=args.data,
        output_dir=args.output_dir,
    )


if __name__ == "__main__":
    main()