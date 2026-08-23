from spark_env import configure_spark_env

configure_spark_env()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Repartition and Coalesce Example").master("local[*]").getOrCreate()

data = [(1, "Aamri", "backend", 85000, "IN"),
        (2, "Raj", "data", 72000, "IN"),
        (3, "Meera", "backend", 91000, "US"),
        (4, "Sam", "ml", 68000, "US")]
columns = ["id", "name", "domain", "salary", "country"]

df = spark.createDataFrame(data, columns)

print("Initial partitions:", df.rdd.getNumPartitions())

df_repartitioned = df.repartition(4)
print("After repartition(4):", df_repartitioned.rdd.getNumPartitions())

df_coalesced = df_repartitioned.coalesce(2)
print("After coalesce(2):", df_coalesced.rdd.getNumPartitions())

df_coalesced.show()

spark.stop()
