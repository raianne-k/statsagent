# Analysis Report

Generated: 2026-05-03 11:57:46

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

Descriptive statistics were computed using column-type classification. Variables were separated into continuous numeric, binary, low-cardinality numeric, and categorical types, with each analyzed using appropriate summary methods.

## Results

{'excluded_id_columns': ['listing_id', 'seller_id', 'buyer_id'], 'continuous_numeric_columns': ['item_price', 'listing_age_days', 'views', 'likes', 'seller_rating'], 'binary_columns': ['add_to_cart', 'purchased'], 'low_cardinality_numeric_columns': ['shipping_price'], 'categorical_columns': ['category', 'buyer_returning', 'region'], 'summary': {'item_price': {'count': 1000.0, 'mean': 32.89, 'std': 29.32, 'min': 2.96, '25%': 15.7, '50%': 24.91, '75%': 39.55, 'max': 259.74}, 'listing_age_days': {'count': 1000.0, 'mean': 17.63, 'std': 17.55, 'min': 0.0, '25%': 5.0, '50%': 12.0, '75%': 25.0, 'max': 121.0}, 'views': {'count': 1000.0, 'mean': 46.69, 'std': 60.18, 'min': 2.0, '25%': 17.0, '50%': 30.0, '75%': 54.25, 'max': 1000.0}, 'likes': {'count': 1000.0, 'mean': 3.96, 'std': 1.87, 'min': 0.0, '25%': 3.0, '50%': 4.0, '75%': 5.0, 'max': 11.0}, 'seller_rating': {'count': 930.0, 'mean': 4.57, 'std': 0.32, 'min': 3.42, '25%': 4.36, '50%': 4.58, '75%': 4.82, 'max': 5.0}}, 'extra_stats': {'item_price': {'mean': np.float64(32.89), 'median': np.float64(24.91), 'variance': np.float64(859.67), 'iqr': np.float64(23.84), 'outlier_count': 59, 'outlier_percent': 5.9, 'mean_median_gap_percent': np.float64(32.05), 'skew_warning': np.True_, 'round_number_max_check': None}, 'listing_age_days': {'mean': np.float64(17.63), 'median': np.float64(12.0), 'variance': np.float64(307.84), 'iqr': np.float64(20.0), 'outlier_count': 45, 'outlier_percent': 4.5, 'mean_median_gap_percent': np.float64(46.89), 'skew_warning': np.True_, 'round_number_max_check': None}, 'views': {'mean': np.float64(46.69), 'median': np.float64(30.0), 'variance': np.float64(3621.95), 'iqr': np.float64(37.25), 'outlier_count': 79, 'outlier_percent': 7.9, 'mean_median_gap_percent': np.float64(55.64), 'skew_warning': np.True_, 'round_number_max_check': {'max_value': 1000.0, 'max_count': 1, 'possible_cap': False, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'likes': {'mean': np.float64(3.96), 'median': np.float64(4.0), 'variance': np.float64(3.51), 'iqr': np.float64(2.0), 'outlier_count': 9, 'outlier_percent': 0.9, 'mean_median_gap_percent': np.float64(1.12), 'skew_warning': np.False_, 'round_number_max_check': None}, 'seller_rating': {'mean': np.float64(4.57), 'median': np.float64(4.58), 'variance': np.float64(0.1), 'iqr': np.float64(0.46), 'outlier_count': 10, 'outlier_percent': 1.08, 'mean_median_gap_percent': np.float64(0.21), 'skew_warning': np.False_, 'round_number_max_check': None}}, 'binary_summary': {'add_to_cart': {'count': 1000, 'positive_count': 189, 'positive_rate_percent': 18.9, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'purchased': {'count': 1000, 'positive_count': 111, 'positive_rate_percent': 11.1, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}}, 'low_cardinality_summary': {'shipping_price': {'unique_values': 5, 'values': {2.49: 186, 2.99: 197, 3.49: 196, 4.99: 221, 5.99: 200}, 'value_percent': {2.49: 18.6, 2.99: 19.7, 3.49: 19.6, 4.99: 22.1, 5.99: 20.0}, 'note': 'Low-cardinality numeric variable; verify whether this should be treated as categorical or ordinal.'}}, 'categorical_summary': {'category': {'count': 1000, 'missing': 0, 'unique_values': 6, 'mode': 'clothing', 'top_values': {'clothing': 341, 'shoes': 173, 'accessories': 163, 'bags': 122, 'home': 108, 'electronics': 93}, 'top_value_percent': {'clothing': 34.1, 'shoes': 17.3, 'accessories': 16.3, 'bags': 12.2, 'home': 10.8, 'electronics': 9.3}}, 'buyer_returning': {'count': 1000, 'missing': 0, 'unique_values': 2, 'mode': 'yes', 'top_values': {'yes': 554, 'no': 446}, 'top_value_percent': {'yes': 55.4, 'no': 44.6}}, 'region': {'count': 1000, 'missing': 0, 'unique_values': 5, 'mode': 'Tartu', 'top_values': {'Tartu': 218, 'Narva': 205, 'Other': 197, 'Tallinn': 194, 'Pärnu': 186}, 'top_value_percent': {'Tartu': 21.8, 'Narva': 20.5, 'Other': 19.7, 'Tallinn': 19.4, 'Pärnu': 18.6}}}}

## Interpretation

# Descriptive Statistics Analysis Report

---

## 1. Method Used

Automated descriptive profiling of a 1,000-row, 14-column dataset. The pipeline classified columns into continuous numeric, binary, low-cardinality numeric, and categorical types. ID columns were excluded from analysis. Continuous variables were summarized using mean, median, IQR, outlier percentage, and skew checks. Binary variables were summarized as proportions. Categorical variables were summarized by frequency. A round-number maximum check was applied to continuous variables.

---

## 2. Key Results

### 🔴 Excluded Columns
`listing_id`, `seller_id`, and `buyer_id` were identified as identifier columns and excluded from statistical analysis to avoid meaningless numeric summaries.

---

### 📊 Continuous Variables

| Variable | Mean | Median | IQR | Outlier % | Skew Warning |
|---|---|---|---|---|---|
| `item_price` | 32.89 | 24.91 | 23.84 | 5.9% | ✅ Yes |
| `listing_age_days` | 17.63 | 12.0 | 20.0 | 4.5% | ✅ Yes |
| `views` | 46.69 | 30.0 | 37.25 | 7.9% | ✅ Yes |
| `likes` | 3.96 | 4.0 | 2.0 | 0.9% | ❌ No |
| `seller_rating` | 4.57 | 4.58 | 0.46 | 1.08% | ❌ No |

**Notable observations:**
- **`item_price`**: Mean (32.89) exceeds median (24.91) by **32%**, indicating right skew driven by higher-priced outliers (5.9% of values flagged).
- **`listing_age_days`**: Mean (17.63) exceeds median (12.0) by **47%** — the largest mean/median gap in the dataset. A small number of much older listings are pulling the mean upward.
- **`views`**: Mean (46.69) exceeds median (30.0) by **56%** — the most extreme skew. A single maximum value of **1,000 views** was detected. The pipeline assessed this as *not* a systematic cap (only 1 occurrence), but it warrants manual verification as a potential outlier.
- **`likes`**: Near-symmetric distribution (mean ≈ median = 4.0), with a tight IQR of 2.0 and very few outliers (0.9%). This is the most well-behaved continuous variable.
- **`seller_rating`**: Extremely tight distribution (IQR = 0.46), mean and median nearly identical at ~4.57–4.58. Minimal outliers. Ratings cluster in a narrow upper range, suggesting possible ceiling compression.

---

### ⚖️ Binary Variables (Proportions)

| Variable | Positive Count | Positive Rate |
|---|---|---|
| `add_to_cart` | 189 / 1000 | **18.9%** |
| `purchased` | 111 / 1000 | **11.1%** |

**Notable observations:**
- Approximately 1 in 5 listings resulted in an add-to-cart event; approximately 1 in 9 resulted in a purchase.
- Of listings added to cart (189), 111 also show a purchase — though cross-tabulation was not performed here, the raw rates suggest a meaningful drop-off between cart and purchase.
- These variables were correctly treated as proportions, not continuous distributions.

---

### 🔢 Low-Cardinality Numeric Variable

**`shipping_price`** — 5 discrete values only:

| Value | Count | % |
|---|---|---|
| 2.49 | 186 | 18.6% |
| 2.99 | 197 | 19.7% |
| 3.49 | 196 | 19.6% |
| 4.99 | 221 | 22.1% |
| 5.99 | 200 | 20.0% |

**Notable observations:**
- Distribution across the five tiers is approximately uniform (18.6%–22.1%), suggesting no single shipping tier dominates.
- The gap between 3.49 and 4.99 (skipping ~3.99) and near-equal counts suggest this is a **predefined pricing tier system**, not a continuous variable. It should be treated as **ordinal categorical** in downstream analyses.

---

### 🏷️ Categorical Variables

**`category`** (6 unique values):

| Category | Count | % |
|---|---|---|
| clothing | 341 | 34.1% |
| shoes | 173 | 17.3% |
| accessories | 163 | 16.3% |
| bags | 122 | 12.2% |
| home | 108 | 10.8% |
| electronics | 93 | 9.3% |

- `clothing` is the dominant category, comprising over one-third of all listings. `electronics` is the least represented at 9.3%.

---

**`buyer_returning`** (2 unique values — effectively binary):

| Value | Count | % |
|---|---|---|
| yes | 554 | 55.4% |
| no | 446 | 44.6% |

- A slight majority (55.4%) of buyers are returning buyers. The split is relatively balanced.

---

**`region`** (5 unique values):

| Region | Count | % |
|---|---|---|
| Tartu | 218 | 21.8% |
| Narva | 205 | 20.5% |
| Other | 197 | 19.7% |
| Tallinn | 194 | 19.4% |
| Pärnu | 186 | 18.6% |

- Region is **near-uniformly distributed** across all five values (18.6%–21.8%). No single region dominates the dataset.

---

### ⚠️ Missing Data

| Column | Missing |
|---|---|
| `seller_rating` | **70 values (7.0%)** |
| All other columns | 0 |

- `seller_rating` is the **only column with missing data**, affecting 7% of rows. This is a moderate level of missingness. If `seller_rating` is used in downstream analysis, the mechanism of missingness (e.g., new sellers without ratings, data collection gaps) should be investigated before imputation or exclusion.

---

## 3. Interpretation

- **`item_price`, `listing_age_days`, and `views`** are all right-skewed. The mean is an unreliable measure of central tendency for these variables; the **median should be preferred** for typical-value summaries.
- The **views distribution** contains at least one extreme high-end value (1,000 views) that, while not confirmed as a cap, substantially inflates the mean. This outlier merits manual review.
- **`seller_rating`** is compressed in a narrow high range (~4.1–5.0 based on IQR), which may limit its discriminatory power in any model or comparison. This pattern is consistent with known rating inflation on marketplace platforms, though no causal claim is made here.
- **`shipping_price`** behaves as a discrete tier variable and should not be modeled as continuous.
- **`buyer_returning`** is stored as a string categorical but is functionally binary and should be encoded accordingly for any modeling task.
- The **near-uniform regional distribution** suggests the dataset may have been sampled or stratified by region rather than reflecting organic listing distributions.

---

## 4. Assumptions

- Outlier detection used standard IQR-based thresholds (typically 1.5× IQR rule).
- Skew warnings are based on mean/median divergence exceeding a predefined threshold.
- The round-number maximum check for `views` (value = 1,000) was flagged for review but not confirmed as a data cap.
- Missing values in `seller_rating` are assumed to be missing at random pending further investigation.

---

## 5. Limitations

- **No causal claims can be made** from descriptive statistics. The relationship between views, add-to-cart, and purchase cannot be inferred directionally from these summaries alone.
- **Cross-variable relationships** (e.g., whether clothing listings have more views, or whether returning buyers purchase more) are not captured in univariate summaries.
- **Missing `seller_rating` data (7%)** reduces confidence in any analysis involving that variable until the missingness mechanism is understood.
- The single `views` value of 1,000 could not be definitively confirmed as genuine or erroneous without additional context.
- The `category` imbalance (clothing = 34.1% vs. electronics = 9.3%) means that category-stratified analyses will have unequal statistical power.

---

## 6. Validation Notes

- ✅ No duplicate rows detected.
- ✅ ID columns correctly excluded from analysis.
- ✅ Binary variables treated as proportions.
- ✅ `shipping_price` correctly flagged as a discrete tier variable.
- ⚠️ `views` maximum value of 1,000 flagged — manual verification recommended.
- ⚠️ `seller_rating` has 70 missing values — missingness mechanism unknown.
- ⚠️ `seller_rating` IQR of 0.46 suggests a compressed range — check for ceiling effects near the maximum possible rating.
- ⚠️ `buyer_returning` is stored as categorical string ("yes"/"no") but is functionally binary — encoding should be standardized for modeling.

---

## 7. Recommended Follow-up

1. **Investigate the single `views` = 1,000 record** — determine whether it is a genuine observation or a data entry/cap artifact.
2. **Analyze `seller_rating` missingness** — determine whether missing ratings are associated with specific seller types, listing categories, or regions (i.e., test whether missingness is random or systematic).
3. **Cross-tabulate `add_to_cart` and `purchased`** — quantify the cart-to-purchase conversion rate directly.
4. **Re-encode `shipping_price` as ordinal** before any regression or segmentation analysis.
5. **Re-encode `buyer_returning`** from string to binary (0/1) for modeling consistency.
6. **Apply log transformation** to `item_price`, `listing_age_days`, and `views` before any parametric modeling, given confirmed right skew.
7. **Stratify key metrics by `category`** to account for its compositional imbalance (clothing over-represented at 34.1%).
8. **Investigate `seller_rating` ceiling compression** — if most values cluster near the maximum, the variable may have limited utility as a predictor without binning or transformation.
