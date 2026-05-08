import argparse
from pathlib import Path

from src.agent.agent import build_stats_agent
from src.tools.data_loader import load_csv, profile_dataset
from src.analysis.descriptive_stats import compute_descriptive_stats
from src.validation.validator import validate_descriptive_analysis
from src.reporting.reporter import save_markdown_report
from src.cleaning.cleaning_engine import CleaningEngine
from src.pipeline.run_metadata import save_run_metadata


def is_technical_column(column: str) -> bool:
    """Identify cleaning/helper columns that should not drive interpretation."""

    return (
        column.endswith("_invalid_flag")
        or column.endswith("_missing_flag")
        or column.endswith("_clean")
    )


def prepare_agent_context(profile: dict, stats: dict) -> dict:
    """Create a compact context for the agent while filtering technical columns."""

    clean_binary_summary = {
        column: values
        for column, values in stats.get("binary_summary", {}).items()
        if not is_technical_column(column)
    }

    clean_categorical_summary = {
        column: values
        for column, values in stats.get("categorical_summary", {}).items()
        if not is_technical_column(column)
    }

    compact_stats = {
        "dataset_overview": {
            "rows": profile.get("row_count"),
            "columns": profile.get("column_count"),
            "duplicate_rows": profile.get("duplicate_rows"),
            "missing_values": profile.get("missing_values"),
        },
        "governance": {
            "llm_exposure": "summary_only",
            "raw_rows_sent_to_llm": False,
            "technical_columns_filtered_from_main_interpretation": True,
        },
        "column_classification": {
            "excluded_id_columns": stats.get("excluded_id_columns"),
            "continuous_numeric_columns": stats.get("continuous_numeric_columns"),
            "binary_columns": [
                column for column in stats.get("binary_columns", [])
                if not is_technical_column(column)
            ],
            "low_cardinality_numeric_columns": stats.get("low_cardinality_numeric_columns"),
            "categorical_columns": [
                column for column in stats.get("categorical_columns", [])
                if not is_technical_column(column)
            ],
            "technical_columns": stats.get("technical_columns"),
        },
        "continuous_summary": {},
        "binary_summary": clean_binary_summary,
        "low_cardinality_summary": stats.get("low_cardinality_summary"),
        "categorical_summary": clean_categorical_summary,
        "technical_validation_summary": stats.get("technical_summary", {}),
    }

    for column, values in stats.get("extra_stats", {}).items():
        if is_technical_column(column):
            continue

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


def get_analysis_data_path(args) -> str:
    """Run cleaning first when cleaning rules are provided."""

    if not args.cleaning_rules:
        return args.data

    cleaner = CleaningEngine(rules_path=args.cleaning_rules)
    cleaner.run()

    cleaned_path = cleaner.rules["data"]["cleaned_path"]

    if not Path(cleaned_path).exists():
        raise FileNotFoundError(f"Cleaned dataset was not created: {cleaned_path}")

    return cleaned_path


def main():
    parser = argparse.ArgumentParser(description="Run StatsAgent analysis.")

    parser.add_argument("--data", required=True)
    parser.add_argument("--task", required=True)
    parser.add_argument("--project", required=True)
    parser.add_argument("--run-name", required=True)
    parser.add_argument("--cleaning-rules", required=False)

    args = parser.parse_args()

    if args.task != "descriptive_stats":
        raise ValueError("Only descriptive_stats is supported in Project 01.")

    analysis_data_path = get_analysis_data_path(args)

    df = load_csv(analysis_data_path)
    profile = profile_dataset(df)

    stats = compute_descriptive_stats(df)
    agent_context = prepare_agent_context(profile, stats)

    agent = build_stats_agent()

    prompt = f"""
You are interpreting the output of a descriptive statistics analysis.

Task:
{args.task}

Dataset used:
{analysis_data_path}

Dataset profile and compact statistical results:
{agent_context}

Write a careful interpretation.

Rules:
- Separate facts from interpretation.
- Mention that cleaning was applied first if the dataset path is a cleaned dataset.
- Mention missing data if present.
- Mention outliers if present.
- Mention skew or mean/median issues if present.
- Mention excluded ID columns if present.
- Mention binary variables as proportions, not continuous distributions.
- Mention categorical summaries if present.
- Mention low-cardinality numeric variables as possible discrete tiers.
- Use technical cleaning columns only in Validation Notes.
- Do not treat *_clean, *_invalid_flag, or *_missing_flag columns as primary analytical variables.
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

    metadata_path = save_run_metadata(
        project_name=args.project,
        run_name=args.run_name,
        task=args.task,
        dataset_path=analysis_data_path,
        report_path=str(report_path),
        validation=validation,
        cleaning_rules_path=args.cleaning_rules,
    )

    print(f"Dataset analyzed: {analysis_data_path}")
    print(f"Report saved to: {report_path}")
    print(f"Run metadata saved to: {metadata_path}")
    print(f"Validation status: {validation['status']}")
    print("Warnings:", validation["warnings"])


if __name__ == "__main__":
    main()