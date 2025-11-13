import sqlite3

DB_NAME = "database/dolar_date.db"


def conectar():
    return sqlite3.connect(DB_NAME)


def crear_tabla():
    """Crea la tabla cotizaciones si esta no existe"""
    conn = conectar()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS cotizaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        compra REAL,
        venta REAL,
        fecha TEXT
    )
    """)

    conn.commit()
    conn.close()

def guardar_cotizacion(nombre, compra, venta, fecha):
    """Guarda una nueva cotizacion en la base de datos"""
    conn = conectar()
    c = conn.cursor()

    c.execute("""
    INSERT INTO cotizaciones (nombre, compra, venta, fecha)
    VALUES (?, ?, ?, ?)
    """, (nombre, compra, venta, fecha))

    conn.commit()
    conn.close()

def obtener_cotizaciones():
    """Te da la tabla de lade contizaciones"""
    conn = conectar()
    c = conn.cursor()

    c.execute("""
        SELECT * FROM cotizaciones
    """)

    resultados = c.fetchall()
    conn.close()
    return resultados

print(obtener_cotizaciones())