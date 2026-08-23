from spark_env import configure_spark_env

configure_spark_env()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BroadCast_Variable").getOrCreate()
sc = spark.sparkContext
# Without Broadcast
lookup = {"US": "United States", "UK": "United Kingdom"}
# Create sample RDD
data = ["US", "UK", "US", "IN", "UK", "CA"]
rdd = sc.parallelize(data)

rdd.map(lambda x: (x,lookup.get(x,'Unknown')))


# With Lookup
broadcast_lookup = sc.broadcast(lookup)
# rdd.map(lambda x: (x,broadcast_lookup.value.get(x, "Unknown")))
result_with_broadcast = rdd.map(lambda x: (x, broadcast_lookup.value.get(x, "Unknown"))).collect()

print("With Broadcast Result:")
for item in result_with_broadcast:
    print(item)

# 2. Cleanup (Good practice to free memory)
broadcast_lookup.unpersist()

# 3. Stop the session
spark.stop()