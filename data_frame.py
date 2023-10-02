from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col

spark = SparkSession.builder.appName("ProductCategory").getOrCreate()

df = (spark.read.format("json")
      .option("inferSchema", "true")  # Автоматическое определение схемы данных
      .load("db.json"))

categories_df = df.select("product_name", explode("categories").alias("category"))

all_products_df = df.select("product_name")

# Соединяем два DataFrame по столбцу "product_name" с использованием левого внешнего соединения
result_df = all_products_df.join(categories_df, "product_name", "left_outer")

# Фильтруем результат, оставляя только строки, где хотя бы один из столбцов ("product_name" или "category") не равен null
result_df = result_df.filter((col("product_name").isNotNull()) | (col("category").isNotNull()))

result_df.show()

spark.stop()
