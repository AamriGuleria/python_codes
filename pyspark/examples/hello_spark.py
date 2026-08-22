from pyspark.sql import SparkSession


spark = (
    SparkSession.builder
    .appName("PySparkPractice")
    .master("local[*]")
    .getOrCreate()
)

try:
    numbers = spark.createDataFrame(
        [(1, "python"), (2, "pyspark"), (3, "sql")],
        ["id", "topic"],
    )

    numbers.show()
    numbers.groupBy().count().show()
finally:
    spark.stop()
