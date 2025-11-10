import sqlite3

conn = sqlite3.connect('database/dolar_data.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS cotizaciones (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre TEXT,
             compra REAL,
             venta REAL,
             fecha TEXT
    )""")

conn.commit()

conn.close()