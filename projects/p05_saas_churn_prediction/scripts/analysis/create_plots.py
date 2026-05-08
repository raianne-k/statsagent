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
    df = pd.read_csv(data_path)
    output_path = ensure_output_dir(output_dir)

    save_histogram(
        df,
        "account_health_score",
        output_path / "account_health_score_distribution.png",
        title="Account health score distribution",
    )

    save_histogram(
        df,
        "feature_adoption_rate",
        output_path / "feature_adoption_rate_distribution.png",
        title="Feature adoption rate distribution",
    )

    save_histogram(
        df,
        "seat_utilization_percent",
        output_path / "seat_utilization_distribution.png",
        title="Seat utilization distribution",
    )

    save_histogram(
        df,
        "days_since_last_login",
        output_path / "days_since_last_login_distribution.png",
        title="Days since last login distribution",
    )

    save_histogram(
        df,
        "monthly_recurring_revenue",
        output_path / "monthly_recurring_revenue_distribution.png",
        title="Monthly recurring revenue distribution",
    )

    save_bar_chart(
        df["churned"].value_counts().sort_index(),
        output_path / "churn_distribution.png",
        title="Churn distribution",
        xlabel="Churned",
    )

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
        df["contract_type"].value_counts(),
        output_path / "contract_type_distribution.png",
        title="Contract type distribution",
        xlabel="Contract type",
    )

    save_bar_chart(
        df["plan_tier"].value_counts(),
        output_path / "plan_tier_distribution.png",
        title="Plan tier distribution",
        xlabel="Plan tier",
    )

    print(f"Saved plots to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Create SaaS churn prediction plots."
    )

    parser.add_argument("--data", required=True)

    parser.add_argument(
        "--output-dir",
        default="projects/p05_saas_churn_prediction/outputs/plots",
    )

    args = parser.parse_args()

    create_descriptive_plots(
        data_path=args.data,
        output_dir=args.output_dir,
    )


if __name__ == "__main__":
    main()