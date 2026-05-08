from pathlib import Path

import pandas as pd


BASE_DIR = Path("projects/p06_product_experimentation")
OUTPUT_DIR = BASE_DIR / "outputs"

REPORT_PATH = OUTPUT_DIR / "reports" / "executive_experiment_report.html"

BRAND_MAIN = "#81A0CE"
BRAND_SECONDARY = "#3F4247"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    return pd.read_csv(path)


def df_to_html_table(df: pd.DataFrame, max_rows: int = 10) -> str:
    return df.head(max_rows).to_html(index=False, classes="data-table", border=0)


def fmt(value, digits: int = 2) -> str:
    try:
        return f"{float(value):.{digits}f}"
    except (ValueError, TypeError):
        return str(value)


def main():
    integrity = read_csv(OUTPUT_DIR / "experimentation" / "experiment_integrity_review.csv")
    binary_results = read_csv(OUTPUT_DIR / "experimentation" / "binary_metric_experiment_results.csv")
    continuous_results = read_csv(OUTPUT_DIR / "experimentation" / "continuous_metric_experiment_results.csv")
    balance = read_csv(OUTPUT_DIR / "experimentation" / "randomization_balance_check.csv")
    segment_summary = read_csv(OUTPUT_DIR / "segmentation" / "segment_profile_summary.csv")
    relationships = read_csv(OUTPUT_DIR / "relationships" / "overall_metric_outcome_correlations.csv")

    primary_metrics = binary_results[
        binary_results["metric"].isin(["activation_flag", "retained_30d"])
    ]

    activation_row = binary_results[binary_results["metric"] == "activation_flag"].iloc[0]
    retention_row = binary_results[binary_results["metric"] == "retained_30d"].iloc[0]

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>Product Experimentation — Executive Report</title>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet" />

  <style>
    :root {{
      --brand: {BRAND_MAIN};
      --brand-dark: #5f7fae;
      --ink: {BRAND_SECONDARY};
      --ink-light: #6b7280;
      --surface: #f7f8fa;
      --surface-2: #eef1f6;
      --border: #dde3ee;
      --white: #ffffff;
      --radius: 10px;
      --shadow: 0 2px 12px rgba(129,160,206,.13);
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Sora', sans-serif;
      background: var(--surface);
      color: var(--ink);
      line-height: 1.65;
      font-size: 14px;
    }}

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
      top: -60px;
      right: -60px;
      width: 340px;
      height: 340px;
      border-radius: 50%;
      background: var(--brand);
      opacity: .12;
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
      position: relative;
    }}

    .header-meta {{
      margin-top: 28px;
      display: flex;
      gap: 32px;
      font-size: 12px;
      color: rgba(255,255,255,.45);
      position: relative;
    }}

    .header-meta strong {{
      color: rgba(255,255,255,.75);
      font-weight: 500;
    }}

    .report-body {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 48px 40px 80px;
    }}

    section {{
      margin-bottom: 52px;
    }}

    .section-label {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
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

    .section-label h2 {{
      font-size: 15px;
      font-weight: 600;
      letter-spacing: .04em;
      text-transform: uppercase;
      color: var(--ink);
    }}

    .summary-card {{
      background: var(--white);
      border: 1px solid var(--border);
      border-left: 4px solid var(--brand);
      border-radius: var(--radius);
      padding: 28px 32px;
      box-shadow: var(--shadow);
      color: var(--ink-light);
      line-height: 1.75;
    }}

    .summary-card p + p {{
      margin-top: 12px;
    }}

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
      top: 0;
      left: 0;
      right: 0;
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
    }}

    .metric-note {{
      margin-top: 6px;
      font-size: 11px;
      color: var(--ink-light);
    }}

    .callout {{
      background: var(--surface-2);
      border-radius: var(--radius);
      padding: 14px 20px;
      font-size: 13px;
      color: var(--ink-light);
      border: 1px solid var(--border);
      margin-top: 14px;
    }}

    .callout strong {{
      color: var(--ink);
    }}

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
    }}

    .data-table tbody tr:last-child {{
      border-bottom: none;
    }}

    .data-table tbody tr:hover {{
      background: var(--surface-2);
    }}

    .data-table tbody td {{
      padding: 11px 16px;
      font-family: 'DM Mono', monospace;
      font-size: 12.5px;
      color: var(--ink);
      white-space: nowrap;
    }}

    .data-table tbody td:first-child {{
      font-family: 'Sora', sans-serif;
      font-weight: 500;
    }}

    .two-col {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }}

    .two-col h3 {{
      font-size: 13px;
      font-weight: 600;
      color: var(--ink-light);
      text-transform: uppercase;
      letter-spacing: .06em;
      margin-bottom: 12px;
    }}

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
    }}

    .governance h3 {{
      font-size: 13px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: .08em;
      margin-bottom: 8px;
    }}

    .governance p {{
      font-size: 13px;
      color: var(--ink-light);
      line-height: 1.7;
    }}

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
      .metric-grid,
      .two-col {{
        grid-template-columns: 1fr;
      }}

      .report-header {{
        padding: 36px 28px 30px;
      }}

      .report-body {{
        padding: 32px 20px 60px;
      }}
    }}
  </style>
</head>

<body>
<header class="report-header">
  <div class="header-eyebrow">Analytical Report · p06_product_experimentation</div>
  <h1>Product Experimentation<br>Executive Report</h1>
  <p class="header-sub">Onboarding experiment evidence for product rollout decisions</p>

  <div class="header-meta">
    <span><strong>Project</strong> p06_product_experimentation</span>
    <span><strong>Method</strong> A/B Experiment Analysis</span>
    <span><strong>Status</strong> Exploratory / Portfolio</span>
  </div>
</header>

<main class="report-body">

  <section>
    <div class="section-label"><h2>Executive Summary</h2></div>
    <div class="summary-card">
      <p>
        This report summarizes an onboarding A/B experiment comparing a control experience against a treatment experience.
        The analysis evaluates activation, retention, churn, monetization, and guardrail outcomes.
      </p>
      <p>
        The goal is not simply to identify statistically significant differences, but to determine whether the observed
        effects are practically meaningful, trustworthy, and appropriate for product rollout consideration.
      </p>
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Primary Experiment Outcomes</h2></div>

    <div class="metric-grid">
      <div class="metric-card">
        <div class="metric-label">Activation Control</div>
        <div class="metric-value">{fmt(activation_row["control_rate_percent"])}</div>
        <div class="metric-note">Control activation rate %</div>
      </div>

      <div class="metric-card">
        <div class="metric-label">Activation Treatment</div>
        <div class="metric-value">{fmt(activation_row["treatment_rate_percent"])}</div>
        <div class="metric-note">Treatment activation rate %</div>
      </div>

      <div class="metric-card">
        <div class="metric-label">Activation Lift</div>
        <div class="metric-value">{fmt(activation_row["absolute_lift_percentage_points"])}</div>
        <div class="metric-note">Percentage-point difference</div>
      </div>

      <div class="metric-card">
        <div class="metric-label">Activation P-value</div>
        <div class="metric-value">{fmt(activation_row["p_value"], 4)}</div>
        <div class="metric-note">Two-sided proportion test</div>
      </div>
    </div>

    <div class="metric-grid">
      <div class="metric-card">
        <div class="metric-label">Retention Control</div>
        <div class="metric-value">{fmt(retention_row["control_rate_percent"])}</div>
        <div class="metric-note">30-day retention rate %</div>
      </div>

      <div class="metric-card">
        <div class="metric-label">Retention Treatment</div>
        <div class="metric-value">{fmt(retention_row["treatment_rate_percent"])}</div>
        <div class="metric-note">30-day retention rate %</div>
      </div>

      <div class="metric-card">
        <div class="metric-label">Retention Lift</div>
        <div class="metric-value">{fmt(retention_row["absolute_lift_percentage_points"])}</div>
        <div class="metric-note">Percentage-point difference</div>
      </div>

      <div class="metric-card">
        <div class="metric-label">Retention P-value</div>
        <div class="metric-value">{fmt(retention_row["p_value"], 4)}</div>
        <div class="metric-note">Two-sided proportion test</div>
      </div>
    </div>

    <div class="callout">
      <strong>Interpretation rule:</strong> statistical significance should not be treated as automatic rollout approval.
      Product teams still need to evaluate practical significance, implementation cost, guardrail movement, and long-term risk.
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Experiment Integrity</h2></div>
    <div class="table-wrap">
      {df_to_html_table(integrity, max_rows=10)}
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Binary Outcome Results</h2></div>
    <div class="table-wrap">
      {df_to_html_table(binary_results, max_rows=12)}
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Continuous Outcome Results</h2></div>
    <div class="table-wrap">
      {df_to_html_table(continuous_results, max_rows=10)}
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Supporting Context</h2></div>
    <div class="two-col">
      <div>
        <h3>Largest Balance Differences</h3>
        <div class="table-wrap">
          {df_to_html_table(balance.sort_values("absolute_difference_percentage_points", ascending=False), max_rows=8)}
        </div>
      </div>

      <div>
        <h3>Strongest Metric Relationships</h3>
        <div class="table-wrap">
          {df_to_html_table(relationships, max_rows=8)}
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Segment Context</h2></div>
    <div class="table-wrap">
      {df_to_html_table(segment_summary, max_rows=12)}
    </div>
    <div class="callout">
      Segment outputs are used as treatment-effect context, not as a replacement for the randomized experiment.
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Governance</h2></div>

    <div class="governance">
      <div class="governance-icon">⚠</div>
      <div>
        <h3>Human-in-the-loop rollout decision</h3>
        <p>
          This experiment analysis is a decision-support artifact. It should not trigger automatic rollout.
          Results should be reviewed for assignment quality, exposure validity, statistical uncertainty,
          practical significance, and guardrail movement before product decisions are made.
        </p>
      </div>
    </div>
  </section>

  <footer class="report-footer">
    <span>p06_product_experimentation · Executive Report</span>
    <span>Analytical output — not an automated rollout decision</span>
  </footer>

</main>
</body>
</html>
"""

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(html, encoding="utf-8")

    print(f"Saved executive report → {REPORT_PATH}")


if __name__ == "__main__":
    main()