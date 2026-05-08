# Marketplace Descriptive Analysis
**Project:** 01_marketplace_descriptive
**Stage:** S01B — Cleaning, Validation & Descriptive Analysis

---

> **Dataset note:** This project uses a synthetic but intentionally realistic marketplace dataset, built for portfolio. Some patterns may reflect deliberate simulation logic rather than organic business behavior. That distinction is flagged where relevant throughout.

---

## 01 Stage goals

Cleaning, validation, statistical profiling, and visual review before drawing any conclusions.
Flag where averages or metrics could be misleading.
Finalizing a report of the stage for this project.

---

## Main Findings

### 1. Concentrated visibility

The `views` distribution is right-skewed. Visibility isn't distributed evenly across the marketplace.

| Metric | Value |
|---|---|
| Mean | 46.69 |
| Median | 30.0 |
| Gap | ~56% |
| Outlier rate | 7.9% |
| Max | 1,000 |

*(What drives visibility differences would be addressed in next steps)*

---

### 2. Medians over means

Three variables show the same right-skew pattern. Means are inflated by high-end values in each case.

| Variable | Mean | Median | Gap |
|---|---|---|---|
| `item_price` | 32.89 | 24.91 | 32% |
| `listing_age_days` | 17.63 | 12.0 | 47% |
| `views` | 46.69 | 30.0 | 56% |

Any reporting on this dataset should default to medians, IQR, and percentiles. Averages consistently overstate what a typical listing looks like.

---

### 3. Shipping price is a tier structure

`shipping_price` takes exactly five values: 2.49 / 2.99 / 3.49 / 4.99 / 5.99 — distributed almost evenly across listings.

Should be treated as ordinal/categorical downstream, not continuous.

> *May partly reflect dataset generation logic. Standardized shipping tiers are also common in real marketplaces.*

---

### 4. Seller ratings — ceiling effect

| Metric | Value |
|---|---|
| Mean | 4.57 |
| Median | 4.58 |
| IQR | 0.46 |

Everything clusters near the top. Low variation means low analytical value as a standalone feature.

> *Compression may reflect simplified simulation logic.*

---

### 5. Marketplace is mostly fashion

| Category | Share |
|---|---|
| Clothing | 34.1% |
| Shoes | 17.3% |
| Accessories | 16.3% |
| Bags | 12.2% |

~80% of listings across four fashion categories. Aggregate marketplace metrics here largely describe fashion-market behavior. Category-level segmentation will be necessary before drawing broader conclusions.

---

### 6. Conversion funnel drop-off

| Metric | Value |
|---|---|
| Add-to-cart rate | 18.9% |
| Purchase rate | 11.1% |

~41% of add-to-cart events don't result in a purchase. Most operationally interesting finding in this stage — worth investigating further.

*(No behavioral or intent data here. The finding is only that the gap exists.)*

---

## Overall

Dataset is clean and suitable for continued work.

Key structural notes to carry forward:
- Skewed visibility with clear concentration effects
- Means unreliable across key variables — use medians
- Shipping price is a categorical tier variable
- Seller ratings compressed near ceiling
- Heavy category skew toward fashion
- Measurable cart-to-purchase attrition

---

## Next step — Segmentation analysis

Likely dimensions:
- Product category
- Visibility tier
- Price tier
- Shipping tier
- Engagement bands
- Returning vs. new buyers

---

*AI-assisted workflow with human validation and review. Portfolio and exploratory use only.*
