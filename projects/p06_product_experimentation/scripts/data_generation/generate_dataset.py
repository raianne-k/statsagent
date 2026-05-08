from pathlib import Path

import numpy as np
import pandas as pd


np.random.seed(42)

N = 10000

OUTPUT_PATH = Path(
    "projects/p06_product_experimentation/data/raw/saas_experimentation_sample.csv"
)
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# -------------------------
# User/account structure
# -------------------------

channels = ["organic", "paid_search", "paid_social", "referral", "partner", "direct"]
regions = ["North America", "Europe", "UK", "APAC", "Other"]
company_sizes = ["solo", "small", "mid_market", "enterprise"]
industries = ["software", "finance", "healthcare", "retail", "education", "other"]

df = pd.DataFrame(
    {
        "user_id": range(1, N + 1),
        "signup_date": pd.to_datetime("2026-01-01")
        + pd.to_timedelta(np.random.randint(0, 90, size=N), unit="D"),
        "acquisition_channel": np.random.choice(
            channels,
            size=N,
            p=[0.28, 0.20, 0.14, 0.16, 0.10, 0.12],
        ),
        "region": np.random.choice(
            regions,
            size=N,
            p=[0.38, 0.29, 0.12, 0.15, 0.06],
        ),
        "company_size": np.random.choice(
            company_sizes,
            size=N,
            p=[0.26, 0.45, 0.22, 0.07],
        ),
        "industry": np.random.choice(
            industries,
            size=N,
            p=[0.28, 0.17, 0.13, 0.15, 0.10, 0.17],
        ),
    }
)


# -------------------------
# Experiment assignment
# -------------------------
# Mostly balanced randomized assignment.
# Small imbalance is realistic but should remain analytically acceptable.

df["experiment_group"] = np.random.choice(
    ["control", "treatment"],
    size=N,
    p=[0.502, 0.498],
)

df["experiment_eligibility_flag"] = np.random.binomial(
    1,
    0.97,
    size=N,
)

# A small assignment quality issue for validation checks.
df["assignment_valid_flag"] = np.where(
    df["experiment_eligibility_flag"] == 1,
    np.random.binomial(1, 0.995, size=N),
    0,
)

df["exposure_days"] = np.where(
    df["assignment_valid_flag"] == 1,
    np.random.randint(21, 31, size=N),
    np.random.randint(0, 15, size=N),
)


# -------------------------
# Baseline user quality
# -------------------------

channel_quality = df["acquisition_channel"].map(
    {
        "organic": 0.22,
        "referral": 0.26,
        "direct": 0.18,
        "partner": 0.14,
        "paid_search": -0.06,
        "paid_social": -0.14,
    }
)

size_quality = df["company_size"].map(
    {
        "solo": -0.10,
        "small": 0.04,
        "mid_market": 0.18,
        "enterprise": 0.24,
    }
)

industry_quality = df["industry"].map(
    {
        "software": 0.08,
        "finance": 0.05,
        "healthcare": 0.02,
        "retail": -0.03,
        "education": -0.05,
        "other": -0.02,
    }
)

baseline_quality = (
    channel_quality
    + size_quality
    + industry_quality
    + np.random.normal(0, 0.35, size=N)
)

baseline_quality = np.clip(baseline_quality, -1.5, 1.5)


# -------------------------
# Treatment effect design
# -------------------------
# Treatment should help, but not magically.
# Stronger effect on activation/onboarding than on later retention.

is_treatment = (df["experiment_group"] == "treatment").astype(int)

treatment_activation_effect = 0.22
treatment_retention_effect = 0.10
treatment_upgrade_effect = 0.06

# Treatment may increase support tickets slightly because more users engage with onboarding.
treatment_support_effect = 0.18


# -------------------------
# Product behavior outcomes
# -------------------------

onboarding_probability = sigmoid(
    -0.20
    + 0.75 * baseline_quality
    + treatment_activation_effect * is_treatment
    + 0.08 * (df["company_size"] == "enterprise").astype(int)
)

df["onboarding_completion_flag"] = np.random.binomial(
    1,
    onboarding_probability,
)

activation_probability = sigmoid(
    -0.35
    + 0.85 * baseline_quality
    + 0.35 * df["onboarding_completion_flag"]
    + treatment_activation_effect * is_treatment
)

df["activation_flag"] = np.random.binomial(
    1,
    activation_probability,
)

df["feature_adoption_count"] = np.random.poisson(
    lam=np.clip(
        2.1
        + 1.4 * baseline_quality
        + 1.2 * df["activation_flag"]
        + 0.45 * is_treatment,
        0.4,
        8.5,
    )
).clip(0, 18)

df["sessions_first_14d"] = np.random.poisson(
    lam=np.clip(
        4.5
        + 2.2 * baseline_quality
        + 4.0 * df["activation_flag"]
        + 0.8 * is_treatment,
        0.5,
        22,
    )
).clip(0, 60)

df["support_tickets_first_30d"] = np.random.poisson(
    lam=np.clip(
        0.55
        + 0.20 * df["activation_flag"]
        + treatment_support_effect * is_treatment
        + 0.18 * (df["company_size"] == "enterprise").astype(int),
        0.05,
        4.5,
    )
).clip(0, 20)


# -------------------------
# Retention / churn outcomes
# -------------------------

retained_30d_probability = sigmoid(
    -0.45
    + 0.80 * baseline_quality
    + 0.70 * df["activation_flag"]
    + treatment_retention_effect * is_treatment
)

df["retained_30d"] = np.random.binomial(
    1,
    retained_30d_probability,
)

retained_60d_probability = sigmoid(
    -0.80
    + 0.85 * baseline_quality
    + 0.60 * df["retained_30d"]
    + 0.35 * df["activation_flag"]
    + 0.06 * is_treatment
)

df["retained_60d"] = np.random.binomial(
    1,
    retained_60d_probability,
)

df["churn_30d"] = 1 - df["retained_30d"]


# -------------------------
# Revenue / upgrade outcomes
# -------------------------

base_subscription_value = df["company_size"].map(
    {
        "solo": 29,
        "small": 79,
        "mid_market": 249,
        "enterprise": 899,
    }
)

df["monthly_subscription_value"] = (
    base_subscription_value
    * np.random.lognormal(mean=0, sigma=0.35, size=N)
).round(2)

df["monthly_subscription_value"] = df["monthly_subscription_value"].clip(10, 5000)

upgrade_probability = sigmoid(
    -2.10
    + 0.45 * baseline_quality
    + 0.45 * df["activation_flag"]
    + 0.25 * df["retained_30d"]
    + treatment_upgrade_effect * is_treatment
)

df["upgrade_flag"] = np.random.binomial(
    1,
    upgrade_probability,
)

df["expansion_revenue_flag"] = np.where(
    df["upgrade_flag"] == 1,
    np.random.binomial(1, 0.62, size=N),
    np.random.binomial(1, 0.05, size=N),
)


# -------------------------
# Guardrail / quality variables
# -------------------------

df["negative_feedback_flag"] = np.random.binomial(
    1,
    np.clip(
        0.07
        + 0.015 * df["support_tickets_first_30d"]
        - 0.015 * df["activation_flag"]
        + 0.01 * is_treatment,
        0.02,
        0.22,
    ),
)

df["time_to_activation_days"] = np.where(
    df["activation_flag"] == 1,
    np.random.gamma(
        shape=2.2,
        scale=np.clip(2.8 - 0.35 * is_treatment, 1.7, 3.1),
        size=N,
    ),
    np.nan,
)

df["time_to_activation_days"] = np.round(df["time_to_activation_days"], 1)


# -------------------------
# Derived analysis bands
# -------------------------

df["subscription_value_band"] = pd.cut(
    df["monthly_subscription_value"],
    bins=[0, 50, 150, 500, np.inf],
    labels=["low_value", "mid_value", "high_value", "enterprise_value"],
)

df["engagement_band"] = pd.cut(
    df["sessions_first_14d"],
    bins=[-1, 3, 8, 15, np.inf],
    labels=["low_engagement", "moderate_engagement", "high_engagement", "power_engagement"],
)

df["feature_adoption_band"] = pd.cut(
    df["feature_adoption_count"],
    bins=[-1, 1, 3, 6, np.inf],
    labels=["minimal_adoption", "basic_adoption", "moderate_adoption", "broad_adoption"],
)


# -------------------------
# Realistic missingness
# -------------------------

# Some users have no activation timing because they never activated.
# Also add small missingness in acquisition channel and company size.

missing_channel_mask = np.random.binomial(1, 0.008, size=N).astype(bool)
df.loc[missing_channel_mask, "acquisition_channel"] = np.nan

missing_company_size_mask = np.random.binomial(1, 0.006, size=N).astype(bool)
df.loc[missing_company_size_mask, "company_size"] = np.nan

# Keep a flag-style column for experiment exposure quality.
df["low_exposure_flag"] = (df["exposure_days"] < 21).astype(int)


# -------------------------
# Column ordering
# -------------------------

ordered_columns = [
    "user_id",
    "signup_date",
    "acquisition_channel",
    "region",
    "company_size",
    "industry",
    "experiment_group",
    "experiment_eligibility_flag",
    "assignment_valid_flag",
    "exposure_days",
    "low_exposure_flag",
    "onboarding_completion_flag",
    "activation_flag",
    "retained_30d",
    "retained_60d",
    "churn_30d",
    "upgrade_flag",
    "expansion_revenue_flag",
    "negative_feedback_flag",
    "sessions_first_14d",
    "feature_adoption_count",
    "support_tickets_first_30d",
    "time_to_activation_days",
    "monthly_subscription_value",
    "subscription_value_band",
    "engagement_band",
    "feature_adoption_band",
]

df = df[ordered_columns]


# -------------------------
# Save
# -------------------------

df.to_csv(OUTPUT_PATH, index=False)

print(f"Saved dataset to: {OUTPUT_PATH}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print()
print("Experiment group distribution:")
print(df["experiment_group"].value_counts(normalize=True).round(3))
print()
print("Primary metric rates by group:")
print(
    df.groupby("experiment_group")[
        ["activation_flag", "retained_30d", "retained_60d", "upgrade_flag"]
    ]
    .mean()
    .round(3)
)