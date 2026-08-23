from pyspark.sql import SparkSession
from spark_env import configure_spark_env
from pyspark.sql.functions import col, sum, avg, count

configure_spark_env()
spark = SparkSession.builder.appName("GroupBy and Aggregation").getOrCreate()

data = [(1, "Aamri", "backend", 85000, "IN"),
        (2, "Raj", "data", 72000, "IN"),
        (3, "Meera", "backend", 91000, "US"),
        (4, "Sam", "ml", 68000, "US")]

cols = ["id", "name", "domain", "salary", "country"]

df = spark.createDataFrame(data, cols)

# GroupBy and Aggregation
df2 = (
    df.groupBy(col("domain")) \
    .agg(
        sum(col("salary")).alias("total_domain_salary"),
        avg(col("salary")).alias("average_domain_salary"),
        count(col("id")).alias("domain_employee_count")
    )
)

df2.show()