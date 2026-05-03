import sys
from pathlib import Path

import pandas as pd

# Allow this script to import from /src
ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR / "src"))

from visualization import (
    ensure_output_dir,
    save_histogram,
    save_bar_chart,
    save_boxplot,
)


DATA_PATH = ROOT_DIR / "data" / "marketplace_sample.csv"
PLOT_DIR = Path(__file__).resolve().parent / "plots"


def main():
    df = pd.read_csv(DATA_PATH)
    output_dir = ensure_output_dir(PLOT_DIR)

    save_histogram(
        df,
        "item_price",
        output_dir / "item_price_distribution.png",
        title="Item price distribution",
    )

    save_histogram(
        df,
        "views",
        output_dir / "views_distribution.png",
        title="Views distribution",
    )

    save_histogram(
        df,
        "listing_age_days",
        output_dir / "listing_age_distribution.png",
        title="Listing age distribution",
    )

    save_boxplot(
        df,
        "views",
        output_dir / "views_boxplot.png",
        title="Views boxplot",
    )

    save_bar_chart(
        df["category"].value_counts(),
        output_dir / "category_distribution.png",
        title="Category distribution",
        xlabel="Category",
    )

    save_bar_chart(
        df["shipping_price"].value_counts().sort_index(),
        output_dir / "shipping_tiers.png",
        title="Shipping price tiers",
        xlabel="Shipping price",
    )

    print(f"Saved plots to {output_dir}")


if __name__ == "__main__":
    main()