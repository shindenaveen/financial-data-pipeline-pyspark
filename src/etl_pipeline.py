from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Initialize Spark Session
spark = SparkSession.builder.appName("FinancialDataETL").getOrCreate()

# Read data
df = spark.read.csv("fintech_sample.csv", header=True, inferSchema=True)

# Data Cleaning: Remove nulls
cleaned_df = df.dropna()

# Feature Engineering: Debt to Income Ratio
cleaned_df = cleaned_df.withColumn(
    "debt_to_income",
    col("current_debt") / col("income")
)

# Risk Scoring (simple rule: high debt_to_income = high risk)
risk_df = cleaned_df.withColumn(
    "risk_score",
    when(col("debt_to_income") > 0.25, "HIGH")
    .when(col("debt_to_income") > 0.10, "MEDIUM")
    .otherwise("LOW")
)

# Save cleaned data & risk scores to output
cleaned_df.toPandas().to_csv("cleaned_data.csv", index=False)
risk_df.select("id", "risk_score").toPandas().to_csv("risk_scores.csv", index=False)

spark.stop()
