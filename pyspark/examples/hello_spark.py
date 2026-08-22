import os
import sys
from pyspark.sql import SparkSession


os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

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
