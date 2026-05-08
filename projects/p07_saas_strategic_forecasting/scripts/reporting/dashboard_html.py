from pathlib import Path
import json

import pandas as pd


BASE_DIR = Path("projects/p07_saas_strategic_forecasting")
OUTPUT_DIR = BASE_DIR / "outputs"

REPORT_PATH = OUTPUT_DIR / "dashboard" / "forecasting_dashboard.html"

BRAND_MAIN = "#81A0CE"
BRAND_SECONDARY = "#3F4247"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    return pd.read_csv(path)


def records_for_js(df: pd.DataFrame, max_rows: int | None = None) -> str:
    if max_rows is not None:
        df = df.head(max_rows)

    clean = df.copy()
    clean = clean.where(pd.notnull(clean), None)

    return json.dumps(clean.to_dict(orient="records"))


def fmt(value, digits: int = 2) -> str:
    try:
        return f"{float(value):.{digits}f}"
    except (ValueError, TypeError):
        return str(value)


def main():
    cohort_summary = read_csv(
        OUTPUT_DIR / "cohorts" / "cohort_summary.csv"
    )

    operational_trends = read_csv(
        OUTPUT_DIR / "trends" / "operational_trends.csv"
    )

    leading_indicators = read_csv(
        OUTPUT_DIR / "trends" / "leading_indicators.csv"
    )

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

    latest_retention = retention_forecast.iloc[-1]
    latest_churn = churn_forecast.iloc[-1]
    latest_mrr = mrr_forecast.iloc[-1]
    latest_risk = risk_forecast.iloc[-1]

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>SaaS Strategic Forecasting Dashboard</title>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet" />

  <script src="https://cdn.plot.ly/plotly-2.30.0.min.js"></script>

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
      --danger: #e07070;
      --success: #7aa874;
      --radius: 10px;
      --shadow: 0 2px 12px rgba(129,160,206,.13);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Sora', sans-serif;
      background: var(--surface);
      color: var(--ink);
      line-height: 1.6;
      font-size: 14px;
    }}

    .dashboard-header {{
      background: var(--ink);
      color: var(--white);
      padding: 44px 64px 38px;
      position: relative;
      overflow: hidden;
    }}

    .dashboard-header::before {{
      content: '';
      position: absolute;
      top: -60px;
      right: -60px;
      width: 320px;
      height: 320px;
      border-radius: 50%;
      background: var(--brand);
      opacity: .12;
    }}

    .eyebrow {{
      font-size: 11px;
      font-weight: 600;
      letter-spacing: .16em;
      text-transform: uppercase;
      color: var(--brand);
      margin-bottom: 14px;
    }}

    .dashboard-header h1 {{
      font-size: 32px;
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

    .dashboard-body {{
      max-width: 1220px;
      margin: 0 auto;
      padding: 44px 40px 80px;
    }}

    section {{
      margin-bottom: 48px;
    }}

    .section-label {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 18px;
    }}

    .section-label::before {{
      content: '';
      display: block;
      width: 4px;
      height: 20px;
      border-radius: 2px;
      background: var(--brand);
    }}

    .section-label h2 {{
      font-size: 15px;
      font-weight: 600;
      letter-spacing: .04em;
      text-transform: uppercase;
      color: var(--ink);
    }}

    .metric-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 18px;
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
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 14px 20px;
      font-size: 13px;
      color: var(--ink-light);
      margin-top: 14px;
    }}

    .grid-two {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }}

    .panel {{
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      overflow: hidden;
    }}

    .panel-title {{
      padding: 14px 18px;
      background: var(--ink);
      color: var(--white);
      font-size: 11px;
      font-weight: 600;
      letter-spacing: .08em;
      text-transform: uppercase;
    }}

    .chart {{
      height: 420px;
      padding: 10px 14px 4px;
    }}

    .table-wrap {{
      overflow-x: auto;
      max-height: 520px;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      background: var(--white);
      font-size: 13px;
    }}

    thead tr {{
      background: var(--ink);
      color: var(--white);
    }}

    th {{
      padding: 13px 16px;
      text-align: left;
      font-weight: 500;
      font-size: 11px;
      letter-spacing: .08em;
      text-transform: uppercase;
      white-space: nowrap;
      position: sticky;
      top: 0;
      background: var(--ink);
      z-index: 1;
    }}

    td {{
      padding: 11px 16px;
      border-bottom: 1px solid var(--border);
      font-family: 'DM Mono', monospace;
      font-size: 12.5px;
      color: var(--ink);
      white-space: nowrap;
    }}

    td:first-child {{
      font-family: 'Sora', sans-serif;
      font-weight: 500;
    }}

    tr:hover td {{
      background: var(--surface-2);
    }}

    .governance {{
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 26px 30px;
      box-shadow: var(--shadow);
      display: flex;
      gap: 18px;
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
      color: var(--ink-light);
      font-size: 13px;
    }}

    @media (max-width: 860px) {{
      .metric-grid,
      .grid-two {{
        grid-template-columns: 1fr;
      }}

      .dashboard-header {{
        padding: 36px 28px 30px;
      }}

      .dashboard-body {{
        padding: 32px 20px 60px;
      }}
    }}
  </style>
</head>

<body>

<header class="dashboard-header">
  <div class="eyebrow">Interactive HTML Dashboard · p07_saas_strategic_forecasting</div>
  <h1>SaaS Strategic Forecasting Dashboard</h1>
  <p class="header-sub">
    Retention forecasting, cohort analysis, operational risk, and scenario planning
  </p>
</header>

<main class="dashboard-body">

<section>
  <div class="section-label"><h2>Forecast Summary</h2></div>

  <div class="metric-grid">

    <div class="metric-card">
      <div class="metric-label">Projected Retention</div>
      <div class="metric-value">{fmt(latest_retention["forecast_retention_rate"] * 100, 1)}%</div>
      <div class="metric-note">Final horizon estimate</div>
    </div>

    <div class="metric-card">
      <div class="metric-label">Projected Churn</div>
      <div class="metric-value">{fmt(latest_churn["forecast_churn_rate"] * 100, 1)}%</div>
      <div class="metric-note">Final horizon estimate</div>
    </div>

    <div class="metric-card">
      <div class="metric-label">Projected MRR</div>
      <div class="metric-value">{fmt(latest_mrr["forecast_total_mrr"], 0)}</div>
      <div class="metric-note">Revenue trajectory</div>
    </div>

    <div class="metric-card">
      <div class="metric-label">Revenue at Risk</div>
      <div class="metric-value">{fmt(latest_risk["forecast_revenue_at_risk"], 0)}</div>
      <div class="metric-note">Forecast exposure</div>
    </div>

  </div>

  <div class="callout">
    Forecasts are directional planning estimates with widening uncertainty bands.
    They support executive planning rather than automated operational decisions.
  </div>
</section>

<section>
  <div class="section-label"><h2>Forecast Trajectories</h2></div>

  <div class="grid-two">

    <div class="panel">
      <div class="panel-title">Retention forecast</div>
      <div id="retentionChart" class="chart"></div>
    </div>

    <div class="panel">
      <div class="panel-title">MRR forecast</div>
      <div id="mrrChart" class="chart"></div>
    </div>

  </div>
</section>

<section>
  <div class="section-label"><h2>Revenue Risk & Scenarios</h2></div>

  <div class="grid-two">

    <div class="panel">
      <div class="panel-title">Revenue at risk forecast</div>
      <div id="riskChart" class="chart"></div>
    </div>

    <div class="panel">
      <div class="panel-title">Scenario MRR impact</div>
      <div id="scenarioChart" class="chart"></div>
    </div>

  </div>
</section>

<section>
  <div class="section-label"><h2>Risk Concentration</h2></div>

  <div class="panel">
    <div class="panel-title">Revenue-risk concentration by segment</div>
    <div id="riskConcentrationChart" class="chart"></div>
  </div>
</section>

<section>
  <div class="section-label"><h2>Segment Tables</h2></div>

  <div class="grid-two">

    <div class="panel">
      <div class="panel-title">Executive segment risk</div>
      <div class="table-wrap">
        <table id="segmentTable"></table>
      </div>
    </div>

    <div class="panel">
      <div class="panel-title">Revenue-risk concentration</div>
      <div class="table-wrap">
        <table id="riskConcentrationTable"></table>
      </div>
    </div>

  </div>
</section>

<section>
  <div class="section-label"><h2>Governance</h2></div>

  <div class="governance">
    <div class="governance-icon">⚠</div>

    <div>
      <h3>Decision-support only</h3>

      <p>
        Forecasts and scenario outputs are assumption-dependent planning estimates.
        Observational operational relationships do not establish causal certainty.
        Human review is required before strategic or customer-facing action.
      </p>
    </div>
  </div>
</section>

</main>

<script>

const retentionForecast = {records_for_js(retention_forecast)};
const mrrForecast = {records_for_js(mrr_forecast)};
const riskForecast = {records_for_js(risk_forecast)};
const scenarioImpact = {records_for_js(scenario_impact)};
const executiveSegments = {records_for_js(executive_segments, 15)};
const riskConcentration = {records_for_js(risk_concentration, 15)};

const brand = "{BRAND_MAIN}";
const ink = "{BRAND_SECONDARY}";
const grid = "#dde3ee";

const plotLayoutBase = {{
  paper_bgcolor: "white",
  plot_bgcolor: "white",
  font: {{
    family: "Sora, sans-serif",
    color: ink,
    size: 12
  }},
  margin: {{
    l: 70,
    r: 30,
    t: 20,
    b: 60
  }},
  xaxis: {{
    gridcolor: grid
  }},
  yaxis: {{
    gridcolor: grid
  }}
}};

const plotConfig = {{
  responsive: true,
  displayModeBar: false
}};

function renderTable(elementId, rows, maxRows = null) {{
  const table = document.getElementById(elementId);

  const data = maxRows ? rows.slice(0, maxRows) : rows;

  if (!data.length) {{
    table.innerHTML = "<tbody><tr><td>No data available</td></tr></tbody>";
    return;
  }}

  const columns = Object.keys(data[0]);

  const thead =
    "<thead><tr>" +
    columns.map(c => `<th>${{c}}</th>`).join("") +
    "</tr></thead>";

  const tbody =
    "<tbody>" +
    data.map(row =>
      "<tr>" +
      columns.map(c => `<td>${{row[c] ?? ""}}</td>`).join("") +
      "</tr>"
    ).join("") +
    "</tbody>";

  table.innerHTML = thead + tbody;
}}

function renderRetentionChart() {{
  Plotly.newPlot(
    "retentionChart",
    [{{
      x: retentionForecast.map(d => d.forecast_month),
      y: retentionForecast.map(d => d.forecast_retention_rate * 100),
      type: "scatter",
      mode: "lines+markers",
      line: {{ color: brand }}
    }}],
    {{
      ...plotLayoutBase,
      yaxis: {{
        title: "Retention %",
        gridcolor: grid
      }}
    }},
    plotConfig
  );
}}

function renderMRRChart() {{
  Plotly.newPlot(
    "mrrChart",
    [{{
      x: mrrForecast.map(d => d.forecast_month),
      y: mrrForecast.map(d => d.forecast_total_mrr),
      type: "scatter",
      mode: "lines+markers",
      line: {{ color: brand }}
    }}],
    {{
      ...plotLayoutBase,
      yaxis: {{
        title: "Projected MRR",
        gridcolor: grid
      }}
    }},
    plotConfig
  );
}}

function renderRiskChart() {{
  Plotly.newPlot(
    "riskChart",
    [{{
      x: riskForecast.map(d => d.forecast_month),
      y: riskForecast.map(d => d.forecast_revenue_at_risk),
      type: "scatter",
      mode: "lines+markers",
      line: {{ color: "#e07070" }}
    }}],
    {{
      ...plotLayoutBase,
      yaxis: {{
        title: "Revenue at Risk",
        gridcolor: grid
      }}
    }},
    plotConfig
  );
}}

function renderScenarioChart() {{
  const sorted = [...scenarioImpact].sort(
    (a, b) => b.projected_mrr_difference - a.projected_mrr_difference
  );

  Plotly.newPlot(
    "scenarioChart",
    [{{
      x: sorted.map(d => d.projected_mrr_difference),
      y: sorted.map(d => d.scenario),
      type: "bar",
      orientation: "h",
      marker: {{ color: brand }}
    }}],
    {{
      ...plotLayoutBase,
      margin: {{ l: 180, r: 30, t: 20, b: 60 }},
      xaxis: {{
        title: "Projected MRR Difference"
      }}
    }},
    plotConfig
  );
}}

function renderRiskConcentrationChart() {{
  const sorted = [...riskConcentration]
    .sort((a, b) => b.risk_concentration_ratio - a.risk_concentration_ratio)
    .slice(0, 10);

  Plotly.newPlot(
    "riskConcentrationChart",
    [{{
      x: sorted.map(
        d => `${{d.health_band}} / ${{d.mrr_band}}`
      ),
      y: sorted.map(d => d.risk_concentration_ratio),
      type: "bar",
      marker: {{ color: brand }}
    }}],
    {{
      ...plotLayoutBase,
      xaxis: {{
        tickangle: -30
      }},
      yaxis: {{
        title: "Risk Concentration Ratio"
      }}
    }},
    plotConfig
  );
}}

renderRetentionChart();
renderMRRChart();
renderRiskChart();
renderScenarioChart();
renderRiskConcentrationChart();

renderTable("segmentTable", executiveSegments, 15);
renderTable("riskConcentrationTable", riskConcentration, 15);

</script>

</body>
</html>
"""

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(html, encoding="utf-8")

    print(f"Saved HTML dashboard → {REPORT_PATH}")


if __name__ == "__main__":
    main()