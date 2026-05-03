# Descriptive Statistics — Change Log

## Run 01 — Initial Agent Output

**Baseline**
- First agent-generated descriptive statistics report
- No fixes applied

**Issues found**
- DS-01: binary variables were treated as continuous for outlier detection
- DS-02: ID columns were included in numeric analysis
- DS-03: suspicious maximum values were flagged but not quantified
- DS-04: categorical variables were not summarized
- DS-05: some metrics were estimated instead of computed
- DS-06: low-cardinality numeric variables were not verified

---

## Run 02 — Changes Applied

**Tool fix**
- DS-02 implemented: ID column exclusion
  - ID columns are labels, not measurements
  - Including them adds noise and could create misleading relationships in later analysis

**Instruction improvements**
- Do not treat binary variables as continuous
- Exclude ID columns
- Prioritize key findings
- Verify suspicious values
- Compute metrics instead of estimating them

**Validation process**
- Added structured validation log to document issues and convert them into fix tickets

---

## Expected Improvements in Run 02

Run 02 should show:

- `listing_id`, `seller_id`, and `buyer_id` excluded from numeric descriptive stats
- clearer prioritization of key findings
- fewer irrelevant numeric summaries
- stronger distinction between valid stats and misleading stats
- less reliance on rough estimates in the interpretation

---

## Known Issues Still Open

The following are not fully fixed yet unless tool logic is added:

- DS-01: binary variables still need tool-level handling
- DS-03: suspicious max values still need automatic quantification
- DS-04: categorical summaries still need tool-level implementation
- DS-05: conversion metrics still need direct computation
- DS-06: low-cardinality numeric variables still need detection

---

## Run 03 — Future Fixes

improvements:

- DS-01: binary handling fixed at tool level
- DS-04: categorical summaries added