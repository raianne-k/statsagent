# Analysis Report

Generated: 2026-04-30 11:06:37

## Task

descriptive_stats

## Dataset Overview

- Rows: 1000
- Columns: 14
- Duplicate rows: 0
- Numeric columns: ['listing_id', 'seller_id', 'buyer_id', 'item_price', 'shipping_price', 'listing_age_days', 'views', 'likes', 'add_to_cart', 'purchased', 'seller_rating']
- Categorical columns: ['category', 'buyer_returning', 'region']

## Missing Values

{'listing_id': 0, 'seller_id': 0, 'buyer_id': 0, 'category': 0, 'item_price': 0, 'shipping_price': 0, 'listing_age_days': 0, 'views': 0, 'likes': 0, 'add_to_cart': 0, 'purchased': 0, 'seller_rating': 70, 'buyer_returning': 0, 'region': 0}

## Method Used

Descriptive statistics using numeric columns only.

## Results

{'summary': {'listing_id': {'count': 1000.0, 'mean': 500.5, 'std': 288.82, 'min': 1.0, '25%': 250.75, '50%': 500.5, '75%': 750.25, 'max': 1000.0}, 'seller_id': {'count': 1000.0, 'mean': 128.57, 'std': 71.27, 'min': 1.0, '25%': 65.0, '50%': 131.0, '75%': 190.0, 'max': 249.0}, 'buyer_id': {'count': 1000.0, 'mean': 338.43, 'std': 204.43, 'min': 1.0, '25%': 156.75, '50%': 334.5, '75%': 517.0, 'max': 699.0}, 'item_price': {'count': 1000.0, 'mean': 32.89, 'std': 29.32, 'min': 2.96, '25%': 15.7, '50%': 24.91, '75%': 39.55, 'max': 259.74}, 'shipping_price': {'count': 1000.0, 'mean': 4.04, 'std': 1.3, 'min': 2.49, '25%': 2.99, '50%': 3.49, '75%': 4.99, 'max': 5.99}, 'listing_age_days': {'count': 1000.0, 'mean': 17.63, 'std': 17.55, 'min': 0.0, '25%': 5.0, '50%': 12.0, '75%': 25.0, 'max': 121.0}, 'views': {'count': 1000.0, 'mean': 46.69, 'std': 60.18, 'min': 2.0, '25%': 17.0, '50%': 30.0, '75%': 54.25, 'max': 1000.0}, 'likes': {'count': 1000.0, 'mean': 3.96, 'std': 1.87, 'min': 0.0, '25%': 3.0, '50%': 4.0, '75%': 5.0, 'max': 11.0}, 'add_to_cart': {'count': 1000.0, 'mean': 0.19, 'std': 0.39, 'min': 0.0, '25%': 0.0, '50%': 0.0, '75%': 0.0, 'max': 1.0}, 'purchased': {'count': 1000.0, 'mean': 0.11, 'std': 0.31, 'min': 0.0, '25%': 0.0, '50%': 0.0, '75%': 0.0, 'max': 1.0}, 'seller_rating': {'count': 930.0, 'mean': 4.57, 'std': 0.32, 'min': 3.42, '25%': 4.36, '50%': 4.58, '75%': 4.82, 'max': 5.0}}, 'extra_stats': {'listing_id': {'mean': np.float64(500.5), 'median': np.float64(500.5), 'variance': np.float64(83416.67), 'iqr': np.float64(499.5), 'outlier_count': 0, 'outlier_percent': 0.0, 'mean_median_gap_percent': np.float64(0.0), 'skew_warning': np.False_}, 'seller_id': {'mean': np.float64(128.57), 'median': np.float64(131.0), 'variance': np.float64(5079.8), 'iqr': np.float64(125.0), 'outlier_count': 0, 'outlier_percent': 0.0, 'mean_median_gap_percent': np.float64(1.85), 'skew_warning': np.False_}, 'buyer_id': {'mean': np.float64(338.43), 'median': np.float64(334.5), 'variance': np.float64(41792.94), 'iqr': np.float64(360.25), 'outlier_count': 0, 'outlier_percent': 0.0, 'mean_median_gap_percent': np.float64(1.18), 'skew_warning': np.False_}, 'item_price': {'mean': np.float64(32.89), 'median': np.float64(24.91), 'variance': np.float64(859.67), 'iqr': np.float64(23.84), 'outlier_count': 59, 'outlier_percent': 5.9, 'mean_median_gap_percent': np.float64(32.05), 'skew_warning': np.True_}, 'shipping_price': {'mean': np.float64(4.04), 'median': np.float64(3.49), 'variance': np.float64(1.68), 'iqr': np.float64(2.0), 'outlier_count': 0, 'outlier_percent': 0.0, 'mean_median_gap_percent': np.float64(15.67), 'skew_warning': np.False_}, 'listing_age_days': {'mean': np.float64(17.63), 'median': np.float64(12.0), 'variance': np.float64(307.84), 'iqr': np.float64(20.0), 'outlier_count': 45, 'outlier_percent': 4.5, 'mean_median_gap_percent': np.float64(46.89), 'skew_warning': np.True_}, 'views': {'mean': np.float64(46.69), 'median': np.float64(30.0), 'variance': np.float64(3621.95), 'iqr': np.float64(37.25), 'outlier_count': 79, 'outlier_percent': 7.9, 'mean_median_gap_percent': np.float64(55.64), 'skew_warning': np.True_}, 'likes': {'mean': np.float64(3.96), 'median': np.float64(4.0), 'variance': np.float64(3.51), 'iqr': np.float64(2.0), 'outlier_count': 9, 'outlier_percent': 0.9, 'mean_median_gap_percent': np.float64(1.12), 'skew_warning': np.False_}, 'add_to_cart': {'mean': np.float64(0.19), 'median': np.float64(0.0), 'variance': np.float64(0.15), 'iqr': np.float64(0.0), 'outlier_count': 189, 'outlier_percent': 18.9, 'mean_median_gap_percent': None, 'skew_warning': False}, 'purchased': {'mean': np.float64(0.11), 'median': np.float64(0.0), 'variance': np.float64(0.1), 'iqr': np.float64(0.0), 'outlier_count': 111, 'outlier_percent': 11.1, 'mean_median_gap_percent': None, 'skew_warning': False}, 'seller_rating': {'mean': np.float64(4.57), 'median': np.float64(4.58), 'variance': np.float64(0.1), 'iqr': np.float64(0.46), 'outlier_count': 10, 'outlier_percent': 1.08, 'mean_median_gap_percent': np.float64(0.21), 'skew_warning': np.False_}}}

## Interpretation

# Descriptive Statistics Interpretation
### E-Commerce Listing Dataset (n = 1,000 rows, 14 columns)

---

## 1. Method Used

**Descriptive statistics** were computed across all numeric columns, including measures of central tendency (mean, median), dispersion (standard deviation, variance, IQR), and distributional diagnostics (outlier counts via IQR fencing, mean/median gap percentage, skew warnings). Categorical columns (`category`, `buyer_returning`, `region`) were identified but not summarized numerically here.

---

## 2. Key Results

### 📋 Dataset Overview

| Property | Value |
|---|---|
| Total Rows | 1,000 |
| Total Columns | 14 |
| Duplicate Rows | 0 |
| Columns with Missing Data | 1 (`seller_rating`) |

---

### 📊 Variable-by-Variable Summary

#### 🔹 Identifier Columns (`listing_id`, `seller_id`, `buyer_id`)
- `listing_id` runs sequentially from 1 to 1,000 with a perfectly symmetric distribution (mean = median = 500.5). This is an index column and carries **no analytical meaning**.
- `seller_id` ranges 1–249, suggesting **~249 unique sellers** across 1,000 transactions (mean ≈ 129, median ≈ 131). Distribution is approximately symmetric (gap: 1.85%).
- `buyer_id` ranges 1–699, suggesting up to **699 unique buyers**. Distribution is near-symmetric (gap: 1.18%).

> ⚠️ **Note:** These are ID columns. Their statistical summaries reflect ID assignment patterns, not behavioral attributes.

---

#### 🔹 `item_price` *(float, fully observed)*

| Stat | Value |
|---|---|
| Mean | $32.89 |
| Median | $24.91 |
| Std Dev | $29.32 |
| Min / Max | $2.96 / $259.74 |
| Outliers (IQR) | 59 (5.9%) |
| Mean/Median Gap | 32.05% |
| Skew Warning | ✅ Yes |

**Observation:** The mean ($32.89) exceeds the median ($24.91) by 32%, and 75% of listings are priced at or below $39.55, while the maximum reaches $259.74. There are **59 high-price outliers (5.9%)**.

**Interpretation:** The distribution is **right-skewed**, driven by a minority of high-value listings. The median ($24.91) is likely a more representative measure of typical item price than the mean.

---

#### 🔹 `shipping_price` *(float, fully observed)*

| Stat | Value |
|---|---|
| Mean | $4.04 |
| Median | $3.49 |
| Std Dev | $1.30 |
| Min / Max | $2.49 / $5.99 |
| Outliers | 0 |
| Mean/Median Gap | 15.67% |

**Observation:** Shipping prices are tightly bounded between $2.49 and $5.99, with no IQR-detected outliers. The mean/median gap (15.67%) is notable but not flagged as a skew warning given the bounded range.

**Interpretation:** Shipping prices appear to be offered in **discrete tiers** (e.g., $2.49, $2.99, $3.49, $4.99, $5.99), which may inflate the apparent gap between mean and median. Distribution is compact and well-behaved.

---

#### 🔹 `listing_age_days` *(int, fully observed)*

| Stat | Value |
|---|---|
| Mean | 17.63 days |
| Median | 12.0 days |
| Std Dev | 17.55 days |
| Min / Max | 0 / 121 days |
| Outliers (IQR) | 45 (4.5%) |
| Mean/Median Gap | 46.89% |
| Skew Warning | ✅ Yes |

**Observation:** The mean (17.6 days) is nearly **47% higher** than the median (12 days). The standard deviation nearly equals the mean. There are 45 listings with ages flagged as outliers, including at least one reaching 121 days.

**Interpretation:** Listing age is **strongly right-skewed**. Most listings are relatively new (half are 12 days or younger), but a tail of long-running listings substantially pulls the mean upward. The median better represents a typical listing age.

---

#### 🔹 `views` *(int, fully observed)*

| Stat | Value |
|---|---|
| Mean | 46.69 |
| Median | 30.0 |
| Std Dev | 60.18 |
| Min / Max | 2 / 1,000 |
| Outliers (IQR) | 79 (7.9%) |
| Mean/Median Gap | 55.64% |
| Skew Warning | ✅ Yes |

**Observation:** This is the most skewed numeric variable in the dataset. The mean (46.69) is **55.6% above the median (30)**. The maximum (1,000 views) is extreme relative to the IQR (17–54 range). There are **79 outlier listings (7.9%)** by view count.

**Interpretation:** A small number of listings attract disproportionately high view counts, creating a **heavy right tail**. Most listings cluster in the 17–54 view range. Any mean-based analysis of views will be heavily influenced by this high-engagement minority.

---

#### 🔹 `likes` *(int, fully observed)*

| Stat | Value |
|---|---|
| Mean | 3.96 |
| Median | 4.0 |
| Std Dev | 1.87 |
| Min / Max | 0 / 11 |
| Outliers (IQR) | 9 (0.9%) |
| Mean/Median Gap | 1.12% |

**Observation:** Likes are tightly distributed (IQR: 3–5) with mean ≈ median. Only 9 records (0.9%) are flagged as outliers.

**Interpretation:** Likes show a **near-symmetric, well-behaved distribution**. This variable is relatively free from skew concerns.

---

#### 🔹 `add_to_cart` *(binary int, fully observed)*

| Stat | Value |
|---|---|
| Mean | 0.19 |
| Median | 0.0 |
| Min / Max | 0 / 1 |
| "Outlier" Count | 189 (18.9%) |

**Observation:** `add_to_cart` is a **binary variable** (0 = not added, 1 = added). The mean of 0.19 indicates that **approximately 19% of listings** in this dataset were added to cart.

> ⚠️ **Caution:** IQR-based outlier detection is **not appropriate** for binary variables. The "189 outliers" represent all positive cases (value = 1), not true anomalies. Mean/median gap is undefined/inapplicable here. The variable should be analyzed as a proportion, not a continuous measure.

---

#### 🔹 `purchased` *(binary int, fully observed)*

| Stat | Value |
|---|---|
| Mean | 0.11 |
| Median | 0.0 |
| Min / Max | 0 / 1 |
| "Outlier" Count | 111 (11.1%) |

**Observation:** `purchased` is also **binary**. The mean of 0.11 indicates **approximately 11% of listings** resulted in a purchase.

> ⚠️ **Same caution applies:** IQR-based outlier flagging is not meaningful for binary data. The 111 "outliers" are simply the purchased cases. The **overall purchase rate is 11%**, and the add-to-cart-to-purchase ratio is approximately 11/19 ≈ 58% (rough estimate; not directly calculated here).

---

#### 🔹 `seller_rating` *(float, **7% missing**)*

| Stat | Value |
|---|---|
| Observed Count | 930 / 1,000 |
| Missing | **70 records (7.0%)** |
| Mean | 4.57 |
| Median | 4.58 |
| Std Dev | 0.32 |
| Min / Max | 3.42 / 5.0 |
| Outliers (IQR) | 10 (1.08%) |
| Mean/Median Gap | 0.21% |

**Observation:** Seller ratings are tightly clustered near the top of the scale (4.36–4.82 IQR), with mean ≈ median (gap: 0.21%). Ten records are flagged as low-end outliers (min: 3.42).

**Interpretation:** Seller ratings show a **compressed, near-symmetric distribution** skewed toward high values — consistent with rating inflation commonly observed in peer-to-peer marketplace platforms.

> ⚠️ **Missing Data Alert:** 70 records (7%) have no seller rating. The reason for missingness is **unknown** and could be non-random (e.g., new sellers, unrated transactions). Results from this column should be interpreted with this caveat in mind.

---

## 3. Interpretation

- The dataset captures **1,000 marketplace listing transactions** with no duplicate rows and complete data across all columns except `seller_rating`.
- **Item price, views, and listing age** are all right-skewed, driven by high-value outliers. Median-based summaries are more representative for these variables.
- **Add-to-cart (19%) and purchased (11%)** are binary conversion metrics. Their descriptive stats should be read as **event rates**, not continuous distributions.
- **Seller ratings** are highly compressed near 5.0, with meaningful missingness (7%) that warrants investigation before using this field in downstream analysis.
- **Likes** and **shipping price** are the most well-behaved, approximately symmetric numeric variables.

---

## 4. Assumptions

- IQR-based outlier detection assumes that values beyond 1.5×IQR from Q1/Q3 are anomalies. This is **not appropriate for binary variables** (`add_to_cart`, `purchased`).
- Missing `seller_rating` values are assumed to be missing at random (MAR) for now, though this has not been verified.
- `listing_id`, `seller_id`, and `buyer_id` are treated as identifiers; their numeric statistics are not analytically meaningful.

---

## 5. Limitations

| Limitation | Detail |
|---|---|
| **Missing `seller_rating`** | 7% missingness; mechanism unknown. Could bias seller-related analysis. |
| **Binary variables mis-flagged as outliers** | IQR outlier counts for `add_to_cart` and `purchased` are artifacts of applying a continuous-variable method to binary data. |
| **No temporal data** | Without timestamps, trends over time cannot be assessed. |
| **No categorical breakdowns** | `category`, `region`, and `buyer_returning` are not summarized here; important variation may be hidden within groups. |
| **Causal inference not possible** | Associations between views, price, and purchases cannot be interpreted causally from descriptive statistics alone. |
| **Outliers not removed** | Skewed variables (price, views, age) retain their outliers; these may disproportionately influence any subsequent regression or mean-based modeling. |

---

## 6. Validation Notes

- ✅ No duplicate rows detected.
- ✅ All ID columns appear complete and plausible.
- ⚠️ `seller_rating` has 70 missing values — source and pattern of missingness should be investigated.
- ⚠️ Skew warnings triggered for `item_price`, `listing_age_days`, and `views` — consider log-transformation or median-based approaches for these in modeling.
- ⚠️ `views` max = 1,000 — verify whether this is a data cap/truncation or a genuine observation.
- ⚠️ Binary variable outlier counts should be disregarded as flagging artifacts.

---

## 7. Recommended Follow-up

1. **Investigate missing `seller_rating`** — Is missingness correlated with `purchased`, `views`, or `category`? Run a missingness pattern analysis.
2. **Examine categorical columns** — Break down `category`, `region`, and `buyer_returning` with frequency counts and cross-tabulations against `purchased` and `views`.
3. **Assess `views` cap** — Determine if the max of 1,000 views is a platform-imposed ceiling or a genuine data point.
4. **Log-transform skewed variables** — For any modeling involving `item_price`, `views`, or `listing_age_days`, consider log or square-root transformations.
5. **Conversion funnel analysis** — Compute views → add-to-cart → purchase rates by `category` and `region` to identify where drop-off occurs.
6. **Seller rating imputation assessment** — Decide whether to impute, exclude, or flag the 70 missing seller rating records based on missingness mechanism.
7. **Seller-level aggregation** — Since ~249 sellers appear across 1,000 listings, consider seller-level clustering effects before running any inferential analysis.

## Validation Notes

Status: pass

Warnings:

[]

## Limitations

This analysis summarizes dataset structure and numeric distributions. It does not test relationships, explain causes, or make predictions.

## Recommended Follow-up

Investigate variables with missing values, outliers, or skew before moving to correlation, hypothesis testing, or regression.
