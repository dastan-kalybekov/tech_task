from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col

spark = SparkSession.builder.appName("ProductCategory").getOrCreate()

df = (spark.read.format("json")
      .option("inferSchema", "true")
      .option("header", "true")
      .load("db.json"))

categories_df = df.select("product_name", explode("categories").alias("category"))

all_products_df = df.select("product_name")

result_df = all_products_df.join(categories_df, "product_name", "left_outer")

result_df = result_df.filter((col("product_name").isNotNull()) | (col("category").isNotNull()))

result_df.show()

spark.stop()
