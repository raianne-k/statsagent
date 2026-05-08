from pathlib import Path

import pandas as pd
import streamlit as st


BASE_DIR = Path("projects/p05_saas_churn_prediction")
OUTPUT_DIR = BASE_DIR / "outputs"

# ── Brand ────────────────────────────────────────────────────────────
BRAND_MAIN = "#81A0CE"
BRAND_DARK  = "#3F4247"
# ─────────────────────────────────────────────────────────────────────

CUSTOM_CSS = f"""
<style>
/* ── Fonts ─────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {{
    font-family: 'Sora', sans-serif !important;
}}

/* ── App background ────────────────────────────────── */
.stApp {{
    background: #f7f8fa;
}}

/* ── Sidebar ───────────────────────────────────────── */
[data-testid="stSidebar"] {{
    background: {BRAND_DARK} !important;
    border-right: none !important;
}}
[data-testid="stSidebar"] * {{
    color: rgba(255,255,255,0.82) !important;
}}
[data-testid="stSidebar"] .sidebar-title {{
    color: {BRAND_MAIN} !important;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: .15em;
    text-transform: uppercase;
    margin-bottom: 4px;
}}
[data-testid="stSidebar"] hr {{
    border-color: rgba(255,255,255,0.1) !important;
    margin: 16px 0 !important;
}}
[data-testid="stSidebar"] .stSlider label {{
    color: rgba(255,255,255,0.6) !important;
    font-size: 11px;
    letter-spacing: .06em;
    text-transform: uppercase;
}}

/* ── Top bar / header ──────────────────────────────── */
.report-header {{
    background: {BRAND_DARK};
    border-radius: 12px;
    padding: 32px 36px 28px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}}
.report-header::before {{
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 220px; height: 220px;
    border-radius: 50%;
    background: {BRAND_MAIN};
    opacity: .10;
}}
.report-header .eyebrow {{
    font-size: 11px;
    font-weight: 600;
    letter-spacing: .18em;
    text-transform: uppercase;
    color: {BRAND_MAIN};
    margin-bottom: 10px;
}}
.report-header h1 {{
    font-size: 26px;
    font-weight: 700;
    color: #ffffff;
    margin: 0 0 6px 0;
    line-height: 1.25;
}}
.report-header .sub {{
    font-size: 13px;
    color: rgba(255,255,255,.45);
    font-weight: 300;
}}

/* ── Section headings ──────────────────────────────── */
.section-heading {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 36px 0 16px;
}}
.section-heading::before {{
    content: '';
    display: block;
    width: 4px;
    height: 18px;
    border-radius: 2px;
    background: {BRAND_MAIN};
    flex-shrink: 0;
}}
.section-heading h2 {{
    font-size: 13px;
    font-weight: 600;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: {BRAND_DARK};
    margin: 0;
}}

/* ── Metric cards ──────────────────────────────────── */
[data-testid="stMetric"] {{
    background: #ffffff;
    border: 1px solid #dde3ee;
    border-radius: 10px;
    padding: 18px 20px 16px !important;
    box-shadow: 0 2px 10px rgba(129,160,206,.10);
    position: relative;
    overflow: hidden;
}}
[data-testid="stMetric"]::before {{
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: {BRAND_MAIN};
    border-radius: 10px 10px 0 0;
}}
[data-testid="stMetricLabel"] {{
    font-size: 10px !important;
    font-weight: 600 !important;
    letter-spacing: .12em !important;
    text-transform: uppercase !important;
    color: #6b7280 !important;
}}
[data-testid="stMetricValue"] {{
    font-family: 'DM Mono', monospace !important;
    font-size: 24px !important;
    font-weight: 500 !important;
    color: {BRAND_DARK} !important;
}}

/* ── Flagged accounts metric ───────────────────────── */
.flagged-metric {{
    background: #ffffff;
    border: 1px solid #dde3ee;
    border-left: 4px solid {BRAND_MAIN};
    border-radius: 10px;
    padding: 18px 24px;
    box-shadow: 0 2px 10px rgba(129,160,206,.10);
    margin-bottom: 16px;
}}
.flagged-metric .label {{
    font-size: 11px;
    font-weight: 600;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: #6b7280;
    margin-bottom: 6px;
}}
.flagged-metric .value {{
    font-family: 'DM Mono', monospace;
    font-size: 28px;
    font-weight: 500;
    color: {BRAND_DARK};
}}

/* ── Dataframes ────────────────────────────────────── */
[data-testid="stDataFrame"] {{
    border: 1px solid #dde3ee !important;
    border-radius: 10px !important;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(129,160,206,.08);
}}

/* ── Bar chart ─────────────────────────────────────── */
[data-testid="stArrowVegaLiteChart"] {{
    border: 1px solid #dde3ee;
    border-radius: 10px;
    padding: 12px;
    background: #ffffff;
    box-shadow: 0 2px 10px rgba(129,160,206,.08);
}}

/* ── Sliders ───────────────────────────────────────── */
[data-testid="stSlider"] {{
    padding: 4px 0;
}}
.stSlider [data-baseweb="slider"] div[data-testid="stTickBar"] {{
    color: #6b7280 !important;
}}

/* ── Divider ───────────────────────────────────────── */
hr {{
    border: none !important;
    border-top: 1px solid #dde3ee !important;
    margin: 28px 0 !important;
}}

/* ── Callout / info boxes ──────────────────────────── */
.callout {{
    background: #eef1f6;
    border: 1px solid #dde3ee;
    border-radius: 8px;
    padding: 13px 18px;
    font-size: 13px;
    color: #6b7280;
    margin: 10px 0 20px;
    line-height: 1.65;
}}

/* ── Warning (governance) ──────────────────────────── */
[data-testid="stAlertContainer"] {{
    border-radius: 10px !important;
    border: 1px solid #dde3ee !important;
    background: #ffffff !important;
    box-shadow: 0 2px 10px rgba(129,160,206,.08) !important;
}}

/* ── Scrollbar ─────────────────────────────────────── */
::-webkit-scrollbar {{ width: 6px; height: 6px; }}
::-webkit-scrollbar-track {{ background: #f7f8fa; }}
::-webkit-scrollbar-thumb {{ background: #c9d4e4; border-radius: 4px; }}
</style>
"""


@st.cache_data
def load_outputs():
    metrics          = pd.read_csv(OUTPUT_DIR / "prediction"   / "model_metrics.csv")
    thresholds       = pd.read_csv(OUTPUT_DIR / "prediction"   / "threshold_comparison.csv")
    features         = pd.read_csv(OUTPUT_DIR / "prediction"   / "feature_importance.csv")
    scored           = pd.read_csv(OUTPUT_DIR / "prediction"   / "scored_test_accounts.csv")
    health_segments  = pd.read_csv(OUTPUT_DIR / "segmentation" / "health_band_comparison.csv")
    contract_segments= pd.read_csv(OUTPUT_DIR / "segmentation" / "contract_type_comparison.csv")
    correlations     = pd.read_csv(OUTPUT_DIR / "relationships" / "continuous_variable_correlations.csv")
    return metrics, thresholds, features, scored, health_segments, contract_segments, correlations


def section(title: str) -> None:
    st.markdown(
        f'<div class="section-heading"><h2>{title}</h2></div>',
        unsafe_allow_html=True,
    )


def callout(text: str) -> None:
    st.markdown(f'<div class="callout">{text}</div>', unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title="SaaS Churn · Executive Dashboard",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Inject custom CSS
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

    # Load data
    metrics, thresholds, features, scored, health_segments, contract_segments, correlations = load_outputs()
    model = metrics.iloc[0]

    # ── SIDEBAR ──────────────────────────────────────────────────────
    with st.sidebar:
        st.markdown('<div class="sidebar-title">StatsAgent</div>', unsafe_allow_html=True)
        st.markdown("**SaaS Churn Prediction**")
        st.markdown("p05 · Portfolio / Exploratory")
        st.markdown("---")

        st.markdown("##### Controls")

        top_n = st.slider(
            "Feature signals to display",
            min_value=5, max_value=25, value=10, step=1,
        )

        threshold = st.slider(
            "Churn probability threshold",
            min_value=0.10, max_value=0.90, value=0.50, step=0.05,
            format="%.2f",
        )

        st.markdown("---")
        st.markdown(
            "<small style='color:rgba(255,255,255,.35);font-size:11px;'>"
            "Predictions are decision-support signals only. "
            "Human review required before operational actions."
            "</small>",
            unsafe_allow_html=True,
        )

    # ── HEADER ───────────────────────────────────────────────────────
    st.markdown("""
    <div class="report-header">
      <div class="eyebrow">Executive Dashboard · p05_saas_churn_prediction</div>
      <h1>SaaS Churn Prediction</h1>
      <div class="sub">Decision-support signals for customer retention operations</div>
    </div>
    """, unsafe_allow_html=True)

    # ── MODEL PERFORMANCE ─────────────────────────────────────────────
    section("Model Performance")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Accuracy",  f"{float(model['accuracy']):.4f}")
    c2.metric("Precision", f"{float(model['precision']):.4f}")
    c3.metric("Recall",    f"{float(model['recall']):.4f}")
    c4.metric("ROC AUC",   f"{float(model['roc_auc']):.4f}")

    callout(
        "Accuracy alone is insufficient for churn workflows. Recall and threshold tradeoffs matter "
        "because missed churn-risk accounts typically carry a higher business cost than false positives."
    )

    st.divider()

    # ── THRESHOLD TRADEOFFS ───────────────────────────────────────────
    section("Threshold Tradeoffs")
    callout(
        "Adjusting the probability threshold shifts the precision–recall balance. "
        "Lower thresholds widen the review net; higher thresholds reduce volume at the cost of missed accounts."
    )
    st.dataframe(thresholds, use_container_width=True, hide_index=True)

    st.divider()

    # ── FEATURE SIGNALS ───────────────────────────────────────────────
    section("Top Churn Signals")

    top_features = features.head(top_n)

    chart_col, table_col = st.columns([1.4, 1])

    with chart_col:
        chart_data = (
            top_features
            .set_index("feature")["absolute_coefficient"]
            .sort_values()
        )
        st.bar_chart(chart_data, color=BRAND_MAIN, height=340)

    with table_col:
        st.dataframe(top_features, use_container_width=True, hide_index=True, height=340)

    callout(
        "<strong>Note:</strong> Feature importance reflects model coefficients. "
        "It does not imply causal relationships between these signals and churn."
    )

    st.divider()

    # ── SEGMENTATION ─────────────────────────────────────────────────
    section("Segmentation Context")

    left, right = st.columns(2)

    with left:
        st.markdown("##### Health Band Comparison")
        st.dataframe(health_segments, use_container_width=True, hide_index=True)

    with right:
        st.markdown("##### Contract Type Comparison")
        st.dataframe(contract_segments, use_container_width=True, hide_index=True)

    st.divider()

    # ── CORRELATIONS ──────────────────────────────────────────────────
    section("Continuous Relationships with Churn")
    st.dataframe(correlations.head(15), use_container_width=True, hide_index=True)

    st.divider()

    # ── SCORED ACCOUNTS ───────────────────────────────────────────────
    section("Scored Test Accounts")

    scored_view = scored.copy()
    scored_view["flagged_for_review"] = (
        scored_view["predicted_churn_probability"] >= threshold
    )

    flagged_count = int(scored_view["flagged_for_review"].sum())
    flagged_rate  = round(flagged_count / len(scored_view) * 100, 2)

    st.markdown(
        f"""<div class="flagged-metric">
          <div class="label">Accounts flagged for review @ threshold {threshold:.2f}</div>
          <div class="value">{flagged_count} <span style="font-size:16px;color:#6b7280;">({flagged_rate}%)</span></div>
        </div>""",
        unsafe_allow_html=True,
    )

    st.dataframe(
        scored_view
        .sort_values("predicted_churn_probability", ascending=False)
        .head(100),
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    # ── GOVERNANCE ────────────────────────────────────────────────────
    st.warning(
        "**Governance:** Predictions are decision-support signals only. "
        "They must not trigger automated customer-success or retention actions "
        "without explicit human review and sign-off.",
        icon="⚠️",
    )


if __name__ == "__main__":
    main()
