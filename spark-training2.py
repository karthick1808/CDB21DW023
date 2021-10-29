# Databricks notebook source
import pyspark
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("spark-training2")
sc = SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

rdd = sc.textFile("/FileStore/tables/sample.txt")

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd1 = rdd.flatMap(lambda x: x.split(" "))

# COMMAND ----------

rdd1.collect()

# COMMAND ----------

rdd1.count()

# COMMAND ----------

rdd1.take(4)

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd2 = rdd.map(lambda x: x.split(" "))

# COMMAND ----------

rdd2.collect()

# COMMAND ----------

rdd3 = rdd2.flatMap(lambda x: x)

# COMMAND ----------

rdd3.collect()

# COMMAND ----------

rdd3.count()

# COMMAND ----------

rdd4 = sc.textFile("/FileStore/tables/task1.txt")

# COMMAND ----------

rdd5 = rdd4.flatMap(lambda x: x.split(" "))

# COMMAND ----------

rdd5.collect()

# COMMAND ----------


