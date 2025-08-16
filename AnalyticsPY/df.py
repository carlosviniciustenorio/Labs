from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import time

spark = SparkSession.builder \
    .appName("Teste Local") \
    .master("local[*]") \
    .getOrCreate()
    
df = spark.range(0, 100_000_000).repartition(4)

start = time.time()
df.filter(col("id") % 2 == 0).count()
print("Tempo de execução:", time.time() - start)

input("Pressione Enter para encerrar o Spark...")
spark.stop()