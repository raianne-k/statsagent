"""
Synthetic SaaS account dataset generator.

Purpose:
- portfolio analytics
- relationship analysis
- correlation and association testing
- customer health analysis
- governance-aware AI-assisted analysis

This dataset is synthetic and should not be interpreted as real customer data.
"""

from pathlib import Path

import numpy as np
import pandas as pd


RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

N = 6000

OUTPUT_PATH = Path("projects/p03_saas_relationships/data/raw/saas_account_sample.csv")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


# -----------------------------
# Account base
# -----------------------------

industries = ["software", "finance", "healthcare", "retail", "education", "other"]
company_sizes = ["small", "mid_market", "enterprise"]
plans = ["starter", "growth", "business", "enterprise"]
contract_types = ["monthly", "annual"]
regions = ["North America", "Europe", "UK", "APAC", "Other"]

df = pd.DataFrame({
    "account_id": range(1, N + 1),
    "industry": np.random.choice(
        industries,
        N,
        p=[0.28, 0.18, 0.14, 0.15, 0.10, 0.15],
    ),
    "company_size": np.random.choice(
        company_sizes,
        N,
        p=[0.58, 0.30, 0.12],
    ),
    "region": np.random.choice(
        regions,
        N,
        p=[0.38, 0.30, 0.12, 0.14, 0.06],
    ),
    "contract_type": np.random.choice(
        contract_types,
        N,
        p=[0.62, 0.38],
    ),
})

plan_probs = {
    "small": [0.54, 0.32, 0.12, 0.02],
    "mid_market": [0.18, 0.42, 0.30, 0.10],
    "enterprise": [0.03, 0.16, 0.38, 0.43],
}

df["subscription_plan"] = [
    np.random.choice(plans, p=plan_probs[size])
    for size in df["company_size"]
]

df["account_age_months"] = np.random.exponential(scale=18, size=N).round().astype(int)
df["account_age_months"] = df["account_age_months"].clip(0, 84)


# -----------------------------
# Plan and account economics
# -----------------------------

plan_base_mrr = {
    "starter": 49,
    "growth": 149,
    "business": 399,
    "enterprise": 1200,
}

size_multiplier = {
    "small": 1.0,
    "mid_market": 2.2,
    "enterprise": 5.0,
}

mrr_noise = np.random.lognormal(mean=0, sigma=0.35, size=N)

df["monthly_recurring_revenue"] = [
    plan_base_mrr[plan] * size_multiplier[size] * noise
    for plan, size, noise in zip(
        df["subscription_plan"],
        df["company_size"],
        mrr_noise,
    )
]

df["monthly_recurring_revenue"] = (
    df["monthly_recurring_revenue"]
    .round(2)
    .clip(20, 25000)
)

df["seat_count"] = [
    int(np.random.poisson(lam={
        "starter": 5,
        "growth": 14,
        "business": 35,
        "enterprise": 120,
    }[plan]) + 1)
    for plan in df["subscription_plan"]
]

df["seat_count"] = pd.Series(df["seat_count"]).clip(1, 500)

df["seats_used_percent"] = (
    np.random.beta(a=4, b=2, size=N) * 100
).round(2)


# -----------------------------
# Product usage behavior
# -----------------------------

base_engagement = (
    0.35 * (df["seats_used_percent"] / 100)
    + 0.25 * (df["account_age_months"] / df["account_age_months"].max())
    + np.random.normal(0, 0.08, N)
).clip(0, 1)

plan_engagement_boost = df["subscription_plan"].map({
    "starter": -0.05,
    "growth": 0.02,
    "business": 0.08,
    "enterprise": 0.12,
}).astype(float)

engagement_score = (base_engagement + plan_engagement_boost).clip(0, 1)

df["weekly_active_users"] = (
    df["seat_count"] * engagement_score * np.random.uniform(0.55, 1.05, N)
).round().astype(int)

df["weekly_active_users"] = df["weekly_active_users"].clip(0, df["seat_count"])

df["feature_adoption_rate"] = (
    (engagement_score * 80)
    + np.random.normal(8, 12, N)
).clip(0, 100).round(2)

df["avg_session_minutes"] = (
    np.random.normal(
        loc=12 + engagement_score * 18,
        scale=6,
        size=N,
    )
).clip(1, 90).round(2)

df["admin_logins_last_30d"] = (
    np.random.poisson(lam=1 + engagement_score * 8, size=N)
).clip(0, 60)

df["onboarding_completion_percent"] = (
    35
    + engagement_score * 60
    + np.random.normal(0, 12, N)
).clip(0, 100).round(2)

df["days_since_last_login"] = (
    np.random.exponential(scale=20 - engagement_score * 14, size=N)
).clip(0, 180).round().astype(int)


# -----------------------------
# Support and customer signals
# -----------------------------

# Some support tickets reflect healthy usage, some reflect friction.
usage_ticket_component = engagement_score * 1.1
friction_component = (1 - df["onboarding_completion_percent"] / 100) * 2.2

df["support_tickets_last_90d"] = (
    np.random.poisson(
        lam=0.4 + usage_ticket_component + friction_component,
        size=N,
    )
).clip(0, 25)

df["nps_score"] = (
    20
    + engagement_score * 55
    - df["support_tickets_last_90d"] * 2.8
    + np.random.normal(0, 15, N)
).clip(-100, 100).round().astype(int)

df["nps_band"] = pd.cut(
    df["nps_score"],
    bins=[-101, 0, 50, 100],
    labels=["detractor", "passive", "promoter"],
)


# -----------------------------
# Account health and commercial outcomes
# -----------------------------

health_score = (
    0.35 * (df["feature_adoption_rate"] / 100)
    + 0.25 * (df["seats_used_percent"] / 100)
    + 0.20 * (df["onboarding_completion_percent"] / 100)
    + 0.10 * (df["nps_score"] + 100) / 200
    - 0.10 * (df["days_since_last_login"] / 180)
)

health_score = (health_score - health_score.min()) / (health_score.max() - health_score.min())

df["account_health_score"] = health_score.round(3)

df["health_band"] = pd.cut(
    df["account_health_score"],
    bins=[-0.01, 0.33, 0.66, 1.0],
    labels=["low_health", "medium_health", "high_health"],
)

churn_probability = (
    0.36
    - 0.28 * health_score
    + 0.08 * (df["contract_type"] == "monthly")
    + 0.05 * (df["onboarding_completion_percent"] < 50)
    + 0.04 * (df["days_since_last_login"] > 45)
).clip(0.02, 0.70)

df["churn_flag"] = np.random.binomial(1, churn_probability)

df["renewal_probability"] = (
    100
    - churn_probability * 100
    + np.random.normal(0, 8, N)
).clip(0, 100).round(2)

df["expansion_revenue"] = (
    df["monthly_recurring_revenue"]
    * np.random.beta(a=1.2 + health_score * 3, b=8, size=N)
).round(2)

df.loc[df["churn_flag"] == 1, "expansion_revenue"] *= np.random.uniform(0, 0.25, df["churn_flag"].sum())
df["expansion_revenue"] = df["expansion_revenue"].round(2)


# -----------------------------
# Derived relationship-analysis labels
# -----------------------------

df["usage_band"] = pd.cut(
    df["feature_adoption_rate"],
    bins=[-1, 35, 70, 100],
    labels=["low_usage", "medium_usage", "high_usage"],
)

df["revenue_band"] = pd.cut(
    df["monthly_recurring_revenue"],
    bins=[0, 100, 500, 1500, np.inf],
    labels=["low_mrr", "mid_mrr", "high_mrr", "enterprise_mrr"],
)

df["login_recency_band"] = pd.cut(
    df["days_since_last_login"],
    bins=[-1, 7, 30, 90, np.inf],
    labels=["active_0_7d", "warming_8_30d", "inactive_31_90d", "dormant_90d_plus"],
)


# -----------------------------
# Realistic missingness
# -----------------------------

# NPS missing more often for low-engagement accounts.
missing_nps_probability = (0.04 + (1 - engagement_score) * 0.18).clip(0.03, 0.25)
missing_nps_mask = np.random.binomial(1, missing_nps_probability).astype(bool)
df.loc[missing_nps_mask, "nps_score"] = np.nan
df.loc[missing_nps_mask, "nps_band"] = np.nan

# Industry missing for a small share of small accounts.
missing_industry_probability = df["company_size"].map({
    "small": 0.04,
    "mid_market": 0.02,
    "enterprise": 0.01,
}).astype(float)

missing_industry_mask = np.random.binomial(1, missing_industry_probability).astype(bool)
df.loc[missing_industry_mask, "industry"] = np.nan


# -----------------------------
# Controlled anomalies for validation
# -----------------------------

# A few unusually high MRR accounts.
mrr_outlier_idx = np.random.choice(df.index, size=18, replace=False)
df.loc[mrr_outlier_idx, "monthly_recurring_revenue"] *= 4
df["monthly_recurring_revenue"] = df["monthly_recurring_revenue"].round(2).clip(20, 30000)

# A few unusually high support-ticket accounts.
ticket_outlier_idx = np.random.choice(df.index, size=20, replace=False)
df.loc[ticket_outlier_idx, "support_tickets_last_90d"] *= 3
df["support_tickets_last_90d"] = df["support_tickets_last_90d"].clip(0, 60)


# -----------------------------
# Save dataset
# -----------------------------

df.to_csv(OUTPUT_PATH, index=False)

print(f"Saved {OUTPUT_PATH}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Random seed: {RANDOM_SEED}")