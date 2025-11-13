from database.db_maneger import crear_tabla, guardar_cotizacion, obtener_cotizaciones

crear_tabla()

guardar_cotizacion("Dolar Blue", 950.50, 970.00, "2025-11-10")



print("✅ Cotización guardada correctamente.")