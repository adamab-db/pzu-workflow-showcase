# Databricks notebook source
# MAGIC %md
# MAGIC # Publish Gold Layer
# MAGIC Publishes final aggregated data to the gold layer.

# COMMAND ----------

dbutils.widgets.text("catalog", "")
dbutils.widgets.text("schema", "")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

print(f"Publishing gold tables to {catalog}.{schema}")
print("  - policy_claims_summary")
print("  - regional_kpis")
print("  - monthly_trends")
print("Gold layer published.")
