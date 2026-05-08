from pathlib import Path
import json

import pandas as pd


BASE_DIR = Path("projects/p06_product_experimentation")
OUTPUT_DIR = BASE_DIR / "outputs"

REPORT_PATH = OUTPUT_DIR / "dashboard" / "experiment_dashboard.html"

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
    integrity = read_csv(OUTPUT_DIR / "experimentation" / "experiment_integrity_review.csv")
    binary_results = read_csv(OUTPUT_DIR / "experimentation" / "binary_metric_experiment_results.csv")
    continuous_results = read_csv(OUTPUT_DIR / "experimentation" / "continuous_metric_experiment_results.csv")
    balance = read_csv(OUTPUT_DIR / "experimentation" / "randomization_balance_check.csv")
    relationships = read_csv(OUTPUT_DIR / "relationships" / "overall_metric_outcome_correlations.csv")
    segment_summary = read_csv(OUTPUT_DIR / "segmentation" / "segment_profile_summary.csv")

    activation_row = binary_results[binary_results["metric"] == "activation_flag"].iloc[0]
    retention_row = binary_results[binary_results["metric"] == "retained_30d"].iloc[0]
    churn_row = binary_results[binary_results["metric"] == "churn_30d"].iloc[0]

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>Product Experimentation — Dashboard</title>

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
      max-width: 1180px;
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
      height: 380px;
      padding: 10px 14px 4px;
    }}

    .small-chart {{
      height: 320px;
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
  <div class="eyebrow">Interactive HTML Dashboard · p06_product_experimentation</div>
  <h1>Product Experimentation Dashboard</h1>
  <p class="header-sub">Treatment effects, uncertainty, guardrails, and rollout context</p>
</header>

<main class="dashboard-body">

  <section>
    <div class="section-label"><h2>Primary Outcomes</h2></div>

    <div class="metric-grid">
      <div class="metric-card">
        <div class="metric-label">Activation Lift</div>
        <div class="metric-value">{fmt(activation_row["absolute_lift_percentage_points"])}</div>
        <div class="metric-note">Percentage points</div>
      </div>

      <div class="metric-card">
        <div class="metric-label">Activation P-value</div>
        <div class="metric-value">{fmt(activation_row["p_value"], 4)}</div>
        <div class="metric-note">Two-sided test</div>
      </div>

      <div class="metric-card">
        <div class="metric-label">30d Retention Lift</div>
        <div class="metric-value">{fmt(retention_row["absolute_lift_percentage_points"])}</div>
        <div class="metric-note">Percentage points</div>
      </div>

      <div class="metric-card">
        <div class="metric-label">30d Churn Lift</div>
        <div class="metric-value">{fmt(churn_row["absolute_lift_percentage_points"])}</div>
        <div class="metric-note">Negative is better</div>
      </div>
    </div>

    <div class="callout">
      This dashboard evaluates experiment evidence for product decision-making.
      Statistical significance is only one input; rollout decisions also require business significance and guardrail review.
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Binary Outcome Lift</h2></div>

    <div class="panel">
      <div class="panel-title">Treatment vs control — conversion and retention outcomes</div>
      <div id="binaryLiftChart" class="chart"></div>
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Continuous Outcome Differences</h2></div>

    <div class="panel">
      <div class="panel-title">Treatment minus control — continuous metrics</div>
      <div id="continuousDifferenceChart" class="chart"></div>
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Experiment Integrity</h2></div>

    <div class="grid-two">
      <div class="panel">
        <div class="panel-title">Integrity review</div>
        <div class="table-wrap"><table id="integrityTable"></table></div>
      </div>

      <div class="panel">
        <div class="panel-title">Largest balance differences</div>
        <div class="table-wrap"><table id="balanceTable"></table></div>
      </div>
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Relationship Context</h2></div>

    <div class="panel">
      <div class="panel-title">Strongest metric-outcome correlations</div>
      <div id="relationshipChart" class="chart"></div>
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Segment Context</h2></div>

    <div class="panel">
      <div class="panel-title">Segment profile summary</div>
      <div class="table-wrap"><table id="segmentTable"></table></div>
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Detailed Experiment Results</h2></div>

    <div class="grid-two">
      <div class="panel">
        <div class="panel-title">Binary metrics</div>
        <div class="table-wrap"><table id="binaryTable"></table></div>
      </div>

      <div class="panel">
        <div class="panel-title">Continuous metrics</div>
        <div class="table-wrap"><table id="continuousTable"></table></div>
      </div>
    </div>
  </section>

  <section>
    <div class="section-label"><h2>Governance</h2></div>

    <div class="governance">
      <div class="governance-icon">⚠</div>
      <div>
        <h3>Rollout decision requires review</h3>
        <p>
          Experiment results should not trigger automatic rollout. Product teams should review assignment quality,
          exposure validity, confidence intervals, practical significance, guardrail metrics, and long-term risk.
        </p>
      </div>
    </div>
  </section>

</main>

<script>
  const binaryResults = {records_for_js(binary_results)};
  const continuousResults = {records_for_js(continuous_results)};
  const integrity = {records_for_js(integrity)};
  const balance = {records_for_js(balance.sort_values("absolute_difference_percentage_points", ascending=False), 12)};
  const relationships = {records_for_js(relationships, 15)};
  const segmentSummary = {records_for_js(segment_summary, 25)};

  const brand = "{BRAND_MAIN}";
  const ink = "{BRAND_SECONDARY}";
  const inkLight = "#6b7280";
  const grid = "#dde3ee";
  const danger = "#e07070";
  const success = "#7aa874";

  const plotLayoutBase = {{
    paper_bgcolor: "white",
    plot_bgcolor: "white",
    font: {{
      family: "Sora, sans-serif",
      color: ink,
      size: 12
    }},
    margin: {{
      l: 80,
      r: 30,
      t: 25,
      b: 70
    }},
    xaxis: {{
      gridcolor: grid,
      zerolinecolor: grid,
      tickfont: {{ color: inkLight }}
    }},
    yaxis: {{
      gridcolor: grid,
      zerolinecolor: grid,
      tickfont: {{ color: inkLight }}
    }},
    legend: {{
      orientation: "h",
      y: -0.22,
      x: 0
    }}
  }};

  const plotConfig = {{
    responsive: true,
    displayModeBar: false
  }};

  function formatValue(value) {{
    if (value === null || value === undefined || Number.isNaN(value)) return "";
    if (typeof value === "number") {{
      return Number.isInteger(value) ? value.toString() : value.toFixed(4);
    }}
    return value;
  }}

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
        columns.map(c => `<td>${{formatValue(row[c])}}</td>`).join("") +
        "</tr>"
      ).join("") +
      "</tbody>";

    table.innerHTML = thead + tbody;
  }}

  function renderBinaryLiftChart() {{
    const metrics = binaryResults.map(d => d.metric);

    const control = {{
      x: metrics,
      y: binaryResults.map(d => Number(d.control_rate_percent)),
      type: "bar",
      name: "Control",
      marker: {{ color: "rgba(63,66,71,0.70)" }}
    }};

    const treatment = {{
      x: metrics,
      y: binaryResults.map(d => Number(d.treatment_rate_percent)),
      type: "bar",
      name: "Treatment",
      marker: {{ color: brand }}
    }};

    const layout = {{
      ...plotLayoutBase,
      barmode: "group",
      yaxis: {{
        ...plotLayoutBase.yaxis,
        title: "Rate %"
      }},
      xaxis: {{
        ...plotLayoutBase.xaxis,
        tickangle: -35
      }}
    }};

    Plotly.newPlot("binaryLiftChart", [control, treatment], layout, plotConfig);
  }}

  function renderContinuousDifferenceChart() {{
    const sorted = [...continuousResults].sort(
      (a, b) => Number(a.mean_difference) - Number(b.mean_difference)
    );

    const trace = {{
      x: sorted.map(d => Number(d.mean_difference)),
      y: sorted.map(d => d.metric),
      type: "bar",
      orientation: "h",
      marker: {{
        color: sorted.map(d => Number(d.mean_difference) >= 0 ? brand : danger)
      }},
      hovertemplate: "<b>%{{y}}</b><br>Mean difference: %{{x:.3f}}<extra></extra>"
    }};

    const layout = {{
      ...plotLayoutBase,
      margin: {{ l: 230, r: 30, t: 25, b: 45 }},
      xaxis: {{
        ...plotLayoutBase.xaxis,
        title: "Treatment mean minus control mean"
      }},
      yaxis: {{
        ...plotLayoutBase.yaxis,
        automargin: true
      }}
    }};

    Plotly.newPlot("continuousDifferenceChart", [trace], layout, plotConfig);
  }}

  function renderRelationshipChart() {{
    const sorted = [...relationships].sort(
      (a, b) => Number(a.absolute_correlation) - Number(b.absolute_correlation)
    );

    const labels = sorted.map(d => `${{d.continuous_variable}} → ${{d.outcome_variable}}`);

    const trace = {{
      x: sorted.map(d => Number(d.absolute_correlation)),
      y: labels,
      type: "bar",
      orientation: "h",
      marker: {{ color: brand }},
      hovertemplate: "<b>%{{y}}</b><br>Abs correlation: %{{x:.4f}}<extra></extra>"
    }};

    const layout = {{
      ...plotLayoutBase,
      margin: {{ l: 300, r: 30, t: 25, b: 45 }},
      xaxis: {{
        ...plotLayoutBase.xaxis,
        title: "Absolute correlation"
      }},
      yaxis: {{
        ...plotLayoutBase.yaxis,
        automargin: true
      }}
    }};

    Plotly.newPlot("relationshipChart", [trace], layout, plotConfig);
  }}

  renderBinaryLiftChart();
  renderContinuousDifferenceChart();
  renderRelationshipChart();

  renderTable("integrityTable", integrity);
  renderTable("balanceTable", balance);
  renderTable("segmentTable", segmentSummary, 25);
  renderTable("binaryTable", binaryResults);
  renderTable("continuousTable", continuousResults);
</script>

</body>
</html>
"""

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(html, encoding="utf-8")

    print(f"Saved HTML dashboard → {REPORT_PATH}")


if __name__ == "__main__":
    main()