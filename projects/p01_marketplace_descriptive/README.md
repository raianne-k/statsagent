# Marketplace Descriptive Statistics Validation Pipeline

**Role:** Data Analytics / Analytics Engineering  
**Domain:** Marketplace / E-commerce  
**Tools:** Python (Pandas, Matplotlib), LLM (Claude), Custom Validation Layer  
**Dataset:** Synthetic marketplace listings  

## Overview

This project demonstrates the descriptive statistics, validation, and cleaning capabilities of StatsAgent using a synthetic marketplace dataset.

The goal is not only to produce descriptive statistics, but to create outputs that are:

- methodologically correct  
- interpretable  
- reproducible  
- safe for downstream analysis  

Pipeline:

- classify variables by type  
- apply different statistical logic depending on the variable structure  
- validate outputs through structured review  
- track issues and fixes across runs  
- produce a cleaned analytical dataset for future modules  

---

## Analytical Goal

The purpose of this project is to answer:

> What does the marketplace dataset look like, and is it reliable enough for further analysis?

---

## Why This Matters

Marketplace datasets often contain a mix of:

- behavioral metrics  
- engagement metrics  
- categorical marketplace structure  
- product pricing variables  
- seller quality indicators  

```text
- binary variables treated as continuous create false outliers  
- ID columns included in numeric analysis create meaningless statistics  
- tier-based prices can be mistaken for continuous variables  
- missing seller ratings may bias seller-quality analysis  
- imbalanced categories can distort comparisons  
```

This project focuses on preventing those issues before moving into deeper analytical stages.

---

## Pipeline Structure

The pipeline currently has four layers:

### 1. Profiling & Variable Classification

The statistical engine first identifies variable structure:

- continuous variables  
- binary variables  
- categorical variables  
- ID columns  
- low-cardinality numeric variables  

This determines which calculations are appropriate for each field.

---

### 2. Descriptive Statistics

The pipeline computes summaries appropriate to the variable type.

Examples:

- mean, median, quartiles, IQR  
- skew detection  
- outlier detection for continuous variables only  
- proportions for binary variables  
- value counts and shares for categorical variables  

The focus is not only on computing statistics, but on making sure the statistics are analytically meaningful.

---

### 3. Validation Layer

The validation layer tracks analytical issues discovered during review.

Issues are logged as DS-01 → DS-07 and converted into:

- tool-level fixes  
- interpretation constraints  
- future validation checks  

Examples include:

- binary variables incorrectly treated as continuous  
- ID columns included in numeric analysis  
- categorical variables ignored  
- suspicious maximum values not verified  
- tier-based variables treated as continuous  

---

### 4. Cleaning & Analytical Dataset Construction

This stage extends the descriptive pipeline by creating an analysis-ready dataset.

The goal is not to make the data “perfect”, but to apply documented and reproducible cleaning rules before future analysis.

Cleaning rules currently include:

- preserving ID columns while excluding them from analysis  
- validating binary fields as 0/1 variables  
- treating shipping price as a tiered categorical variable  
- flagging missing seller ratings instead of blindly imputing them  
- checking impossible numeric values (negative prices, views, etc.)  
- removing exact duplicate rows only when justified  
- logging all transformations  

This creates a cleaner analytical baseline for future modules.

---

## Final Outputs

- validated descriptive report  
- validation log  
- cleaning log  
- analytical plots  
- cleaned analytical dataset  

---

## Key Findings

The final descriptive analysis identified several important patterns:

- `item_price`, `views`, and `listing_age_days` are strongly right-skewed  
- `views` contains extreme values that inflate the mean  
- `shipping_price` behaves like a tiered marketplace fee structure  
- `seller_rating` is compressed near the upper bound  
- add-to-cart and purchase behavior show measurable funnel drop-off  
- category distribution is imbalanced across listings  

---

## Validation & Iteration

The pipeline was improved across multiple runs by converting analytical issues into:

- statistical fixes  
- validation rules  
- interpretation improvements 

and follows: Run > Validate > Fix > Re-run

---

## Stage Boundary

This project does:

- profile the dataset  
- classify variables correctly  
- compute descriptive statistics  
- validate analytical outputs  
- apply basic cleaning rules  
- produce an analysis-ready dataset  

This project does not:

- perform segmentation  
- test relationships  
- infer causality  
- build predictive models  
- optimize marketplace decisions  

---

## Repository Structure

```text
projects/01_marketplace_descriptive/
├── data/
│   ├── raw/
│   └── cleaned/
├── outputs/
│   ├── reports/
│   ├── plots/
│   ├── validation/
│   └── cleaning/
├── configs/
│   └── project_config.yaml
├── README.md
├── changelog.md
└── notes.md
```

---

## Limitations

- Synthetic dataset (patterns are realistic but not real-world verified)  
- No time dimension  
- No multivariate analysis  
- Cleaning rules are intentionally conservative  
- Findings describe patterns, not causal relationships  
