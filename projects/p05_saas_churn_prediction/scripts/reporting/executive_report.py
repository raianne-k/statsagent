from pathlib import Path

import pandas as pd


BASE_DIR = Path("projects/p05_saas_churn_prediction")
OUTPUT_DIR = BASE_DIR / "outputs"

REPORT_PATH = OUTPUT_DIR / "reports" / "executive_churn_report.html"

BRAND_MAIN = "#81A0CE"
BRAND_SECONDARY = "#3F4247"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    return pd.read_csv(path)


def df_to_html_table(df: pd.DataFrame, max_rows: int = 10) -> str:
    return df.head(max_rows).to_html(index=False, classes="data-table", border=0)


def fmt(val) -> str:
    """Format a numeric value to 4 decimal places if float, else return as-is."""
    try:
        return f"{float(val):.4f}"
    except (ValueError, TypeError):
        return str(val)


def main():
    metrics = read_csv(OUTPUT_DIR / "prediction" / "model_metrics.csv")
    thresholds = read_csv(OUTPUT_DIR / "prediction" / "threshold_comparison.csv")
    features = read_csv(OUTPUT_DIR / "prediction" / "feature_importance.csv")
    health_segments = read_csv(OUTPUT_DIR / "segmentation" / "health_band_comparison.csv")
    contract_segments = read_csv(OUTPUT_DIR / "segmentation" / "contract_type_comparison.csv")
    correlations = read_csv(OUTPUT_DIR / "relationships" / "continuous_variable_correlations.csv")

    model = metrics.iloc[0]

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SaaS Churn Prediction — Executive Report</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --brand:      {BRAND_MAIN};
      --brand-dark: #5f7fae;
      --ink:        {BRAND_SECONDARY};
      --ink-light:  #6b7280;
      --surface:    #f7f8fa;
      --surface-2:  #eef1f6;
      --border:     #dde3ee;
      --white:      #ffffff;
      --accent-r:   #e07070;
      --radius:     10px;
      --shadow:     0 2px 12px rgba(129,160,206,.13);
    }}

    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: 'Sora', sans-serif;
      background: var(--surface);
      color: var(--ink);
      line-height: 1.65;
      font-size: 14px;
    }}

    /* ── HEADER ─────────────────────────────────────────── */
    .report-header {{
      background: var(--ink);
      color: var(--white);
      padding: 52px 64px 44px;
      position: relative;
      overflow: hidden;
    }}
    .report-header::before {{
      content: '';
      position: absolute;
      top: -60px; right: -60px;
      width: 340px; height: 340px;
      border-radius: 50%;
      background: var(--brand);
      opacity: .12;
    }}
    .report-header::after {{
      content: '';
      position: absolute;
      bottom: -80px; right: 120px;
      width: 200px; height: 200px;
      border-radius: 50%;
      background: var(--brand);
      opacity: .07;
    }}
    .header-eyebrow {{
      font-size: 11px;
      font-weight: 600;
      letter-spacing: .16em;
      text-transform: uppercase;
      color: var(--brand);
      margin-bottom: 14px;
    }}
    .report-header h1 {{
      font-size: 32px;
      font-weight: 700;
      line-height: 1.2;
      margin-bottom: 10px;
      position: relative;
    }}
    .header-sub {{
      font-size: 13px;
      color: rgba(255,255,255,.55);
      font-weight: 300;
    }}
    .header-meta {{
      margin-top: 28px;
      display: flex;
      gap: 32px;
      font-size: 12px;
      color: rgba(255,255,255,.45);
      position: relative;
    }}
    .header-meta span strong {{
      color: rgba(255,255,255,.75);
      font-weight: 500;
    }}

    /* ── LAYOUT ─────────────────────────────────────────── */
    .report-body {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 48px 40px 80px;
    }}

    /* ── SECTION ────────────────────────────────────────── */
    section {{
      margin-bottom: 52px;
    }}
    .section-label {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
    }}
    .section-label h2 {{
      font-size: 15px;
      font-weight: 600;
      letter-spacing: .04em;
      text-transform: uppercase;
      color: var(--ink);
    }}
    .section-label::before {{
      content: '';
      display: block;
      width: 4px;
      height: 20px;
      border-radius: 2px;
      background: var(--brand);
      flex-shrink: 0;
    }}

    /* ── EXEC SUMMARY CARD ──────────────────────────────── */
    .summary-card {{
      background: var(--white);
      border: 1px solid var(--border);
      border-left: 4px solid var(--brand);
      border-radius: var(--radius);
      padding: 28px 32px;
      box-shadow: var(--shadow);
      color: var(--ink-light);
      font-size: 14px;
      line-height: 1.75;
    }}
    .summary-card p + p {{ margin-top: 12px; }}

    /* ── METRIC CARDS ───────────────────────────────────── */
    .metric-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 16px;
    }}
    .metric-card {{
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 22px 24px 20px;
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
    }}
    .metric-card::after {{
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 3px;
      background: var(--brand);
    }}
    .metric-label {{
      font-size: 11px;
      font-weight: 600;
      letter-spacing: .1em;
      text-transform: uppercase;
      color: var(--ink-light);
      margin-bottom: 10px;
    }}
    .metric-value {{
      font-family: 'DM Mono', monospace;
      font-size: 26px;
      font-weight: 500;
      color: var(--ink);
      letter-spacing: -.01em;
    }}
    .metric-note {{
      margin-top: 6px;
      font-size: 11px;
      color: var(--ink-light);
    }}

    /* ── CALLOUT ────────────────────────────────────────── */
    .callout {{
      background: var(--surface-2);
      border-radius: var(--radius);
      padding: 14px 20px;
      font-size: 13px;
      color: var(--ink-light);
      border: 1px solid var(--border);
      margin-top: 14px;
    }}
    .callout strong {{ color: var(--ink); }}

    /* ── TABLES ─────────────────────────────────────────── */
    .table-wrap {{
      overflow-x: auto;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      background: var(--white);
      font-size: 13px;
    }}
    .data-table thead tr {{
      background: var(--ink);
      color: var(--white);
    }}
    .data-table thead th {{
      padding: 13px 16px;
      text-align: left;
      font-weight: 500;
      font-size: 11px;
      letter-spacing: .08em;
      text-transform: uppercase;
      white-space: nowrap;
    }}
    .data-table tbody tr {{
      border-bottom: 1px solid var(--border);
      transition: background .15s;
    }}
    .data-table tbody tr:last-child {{ border-bottom: none; }}
    .data-table tbody tr:hover {{ background: var(--surface-2); }}
    .data-table tbody td {{
      padding: 11px 16px;
      font-family: 'DM Mono', monospace;
      font-size: 12.5px;
      color: var(--ink);
    }}
    .data-table tbody td:first-child {{
      font-family: 'Sora', sans-serif;
      font-weight: 500;
      color: var(--ink);
    }}

    /* ── TWO-COL ────────────────────────────────────────── */
    .two-col {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }}
    .two-col .section-label {{ margin-bottom: 14px; }}
    .two-col h3 {{
      font-size: 13px;
      font-weight: 600;
      color: var(--ink-light);
      text-transform: uppercase;
      letter-spacing: .06em;
      margin-bottom: 12px;
    }}

    /* ── GOVERNANCE ─────────────────────────────────────── */
    .governance {{
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 28px 32px;
      box-shadow: var(--shadow);
      display: flex;
      gap: 20px;
      align-items: flex-start;
    }}
    .governance-icon {{
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--surface-2);
      border: 2px solid var(--brand);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      font-size: 16px;
      margin-top: 2px;
    }}
    .governance-text h3 {{
      font-size: 13px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: .08em;
      margin-bottom: 8px;
      color: var(--ink);
    }}
    .governance-text p {{
      font-size: 13px;
      color: var(--ink-light);
      line-height: 1.7;
    }}

    /* ── FOOTER ─────────────────────────────────────────── */
    .report-footer {{
      border-top: 1px solid var(--border);
      margin-top: 64px;
      padding-top: 24px;
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      color: var(--ink-light);
    }}

    @media (max-width: 780px) {{
      .metric-grid {{ grid-template-columns: 1fr 1fr; }}
      .two-col {{ grid-template-columns: 1fr; }}
      .report-header {{ padding: 36px 28px 30px; }}
      .report-body {{ padding: 32px 20px 60px; }}
    }}
  </style>
</head>
<body>

<!-- ══ HEADER ══════════════════════════════════════════════ -->
<header class="report-header">
  <div class="header-eyebrow">Analytical Report · p05_saas_churn_prediction</div>
  <h1>SaaS Churn Prediction<br>Executive Report</h1>
  <p class="header-sub">Decision-support signals for customer retention operations</p>
  <div class="header-meta">
    <span><strong>Project</strong> p05_saas_churn_prediction</span>
    <span><strong>Model</strong> Logistic Regression Baseline</span>
    <span><strong>Status</strong> Exploratory / Portfolio</span>
  </div>
</header>

<!-- ══ BODY ════════════════════════════════════════════════ -->
<main class="report-body">

  <!-- EXECUTIVE SUMMARY -->
  <section>
    <div class="section-label"><h2>Executive Summary</h2></div>
    <div class="summary-card">
      <p>
        This report summarises the churn-prediction baseline built on a synthetic SaaS customer dataset.
        The model ingests behavioural, product-usage, support, and account-health signals to surface accounts
        most likely to churn before renewal.
      </p>
      <p>
        The intent is <strong>decision support, not automation</strong>: outputs help customer-success teams
        prioritise outreach rather than trigger any automated action. All predictions should pass
        human review before influencing retention workflows.
      </p>
    </div>
  </section>

  <!-- MODEL PERFORMANCE -->
  <section>
    <div class="section-label"><h2>Model Performance</h2></div>
    <div class="metric-grid">
      <div class="metric-card">
        <div class="metric-label">Accuracy</div>
        <div class="metric-value">{fmt(model["accuracy"])}</div>
        <div class="metric-note">Overall correct classifications</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Precision</div>
        <div class="metric-value">{fmt(model["precision"])}</div>
        <div class="metric-note">Of flagged accounts, truly at risk</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Recall</div>
        <div class="metric-value">{fmt(model["recall"])}</div>
        <div class="metric-note">Actual churners correctly caught</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">ROC AUC</div>
        <div class="metric-value">{fmt(model["roc_auc"])}</div>
        <div class="metric-note">Discrimination ability (1.0 = perfect)</div>
      </div>
    </div>
    <div class="callout">
      <strong>Threshold context:</strong> Accuracy alone is insufficient for churn workflows.
      Recall and threshold tradeoffs matter because missed churn-risk accounts typically carry
      higher business cost than reviewing false positives.
    </div>
  </section>

  <!-- THRESHOLD TRADEOFFS -->
  <section>
    <div class="section-label"><h2>Threshold Tradeoffs</h2></div>
    <div class="table-wrap">
      {df_to_html_table(thresholds, max_rows=10)}
    </div>
    <div class="callout">
      Adjusting the probability threshold shifts the precision–recall balance.
      Lower thresholds cast a wider net; higher thresholds reduce review volume at the cost of missed accounts.
    </div>
  </section>

  <!-- TOP FEATURE SIGNALS -->
  <section>
    <div class="section-label"><h2>Top Feature Signals</h2></div>
    <div class="table-wrap">
      {df_to_html_table(features, max_rows=12)}
    </div>
    <div class="callout">
      <strong>Note:</strong> Feature importance reflects the model's learned coefficients and does not
      imply causal relationships between these signals and customer churn.
    </div>
  </section>

  <!-- SEGMENTATION -->
  <section>
    <div class="section-label"><h2>Segmentation Context</h2></div>
    <div class="two-col">
      <div>
        <h3>Health Band Comparison</h3>
        <div class="table-wrap">
          {df_to_html_table(health_segments, max_rows=10)}
        </div>
      </div>
      <div>
        <h3>Contract Type Comparison</h3>
        <div class="table-wrap">
          {df_to_html_table(contract_segments, max_rows=10)}
        </div>
      </div>
    </div>
  </section>

  <!-- CORRELATIONS -->
  <section>
    <div class="section-label"><h2>Strongest Continuous Relationships with Churn</h2></div>
    <div class="table-wrap">
      {df_to_html_table(correlations, max_rows=10)}
    </div>
  </section>

  <!-- GOVERNANCE -->
  <section>
    <div class="section-label"><h2>Governance</h2></div>
    <div class="governance">
      <div class="governance-icon">⚠</div>
      <div class="governance-text">
        <h3>Human-in-the-loop requirement</h3>
        <p>
          This is an AI-assisted analytical output produced for portfolio and exploratory purposes.
          All predictions are <strong>decision-support signals only</strong> and must not trigger
          automated customer-success or retention actions without explicit human review and sign-off.
          Feature importance coefficients do not establish causality and should not be used as
          sole justification for operational changes.
        </p>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="report-footer">
    <span>p05_saas_churn_prediction · Executive Report</span>
    <span>Analytical output — not for automated decision-making</span>
  </footer>

</main>
</body>
</html>"""

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(html, encoding="utf-8")
    print(f"Saved executive report → {REPORT_PATH}")


if __name__ == "__main__":
    main()
