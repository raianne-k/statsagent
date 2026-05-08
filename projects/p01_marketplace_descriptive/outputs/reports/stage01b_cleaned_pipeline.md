# Analysis Report

Generated: 2026-05-07 10:38:21

## Task

descriptive_stats

## Dataset Overview

- Rows: 1000
- Columns: 26
- Duplicate rows: 0
- Numeric columns: ['listing_id', 'seller_id', 'buyer_id', 'item_price', 'shipping_price', 'listing_age_days', 'views', 'likes', 'add_to_cart', 'purchased', 'seller_rating', 'add_to_cart_clean', 'purchased_clean', 'buyer_returning_clean']
- Categorical columns: ['category', 'buyer_returning', 'region', 'add_to_cart_invalid_flag', 'purchased_invalid_flag', 'buyer_returning_invalid_flag', 'seller_rating_missing_flag', 'item_price_invalid_flag', 'views_invalid_flag', 'listing_age_days_invalid_flag', 'likes_invalid_flag', 'seller_rating_invalid_flag']

## Missing Values

{'listing_id': 0, 'seller_id': 0, 'buyer_id': 0, 'category': 0, 'item_price': 0, 'shipping_price': 0, 'listing_age_days': 0, 'views': 0, 'likes': 0, 'add_to_cart': 0, 'purchased': 0, 'seller_rating': 70, 'buyer_returning': 0, 'region': 0, 'add_to_cart_invalid_flag': 0, 'purchased_invalid_flag': 0, 'buyer_returning_invalid_flag': 0, 'add_to_cart_clean': 0, 'purchased_clean': 0, 'buyer_returning_clean': 0, 'seller_rating_missing_flag': 0, 'item_price_invalid_flag': 0, 'views_invalid_flag': 0, 'listing_age_days_invalid_flag': 0, 'likes_invalid_flag': 0, 'seller_rating_invalid_flag': 0}

## Method Used

Descriptive statistics were computed using column-type classification. Variables were separated into continuous numeric, binary, low-cardinality numeric, and categorical types, with each analyzed using appropriate summary methods.

## Results

{'excluded_id_columns': ['listing_id', 'seller_id', 'buyer_id'], 'continuous_numeric_columns': ['item_price', 'listing_age_days', 'views', 'likes', 'seller_rating'], 'binary_columns': ['add_to_cart', 'purchased', 'add_to_cart_clean', 'purchased_clean', 'buyer_returning_clean'], 'low_cardinality_numeric_columns': ['shipping_price'], 'categorical_columns': ['category', 'buyer_returning', 'region', 'add_to_cart_invalid_flag', 'purchased_invalid_flag', 'buyer_returning_invalid_flag', 'seller_rating_missing_flag', 'item_price_invalid_flag', 'views_invalid_flag', 'listing_age_days_invalid_flag', 'likes_invalid_flag', 'seller_rating_invalid_flag'], 'summary': {'item_price': {'count': 1000.0, 'mean': 32.89, 'std': 29.32, 'min': 2.96, '25%': 15.7, '50%': 24.91, '75%': 39.55, 'max': 259.74}, 'listing_age_days': {'count': 1000.0, 'mean': 17.63, 'std': 17.55, 'min': 0.0, '25%': 5.0, '50%': 12.0, '75%': 25.0, 'max': 121.0}, 'views': {'count': 1000.0, 'mean': 46.69, 'std': 60.18, 'min': 2.0, '25%': 17.0, '50%': 30.0, '75%': 54.25, 'max': 1000.0}, 'likes': {'count': 1000.0, 'mean': 3.96, 'std': 1.87, 'min': 0.0, '25%': 3.0, '50%': 4.0, '75%': 5.0, 'max': 11.0}, 'seller_rating': {'count': 930.0, 'mean': 4.57, 'std': 0.32, 'min': 3.42, '25%': 4.36, '50%': 4.58, '75%': 4.82, 'max': 5.0}}, 'extra_stats': {'item_price': {'mean': np.float64(32.89), 'median': np.float64(24.91), 'variance': np.float64(859.67), 'iqr': np.float64(23.84), 'outlier_count': 59, 'outlier_percent': 5.9, 'mean_median_gap_percent': np.float64(32.05), 'skew_warning': np.True_, 'round_number_max_check': None}, 'listing_age_days': {'mean': np.float64(17.63), 'median': np.float64(12.0), 'variance': np.float64(307.84), 'iqr': np.float64(20.0), 'outlier_count': 45, 'outlier_percent': 4.5, 'mean_median_gap_percent': np.float64(46.89), 'skew_warning': np.True_, 'round_number_max_check': None}, 'views': {'mean': np.float64(46.69), 'median': np.float64(30.0), 'variance': np.float64(3621.95), 'iqr': np.float64(37.25), 'outlier_count': 79, 'outlier_percent': 7.9, 'mean_median_gap_percent': np.float64(55.64), 'skew_warning': np.True_, 'round_number_max_check': {'max_value': 1000.0, 'max_count': 1, 'possible_cap': False, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'likes': {'mean': np.float64(3.96), 'median': np.float64(4.0), 'variance': np.float64(3.51), 'iqr': np.float64(2.0), 'outlier_count': 9, 'outlier_percent': 0.9, 'mean_median_gap_percent': np.float64(1.12), 'skew_warning': np.False_, 'round_number_max_check': None}, 'seller_rating': {'mean': np.float64(4.57), 'median': np.float64(4.58), 'variance': np.float64(0.1), 'iqr': np.float64(0.46), 'outlier_count': 10, 'outlier_percent': 1.08, 'mean_median_gap_percent': np.float64(0.21), 'skew_warning': np.False_, 'round_number_max_check': None}}, 'binary_summary': {'add_to_cart': {'count': 1000, 'positive_count': 189, 'positive_rate_percent': 18.9, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'purchased': {'count': 1000, 'positive_count': 111, 'positive_rate_percent': 11.1, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'add_to_cart_clean': {'count': 1000, 'positive_count': 189, 'positive_rate_percent': 18.9, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'purchased_clean': {'count': 1000, 'positive_count': 111, 'positive_rate_percent': 11.1, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'buyer_returning_clean': {'count': 1000, 'positive_count': 554, 'positive_rate_percent': 55.4, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}}, 'low_cardinality_summary': {'shipping_price': {'unique_values': 5, 'values': {2.49: 186, 2.99: 197, 3.49: 196, 4.99: 221, 5.99: 200}, 'value_percent': {2.49: 18.6, 2.99: 19.7, 3.49: 19.6, 4.99: 22.1, 5.99: 20.0}, 'note': 'Low-cardinality numeric variable; verify whether this should be treated as categorical or ordinal.'}}, 'categorical_summary': {'category': {'count': 1000, 'missing': 0, 'unique_values': 6, 'mode': 'clothing', 'top_values': {'clothing': 341, 'shoes': 173, 'accessories': 163, 'bags': 122, 'home': 108, 'electronics': 93}, 'top_value_percent': {'clothing': 34.1, 'shoes': 17.3, 'accessories': 16.3, 'bags': 12.2, 'home': 10.8, 'electronics': 9.3}}, 'buyer_returning': {'count': 1000, 'missing': 0, 'unique_values': 2, 'mode': 'yes', 'top_values': {'yes': 554, 'no': 446}, 'top_value_percent': {'yes': 55.4, 'no': 44.6}}, 'region': {'count': 1000, 'missing': 0, 'unique_values': 5, 'mode': 'Tartu', 'top_values': {'Tartu': 218, 'Narva': 205, 'Other': 197, 'Tallinn': 194, 'Pärnu': 186}, 'top_value_percent': {'Tartu': 21.8, 'Narva': 20.5, 'Other': 19.7, 'Tallinn': 19.4, 'Pärnu': 18.6}}, 'add_to_cart_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'purchased_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'buyer_returning_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'seller_rating_missing_flag': {'count': 1000, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 930, True: 70}, 'top_value_percent': {False: 93.0, True: 7.0}}, 'item_price_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'views_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'listing_age_days_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'likes_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'seller_rating_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}}}

## Interpretation

# Descriptive Statistics Report
### Dataset: `marketplace_cleaned.csv` | 1,000 rows × 26 columns

---

## 1. Method Used

Standard descriptive statistics were computed on a pre-cleaned dataset (`marketplace_cleaned.csv`), meaning upstream data cleaning and validation had already been applied prior to this analysis. Columns were automatically classified into continuous numeric, binary, low-cardinality numeric, and categorical types. ID columns were excluded from analytical summaries. Binary variables were summarized as proportions rather than continuous distributions. Technical pipeline columns (flags and clean versions) were reserved for validation review only.

---

## 2. Key Results

### 🔢 Continuous Numeric Variables

| Variable | Mean | Median | IQR | Outlier % | Skew Warning |
|---|---|---|---|---|---|
| `item_price` | 32.89 | 24.91 | 23.84 | 5.9% | ⚠️ Yes |
| `listing_age_days` | 17.63 | 12.0 | 20.0 | 4.5% | ⚠️ Yes |
| `views` | 46.69 | 30.0 | 37.25 | 7.9% | ⚠️ Yes |
| `likes` | 3.96 | 4.0 | 2.0 | 0.9% | ✅ No |
| `seller_rating` | 4.57 | 4.58 | 0.46 | 1.08% | ✅ No |

**Notable flags:**
- `views` has a maximum value of **1,000** — a round number that warrants manual verification (see Validation Notes).
- `item_price`, `listing_age_days`, and `views` all show meaningful mean-median gaps (32%, 47%, and 56% respectively), indicating right-skewed distributions.

---

### ☑️ Binary Variables (Proportions)

| Variable | Positive Rate |
|---|---|
| `add_to_cart` | **18.9%** (189 / 1,000) |
| `purchased` | **11.1%** (111 / 1,000) |

---

### 📦 Low-Cardinality Numeric: `shipping_price`

`shipping_price` takes only **5 distinct values** (2.49, 2.99, 3.49, 4.99, 5.99), distributed fairly evenly across listings (18.6%–22.1% each). This pattern is consistent with a **fixed pricing tier structure** rather than a continuous pricing variable.

---

### 🏷️ Categorical Variables

**`category`** (6 values):
- Dominated by **clothing** (34.1%), followed by shoes (17.3%) and accessories (16.3%). Electronics is the smallest category (9.3%).

**`buyer_returning`** (2 values):
- **55.4%** of buyers are returning; **44.6%** are new. The split is moderately uneven but not extreme.

**`region`** (5 values):
- Listings are distributed fairly evenly across Tartu (21.8%), Narva (20.5%), Other (19.7%), Tallinn (19.4%), and Pärnu (18.6%). No strong regional concentration is present.

---

## 3. Interpretation

**Item price** shows a notable right skew — the mean (€32.89) is approximately 32% higher than the median (€24.91), suggesting a minority of high-priced listings is pulling the average upward. The median is likely a more representative measure of the typical listing price.

**Listing age and views** are similarly right-skewed. Most listings are relatively new (median: 12 days) and have moderate view counts (median: 30), but a tail of older, highly-viewed listings inflates the respective means. The 56% mean-median gap for `views` is the largest in the dataset and warrants attention.

**Likes and seller rating** are well-behaved and symmetrically distributed. Seller ratings cluster tightly (IQR: 0.46) around a median of 4.58 out of a presumed 5-point scale, suggesting most sellers in this dataset are rated highly with limited variation.

**Conversion funnel observation:** 18.9% of listings result in an add-to-cart event, and 11.1% result in a purchase. This implies that of all listings viewed, roughly **59% of add-to-cart events proceed to purchase** (111/189). This is an observational pattern only — no causal relationship between these variables can be concluded from descriptive statistics alone.

**Shipping price tiers** are evenly distributed, suggesting these may be pre-defined seller options rather than freely entered prices.

**Category imbalance** is present — clothing accounts for over a third of all listings, while electronics is underrepresented at under 10%. Any category-level comparisons should account for this imbalance.

---

## 4. Assumptions

- The dataset has already undergone cleaning; results reflect post-cleaning values.
- Binary variables (`add_to_cart`, `purchased`) are treated as event indicators, not ordinal or continuous measures.
- `shipping_price` is treated as a discrete tier variable rather than a continuous measure.
- `seller_rating` is assumed to operate on a 0–5 scale based on the observed range.

---

## 5. Limitations

- **Missing seller ratings:** 70 records (7.0%) have missing `seller_rating` values. Any analysis involving seller ratings applies only to the 930 complete records and may not be representative of all sellers.
- **Right-skewed distributions** in `item_price`, `listing_age_days`, and `views` reduce the usefulness of means as central tendency measures. Median and IQR are preferred for these variables.
- **No temporal context:** Listing age is available, but no absolute timestamps are provided, making trend analysis impossible from this data alone.
- **Category imbalance** limits comparability across product groups without weighting or stratification.
- **No relational linking:** While `seller_id` and `buyer_id` exist, they were excluded as ID columns. Seller- or buyer-level aggregations would require separate analysis.
- This is a single cross-sectional snapshot; no longitudinal or causal conclusions can be drawn.

---

## 6. Validation Notes

All technical pipeline columns were reviewed and are summarized here:

| Flag Column | Finding |
|---|---|
| `add_to_cart_invalid_flag` | 0 invalid records — clean ✅ |
| `purchased_invalid_flag` | 0 invalid records — clean ✅ |
| `buyer_returning_invalid_flag` | 0 invalid records — clean ✅ |
| `item_price_invalid_flag` | 0 invalid records — clean ✅ |
| `views_invalid_flag` | 0 invalid records — clean ✅ |
| `listing_age_days_invalid_flag` | 0 invalid records — clean ✅ |
| `likes_invalid_flag` | 0 invalid records — clean ✅ |
| `seller_rating_invalid_flag` | 0 invalid records (among non-missing) ✅ |
| `seller_rating_missing_flag` | **70 records flagged as missing (7.0%)** ⚠️ |

The `_clean` columns for `add_to_cart`, `purchased`, and `buyer_returning` matched their source columns — confirming no corrections were applied during cleaning for these fields.

**Round-number maximum — `views`:** The maximum value of 1,000 was automatically flagged. The pipeline assessed this as a possible but unconfirmed cap (`possible_cap: False`). Manual verification is recommended to confirm whether this represents a genuine observation or a data entry ceiling.

---

## 7. Recommended Follow-up

1. **Investigate the `views` maximum of 1,000** — confirm with the data source whether this is a true value or a platform-imposed cap.
2. **Assess missingness in `seller_rating`** — determine whether the 7% missing rate is random or systematic (e.g., new sellers, specific categories, or regions).
3. **Segment analysis by category** — given the strong skew toward clothing, stratified analysis would be more informative than aggregate comparisons.
4. **Explore the conversion funnel** — a follow-up analysis comparing `add_to_cart` and `purchased` rates across categories, regions, and price tiers could reveal meaningful patterns (without implying causation).
5. **Treat `shipping_price` as categorical or ordinal** in any regression or modeling work, given its discrete tier structure.
6. **Consider median-based reporting** for `item_price`, `listing_age_days`, and `views` in any executive or operational summaries, given their right-skewed distributions.
