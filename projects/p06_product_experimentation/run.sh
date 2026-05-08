python -m src.pipeline.main \
  --data projects/p06_product_experimentation/data/raw/saas_experimentation_sample.csv \
  --task descriptive_stats \
  --project p06_product_experimentation \
  --run-name stage06a_product_experimentation_baseline \
  --cleaning-rules projects/p06_product_experimentation/configs/project_config.yaml

python projects/p06_product_experimentation/scripts/analysis/create_plots.py \
  --data projects/p06_product_experimentation/data/cleaned/saas_experimentation_cleaned.csv

python projects/p06_product_experimentation/scripts/analysis/experiment_analysis.py

python projects/p06_product_experimentation/scripts/analysis/segmentation_analysis.py

python projects/p06_product_experimentation/scripts/analysis/relationships.py

python projects/p06_product_experimentation/scripts/reporting/executive_report.py

python projects/p06_product_experimentation/scripts/reporting/dashboard_html.py