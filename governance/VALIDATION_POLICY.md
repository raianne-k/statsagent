# Validation Policy

StatsAgent uses validation to detect analytical risks before outputs are trusted.

## Validation Purpose

Validation is used to check:
- statistical correctness
- responsible interpretation
- data quality issues
- cleaning consistency
- overclaiming or causal language

## Warning-Level Issues

Warnings require review but do not automatically invalidate the analysis.

Examples:
- missing values
- skewed distributions
- outliers
- suspicious maximum values
- category imbalance
- unclear interpretation

## Critical Issues

Critical issues should block or delay downstream analysis until reviewed.

Examples:
- invalid binary values
- impossible numeric values
- schema mismatch
- missing required fields
- unresolved cleaning flags
- duplicated or contradictory outputs

## Interpretation Validation

The system should flag:
- causal claims from descriptive analysis
- unsupported conclusions
- missing discussion of important data quality issues
- overemphasis on weak or small-sample findings

## Validation Outcome

Each run should produce:
- validation status
- warnings
- issues requiring human review
- recommended next action

# Governance Alignment

The validation framework is designed around principles commonly associated with trustworthy and reviewable AI systems.

The purpose of validation is to reduce:
- unsupported conclusions
- hidden assumptions
- misleading interpretations
- silent data-quality failures

This follows broader governance ideas emphasized in modern AI regulation and risk-management literature, including:
- transparency
- explainability
- human oversight
- risk-based review

## References

- [EU AI Act Overview](https://aiactinfo.eu/)
- [Risk Management in the AI Act (research paper)](https://arxiv.org/abs/2212.03109)
- [Trustworthy AI & EU AI Governance Discussion](https://arxiv.org/abs/2408.08318)