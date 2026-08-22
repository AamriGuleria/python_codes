from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CachingExample").getOrCreate()

df = spark.read.csv(
	r"C:\Users\asus\Downloads\project_assets\project_assets\0_data\ecomm-raw-data\products\products.csv",
	header=True,
	inferSchema=True,
)

df.cache()

print(f"Count: {df.count()}")

df.filter(df.rating_count > 0).show()
df.unpersist()


# from pyspark.storagelevel import StorageLevel
# df.persist(StorageLevel.MEMORY_AND_DISK)