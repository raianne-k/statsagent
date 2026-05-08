"""
Scenario modeling for P07.

Purpose:
- evaluate directional impact of operational improvement scenarios
- estimate scenario-adjusted retention, churn, MRR, and revenue-at-risk trajectories
- support executive decision discussions

Important:
Scenario outputs are assumption-dependent planning estimates.
They are not causal proof and do not guarantee business outcomes.

Metric governance:
- Scenario retention uses the same definition as forecasting_analysis.py:
  monthly operational retention = 1 - monthly churn risk.
- It does NOT use cumulative cohort survival.
"""

from pathlib import Path

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


def load_data(config: dict) -> pd.DataFrame:
    cleaned_path = Path(config["data"]["cleaned_path"])
    path = cleaned_path if cleaned_path.exists() else RAW_FALLBACK_PATH

    df = pd.read_csv(path)

    df["snapshot_month"] = pd.to_datetime(df["snapshot_month"])
    df["signup_month"] = pd.to_datetime(df["signup_month"])
    df["cohort_month"] = pd.to_datetime(df["cohort_month"])

    return df.sort_values(["account_id", "snapshot_month"])


def ensure_output_dirs(config: dict) -> None:
    for path in config["outputs"]["scenarios"].values():
        Path(path).parent.mkdir(parents=True, exist_ok=True)


def read_forecast_outputs(config: dict) -> dict:
    forecasting_paths = config["outputs"]["forecasting"]

    retention = pd.read_csv(forecasting_paths["retention_forecast"])
    churn = pd.read_csv(forecasting_paths["churn_risk_forecast"])
    mrr = pd.read_csv(forecasting_paths["mrr_forecast"])
    risk = pd.read_csv(forecasting_paths["revenue_at_risk_forecast"])

    return {
        "retention": retention,
        "churn": churn,
        "mrr": mrr,
        "risk": risk,
    }


def get_latest_active_snapshot(df: pd.DataFrame) -> pd.DataFrame:
    latest_month = df["snapshot_month"].max()
    return df[df["snapshot_month"] == latest_month].copy()


def prepare_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()

    float_columns = [
        "onboarding_completion",
        "days_since_last_login",
        "feature_adoption_rate",
        "usage_frequency",
        "support_tickets",
        "product_health_score",
        "monthly_recurring_revenue",
        "renewal_probability",
        "revenue_at_risk",
    ]

    for col in float_columns:
        if col in result.columns:
            result[col] = pd.to_numeric(result[col], errors="coerce").astype(float)

    return result


def estimate_operational_risk(df: pd.DataFrame) -> float:
    """
    Estimate portfolio-level operational risk from latest account state.

    This is used only to scale scenario sensitivity.
    """

    latest = prepare_numeric_columns(df)

    health_risk = 1 - latest["product_health_score"].clip(0, 1)
    inactivity_risk = (latest["days_since_last_login"] / 90).clip(0, 1)
    adoption_risk = (1 - latest["feature_adoption_rate"].fillna(50) / 100).clip(0, 1)
    support_risk = (latest["support_tickets"].fillna(0) / 10).clip(0, 1)
    onboarding_risk = (1 - latest["onboarding_completion"] / 100).clip(0, 1)
    usage_risk = (1 - latest["usage_frequency"] / 31).clip(0, 1)

    risk_score = (
        0.30 * health_risk
        + 0.22 * inactivity_risk
        + 0.18 * adoption_risk
        + 0.12 * onboarding_risk
        + 0.10 * usage_risk
        + 0.08 * support_risk
    )

    return float(risk_score.mean())


def scenario_effects() -> dict:
    """
    Scenario effects are intentionally modest.

    Values represent final-horizon directional impact.
    They are applied gradually across forecast months.
    """

    return {
        "current_trajectory": {
            "retention_uplift": 0.000,
            "mrr_uplift": 0.000,
            "risk_reduction": 0.000,
            "note": "Baseline current trajectory with no operational adjustment.",
        },
        "improved_onboarding": {
            "retention_uplift": 0.010,
            "mrr_uplift": 0.012,
            "risk_reduction": 0.070,
            "note": "Improves onboarding for lower-onboarding accounts; expected to modestly improve retention and reduce revenue risk.",
        },
        "reduced_inactivity": {
            "retention_uplift": 0.012,
            "mrr_uplift": 0.014,
            "risk_reduction": 0.090,
            "note": "Reduces inactivity for accounts with login gaps; expected to improve medium-term retention resilience.",
        },
        "higher_feature_adoption": {
            "retention_uplift": 0.014,
            "mrr_uplift": 0.018,
            "risk_reduction": 0.100,
            "note": "Improves feature adoption for lower-adoption accounts; expected to strengthen product stickiness and revenue resilience.",
        },
        "lower_support_burden": {
            "retention_uplift": 0.004,
            "mrr_uplift": 0.005,
            "risk_reduction": 0.035,
            "note": "Reduces support burden for higher-friction accounts; expected impact is smaller and more operationally indirect.",
        },
        "engagement_improvement": {
            "retention_uplift": 0.020,
            "mrr_uplift": 0.028,
            "risk_reduction": 0.140,
            "note": "Improves adoption, usage, login recency, and product health for lower-engagement accounts; expected to have the strongest directional effect.",
        },
    }


def build_scenario_summary(
    forecasts: dict,
    latest_accounts: pd.DataFrame,
    operational_risk_score: float,
) -> pd.DataFrame:
    effects = scenario_effects()
    rows = []

    retention_forecast = forecasts["retention"]
    churn_forecast = forecasts["churn"]
    mrr_forecast = forecasts["mrr"]
    risk_forecast = forecasts["risk"]

    latest_active_accounts = latest_accounts["account_id"].nunique()
    latest_total_mrr = latest_accounts["monthly_recurring_revenue"].sum()

    for scenario_name, effect in effects.items():
        for idx in range(len(retention_forecast)):
            horizon = int(retention_forecast.loc[idx, "forecast_horizon_month"])
            horizon_share = horizon / retention_forecast["forecast_horizon_month"].max()

            baseline_retention = float(
                retention_forecast.loc[idx, "forecast_retention_rate"]
            )
            baseline_churn = float(
                churn_forecast.loc[idx, "forecast_churn_rate"]
            )
            baseline_mrr = float(
                mrr_forecast.loc[idx, "forecast_total_mrr"]
            )
            baseline_risk = float(
                risk_forecast.loc[idx, "forecast_revenue_at_risk"]
            )

            risk_scaled_retention_uplift = (
                effect["retention_uplift"]
                * horizon_share
                * (0.75 + operational_risk_score)
            )

            risk_scaled_mrr_uplift = (
                effect["mrr_uplift"]
                * horizon_share
                * (0.75 + operational_risk_score)
            )

            risk_scaled_risk_reduction = (
                effect["risk_reduction"]
                * horizon_share
                * (0.75 + operational_risk_score)
            )

            projected_retention = min(
                0.985,
                baseline_retention + risk_scaled_retention_uplift,
            )

            projected_churn = max(
                0.005,
                1 - projected_retention,
            )

            projected_mrr = baseline_mrr * (1 + risk_scaled_mrr_uplift)

            projected_revenue_at_risk = baseline_risk * (
                1 - risk_scaled_risk_reduction
            )

            rows.append({
                "scenario": scenario_name,
                "forecast_horizon_month": horizon,
                "projected_retention_rate": round(projected_retention, 4),
                "projected_churn_rate": round(projected_churn, 4),
                "projected_mrr": round(projected_mrr, 2),
                "projected_revenue_at_risk": round(projected_revenue_at_risk, 2),
                "baseline_retention_rate": round(baseline_retention, 4),
                "baseline_churn_rate": round(baseline_churn, 4),
                "baseline_projected_mrr": round(baseline_mrr, 2),
                "baseline_revenue_at_risk": round(baseline_risk, 2),
                "active_accounts_at_baseline": latest_active_accounts,
                "baseline_total_mrr": round(latest_total_mrr, 2),
                "scenario_note": effect["note"],
                "governance_note": (
                    "Scenario estimate is assumption-dependent and not causal proof."
                ),
            })

    return pd.DataFrame(rows)


def build_scenario_comparison(scenario_summary: pd.DataFrame) -> pd.DataFrame:
    baseline = scenario_summary[
        scenario_summary["scenario"] == "current_trajectory"
    ].copy()

    comparison_rows = []

    max_horizon = scenario_summary["forecast_horizon_month"].max()

    baseline_latest = baseline[
        baseline["forecast_horizon_month"] == max_horizon
    ].iloc[0]

    for scenario_name, scenario_df in scenario_summary.groupby("scenario"):
        if scenario_name == "current_trajectory":
            continue

        latest = scenario_df[
            scenario_df["forecast_horizon_month"] == max_horizon
        ].iloc[0]

        comparison_rows.append({
            "scenario": scenario_name,
            "horizon_month": max_horizon,
            "projected_retention_rate": latest["projected_retention_rate"],
            "baseline_retention_rate": baseline_latest["projected_retention_rate"],
            "retention_rate_difference": round(
                latest["projected_retention_rate"]
                - baseline_latest["projected_retention_rate"],
                4,
            ),
            "projected_mrr": latest["projected_mrr"],
            "baseline_projected_mrr": baseline_latest["projected_mrr"],
            "projected_mrr_difference": round(
                latest["projected_mrr"] - baseline_latest["projected_mrr"],
                2,
            ),
            "projected_revenue_at_risk": latest["projected_revenue_at_risk"],
            "baseline_revenue_at_risk": baseline_latest["projected_revenue_at_risk"],
            "revenue_at_risk_difference": round(
                latest["projected_revenue_at_risk"]
                - baseline_latest["projected_revenue_at_risk"],
                2,
            ),
            "interpretation_warning": (
                "Difference reflects scenario assumptions, not proven causal impact."
            ),
        })

    return pd.DataFrame(comparison_rows).sort_values(
        "projected_mrr_difference",
        ascending=False,
    )


def main() -> None:
    config = load_config(CONFIG_PATH)
    ensure_output_dirs(config)

    df = load_data(config)
    latest_accounts = get_latest_active_snapshot(df)
    latest_accounts = prepare_numeric_columns(latest_accounts)

    forecasts = read_forecast_outputs(config)
    operational_risk_score = estimate_operational_risk(latest_accounts)

    scenario_summary = build_scenario_summary(
        forecasts=forecasts,
        latest_accounts=latest_accounts,
        operational_risk_score=operational_risk_score,
    )

    scenario_comparison = build_scenario_comparison(scenario_summary)

    scenario_summary_path = Path(
        config["outputs"]["scenarios"]["scenario_summary"]
    )

    scenario_revenue_impact_path = Path(
        config["outputs"]["scenarios"]["scenario_revenue_impact"]
    )

    scenario_summary.to_csv(scenario_summary_path, index=False)
    scenario_comparison.to_csv(scenario_revenue_impact_path, index=False)

    print("Scenario modeling complete.")
    print(f"Saved scenario summary: {scenario_summary_path}")
    print(f"Saved scenario revenue impact: {scenario_revenue_impact_path}")
    print(f"Operational risk score: {operational_risk_score:.3f}")
    print(f"Scenarios modeled: {scenario_summary['scenario'].nunique()}")
    print(f"Forecast horizon: {scenario_summary['forecast_horizon_month'].max()} months")


if __name__ == "__main__":
    main()