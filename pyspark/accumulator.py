import os
import sys

from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

spark = SparkSession.builder.appName("AccumulatorExample").getOrCreate()
sc = spark.sparkContext
error_count = sc.accumulator(0)


def process_data(record):
    if "BAD_DATA" in record:
        error_count.add(1)
        return None
    return record.upper()


data = [
    "GOOD_RECORD_1",
    "BAD_DATA_1",
    "GOOD_RECORD_2",
    "BAD_DATA_2",
    "GOOD_RECORD_3",
]
rdd = sc.parallelize(data)
result = rdd.map(process_data).filter(lambda x: x is not None).collect()
print(f"Processed records: {result}")
print(f"Total errors found: {error_count.value}")

spark.stop()