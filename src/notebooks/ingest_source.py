# Databricks notebook source
# MAGIC %md
# MAGIC # Ingest Source
# MAGIC Simulates ingesting data from a source system.
# MAGIC Parameterized — the same notebook runs for each source (A, B, C).

# COMMAND ----------

dbutils.widgets.text("source_name", "unknown")

source_name = dbutils.widgets.get("source_name")

# COMMAND ----------

import random
import time

# Simulate variable ingestion time
delay = random.uniform(1, 3)
time.sleep(delay)

# Simulate row count
row_count = random.randint(1000, 50000)

print(f"Source '{source_name}': ingested {row_count:,} rows in {delay:.1f}s")

# COMMAND ----------

# Pass row count to downstream tasks via task values
dbutils.jobs.taskValues.set(key="row_count", value=row_count)
dbutils.jobs.taskValues.set(key="source_name", value=source_name)
