import sys
from pathlib import Path
import argparse

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.visualization.visualization import (
    ensure_output_dir,
    save_histogram,
    save_bar_chart,
)


def create_descriptive_plots(data_path: str, output_dir: str) -> None:
    # Load data - Use the cleaned SaaS dataset.
    df = pd.read_csv(data_path)

    # Output directory - Save plots to project outputs/plots.
    output_path = ensure_output_dir(output_dir)

    # Usage distributions - Check engagement and product adoption.
    save_histogram(
        df,
        "feature_adoption_rate",
        output_path / "feature_adoption_rate_distribution.png",
        title="Feature adoption rate distribution",
    )

    save_histogram(
        df,
        "seats_used_percent",
        output_path / "seats_used_percent_distribution.png",
        title="Seats used percent distribution",
    )

    save_histogram(
        df,
        "days_since_last_login",
        output_path / "days_since_last_login_distribution.png",
        title="Days since last login distribution",
    )

    # Commercial distribution - Check revenue concentration.
    save_histogram(
        df,
        "monthly_recurring_revenue",
        output_path / "monthly_recurring_revenue_distribution.png",
        title="Monthly recurring revenue distribution",
    )

    # Account health - Check relationship-analysis target structure.
    save_histogram(
        df,
        "account_health_score",
        output_path / "account_health_score_distribution.png",
        title="Account health score distribution",
    )

    # Segment balance - Check whether groups are usable for comparison.
    save_bar_chart(
        df["health_band"].value_counts(),
        output_path / "health_band_distribution.png",
        title="Health band distribution",
        xlabel="Health band",
    )

    save_bar_chart(
        df["usage_band"].value_counts(),
        output_path / "usage_band_distribution.png",
        title="Usage band distribution",
        xlabel="Usage band",
    )

    save_bar_chart(
        df["subscription_plan"].value_counts(),
        output_path / "subscription_plan_distribution.png",
        title="Subscription plan distribution",
        xlabel="Subscription plan",
    )

    # Core outcome - Baseline churn share.
    save_bar_chart(
        df["churn_flag"].value_counts().sort_index(),
        output_path / "churn_flag_distribution.png",
        title="Churn flag distribution",
        xlabel="Churn flag",
    )

    print(f"Saved plots to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Create SaaS descriptive plots.")

    parser.add_argument("--data", required=True)
    parser.add_argument(
        "--output-dir",
        default="projects/p03_saas_relationships/outputs/plots",
    )

    args = parser.parse_args()

    create_descriptive_plots(
        data_path=args.data,
        output_dir=args.output_dir,
    )


if __name__ == "__main__":
    main()