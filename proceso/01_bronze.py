# Databricks notebook source
# 1. Definir la ruta base del Data Lake 
ruta_raw = "abfss://raw@adlsmedallionproyfinal.dfs.core.windows.net/"

# 2. Leer los tres archivos CSV
df_features = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(ruta_raw + "Features data set.csv")
df_sales = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(ruta_raw + "sales data-set.csv")
df_stores = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(ruta_raw + "stores data-set.csv")

# 3. Guardar los DataFrames como tablas Delta en la capa Bronze
df_features.write.format("delta").mode("overwrite").saveAsTable("retail_catalog.bronze.features")
df_sales.write.format("delta").mode("overwrite").saveAsTable("retail_catalog.bronze.sales")
df_stores.write.format("delta").mode("overwrite").saveAsTable("retail_catalog.bronze.stores")

print("Carga a Bronze completada exitosamente.")