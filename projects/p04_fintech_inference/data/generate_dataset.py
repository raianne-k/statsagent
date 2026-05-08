from pathlib import Path

import numpy as np
import pandas as pd

np.random.seed(42)

N = 7000

OUTPUT_PATH = Path(
    "projects/p04_fintech_inference/data/raw/fintech_repayment_inference_sample.csv"
)
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


regions = ["Tallinn", "Tartu", "Narva", "Pärnu", "Other"]
income_bands = ["low", "lower_mid", "mid", "upper_mid", "high"]
employment_types = ["salaried", "self_employed", "gig_worker", "student", "unemployed"]
repayment_plan_types = ["standard", "restructured", "grace_period"]


# -------------------------
# Base customer structure
# -------------------------

df = pd.DataFrame({
    "customer_id": range(1, N + 1),

    "region": np.random.choice(
        regions,
        size=N,
        p=[0.42, 0.22, 0.12, 0.10, 0.14],
    ),

    "income_band": np.random.choice(
        income_bands,
        size=N,
        p=[0.18, 0.32, 0.34, 0.13, 0.03],
    ),

    "employment_type": np.random.choice(
        employment_types,
        size=N,
        p=[0.58, 0.16, 0.11, 0.08, 0.07],
    ),
})


# -------------------------
# Financial profile
# -------------------------

income_base = {
    "low": 950,
    "lower_mid": 1400,
    "mid": 2100,
    "upper_mid": 3300,
    "high": 5200,
}

df["monthly_income"] = [
    np.random.lognormal(mean=np.log(income_base[band]), sigma=0.32)
    for band in df["income_band"]
]

df["monthly_income"] = df["monthly_income"].round(2).clip(400, 9500)

df["loan_balance"] = np.random.lognormal(
    mean=8.35,
    sigma=0.75,
    size=N,
).round(2)

df["loan_balance"] = df["loan_balance"].clip(300, 45000)

loan_terms = np.random.choice(
    [6, 12, 18, 24, 36],
    size=N,
    p=[0.10, 0.35, 0.25, 0.20, 0.10],
)

df["monthly_payment"] = (df["loan_balance"] / loan_terms).round(2)

df["loan_to_income_ratio"] = (
    df["loan_balance"] / df["monthly_income"]
).round(2)

df["credit_utilization_percent"] = (
    np.random.beta(a=2.4, b=3.2, size=N) * 100
).round(2)


# -------------------------
# Risk score with realistic spread
# -------------------------

raw_risk = (
    0.34 * np.log1p(df["loan_to_income_ratio"])
    + 0.30 * (df["credit_utilization_percent"] / 100)
    + 0.18 * (df["income_band"].map({
        "low": 1.00,
        "lower_mid": 0.70,
        "mid": 0.45,
        "upper_mid": 0.25,
        "high": 0.10,
    }).astype(float))
    + np.random.normal(0, 0.13, N)
)

risk_score = (
    (raw_risk - raw_risk.min())
    / (raw_risk.max() - raw_risk.min())
)

df["risk_score"] = risk_score.round(3)

df["risk_tier"] = pd.cut(
    df["risk_score"],
    bins=[-0.01, 0.45, 0.68, 1.0],
    labels=["low_risk", "medium_risk", "high_risk"],
)


# -------------------------
# Repayment behavior
# -------------------------

missed_6m_lambda = (
    0.35
    + df["risk_score"] * 2.8
)

df["missed_payments_last_6m"] = np.random.poisson(
    lam=missed_6m_lambda,
    size=N,
).clip(0, 8)

df["days_late_average"] = np.random.gamma(
    shape=1.4 + df["risk_score"] * 2.2,
    scale=2.4,
    size=N,
).round(1)

df["days_late_average"] = df["days_late_average"].clip(0, 45)


# -------------------------
# Binary repayment indicators
# -------------------------

df["missed_payment_last_30d"] = np.random.binomial(
    1,
    np.clip(0.05 + df["risk_score"] * 0.30, 0.03, 0.42),
)

df["prior_delinquency_flag"] = np.random.binomial(
    1,
    np.clip(0.04 + df["risk_score"] * 0.28, 0.02, 0.38),
)

df["current_delinquency_flag"] = np.random.binomial(
    1,
    np.clip(
        0.03
        + df["risk_score"] * 0.22
        + df["missed_payment_last_30d"] * 0.12
        + df["prior_delinquency_flag"] * 0.10,
        0.02,
        0.55,
    ),
)

df["autopay_enabled"] = np.random.binomial(
    1,
    np.clip(0.78 - df["risk_score"] * 0.32, 0.35, 0.88),
)

df["support_contact_last_30d"] = np.random.binomial(
    1,
    np.clip(
        0.09
        + df["risk_score"] * 0.18
        + df["current_delinquency_flag"] * 0.22,
        0.05,
        0.60,
    ),
)

df["hardship_program_enrolled"] = np.random.binomial(
    1,
    np.clip(
        0.02
        + df["risk_score"] * 0.10
        + df["current_delinquency_flag"] * 0.18,
        0.01,
        0.45,
    ),
)


# -------------------------
# Intervention assignment
# -------------------------
# Important:
# This is intentionally NOT randomized.
# Higher-risk customers are more likely to receive stronger interventions,
# creating selection bias for inference discussion.

intervention_group = []

for risk in df["risk_score"]:
    if risk < 0.35:
        intervention_group.append(
            np.random.choice(
                ["none", "sms_reminder"],
                p=[0.82, 0.18],
            )
        )
    elif risk < 0.60:
        intervention_group.append(
            np.random.choice(
                ["none", "sms_reminder", "repayment_call"],
                p=[0.45, 0.38, 0.17],
            )
        )
    else:
        intervention_group.append(
            np.random.choice(
                ["sms_reminder", "repayment_call", "hardship_outreach"],
                p=[0.30, 0.42, 0.28],
            )
        )

df["intervention_group"] = intervention_group


# -------------------------
# Repayment plan and recovery
# -------------------------

df["repayment_plan_type"] = np.where(
    df["hardship_program_enrolled"] == 1,
    np.random.choice(
        ["restructured", "grace_period"],
        size=N,
        p=[0.70, 0.30],
    ),
    np.random.choice(
        repayment_plan_types,
        size=N,
        p=[0.82, 0.13, 0.05],
    ),
)

recovery_probability = np.clip(
    0.64
    - df["risk_score"] * 0.28
    - df["current_delinquency_flag"] * 0.18
    + df["autopay_enabled"] * 0.10
    + (df["intervention_group"] == "sms_reminder") * 0.04
    + (df["intervention_group"] == "repayment_call") * 0.07
    + (df["intervention_group"] == "hardship_outreach") * 0.03,
    0.08,
    0.88,
)

df["payment_recovery_flag"] = np.random.binomial(
    1,
    recovery_probability,
)

df["repayment_probability_score"] = np.clip(
    0.86
    - df["risk_score"] * 0.45
    - df["current_delinquency_flag"] * 0.18
    + df["autopay_enabled"] * 0.08,
    0,
    1,
).round(3)


# -------------------------
# Realistic missingness
# -------------------------

missing_income_probability = df["income_band"].map({
    "low": 0.04,
    "lower_mid": 0.03,
    "mid": 0.02,
    "upper_mid": 0.015,
    "high": 0.01,
}).astype(float)

missing_income_mask = np.random.binomial(
    1,
    missing_income_probability,
).astype(bool)

df.loc[missing_income_mask, "monthly_income"] = np.nan

missing_employment_probability = df["employment_type"].map({
    "salaried": 0.01,
    "self_employed": 0.03,
    "gig_worker": 0.05,
    "student": 0.02,
    "unemployed": 0.04,
}).astype(float)

missing_employment_mask = np.random.binomial(
    1,
    missing_employment_probability,
).astype(bool)

df.loc[missing_employment_mask, "employment_type"] = np.nan


# -------------------------
# Save
# -------------------------

df.to_csv(OUTPUT_PATH, index=False)

print(f"Saved {OUTPUT_PATH}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("Expected analytical shape:")
print(df["risk_tier"].value_counts(normalize=True).round(3))
print(df["intervention_group"].value_counts(normalize=True).round(3))
print(df["current_delinquency_flag"].value_counts(normalize=True).round(3))