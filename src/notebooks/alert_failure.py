# Databricks notebook source
# MAGIC %md
# MAGIC # Alert on Failure
# MAGIC Runs only when **at least one upstream task fails** (Run If: AT_LEAST_ONE_FAILED).

# COMMAND ----------

print("PIPELINE FAILURE DETECTED")
print("In production this would:")
print("  - Page the on-call engineer via PagerDuty")
print("  - Post to #data-incidents Slack channel")
print("  - Create a JIRA ticket")
print("  - Log to incident management system")
