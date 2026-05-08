from pathlib import Path
from datetime import datetime
import json


def save_run_metadata(
    project_name: str,
    run_name: str,
    task: str,
    dataset_path: str,
    report_path: str,
    validation: dict,
    cleaning_rules_path: str | None = None,
) -> Path:
    """Save versioned run metadata for auditability."""

    output_dir = Path(f"projects/{project_name}/outputs/metadata")
    output_dir.mkdir(parents=True, exist_ok=True)

    base_path = output_dir / f"{run_name}.json"

    if not base_path.exists():
        output_path = base_path
    else:
        version = 2

        while True:
            versioned_path = output_dir / f"{run_name}_v{version}.json"

            if not versioned_path.exists():
                output_path = versioned_path
                break

            version += 1

    metadata = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "project": project_name,
        "run_name": run_name,
        "task": task,
        "dataset_analyzed": dataset_path,
        "cleaning_rules": cleaning_rules_path,
        "report_path": report_path,
        "report_version": output_path.stem,
        "validation_status": validation.get("status"),
        "validation_warnings": validation.get("warnings", []),
        "validation_issues": validation.get("issues", []),
        "critical_count": validation.get("critical_count", 0),
        "warning_count": validation.get("warning_count", 0),
        "llm_assisted": True,
        "manual_review_required": True,
        "manual_review_completed": False,
        "governance_note": "AI-assisted analysis output; human review required before business-critical use.",
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(metadata, file, indent=2)

    return output_path