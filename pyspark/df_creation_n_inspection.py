from spark_env import configure_spark_env

configure_spark_env()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataFrameCreation").master("local[*]").getOrCreate()

data = [(1, "Aamri", "backend", 85000, "IN"),
        (2, "Raj", "data", 72000, "IN"),
        (3, "Meera", "backend", 91000, "US"),
        (4, "Sam", "ml", 68000, "US")]

cols = ["id", "name", "domain", "salary", "country"]

df = spark.createDataFrame(data, cols)

df.printSchema()
df.show()

spark.stop()