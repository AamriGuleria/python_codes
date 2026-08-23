from pyspark.sql import SparkSession
from spark_env import configure_spark_env
from pyspark.sql.functions import broadcast

configure_spark_env()
spark = SparkSession.builder.appName("Joins").getOrCreate()

emp_data = [(1, "Aamri", 1, 85000),
           (2, "Raj", 2, 72000),
           (3, "Meera", 3, 91000),
           (4, "Sam", None, 68000)]

depts = [(1,"IT", "Hyderabad"),
           (2,"Data", "Bangalore"),
           (3,"ML", "Bangalore")]

emp_df = spark.createDataFrame(emp_data, ["id", "name", "dept_id", "salary"])
dept_df = spark.createDataFrame(depts, ["id", "name", "location"])

df2 = emp_df.join(dept_df, emp_df.dept_id == dept_df.id, "inner")
df3 = emp_df.join(dept_df, emp_df.dept_id == dept_df.id, "left")
df4 = emp_df.join(dept_df, emp_df.dept_id == dept_df.id, "right")
df5 = emp_df.join(dept_df, emp_df.dept_id == dept_df.id, "full")
df6 = emp_df.join(broadcast(depts), emp_df.dept_id == dept_df.id, how="inner").show()
df6.show()

