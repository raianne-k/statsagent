from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


DATA_PATH = Path(
    "projects/p06_product_experimentation/data/cleaned/saas_experimentation_cleaned.csv"
)

OUTPUT_DIR = Path(
    "projects/p06_product_experimentation/outputs/experimentation"
)

GROUP_COLUMN = "experiment_group"
CONTROL_GROUP = "control"
TREATMENT_GROUP = "treatment"

BINARY_OUTCOME_METRICS = [
    "onboarding_completion_flag",
    "activation_flag",
    "retained_30d",
    "retained_60d",
    "churn_30d",
    "upgrade_flag",
    "expansion_revenue_flag",
    "negative_feedback_flag",
]

CONTINUOUS_OUTCOME_METRICS = [
    "sessions_first_14d",
    "feature_adoption_count",
    "support_tickets_first_30d",
    "time_to_activation_days",
    "monthly_subscription_value",
]


def save_table(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def proportion_confidence_interval(
    successes: int,
    n: int,
    confidence_level: float = 0.95,
) -> tuple[float, float]:
    if n == 0:
        return np.nan, np.nan

    p_hat = successes / n
    z = stats.norm.ppf(1 - (1 - confidence_level) / 2)
    se = np.sqrt((p_hat * (1 - p_hat)) / n)

    lower = max(0, p_hat - z * se)
    upper = min(1, p_hat + z * se)

    return lower, upper


def difference_in_proportions_test(
    control_successes: int,
    control_n: int,
    treatment_successes: int,
    treatment_n: int,
) -> float:
    if control_n == 0 or treatment_n == 0:
        return np.nan

    control_rate = control_successes / control_n
    treatment_rate = treatment_successes / treatment_n

    pooled_rate = (control_successes + treatment_successes) / (
        control_n + treatment_n
    )

    se = np.sqrt(
        pooled_rate
        * (1 - pooled_rate)
        * ((1 / control_n) + (1 / treatment_n))
    )

    if se == 0:
        return np.nan

    z_score = (treatment_rate - control_rate) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))

    return p_value


def analyze_binary_metrics(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for metric in BINARY_OUTCOME_METRICS:
        control = df[df[GROUP_COLUMN] == CONTROL_GROUP][metric].dropna()
        treatment = df[df[GROUP_COLUMN] == TREATMENT_GROUP][metric].dropna()

        control_n = len(control)
        treatment_n = len(treatment)

        control_successes = int(control.sum()) if control_n > 0 else 0
        treatment_successes = int(treatment.sum()) if treatment_n > 0 else 0

        control_rate = control_successes / control_n if control_n > 0 else np.nan
        treatment_rate = (
            treatment_successes / treatment_n if treatment_n > 0 else np.nan
        )

        absolute_lift = treatment_rate - control_rate
        relative_lift = absolute_lift / control_rate if control_rate not in [0, np.nan] else np.nan

        control_ci_low, control_ci_high = proportion_confidence_interval(
            control_successes,
            control_n,
        )

        treatment_ci_low, treatment_ci_high = proportion_confidence_interval(
            treatment_successes,
            treatment_n,
        )

        p_value = difference_in_proportions_test(
            control_successes,
            control_n,
            treatment_successes,
            treatment_n,
        )

        rows.append(
            {
                "metric": metric,
                "control_n": control_n,
                "treatment_n": treatment_n,
                "control_rate_percent": round(control_rate * 100, 2),
                "treatment_rate_percent": round(treatment_rate * 100, 2),
                "absolute_lift_percentage_points": round(absolute_lift * 100, 2),
                "relative_lift_percent": round(relative_lift * 100, 2)
                if pd.notna(relative_lift)
                else np.nan,
                "control_ci_low_percent": round(control_ci_low * 100, 2),
                "control_ci_high_percent": round(control_ci_high * 100, 2),
                "treatment_ci_low_percent": round(treatment_ci_low * 100, 2),
                "treatment_ci_high_percent": round(treatment_ci_high * 100, 2),
                "p_value": round(p_value, 4) if pd.notna(p_value) else np.nan,
                "statistically_significant_05": bool(p_value < 0.05)
                if pd.notna(p_value)
                else False,
            }
        )

    return pd.DataFrame(rows)


def analyze_continuous_metrics(df: pd.DataFrame) -> pd.DataFrame:
    rows = []

    for metric in CONTINUOUS_OUTCOME_METRICS:
        control = df[df[GROUP_COLUMN] == CONTROL_GROUP][metric].dropna()
        treatment = df[df[GROUP_COLUMN] == TREATMENT_GROUP][metric].dropna()

        control_mean = control.mean()
        treatment_mean = treatment.mean()

        control_median = control.median()
        treatment_median = treatment.median()

        absolute_difference = treatment_mean - control_mean
        relative_difference = (
            absolute_difference / control_mean
            if pd.notna(control_mean) and control_mean != 0
            else np.nan
        )

        if len(control) > 1 and len(treatment) > 1:
            _, p_value = stats.ttest_ind(
                treatment,
                control,
                equal_var=False,
                nan_policy="omit",
            )
        else:
            p_value = np.nan

        rows.append(
            {
                "metric": metric,
                "control_n": len(control),
                "treatment_n": len(treatment),
                "control_mean": round(control_mean, 3),
                "treatment_mean": round(treatment_mean, 3),
                "mean_difference": round(absolute_difference, 3),
                "relative_difference_percent": round(relative_difference * 100, 2)
                if pd.notna(relative_difference)
                else np.nan,
                "control_median": round(control_median, 3),
                "treatment_median": round(treatment_median, 3),
                "p_value": round(p_value, 4) if pd.notna(p_value) else np.nan,
                "statistically_significant_05": bool(p_value < 0.05)
                if pd.notna(p_value)
                else False,
            }
        )

    return pd.DataFrame(rows)


def experiment_integrity_review(df: pd.DataFrame) -> pd.DataFrame:
    group_counts = df[GROUP_COLUMN].value_counts(dropna=False)

    control_count = int(group_counts.get(CONTROL_GROUP, 0))
    treatment_count = int(group_counts.get(TREATMENT_GROUP, 0))
    total_count = control_count + treatment_count

    imbalance_percent = (
        abs(control_count - treatment_count) / total_count * 100
        if total_count > 0
        else np.nan
    )

    duplicate_user_ids = int(df["user_id"].duplicated().sum())
    null_experiment_groups = int(df[GROUP_COLUMN].isna().sum())

    assignment_valid_rate = df["assignment_valid_flag"].mean() * 100
    eligibility_rate = df["experiment_eligibility_flag"].mean() * 100
    low_exposure_rate = df["low_exposure_flag"].mean() * 100

    control_exposure_mean = df[df[GROUP_COLUMN] == CONTROL_GROUP]["exposure_days"].mean()
    treatment_exposure_mean = df[df[GROUP_COLUMN] == TREATMENT_GROUP]["exposure_days"].mean()

    exposure_gap = abs(treatment_exposure_mean - control_exposure_mean)

    rows = [
        {
            "check": "control_group_count",
            "status": "info",
            "value": control_count,
            "note": "Number of users assigned to control.",
        },
        {
            "check": "treatment_group_count",
            "status": "info",
            "value": treatment_count,
            "note": "Number of users assigned to treatment.",
        },
        {
            "check": "group_imbalance_percent",
            "status": "pass" if imbalance_percent <= 10 else "review",
            "value": round(imbalance_percent, 2),
            "note": "Absolute imbalance between control and treatment as percent of assigned population.",
        },
        {
            "check": "duplicate_user_ids",
            "status": "pass" if duplicate_user_ids == 0 else "fail",
            "value": duplicate_user_ids,
            "note": "Duplicate user IDs should be zero for user-level experiment analysis.",
        },
        {
            "check": "null_experiment_groups",
            "status": "pass" if null_experiment_groups == 0 else "fail",
            "value": null_experiment_groups,
            "note": "Users should have non-null experiment assignment.",
        },
        {
            "check": "assignment_valid_rate_percent",
            "status": "pass" if assignment_valid_rate >= 95 else "review",
            "value": round(assignment_valid_rate, 2),
            "note": "Share of users with valid experiment assignment.",
        },
        {
            "check": "experiment_eligibility_rate_percent",
            "status": "pass" if eligibility_rate >= 90 else "review",
            "value": round(eligibility_rate, 2),
            "note": "Share of users eligible for the experiment.",
        },
        {
            "check": "low_exposure_rate_percent",
            "status": "pass" if low_exposure_rate <= 10 else "review",
            "value": round(low_exposure_rate, 2),
            "note": "Share of users with less than full exposure window.",
        },
        {
            "check": "exposure_gap_days",
            "status": "pass" if exposure_gap <= 3 else "review",
            "value": round(exposure_gap, 2),
            "note": "Absolute difference in average exposure days between treatment and control.",
        },
    ]

    return pd.DataFrame(rows)


def balance_check(df: pd.DataFrame) -> pd.DataFrame:
    categorical_columns = [
        "acquisition_channel",
        "region",
        "company_size",
        "industry",
    ]

    rows = []

    for column in categorical_columns:
        counts = (
            df.groupby([GROUP_COLUMN, column], dropna=False)
            .size()
            .reset_index(name="count")
        )

        group_totals = (
            df.groupby(GROUP_COLUMN)
            .size()
            .reset_index(name="group_total")
        )

        merged = counts.merge(
            group_totals,
            on=GROUP_COLUMN,
            how="left",
        )

        merged["percent"] = (
            merged["count"] / merged["group_total"] * 100
        )

        pivot = merged.pivot_table(
            index=column,
            columns=GROUP_COLUMN,
            values="percent",
            aggfunc="sum",
        ).reset_index()

        if CONTROL_GROUP not in pivot.columns:
            pivot[CONTROL_GROUP] = np.nan

        if TREATMENT_GROUP not in pivot.columns:
            pivot[TREATMENT_GROUP] = np.nan

        pivot["absolute_difference_percentage_points"] = (
            pivot[TREATMENT_GROUP] - pivot[CONTROL_GROUP]
        ).abs()

        pivot["balance_variable"] = column

        rows.append(pivot)

    balance = pd.concat(rows, ignore_index=True)

    balance = balance.rename(
        columns={
            CONTROL_GROUP: "control_percent",
            TREATMENT_GROUP: "treatment_percent",
        }
    )

    numeric_cols = balance.select_dtypes(include="number").columns
    balance[numeric_cols] = balance[numeric_cols].round(2)

    return balance

def main():
    df = pd.read_csv(DATA_PATH)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    integrity = experiment_integrity_review(df)
    binary_results = analyze_binary_metrics(df)
    continuous_results = analyze_continuous_metrics(df)
    balance_results = balance_check(df)

    save_table(
        integrity,
        OUTPUT_DIR / "experiment_integrity_review.csv",
    )

    save_table(
        binary_results,
        OUTPUT_DIR / "binary_metric_experiment_results.csv",
    )

    save_table(
        continuous_results,
        OUTPUT_DIR / "continuous_metric_experiment_results.csv",
    )

    save_table(
        balance_results,
        OUTPUT_DIR / "randomization_balance_check.csv",
    )

    print("Saved experiment integrity review")
    print("Saved binary metric experiment results")
    print("Saved continuous metric experiment results")
    print("Saved randomization balance check")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()