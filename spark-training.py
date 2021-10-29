# Databricks notebook source
import pyspark

# COMMAND ----------

from pyspark import SparkContext, SparkConf

# COMMAND ----------

conf = SparkConf().setAppName("Read File")

# COMMAND ----------

sc = SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

text = sc.textFile("/FileStore/tables/demotext.txt")

# COMMAND ----------

print(type(text))

# COMMAND ----------

print(text)

# COMMAND ----------

text.collect()

# COMMAND ----------

text.take(2)

# COMMAND ----------

text.first()

# COMMAND ----------

text.count()

# COMMAND ----------


