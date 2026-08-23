from pyspark.sql import SparkSession
from spark_env import configure_spark_env
from pyspark.sql.window import Window
from pyspark.sql.functions import col, rank, sum, lag


spark = SparkSession.builder.appName("Window Functions Example").getOrCreate()
configure_spark_env()

data = [(1, "Aamri", "backend", 85000, "IN"),
        (2, "Raj", "data", 72000, "IN"),
        (3, "Meera", "backend", 91000, "US"),
        (4, "Sam", "ml", 68000, "US")]
columns = ["id", "name", "domain", "salary", "country"]

df = spark.createDataFrame(data, columns)

w = Window.partitionBy(col("domain")).orderBy(col("salary").desc())

df_with_rank = df.withColumn(
    "rank_w_domain", rank().over(w)
).withColumn("prev_salary", lag("salary").over(w))
df_with_rank.show()

filtered = df.filter(col("country") == "IN").cache()
filtered.count()
filtered.groupBy("domain").count().show()
filtered.unpersist()
spark.stop()