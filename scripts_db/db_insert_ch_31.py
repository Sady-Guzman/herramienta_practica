import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("catalogo.db")  # Replace with your database file
cursor = conn.cursor()

# Enable foreign key constraints
cursor.execute("PRAGMA foreign_keys = ON;")

# Data to insert
piezas_data = [
    ("CH", "31"),  # Add more rows here as needed
]

parametros_data = [
    (1, 3),  # (tipo_seccion, trapecios)
]

trapecios_data = [
    (1, 3, 0.400, 0.400, 0.103),  # (tipo_seccion, posicion, base_inf, base_sup, altura)
    (1, 2, 0.160, 0.200, 0.192),
    (1, 1, 0.100, 0.160, 0.015)
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

print("Se insertaron los datos de: CH - 31")