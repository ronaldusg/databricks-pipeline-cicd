# Databricks notebook source
from pyspark.sql.functions import col, year, month, sum, avg, round

# 1. EXTRACCIÓN: Leer los datos limpios y cruzados de la capa Silver
df_silver = spark.table("retail_catalog.silver.ventas_consolidadas")

# 2. MODELO DE NEGOCIO 1: Rendimiento Total por Tienda
df_ventas_tienda = df_silver.groupBy("Store", "Type", "Size").agg(
    round(sum("Weekly_Sales"), 2).alias("Total_Ventas"),
    round(avg("Weekly_Sales"), 2).alias("Promedio_Ventas_Semanales")
)

# 3. MODELO DE NEGOCIO 2: Tendencia de Ventas Mensuales
df_tendencia_mensual = df_silver.withColumn("Anio", year(col("Date"))) \
                                .withColumn("Mes", month(col("Date"))) \
                                .groupBy("Anio", "Mes").agg(
    round(sum("Weekly_Sales"), 2).alias("Total_Ventas_Mensual")
).orderBy("Anio", "Mes")

# 4. CARGA: Guardar los modelos en la capa Gold
df_ventas_tienda.write.format("delta").mode("overwrite").saveAsTable("retail_catalog.gold.ventas_por_tienda")
df_tendencia_mensual.write.format("delta").mode("overwrite").saveAsTable("retail_catalog.gold.tendencia_ventas_mensual")

print("Modelos de negocio creados y guardados exitosamente en la capa Gold.")