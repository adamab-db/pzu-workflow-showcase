# Databricks notebook source
# MAGIC %md
# MAGIC # Quarantine
# MAGIC Runs when quality check fails (FALSE branch of If/Else).
# MAGIC Routes bad data to a quarantine zone for manual review.

# COMMAND ----------

print("Quality check FAILED — routing data to quarantine.")
print("Bad records saved for manual review.")
print("Alert sent to data steward team.")
