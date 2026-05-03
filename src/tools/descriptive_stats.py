import pandas as pd


def detect_id_columns(df: pd.DataFrame) -> list:
    """Detect likely identifier columns using name-based rules.

    Rationale:
    - ID columns are labels, not measured variables.
    - Detection is based on naming conventions to avoid misclassifying real numeric variables (e.g., item_price).
    - This is a conservative heuristic: better to miss an ID than wrongly exclude a real feature.
    """

    id_columns = []

    known_id_columns = {
        "id",
        "listing_id",
        "seller_id",
        "buyer_id",
        "customer_id",
        "user_id",
        "transaction_id",
        "order_id",
        "product_id",
    }

    for column in df.columns:
        column_lower = column.lower()

        if (
            column_lower in known_id_columns
            or column_lower.endswith("_id")
        ):
            id_columns.append(column)

    return id_columns


def is_binary_column(series: pd.Series) -> bool:
    """Detect binary columns such as 0/1 or yes/no flags."""

    values = set(series.dropna().unique())

    return values in [
        {0, 1},
        {0.0, 1.0},
        {"yes", "no"},
        {"no", "yes"},
        {True, False},
        {False, True},
    ]


def summarize_binary_column(series: pd.Series) -> dict:
    """Summarize binary variables as event counts and proportions."""

    clean = series.dropna()

    if clean.empty:
        return {
            "count": 0,
            "positive_count": 0,
            "positive_rate": None,
            "note": "No non-missing values."
        }

    # Numeric binary: 1 means positive event
    if set(clean.unique()).issubset({0, 1, 0.0, 1.0}):
        positive_count = int((clean == 1).sum())
        positive_rate = round(positive_count / len(clean) * 100, 2)
        return {
            "count": int(len(clean)),
            "positive_count": positive_count,
            "positive_rate_percent": positive_rate,
            "note": "Binary variable summarized as proportion, not continuous distribution."
        }

    # String binary: yes means positive event
    lower = clean.astype(str).str.lower()
    positive_count = int((lower == "yes").sum())
    positive_rate = round(positive_count / len(clean) * 100, 2)

    return {
        "count": int(len(clean)),
        "positive_count": positive_count,
        "positive_rate_percent": positive_rate,
        "note": "Binary variable summarized as proportion, not continuous distribution."
    }


def detect_round_number_max(series: pd.Series) -> dict | None:
    """Check whether a suspicious round-number max appears repeatedly."""

    clean = series.dropna()

    if clean.empty:
        return None

    max_value = clean.max()

    if max_value == 0:
        return None

    is_round_number = (
        max_value % 100 == 0
        or max_value % 1000 == 0
    )

    if not is_round_number:
        return None

    max_count = int((clean == max_value).sum())

    return {
        "max_value": float(max_value),
        "max_count": max_count,
        "possible_cap": max_count > 1,
        "note": "Round-number maximum detected; verify whether this is a genuine value or a cap."
    }


def summarize_categorical_columns(df: pd.DataFrame, id_columns: list) -> dict:
    """Summarize categorical variables using counts and proportions."""

    categorical_summary = {}

    categorical_df = df.select_dtypes(exclude="number").drop(
        columns=id_columns,
        errors="ignore"
    )

    for column in categorical_df.columns:
        clean = categorical_df[column].dropna()
        value_counts = clean.value_counts()
        value_percent = (clean.value_counts(normalize=True) * 100).round(2)

        categorical_summary[column] = {
            "count": int(len(clean)),
            "missing": int(df[column].isna().sum()),
            "unique_values": int(clean.nunique()),
            "mode": clean.mode().iloc[0] if not clean.mode().empty else None,
            "top_values": value_counts.head(10).to_dict(),
            "top_value_percent": value_percent.head(10).to_dict(),
        }

    return categorical_summary


def compute_descriptive_stats(df: pd.DataFrame) -> dict:
    """Compute descriptive statistics with column-aware handling."""

    id_columns = detect_id_columns(df)

    numeric_df = df.select_dtypes(include="number").drop(
        columns=id_columns,
        errors="ignore"
    )

    continuous_columns = []
    binary_columns = []
    low_cardinality_numeric_columns = []

    for column in numeric_df.columns:
        series = numeric_df[column].dropna()

        if is_binary_column(series):
            binary_columns.append(column)
        elif series.nunique() < 10:
            low_cardinality_numeric_columns.append(column)
        else:
            continuous_columns.append(column)

    continuous_df = numeric_df[continuous_columns]

    summary = (
        continuous_df.describe().round(2).to_dict()
        if not continuous_df.empty
        else {}
    )

    extra_stats = {}

    for column in continuous_columns:
        series = numeric_df[column].dropna()

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = series[
            (series < lower_bound) | (series > upper_bound)
        ]

        mean_value = series.mean()
        median_value = series.median()

        if median_value != 0:
            mean_median_gap_pct = abs(mean_value - median_value) / abs(median_value) * 100
        else:
            mean_median_gap_pct = None

        extra_stats[column] = {
            "mean": round(mean_value, 2),
            "median": round(median_value, 2),
            "variance": round(series.var(), 2),
            "iqr": round(iqr, 2),
            "outlier_count": int(len(outliers)),
            "outlier_percent": round(len(outliers) / len(series) * 100, 2),
            "mean_median_gap_percent": round(mean_median_gap_pct, 2)
            if mean_median_gap_pct is not None
            else None,
            "skew_warning": (
                mean_median_gap_pct is not None
                and mean_median_gap_pct > 20
            ),
            "round_number_max_check": detect_round_number_max(series),
        }

    binary_summary = {
        column: summarize_binary_column(numeric_df[column])
        for column in binary_columns
    }

    low_cardinality_summary = {}

    for column in low_cardinality_numeric_columns:
        series = numeric_df[column].dropna()
        counts = series.value_counts().sort_index()
        percents = (series.value_counts(normalize=True).sort_index() * 100).round(2)

        low_cardinality_summary[column] = {
            "unique_values": int(series.nunique()),
            "values": counts.to_dict(),
            "value_percent": percents.to_dict(),
            "note": "Low-cardinality numeric variable; verify whether this should be treated as categorical or ordinal."
        }

    categorical_summary = summarize_categorical_columns(df, id_columns)

    return {
        "excluded_id_columns": id_columns,
        "continuous_numeric_columns": continuous_columns,
        "binary_columns": binary_columns,
        "low_cardinality_numeric_columns": low_cardinality_numeric_columns,
        "categorical_columns": list(categorical_summary.keys()),
        "summary": summary,
        "extra_stats": extra_stats,
        "binary_summary": binary_summary,
        "low_cardinality_summary": low_cardinality_summary,
        "categorical_summary": categorical_summary,
    }