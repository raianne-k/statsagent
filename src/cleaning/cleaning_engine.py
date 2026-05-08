from pathlib import Path
import json
import pandas as pd

from src.cleaning.cleaning_rules import load_cleaning_rules


class CleaningEngine:
    """
    Conservative cleaning engine.

    Main idea:
    - do not overwrite raw data
    - do not silently delete or impute values
    - apply only documented rules from YAML
    - create a cleaned analytical dataset + cleaning log
    """

    def __init__(self, rules_path: str):
        self.rules_path = Path(rules_path)
        self.rules = load_cleaning_rules(self.rules_path)
        self.cleaning_log = []

    # Logging - Record each cleaning action for auditability.
    def log(self, rule_id: str, action: str, details: dict):
        self.cleaning_log.append({
            "rule_id": rule_id,
            "action": action,
            "details": details
        })

    # Load data - Read the raw dataset without modifying the source file.
    def load_data(self) -> pd.DataFrame:
        raw_path = Path(self.rules["data"]["raw_path"])

        if not raw_path.exists():
            raise FileNotFoundError(f"Raw dataset not found: {raw_path}")

        df = pd.read_csv(raw_path)

        self.log(
            rule_id="LOAD-01",
            action="loaded_raw_dataset",
            details={
                "path": str(raw_path),
                "rows": len(df),
                "columns": len(df.columns)
            }
        )

        return df

    # Duplicate check - Remove only exact duplicate rows.
    def remove_exact_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        before = len(df)

        df = df.drop_duplicates()

        removed = before - len(df)

        self.log(
            rule_id="CL-01",
            action="removed_exact_duplicates",
            details={
                "rows_before": before,
                "rows_after": len(df),
                "rows_removed": removed
            }
        )

        return df

    # Binary validation - Validate binary columns using flexible yes/no and 0/1 logic.
    def validate_binary_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        binary_columns = self.rules["variables"].get("binary_columns", [])

        valid_string_values = {
            "yes",
            "no",
            "true",
            "false",
            "0",
            "1"
        }

        valid_numeric_values = {
            0,
            1,
            0.0,
            1.0,
            True,
            False
        }

        for col in binary_columns:
            if col not in df.columns:
                self.log(
                    "CL-02",
                    "binary_column_missing",
                    {"column": col}
                )
                continue

            if (
                pd.api.types.is_object_dtype(df[col])
                or pd.api.types.is_string_dtype(df[col])
                or pd.api.types.is_categorical_dtype(df[col])
            ):
                normalized = (
                    df[col]
                    .astype(str)
                    .str.lower()
                    .str.strip()
                )

                invalid_mask = ~normalized.isin(valid_string_values)

            else:
                invalid_mask = ~df[col].isin(valid_numeric_values)

            flag_col = f"{col}_invalid_flag"

            df[flag_col] = invalid_mask

            self.log(
                rule_id="CL-02",
                action="validated_binary_column",
                details={
                    "column": col,
                    "invalid_values_found": int(invalid_mask.sum()),
                    "flag_column_created": flag_col,
                    "accepted_values": "0/1, true/false, yes/no"
                }
            )

        return df

    # Binary standardization - Create consistent 0/1 analytical versions of binary fields.
    def standardize_binary_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        binary_columns = self.rules["variables"].get("binary_columns", [])

        mapping = {
            "yes": 1,
            "true": 1,
            "1": 1,
            "no": 0,
            "false": 0,
            "0": 0,
        }

        for col in binary_columns:
            if col not in df.columns:
                self.log(
                    "CL-06",
                    "binary_standardization_column_missing",
                    {"column": col}
                )
                continue

            clean_col = f"{col}_clean"

            if (
                pd.api.types.is_object_dtype(df[col])
                or pd.api.types.is_string_dtype(df[col])
                or pd.api.types.is_categorical_dtype(df[col])
            ):
                df[clean_col] = (
                    df[col]
                    .astype(str)
                    .str.lower()
                    .str.strip()
                    .map(mapping)
                )

            else:
                df[clean_col] = df[col]

            self.log(
                rule_id="CL-06",
                action="standardized_binary_column",
                details={
                    "source_column": col,
                    "clean_column_created": clean_col,
                    "unmapped_or_invalid_values": int(df[clean_col].isna().sum())
                }
            )

        return df

    # Missing value flags - Preserve rows while marking configured missing values.
    def flag_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        policies = self.rules.get("missing_value_policy", {})

        for col, policy in policies.items():
            if col not in df.columns:
                self.log(
                    "CL-03",
                    "missing_policy_column_not_found",
                    {"column": col}
                )
                continue

            missing_mask = df[col].isna()

            missing_count = int(missing_mask.sum())

            if policy.get("action") == "flag_and_keep":
                flag_col = f"{col}_missing_flag"

                df[flag_col] = missing_mask

                self.log(
                    rule_id="CL-03",
                    action="flagged_missing_values",
                    details={
                        "column": col,
                        "missing_count": missing_count,
                        "flag_column_created": flag_col,
                        "reason": policy.get("reason")
                    }
                )

        return df

    # Numeric validity checks - Flag impossible values without modifying them.
    def flag_invalid_numeric_values(self, df: pd.DataFrame) -> pd.DataFrame:
        rules = self.rules.get("invalid_numeric_values", {})

        for col, bounds in rules.items():
            if col not in df.columns:
                self.log(
                    "CL-04",
                    "numeric_rule_column_not_found",
                    {"column": col}
                )
                continue

            invalid_mask = pd.Series(False, index=df.index)

            if "min" in bounds:
                invalid_mask |= df[col] < bounds["min"]

            if "max" in bounds:
                invalid_mask |= df[col] > bounds["max"]

            invalid_count = int(invalid_mask.sum())

            flag_col = f"{col}_invalid_flag"

            df[flag_col] = invalid_mask

            self.log(
                rule_id="CL-04",
                action="flagged_invalid_numeric_values",
                details={
                    "column": col,
                    "invalid_count": invalid_count,
                    "bounds": bounds,
                    "flag_column_created": flag_col
                }
            )

        return df

    # Type overrides - Apply semantic type choices from configuration.
    def apply_type_overrides(self, df: pd.DataFrame) -> pd.DataFrame:
        categorical_columns = self.rules["variables"].get(
            "categorical_columns",
            []
        )

        for col in categorical_columns:
            if col not in df.columns:
                self.log(
                    "CL-05",
                    "categorical_column_missing",
                    {"column": col}
                )
                continue

            df[col] = df[col].astype("category")

            self.log(
                rule_id="CL-05",
                action="cast_column_to_category",
                details={
                    "column": col,
                    "new_type": "category"
                }
            )

        return df

    # Save outputs - Write cleaned dataset and cleaning log to disk.
    def save_outputs(self, df: pd.DataFrame):
        cleaned_path = Path(self.rules["data"]["cleaned_path"])

        log_path = Path(self.rules["outputs"]["cleaning_log"])

        cleaned_path.parent.mkdir(parents=True, exist_ok=True)

        log_path.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(cleaned_path, index=False)

        self.log(
            rule_id="SAVE-01",
            action="saved_cleaned_dataset_and_log",
            details={
                "cleaned_dataset_path": str(cleaned_path),
                "cleaning_log_path": str(log_path),
                "rows": len(df),
                "columns": len(df.columns)
            }
        )

        with open(log_path, "w", encoding="utf-8") as file:
            json.dump(self.cleaning_log, file, indent=2)

    # Run order - Apply cleaning rules in a controlled sequence.
    def run(self) -> pd.DataFrame:
        df = self.load_data()

        df = self.remove_exact_duplicates(df)

        df = self.validate_binary_columns(df)

        df = self.standardize_binary_columns(df)

        df = self.flag_missing_values(df)

        df = self.flag_invalid_numeric_values(df)

        df = self.apply_type_overrides(df)

        self.save_outputs(df)

        return df


if __name__ == "__main__":
    engine = CleaningEngine(
        rules_path="configs/cleaning_rules.yaml"
    )

    engine.run()