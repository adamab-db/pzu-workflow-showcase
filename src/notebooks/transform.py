# Databricks notebook source
# MAGIC %md
# MAGIC # Transform
# MAGIC Runs when quality check passes (TRUE branch of If/Else).

# COMMAND ----------

total_rows = dbutils.jobs.taskValues.get(taskKey="check_data_quality", key="total_rows", debugValue=10000)

print(f"Transforming {total_rows:,} rows...")
print("Applying business rules, deduplication, type casting...")
print("Transform complete.")

# COMMAND ----------

dbutils.jobs.taskValues.set(key="transformed_rows", value=total_rows)
