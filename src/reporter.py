from pathlib import Path
from datetime import datetime


def save_markdown_report(
    task: str,
    profile: dict,
    stats: dict,
    interpretation: str,
    validation: dict,
    project_name: str,
    run_name: str,
) -> str:
    """Save the analysis report as a markdown file."""

    output_path = Path(f"projects/{project_name}/reports/{run_name}.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    report = f"""# Analysis Report

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Task

{task}

## Dataset Overview

- Rows: {profile.get("row_count")}
- Columns: {profile.get("column_count")}
- Duplicate rows: {profile.get("duplicate_rows")}
- Numeric columns: {profile.get("numeric_columns")}
- Categorical columns: {profile.get("categorical_columns")}

## Missing Values

{profile.get("missing_values")}

## Method Used

Descriptive statistics were computed using column-type classification. Variables were separated into continuous numeric, binary, low-cardinality numeric, and categorical types, with each analyzed using appropriate summary methods.

## Results

{stats}

## Interpretation

{interpretation}
"""

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(report)

    return str(output_path)