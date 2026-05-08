"""
Plot creation for P07.

Purpose:
- create executive-oriented forecasting visuals
- visualize cohort retention and operational trends
- display forecast uncertainty and scenario trajectories

Important:
Plots are designed for strategic interpretation and governance-aware reporting.
Forecasts and scenarios are probabilistic and assumption-dependent.
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sys.path.append(str(Path(__file__).resolve().parents[2]))


PLOTS_DIR = Path(
    "projects/p07_saas_strategic_forecasting/outputs/plots"
)

DATA_PATH = Path(
    "projects/p07_saas_strategic_forecasting/data/cleaned/saas_account_monthly_cleaned.csv"
)

RAW_FALLBACK_PATH = Path(
    "projects/p07_saas_strategic_forecasting/data/raw/saas_account_monthly_forecasting.csv"
)

COHORT_RETENTION_PATH = Path(
    "projects/p07_saas_strategic_forecasting/outputs/cohorts/cohort_retention_table.csv"
)

OPERATIONAL_TRENDS_PATH = Path(
    "projects/p07_saas_strategic_forecasting/outputs/trends/operational_trends.csv"
)

FORECAST_RETENTION_PATH = Path(
    "projects/p07_saas_strategic_forecasting/outputs/forecasting/retention_forecast.csv"
)

FORECAST_MRR_PATH = Path(
    "projects/p07_saas_strategic_forecasting/outputs/forecasting/mrr_forecast.csv"
)

FORECAST_RISK_PATH = Path(
    "projects/p07_saas_strategic_forecasting/outputs/forecasting/revenue_at_risk_forecast.csv"
)

SCENARIO_PATH = Path(
    "projects/p07_saas_strategic_forecasting/outputs/scenarios/scenario_summary.csv"
)


# -----------------------------
# Style
# -----------------------------

sns.set_style("whitegrid")

BRAND_MAIN = "#81A0CE"
BRAND_DARK = "#3F4247"
BACKGROUND = "#F6F7F9"


def ensure_output_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def load_data() -> dict:
    data_path = DATA_PATH if DATA_PATH.exists() else RAW_FALLBACK_PATH

    return {
        "raw": pd.read_csv(data_path),
        "cohort": pd.read_csv(COHORT_RETENTION_PATH),
        "trends": pd.read_csv(OPERATIONAL_TRENDS_PATH),
        "retention_forecast": pd.read_csv(FORECAST_RETENTION_PATH),
        "mrr_forecast": pd.read_csv(FORECAST_MRR_PATH),
        "risk_forecast": pd.read_csv(FORECAST_RISK_PATH),
        "scenario": pd.read_csv(SCENARIO_PATH),
    }


# -----------------------------
# Cohort retention curve
# -----------------------------

def plot_retention_curve(cohort_df: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 7), facecolor=BACKGROUND)

    sample_cohorts = (
        cohort_df["cohort_month"]
        .drop_duplicates()
        .sort_values()
        .tail(6)
    )

    for cohort in sample_cohorts:
        subset = cohort_df[cohort_df["cohort_month"] == cohort]

        plt.plot(
            subset["cohort_age_months"],
            subset["retention_rate"],
            linewidth=2,
            label=str(cohort)[:10],
        )

    plt.title(
        "Cohort Retention Curves",
        fontsize=16,
        color=BRAND_DARK,
    )

    plt.xlabel("Cohort Age (Months)")
    plt.ylabel("Retention Rate")

    plt.legend(title="Cohort Month")

    plt.tight_layout()

    plt.savefig(
        PLOTS_DIR / "retention_curve.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


# -----------------------------
# Cohort heatmap
# -----------------------------

def plot_cohort_heatmap(cohort_df: pd.DataFrame) -> None:
    pivot = cohort_df.pivot_table(
        index="cohort_month",
        columns="cohort_age_months",
        values="retention_rate",
    )

    plt.figure(figsize=(14, 8), facecolor=BACKGROUND)

    sns.heatmap(
        pivot,
        cmap="Blues",
        linewidths=0.5,
        annot=False,
    )

    plt.title(
        "Cohort Retention Heatmap",
        fontsize=16,
        color=BRAND_DARK,
    )

    plt.xlabel("Cohort Age (Months)")
    plt.ylabel("Cohort Month")

    plt.tight_layout()

    plt.savefig(
        PLOTS_DIR / "cohort_heatmap.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


# -----------------------------
# Rolling health trend
# -----------------------------

def plot_health_trend(trends_df: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 6), facecolor=BACKGROUND)

    plt.plot(
        trends_df["snapshot_month"],
        trends_df["health_trend_3m"],
        linewidth=3,
        color=BRAND_MAIN,
    )

    plt.title(
        "Rolling Product Health Trend (3-Month)",
        fontsize=16,
        color=BRAND_DARK,
    )

    plt.xlabel("Snapshot Month")
    plt.ylabel("Average Product Health")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        PLOTS_DIR / "rolling_health_trend.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


# -----------------------------
# Forecast band plot
# -----------------------------

def plot_forecast_band(retention_forecast: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 6), facecolor=BACKGROUND)

    x = retention_forecast["forecast_month"]

    plt.plot(
        x,
        retention_forecast["forecast_retention_rate"],
        linewidth=3,
        color=BRAND_MAIN,
        label="Forecast Retention",
    )

    plt.fill_between(
        x,
        retention_forecast["forecast_retention_lower"],
        retention_forecast["forecast_retention_upper"],
        alpha=0.25,
        color=BRAND_MAIN,
        label="Forecast Band",
    )

    plt.title(
        "Retention Forecast With Uncertainty Band",
        fontsize=16,
        color=BRAND_DARK,
    )

    plt.xlabel("Forecast Month")
    plt.ylabel("Retention Rate")

    plt.legend()

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        PLOTS_DIR / "forecast_band.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


# -----------------------------
# MRR forecast trajectory
# -----------------------------

def plot_mrr_forecast(mrr_forecast: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 6), facecolor=BACKGROUND)

    x = mrr_forecast["forecast_month"]

    plt.plot(
        x,
        mrr_forecast["forecast_total_mrr"],
        linewidth=3,
        color=BRAND_MAIN,
        label="Projected MRR",
    )

    plt.fill_between(
        x,
        mrr_forecast["forecast_mrr_lower"],
        mrr_forecast["forecast_mrr_upper"],
        alpha=0.25,
        color=BRAND_MAIN,
    )

    plt.title(
        "Projected MRR Trajectory",
        fontsize=16,
        color=BRAND_DARK,
    )

    plt.xlabel("Forecast Month")
    plt.ylabel("Projected MRR")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        PLOTS_DIR / "mrr_forecast_trajectory.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


# -----------------------------
# Revenue at risk forecast
# -----------------------------

def plot_revenue_at_risk(risk_forecast: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 6), facecolor=BACKGROUND)

    x = risk_forecast["forecast_month"]

    plt.plot(
        x,
        risk_forecast["forecast_revenue_at_risk"],
        linewidth=3,
        color=BRAND_DARK,
    )

    plt.fill_between(
        x,
        risk_forecast["forecast_revenue_at_risk_lower"],
        risk_forecast["forecast_revenue_at_risk_upper"],
        alpha=0.25,
        color=BRAND_DARK,
    )

    plt.title(
        "Projected Revenue at Risk",
        fontsize=16,
        color=BRAND_DARK,
    )

    plt.xlabel("Forecast Month")
    plt.ylabel("Revenue at Risk")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        PLOTS_DIR / "revenue_at_risk_forecast.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


# -----------------------------
# Scenario trajectory comparison
# -----------------------------

def plot_scenario_trajectory(scenario_df: pd.DataFrame) -> None:
    plt.figure(figsize=(13, 7), facecolor=BACKGROUND)

    for scenario, group in scenario_df.groupby("scenario"):
        plt.plot(
            group["forecast_horizon_month"],
            group["projected_mrr"],
            linewidth=2,
            label=scenario,
        )

    plt.title(
        "Scenario-Based Projected MRR Trajectories",
        fontsize=16,
        color=BRAND_DARK,
    )

    plt.xlabel("Forecast Horizon Month")
    plt.ylabel("Projected MRR")

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        PLOTS_DIR / "scenario_revenue_trajectory.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


# -----------------------------
# Operational deterioration plot
# -----------------------------

def plot_operational_deterioration(trends_df: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 7), facecolor=BACKGROUND)

    plt.plot(
        trends_df["snapshot_month"],
        trends_df["avg_days_since_last_login"],
        linewidth=2,
        label="Inactivity",
    )

    plt.plot(
        trends_df["snapshot_month"],
        trends_df["avg_support_tickets"],
        linewidth=2,
        label="Support Burden",
    )

    plt.plot(
        trends_df["snapshot_month"],
        trends_df["avg_feature_adoption"],
        linewidth=2,
        label="Feature Adoption",
    )

    plt.title(
        "Operational Leading Indicators",
        fontsize=16,
        color=BRAND_DARK,
    )

    plt.xlabel("Snapshot Month")

    plt.legend()

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        PLOTS_DIR / "operational_leading_indicators.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


# -----------------------------
# Main
# -----------------------------

def main() -> None:
    ensure_output_dir(PLOTS_DIR)

    data = load_data()

    plot_retention_curve(data["cohort"])
    plot_cohort_heatmap(data["cohort"])
    plot_health_trend(data["trends"])

    plot_forecast_band(data["retention_forecast"])
    plot_mrr_forecast(data["mrr_forecast"])
    plot_revenue_at_risk(data["risk_forecast"])

    plot_scenario_trajectory(data["scenario"])
    plot_operational_deterioration(data["trends"])

    print(f"Saved plots to: {PLOTS_DIR}")


if __name__ == "__main__":
    main()