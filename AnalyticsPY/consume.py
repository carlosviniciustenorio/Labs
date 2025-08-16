import os
from pyspark.sql import SparkSession, functions as F

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-17-openjdk-amd64"

spark = SparkSession.builder \
    .appName("Teste Local") \
    .master("local[*]") \
    .getOrCreate()
    
df = spark.read.parquet("output/dados_parquet", header=True, inferSchema=True)

df.show()

df \
.withColumnRenamed('id','key') \
.withColumnRenamed('idade','age') \
.withColumnRenamed('salario','compensation') \
.withColumnRenamed('salario_mensal','compensation per month') \
.withColumn("compensation", F.round(F.col("compensation") + 1000, 2)) \
.withColumn("compensation per month", F.round(F.col("compensation") / 12, 2)) \
.filter("age % 2 == 0") \
.sort(F.col("age").asc()) \
.show()

df_pandas = df.toPandas()

spark.stop()

print(df_pandas)
print(df_pandas.head())      # primeiras 5 linhas
print(df_pandas.tail())      # últimas 5 linhas
print(df_pandas.info())      # resumo das colunas, tipos e valores nulos
print(df_pandas.describe())  # estatísticas descritivas das colunas numéricas
print(df_pandas.columns)     # nomes das colunas