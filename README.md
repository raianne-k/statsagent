# StatsAgent: Agent-driven analysis with human-validated logic

**Framework:** Agno (Arbon)  
**Model:** Claude (Anthropic)  
**Tools:** Python (Pandas, Matplotlib), Custom Validation Layer  

---

## Overview

StatsAgent is a structured analysis system that combines programmatic statistics, an LLM agent, and a validation layer to produce outputs that are not just correct,  but **methodologically reliable and interpretable**.

The goal is to bridge a common gap:

Analytical workflows often generate numbers,
but not necessarily trustworthy conclusions.

StatsAgent enforces consistency between:
- what is computed  
- how it is interpreted  
- and whether it should be trusted  

It combines programmatic analysis, a constrained LLM agent, and a validation layer to reduce common analytical mistakes and enforce consistent reasoning.


---
## What makes it agent-driven

StatsAgent uses an LLM agent to interpret statistical outputs under strict constraints.

The agent:
- follows predefined analytical rules  
- separates observation from interpretation  
- avoids unsupported claims  

It operates on computed results (not raw data).

---

## Problem

Standard workflows using Pandas + LLMs often produce outputs that are:

- technically correct but misleading  
- inconsistent in reasoning  
- unaware of common statistical pitfalls  

Examples:
- treating binary variables as continuous  
- including ID columns in analysis  
- ignoring categorical structure  
- flagging issues without verifying them  

StatsAgent addresses these issues at the system level.

---

## Approach

The system is built as a layered pipeline:

### 1. Statistical Engine (Python)

Handles:
- dataset profiling  
- type-aware descriptive statistics  
- outlier detection (IQR)  
- skew detection (mean vs median)  
- categorical and tiered variable handling  
- missing value tracking  

---

### 2. Interpretation Layer (LLM Agent)

A constrained LLM agent (Claude via Agno) is used to interpret outputs.

It operates under explicit instructions to:
- separate observation from interpretation  
- avoid causal claims from descriptive statistics  
- follow consistent analytical rules  
- prioritize meaningful findings over exhaustive listing  

The output is controlled, not free-form. The agent is guided to produce structured, auditable reasoning aligned with the statistical output.

An API key is required to run the agent.

---

### 3. Validation Layer

Adds a structured review step:

- issues tracked as DS-01, DS-02, etc. (depending on module) 
- each issue includes:
  - what went wrong  
  - impact  
  - correction  

These are translated into:
- tool-level fixes  
- instruction updates  

---

### 4. Iterative Improvement Loop

Run → Validate → Fix → Re-run  

Improvements are driven by validation and manual review, not autonomous learning.

---

## Project Structure

statsagent/

├── src/  
│   ├── agent.py  
│   ├── main.py  
│   ├── reporter.py  
│   ├── validator.py  
│   ├── visualization.py  
│   └── tools/  
│       ├── data_loader.py  
│       └── descriptive_stats.py  

├── projects/  
│   └── 01_marketplace_descriptive_statistics/  
│       ├── README.md  
│       ├── changelog.md  
│       ├── validation_log.json  
│       ├── reports/  
│       ├── plots/  
│       └── create_plots.py  

├── data/  
│   └── marketplace_sample.csv  

├── run.sh  
├── requirements.txt  
├── .env.example  
└── README.md  

---

## Running the Analysis

StatsAgent is reusable across datasets and projects.

### Basic command

bash run.sh --data <path_to_csv> --project <project_name> --run-name <run_name>

---

### Project structure logic

Each dataset is treated as a separate project:

projects/  
  01_marketplace_descriptive/  
  02_finance_descriptive/  
  03_logistics_descriptive/  

- `project_name` defines where outputs are stored  
- `run_name` defines the specific run within that project  

---

### Avoiding overwrites

Reports are saved as:

projects/{project_name}/reports/{run_name}.md  

To avoid overwriting:

- use a new project name for new datasets  
- use a new run name for each iteration  

---

### Recommended workflow

1. Create a new project folder for each dataset  
2. Run descriptive analysis (Stage 01)  
3. Review report and validation  
4. Generate plots  
5. Iterate using new run names  

---

## Example Project

The first project applies the system to a marketplace dataset, demonstrating:

- type-aware descriptive statistics  
- validation-driven corrections  
- structured interpretation  
- visual confirmation of findings  

See:  
/projects/01_marketplace_descriptive_statistics  

---

## Limitations

- Currently focused on descriptive statistics  
- No multivariate or predictive modeling yet  
- Validation rules are manually defined  
- Synthetic dataset used for demonstration  

---

## Roadmap

- Stage 02: segmentation and comparison  
- Stage 03: relationships and correlation  
- Stage 04: modeling and drivers  
- Expand validation to later stages  

---

## Summary

- produces statistically sound descriptive analysis  
- enforces consistent interpretation rules  
- reduces common analytical errors through validation