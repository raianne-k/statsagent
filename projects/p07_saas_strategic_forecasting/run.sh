#!/bin/bash

set -e

echo "=========================================="
echo "P07 SaaS Strategic Forecasting Pipeline"
echo "=========================================="

echo ""
echo "[1/10] Generating longitudinal SaaS dataset..."
python projects/p07_saas_strategic_forecasting/scripts/data_generation/generate_dataset.py

echo ""
echo "[2/10] Running cleaning + validation pipeline..."
python -m src.pipeline.main \
  --data projects/p07_saas_strategic_forecasting/data/raw/saas_account_monthly_forecasting.csv \
  --task descriptive_stats \
  --project p07_saas_strategic_forecasting \
  --run-name stage07_strategic_forecasting_baseline \
  --cleaning-rules projects/p07_saas_strategic_forecasting/configs/project_config.yaml

echo ""
echo "[3/10] Running cohort retention analysis..."
python projects/p07_saas_strategic_forecasting/scripts/analysis/cohort_analysis.py

echo ""
echo "[4/10] Running operational trend analysis..."
python projects/p07_saas_strategic_forecasting/scripts/analysis/trend_analysis.py

echo ""
echo "[5/10] Running relationship analysis..."
python projects/p07_saas_strategic_forecasting/scripts/analysis/relationships.py

echo ""
echo "[6/10] Running segmentation analysis..."
python projects/p07_saas_strategic_forecasting/scripts/analysis/segmentation_analysis.py

echo ""
echo "[7/10] Running forecasting analysis..."
python projects/p07_saas_strategic_forecasting/scripts/analysis/forecasting_analysis.py

echo ""
echo "[8/10] Running scenario modeling..."
python projects/p07_saas_strategic_forecasting/scripts/analysis/scenario_modeling.py

echo ""
echo "[9/10] Generating plots..."
python projects/p07_saas_strategic_forecasting/scripts/analysis/create_plots.py

echo ""
echo "[10/10] Building executive outputs..."
python projects/p07_saas_strategic_forecasting/scripts/reporting/executive_report.py

python projects/p07_saas_strategic_forecasting/scripts/reporting/dashboard_html.py

echo ""
echo "=========================================="
echo "P07 Pipeline Complete"
echo "=========================================="