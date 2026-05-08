from pathlib import Path

import pandas as pd


DATA_PATH = Path(
    "projects/p03_saas_relationships/data/cleaned/saas_account_cleaned.csv"
)

OUTPUT_DIR = Path(
    "projects/p03_saas_relationships/outputs/relationships"
)


CORRELATION_COLUMNS = [
    "monthly_recurring_revenue",
    "seat_count",
    "seats_used_percent",
    "weekly_active_users",
    "feature_adoption_rate",
    "avg_session_minutes",
    "admin_logins_last_30d",
    "onboarding_completion_percent",
    "days_since_last_login",
    "support_tickets_last_90d",
    "nps_score",
    "account_health_score",
    "renewal_probability",
    "expansion_revenue",
]


TARGET_COLUMNS = [
    "account_health_score",
    "renewal_probability",
    "churn_flag",
]


def save_table(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def compute_correlations(df: pd.DataFrame, method: str) -> pd.DataFrame:
    """Compute correlation matrix for numeric relationship analysis."""

    available_columns = [
        col for col in CORRELATION_COLUMNS
        if col in df.columns
    ]

    corr = df[available_columns].corr(method=method)

    return corr.reset_index().rename(columns={"index": "variable"})


def compute_target_relationships(df: pd.DataFrame, method: str) -> pd.DataFrame:
    """Rank relationships between candidate variables and target metrics."""

    available_columns = [
        col for col in CORRELATION_COLUMNS + TARGET_COLUMNS
        if col in df.columns
    ]

    rows = []

    for target in TARGET_COLUMNS:
        if target not in df.columns:
            continue

        for col in available_columns:
            if col == target:
                continue

            valid = df[[col, target]].dropna()

            if len(valid) < 30:
                continue

            corr_value = valid[col].corr(valid[target], method=method)

            rows.append({
                "target": target,
                "variable": col,
                "method": method,
                "correlation": round(corr_value, 3),
                "abs_correlation": round(abs(corr_value), 3),
                "n": len(valid),
            })

    result = pd.DataFrame(rows)

    if result.empty:
        return result

    return result.sort_values(
        ["target", "abs_correlation"],
        ascending=[True, False],
    )


def compute_churn_group_comparison(df: pd.DataFrame) -> pd.DataFrame:
    """Compare key metrics between churned and non-churned accounts."""

    grouped = df.groupby("churn_flag", dropna=False)

    summary = grouped.agg(
        account_count=("account_id", "count"),
        median_account_health_score=("account_health_score", "median"),
        median_renewal_probability=("renewal_probability", "median"),
        median_feature_adoption_rate=("feature_adoption_rate", "median"),
        median_onboarding_completion_percent=("onboarding_completion_percent", "median"),
        median_days_since_last_login=("days_since_last_login", "median"),
        median_support_tickets_last_90d=("support_tickets_last_90d", "median"),
        median_monthly_recurring_revenue=("monthly_recurring_revenue", "median"),
        median_expansion_revenue=("expansion_revenue", "median"),
    ).reset_index()

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(2)

    return summary


def main():
    df = pd.read_csv(DATA_PATH)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pearson_corr = compute_correlations(df, method="pearson")
    spearman_corr = compute_correlations(df, method="spearman")

    save_table(
        pearson_corr,
        OUTPUT_DIR / "pearson_correlation_matrix.csv",
    )

    save_table(
        spearman_corr,
        OUTPUT_DIR / "spearman_correlation_matrix.csv",
    )

    pearson_targets = compute_target_relationships(df, method="pearson")
    spearman_targets = compute_target_relationships(df, method="spearman")

    save_table(
        pearson_targets,
        OUTPUT_DIR / "pearson_target_relationships.csv",
    )

    save_table(
        spearman_targets,
        OUTPUT_DIR / "spearman_target_relationships.csv",
    )

    churn_comparison = compute_churn_group_comparison(df)

    save_table(
        churn_comparison,
        OUTPUT_DIR / "churn_group_comparison.csv",
    )

    print("Saved Pearson correlation matrix")
    print("Saved Spearman correlation matrix")
    print("Saved target relationship rankings")
    print("Saved churn group comparison")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()