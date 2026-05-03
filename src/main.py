import argparse

from agent import build_stats_agent
from tools.data_loader import load_csv, profile_dataset
from tools.descriptive_stats import compute_descriptive_stats
from validator import validate_descriptive_analysis
from reporter import save_markdown_report


def prepare_agent_context(profile: dict, stats: dict) -> dict:
    """Create a compact context for the agent to reduce token usage."""

    compact_stats = {
        "dataset_overview": {
            "rows": profile.get("row_count"),
            "columns": profile.get("column_count"),
            "duplicate_rows": profile.get("duplicate_rows"),
            "missing_values": profile.get("missing_values"),
        },
        "column_classification": {
            "excluded_id_columns": stats.get("excluded_id_columns"),
            "continuous_numeric_columns": stats.get("continuous_numeric_columns"),
            "binary_columns": stats.get("binary_columns"),
            "low_cardinality_numeric_columns": stats.get("low_cardinality_numeric_columns"),
            "categorical_columns": stats.get("categorical_columns"),
        },
        "continuous_summary": {},
        "binary_summary": stats.get("binary_summary"),
        "low_cardinality_summary": stats.get("low_cardinality_summary"),
        "categorical_summary": stats.get("categorical_summary"),
    }

    for column, values in stats.get("extra_stats", {}).items():
        compact_stats["continuous_summary"][column] = {
            "mean": values.get("mean"),
            "median": values.get("median"),
            "iqr": values.get("iqr"),
            "outlier_percent": values.get("outlier_percent"),
            "mean_median_gap_percent": values.get("mean_median_gap_percent"),
            "skew_warning": values.get("skew_warning"),
            "round_number_max_check": values.get("round_number_max_check"),
        }

    return compact_stats


def main():
    parser = argparse.ArgumentParser(description="Run StatsAgent analysis.")

    parser.add_argument("--data", required=True)
    parser.add_argument("--task", required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--run-name", required=True)

    args = parser.parse_args()

    df = load_csv(args.data)
    profile = profile_dataset(df)

    if args.task != "descriptive_stats":
        raise ValueError("Only descriptive_stats is supported on Day 1.")

    stats = compute_descriptive_stats(df)
    agent_context = prepare_agent_context(profile, stats)

    agent = build_stats_agent()

    prompt = f"""
You are interpreting the output of a descriptive statistics analysis.

Task:
{args.task}

Dataset profile and compact statistical results:
{agent_context}

Write a careful interpretation.

Rules:
- Separate facts from interpretation.
- Mention missing data if present.
- Mention outliers if present.
- Mention skew or mean/median issues if present.
- Mention excluded ID columns if present.
- Mention binary variables as proportions, not continuous distributions.
- Mention categorical summaries if present.
- Mention low-cardinality numeric variables as possible discrete tiers.
- Do not make causal claims.
- Do not claim this analysis explains why something happened.
"""

    response = agent.run(prompt)
    interpretation = response.content

    validation = validate_descriptive_analysis(
        profile=profile,
        stats=stats,
        interpretation=interpretation,
    )

    report_path = save_markdown_report(
        task=args.task,
        profile=profile,
        stats=stats,
        interpretation=interpretation,
        validation=validation,
        project_name=args.project,
        run_name=args.run_name,
    )

    print(f"Report saved to: {report_path}")
    print(f"Validation status: {validation['status']}")
    print("Warnings:", validation["warnings"])


if __name__ == "__main__":
    main()