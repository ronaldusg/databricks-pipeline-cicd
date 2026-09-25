-- Eliminar tablas físicas y lógicas
DROP TABLE IF EXISTS retail_catalog.gold.ventas_por_tienda;
DROP TABLE IF EXISTS retail_catalog.gold.tendencia_ventas_mensual;
DROP TABLE IF EXISTS retail_catalog.silver.ventas_consolidadas;
DROP TABLE IF EXISTS retail_catalog.bronze.features;
DROP TABLE IF EXISTS retail_catalog.bronze.sales;
DROP TABLE IF EXISTS retail_catalog.bronze.stores;

-- Eliminar esquemas
DROP SCHEMA IF EXISTS retail_catalog.gold CASCADE;
DROP SCHEMA IF EXISTS retail_catalog.silver CASCADE;
DROP SCHEMA IF EXISTS retail_catalog.bronze CASCADE;

-- Eliminar el catálogo completo
DROP CATALOG IF EXISTS retail_catalog CASCADE;
