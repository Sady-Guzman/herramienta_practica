import sqlite3

# Path to SQLite database file
db_path = "catalogo.db"

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create tables (they will be created if they don't already exist)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS piezas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        familia TEXT NOT NULL,
        modelo TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS parametros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_seccion INTEGER NOT NULL,
        trapecios INTEGER NOT NULL,
        pieza_id INTEGER NOT NULL, 
        FOREIGN KEY (pieza_id) REFERENCES piezas (id)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS trapecios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_seccion TEXT NOT NULL,
        posicion INTEGER NOT NULL,
        base_inf REAL NOT NULL,
        base_sup REAL NOT NULL,
        altura REAL NOT NULL,
        pieza_id INTEGER NOT NULL,
        FOREIGN KEY (pieza_id) REFERENCES piezas (id)
    )
""")

# Commit changes and close the connection
conn.commit()
conn.close()
