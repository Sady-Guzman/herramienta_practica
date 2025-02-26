import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("catalogo.db")  # Replace with your database file
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON;")

# Data to insert
piezas_data = [
    ("BN", "080_CH"),  # Add more rows here as needed
]

parametros_data = [
    (1, 9),  # (tipo_seccion, trapecios)
]

trapecios_data = [
    (1, 1, 0.570, 0.620, 0.025, 0)
    (1, 2, 0.620, 0.620, 0.125, 0),
    (1, 3, 0.620, 0.320, 0.050, 0),
    (1, 4, 0.320, 0.150, 0.100, 0),
    (1, 5, 0.150, 0.150, 0.290, 0),
    (1, 6, 0.150, 0.530, 0.100, 0),
    (1, 7, 0.530, 1.170, 0.038, 0),
    (1, 8, 1.170, 1.170, 0.072, 0), # (tipo_seccion, posicion, base_inf, base_sup, altura)
    (1, 9, 1.170, 1.170, 0.200, 1), # En jacena el 9no trapecio es in situ --->  Crear Campo para especificar material/inSitu o Tabla separada para trapecios que no son de Prefabricado
]

# Insert data into piezas and fetch the auto-generated pieza_id
for familia, modelo in piezas_data:
    cursor.execute("INSERT INTO piezas (familia, modelo) VALUES (?, ?);", (familia, modelo))
    pieza_id = cursor.lastrowid  # Dynamically fetch the ID of the last inserted row

    # Insert data into parametros using the fetched pieza_id
    parametros_data_with_id = [(ts, tr, pieza_id) for ts, tr in parametros_data]
    cursor.executemany(
        "INSERT INTO parametros (tipo_seccion, trapecios, pieza_id) VALUES (?, ?, ?);",
        parametros_data_with_id,
    )

    # Insert data into trapecios using the fetched pieza_id
    trapecios_data_with_id = [(ts, pos, bi, bs, h, pieza_id) for ts, pos, bi, bs, h in trapecios_data]
    cursor.executemany(
        "INSERT INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id, es_insitu) VALUES (?, ?, ?, ?, ?, ?, ?);",
        trapecios_data_with_id,
    )

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Se insertaron los datos de: BN 080CH")