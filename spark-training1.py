# Databricks notebook source
import pyspark

# COMMAND ----------

from pyspark import SparkConf, SparkContext

# COMMAND ----------

conf = SparkConf().setAppName("spark-training1")

# COMMAND ----------

sc = SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

rdd = sc.parallelize([1,2,3,4,5,6,7,8,9,10])

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd.first()

# COMMAND ----------

rdd.collect()

# COMMAND ----------

#map -> Return a new distributed dataset formed by passing each element of the source through a function func.
rdd1 = rdd.map(lambda x: x+500)

# COMMAND ----------

rdd1.collect()

# COMMAND ----------


