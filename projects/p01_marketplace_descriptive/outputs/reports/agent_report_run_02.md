# Analysis Report

Generated: 2026-05-03 10:59:31

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

{'excluded_id_columns': ['listing_id', 'seller_id', 'buyer_id', 'item_price'], 'summary': {'shipping_price': {'count': 1000.0, 'mean': 4.04, 'std': 1.3, 'min': 2.49, '25%': 2.99, '50%': 3.49, '75%': 4.99, 'max': 5.99}, 'listing_age_days': {'count': 1000.0, 'mean': 17.63, 'std': 17.55, 'min': 0.0, '25%': 5.0, '50%': 12.0, '75%': 25.0, 'max': 121.0}, 'views': {'count': 1000.0, 'mean': 46.69, 'std': 60.18, 'min': 2.0, '25%': 17.0, '50%': 30.0, '75%': 54.25, 'max': 1000.0}, 'likes': {'count': 1000.0, 'mean': 3.96, 'std': 1.87, 'min': 0.0, '25%': 3.0, '50%': 4.0, '75%': 5.0, 'max': 11.0}, 'add_to_cart': {'count': 1000.0, 'mean': 0.19, 'std': 0.39, 'min': 0.0, '25%': 0.0, '50%': 0.0, '75%': 0.0, 'max': 1.0}, 'purchased': {'count': 1000.0, 'mean': 0.11, 'std': 0.31, 'min': 0.0, '25%': 0.0, '50%': 0.0, '75%': 0.0, 'max': 1.0}, 'seller_rating': {'count': 930.0, 'mean': 4.57, 'std': 0.32, 'min': 3.42, '25%': 4.36, '50%': 4.58, '75%': 4.82, 'max': 5.0}}, 'extra_stats': {'shipping_price': {'mean': np.float64(4.04), 'median': np.float64(3.49), 'variance': np.float64(1.68), 'iqr': np.float64(2.0), 'outlier_count': 0, 'outlier_percent': 0.0, 'mean_median_gap_percent': np.float64(15.67), 'skew_warning': np.False_}, 'listing_age_days': {'mean': np.float64(17.63), 'median': np.float64(12.0), 'variance': np.float64(307.84), 'iqr': np.float64(20.0), 'outlier_count': 45, 'outlier_percent': 4.5, 'mean_median_gap_percent': np.float64(46.89), 'skew_warning': np.True_}, 'views': {'mean': np.float64(46.69), 'median': np.float64(30.0), 'variance': np.float64(3621.95), 'iqr': np.float64(37.25), 'outlier_count': 79, 'outlier_percent': 7.9, 'mean_median_gap_percent': np.float64(55.64), 'skew_warning': np.True_}, 'likes': {'mean': np.float64(3.96), 'median': np.float64(4.0), 'variance': np.float64(3.51), 'iqr': np.float64(2.0), 'outlier_count': 9, 'outlier_percent': 0.9, 'mean_median_gap_percent': np.float64(1.12), 'skew_warning': np.False_}, 'add_to_cart': {'mean': np.float64(0.19), 'median': np.float64(0.0), 'variance': np.float64(0.15), 'iqr': np.float64(0.0), 'outlier_count': 189, 'outlier_percent': 18.9, 'mean_median_gap_percent': None, 'skew_warning': False}, 'purchased': {'mean': np.float64(0.11), 'median': np.float64(0.0), 'variance': np.float64(0.1), 'iqr': np.float64(0.0), 'outlier_count': 111, 'outlier_percent': 11.1, 'mean_median_gap_percent': None, 'skew_warning': False}, 'seller_rating': {'mean': np.float64(4.57), 'median': np.float64(4.58), 'variance': np.float64(0.1), 'iqr': np.float64(0.46), 'outlier_count': 10, 'outlier_percent': 1.08, 'mean_median_gap_percent': np.float64(0.21), 'skew_warning': np.False_}}}

## Interpretation

# Descriptive Statistics Analysis Report

---

## 1. Method Used

Standard descriptive statistics were computed across numeric columns in a 1,000-row marketplace listing dataset (14 columns total). ID columns (`listing_id`, `seller_id`, `buyer_id`) and `item_price` were appropriately excluded from distributional analysis. Extra diagnostics were computed including: IQR-based outlier detection, mean/median gap percentage, variance, and skew warnings. Binary columns (`add_to_cart`, `purchased`) were treated as proportion metrics rather than continuous distributions.

---

## 2. Key Results

### Numeric Summary Table

| Variable | Mean | Median | Std Dev | Min | Max | Outliers (%) | Skew Warning |
|---|---|---|---|---|---|---|---|
| `shipping_price` | 4.04 | 3.49 | 1.30 | 2.49 | 5.99 | 0 (0%) | ❌ |
| `listing_age_days` | 17.63 | 12.00 | 17.55 | 0 | 121 | 45 (4.5%) | ⚠️ Yes |
| `views` | 46.69 | 30.00 | 60.18 | 2 | 1,000 | 79 (7.9%) | ⚠️ Yes |
| `likes` | 3.96 | 4.00 | 1.87 | 0 | 11 | 9 (0.9%) | ❌ |
| `add_to_cart` | 0.19 | 0.00 | 0.39 | 0 | 1 | — (binary) | — |
| `purchased` | 0.11 | 0.00 | 0.31 | 0 | 1 | — (binary) | — |
| `seller_rating` | 4.57 | 4.58 | 0.32 | 3.42 | 5.00 | 10 (1.08%) | ❌ |

> **Note:** `seller_rating` has **70 missing values (7.0%)** — all statistics for this column reflect only the 930 available records.

### Binary Variable Proportions
- **`add_to_cart`:** 19% of listings had an add-to-cart event
- **`purchased`:** 11% of listings resulted in a purchase

---

## 3. Interpretation

### 🔴 Priority Finding: `views` is Heavily Right-Skewed
**Observation:** Mean views = 46.69, median = 30.00, max = 1,000. The mean/median gap is **55.6%**, and 79 listings (7.9%) are flagged as outliers. Standard deviation (60.18) exceeds the mean.

**Interpretation:** The majority of listings receive modest view counts, but a small subset attracts disproportionately high traffic. The mean is substantially inflated by high-view outliers. The median (30 views) is a more representative central value for a typical listing.

---

### 🔴 Priority Finding: `listing_age_days` is Right-Skewed
**Observation:** Mean = 17.63, median = 12.00, mean/median gap = **46.9%**, max = 121 days, with 45 outliers (4.5%). Standard deviation nearly equals the mean.

**Interpretation:** Most listings are relatively new (half are 12 days old or younger), but a long tail of older listings pulls the mean upward. The outlier threshold at 121 days suggests a small number of listings have remained active for several months.

---

### 🟡 Finding: `shipping_price` Has Discrete Tier Structure
**Observation:** Min = 2.49, 25th percentile = 2.99, median = 3.49, 75th percentile = 4.99, max = 5.99. No IQR-based outliers detected. Mean/median gap = 15.67%.

**Interpretation:** The values cluster around distinct price points (2.49, 2.99, 3.49, 4.99, 5.99), strongly suggesting **predefined shipping tiers** rather than a continuous distribution. This variable should be treated as an ordinal or categorical variable in downstream modeling. The mean/median gap is modest but is partly an artifact of the non-continuous structure.

---

### 🟡 Finding: Conversion Funnel Proportions
**Observation:** 19% of records have `add_to_cart = 1`; 11% have `purchased = 1`. Both are binary (0/1) variables with median = 0 and IQR = 0.

**Interpretation:** These are binary event flags, not continuous measures. The figures indicate that roughly 1 in 5 listings received a cart event, and approximately 1 in 9 resulted in a purchase. The gap between add-to-cart (19%) and purchase (11%) suggests meaningful drop-off between cart intent and completed transaction. Causal interpretation requires further analysis.

---

### 🟢 Finding: `seller_rating` is Tightly Distributed Near Maximum
**Observation:** Mean = 4.57, median = 4.58, std = 0.32, min = 3.42, max = 5.00. Mean/median gap = 0.21% — extremely close. Only 10 outliers (1.08%).

**Interpretation:** Seller ratings are compressed toward the high end of the scale (effectively 3.42–5.00 out of 5.00). This **ceiling effect** limits the discriminatory power of this variable. The 70 missing values (7%) could introduce bias if the missingness is systematic (e.g., new sellers or disputed transactions).

---

### 🟢 Finding: `likes` is Symmetrically Distributed
**Observation:** Mean = 3.96, median = 4.00, std = 1.87, range = 0–11. Mean/median gap = 1.12%, 9 outliers (0.9%).

**Interpretation:** `likes` is the most normally distributed variable in this dataset. Values are centered around 4 with low dispersion, suggesting relatively uniform engagement with listings at this metric.

---

## 4. Assumptions

- Binary variables (`add_to_cart`, `purchased`) are treated as **event flags** (0/1), and standard continuous distribution metrics (mean/median gap, skew warnings) are not applied to them.
- ID columns (`listing_id`, `seller_id`, `buyer_id`) are correctly excluded from distributional analysis as they carry no statistical meaning.
- `item_price` was listed as excluded per the analysis configuration — no statistics were produced for it and no interpretation is offered.
- IQR × 1.5 fence method is assumed for outlier detection.
- Missing values in `seller_rating` are assumed to be missing at random unless further investigation indicates otherwise.

---

## 5. Limitations

| Limitation | Impact |
|---|---|
| `seller_rating` has 7% missing values | Rating-based conclusions are based on 93% of data; if missing values are non-random (e.g., absent for low-rated sellers), the mean of 4.57 may be **upward biased** |
| `item_price` was excluded | A key variable for marketplace analysis is unavailable for this report |
| `views` outliers (max = 1,000) are extreme | These may represent viral or promoted listings; they distort the mean significantly |
| `shipping_price` has a discrete tier structure | Treating it as continuous in any model would be inappropriate |
| No temporal dimension is available beyond `listing_age_days` | Cannot assess trends over time |
| Categorical columns (`category`, `region`, `buyer_returning`) were not summarized here | Frequency distributions for these are absent from this output |
| Cross-variable relationships are not assessed | Descriptive statistics cannot reveal associations between variables |

---

## 6. Validation Notes

- ✅ No duplicate rows detected
- ✅ All binary variables (`add_to_cart`, `purchased`) correctly bounded at 0–1
- ✅ `seller_rating` max does not exceed 5.0 — plausible scale ceiling
- ⚠️ `views` max = 1,000 — a suspiciously round number; verify whether this represents a data cap or a true observation
- ⚠️ `listing_age_days` max = 121 — verify whether listings older than ~90 days represent stale data, testing data, or legitimate long-running listings
- ⚠️ `shipping_price` min of 2.49 and max of 5.99 with values clustering at specific points — confirm whether these are platform-enforced shipping tiers

---

## 7. Recommended Follow-up

1. **Investigate `views` cap at 1,000** — Determine whether this is a platform-imposed ceiling or a genuine observation. If capped, consider this a censored variable.
2. **Analyze missingness in `seller_rating`** — Test whether missing ratings are associated with specific categories, regions, or purchase outcomes to assess non-random missingness.
3. **Frequency analysis of categorical columns** — Produce value counts and proportions for `category`, `region`, and `buyer_returning` to complete the dataset profile.
4. **Log-transform `views` and `listing_age_days`** — For any regression or modeling work, both right-skewed variables should be transformed or modeled with appropriate distributions.
5. **Treat `shipping_price` as ordinal or categorical** — Recode into tier labels before modeling.
6. **Compute conversion rates conditionally** — Examine add-to-cart and purchase rates segmented by `category`, `region`, and `buyer_returning` to identify meaningful subgroup differences.
7. **Restore and analyze `item_price`** — This variable was excluded from analysis but is likely central to marketplace behavior; its exclusion should be reviewed.

## Validation Notes

Status: pass

Warnings:

[]

## Limitations

This analysis summarizes dataset structure and numeric distributions. It does not test relationships, explain causes, or make predictions.

## Recommended Follow-up

Investigate variables with missing values, outliers, or skew before moving to correlation, hypothesis testing, or regression.
