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
    # Load cleaned inference dataset
    df = pd.read_csv(data_path)

    # Output directory
    output_path = ensure_output_dir(output_dir)

    # -------------------------
    # Risk distributions
    # -------------------------

    save_histogram(
        df,
        "risk_score",
        output_path / "risk_score_distribution.png",
        title="Risk score distribution",
    )

    save_histogram(
        df,
        "loan_to_income_ratio",
        output_path / "loan_to_income_ratio_distribution.png",
        title="Loan-to-income ratio distribution",
    )

    save_histogram(
        df,
        "days_late_average",
        output_path / "days_late_average_distribution.png",
        title="Average days late distribution",
    )

    # -------------------------
    # Operational repayment behavior
    # -------------------------

    save_histogram(
        df,
        "missed_payments_last_6m",
        output_path / "missed_payments_last_6m_distribution.png",
        title="Missed payments (last 6 months)",
    )

    save_histogram(
        df,
        "repayment_probability_score",
        output_path / "repayment_probability_distribution.png",
        title="Repayment probability score distribution",
    )

    # -------------------------
    # Group balance checks
    # -------------------------

    save_bar_chart(
        df["risk_tier"].value_counts(),
        output_path / "risk_tier_distribution.png",
        title="Risk tier distribution",
        xlabel="Risk tier",
    )

    save_bar_chart(
        df["intervention_group"].value_counts(),
        output_path / "intervention_group_distribution.png",
        title="Intervention group distribution",
        xlabel="Intervention group",
    )

    save_bar_chart(
        df["current_delinquency_flag"]
        .value_counts()
        .sort_index(),
        output_path / "current_delinquency_distribution.png",
        title="Current delinquency distribution",
        xlabel="Current delinquency",
    )

    print(f"Saved plots to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Create fintech inference plots."
    )

    parser.add_argument("--data", required=True)

    parser.add_argument(
        "--output-dir",
        default="projects/p04_fintech_inference/outputs/plots",
    )

    args = parser.parse_args()

    create_descriptive_plots(
        data_path=args.data,
        output_dir=args.output_dir,
    )


if __name__ == "__main__":
    main()