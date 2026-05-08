python -m src.pipeline.main \
  --data projects/p02_fintech_customer_segmentation/data/raw/fintech_customer_sample.csv \
  --task descriptive_stats \
  --project p02_fintech_customer_segmentation \
  --run-name stage02a_fintech_descriptive_baseline \
  --cleaning-rules projects/p02_fintech_customer_segmentation/configs/project_config.yaml