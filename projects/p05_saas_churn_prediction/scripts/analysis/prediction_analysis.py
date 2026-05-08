from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATA_PATH = Path(
    "projects/p05_saas_churn_prediction/data/cleaned/saas_churn_prediction_cleaned.csv"
)

OUTPUT_DIR = Path(
    "projects/p05_saas_churn_prediction/outputs/prediction"
)


TARGET = "churned"


NUMERIC_FEATURES = [
    "monthly_recurring_revenue",
    "tenure_months",
    "weekly_active_users",
    "feature_adoption_rate",
    "login_frequency_30d",
    "avg_session_duration_minutes",
    "support_ticket_count_90d",
    "unresolved_ticket_count",
    "nps_score",
    "account_health_score",
    "seat_utilization_percent",
    "days_since_last_login",
]

BINARY_FEATURES = [
    "multi_product_adoption",
    "onboarding_completed",
    "support_escalation_flag",
    "renewal_meeting_completed",
    "discount_received",
]

CATEGORICAL_FEATURES = [
    "region",
    "industry",
    "company_size",
    "plan_tier",
    "contract_type",
]


def save_table(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def build_model_pipeline() -> Pipeline:
    numeric_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", numeric_transformer, NUMERIC_FEATURES),
            ("binary", "passthrough", BINARY_FEATURES),
            ("categorical", categorical_transformer, CATEGORICAL_FEATURES),
        ]
    )

    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42,
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    return pipeline


def evaluate_thresholds(y_true, y_probability) -> pd.DataFrame:
    rows = []

    for threshold in [0.30, 0.40, 0.50, 0.60, 0.70]:
        y_pred = (y_probability >= threshold).astype(int)

        tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

        rows.append({
            "threshold": threshold,
            "accuracy": round(accuracy_score(y_true, y_pred), 3),
            "precision": round(precision_score(y_true, y_pred, zero_division=0), 3),
            "recall": round(recall_score(y_true, y_pred, zero_division=0), 3),
            "f1_score": round(f1_score(y_true, y_pred, zero_division=0), 3),
            "true_positives": int(tp),
            "false_positives": int(fp),
            "true_negatives": int(tn),
            "false_negatives": int(fn),
            "accounts_flagged_percent": round(y_pred.mean() * 100, 2),
        })

    return pd.DataFrame(rows)


def extract_feature_importance(pipeline: Pipeline) -> pd.DataFrame:
    preprocessor = pipeline.named_steps["preprocessor"]
    model = pipeline.named_steps["model"]

    numeric_names = NUMERIC_FEATURES
    binary_names = BINARY_FEATURES

    categorical_names = (
        preprocessor
        .named_transformers_["categorical"]
        .named_steps["onehot"]
        .get_feature_names_out(CATEGORICAL_FEATURES)
        .tolist()
    )

    feature_names = numeric_names + binary_names + categorical_names

    coefficients = model.coef_[0]

    importance = pd.DataFrame({
        "feature": feature_names,
        "coefficient": coefficients,
        "absolute_coefficient": abs(coefficients),
    })

    importance["direction"] = importance["coefficient"].apply(
        lambda value: "increases_churn_probability" if value > 0 else "decreases_churn_probability"
    )

    importance = importance.sort_values(
        by="absolute_coefficient",
        ascending=False,
    )

    importance["coefficient"] = importance["coefficient"].round(4)
    importance["absolute_coefficient"] = importance["absolute_coefficient"].round(4)

    return importance


def main():
    df = pd.read_csv(DATA_PATH)

    feature_columns = NUMERIC_FEATURES + BINARY_FEATURES + CATEGORICAL_FEATURES

    X = df[feature_columns]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    pipeline = build_model_pipeline()
    pipeline.fit(X_train, y_train)

    y_probability = pipeline.predict_proba(X_test)[:, 1]
    y_pred_default = (y_probability >= 0.50).astype(int)

    metrics = pd.DataFrame([{
        "model": "logistic_regression_balanced",
        "test_rows": len(y_test),
        "churn_rate_test_percent": round(y_test.mean() * 100, 2),
        "accuracy": round(accuracy_score(y_test, y_pred_default), 3),
        "precision": round(precision_score(y_test, y_pred_default, zero_division=0), 3),
        "recall": round(recall_score(y_test, y_pred_default, zero_division=0), 3),
        "f1_score": round(f1_score(y_test, y_pred_default, zero_division=0), 3),
        "roc_auc": round(roc_auc_score(y_test, y_probability), 3),
        "threshold_used": 0.50,
    }])

    threshold_table = evaluate_thresholds(y_test, y_probability)
    feature_importance = extract_feature_importance(pipeline)

    scored_accounts = X_test.copy()
    scored_accounts["actual_churned"] = y_test.values
    scored_accounts["predicted_churn_probability"] = y_probability.round(4)
    scored_accounts["predicted_churn_50_threshold"] = y_pred_default

    scored_accounts = scored_accounts.sort_values(
        by="predicted_churn_probability",
        ascending=False,
    )

    save_table(metrics, OUTPUT_DIR / "model_metrics.csv")
    save_table(threshold_table, OUTPUT_DIR / "threshold_comparison.csv")
    save_table(feature_importance, OUTPUT_DIR / "feature_importance.csv")
    save_table(scored_accounts, OUTPUT_DIR / "scored_test_accounts.csv")

    print("Saved model metrics")
    print("Saved threshold comparison")
    print("Saved feature importance")
    print("Saved scored test accounts")
    print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()