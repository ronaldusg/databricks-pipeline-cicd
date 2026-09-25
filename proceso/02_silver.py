# Databricks notebook source
from pyspark.sql.functions import col, to_date, lit
from pyspark.sql.types import DecimalType

# 1. EXTRACCIÓN: Leer los datos desde la capa Bronze
df_sales = spark.table("retail_catalog.bronze.sales")
df_features = spark.table("retail_catalog.bronze.features")
df_stores = spark.table("retail_catalog.bronze.stores")

# 2. LIMPIEZA Y FORMATOS (Regla del ETL Silver)

# A. Limpieza de Ventas (Sales)
df_sales = df_sales.withColumn("Date", to_date(col("Date"), "dd/MM/yyyy"))
df_sales = df_sales.withColumn("Weekly_Sales", col("Weekly_Sales").cast(DecimalType(18, 2)))
df_sales = df_sales.dropDuplicates()

# B. Limpieza de Características (Features)
df_features = df_features.withColumn("Date", to_date(col("Date"), "dd/MM/yyyy"))
markdown_cols = ["MarkDown1", "MarkDown2", "MarkDown3", "MarkDown4", "MarkDown5"]
df_features = df_features.fillna(0, subset=markdown_cols)
df_features = df_features.drop("IsHoliday")
df_features = df_features.dropDuplicates()

# C. Limpieza de Tiendas (Stores)
df_stores = df_stores.dropDuplicates()

# 3. TRANSFORMACIÓN: Cruces (JOINs)
df_step1 = df_sales.join(df_stores, on="Store", how="left")
df_silver = df_step1.join(df_features, on=["Store", "Date"], how="left")

# 4. CARGA: Guardar en la capa Silver
df_silver.write.format("delta").mode("overwrite").saveAsTable("retail_catalog.silver.ventas_consolidadas")

print("Limpieza, transformación (JOINs) y carga a Silver completada exitosamente.")