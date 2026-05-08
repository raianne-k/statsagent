python -m src.pipeline.main \
  --data projects/p04_fintech_inference/data/raw/fintech_repayment_inference_sample.csv \
  --task descriptive_stats \
  --project p04_fintech_inference \
  --run-name stage04a_fintech_inference_baseline \
  --cleaning-rules projects/p04_fintech_inference/configs/project_config.yaml

python projects/p04_fintech_inference/create_plots.py \
  --data projects/p04_fintech_inference/data/cleaned/fintech_repayment_inference_cleaned.csv

python projects/p04_fintech_inference/inference_analysis.py