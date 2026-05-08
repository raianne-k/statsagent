python -m src.pipeline.main \
  --data projects/p05_saas_churn_prediction/data/raw/saas_churn_prediction_sample.csv \
  --task descriptive_stats \
  --project p05_saas_churn_prediction \
  --run-name stage05a_saas_churn_prediction_baseline \
  --cleaning-rules projects/p05_saas_churn_prediction/configs/project_config.yaml

python projects/p05_saas_churn_prediction/create_plots.py \
  --data projects/p05_saas_churn_prediction/data/cleaned/saas_churn_prediction_cleaned.csv

python projects/p05_saas_churn_prediction/segmentation_analysis.py

python projects/p05_saas_churn_prediction/relationships.py

python projects/p05_saas_churn_prediction/prediction_analysis.py

python projects/p05_saas_churn_prediction/executive_report.py

python projects/p05_saas_churn_prediction/dashboard_html.py