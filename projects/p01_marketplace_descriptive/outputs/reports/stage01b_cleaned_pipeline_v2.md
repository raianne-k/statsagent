# Analysis Report

Generated: 2026-05-07 11:03:40

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

Descriptive statistics were computed using column-type classification. Variables were separated into continuous numeric, binary, low-cardinality numeric, categorical, and technical pipeline columns.

Technical columns such as `_clean`, `_invalid_flag`, and `_missing_flag` are excluded from primary analytical interpretation and reserved for validation notes.

## Results

{'excluded_id_columns': ['listing_id', 'seller_id', 'buyer_id'], 'continuous_numeric_columns': ['item_price', 'listing_age_days', 'views', 'likes', 'seller_rating'], 'binary_columns': ['add_to_cart', 'purchased'], 'low_cardinality_numeric_columns': ['shipping_price'], 'categorical_columns': ['category', 'buyer_returning', 'region'], 'technical_columns': ['add_to_cart_invalid_flag', 'purchased_invalid_flag', 'buyer_returning_invalid_flag', 'add_to_cart_clean', 'purchased_clean', 'buyer_returning_clean', 'seller_rating_missing_flag', 'item_price_invalid_flag', 'views_invalid_flag', 'listing_age_days_invalid_flag', 'likes_invalid_flag', 'seller_rating_invalid_flag'], 'summary': {'item_price': {'count': 1000.0, 'mean': 32.89, 'std': 29.32, 'min': 2.96, '25%': 15.7, '50%': 24.91, '75%': 39.55, 'max': 259.74}, 'listing_age_days': {'count': 1000.0, 'mean': 17.63, 'std': 17.55, 'min': 0.0, '25%': 5.0, '50%': 12.0, '75%': 25.0, 'max': 121.0}, 'views': {'count': 1000.0, 'mean': 46.69, 'std': 60.18, 'min': 2.0, '25%': 17.0, '50%': 30.0, '75%': 54.25, 'max': 1000.0}, 'likes': {'count': 1000.0, 'mean': 3.96, 'std': 1.87, 'min': 0.0, '25%': 3.0, '50%': 4.0, '75%': 5.0, 'max': 11.0}, 'seller_rating': {'count': 930.0, 'mean': 4.57, 'std': 0.32, 'min': 3.42, '25%': 4.36, '50%': 4.58, '75%': 4.82, 'max': 5.0}}, 'extra_stats': {'item_price': {'mean': np.float64(32.89), 'median': np.float64(24.91), 'variance': np.float64(859.67), 'iqr': np.float64(23.84), 'outlier_count': 59, 'outlier_percent': 5.9, 'mean_median_gap_percent': np.float64(32.05), 'skew_warning': np.True_, 'round_number_max_check': None}, 'listing_age_days': {'mean': np.float64(17.63), 'median': np.float64(12.0), 'variance': np.float64(307.84), 'iqr': np.float64(20.0), 'outlier_count': 45, 'outlier_percent': 4.5, 'mean_median_gap_percent': np.float64(46.89), 'skew_warning': np.True_, 'round_number_max_check': None}, 'views': {'mean': np.float64(46.69), 'median': np.float64(30.0), 'variance': np.float64(3621.95), 'iqr': np.float64(37.25), 'outlier_count': 79, 'outlier_percent': 7.9, 'mean_median_gap_percent': np.float64(55.64), 'skew_warning': np.True_, 'round_number_max_check': {'max_value': 1000.0, 'max_count': 1, 'possible_cap': False, 'note': 'Round-number maximum detected; verify whether this is a genuine value or a cap.'}}, 'likes': {'mean': np.float64(3.96), 'median': np.float64(4.0), 'variance': np.float64(3.51), 'iqr': np.float64(2.0), 'outlier_count': 9, 'outlier_percent': 0.9, 'mean_median_gap_percent': np.float64(1.12), 'skew_warning': np.False_, 'round_number_max_check': None}, 'seller_rating': {'mean': np.float64(4.57), 'median': np.float64(4.58), 'variance': np.float64(0.1), 'iqr': np.float64(0.46), 'outlier_count': 10, 'outlier_percent': 1.08, 'mean_median_gap_percent': np.float64(0.21), 'skew_warning': np.False_, 'round_number_max_check': None}}, 'binary_summary': {'add_to_cart': {'count': 1000, 'positive_count': 189, 'positive_rate_percent': 18.9, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}, 'purchased': {'count': 1000, 'positive_count': 111, 'positive_rate_percent': 11.1, 'note': 'Binary variable summarized as proportion, not continuous distribution.'}}, 'low_cardinality_summary': {'shipping_price': {'unique_values': 5, 'values': {2.49: 186, 2.99: 197, 3.49: 196, 4.99: 221, 5.99: 200}, 'value_percent': {2.49: 18.6, 2.99: 19.7, 3.49: 19.6, 4.99: 22.1, 5.99: 20.0}, 'note': 'Low-cardinality numeric variable; verify whether this should be treated as categorical or ordinal.'}}, 'categorical_summary': {'category': {'count': 1000, 'missing': 0, 'unique_values': 6, 'mode': 'clothing', 'top_values': {'clothing': 341, 'shoes': 173, 'accessories': 163, 'bags': 122, 'home': 108, 'electronics': 93}, 'top_value_percent': {'clothing': 34.1, 'shoes': 17.3, 'accessories': 16.3, 'bags': 12.2, 'home': 10.8, 'electronics': 9.3}}, 'buyer_returning': {'count': 1000, 'missing': 0, 'unique_values': 2, 'mode': 'yes', 'top_values': {'yes': 554, 'no': 446}, 'top_value_percent': {'yes': 55.4, 'no': 44.6}}, 'region': {'count': 1000, 'missing': 0, 'unique_values': 5, 'mode': 'Tartu', 'top_values': {'Tartu': 218, 'Narva': 205, 'Other': 197, 'Tallinn': 194, 'Pärnu': 186}, 'top_value_percent': {'Tartu': 21.8, 'Narva': 20.5, 'Other': 19.7, 'Tallinn': 19.4, 'Pärnu': 18.6}}}, 'technical_summary': {'add_to_cart_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'purchased_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'buyer_returning_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'seller_rating_missing_flag': {'count': 1000, 'missing': 0, 'unique_values': 2, 'mode': np.False_, 'top_values': {False: 930, True: 70}, 'top_value_percent': {False: 93.0, True: 7.0}}, 'item_price_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'views_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'listing_age_days_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'likes_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}, 'seller_rating_invalid_flag': {'count': 1000, 'missing': 0, 'unique_values': 1, 'mode': np.False_, 'top_values': {False: 1000}, 'top_value_percent': {False: 100.0}}}}

## Interpretation

# Descriptive Statistics Report
### Dataset: `marketplace_cleaned.csv` — 1,000 rows × 26 columns

> **Note:** This dataset has been pre-processed through a cleaning pipeline prior to analysis. Results reflect the cleaned version of the data. Three identifier columns (`listing_id`, `seller_id`, `buyer_id`) were excluded from all analytical summaries.

---

## 1. Method Used

Standard descriptive statistics were computed across all non-identifier columns, with variables classified into five groups: continuous numeric, binary, low-cardinality numeric, categorical, and technical/pipeline columns. Binary variables were summarized as proportions. Skew warnings were triggered when the mean/median gap exceeded a defined threshold. Outlier percentages were calculated using IQR-based fencing.

---

## 2. Key Results

### 📦 Continuous Numeric Variables

| Variable | Mean | Median | IQR | Outlier % | Skew Warning |
|---|---|---|---|---|---|
| `item_price` | £32.89 | £24.91 | £23.84 | 5.9% | ✅ Yes |
| `listing_age_days` | 17.63 | 12.0 | 20.0 | 4.5% | ✅ Yes |
| `views` | 46.69 | 30.0 | 37.25 | 7.9% | ✅ Yes |
| `likes` | 3.96 | 4.0 | 2.0 | 0.9% | ❌ No |
| `seller_rating` | 4.57 | 4.58 | 0.46 | 1.08% | ❌ No |

**Item Price** — The mean (£32.89) exceeds the median (£24.91) by approximately **32%**, indicating a right-skewed distribution. A minority of high-priced listings are pulling the mean upward. 5.9% of values are flagged as outliers.

**Listing Age (Days)** — The most pronounced skew in the dataset: mean (17.63 days) is nearly **47% higher** than the median (12.0 days). The majority of listings are relatively fresh, but a long tail of older listings exists.

**Views** — The widest mean/median gap at **~56%** (mean: 46.69, median: 30.0). A small number of high-traffic listings are substantially raising the average. The maximum value of **1,000 views** (single occurrence) triggered a round-number check — while the pipeline did not flag it as a definitive cap, it warrants manual verification. Outlier rate of 7.9% is the highest across all continuous variables.

**Likes** — Tightly distributed around a median and mean of ~4, with low IQR (2.0) and negligible skew. This variable appears to behave more like a discrete tier than a broadly continuous measure.

**Seller Rating** — Highly concentrated: mean 4.57, median 4.58, IQR of only 0.46. This suggests most sellers in this dataset cluster in a narrow high-rating band. Very few outliers (1.08%).

---

### 🔘 Binary Variables (Proportions)

| Variable | Positive Rate |
|---|---|
| `add_to_cart` | **18.9%** (189 / 1,000) |
| `purchased` | **11.1%** (111 / 1,000) |

- Approximately 1 in 5 listings resulted in an add-to-cart event.
- Approximately 1 in 9 listings resulted in a purchase.
- The gap between add-to-cart (18.9%) and purchase (11.1%) suggests that not all cart additions convert to purchases, though the relationship between these events cannot be inferred directionally from descriptive statistics alone.

---

### 🔢 Low-Cardinality Numeric Variable

**Shipping Price** — Takes exactly **5 discrete values**: £2.49, £2.99, £3.49, £4.99, and £5.99. Distribution across tiers is notably even (18.6%–22.1%), suggesting this is a structured pricing tier system rather than a continuous variable. It should be treated as **ordinal or categorical** in downstream analysis.

---

### 🏷️ Categorical Variables

**Category** — Six product categories present. `clothing` dominates at **34.1%** (341 listings), followed by `shoes` (17.3%), `accessories` (16.3%), `bags` (12.2%), `home` (10.8%), and `electronics` (9.3%). The dataset is notably skewed toward fashion-related categories.

**Buyer Returning** — Slight majority of buyers are returning customers: **55.4% yes** vs. 44.6% no. The split is relatively balanced.

**Region** — Five regions represented with near-uniform distribution: Tartu (21.8%), Narva (20.5%), Other (19.7%), Tallinn (19.4%), and Pärnu (18.6%). No region dominates, suggesting either genuine geographic balance or a stratified sampling design.

---

## 3. Interpretation

- **Item price, views, and listing age** are all right-skewed, meaning median-based measures are more representative of typical values than means for these variables.
- The **views distribution** is particularly dispersed, with a small number of high-visibility listings coexisting with a long tail of low-visibility ones. The single 1,000-view data point is notable and should be confirmed as a genuine observation.
- **Seller ratings are compressed** near the top of the scale, which limits their discriminating power in any downstream analysis.
- The **conversion gap** between add-to-cart (18.9%) and purchase (11.1%) is descriptively notable, though no causal conclusion can be drawn from these proportions alone.
- **Shipping price tiers** are evenly distributed, which may reflect a controlled experimental or platform-level design decision.
- The category composition is heavily weighted toward fashion (clothing, shoes, accessories, bags account for ~80% of listings), which should be considered when generalizing findings.

---

## 4. Assumptions

- The cleaned dataset is assumed to reflect the intended analytical population after pipeline transformations.
- Binary variables (`add_to_cart`, `purchased`) are assumed to represent listing-level events, not user-level aggregates.
- `buyer_returning` is assumed to be a reliable self-reported or system-inferred flag.
- Seller ratings are assumed to be valid scores on a bounded scale, even after the 70 missing values are accounted for.

---

## 5. Limitations

- **Missing seller ratings (70 / 1,000 = 7%)** reduce the reliability of seller_rating summaries. The distribution may be biased if missing ratings are non-random (e.g., new sellers with no ratings yet).
- **Skewed distributions** for price, views, and listing age mean that mean values are unrepresentative of typical listings. Comparisons using means could be misleading.
- **Seller rating compression** (tight IQR of 0.46) means this variable may have limited analytical utility without additional segmentation.
- **No temporal data** is available in this snapshot; listing age is included, but trends over time cannot be assessed.
- The **"Other" region bucket** (19.7%) aggregates an unknown set of locations, which limits geographic granularity.
- Descriptive statistics do not support causal inference. This analysis cannot determine why purchases, cart additions, or views occur.

---

## 6. Validation Notes

All technical pipeline flags were reviewed and are summarized here:

| Flag Column | Summary |
|---|---|
| `add_to_cart_invalid_flag` | 0 invalid values detected (100% clean) |
| `purchased_invalid_flag` | 0 invalid values detected (100% clean) |
| `buyer_returning_invalid_flag` | 0 invalid values detected (100% clean) |
| `item_price_invalid_flag` | 0 invalid values detected (100% clean) |
| `views_invalid_flag` | 0 invalid values detected (100% clean) |
| `listing_age_days_invalid_flag` | 0 invalid values detected (100% clean) |
| `likes_invalid_flag` | 0 invalid values detected (100% clean) |
| `seller_rating_invalid_flag` | 0 invalid values detected (valid where present) |
| `seller_rating_missing_flag` | **70 rows flagged as missing (7.0%)** |

- All `_clean` columns passed validation (matching their originals); no corrections were applied post-flag.
- The only active data quality concern is the **70 missing seller ratings**, confirmed by the missing flag.
- The views maximum of 1,000 did not trigger an automatic cap flag but should be manually confirmed.

---

## 7. Recommended Follow-up

1. **Investigate missing seller ratings** — Determine whether missingness correlates with seller age, category, or purchase outcomes before including `seller_rating` in comparative analysis.
2. **Verify the 1,000-view listing** — Confirm whether this is a genuine outlier or a system-imposed cap value. If capped, views analysis will underestimate true engagement for top listings.
3. **Segment by category** — Given the dominance of clothing (34%), split key metrics (price, views, conversion) by category to avoid fashion-specific patterns distorting overall results.
4. **Treat shipping_price as categorical/ordinal** — Do not use it as a continuous variable in regression or correlation analysis.
5. **Use median instead of mean** for `item_price`, `views`, and `listing_age_days` in any summary reporting or segmentation, given confirmed right skew.
6. **Explore add-to-cart vs. purchase overlap** — A crosstab or funnel analysis would clarify how often cart additions lead to purchases without making causal assumptions.

## Validation

"validation_status": "pass_after_human_review",
"validation_warnings": [],
"human_review_notes": [
  "Validator flagged causal term 'drives'. Human reviewer confirmed wording was revised to remove causal implication."
]

## Governance Note

This report was generated by StatsAgent as an AI-assisted analytical output.

The report is intended for analytical support and validation purposes. Outputs should be reviewed by a human analyst before operational, financial, customer-impacting, or business-critical use.

Raw row-level data is not required for interpretation; the LLM interpretation layer should receive compact statistical summaries where possible.
