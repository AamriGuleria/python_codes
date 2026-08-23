from pyspark.sql.functions import  filter , col , when
from pyspark.sql import SparkSession
from spark_env import configure_spark_env


configure_spark_env()
spark = SparkSession.builder.appName("Transformation Sample").getOrCreate()


data = [(1, "Aamri", "backend", 85000, "IN"),
        (2, "Raj", "data", 72000, "IN"),
        (3, "Meera", "backend", 91000, "US"),
        (4, "Sam", "ml", 68000, "US")]
columns = ["id", "name", "domain", "salary", "country"]

df = spark.createDataFrame(data, columns)
df2 = (df.select(col("id"), col("name"), col("salary")) \
    .filter(col("salary")>7000) \
    .withColumn("salary_band", when(col("salary")>70000, "high").otherwise("low"))
)



df2.show()