# Databricks notebook source
# MAGIC %md
# MAGIC # Process Region
# MAGIC Inner task of the **For Each** loop.
# MAGIC Receives a single region and processes it independently.

# COMMAND ----------

dbutils.widgets.text("region", "unknown")

region = dbutils.widgets.get("region")

# COMMAND ----------

import time
import random

delay = random.uniform(0.5, 2)
time.sleep(delay)

records = random.randint(500, 5000)
print(f"Region '{region}': processed {records:,} records in {delay:.1f}s")
