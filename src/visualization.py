from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def ensure_output_dir(output_dir: str | Path) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path


def save_histogram(
    df: pd.DataFrame,
    column: str,
    output_path: str | Path,
    bins: int = 30,
    title: str | None = None,
) -> None:
    plt.figure()
    df[column].dropna().hist(bins=bins)
    plt.title(title or f"{column} distribution")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def save_bar_chart(
    series: pd.Series,
    output_path: str | Path,
    title: str,
    xlabel: str,
    ylabel: str = "Count",
) -> None:
    plt.figure()
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def save_boxplot(
    df: pd.DataFrame,
    column: str,
    output_path: str | Path,
    title: str | None = None,
) -> None:
    plt.figure()
    df[column].dropna().plot(kind="box")
    plt.title(title or f"{column} boxplot")
    plt.ylabel(column)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()