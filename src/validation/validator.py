def add_issue(issues: list, severity: str, message: str):
    issues.append({
        "severity": severity,
        "message": message,
    })


def validate_descriptive_analysis(profile: dict, stats: dict, interpretation: str) -> dict:
    """Validate whether the descriptive analysis is responsibly interpreted."""

    issues = []
    text = interpretation.lower()

    # Causal language - Descriptive statistics should not imply causality.
    causal_words = ["causes", "caused", "drives", "leads to", "because of", "results in", "proves"]

    for word in causal_words:
        if word in text:
            add_issue(
                issues,
                "critical",
                f"Possible overclaim: interpretation uses causal language: '{word}'."
            )

    # Missing values - Missingness must be mentioned if present.
    if any(value > 0 for value in profile.get("missing_values", {}).values()):
        if "missing" not in text:
            add_issue(
                issues,
                "warning",
                "Missing values exist but were not mentioned in the interpretation."
            )

    # Outlier/skew checks - Important distribution issues must be discussed.
    outlier_flags = []
    skew_flags = []

    for column, values in stats.get("extra_stats", {}).items():
        if values.get("outlier_count", 0) > 0:
            outlier_flags.append(column)

        if values.get("skew_warning"):
            skew_flags.append(column)

    if outlier_flags and "outlier" not in text:
        add_issue(
            issues,
            "warning",
            f"Outliers detected in {outlier_flags}, but interpretation did not mention them."
        )

    if skew_flags and "skew" not in text and "median" not in text:
        add_issue(
            issues,
            "warning",
            f"Possible skew detected in {skew_flags}, but interpretation did not discuss skew or median."
        )

    # Cleaning flags - Invalid flag columns should not contain True values after cleaning.
    invalid_flag_issues = []

    for column, summary in stats.get("categorical_summary", {}).items():
        if not column.endswith("_invalid_flag"):
            continue

        top_values = summary.get("top_values", {})

        true_count = (
            top_values.get(True, 0)
            or top_values.get("True", 0)
            or top_values.get("true", 0)
        )

        if true_count > 0:
            invalid_flag_issues.append({
                "column": column,
                "true_count": true_count
            })

    if invalid_flag_issues:
        add_issue(
            issues,
            "critical",
            f"Invalid cleaning flags detected: {invalid_flag_issues}"
        )

    critical_count = sum(issue["severity"] == "critical" for issue in issues)
    warning_count = sum(issue["severity"] == "warning" for issue in issues)

    if critical_count > 0:
        status = "human_review_required"
    elif warning_count > 0:
        status = "review_needed"
    else:
        status = "pass"

    return {
        "status": status,
        "issues": issues,
        "warnings": [issue["message"] for issue in issues],
        "critical_count": critical_count,
        "warning_count": warning_count,
    }