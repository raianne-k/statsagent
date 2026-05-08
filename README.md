# StatsAgent

**Agent-driven analytics and decision-support framework with human-validated statistical reasoning.**

StatsAgent combines:

- programmatic statistical analysis,
- AI-assisted analytical interpretation,
- validation-aware workflows,
- executive reporting,
- and governance-oriented decision support.

The framework was built to explore how modern analytical systems can combine:

- statistical tooling,
- structured reasoning,
- agent workflows,
- and human validation into repeatable analytical pipelines across multiple business domains.

---

# Framework Progression

| Stage | Focus |
|---|---|
| P01 | Descriptive analytics foundations |
| P02 | Segmentation & comparative analysis |
| P03 | Relationship & operational pattern analysis |
| P04 | Statistical inference & uncertainty |
| P05 | Predictive churn modeling |
| P06 | Experimentation & A/B testing |
| P07 | Forecasting & strategic planning |

---

# Repository Navigation

| Section | Purpose |
|---|---|
| `/src` | Shared analytical framework components |
| `/projects` | Portfolio case-study pipelines |
| `/governance` | Shared governance and validation policies |
| `/outputs` | Analytical reports, dashboards, and plots |

---

# Core Stack

| Layer              | Technology                         |
| ------------------ | ---------------------------------- |
| Agent framework    | Agno                               |
| LLMs               | Claude (Anthropic)                 |
| Statistical engine | Python                             |
| Core libraries     | Pandas, NumPy, SciPy, Scikit-learn |
| Visualization      | Matplotlib, HTML dashboards        |
| Reporting          | Executive HTML reporting           |
| Validation         | Custom governance & review layer   |

---

# What StatsAgent Is

StatsAgent is a modular analytics framework designed to support:

```text
descriptive analysis
→ segmentation
→ relationship analysis
→ inference
→ prediction
→ experimentation
→ strategic forecasting
```

The system combines:

- reusable analytical modules,
- AI-assisted interpretation,
- validation-aware workflows,
- and human-reviewed analytical outputs.

The repository contains both:

1. the underlying analytical framework
2. portfolio case-study projects demonstrating how the framework can be applied across different business and operational contexts

---

# Why StatsAgent Exists

Modern analytical workflows often generate:

- dashboards,
- metrics,
- and model outputs,

without sufficiently validating:

- whether conclusions are methodologically sound,
- whether assumptions are reasonable,
- whether interpretation is defensible,
- or whether operational recommendations should actually be trusted.

StatsAgent was built to bridge that gap.

The framework emphasizes:

- structured reasoning,
- interpretability,
- governance-aware analytics,
- and operational realism.

---

# AI-Assisted Analytical Workflow

A major goal of StatsAgent is demonstrating how AI agents can be integrated into analytical workflows responsibly.

The framework intentionally uses:

- LLM-assisted interpretation,
- structured prompting,
- analytical constraints,
- and validation-aware review systems

rather than unrestricted autonomous analysis.

The objective is to explore how AI-assisted systems can:

- accelerate structured analysis,
- improve workflow consistency,
- support interpretation,
- and reinforce analytical reasoning while still maintaining human oversight.

---

# Agent-Driven Architecture

StatsAgent uses AI agents as constrained analytical interpreters rather than unrestricted generators.

The agents:

- operate on computed analytical outputs
- follow predefined reasoning rules
- separate observation from interpretation
- avoid unsupported causal claims
- enforce analytical consistency
- prioritize operationally meaningful findings
- support executive-facing narrative generation

Outputs are intentionally designed to remain:

- auditable,
- reviewable,
- and governance-aware.

---

# Portfolio Roadmap

The repository includes seven major analytical projects.

| Project | Domain            | Focus                                                  |
| ------- | ----------------- | ------------------------------------------------------ |
| P01     | Marketplace       | Descriptive analytics and KPI foundations              |
| P02     | Fintech           | Customer segmentation and repayment-risk profiling     |
| P03     | SaaS              | Relationship analysis and operational account patterns |
| P04     | Fintech           | Statistical inference and uncertainty-aware analysis   |
| P05     | SaaS              | Churn prediction and retention-risk modeling           |
| P06     | Product Analytics | Experimentation and A/B testing                        |
| P07     | SaaS Strategy     | Strategic forecasting and scenario modeling            |

Together, these projects demonstrate a complete analytics lifecycle.

---

# Portfolio Lifecycle

StatsAgent intentionally progresses through increasingly advanced analytical stages:

```text
P01 → What is happening?
P02 → Which groups behave differently?
P03 → Which variables move together?
P04 → How confident are we?
P05 → Which accounts are likely at risk?
P06 → Did the product change work?
P07 → What might happen next under different decisions?
```

This progression mirrors how analytical maturity evolves within real organizations.

---

# Interactive Outputs

### P05 — Churn Prediction Dashboard
- [Interactive Dashboard](projects/p05_saas_churn_prediction/outputs/dashboards/churn_dashboard.html)
- [Executive Report](projects/p05_saas_churn_prediction/outputs/reports/executive_report.html)

### P06 — Experimentation Dashboard
- [Interactive Dashboard](projects/p06_product_experimentation/outputs/dashboards/experiment_dashboard.html)
- [Executive Report](projects/p06_product_experimentation/outputs/reports/executive_experiment_report.html)

### P07 — Strategic Forecasting Dashboard
- [Interactive Dashboard](projects/p07_saas_strategic_forecasting/outputs/dashboards/forecasting_dashboard.html)
- [Executive Report](projects/p07_saas_strategic_forecasting/outputs/reports/executive_forecasting_report.html)

---

# Analytical Philosophy

## 1. Context Before Calculation

Every metric should answer a business question.

Calculations without operational interpretation are incomplete analysis.

---

## 2. Validation Before Interpretation

Analytical outputs are not automatically trusted because code executed successfully.

Each project includes:

- validation checks,
- assumption review,
- uncertainty discussion,
- and governance-aware interpretation.

---

## 3. Interpretation Before Automation

StatsAgent is designed as:

> AI-assisted analysis with human validation

not fully autonomous decision-making.

---

## 4. Governance-Aware Analytics

The framework explicitly reinforces:

- uncertainty awareness,
- limitation disclosure,
- observational vs causal distinction,
- assumption transparency,
- and operational review requirements.

---

# Framework Architecture

```text
statsagent/
├── src/
│   ├── cleaning/
│   ├── pipeline/
│   ├── reporting/
│   ├── validation/
│   └── visualization/
│
├── projects/
│   ├── p01_marketplace_descriptive/
│   ├── p02_fintech_customer_segmentation/
│   ├── p03_saas_relationships/
│   ├── p04_fintech_inference/
│   ├── p05_saas_churn_prediction/
│   ├── p06_product_experimentation/
│   └── p07_saas_strategic_forecasting/
│
├── governance/
├── README.md
└── requirements.txt
```

---

# Project Architecture

Most projects follow a standardized structure:

```text
project/
├── configs/
├── data/
│   ├── raw/
│   └── cleaned/
├── outputs/
│   ├── reports/
│   ├── dashboards/
│   ├── plots/
│   ├── validation/
│   ├── cleaning/
│   └── metadata/
├── scripts/
│   ├── data_generation/
│   ├── analysis/
│   └── reporting/
├── docs/
│   ├── findings.md
│   └── changelog.md
├── README.md
└── run.sh
```

Earlier projects use a simpler structure because they were built before the framework matured.

---

# Core Analytical Modules

StatsAgent currently includes reusable workflows for:

- descriptive statistics
- segmentation analysis
- relationship analysis
- correlation analysis
- statistical inference
- uncertainty estimation
- predictive modeling
- experimentation & A/B testing
- forecasting & scenario modeling
- validation logging
- executive reporting
- HTML dashboards
- governance-aware interpretation

---

# Executive Reporting Layer

Later-stage projects include executive-facing outputs such as:

- HTML analytical reports
- strategic dashboards
- forecasting interfaces
- scenario comparison systems
- model evaluation summaries
- experimentation reviews
- cohort-retention visualizations

The reporting layer focuses not only on technical correctness, but on:

- interpretability,
- communication quality,
- and decision-support usefulness.

---

# Governance Layer

StatsAgent includes governance-oriented analytical principles across projects:

- synthetic-data disclosure
- human-review requirements
- uncertainty-aware reporting
- separation of observation from causal inference
- validation-aware interpretation
- assumption disclosure
- operational-review requirements
- non-automation framing
- auditability and traceability

The framework intentionally prioritizes:

- analytical realism,
- interpretability,
- and governance-aware workflows over opaque optimization-focused systems.

---

# Synthetic Dataset Note

The repository uses synthetic but intentionally realistic datasets.

The datasets are designed to:

- emulate realistic operational behavior,
- support analytical practice,
- demonstrate framework capabilities,
- and avoid exposing private or regulated data.

Some patterns may partly reflect simulation assumptions rather than naturally occurring production behavior.

That distinction is disclosed throughout project documentation where relevant.

---

# Current Repository Context

This repository contains:

- reusable analytical framework components,
- AI-assisted workflow architecture,
- validation systems,
- and portfolio demonstration projects.

The included projects are representative case studies demonstrating how the framework can be applied across:

- product analytics,
- fintech,
- SaaS operations,
- experimentation,
- forecasting,
- and executive decision-support contexts.

The analytical modules themselves are designed to be reusable and extensible beyond the included portfolio examples.

---

# Current Limitations

- Repository datasets are synthetic
- Some operational assumptions are intentionally simplified for interpretability
- Forecasting outputs are probabilistic rather than deterministic
- Scenario outputs are assumption-dependent
- Production orchestration and deployment infrastructure are outside the repository scope
- Human analytical review remains required for operational usage
- Some modules prioritize transparency and governance over optimization complexity

---

# Running Projects

Projects are executed independently through project-specific analytical pipelines and reporting workflows.

Typical execution:

```bash
bash run.sh
```

Each project contains:

- its own dataset generation layer,
- analytical scripts,
- reporting modules,
- validation outputs,
- and executive deliverables.

---

# Long-Term Direction

StatsAgent is intended to continue evolving as:

- a reusable analytics framework,
- an AI-assisted analytical workflow system,
- and a structured environment for validating and improving analytical reasoning.

Future directions may include:

- expanded forecasting modules,
- richer agent workflows,
- automated validation orchestration,
- interactive analytical tooling,
- and broader decision-support capabilities.

---

# Summary

StatsAgent demonstrates how AI-assisted systems can be combined with:

- structured statistical workflows,
- governance-aware reasoning,
- validation layers,
- and executive communication

to produce analytical outputs that are:

- interpretable,
- reviewable,
- operationally meaningful,
- and strategically useful.
