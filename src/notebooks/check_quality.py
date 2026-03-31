# Databricks notebook source
# MAGIC %md
# MAGIC # Check Data Quality
# MAGIC Reads task values from all ingestion tasks and computes a quality score.
# MAGIC Demonstrates **reading task values** set by upstream tasks.

# COMMAND ----------

# Read row counts from each parallel ingest task
rows_a = dbutils.jobs.taskValues.get(taskKey="ingest_a", key="row_count", debugValue=5000)
rows_b = dbutils.jobs.taskValues.get(taskKey="ingest_b", key="row_count", debugValue=3000)
rows_c = dbutils.jobs.taskValues.get(taskKey="ingest_c", key="row_count", debugValue=4000)

total_rows = rows_a + rows_b + rows_c

print(f"Source A: {rows_a:,} rows")
print(f"Source B: {rows_b:,} rows")
print(f"Source C: {rows_c:,} rows")
print(f"Total:    {total_rows:,} rows")

# COMMAND ----------

# Simple quality check: all sources must have > 0 rows
quality_passed = rows_a > 0 and rows_b > 0 and rows_c > 0
quality_score = round(min(rows_a, rows_b, rows_c) / max(rows_a, rows_b, rows_c) * 100, 1)

print(f"Quality score: {quality_score}%")
print(f"Quality passed: {quality_passed}")

# COMMAND ----------

# Set the result for the downstream If/Else task to evaluate
dbutils.jobs.taskValues.set(key="quality_passed", value=quality_passed)
dbutils.jobs.taskValues.set(key="total_rows", value=total_rows)
