from pathlib import Path

import numpy as np
import pandas as pd

np.random.seed(42)

N = 8000

OUTPUT_PATH = Path(
    "projects/p05_saas_churn_prediction/data/raw/saas_churn_prediction_sample.csv"
)
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


regions = ["North America", "Europe", "UK", "APAC", "Other"]
industries = ["software", "finance", "healthcare", "retail", "education", "other"]
company_sizes = ["small", "mid_market", "enterprise"]
plan_tiers = ["starter", "growth", "business", "enterprise"]
contract_types = ["monthly", "annual"]


df = pd.DataFrame({
    "account_id": range(1, N + 1),

    "region": np.random.choice(
        regions,
        size=N,
        p=[0.38, 0.30, 0.12, 0.14, 0.06],
    ),

    "industry": np.random.choice(
        industries,
        size=N,
        p=[0.28, 0.18, 0.14, 0.15, 0.10, 0.15],
    ),

    "company_size": np.random.choice(
        company_sizes,
        size=N,
        p=[0.58, 0.30, 0.12],
    ),

    "contract_type": np.random.choice(
        contract_types,
        size=N,
        p=[0.62, 0.38],
    ),
})


plan_probs = {
    "small": [0.55, 0.33, 0.10, 0.02],
    "mid_market": [0.18, 0.42, 0.30, 0.10],
    "enterprise": [0.03, 0.14, 0.38, 0.45],
}

df["plan_tier"] = [
    np.random.choice(plan_tiers, p=plan_probs[size])
    for size in df["company_size"]
]


# -------------------------
# Commercial structure
# -------------------------

plan_base_mrr = {
    "starter": 49,
    "growth": 149,
    "business": 399,
    "enterprise": 1200,
}

size_multiplier = {
    "small": 1.0,
    "mid_market": 2.1,
    "enterprise": 5.0,
}

df["monthly_recurring_revenue"] = [
    plan_base_mrr[plan] * size_multiplier[size] * np.random.lognormal(0, 0.35)
    for plan, size in zip(df["plan_tier"], df["company_size"])
]

df["monthly_recurring_revenue"] = (
    df["monthly_recurring_revenue"]
    .round(2)
    .clip(20, 30000)
)

df["tenure_months"] = (
    np.random.exponential(scale=18, size=N)
    .round()
    .astype(int)
    .clip(0, 96)
)


# -------------------------
# Engagement behavior
# -------------------------

base_engagement = (
    0.25 * (df["contract_type"] == "annual").astype(float)
    + 0.20 * df["plan_tier"].map({
        "starter": 0.20,
        "growth": 0.45,
        "business": 0.65,
        "enterprise": 0.80,
    }).astype(float)
    + 0.20 * np.clip(df["tenure_months"] / 36, 0, 1)
    + np.random.normal(0, 0.12, N)
)

base_engagement = np.clip(base_engagement, 0, 1)

df["feature_adoption_rate"] = (
    20 + base_engagement * 70 + np.random.normal(0, 12, N)
).clip(0, 100).round(2)

df["seat_utilization_percent"] = (
    25 + base_engagement * 70 + np.random.normal(0, 10, N)
).clip(0, 100).round(2)

df["weekly_active_users"] = (
    np.random.lognormal(
        mean=1.1 + base_engagement * 1.8,
        sigma=0.65,
        size=N,
    )
).round().astype(int).clip(0, 500)

df["login_frequency_30d"] = (
    np.random.poisson(
        lam=3 + base_engagement * 18,
        size=N,
    )
).clip(0, 90)

df["avg_session_duration_minutes"] = (
    np.random.normal(
        loc=8 + base_engagement * 22,
        scale=6,
        size=N,
    )
).clip(1, 120).round(2)

df["days_since_last_login"] = (
    np.random.exponential(
        scale=22 - base_engagement * 15,
        size=N,
    )
).clip(0, 180).round().astype(int)


# -------------------------
# Support and account health
# -------------------------

df["support_ticket_count_90d"] = (
    np.random.poisson(
        lam=0.8 + (1 - base_engagement) * 2.2,
        size=N,
    )
).clip(0, 40)

df["unresolved_ticket_count"] = (
    np.random.binomial(
        n=df["support_ticket_count_90d"].clip(0, 20),
        p=np.clip(0.15 + (1 - base_engagement) * 0.25, 0.05, 0.55),
    )
)

df["support_escalation_flag"] = (
    df["unresolved_ticket_count"] >= 2
).astype(int)

df["onboarding_completed"] = np.random.binomial(
    1,
    np.clip(0.45 + base_engagement * 0.45, 0.35, 0.95),
)

df["multi_product_adoption"] = np.random.binomial(
    1,
    np.clip(0.12 + base_engagement * 0.45, 0.05, 0.75),
)

df["renewal_meeting_completed"] = np.random.binomial(
    1,
    np.clip(0.15 + base_engagement * 0.35, 0.05, 0.70),
)

df["discount_received"] = np.random.binomial(
    1,
    np.clip(0.28 - base_engagement * 0.10, 0.05, 0.35),
)


# -------------------------
# NPS and health score
# -------------------------

df["nps_score"] = (
    -10
    + base_engagement * 85
    - df["support_escalation_flag"] * 18
    + np.random.normal(0, 18, N)
).clip(-100, 100).round()

health_score = (
    0.28 * (df["feature_adoption_rate"] / 100)
    + 0.24 * (df["seat_utilization_percent"] / 100)
    + 0.16 * df["onboarding_completed"]
    + 0.14 * df["multi_product_adoption"]
    + 0.10 * ((df["nps_score"] + 100) / 200)
    - 0.08 * (df["days_since_last_login"] / 180)
    - 0.08 * df["support_escalation_flag"]
)

health_score = (
    (health_score - health_score.min())
    / (health_score.max() - health_score.min())
)

df["account_health_score"] = (health_score * 100).round(2)

df["health_band"] = pd.cut(
    df["account_health_score"],
    bins=[-1, 40, 70, 100],
    labels=["low_health", "medium_health", "high_health"],
)


# -------------------------
# Churn target
# -------------------------

churn_probability = (
    0.42
    - 0.26 * health_score
    + 0.09 * (df["contract_type"] == "monthly").astype(float)
    + 0.08 * df["support_escalation_flag"]
    + 0.07 * (df["days_since_last_login"] > 45).astype(float)
    - 0.05 * df["renewal_meeting_completed"]
    - 0.04 * df["onboarding_completed"]
)

churn_probability = np.clip(churn_probability, 0.04, 0.72)

df["churned"] = np.random.binomial(
    1,
    churn_probability,
)

df["renewal_probability_score"] = (
    1 - churn_probability + np.random.normal(0, 0.06, N)
).clip(0, 1).round(3)


# -------------------------
# Derived bands for analysis
# -------------------------

df["usage_band"] = pd.cut(
    df["feature_adoption_rate"],
    bins=[-1, 35, 70, 100],
    labels=["low_usage", "medium_usage", "high_usage"],
)

df["login_recency_band"] = pd.cut(
    df["days_since_last_login"],
    bins=[-1, 7, 30, 90, 180],
    labels=["active_0_7d", "warming_8_30d", "inactive_31_90d", "dormant_90d_plus"],
)

df["revenue_band"] = pd.cut(
    df["monthly_recurring_revenue"],
    bins=[0, 100, 500, 1500, np.inf],
    labels=["low_mrr", "mid_mrr", "high_mrr", "enterprise_mrr"],
)


# -------------------------
# Realistic missingness
# -------------------------

missing_nps_probability = np.clip(
    0.04 + (1 - base_engagement) * 0.14,
    0.03,
    0.22,
)

missing_nps_mask = np.random.binomial(
    1,
    missing_nps_probability,
).astype(bool)

df.loc[missing_nps_mask, "nps_score"] = np.nan

missing_health_probability = np.clip(
    0.01 + (df["tenure_months"] < 2).astype(float) * 0.08,
    0.01,
    0.12,
)

missing_health_mask = np.random.binomial(
    1,
    missing_health_probability,
).astype(bool)

df.loc[missing_health_mask, "account_health_score"] = np.nan
df.loc[missing_health_mask, "health_band"] = np.nan


# -------------------------
# Save
# -------------------------

df.to_csv(OUTPUT_PATH, index=False)

print(f"Saved {OUTPUT_PATH}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("Churn rate:")
print(df["churned"].mean().round(3))
print("Health band distribution:")
print(df["health_band"].value_counts(normalize=True, dropna=False).round(3))