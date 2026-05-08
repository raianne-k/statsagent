import argparse

import pandas as pd

from src.visualization.visualization import (
    ensure_output_dir,
    save_histogram,
    save_bar_chart,
)


def create_descriptive_plots(data_path: str, output_dir: str) -> None:
    # Load data - Use the cleaned fintech dataset.
    df = pd.read_csv(data_path)

    # Output directory - Save plots to project outputs/plots.
    output_path = ensure_output_dir(output_dir)

    # Financial distributions - Check skew and scale.
    save_histogram(
        df,
        "active_loan_amount",
        output_path / "active_loan_amount_distribution.png",
        title="Active loan amount distribution",
    )

    save_histogram(
        df,
        "loan_to_income_ratio",
        output_path / "loan_to_income_ratio_distribution.png",
        title="Loan-to-income ratio distribution",
    )

    save_histogram(
        df,
        "savings_balance",
        output_path / "savings_balance_distribution.png",
        title="Savings balance distribution",
    )

    # Segment balance - Check whether groups are usable for comparison.
    save_bar_chart(
        df["risk_band"].value_counts(),
        output_path / "risk_band_distribution.png",
        title="Risk band distribution",
        xlabel="Risk band",
    )

    save_bar_chart(
        df["income_band"].value_counts(),
        output_path / "income_band_distribution.png",
        title="Income band distribution",
        xlabel="Income band",
    )

    # Core risk outcome - Baseline delinquency share.
    save_bar_chart(
        df["delinquency_flag"].value_counts().sort_index(),
        output_path / "delinquency_flag_distribution.png",
        title="Delinquency flag distribution",
        xlabel="Delinquency flag",
    )

    print(f"Saved plots to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Create fintech descriptive plots.")

    parser.add_argument("--data", required=True)
    parser.add_argument(
        "--output-dir",
        default="projects/p02_fintech_customer_segmentation/outputs/plots",
    )

    args = parser.parse_args()

    create_descriptive_plots(
        data_path=args.data,
        output_dir=args.output_dir,
    )


if __name__ == "__main__":
    main()