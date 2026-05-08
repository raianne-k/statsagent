# Data Handling Policy

This project is designed with data minimization, traceability, and privacy awareness in mind.

## Raw Data

Raw datasets should be treated as the source of truth.

Rules:
- raw data should not be overwritten
- cleaned datasets should be saved separately
- all transformations should be logged
- raw and cleaned data should remain clearly separated

## Synthetic Data

Portfolio projects should use synthetic or anonymized data.

This reduces:
- privacy risk
- client confidentiality risk
- exposure of sensitive business information

## Identifier Handling

Identifiers such as user IDs, customer IDs, seller IDs, buyer IDs, transaction IDs, or loan IDs should not be used as analytical variables unless there is a justified reason.

Default treatment:
- preserve identifiers if needed for traceability
- exclude identifiers from statistical summaries
- avoid sending identifiers to LLM prompts

## Key Principles Applied

### Data Minimization
Only the data needed for the analytical question should be used.

Preferred order:
1. aggregated data
2. anonymized analytical datasets
3. row-level data without direct identifiers
4. identifiable data only if strictly necessary

### Separation of Raw vs Processed Data
Raw datasets should remain immutable whenever possible.

### Least Required Exposure
External AI models should receive summarized analytical outputs rather than full raw datasets where possible.

### Business Confidentiality Awareness
Business metrics and operational datasets may contain commercially sensitive information even when no personal data is present.


## External Model Exposure

The LLM should receive compact summaries and statistical outputs where possible, not full raw datasets.

Sensitive fields should be excluded from prompts unless explicitly required and approved.

## Client / Company Information

Client data may include sensitive business information even when it does not include personal data.

Examples:
- conversion rates
- revenue metrics
- default rates
- retention metrics
- customer behavior
- internal KPIs

These should be treated as confidential.

---

# Governance Context

The data handling approach used in this project is influenced by principles commonly found in:

- GDPR data minimization principles
- privacy-aware analytical system design
- auditability and traceability practices
- responsible handling of business-sensitive information


## References

- [GDPR Legal Text](https://gdpr-info.eu/)
- [GDPR Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj)