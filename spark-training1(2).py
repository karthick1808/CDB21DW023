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

rdd2 = sc.textFile("/FileStore/tables/sample.txt")

# COMMAND ----------

rdd2.collect()

# COMMAND ----------

x = "1 2 3 4 5"

# COMMAND ----------

b= x.split(" ")

# COMMAND ----------

print(b)

# COMMAND ----------

rdd3 = rdd2.map(lambda x: x.split(" "))

# COMMAND ----------

rdd3.collect()

# COMMAND ----------

rdd2.count()

# COMMAND ----------

rdd3.count()

# COMMAND ----------

task = sc.textFile("/FileStore/tables/task1.txt")

# COMMAND ----------

task.collect()

# COMMAND ----------

#word letter count in array of object
def count(x):
  l = x.split(" ")
  l2 = []
  for s in l:
      l2.append(len(s))
  return l2  

# COMMAND ----------

rdd4 = task.map(count)

# COMMAND ----------

rdd4.collect()

# COMMAND ----------


