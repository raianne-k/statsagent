"""
Revenue-risk concentration analysis for P07.

Purpose:
- identify which customer segments contribute disproportionate revenue risk
- compare risk share against MRR share and account share
- support executive prioritization and findings narrative

Important:
This analysis ranks exposure concentration.
It does not prove causal drivers of churn or revenue loss.
"""

from pathlib import Path

import pandas as pd


DATA_PATH = Path(
    "projects/p07_saas_strategic_forecasting/data/cleaned/saas_account_monthly_cleaned.csv"
)

RAW_FALLBACK_PATH = Path(
    "projects/p07_saas_strategic_forecasting/data/raw/saas_account_monthly_forecasting.csv"
)

OUTPUT_PATH = Path(
    "projects/p07_saas_strategic_forecasting/outputs/segmentation/revenue_risk_concentration.csv"
)


def load_data() -> pd.DataFrame:
    path = DATA_PATH if DATA_PATH.exists() else RAW_FALLBACK_PATH

    df = pd.read_csv(path)

    df["snapshot_month"] = pd.to_datetime(df["snapshot_month"])

    return df


def get_latest_snapshot(df: pd.DataFrame) -> pd.DataFrame:
    latest_month = df["snapshot_month"].max()
    return df[df["snapshot_month"] == latest_month].copy()


def build_revenue_risk_concentration(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby(["health_band", "mrr_band"], dropna=False)
        .agg(
            account_count=("account_id", "nunique"),
            total_mrr=("monthly_recurring_revenue", "sum"),
            total_revenue_at_risk=("revenue_at_risk", "sum"),
            avg_product_health_score=("product_health_score", "mean"),
            avg_renewal_probability=("renewal_probability", "mean"),
            avg_feature_adoption_rate=("feature_adoption_rate", "mean"),
            avg_usage_frequency=("usage_frequency", "mean"),
            avg_days_since_last_login=("days_since_last_login", "mean"),
            avg_support_tickets=("support_tickets", "mean"),
            churn_rate=("churn_flag", "mean"),
        )
        .reset_index()
    )

    total_accounts = grouped["account_count"].sum()
    total_mrr = grouped["total_mrr"].sum()
    total_risk = grouped["total_revenue_at_risk"].sum()

    grouped["share_total_accounts_pct"] = (
        grouped["account_count"] / total_accounts * 100
    )

    grouped["share_total_mrr_pct"] = (
        grouped["total_mrr"] / total_mrr * 100
    )

    grouped["share_total_risk_pct"] = (
        grouped["total_revenue_at_risk"] / total_risk * 100
    )

    grouped["risk_concentration_ratio"] = (
        grouped["share_total_risk_pct"] / grouped["share_total_mrr_pct"]
    )

    grouped["risk_minus_mrr_share_pct"] = (
        grouped["share_total_risk_pct"] - grouped["share_total_mrr_pct"]
    )

    grouped["revenue_at_risk_rate"] = (
        grouped["total_revenue_at_risk"] / grouped["total_mrr"]
    )

    grouped["priority_label"] = grouped["risk_concentration_ratio"].apply(
        classify_priority
    )

    numeric_cols = grouped.select_dtypes(include="number").columns
    grouped[numeric_cols] = grouped[numeric_cols].round(4)

    return grouped.sort_values(
        ["total_revenue_at_risk", "risk_concentration_ratio"],
        ascending=[False, False],
    )


def classify_priority(value: float) -> str:
    if value >= 1.5:
        return "overrepresented_risk"
    if value >= 1.0:
        return "proportional_or_slightly_elevated_risk"
    return "underrepresented_risk"


def main() -> None:
    df = load_data()
    latest = get_latest_snapshot(df)

    concentration = build_revenue_risk_concentration(latest)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    concentration.to_csv(OUTPUT_PATH, index=False)

    print("Revenue-risk concentration analysis complete.")
    print(f"Saved: {OUTPUT_PATH}")
    print(f"Segments analyzed: {len(concentration)}")


if __name__ == "__main__":
    main()