-- Otorgar uso sobre el catálogo y esquema principal
GRANT USAGE ON CATALOG retail_catalog TO `account users`;
GRANT USAGE ON SCHEMA retail_catalog.gold TO `account users`;

-- Otorgar permisos de lectura (SELECT) sobre las tablas finales
GRANT SELECT ON TABLE retail_catalog.gold.ventas_por_tienda TO `account users`;
GRANT SELECT ON TABLE retail_catalog.gold.tendencia_ventas_mensual TO `account users`;
