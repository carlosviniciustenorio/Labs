from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Teste").getOrCreate()
df = spark.createDataFrame([("Ana",28),("Carlos",34)], ["nome","idade"])
df.show()
spark.stop()
