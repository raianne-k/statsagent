"""
Synthetic SaaS strategic forecasting dataset generator.

Project:
p07_saas_strategic_forecasting

Purpose:
- cohort analysis
- retention forecasting
- operational trend analysis
- leading-indicator analysis
- scenario modeling
- revenue-risk forecasting
- governance-aware executive decision support

Dataset design:
- 1 row = 1 account x 1 month
- longitudinal SaaS account behavior
- synthetic but intentionally realistic operational relationships

Important:
This dataset is synthetic and should not be interpreted as real customer data.
Operational relationships partly reflect simulation logic and should be documented
as assumptions throughout the project.
"""

from pathlib import Path

import numpy as np
import pandas as pd


# -----------------------------
# Configuration
# -----------------------------

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

N_ACCOUNTS = 1800
N_MONTHS = 36

START_MONTH = "2022-01-01"

OUTPUT_PATH = Path(
    "projects/p07_saas_strategic_forecasting/data/raw/saas_account_monthly_forecasting.csv"
)
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


# -----------------------------
# Reference values
# -----------------------------

industries = ["software", "finance", "healthcare", "retail", "education", "other"]
company_sizes = ["small", "mid_market", "enterprise"]
plan_types = ["starter", "growth", "business", "enterprise"]
regions = ["North America", "Europe", "UK", "APAC", "Other"]
acquisition_channels = ["organic", "paid_search", "partner", "sales_outbound", "referral"]

plan_probs = {
    "small": [0.55, 0.32, 0.11, 0.02],
    "mid_market": [0.16, 0.42, 0.32, 0.10],
    "enterprise": [0.02, 0.12, 0.38, 0.48],
}

plan_base_mrr = {
    "starter": 79,
    "growth": 249,
    "business": 699,
    "enterprise": 2200,
}

size_multiplier = {
    "small": 1.0,
    "mid_market": 2.3,
    "enterprise": 5.5,
}

seat_baseline = {
    "starter": 7,
    "growth": 20,
    "business": 55,
    "enterprise": 180,
}

months = pd.date_range(START_MONTH, periods=N_MONTHS, freq="MS")


# -----------------------------
# Account-level base table
# -----------------------------

accounts = pd.DataFrame({
    "account_id": range(1, N_ACCOUNTS + 1),
    "industry": np.random.choice(
        industries,
        N_ACCOUNTS,
        p=[0.28, 0.18, 0.14, 0.15, 0.10, 0.15],
    ),
    "company_size": np.random.choice(
        company_sizes,
        N_ACCOUNTS,
        p=[0.56, 0.31, 0.13],
    ),
    "region": np.random.choice(
        regions,
        N_ACCOUNTS,
        p=[0.38, 0.29, 0.12, 0.15, 0.06],
    ),
    "acquisition_channel": np.random.choice(
        acquisition_channels,
        N_ACCOUNTS,
        p=[0.34, 0.24, 0.15, 0.17, 0.10],
    ),
})

accounts["plan_type"] = [
    np.random.choice(plan_types, p=plan_probs[size])
    for size in accounts["company_size"]
]

# signup months spread across the 36-month window
accounts["signup_month"] = np.random.choice(months, size=N_ACCOUNTS)

accounts["cohort_month"] = accounts["signup_month"]

# persistent account quality represents unobserved fit/product-market alignment
accounts["account_quality"] = np.random.beta(a=4, b=3, size=N_ACCOUNTS)

# onboarding is partly driven by account quality, acquisition channel, and company size
channel_onboarding_effect = accounts["acquisition_channel"].map({
    "organic": 4,
    "paid_search": -2,
    "partner": 6,
    "sales_outbound": 2,
    "referral": 7,
}).astype(float)

size_onboarding_effect = accounts["company_size"].map({
    "small": -3,
    "mid_market": 2,
    "enterprise": 4,
}).astype(float)

accounts["onboarding_completion"] = (
    45
    + accounts["account_quality"] * 45
    + channel_onboarding_effect
    + size_onboarding_effect
    + np.random.normal(0, 10, N_ACCOUNTS)
).clip(5, 100).round(2)

accounts["starting_seats"] = [
    max(1, int(np.random.poisson(seat_baseline[plan])))
    for plan in accounts["plan_type"]
]

accounts["base_mrr"] = [
    plan_base_mrr[plan] * size_multiplier[size] * noise
    for plan, size, noise in zip(
        accounts["plan_type"],
        accounts["company_size"],
        np.random.lognormal(mean=0, sigma=0.35, size=N_ACCOUNTS),
    )
]

accounts["base_mrr"] = accounts["base_mrr"].clip(40, 35000).round(2)


# -----------------------------
# Monthly account panel
# -----------------------------

records = []

for _, acc in accounts.iterrows():
    churned = False
    churn_month = None

    account_id = acc["account_id"]
    signup_month = pd.Timestamp(acc["signup_month"])
    quality = acc["account_quality"]
    onboarding = acc["onboarding_completion"]
    base_mrr = acc["base_mrr"]
    seats = acc["starting_seats"]

    # account-specific drift tendency
    engagement_drift = np.random.normal(0.001, 0.012)
    support_sensitivity = np.random.uniform(0.8, 1.4)

    current_mrr = base_mrr

    for snapshot_month in months:
        if snapshot_month < signup_month:
            continue

        cohort_age = (
            (snapshot_month.year - signup_month.year) * 12
            + (snapshot_month.month - signup_month.month)
        )

        if churned:
            continue

        lifecycle_ramp = min(1, (cohort_age + 1) / 6)

        seasonal_effect = 0.03 * np.sin((snapshot_month.month / 12) * 2 * np.pi)

        natural_decay = max(0, cohort_age - 9) * 0.006

        onboarding_boost = (onboarding - 60) / 100 * 0.28

        engagement_base = (
            0.34
            + quality * 0.36
            + onboarding_boost
            + lifecycle_ramp * 0.16
            + engagement_drift * cohort_age
            + seasonal_effect
            - natural_decay
            + np.random.normal(0, 0.06)
        )

        engagement_base = np.clip(engagement_base, 0.02, 0.98)

        feature_adoption_rate = (
            engagement_base * 82
            + onboarding * 0.12
            + np.random.normal(0, 7)
        ).clip(0, 100)

        usage_frequency = (
            2
            + engagement_base * 18
            + lifecycle_ramp * 3
            + np.random.normal(0, 3)
        ).clip(0, 31)

        active_users = int(
            np.round(
                seats
                * np.clip(engagement_base * np.random.uniform(0.65, 1.10), 0, 1)
            )
        )

        active_users = max(0, min(active_users, seats))

        days_since_last_login = int(
            np.random.exponential(scale=max(2, 32 - engagement_base * 25))
        )
        days_since_last_login = min(days_since_last_login, 180)

        friction = (
            (1 - onboarding / 100) * 1.6
            + max(0, 0.45 - engagement_base) * 2.4
            + np.random.normal(0, 0.25)
        )

        support_lambda = max(
            0.15,
            0.35
            + engagement_base * 0.7
            + friction * support_sensitivity
        )

        support_tickets = int(np.random.poisson(support_lambda))
        support_tickets = min(support_tickets, 35)

        product_health_score = (
            0.34 * engagement_base
            + 0.24 * (feature_adoption_rate / 100)
            + 0.18 * (usage_frequency / 31)
            + 0.16 * (onboarding / 100)
            - 0.08 * (days_since_last_login / 180)
            - 0.06 * min(support_tickets / 20, 1)
            + np.random.normal(0, 0.035)
        )

        product_health_score = np.clip(product_health_score, 0.01, 1.0)

        downgrade_risk = (
            0.03
            + 0.12 * (product_health_score < 0.35)
            + 0.06 * (days_since_last_login > 45)
            + 0.05 * (feature_adoption_rate < 35)
        )

        downgrade_flag = np.random.binomial(1, np.clip(downgrade_risk, 0.01, 0.35))

        expansion_probability = (
            0.04
            + 0.10 * (product_health_score > 0.70)
            + 0.06 * (feature_adoption_rate > 70)
            + 0.04 * (usage_frequency > 18)
            - 0.05 * downgrade_flag
        )

        expansion_probability = np.clip(expansion_probability, 0.01, 0.28)

        expansion_event = np.random.binomial(1, expansion_probability)

        expansion_revenue = 0
        if expansion_event:
            expansion_revenue = current_mrr * np.random.uniform(0.04, 0.18)

        if downgrade_flag:
            current_mrr *= np.random.uniform(0.84, 0.96)

        current_mrr += expansion_revenue

        # mild organic price/seat growth for retained healthy accounts
        if product_health_score > 0.65 and np.random.rand() < 0.08:
            current_mrr *= np.random.uniform(1.01, 1.04)

        current_mrr = float(np.clip(current_mrr, 20, 50000))

        churn_probability = (
            0.010
            + 0.095 * (1 - product_health_score)
            + 0.050 * (feature_adoption_rate < 35)
            + 0.045 * (days_since_last_login > 45)
            + 0.035 * (support_tickets >= 6)
            + 0.035 * (downgrade_flag == 1)
            - 0.030 * (onboarding > 80)
            - 0.020 * (cohort_age < 3)
        )

        # lifecycle churn risk generally rises after early ramp
        churn_probability += max(0, cohort_age - 12) * 0.0018

        churn_probability = np.clip(churn_probability, 0.002, 0.45)

        churn_flag = np.random.binomial(1, churn_probability)

        renewal_probability = (
            100
            - churn_probability * 100
            + product_health_score * 8
            + np.random.normal(0, 4)
        ).clip(0, 100)

        records.append({
            "account_id": account_id,
            "snapshot_month": snapshot_month,
            "signup_month": signup_month,
            "cohort_month": acc["cohort_month"],
            "cohort_age_months": cohort_age,
            "plan_type": acc["plan_type"],
            "company_size": acc["company_size"],
            "industry": acc["industry"],
            "region": acc["region"],
            "acquisition_channel": acc["acquisition_channel"],
            "active_users": active_users,
            "feature_adoption_rate": round(feature_adoption_rate, 2),
            "usage_frequency": round(usage_frequency, 2),
            "support_tickets": support_tickets,
            "days_since_last_login": days_since_last_login,
            "onboarding_completion": round(onboarding, 2),
            "product_health_score": round(product_health_score, 3),
            "monthly_recurring_revenue": round(current_mrr, 2),
            "expansion_revenue": round(expansion_revenue, 2),
            "downgrade_flag": downgrade_flag,
            "renewal_probability": round(renewal_probability, 2),
            "churn_flag": churn_flag,
        })

        if churn_flag == 1:
            churned = True
            churn_month = snapshot_month


df = pd.DataFrame(records)


# -----------------------------
# Sort and derive forecasting helpers
# -----------------------------

df = df.sort_values(["account_id", "snapshot_month"]).reset_index(drop=True)

df["rolling_health_3m"] = (
    df.groupby("account_id")["product_health_score"]
    .transform(lambda s: s.rolling(window=3, min_periods=1).mean())
    .round(3)
)

df["rolling_usage_3m"] = (
    df.groupby("account_id")["usage_frequency"]
    .transform(lambda s: s.rolling(window=3, min_periods=1).mean())
    .round(2)
)

df["prior_health"] = df.groupby("account_id")["product_health_score"].shift(1)
df["prior_usage"] = df.groupby("account_id")["usage_frequency"].shift(1)
df["prior_mrr"] = df.groupby("account_id")["monthly_recurring_revenue"].shift(1)

df["engagement_trend"] = (
    df["product_health_score"] - df["prior_health"]
).fillna(0).round(3)

df["revenue_trend"] = (
    (df["monthly_recurring_revenue"] - df["prior_mrr"]) / df["prior_mrr"]
).replace([np.inf, -np.inf], np.nan).fillna(0).round(4)

df["usage_trend"] = (
    df["usage_frequency"] - df["prior_usage"]
).fillna(0).round(2)

df = df.drop(columns=["prior_health", "prior_usage", "prior_mrr"])


# -----------------------------
# Analytical helper labels
# -----------------------------

df["health_band"] = pd.cut(
    df["product_health_score"],
    bins=[-0.01, 0.35, 0.65, 1.0],
    labels=["low_health", "medium_health", "high_health"],
)

df["usage_band"] = pd.cut(
    df["feature_adoption_rate"],
    bins=[-1, 35, 70, 100],
    labels=["low_usage", "medium_usage", "high_usage"],
)

df["login_recency_band"] = pd.cut(
    df["days_since_last_login"],
    bins=[-1, 7, 30, 90, np.inf],
    labels=[
        "active_0_7d",
        "warming_8_30d",
        "inactive_31_90d",
        "dormant_90d_plus",
    ],
)

df["mrr_band"] = pd.cut(
    df["monthly_recurring_revenue"],
    bins=[0, 250, 1000, 5000, np.inf],
    labels=["low_mrr", "mid_mrr", "high_mrr", "enterprise_mrr"],
)

df["revenue_at_risk"] = (
    df["monthly_recurring_revenue"] * (1 - df["renewal_probability"] / 100)
).round(2)


# -----------------------------
# Realistic missingness
# -----------------------------

# Feature adoption missing more often for low-usage accounts and very early lifecycle months.
missing_adoption_probability = (
    0.015
    + 0.08 * (df["usage_frequency"] < 3)
    + 0.04 * (df["cohort_age_months"] <= 1)
).clip(0.01, 0.18)

missing_adoption_mask = np.random.binomial(
    1,
    missing_adoption_probability,
).astype(bool)

df.loc[missing_adoption_mask, "feature_adoption_rate"] = np.nan
df.loc[missing_adoption_mask, "usage_band"] = np.nan

# Support tickets occasionally missing due to operational logging gaps.
missing_support_mask = np.random.binomial(1, 0.012, size=len(df)).astype(bool)
df.loc[missing_support_mask, "support_tickets"] = np.nan

# Industry missing for a small share of small accounts.
small_account_mask = df["company_size"] == "small"
missing_industry_mask = (
    small_account_mask
    & np.random.binomial(1, 0.025, size=len(df)).astype(bool)
)
df.loc[missing_industry_mask, "industry"] = np.nan


# -----------------------------
# Controlled anomalies for validation
# -----------------------------

# Small number of unusually high MRR rows.
mrr_outlier_idx = np.random.choice(df.index, size=20, replace=False)
df.loc[mrr_outlier_idx, "monthly_recurring_revenue"] *= np.random.uniform(2.5, 4.5, size=20)
df["monthly_recurring_revenue"] = df["monthly_recurring_revenue"].round(2).clip(20, 75000)

# Small number of support-ticket spikes.
valid_support_idx = df[df["support_tickets"].notna()].index
ticket_outlier_idx = np.random.choice(valid_support_idx, size=25, replace=False)
df.loc[ticket_outlier_idx, "support_tickets"] *= np.random.randint(3, 6, size=25)
df["support_tickets"] = df["support_tickets"].clip(0, 80)

# Recalculate revenue at risk after MRR anomaly injection.
df["revenue_at_risk"] = (
    df["monthly_recurring_revenue"] * (1 - df["renewal_probability"] / 100)
).round(2)


# -----------------------------
# Final formatting
# -----------------------------

date_cols = ["snapshot_month", "signup_month", "cohort_month"]
for col in date_cols:
    df[col] = pd.to_datetime(df[col]).dt.strftime("%Y-%m-%d")

ordered_columns = [
    "account_id",
    "snapshot_month",
    "signup_month",
    "cohort_month",
    "cohort_age_months",
    "plan_type",
    "company_size",
    "industry",
    "region",
    "acquisition_channel",
    "active_users",
    "feature_adoption_rate",
    "usage_frequency",
    "support_tickets",
    "days_since_last_login",
    "onboarding_completion",
    "product_health_score",
    "rolling_health_3m",
    "rolling_usage_3m",
    "engagement_trend",
    "usage_trend",
    "monthly_recurring_revenue",
    "expansion_revenue",
    "revenue_trend",
    "downgrade_flag",
    "renewal_probability",
    "churn_flag",
    "revenue_at_risk",
    "health_band",
    "usage_band",
    "login_recency_band",
    "mrr_band",
]

df = df[ordered_columns]


# -----------------------------
# Save dataset
# -----------------------------

df.to_csv(OUTPUT_PATH, index=False)

print(f"Saved {OUTPUT_PATH}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Accounts: {df['account_id'].nunique()}")
print(f"Months: {df['snapshot_month'].nunique()}")
print(f"Random seed: {RANDOM_SEED}")
print(f"Churn rate by row: {df['churn_flag'].mean():.3f}")
print(f"Average MRR: {df['monthly_recurring_revenue'].mean():.2f}")