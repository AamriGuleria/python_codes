import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from spark_env import configure_spark_env
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession
from delta.tables import DeltaTable

configure_spark_env()

spark = (
    configure_spark_with_delta_pip(
        SparkSession.builder
        .appName("DeltaExample")
        .master("local[*]")
    )
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

data = [
    (1, "Aamri", "backend", 85000, "IN"),
    (2, "Raj", "data", 72000, "IN"),
    (3, "Meera", "backend", 91000, "US"),
    (4, "Sam", "ml", 68000, "US"),
]

columns = ["id", "name", "domain", "salary", "country"]

df = spark.createDataFrame(data, columns)

df.write.format("delta").mode("overwrite").saveAsTable("bronze_employees")
spark.sql("SELECT * FROM bronze_employees").show()


new_data = spark.createDataFrame(
    [(2, "Raj", "data", 78000, "IN"),   
     (5, "Priya", "ml", 70000, "IN")], 
    columns
)
new_data.createOrReplaceTempView("updates")
delta_table = DeltaTable.forName(spark, "bronze_employees")

delta_table.alias("target").merge(new_data.alias("source"),"target.id = source.id") \
    .whenMatchedUpdateAll() \
    .whenNotMatchedInsertAll().execute()

spark.sql("SELECT * FROM bronze_employees ORDER BY id").show()

spark.stop()