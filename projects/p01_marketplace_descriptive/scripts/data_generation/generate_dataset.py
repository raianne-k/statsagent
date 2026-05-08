import numpy as np
import pandas as pd

np.random.seed(42)

n = 1000

categories = ["clothing", "shoes", "bags", "accessories", "electronics", "home"]
regions = ["Tallinn", "Tartu", "Pärnu", "Narva", "Other"]

df = pd.DataFrame({
    "listing_id": range(1, n + 1),
    "seller_id": np.random.randint(1, 250, n),
    "buyer_id": np.random.randint(1, 700, n),
    "category": np.random.choice(categories, n, p=[0.35, 0.18, 0.12, 0.15, 0.08, 0.12]),
    "item_price": np.random.lognormal(mean=3.2, sigma=0.7, size=n).round(2),
    "shipping_price": np.random.choice([2.49, 2.99, 3.49, 4.99, 5.99], n),
    "listing_age_days": np.random.exponential(scale=18, size=n).round().astype(int),
    "views": np.random.lognormal(mean=3.4, sigma=0.9, size=n).round().astype(int),
    "likes": np.random.poisson(4, n),
    "add_to_cart": np.random.binomial(1, 0.18, n),
    "purchased": np.random.binomial(1, 0.11, n),
    "seller_rating": np.random.normal(4.6, 0.35, n).round(2).clip(1, 5),
    "buyer_returning": np.random.choice(["yes", "no"], n, p=[0.55, 0.45]),
    "region": np.random.choice(regions, n),
})

# Add realistic missingness
missing_rating_idx = np.random.choice(df.index, size=70, replace=False)
df.loc[missing_rating_idx, "seller_rating"] = np.nan

# Add high-price outliers
outlier_idx = np.random.choice(df.index, size=12, replace=False)
df.loc[outlier_idx, "item_price"] *= 6

# Add high-view outliers
viral_idx = np.random.choice(df.index, size=15, replace=False)
df.loc[viral_idx, "views"] *= 8

df.to_csv("data/marketplace_sample.csv", index=False)

print("Saved data/marketplace_sample.csv")