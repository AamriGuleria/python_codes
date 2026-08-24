from pyspark.sql import SparkSession
from spark_env import configure_spark_env
from delta.tables import DeltaTable
from pyspark.sql.functions import avg, col, count, when

configure_spark_env()
spark = SparkSession.builder.appName("Metallian Architecture").getOrCreate()

data = [
    (1, "Alice", "Engineering", 90000),
    (2, "Bob", "Marketing", 75000),
    (3, "Charlie", "Sales", 80000),
    (4, "David", "Engineering", 95000),
    (5, "Eve", "Marketing", 70000),
]

df = spark.createDataFrame(data,["id", "name", "domain", "salary"])

df.write.format("delta").mode("overwrite").saveAsTable("bronze_table")

silver_df = spark.table("bronze_table").filter(col("salary") \
            .isNotNull()) \
            .drop_duplicates(["id"]) \
            .withColumn("domain", when(col("domain")=="","unknown").otherwise(col("domain")))
silver_df.write.format("delta").mode("overwrite").saveAsTable("silver_validated")

gold_df = spark.table("silver_validated").groupBy("domain").agg(avg("salary").alias("avg_salary"), count("*").alias("headcount"))
gold_df.write.format("delta").mode("overwrite").saveAsTable("gold_summary")

spark.sql("SELECT * FROM gold_summary").show()

spark.stop()