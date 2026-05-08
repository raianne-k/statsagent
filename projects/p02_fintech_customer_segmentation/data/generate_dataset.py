"""
Synthetic fintech dataset generator.

Purpose:
- portfolio analytics
- segmentation analysis
- repayment-risk comparison
- validation-aware workflows
- governance-aware AI-assisted analysis

This dataset is synthetic and should not be interpreted as real customer data.
"""

from pathlib import Path

import numpy as np
import pandas as pd


RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

N = 8000

OUTPUT_PATH = Path("projects/02_fintech_segmentation/data/raw/fintech_customer_sample.csv")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


# -----------------------------
# Customer base
# -----------------------------

customer_id = range(1, N + 1)

regions = ["Tallinn", "Tartu", "Pärnu", "Narva", "Other"]
acquisition_channels = ["organic", "paid_search", "referral", "partner", "social"]
employment_types = ["salaried", "self_employed", "gig_worker", "student", "unemployed"]
device_types = ["ios", "android", "web"]

df = pd.DataFrame({
    "customer_id": customer_id,
    "region": np.random.choice(regions, N, p=[0.42, 0.22, 0.10, 0.11, 0.15]),
    "acquisition_channel": np.random.choice(
        acquisition_channels,
        N,
        p=[0.34, 0.24, 0.16, 0.14, 0.12],
    ),
    "employment_type": np.random.choice(
        employment_types,
        N,
        p=[0.56, 0.16, 0.12, 0.09, 0.07],
    ),
    "device_type": np.random.choice(device_types, N, p=[0.38, 0.52, 0.10]),
    "customer_tenure_months": np.random.exponential(scale=14, size=N).round().astype(int),
})

df["customer_tenure_months"] = df["customer_tenure_months"].clip(0, 72)


# -----------------------------
# Financial profile
# -----------------------------

employment_income_base = {
    "salaried": 2100,
    "self_employed": 1900,
    "gig_worker": 1350,
    "student": 850,
    "unemployed": 650,
}

income_noise = np.random.lognormal(mean=0, sigma=0.35, size=N)

df["monthly_income"] = [
    employment_income_base[employment] * noise
    for employment, noise in zip(df["employment_type"], income_noise)
]

df["monthly_income"] = df["monthly_income"].round(2).clip(350, 8500)

df["income_band"] = pd.cut(
    df["monthly_income"],
    bins=[0, 1000, 1800, 3000, 5000, np.inf],
    labels=["low", "lower_mid", "mid", "upper_mid", "high"],
)

base_utilization = np.random.beta(a=2.2, b=5.0, size=N)

employment_risk_adjustment = df["employment_type"].map({
    "salaried": -0.04,
    "self_employed": 0.02,
    "gig_worker": 0.09,
    "student": 0.05,
    "unemployed": 0.14,
}).astype(float)

df["credit_utilization_percent"] = (
    (base_utilization + employment_risk_adjustment + np.random.normal(0, 0.06, N))
    .clip(0, 1)
    * 100
).round(2)

df["debt_to_income_ratio"] = (
    0.15
    + (df["credit_utilization_percent"] / 100) * 0.55
    + np.random.normal(0, 0.08, N)
).clip(0.02, 1.4).round(2)

df["savings_balance"] = (
    df["monthly_income"]
    * np.random.lognormal(mean=-0.4, sigma=0.75, size=N)
    * (1 - df["credit_utilization_percent"] / 140)
).clip(0, 25000).round(2)


# -----------------------------
# Loan profile
# -----------------------------

loan_size_factor = np.random.lognormal(mean=-0.2, sigma=0.55, size=N)

df["active_loan_amount"] = (
    df["monthly_income"]
    * loan_size_factor
    * np.random.uniform(0.35, 1.8, N)
).round(2).clip(100, 15000)

df["loan_term_months"] = np.random.choice(
    [3, 6, 9, 12, 18, 24],
    N,
    p=[0.10, 0.22, 0.18, 0.28, 0.12, 0.10],
)

df["installment_size"] = (
    df["active_loan_amount"] / df["loan_term_months"]
).round(2)

df["loan_to_income_ratio"] = (
    df["active_loan_amount"] / df["monthly_income"]
).round(2)


# -----------------------------
# Behavioral profile
# -----------------------------

stress_score = (
    0.35 * df["debt_to_income_ratio"]
    + 0.35 * (df["credit_utilization_percent"] / 100)
    + 0.20 * df["loan_to_income_ratio"]
    - 0.10 * np.log1p(df["savings_balance"]) / 10
)

stress_score = (stress_score - stress_score.min()) / (stress_score.max() - stress_score.min())

df["financial_stress_score"] = stress_score.round(3)

df["app_sessions_per_week"] = (
    np.random.poisson(lam=3 + stress_score * 5, size=N)
).clip(0, 35)

df["avg_session_minutes"] = (
    np.random.normal(loc=5 + stress_score * 4, scale=2.2, size=N)
).clip(0.5, 35).round(2)

df["days_since_last_login"] = (
    np.random.exponential(scale=10 - stress_score * 5, size=N)
).clip(0, 90).round().astype(int)

df["support_tickets_last_90d"] = (
    np.random.poisson(lam=0.3 + stress_score * 2.2, size=N)
).clip(0, 15)

df["autopay_enabled"] = np.random.binomial(
    1,
    p=(0.72 - stress_score * 0.28).clip(0.25, 0.85),
)

df["number_of_products"] = np.random.choice(
    [1, 2, 3, 4],
    N,
    p=[0.58, 0.27, 0.11, 0.04],
)

df["promo_usage_rate"] = (
    np.random.beta(a=1.5 + stress_score * 2, b=5, size=N) * 100
).round(2)


# -----------------------------
# Repayment behavior
# -----------------------------

delinquency_probability = (
    0.04
    + 0.33 * stress_score
    + 0.08 * (df["autopay_enabled"] == 0)
    + 0.04 * (df["customer_tenure_months"] < 3)
).clip(0.02, 0.65)

df["delinquency_flag"] = np.random.binomial(1, delinquency_probability)

df["missed_payments_last_12m"] = np.random.poisson(
    lam=0.25 + stress_score * 2.5 + df["delinquency_flag"] * 1.2,
    size=N,
).clip(0, 8)

df["avg_days_late"] = (
    df["missed_payments_last_12m"]
    * np.random.uniform(1.5, 5.5, N)
    + np.random.normal(0, 2, N)
).clip(0, 60).round(1)

df["repayment_rate_percent"] = (
    100
    - df["missed_payments_last_12m"] * np.random.uniform(4, 9, N)
    - stress_score * np.random.uniform(2, 8, N)
).clip(35, 100).round(2)


# -----------------------------
# Derived segment labels
# -----------------------------

df["risk_band"] = pd.cut(
    df["financial_stress_score"],
    bins=[-0.01, 0.33, 0.66, 1.0],
    labels=["low_risk", "medium_risk", "high_risk"],
)

df["engagement_band"] = pd.cut(
    df["app_sessions_per_week"],
    bins=[-1, 2, 6, np.inf],
    labels=["low_engagement", "medium_engagement", "high_engagement"],
)

df["utilization_band"] = pd.cut(
    df["credit_utilization_percent"],
    bins=[-1, 30, 70, 100],
    labels=["low_utilization", "medium_utilization", "high_utilization"],
)


# -----------------------------
# Realistic missingness
# -----------------------------

# Savings balance missing more often for high-stress customers.
missing_savings_probability = (0.04 + stress_score * 0.18).clip(0.02, 0.30)
missing_savings_mask = np.random.binomial(1, missing_savings_probability).astype(bool)
df.loc[missing_savings_mask, "savings_balance"] = np.nan

# Employment type missing more often for gig/self-employed users.
employment_missing_probability = df["employment_type"].map({
    "salaried": 0.01,
    "self_employed": 0.05,
    "gig_worker": 0.08,
    "student": 0.03,
    "unemployed": 0.04,
}).astype(float)

employment_missing_mask = np.random.binomial(1, employment_missing_probability).astype(bool)
df.loc[employment_missing_mask, "employment_type"] = np.nan


# -----------------------------
# Controlled anomalies for validation
# -----------------------------

# A few unusually high loan amounts for outlier testing.
loan_outlier_idx = np.random.choice(df.index, size=20, replace=False)
df.loc[loan_outlier_idx, "active_loan_amount"] *= 3
df["active_loan_amount"] = df["active_loan_amount"].round(2).clip(100, 25000)

# A few unusually high app-session users.
session_outlier_idx = np.random.choice(df.index, size=25, replace=False)
df.loc[session_outlier_idx, "app_sessions_per_week"] *= 3
df["app_sessions_per_week"] = df["app_sessions_per_week"].clip(0, 80)


# -----------------------------
# Save dataset
# -----------------------------

df.to_csv(OUTPUT_PATH, index=False)

print(f"Saved {OUTPUT_PATH}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Random seed: {RANDOM_SEED}")