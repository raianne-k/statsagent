import argparse
from pathlib import Path

import pandas as pd

from src.visualization.visualization import (
    ensure_output_dir,
    save_histogram,
    save_bar_chart,
    save_boxplot,
)


def create_descriptive_plots(data_path: str, output_dir: str) -> None:
    # Load data - Use the dataset passed by the run command.
    df = pd.read_csv(data_path)

    # Output directory - Save plots to the project/run-specific folder.
    output_path = ensure_output_dir(output_dir)

    # Continuous distributions - Check skew and spread.
    save_histogram(
        df,
        "item_price",
        output_path / "item_price_distribution.png",
        title="Item price distribution",
    )

    save_histogram(
        df,
        "views",
        output_path / "views_distribution.png",
        title="Views distribution",
    )

    save_histogram(
        df,
        "listing_age_days",
        output_path / "listing_age_distribution.png",
        title="Listing age distribution",
    )

    # Outlier view - Inspect extreme engagement values.
    save_boxplot(
        df,
        "views",
        output_path / "views_boxplot.png",
        title="Views boxplot",
    )

    # Categorical structure - Check marketplace composition.
    save_bar_chart(
        df["category"].value_counts(),
        output_path / "category_distribution.png",
        title="Category distribution",
        xlabel="Category",
    )

    # Tiered pricing - Confirm shipping price behaves like discrete tiers.
    save_bar_chart(
        df["shipping_price"].value_counts().sort_index(),
        output_path / "shipping_tiers.png",
        title="Shipping price tiers",
        xlabel="Shipping price",
    )

    print(f"Saved plots to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Create descriptive analysis plots.")

    parser.add_argument("--data", required=True)
    parser.add_argument("--output-dir", required=True)

    args = parser.parse_args()

    create_descriptive_plots(
        data_path=args.data,
        output_dir=args.output_dir,
    )


if __name__ == "__main__":
    main()