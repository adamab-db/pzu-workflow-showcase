# Databricks notebook source
# MAGIC %md
# MAGIC # Child Job Task
# MAGIC This notebook runs as part of a **separate child workflow**,
# MAGIC triggered by a Run Job task in the parent workflow.
# MAGIC Demonstrates cross-workflow dependencies.

# COMMAND ----------

print("Child workflow executing...")
print("This could be: downstream reporting, data export, ML model refresh, etc.")
print("Child workflow complete.")
