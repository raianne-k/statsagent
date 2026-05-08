"""
Forecasting analysis for P07.

Purpose:
- build interpretable operational forecasts
- estimate retention and revenue trajectories
- create forecast bands
- support scenario modeling and executive reporting

Important:
Forecasts are probabilistic directional estimates based on historical patterns.
They should not be interpreted as guaranteed future outcomes.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import yaml


CONFIG_PATH = Path(
    "projects/p07_saas_strategic_forecasting/configs/project_config.yaml"
)

RAW_FALLBACK_PATH = Path(
    "projects/p07_saas_strategic_forecasting/data/raw/saas_account_monthly_forecasting.csv"
)


def load_config(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def ensure_output_dirs(config: dict) -> None:
    for path in config["outputs"]["forecasting"].values():
        Path(path).parent.mkdir(parents=True, exist_ok=True)


def load_data(config: dict) -> pd.DataFrame:
    cleaned_path = Path(config["data"]["cleaned_path"])
    path = cleaned_path if cleaned_path.exists() else RAW_FALLBACK_PATH

    df = pd.read_csv(path)

    df["snapshot_month"] = pd.to_datetime(df["snapshot_month"])
    df["signup_month"] = pd.to_datetime(df["signup_month"])
    df["cohort_month"] = pd.to_datetime(df["cohort_month"])

    return df.sort_values(["account_id", "snapshot_month"])


def build_monthly_operating_frame(df: pd.DataFrame) -> pd.DataFrame:
    monthly = (
        df.groupby("snapshot_month")
        .agg(
            active_accounts=("account_id", "nunique"),
            churn_rate=("churn_flag", "mean"),
            avg_health=("product_health_score", "mean"),
            avg_usage=("usage_frequency", "mean"),
            avg_adoption=("feature_adoption_rate", "mean"),
            avg_support=("support_tickets", "mean"),
            avg_inactivity=("days_since_last_login", "mean"),
            avg_renewal_probability=("renewal_probability", "mean"),
            total_mrr=("monthly_recurring_revenue", "sum"),
            total_revenue_at_risk=("revenue_at_risk", "sum"),
        )
        .reset_index()
        .sort_values("snapshot_month")
    )

    monthly["retention_rate"] = 1 - monthly["churn_rate"]

    monthly["operational_risk_score"] = (
        0.35 * (1 - monthly["avg_health"].clip(0, 1))
        + 0.25 * (monthly["avg_inactivity"] / 90).clip(0, 1)
        + 0.20 * (1 - monthly["avg_adoption"].fillna(50) / 100).clip(0, 1)
        + 0.10 * (monthly["avg_support"].fillna(0) / 10).clip(0, 1)
        + 0.10 * (1 - monthly["avg_usage"] / 31).clip(0, 1)
    ).clip(0, 1)

    return monthly


def linear_projection(series: pd.Series, periods: int) -> list:
    clean = series.dropna().reset_index(drop=True)

    if len(clean) < 3:
        return [clean.iloc[-1]] * periods

    x = np.arange(len(clean))
    y = clean.values

    slope, intercept = np.polyfit(x, y, 1)

    forecasts = []

    for i in range(periods):
        next_x = len(clean) + i
        value = intercept + slope * next_x
        forecasts.append(value)

    return forecasts


def build_forecast_band(base_value: float, step: int, uncertainty_rate: float):
    widening = 1 + (step * uncertainty_rate)

    lower = base_value / widening
    upper = base_value * widening

    return lower, upper


def forecast_retention(monthly: pd.DataFrame, horizon: int) -> pd.DataFrame:
    projected_retention = linear_projection(
        monthly["retention_rate"],
        horizon,
    )

    latest_risk = monthly["operational_risk_score"].tail(3).mean()

    future_months = pd.date_range(
        monthly["snapshot_month"].max() + pd.offsets.MonthBegin(1),
        periods=horizon,
        freq="MS",
    )

    rows = []

    for idx, (month, retention) in enumerate(
        zip(future_months, projected_retention),
        start=1,
    ):
        operational_decay = latest_risk * 0.018 * idx
        retention = retention - operational_decay
        retention = np.clip(retention, 0.86, 0.99)

        lower, upper = build_forecast_band(
            retention,
            step=idx,
            uncertainty_rate=0.035,
        )

        rows.append({
            "forecast_month": month,
            "forecast_retention_rate": round(retention, 4),
            "forecast_retention_lower": round(max(0, lower), 4),
            "forecast_retention_upper": round(min(1, upper), 4),
            "forecast_horizon_month": idx,
            "forecast_method": "linear_projection_with_operational_decay_and_uncertainty_band",
        })

    return pd.DataFrame(rows)


def forecast_churn_risk(monthly: pd.DataFrame, horizon: int) -> pd.DataFrame:
    projected_churn = linear_projection(
        monthly["churn_rate"],
        horizon,
    )

    latest_risk = monthly["operational_risk_score"].tail(3).mean()

    future_months = pd.date_range(
        monthly["snapshot_month"].max() + pd.offsets.MonthBegin(1),
        periods=horizon,
        freq="MS",
    )

    rows = []

    for idx, (month, churn_rate) in enumerate(
        zip(future_months, projected_churn),
        start=1,
    ):
        operational_pressure = latest_risk * 0.018 * idx
        churn_rate = churn_rate + operational_pressure
        churn_rate = np.clip(churn_rate, 0.01, 0.14)

        lower, upper = build_forecast_band(
            churn_rate,
            step=idx,
            uncertainty_rate=0.06,
        )

        rows.append({
            "forecast_month": month,
            "forecast_churn_rate": round(churn_rate, 4),
            "forecast_churn_lower": round(max(0, lower), 4),
            "forecast_churn_upper": round(min(1, upper), 4),
            "forecast_horizon_month": idx,
            "forecast_method": "linear_projection_with_operational_pressure_and_uncertainty_band",
        })

    return pd.DataFrame(rows)


def forecast_mrr(monthly: pd.DataFrame, horizon: int) -> pd.DataFrame:
    projected_mrr = linear_projection(
        monthly["total_mrr"],
        horizon,
    )

    latest_risk = monthly["operational_risk_score"].tail(3).mean()

    future_months = pd.date_range(
        monthly["snapshot_month"].max() + pd.offsets.MonthBegin(1),
        periods=horizon,
        freq="MS",
    )

    rows = []

    for idx, (month, mrr) in enumerate(
        zip(future_months, projected_mrr),
        start=1,
    ):
        risk_adjustment = 1 - (latest_risk * 0.010 * idx)
        mrr = max(0, mrr * risk_adjustment)

        lower, upper = build_forecast_band(
            mrr,
            step=idx,
            uncertainty_rate=0.08,
        )

        rows.append({
            "forecast_month": month,
            "forecast_total_mrr": round(mrr, 2),
            "forecast_mrr_lower": round(max(0, lower), 2),
            "forecast_mrr_upper": round(upper, 2),
            "forecast_horizon_month": idx,
            "forecast_method": "linear_projection_with_operational_risk_adjustment_and_uncertainty_band",
        })

    return pd.DataFrame(rows)


def forecast_revenue_at_risk(monthly: pd.DataFrame, horizon: int) -> pd.DataFrame:
    projected_risk = linear_projection(
        monthly["total_revenue_at_risk"],
        horizon,
    )

    latest_risk = monthly["operational_risk_score"].tail(3).mean()

    future_months = pd.date_range(
        monthly["snapshot_month"].max() + pd.offsets.MonthBegin(1),
        periods=horizon,
        freq="MS",
    )

    rows = []

    for idx, (month, risk) in enumerate(
        zip(future_months, projected_risk),
        start=1,
    ):
        risk = max(0, risk * (1 + latest_risk * 0.035 * idx))

        lower, upper = build_forecast_band(
            risk,
            step=idx,
            uncertainty_rate=0.10,
        )

        rows.append({
            "forecast_month": month,
            "forecast_revenue_at_risk": round(risk, 2),
            "forecast_revenue_at_risk_lower": round(max(0, lower), 2),
            "forecast_revenue_at_risk_upper": round(upper, 2),
            "forecast_horizon_month": idx,
            "forecast_method": "linear_projection_with_operational_risk_adjustment_and_uncertainty_band",
        })

    return pd.DataFrame(rows)


def build_forecast_summary(
    retention_forecast: pd.DataFrame,
    churn_forecast: pd.DataFrame,
    mrr_forecast: pd.DataFrame,
    risk_forecast: pd.DataFrame,
) -> pd.DataFrame:
    rows = []

    rows.append({
        "metric": "retention_rate",
        "latest_forecast": retention_forecast["forecast_retention_rate"].iloc[-1],
        "forecast_direction": (
            "improving"
            if retention_forecast["forecast_retention_rate"].iloc[-1]
            > retention_forecast["forecast_retention_rate"].iloc[0]
            else "deteriorating"
        ),
    })

    rows.append({
        "metric": "churn_rate",
        "latest_forecast": churn_forecast["forecast_churn_rate"].iloc[-1],
        "forecast_direction": (
            "improving"
            if churn_forecast["forecast_churn_rate"].iloc[-1]
            < churn_forecast["forecast_churn_rate"].iloc[0]
            else "deteriorating"
        ),
    })

    rows.append({
        "metric": "total_mrr",
        "latest_forecast": mrr_forecast["forecast_total_mrr"].iloc[-1],
        "forecast_direction": (
            "growing"
            if mrr_forecast["forecast_total_mrr"].iloc[-1]
            > mrr_forecast["forecast_total_mrr"].iloc[0]
            else "declining"
        ),
    })

    rows.append({
        "metric": "revenue_at_risk",
        "latest_forecast": risk_forecast["forecast_revenue_at_risk"].iloc[-1],
        "forecast_direction": (
            "improving"
            if risk_forecast["forecast_revenue_at_risk"].iloc[-1]
            < risk_forecast["forecast_revenue_at_risk"].iloc[0]
            else "deteriorating"
        ),
    })

    return pd.DataFrame(rows)


def main() -> None:
    config = load_config(CONFIG_PATH)
    ensure_output_dirs(config)

    df = load_data(config)

    horizon = config["forecasting"]["forecast_horizon_months"]

    monthly = build_monthly_operating_frame(df)

    retention_forecast = forecast_retention(monthly, horizon)
    churn_forecast = forecast_churn_risk(monthly, horizon)
    mrr_forecast = forecast_mrr(monthly, horizon)
    risk_forecast = forecast_revenue_at_risk(monthly, horizon)

    forecast_summary = build_forecast_summary(
        retention_forecast,
        churn_forecast,
        mrr_forecast,
        risk_forecast,
    )

    retention_path = Path(
        config["outputs"]["forecasting"]["retention_forecast"]
    )

    churn_path = Path(
        config["outputs"]["forecasting"]["churn_risk_forecast"]
    )

    mrr_path = Path(
        config["outputs"]["forecasting"]["mrr_forecast"]
    )

    risk_path = Path(
        config["outputs"]["forecasting"]["revenue_at_risk_forecast"]
    )

    summary_path = retention_path.parent / "forecast_summary.csv"

    retention_forecast.to_csv(retention_path, index=False)
    churn_forecast.to_csv(churn_path, index=False)
    mrr_forecast.to_csv(mrr_path, index=False)
    risk_forecast.to_csv(risk_path, index=False)
    forecast_summary.to_csv(summary_path, index=False)

    print("Forecasting analysis complete.")
    print(f"Saved retention forecast: {retention_path}")
    print(f"Saved churn-risk forecast: {churn_path}")
    print(f"Saved MRR forecast: {mrr_path}")
    print(f"Saved revenue-at-risk forecast: {risk_path}")
    print(f"Saved forecast summary: {summary_path}")


if __name__ == "__main__":
    main()