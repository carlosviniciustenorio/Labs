import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-17-openjdk-amd64"

spark = SparkSession.builder \
    .appName("Teste Local") \
    .master("local[*]") \
    .getOrCreate()

df = spark.read.csv("input/dados.csv", header=True, inferSchema=True)

print(f'num of partitions: {df.rdd.getNumPartitions()}')

df.show()

df_changed = df \
            .withColumn("salario_mensal", col("salario") / 12) \
            .withColumnRenamed("nome","alias") \
            .filter(col("salario_mensal") > 400) \
            .orderBy(col("id"))

df_changed.show()

df_changed.write.mode('overwrite').parquet("output/dados_parquet")

spark.stop()