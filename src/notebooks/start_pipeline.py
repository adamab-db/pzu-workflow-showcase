# Databricks notebook source
# MAGIC %md
# MAGIC # Start Pipeline
# MAGIC Sets run context and validates parameters.

# COMMAND ----------

dbutils.widgets.text("catalog", "")
dbutils.widgets.text("schema", "")
dbutils.widgets.text("run_date", "")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
run_date = dbutils.widgets.get("run_date")

print(f"Pipeline starting")
print(f"  Catalog:  {catalog}")
print(f"  Schema:   {schema}")
print(f"  Run date: {run_date}")

# COMMAND ----------

# Pass the run_date downstream via task values
dbutils.jobs.taskValues.set(key="run_date", value=run_date)
dbutils.jobs.taskValues.set(key="regions", value=["Mazowieckie", "Malopolskie", "Slaskie", "Wielkopolskie"])

print("Task values set: run_date, regions")
