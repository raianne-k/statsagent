from pathlib import Path
import yaml

# Project-specific cleaning rules from YAML.
def load_cleaning_rules(config_path: str | Path) -> dict:
    """
    Load project-specific cleaning rules from YAML.

    This keeps cleaning decisions outside the code so they are
    explicit, reviewable, and project-specific.
    """
    config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Cleaning rules file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)