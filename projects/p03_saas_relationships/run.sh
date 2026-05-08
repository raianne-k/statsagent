python -m src.pipeline.main \
  --data projects/p03_saas_relationships/data/raw/saas_account_sample.csv \
  --task descriptive_stats \
  --project p03_saas_relationships \
  --run-name stage03a_saas_descriptive_baseline \
  --cleaning-rules projects/p03_saas_relationships/configs/project_config.yaml

python projects/p03_saas_relationships/create_plots.py \
  --data projects/p03_saas_relationships/data/cleaned/saas_account_cleaned.csv

python projects/p03_saas_relationships/segmentation_analysis.py

python projects/p03_saas_relationships/relationships.py