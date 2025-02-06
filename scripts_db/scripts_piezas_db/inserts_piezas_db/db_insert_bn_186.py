import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("catalogo.db")  # Replace with your database file
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON;")

# Data to insert
piezas_data = [
    ("BN", "186"),  # Add more rows here as needed
]

parametros_data = [
    (1, 9),  # (tipo_seccion, trapecios)
]

trapecios_data = [
    (1, 9, 1.530, 1.530, 0.200), # En jacena el 9no trapecio es in situ --->  Crear Campo para especificar material/inSitu o Tabla separada para trapecios que no son de Prefabricado
    (1, 8, 1.530, 1.530, 0.050), # (tipo_seccion, posicion, base_inf, base_sup, altura)
    (1, 7, 0.430, 1.530, 0.060),
    (1, 6, 0.180, 0.430, 0.200),
    (1, 5, 0.180, 0.180, 1.100),
    (1, 4, 0.270, 0.180, 0.150),
    (1, 3, 0.720, 0.270, 0.150),
    (1, 2, 0.720, 0.720, 0.125),
    (1, 1, 0.670, 0.720, 0.025)
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
        "INSERT INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id) VALUES (?, ?, ?, ?, ?, ?);",
        trapecios_data_with_id,
    )

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Se insertaron los datos de: CH - 51")