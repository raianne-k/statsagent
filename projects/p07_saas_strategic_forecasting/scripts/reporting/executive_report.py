from pathlib import Path

import pandas as pd


BASE_DIR = Path("projects/p07_saas_strategic_forecasting")
OUTPUT_DIR = BASE_DIR / "outputs"

REPORT_PATH = OUTPUT_DIR / "reports" / "executive_forecasting_report.html"

BRAND_MAIN = "#81A0CE"
BRAND_SECONDARY = "#3F4247"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    return pd.read_csv(path)


def df_to_html_table(df: pd.DataFrame, max_rows: int = 10) -> str:
    return df.head(max_rows).to_html(index=False, classes="data-table", border=0)


def fmt_number(value, decimals: int = 2) -> str:
    try:
        return f"{float(value):,.{decimals}f}"
    except (ValueError, TypeError):
        return str(value)


def fmt_percent(value, decimals: int = 1) -> str:
    try:
        return f"{float(value) * 100:.{decimals}f}%"
    except (ValueError, TypeError):
        return str(value)


def main():
    cohort_summary = read_csv(OUTPUT_DIR / "cohorts" / "cohort_summary.csv")
    operational_trends = read_csv(OUTPUT_DIR / "trends" / "operational_trends.csv")
    leading_indicators = read_csv(OUTPUT_DIR / "trends" / "leading_indicators.csv")

    retention_forecast = read_csv(
        OUTPUT_DIR / "forecasting" / "retention_forecast.csv"
    )
    churn_forecast = read_csv(
        OUTPUT_DIR / "forecasting" / "churn_risk_forecast.csv"
    )
    mrr_forecast = read_csv(
        OUTPUT_DIR / "forecasting" / "mrr_forecast.csv"
    )
    risk_forecast = read_csv(
        OUTPUT_DIR / "forecasting" / "revenue_at_risk_forecast.csv"
    )

    scenario_impact = read_csv(
        OUTPUT_DIR / "scenarios" / "scenario_revenue_impact.csv"
    )

    executive_segments = read_csv(
        OUTPUT_DIR / "segmentation" / "executive_segment_risk_table.csv"
    )

    risk_concentration = read_csv(
        OUTPUT_DIR / "segmentation" / "revenue_risk_concentration.csv"
    )

    latest_trend = operational_trends.iloc[-1]
    latest_retention = retention_forecast.iloc[-1]
    latest_churn = churn_forecast.iloc[-1]
    latest_mrr = mrr_forecast.iloc[-1]
    latest_risk = risk_forecast.iloc[-1]

    top_scenario = scenario_impact.sort_values(
        "projected_mrr_difference",
        ascending=False,
    ).iloc[0]

    top_risk_segment = risk_concentration.sort_values(
        "total_revenue_at_risk",
        ascending=False,
    ).iloc[0]

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SaaS Strategic Forecasting — Executive Report</title>
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
      flex-wrap: wrap;
    }}

    .header-meta span strong {{
      color: rgba(255,255,255,.75);
      font-weight: 500;
    }}

    .report-body {{
      max-width: 1120px;
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

<header class="report-header">
  <div class="header-eyebrow">Strategic Forecasting Report · p07_saas_strategic_forecasting</div>
  <h1>SaaS Strategic Forecasting<br>Executive Report</h1>
  <p class="header-sub">Governance-aware retention, engagement, scenario, and revenue-risk planning</p>
  <div class="header-meta">
    <span><strong>Project</strong> p07_saas_strategic_forecasting</span>
    <span><strong>Method</strong> Interpretable Forecasting</span>
    <span><strong>Status</strong> Exploratory / Portfolio</span>
  </div>
</header>

<main class="report-body">

  <section>
    <div class="section-label"><h2>Executive Summary</h2></div>
    <div class="summary-card">
      <p>
        This report summarizes a governance-aware SaaS strategic forecasting pipeline built on a synthetic
        longitudinal account-month dataset. The analysis evaluates cohort retention, product-health movement,
        leading operational indicators, revenue-at-risk exposure, scenario-adjusted future trajectories, and
        segment-level risk concentration.
      </p>
      <p>
        Projected MRR growth remains positive despite mild retention pressure, suggesting that account growth,
        expansion effects, and revenue mix may offset expected churn pressure over the forecast horizon.
      </p>
      <p>
        The purpose is <strong>executive decision support, not automated decision-making</strong>. Forecasts are
        probabilistic, scenario outputs depend on assumptions, and observed relationships should not be interpreted
        as causal proof.
      </p>
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Forecast Posture</h2></div>
    <div class="metric-grid">
      <div class="metric-card">
        <div class="metric-label">Projected Retention</div>
        <div class="metric-value">{fmt_percent(latest_retention["forecast_retention_rate"])}</div>
        <div class="metric-note">Final forecast horizon</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Projected Churn</div>
        <div class="metric-value">{fmt_percent(latest_churn["forecast_churn_rate"])}</div>
        <div class="metric-note">Final forecast horizon</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Projected MRR</div>
        <div class="metric-value">{fmt_number(latest_mrr["forecast_total_mrr"], 0)}</div>
        <div class="metric-note">Directional revenue trajectory</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Revenue at Risk</div>
        <div class="metric-value">{fmt_number(latest_risk["forecast_revenue_at_risk"], 0)}</div>
        <div class="metric-note">Uncertainty-aware exposure</div>
      </div>
    </div>
    <div class="callout">
      <strong>Forecast context:</strong> These projections use interpretable trend-based methods and widening
      forecast bands. They are planning estimates, not guaranteed outcomes.
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Current Operating Signals</h2></div>
    <div class="metric-grid">
      <div class="metric-card">
        <div class="metric-label">Avg Health</div>
        <div class="metric-value">{fmt_number(latest_trend["avg_product_health"], 3)}</div>
        <div class="metric-note">Latest observed month</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Avg Adoption</div>
        <div class="metric-value">{fmt_number(latest_trend["avg_feature_adoption"], 1)}</div>
        <div class="metric-note">Feature adoption rate</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Avg Inactivity</div>
        <div class="metric-value">{fmt_number(latest_trend["avg_days_since_last_login"], 1)}</div>
        <div class="metric-note">Days since last login</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Risk Rate</div>
        <div class="metric-value">{fmt_percent(latest_trend["revenue_at_risk_rate"])}</div>
        <div class="metric-note">Revenue at risk / MRR</div>
      </div>
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Scenario Impact Summary</h2></div>
    <div class="summary-card">
      <p>
        The strongest modeled scenario by projected MRR difference is
        <strong>{top_scenario["scenario"]}</strong>, with an estimated final-horizon MRR difference of
        <strong>{fmt_number(top_scenario["projected_mrr_difference"], 2)}</strong> versus the baseline scenario.
      </p>
      <p>
        This difference reflects transparent operational assumptions, not proven causal impact.
      </p>
    </div>
    <div class="table-wrap">
      {df_to_html_table(scenario_impact, max_rows=10)}
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Revenue-Risk Concentration</h2></div>
    <div class="summary-card">
      <p>
        The largest current revenue-risk exposure is concentrated in the
        <strong>{top_risk_segment["health_band"]}</strong> /
        <strong>{top_risk_segment["mrr_band"]}</strong> segment, with
        <strong>{fmt_number(top_risk_segment["total_revenue_at_risk"], 2)}</strong>
        in observed revenue at risk.
      </p>
      <p>
        The risk concentration ratio compares a segment's share of total revenue risk against its share of total MRR.
        Ratios above 1.0 indicate that risk is overrepresented relative to revenue size.
      </p>
    </div>
    <div class="table-wrap">
      {df_to_html_table(risk_concentration, max_rows=12)}
    </div>
    <div class="callout">
      <strong>Interpretation:</strong> This analysis supports prioritization by exposure concentration.
      It should guide investigation and resource allocation, not automate customer intervention.
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Forecast Tables</h2></div>
    <div class="two-col">
      <div>
        <h3>Retention Forecast</h3>
        <div class="table-wrap">
          {df_to_html_table(retention_forecast, max_rows=8)}
        </div>
      </div>
      <div>
        <h3>MRR Forecast</h3>
        <div class="table-wrap">
          {df_to_html_table(mrr_forecast, max_rows=8)}
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Cohort & Operational Context</h2></div>
    <div class="two-col">
      <div>
        <h3>Cohort Summary</h3>
        <div class="table-wrap">
          {df_to_html_table(cohort_summary, max_rows=10)}
        </div>
      </div>
      <div>
        <h3>Leading Indicators</h3>
        <div class="table-wrap">
          {df_to_html_table(leading_indicators, max_rows=10)}
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Executive Segment Risk</h2></div>
    <div class="table-wrap">
      {df_to_html_table(executive_segments, max_rows=12)}
    </div>
    <div class="callout">
      <strong>Interpretation:</strong> Segment risk concentration combines revenue exposure, churn risk,
      and product-health weakness. It should guide investigation rather than trigger automated intervention.
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Governance</h2></div>
    <div class="governance">
      <div class="governance-icon">⚠</div>
      <div class="governance-text">
        <h3>Human-in-the-loop forecasting requirement</h3>
        <p>
          This is an AI-assisted analytical output produced for portfolio and exploratory purposes.
          Forecasts are probabilistic, scenario models are assumption-dependent, and observational
          relationships do not establish causality. Outputs are intended to support executive discussion,
          prioritization, and planning, not automate strategic decisions or customer interventions.
        </p>
      </div>
    </div>
  </section>

  <footer class="report-footer">
    <span>p07_saas_strategic_forecasting · Executive Report</span>
    <span>Forecasting output — not for automated decision-making</span>
  </footer>

</main>
</body>
</html>"""

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(html, encoding="utf-8")
    print(f"Saved executive report → {REPORT_PATH}")


if __name__ == "__main__":
    main()