# Databricks notebook source
# MAGIC %md
# MAGIC # Notify Success
# MAGIC Runs only when **all upstream tasks succeed** (Run If: ALL_SUCCEEDED).

# COMMAND ----------

print("Pipeline completed successfully!")
print("In production this would send:")
print("  - Slack message to #data-engineering")
print("  - Email to stakeholders")
print("  - Update monitoring dashboard")
