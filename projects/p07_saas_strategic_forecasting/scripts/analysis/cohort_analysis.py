"""
Cohort retention analysis for P07.

Purpose:
- build cohort retention tables
- analyze retention decay by cohort age
- summarize cohort-level MRR and churn behavior
- create outputs used later by forecasting, plotting, dashboard, and reporting

Important:
This script describes observed cohort behavior. It does not infer causality.
"""

from pathlib import Path

import pandas as pd
import yaml


CONFIG_PATH = Path("projects/p07_saas_strategic_forecasting/configs/project_config.yaml")


def load_config(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def ensure_output_dirs(config: dict) -> None:
    output_paths = config["outputs"]["cohorts"]

    for path in output_paths.values():
        Path(path).parent.mkdir(parents=True, exist_ok=True)


def load_data(config: dict) -> pd.DataFrame:
    cleaned_path = Path(config["data"]["cleaned_path"])
    raw_path = Path(config["data"]["raw_path"])

    path = cleaned_path if cleaned_path.exists() else raw_path

    df = pd.read_csv(path)

    df["snapshot_month"] = pd.to_datetime(df["snapshot_month"])
    df["signup_month"] = pd.to_datetime(df["signup_month"])
    df["cohort_month"] = pd.to_datetime(df["cohort_month"])

    return df


def build_cohort_retention_table(df: pd.DataFrame) -> pd.DataFrame:
    cohort_base = (
        df[df["cohort_age_months"] == 0]
        .groupby("cohort_month")["account_id"]
        .nunique()
        .rename("starting_accounts")
        .reset_index()
    )

    cohort_activity = (
        df.groupby(["cohort_month", "cohort_age_months"])
        .agg(
            active_accounts=("account_id", "nunique"),
            churned_accounts=("churn_flag", "sum"),
            total_mrr=("monthly_recurring_revenue", "sum"),
            avg_mrr=("monthly_recurring_revenue", "mean"),
            avg_health=("product_health_score", "mean"),
            avg_usage=("usage_frequency", "mean"),
            avg_adoption=("feature_adoption_rate", "mean"),
            avg_days_since_login=("days_since_last_login", "mean"),
            avg_support_tickets=("support_tickets", "mean"),
            avg_renewal_probability=("renewal_probability", "mean"),
            total_revenue_at_risk=("revenue_at_risk", "sum"),
        )
        .reset_index()
    )

    cohort_table = cohort_activity.merge(
        cohort_base,
        on="cohort_month",
        how="left",
    )

    cohort_table["retention_rate"] = (
        cohort_table["active_accounts"] / cohort_table["starting_accounts"]
    ).round(4)

    cohort_table["cohort_churn_rate"] = (
        cohort_table["churned_accounts"] / cohort_table["active_accounts"]
    ).round(4)

    cohort_table["mrr_per_starting_account"] = (
        cohort_table["total_mrr"] / cohort_table["starting_accounts"]
    ).round(2)

    cohort_table["revenue_at_risk_per_starting_account"] = (
        cohort_table["total_revenue_at_risk"] / cohort_table["starting_accounts"]
    ).round(2)

    return cohort_table.sort_values(["cohort_month", "cohort_age_months"])


def build_cohort_summary(cohort_table: pd.DataFrame) -> pd.DataFrame:
    summary_rows = []

    for cohort_month, group in cohort_table.groupby("cohort_month"):
        group = group.sort_values("cohort_age_months")

        starting_accounts = group["starting_accounts"].iloc[0]
        max_age = group["cohort_age_months"].max()

        month_3 = group.loc[group["cohort_age_months"] == 3, "retention_rate"]
        month_6 = group.loc[group["cohort_age_months"] == 6, "retention_rate"]
        month_12 = group.loc[group["cohort_age_months"] == 12, "retention_rate"]

        latest = group.iloc[-1]

        summary_rows.append({
            "cohort_month": cohort_month,
            "starting_accounts": starting_accounts,
            "max_observed_age_months": max_age,
            "retention_month_3": month_3.iloc[0] if not month_3.empty else pd.NA,
            "retention_month_6": month_6.iloc[0] if not month_6.empty else pd.NA,
            "retention_month_12": month_12.iloc[0] if not month_12.empty else pd.NA,
            "latest_retention_rate": latest["retention_rate"],
            "latest_total_mrr": latest["total_mrr"],
            "latest_avg_health": latest["avg_health"],
            "latest_avg_usage": latest["avg_usage"],
            "latest_revenue_at_risk": latest["total_revenue_at_risk"],
        })

    summary = pd.DataFrame(summary_rows)

    summary["retention_drop_to_latest"] = (
        1 - summary["latest_retention_rate"]
    ).round(4)

    return summary.sort_values("cohort_month")


def main() -> None:
    config = load_config(CONFIG_PATH)
    ensure_output_dirs(config)

    df = load_data(config)

    cohort_table = build_cohort_retention_table(df)
    cohort_summary = build_cohort_summary(cohort_table)

    cohort_table_path = Path(config["outputs"]["cohorts"]["retention_table"])
    cohort_summary_path = Path(config["outputs"]["cohorts"]["cohort_summary"])

    cohort_table.to_csv(cohort_table_path, index=False)
    cohort_summary.to_csv(cohort_summary_path, index=False)

    print("Cohort analysis complete.")
    print(f"Saved retention table: {cohort_table_path}")
    print(f"Saved cohort summary: {cohort_summary_path}")
    print(f"Cohorts analyzed: {cohort_table['cohort_month'].nunique()}")
    print(f"Rows written: {len(cohort_table)}")


if __name__ == "__main__":
    main()