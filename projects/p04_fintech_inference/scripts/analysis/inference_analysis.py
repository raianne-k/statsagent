from pathlib import Path
from math import sqrt

import pandas as pd


DATA_PATH = Path(
    "projects/p04_fintech_inference/data/cleaned/fintech_repayment_inference_cleaned.csv"
)

OUTPUT_DIR = Path(
    "projects/p04_fintech_inference/outputs/inference"
)


def proportion_confidence_interval(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    """Approximate 95% confidence interval for a proportion."""

    if total == 0:
        return (0.0, 0.0)

    p = successes / total
    margin = z * sqrt((p * (1 - p)) / total)

    lower = max(0, p - margin)
    upper = min(1, p + margin)

    return lower, upper


def summarize_binary_condition(
    df: pd.DataFrame,
    condition_col: str,
    outcome_col: str,
) -> pd.DataFrame:
    """Calculate outcome probability by binary condition with confidence intervals."""

    rows = []

    for value, group in df.groupby(condition_col, dropna=False):
        total = len(group)
        successes = int(group[outcome_col].sum())

        rate = successes / total if total else 0
        ci_low, ci_high = proportion_confidence_interval(successes, total)

        rows.append({
            "condition": condition_col,
            "condition_value": value,
            "outcome": outcome_col,
            "n": total,
            "successes": successes,
            "rate_percent": round(rate * 100, 2),
            "ci_low_percent": round(ci_low * 100, 2),
            "ci_high_percent": round(ci_high * 100, 2),
            "ci_width_percent": round((ci_high - ci_low) * 100, 2),
        })

    return pd.DataFrame(rows)


def compare_two_groups(
    df: pd.DataFrame,
    group_col: str,
    outcome_col: str,
) -> pd.DataFrame:
    """Compare outcome rates across groups with confidence intervals."""

    rows = []

    for value, group in df.groupby(group_col, dropna=False):
        total = len(group)
        successes = int(group[outcome_col].sum())

        rate = successes / total if total else 0
        ci_low, ci_high = proportion_confidence_interval(successes, total)

        rows.append({
            "group": group_col,
            "group_value": value,
            "outcome": outcome_col,
            "n": total,
            "successes": successes,
            "rate_percent": round(rate * 100, 2),
            "ci_low_percent": round(ci_low * 100, 2),
            "ci_high_percent": round(ci_high * 100, 2),
            "ci_width_percent": round((ci_high - ci_low) * 100, 2),
        })

    result = pd.DataFrame(rows)

    return result.sort_values("rate_percent", ascending=False)


def bayesian_risk_update(
    df: pd.DataFrame,
    evidence_col: str,
    outcome_col: str,
) -> pd.DataFrame:
    """
    Simple Bayesian-style update:
    prior = overall outcome probability
    posterior = outcome probability after observing evidence = 1
    """

    prior = df[outcome_col].mean()

    evidence_group = df[df[evidence_col] == 1]
    no_evidence_group = df[df[evidence_col] == 0]

    posterior_evidence = evidence_group[outcome_col].mean()
    posterior_no_evidence = no_evidence_group[outcome_col].mean()

    return pd.DataFrame([
        {
            "evidence": evidence_col,
            "outcome": outcome_col,
            "group": "overall_prior",
            "n": len(df),
            "probability_percent": round(prior * 100, 2),
        },
        {
            "evidence": evidence_col,
            "outcome": outcome_col,
            "group": "evidence_present",
            "n": len(evidence_group),
            "probability_percent": round(posterior_evidence * 100, 2),
        },
        {
            "evidence": evidence_col,
            "outcome": outcome_col,
            "group": "evidence_absent",
            "n": len(no_evidence_group),
            "probability_percent": round(posterior_no_evidence * 100, 2),
        },
    ])


def summarize_risk_difference(
    df: pd.DataFrame,
    group_col: str,
    outcome_col: str,
) -> pd.DataFrame:
    """Calculate simple rate differences between lowest and highest observed group rates."""

    group_summary = compare_two_groups(df, group_col, outcome_col)

    highest = group_summary.iloc[0]
    lowest = group_summary.iloc[-1]

    rate_difference = highest["rate_percent"] - lowest["rate_percent"]

    return pd.DataFrame([{
        "group": group_col,
        "outcome": outcome_col,
        "highest_group": highest["group_value"],
        "highest_rate_percent": highest["rate_percent"],
        "highest_n": highest["n"],
        "lowest_group": lowest["group_value"],
        "lowest_rate_percent": lowest["rate_percent"],
        "lowest_n": lowest["n"],
        "rate_difference_percent": round(rate_difference, 2),
        "interpretation_note": "Rate difference is observational only and does not imply causality.",
    }])


def save_table(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def main():
    df = pd.read_csv(DATA_PATH)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Conditional probability:
    # P(current delinquency | missed payment in last 30 days)
    missed_payment_condition = summarize_binary_condition(
        df=df,
        condition_col="missed_payment_last_30d",
        outcome_col="current_delinquency_flag",
    )

    save_table(
        missed_payment_condition,
        OUTPUT_DIR / "conditional_probability_missed_payment.csv",
    )

    # 2. Conditional probability:
    # P(current delinquency | prior delinquency)
    prior_delinquency_condition = summarize_binary_condition(
        df=df,
        condition_col="prior_delinquency_flag",
        outcome_col="current_delinquency_flag",
    )

    save_table(
        prior_delinquency_condition,
        OUTPUT_DIR / "conditional_probability_prior_delinquency.csv",
    )

    # 3. Risk-tier uncertainty
    risk_tier_ci = compare_two_groups(
        df=df,
        group_col="risk_tier",
        outcome_col="current_delinquency_flag",
    )

    save_table(
        risk_tier_ci,
        OUTPUT_DIR / "risk_tier_delinquency_confidence_intervals.csv",
    )

    # 4. Intervention-group comparison
    intervention_ci = compare_two_groups(
        df=df,
        group_col="intervention_group",
        outcome_col="payment_recovery_flag",
    )

    save_table(
        intervention_ci,
        OUTPUT_DIR / "intervention_recovery_confidence_intervals.csv",
    )

    # 5. Bayesian-style risk update: missed payment evidence
    missed_payment_update = bayesian_risk_update(
        df=df,
        evidence_col="missed_payment_last_30d",
        outcome_col="current_delinquency_flag",
    )

    save_table(
        missed_payment_update,
        OUTPUT_DIR / "bayesian_update_missed_payment.csv",
    )

    # 6. Bayesian-style risk update: prior delinquency evidence
    prior_delinquency_update = bayesian_risk_update(
        df=df,
        evidence_col="prior_delinquency_flag",
        outcome_col="current_delinquency_flag",
    )

    save_table(
        prior_delinquency_update,
        OUTPUT_DIR / "bayesian_update_prior_delinquency.csv",
    )

    # 7. Summary risk differences
    risk_difference = summarize_risk_difference(
        df=df,
        group_col="risk_tier",
        outcome_col="current_delinquency_flag",
    )

    save_table(
        risk_difference,
        OUTPUT_DIR / "risk_tier_rate_difference_summary.csv",
    )

    intervention_difference = summarize_risk_difference(
        df=df,
        group_col="intervention_group",
        outcome_col="payment_recovery_flag",
    )

    save_table(
        intervention_difference,
        OUTPUT_DIR / "intervention_recovery_rate_difference_summary.csv",
    )

    print("Saved conditional probability outputs")
    print("Saved confidence interval outputs")
    print("Saved Bayesian-style update outputs")
    print("Saved risk difference summaries")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()