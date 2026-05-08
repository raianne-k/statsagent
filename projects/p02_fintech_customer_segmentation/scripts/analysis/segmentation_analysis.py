from pathlib import Path

import pandas as pd


DATA_PATH = Path(
    "projects/p02_fintech_customer_segmentation/data/cleaned/fintech_customer_cleaned.csv"
)

OUTPUT_DIR = Path(
    "projects/p02_fintech_customer_segmentation/outputs/segmentation"
)


SEGMENT_COLUMNS = [
    "risk_band",
    "engagement_band",
    "tenure_cohort",
]


def add_tenure_cohort(df: pd.DataFrame) -> pd.DataFrame:
    """Create simple tenure cohorts for lightweight cohort comparison."""

    df = df.copy()

    df["tenure_cohort"] = pd.cut(
        df["customer_tenure_months"],
        bins=[-1, 3, 12, 24, float("inf")],
        labels=[
            "new_0_3m",
            "early_4_12m",
            "established_13_24m",
            "mature_25m_plus",
        ],
    )

    return df


def summarize_by_segment(df: pd.DataFrame, segment_col: str) -> pd.DataFrame:
    """Create segment-level comparison table for one grouping variable."""

    grouped = df.groupby(segment_col, dropna=False)

    summary = grouped.agg(
        customer_count=("customer_id", "count"),
        delinquency_rate_percent=("delinquency_flag", lambda x: round(x.mean() * 100, 2)),
        autopay_rate_percent=("autopay_enabled", lambda x: round(x.mean() * 100, 2)),

        median_active_loan_amount=("active_loan_amount", "median"),
        mean_active_loan_amount=("active_loan_amount", "mean"),

        median_loan_to_income_ratio=("loan_to_income_ratio", "median"),
        mean_loan_to_income_ratio=("loan_to_income_ratio", "mean"),

        median_savings_balance=("savings_balance", "median"),
        mean_savings_balance=("savings_balance", "mean"),

        median_installment_size=("installment_size", "median"),
        mean_installment_size=("installment_size", "mean"),

        median_repayment_rate_percent=("repayment_rate_percent", "median"),
        mean_repayment_rate_percent=("repayment_rate_percent", "mean"),

        median_avg_days_late=("avg_days_late", "median"),
        mean_avg_days_late=("avg_days_late", "mean"),

        median_missed_payments=("missed_payments_last_12m", "median"),
        mean_missed_payments=("missed_payments_last_12m", "mean"),

        median_app_sessions_per_week=("app_sessions_per_week", "median"),
        mean_app_sessions_per_week=("app_sessions_per_week", "mean"),

        median_days_since_last_login=("days_since_last_login", "median"),
        mean_days_since_last_login=("days_since_last_login", "mean"),

        median_number_of_products=("number_of_products", "median"),
        mean_number_of_products=("number_of_products", "mean"),
    ).reset_index()

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(2)

    return summary


def summarize_cross_segment(
    df: pd.DataFrame,
    segment_cols: list[str],
) -> pd.DataFrame:
    """Create comparison table across two segmentation dimensions."""

    grouped = df.groupby(segment_cols, dropna=False)

    summary = grouped.agg(
        customer_count=("customer_id", "count"),
        delinquency_rate_percent=("delinquency_flag", lambda x: round(x.mean() * 100, 2)),
        autopay_rate_percent=("autopay_enabled", lambda x: round(x.mean() * 100, 2)),

        median_loan_to_income_ratio=("loan_to_income_ratio", "median"),
        median_savings_balance=("savings_balance", "median"),
        median_active_loan_amount=("active_loan_amount", "median"),
        median_repayment_rate_percent=("repayment_rate_percent", "median"),
        median_avg_days_late=("avg_days_late", "median"),
        median_missed_payments=("missed_payments_last_12m", "median"),
        median_app_sessions_per_week=("app_sessions_per_week", "median"),
        median_number_of_products=("number_of_products", "median"),
    ).reset_index()

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(2)

    return summary


def summarize_operational_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """Create operational KPI table across risk and tenure cohorts."""

    grouped = df.groupby(
        ["risk_band", "tenure_cohort"],
        dropna=False,
    )

    summary = grouped.agg(
        customer_count=("customer_id", "count"),
        delinquency_rate_percent=("delinquency_flag", lambda x: round(x.mean() * 100, 2)),
        autopay_rate_percent=("autopay_enabled", lambda x: round(x.mean() * 100, 2)),
        median_repayment_rate_percent=("repayment_rate_percent", "median"),
        median_loan_to_income_ratio=("loan_to_income_ratio", "median"),
        median_savings_balance=("savings_balance", "median"),
        median_missed_payments=("missed_payments_last_12m", "median"),
        median_avg_days_late=("avg_days_late", "median"),
        median_products=("number_of_products", "median"),
    ).reset_index()

    numeric_cols = summary.select_dtypes(include="number").columns
    summary[numeric_cols] = summary[numeric_cols].round(2)

    return summary


def save_table(df: pd.DataFrame, output_path: Path) -> None:
    """Save one comparison table."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def main():
    df = pd.read_csv(DATA_PATH)

    df = add_tenure_cohort(df)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for segment_col in SEGMENT_COLUMNS:
        summary = summarize_by_segment(df, segment_col)

        save_table(
            summary,
            OUTPUT_DIR / f"{segment_col}_comparison.csv",
        )

        print(f"Saved {segment_col} comparison")

    risk_by_engagement = summarize_cross_segment(
        df,
        ["risk_band", "engagement_band"],
    )

    save_table(
        risk_by_engagement,
        OUTPUT_DIR / "risk_by_engagement_comparison.csv",
    )

    print("Saved risk by engagement comparison")

    risk_by_tenure = summarize_operational_kpis(df)

    save_table(
        risk_by_tenure,
        OUTPUT_DIR / "risk_by_tenure_operational_kpis.csv",
    )

    print("Saved risk by tenure operational KPIs")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()