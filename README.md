# Financial Data Pipeline Automation with PySpark

ETL pipeline for financial data using PySpark. Cleans data, engineers features, and outputs risk assessments.

## Structure
- data/: Input raw data files
- src/: Main ETL pipeline script (PySpark)
- output/: Cleaned data and scoring outputs
- notebooks/: Analytics and plots

## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Run pipeline: `spark-submit src/etl_pipeline.py`
3. See outputs in `output/`
