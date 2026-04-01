# Databricks notebook source
# MAGIC %md
# MAGIC # Child Job Task
# MAGIC This notebook runs as part of a **separate child workflow**,
# MAGIC triggered by a Run Job task in the parent workflow.
# MAGIC Demonstrates cross-workflow dependencies.

# COMMAND ----------

dbutils.widgets.text("catalog", "")
dbutils.widgets.text("schema", "")
dbutils.widgets.text("run_date", "")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
run_date = dbutils.widgets.get("run_date")

# COMMAND ----------

print("Child workflow executing...")
print(f"  Catalog:  {catalog}")
print(f"  Schema:   {schema}")
print(f"  Run date: {run_date}")
print("Parameters passed from parent workflow via Run Job task.")
print("Child workflow complete.")
