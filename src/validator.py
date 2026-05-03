def validate_descriptive_analysis(profile: dict, stats: dict, interpretation: str) -> dict:
    """Validate whether the descriptive analysis is responsibly interpreted."""

    warnings = []

    text = interpretation.lower()

    causal_words = ["causes", "caused", "drives", "leads to", "because of", "results in", "proves"]

    for word in causal_words:
        if word in text:
            warnings.append(
                f"Possible overclaim: interpretation uses causal language: '{word}'."
            )

    if any(value > 0 for value in profile.get("missing_values", {}).values()):
        if "missing" not in text:
            warnings.append(
                "Missing values exist but were not mentioned in the interpretation."
            )

    outlier_flags = []
    skew_flags = []

    for column, values in stats.get("extra_stats", {}).items():
        if values.get("outlier_count", 0) > 0:
            outlier_flags.append(column)

        if values.get("skew_warning"):
            skew_flags.append(column)

    if outlier_flags and "outlier" not in text:
        warnings.append(
            f"Outliers detected in {outlier_flags}, but interpretation did not mention them."
        )

    if skew_flags and "skew" not in text and "median" not in text:
        warnings.append(
            f"Possible skew detected in {skew_flags}, but interpretation did not discuss skew or median."
        )

    if not warnings:
        status = "pass"
    else:
        status = "review_needed"

    return {
        "status": status,
        "warnings": warnings,
    }