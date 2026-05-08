from pathlib import Path
import json

import pandas as pd


BASE_DIR = Path("projects/p05_saas_churn_prediction")
OUTPUT_DIR = BASE_DIR / "outputs"
REPORT_PATH = OUTPUT_DIR / "reports" / "churn_dashboard.html"

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


def fmt(value, digits: int = 4) -> str:
    try:
        return f"{float(value):.{digits}f}"
    except (ValueError, TypeError):
        return str(value)


def main():
    metrics = read_csv(OUTPUT_DIR / "prediction" / "model_metrics.csv")
    thresholds = read_csv(OUTPUT_DIR / "prediction" / "threshold_comparison.csv")
    features = read_csv(OUTPUT_DIR / "prediction" / "feature_importance.csv")
    scored = read_csv(OUTPUT_DIR / "prediction" / "scored_test_accounts.csv")

    health_segments = read_csv(
        OUTPUT_DIR / "segmentation" / "health_band_comparison.csv"
    )
    contract_segments = read_csv(
        OUTPUT_DIR / "segmentation" / "contract_type_comparison.csv"
    )
    correlations = read_csv(
        OUTPUT_DIR / "relationships" / "continuous_variable_correlations.csv"
    )

    model = metrics.iloc[0]

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>SaaS Churn Prediction — Dashboard</title>

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

    .control-card {{
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      box-shadow: var(--shadow);
      display: grid;
      grid-template-columns: 1fr 260px;
      gap: 28px;
      align-items: center;
    }}

    .slider-label {{
      font-size: 11px;
      font-weight: 600;
      letter-spacing: .1em;
      text-transform: uppercase;
      color: var(--ink-light);
      margin-bottom: 10px;
    }}

    input[type="range"] {{
      width: 100%;
      accent-color: var(--brand);
    }}

    .threshold-value {{
      font-family: 'DM Mono', monospace;
      font-size: 28px;
      color: var(--ink);
      margin-top: 8px;
    }}

    .flagged-box {{
      background: var(--surface-2);
      border-left: 4px solid var(--brand);
      border-radius: var(--radius);
      padding: 18px 20px;
    }}

    .flagged-box .label {{
      font-size: 11px;
      font-weight: 600;
      letter-spacing: .1em;
      text-transform: uppercase;
      color: var(--ink-light);
      margin-bottom: 6px;
    }}

    .flagged-box .value {{
      font-family: 'DM Mono', monospace;
      font-size: 28px;
      color: var(--ink);
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
      .grid-two,
      .control-card {{
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
    <div class="eyebrow">Interactive HTML Dashboard · p05_saas_churn_prediction</div>
    <h1>SaaS Churn Prediction Dashboard</h1>
    <p class="header-sub">Decision-support signals for customer retention operations</p>
  </header>

  <main class="dashboard-body">

    <section>
      <div class="section-label"><h2>Model Performance</h2></div>

      <div class="metric-grid">
        <div class="metric-card">
          <div class="metric-label">Accuracy</div>
          <div class="metric-value">{fmt(model["accuracy"])}</div>
        </div>

        <div class="metric-card">
          <div class="metric-label">Precision</div>
          <div class="metric-value">{fmt(model["precision"])}</div>
        </div>

        <div class="metric-card">
          <div class="metric-label">Recall</div>
          <div class="metric-value">{fmt(model["recall"])}</div>
        </div>

        <div class="metric-card">
          <div class="metric-label">ROC AUC</div>
          <div class="metric-value">{fmt(model["roc_auc"])}</div>
        </div>
      </div>

      <div class="callout">
        Accuracy alone is not enough for churn workflows. Thresholds change how many customers get flagged,
        how many churners are caught, and how much review workload customer-success teams absorb.
      </div>
    </section>

    <section>
      <div class="section-label"><h2>Threshold Control</h2></div>

      <div class="control-card">
        <div>
          <div class="slider-label">Churn probability threshold</div>
          <input id="thresholdSlider" type="range" min="0.10" max="0.90" step="0.05" value="0.50" />
          <div class="threshold-value" id="thresholdValue">0.50</div>
        </div>

        <div class="flagged-box">
          <div class="label">Accounts flagged for review</div>
          <div class="value" id="flaggedCount">—</div>
        </div>
      </div>
    </section>

    <section>
      <div class="section-label"><h2>Threshold Tradeoffs</h2></div>

      <div class="panel">
        <div class="panel-title">Precision, recall, and accounts flagged by threshold</div>
        <div id="thresholdChart" class="chart"></div>
      </div>

      <div class="callout">
        Lower thresholds catch more churners but create heavier review volume.
        Higher thresholds reduce workload but miss more potential churners.
      </div>
    </section>

    <section>
      <div class="section-label"><h2>Top Churn Signals</h2></div>

      <div class="panel">
        <div class="panel-title">Feature importance — absolute model coefficients</div>
        <div id="featureChart" class="chart"></div>
      </div>

      <div class="callout">
        Feature importance reflects model coefficients. It does not prove causal drivers of churn.
      </div>
    </section>

    <section>
      <div class="section-label"><h2>Segmentation Context</h2></div>

      <div class="grid-two">
        <div class="panel">
          <div class="panel-title">Churn rate by health band</div>
          <div id="healthChart" class="small-chart"></div>
        </div>

        <div class="panel">
          <div class="panel-title">Churn rate by contract type</div>
          <div id="contractChart" class="small-chart"></div>
        </div>
      </div>
    </section>

    <section>
      <div class="section-label"><h2>Continuous Relationships With Churn</h2></div>

      <div class="panel">
        <div class="panel-title">Absolute correlation with churn</div>
        <div id="correlationChart" class="chart"></div>
      </div>
    </section>

    <section>
      <div class="section-label"><h2>Threshold Comparison Table</h2></div>

      <div class="panel">
        <div class="table-wrap">
          <table id="thresholdTable"></table>
        </div>
      </div>
    </section>

    <section>
      <div class="section-label"><h2>Top Scored Accounts</h2></div>

      <div class="panel">
        <div class="table-wrap">
          <table id="scoredTable"></table>
        </div>
      </div>
    </section>

    <section>
      <div class="section-label"><h2>Governance</h2></div>

      <div class="governance">
        <div class="governance-icon">⚠</div>
        <div>
          <h3>Human review required</h3>
          <p>
            Predictions are decision-support signals only. They must not trigger automated customer-success
            or retention actions without human review. Model coefficients and relationships do not establish causality.
          </p>
        </div>
      </div>
    </section>

  </main>

<script>
  const thresholds = {records_for_js(thresholds)};
  const features = {records_for_js(features, 15)};
  const scored = {records_for_js(scored, 300)};
  const healthSegments = {records_for_js(health_segments)};
  const contractSegments = {records_for_js(contract_segments)};
  const correlations = {records_for_js(correlations, 15)};

  const brand = "{BRAND_MAIN}";
  const ink = "{BRAND_SECONDARY}";
  const inkLight = "#6b7280";
  const grid = "#dde3ee";
  const surface = "#f7f8fa";
  const danger = "#e07070";

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
      t: 25,
      b: 60
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

  function renderThresholdChart() {{
    const x = thresholds.map(d => d.threshold);

    const precision = {{
      x: x,
      y: thresholds.map(d => d.precision),
      mode: "lines+markers",
      name: "Precision",
      line: {{ color: brand, width: 3 }},
      marker: {{ size: 7 }}
    }};

    const recall = {{
      x: x,
      y: thresholds.map(d => d.recall),
      mode: "lines+markers",
      name: "Recall",
      line: {{ color: danger, width: 3 }},
      marker: {{ size: 7 }}
    }};

    const flagged = {{
      x: x,
      y: thresholds.map(d => d.accounts_flagged_percent),
      type: "bar",
      name: "Accounts flagged %",
      marker: {{ color: "rgba(129,160,206,0.28)" }},
      yaxis: "y2"
    }};

    const layout = {{
      ...plotLayoutBase,
      barmode: "overlay",
      xaxis: {{
        ...plotLayoutBase.xaxis,
        title: "Probability threshold"
      }},
      yaxis: {{
        ...plotLayoutBase.yaxis,
        title: "Precision / Recall",
        range: [0, 1]
      }},
      yaxis2: {{
        title: "Accounts flagged %",
        overlaying: "y",
        side: "right",
        range: [0, 100],
        gridcolor: "rgba(0,0,0,0)",
        tickfont: {{ color: inkLight }}
      }}
    }};

    Plotly.newPlot("thresholdChart", [flagged, precision, recall], layout, plotConfig);
  }}

  function renderFeatureChart() {{
    const sorted = [...features].sort(
      (a, b) => Number(a.absolute_coefficient) - Number(b.absolute_coefficient)
    );

    const trace = {{
      x: sorted.map(d => Number(d.absolute_coefficient)),
      y: sorted.map(d => d.feature),
      type: "bar",
      orientation: "h",
      marker: {{ color: brand }},
      text: sorted.map(d => d.direction),
      hovertemplate: "<b>%{{y}}</b><br>Abs coefficient: %{{x:.4f}}<br>%{{text}}<extra></extra>"
    }};

    const layout = {{
      ...plotLayoutBase,
      margin: {{ l: 230, r: 30, t: 25, b: 45 }},
      xaxis: {{
        ...plotLayoutBase.xaxis,
        title: "Absolute coefficient"
      }},
      yaxis: {{
        ...plotLayoutBase.yaxis,
        automargin: true
      }}
    }};

    Plotly.newPlot("featureChart", [trace], layout, plotConfig);
  }}

  function renderHealthChart() {{
    const rows = healthSegments.filter(d => d.health_band !== null && d.health_band !== "NaN");

    const trace = {{
      x: rows.map(d => d.health_band),
      y: rows.map(d => Number(d.churn_rate_percent)),
      type: "bar",
      marker: {{ color: brand }},
      hovertemplate: "<b>%{{x}}</b><br>Churn rate: %{{y:.2f}}%<extra></extra>"
    }};

    const layout = {{
      ...plotLayoutBase,
      margin: {{ l: 60, r: 20, t: 20, b: 70 }},
      xaxis: {{
        ...plotLayoutBase.xaxis,
        title: ""
      }},
      yaxis: {{
        ...plotLayoutBase.yaxis,
        title: "Churn rate %"
      }}
    }};

    Plotly.newPlot("healthChart", [trace], layout, plotConfig);
  }}

  function renderContractChart() {{
    const trace = {{
      x: contractSegments.map(d => d.contract_type),
      y: contractSegments.map(d => Number(d.churn_rate_percent)),
      type: "bar",
      marker: {{ color: brand }},
      hovertemplate: "<b>%{{x}}</b><br>Churn rate: %{{y:.2f}}%<extra></extra>"
    }};

    const layout = {{
      ...plotLayoutBase,
      margin: {{ l: 60, r: 20, t: 20, b: 70 }},
      xaxis: {{
        ...plotLayoutBase.xaxis,
        title: ""
      }},
      yaxis: {{
        ...plotLayoutBase.yaxis,
        title: "Churn rate %"
      }}
    }};

    Plotly.newPlot("contractChart", [trace], layout, plotConfig);
  }}

  function renderCorrelationChart() {{
    const sorted = [...correlations].sort(
      (a, b) => Number(a.absolute_correlation) - Number(b.absolute_correlation)
    );

    const trace = {{
      x: sorted.map(d => Number(d.absolute_correlation)),
      y: sorted.map(d => d.variable),
      type: "bar",
      orientation: "h",
      marker: {{ color: brand }},
      text: sorted.map(d => Number(d.correlation_with_churn)),
      hovertemplate: "<b>%{{y}}</b><br>Abs correlation: %{{x:.4f}}<br>Signed correlation: %{{text:.4f}}<extra></extra>"
    }};

    const layout = {{
      ...plotLayoutBase,
      margin: {{ l: 230, r: 30, t: 25, b: 45 }},
      xaxis: {{
        ...plotLayoutBase.xaxis,
        title: "Absolute correlation"
      }},
      yaxis: {{
        ...plotLayoutBase.yaxis,
        automargin: true
      }}
    }};

    Plotly.newPlot("correlationChart", [trace], layout, plotConfig);
  }}

  function updateThreshold() {{
    const slider = document.getElementById("thresholdSlider");
    const threshold = Number(slider.value);

    document.getElementById("thresholdValue").innerText = threshold.toFixed(2);

    const flagged = scored.filter(
      row => Number(row.predicted_churn_probability) >= threshold
    );

    const pct = scored.length
      ? ((flagged.length / scored.length) * 100).toFixed(2)
      : "0.00";

    document.getElementById("flaggedCount").innerHTML =
      `${{flagged.length}} <span style="font-size:16px;color:#6b7280;">(${{pct}}%)</span>`;

    renderTable("scoredTable", flagged, 100);
  }}

  renderThresholdChart();
  renderFeatureChart();
  renderHealthChart();
  renderContractChart();
  renderCorrelationChart();

  renderTable("thresholdTable", thresholds);

  document.getElementById("thresholdSlider").addEventListener("input", updateThreshold);
  updateThreshold();
</script>

</body>
</html>
"""

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(html, encoding="utf-8")

    print(f"Saved HTML dashboard → {REPORT_PATH}")


if __name__ == "__main__":
    main()