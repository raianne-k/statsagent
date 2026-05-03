# Descriptive Statistics Validation Pipeline (Marketplace Dataset)

**Role:** Data Analytics / Analytics Engineering  
**Domain:** Marketplace / E-commerce  
**Tools:** Python (Pandas, Matplotlib), LLM (Claude), Custom Validation Layer  
**Dataset:** Synthetic marketplace listings  

## Final Output

[View Final Report](./reports/final_report.md)


---

## Overview

This project builds a **validated descriptive statistics pipeline**, focusing on producing results that are not only correct, but also **interpretable and trustworthy**.

Instead of relying on default summaries, the pipeline:
- classifies variables by type  
- avoids common statistical mistakes  
- validates outputs through structured review  
- improves iteratively through logged issues  

---

## Problem

Automated descriptive analysis often produces misleading results:
- binary variables treated as continuous  
- ID columns included in analysis  
- categorical variables ignored  
- suspicious values flagged but not verified  

This project addresses those issues at the tool level.

---

## Approach

The pipeline has three layers:

### 1. Statistical Engine (Python)
- Column classification (continuous, binary, categorical, tiered)
- IQR-based outlier detection (continuous only)
- Skew detection (mean vs median)
- Round-number max checks (e.g. 1000)
- Missing value tracking

### 2. Interpretation Layer (LLM)
- Structured output (method, results, interpretation, limitations)
- Enforces correct reasoning (no causal claims, proper variable handling)

### 3. Validation Layer
- Issues tracked as DS-01 → DS-07
- Each issue converted into a concrete fix
- Iterative improvement across runs

---

## Key Findings

- **Right-skewed distributions** in price, views, and listing age  
- **Extreme values in views** significantly inflate the mean  
- **Shipping price is tier-based**, not continuous  
- **Seller ratings are tightly clustered** near the maximum  
- **Conversion drop-off** from add-to-cart (18.9%) to purchase (11.1%)

---

## Visual Validation

Plots confirm:
- strong skew in key variables  
- discrete structure in shipping prices  
- imbalance in category distribution  

See `/plots`.

---

## Validation & Iteration

Three runs were used to improve the system:

- **Run 01:** baseline output, multiple methodological issues  
- **Run 02:** ID exclusion + instruction fixes  
- **Run 03:** full tool-level fixes (binary handling, categorical summaries, tier detection)

Final status:
- All major statistical issues fixed  
- Conversion funnel calculation remains open  

---

## Repository Structure
/src
descriptive_stats.py
agent.py
validator.py
reporter.py

/projects/01_descriptive_statistics
changelog.md
/reports
/plots

---

## Limitations

- Synthetic dataset (not fully realistic distributions)  
- No multivariate analysis  
- Conversion funnel not explicitly computed  
- No time-based analysis  

---

## Next Steps

- Compute full conversion funnel  
- Add segmentation (category, region, returning users)  
- Extend to correlation and regression  

---

## Summary

This project demonstrates:
- correct handling of different data types  
- identification and correction of statistical errors  
- building a validation-driven analytics workflow  