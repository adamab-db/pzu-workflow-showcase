# Databricks notebook source
# MAGIC %md
# MAGIC # Validate Output
# MAGIC Validates the gold layer output.
# MAGIC
# MAGIC **For Repair Run demo:** Set `should_fail` to `true` to make this task fail.
# MAGIC Then use **Repair Run** in the UI to re-run from this task only.

# COMMAND ----------

dbutils.widgets.text("should_fail", "false")

should_fail = dbutils.widgets.get("should_fail").lower() == "true"

# COMMAND ----------

print("Running output validation checks...")
print("  - Row count check: OK")
print("  - Schema check: OK")
print("  - Freshness check: OK")

# COMMAND ----------

if should_fail:
    raise Exception(
        "INTENTIONAL FAILURE for Repair Run demo. "
        "Set should_fail=false and use Repair Run to re-run from this task."
    )

print("All validation checks passed.")
