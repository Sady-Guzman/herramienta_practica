import sqlite3

def db_cargar_familias_modelos(es_catalogo):
    """
        Conecta la base de datos y recupera tuplas para poblar combo_familia y combo_modelo.
        Retorna un diccionario donde cada familia mapea a una lista de modelos.

        db_es_catalogo: True -> Usa base datos catalogo.db, donde estan las piezas migradas de Jacena
                        False -> Usa base datos creada por usuario (piezas_creadas.db)
    """

    if es_catalogo == True:
        db_path = 'catalogo.db' 
    else:
        db_path = 'piezas_creadas.db'
    
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Diccionario para guardar el mapeo de familia-modelos
    dict_fam_mod = {}

    try:
        # Fetch distinct familia values
        cursor.execute("SELECT DISTINCT familia FROM piezas") 
        familias = cursor.fetchall()

        # agrega al diccionario las familias con sus respectivos modelos
        for familia in familias:
            family = familia[0]  # Extrae valor familia de la tupla
            cursor.execute("SELECT modelo FROM piezas WHERE familia = ?", (family,))
            modelos = [row[0] for row in cursor.fetchall()]
            dict_fam_mod[family] = modelos
    except sqlite3.Error as e:
        print(f"DEBUG db_cargar_fam_mod() > Database error: {e}")
    finally:
        # Close the database connection
        connection.close()

    return dict_fam_mod

def db_cargar_tipos_secciones(familia, modelo, es_catalogo):
    """
    obtiene tipos de secciones existentes para una pieza seleccionada
    """
    print("XXXXXXXXXXXXXXXXXXXXXXXXXX valor es_catalogo: ", es_catalogo)

    if es_catalogo == True:
        db_path = 'catalogo.db' 
    else:
        db_path = 'piezas_creadas.db'
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Diccionario para guardar el mapeo de familia-modelos
    tipos_secciones = []

    try:    
        query = """
        SELECT parametros.tipo_seccion
        FROM parametros
        JOIN piezas ON parametros.pieza_id = piezas.id
        WHERE piezas.familia = ? AND piezas.modelo = ?;
        """

        # Execute the query with the provided familia and modelo
        cursor.execute(query, (familia, modelo))

        # Fetch all matching rows
        tipos_secciones = cursor.fetchall()

        # Close the database connection
        conn.close()

    except sqlite3.Error as e:
        print(f"Debug print db_cargar_tipos_secciones() -> Database error: {e}")
    finally:
        # Close the database connection
        conn.close()

    print(tipos_secciones)

    return tipos_secciones




def db_get_datos_trapecios(pieza_id, seccion, es_creada):
    # Connect to the database
    # conn = sqlite3.connect("catalogo.db")  # Replace with your database file
    # cursor = conn.cursor()

    if es_creada == False:
        conn = sqlite3.connect("catalogo.db")
    else:
        conn = sqlite3.connect("piezas_creadas.db")
    cursor = conn.cursor()

    print("pieza_id = " ,pieza_id)
    pieza_id_str = pieza_id[0]
    print("pieza_id_Str = ", pieza_id_str)

    
    # Query to get the trapecios from the trapecios table based on pieza_id and tipo_seccion
    cursor.execute("""
        SELECT * FROM trapecios WHERE pieza_id = ? AND tipo_seccion = ?
    """, (pieza_id_str, seccion))

    # Fetch all matching trapecios
    trapecios = cursor.fetchall()

    # Close the database connection
    conn.close()


    return trapecios


def db_get_cant_trapecios(pieza_id, seccion, es_creada):
    # Connect to the database
    # conn = sqlite3.connect("catalogo.db")  # Replace with your database file
    # cursor = conn.cursor()

    if es_creada == False:
        conn = sqlite3.connect("catalogo.db")
    else:
        conn = sqlite3.connect("piezas_creadas.db")
    cursor = conn.cursor()

    print("pieza_id = " ,pieza_id)
    pieza_id_str = pieza_id[0]
    print("pieza_id_Str = ", pieza_id_str)

    
    # Query to get the trapecios from the trapecios table based on pieza_id and tipo_seccion
    cursor.execute("""
        SELECT trapecios FROM parametros WHERE pieza_id = ? AND tipo_seccion = ?
    """, (pieza_id_str, seccion))

    # Fetch all matching trapecios
    cant_trapecios = cursor.fetchone()
    cant_trapecios = cant_trapecios[0]

    # Close the database connection
    conn.close()

    print("DEBUG get_cant_trapecios > Cantidad de trapecios en seccion: ", cant_trapecios)
    return cant_trapecios

def db_get_id_pieza(familia, modelo, es_creada):
    """
    Fetch the pieza_id for a given familia and modelo.
    """

    # print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB --> Valor es_Creada: ", es_creada)
    # print("valor familia y modelo: ",familia, modelo)
    # Connect to the database
    if es_creada == False:
        conn = sqlite3.connect("catalogo.db")
    else:
        conn = sqlite3.connect("piezas_creadas.db")
    cursor = conn.cursor()

    try:
        # Query to get pieza_id from the piezas table
        cursor.execute("""
            SELECT id FROM piezas WHERE familia = ? AND modelo = ?
        """, (familia, modelo))

        # Fetch the pieza_id
        pieza_id = cursor.fetchone()

        if pieza_id:
            return pieza_id  # Return the pieza_id as a tuple
        else:
            print(f"Debug: No pieza_id found for familia '{familia}' and modelo '{modelo}'")
            return None
    except sqlite3.Error as e:
        print(f"Debug: Database error in db_get_id_pieza: {e}")
        return None
    finally:
        # Close the database connection
        conn.close()


''' print todas las familias y sus respectivos modelos de forma estructurada'''
def print_familias_modelos():
    def print_families_and_models(title, data):
        print(title)
        for family, models in data.items():
            print(f"Family: {family}")
            print("Models:")
            for model in models:
                print(f"  - {model}")
            print()
    

    dict_fam_mod_catalogo = db_cargar_familias_modelos(True)
    dict_fam_mod_creadas = db_cargar_familias_modelos(False)

    print_families_and_models("Piezas CATALOGO", dict_fam_mod_catalogo)
    print_families_and_models("Piezas CREADAS", dict_fam_mod_creadas)

''' init_db '''
def db_iniciar_database(db_path):
    """
    Inicializa la base de datos creando las tablas requeridas si no existen.

    Args:
        db_path (str): Path al archivo base de datos (ej., 'catalogo.db').
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Revisa si existe la relacion
    def table_exists(table_name):
        cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name=?
        """, (table_name,))
        return cursor.fetchone() is not None

    try:
        # REVISAR RELACION PIEZAS
        if not table_exists("piezas"):
            cursor.execute("""
                CREATE TABLE piezas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    familia TEXT NOT NULL,
                    modelo TEXT NOT NULL UNIQUE
                )
            """)
            print(f"init_db {db_path} > Tabla 'piezas' creada.")
        else:
            print(f"init_db {db_path} > La relacion 'piezas' ya existe. No se realizaron cambios.")

        # REVISAR RELACION PARAMETROS
        if not table_exists("parametros"):
            cursor.execute("""
                CREATE TABLE parametros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo_seccion INTEGER NOT NULL,
                    trapecios INTEGER NOT NULL,
                    pieza_id INTEGER NOT NULL, 
                    FOREIGN KEY (pieza_id) REFERENCES piezas (id)
                )
            """)
            print(f"init_db {db_path} > Tabla 'parametros' creada")
        else:
            print(f"init_db {db_path} > La relacion 'parametros' ya existe. No se realizaron cambios.")

        # REVISAR RELACION TRAPECIOS
        if not table_exists("trapecios"):
            cursor.execute("""
                CREATE TABLE trapecios (
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
            print(f"init_db {db_path} > Tabla 'trapecios' creada.")
        else:
            print(f"init_db {db_path} > La relacion 'trapecios' ya existe. No se realizaron cambios.")

    except sqlite3.Error as e:
        print(f"DEBUG error al inicializar DB '{db_path}': {e}")
    finally:
        connection.close()

    return


''' ==================================================================================================== '''

# def insert_pieza_dynamically(pieza_data, parametros_data, trapecios_data):
#     """
#     Inserts a new pieza into the database with a variable number of sections (parametros)
#     and trapezoids (trapecios).
    
#     :param db_path: Path to the SQLite database file.
#     :param pieza_data: Tuple containing the familia and modelo for the pieza.
#     :param parametros_data: List of tuples, each representing a (tipo_seccion, trapecios).
#     :param trapecios_data: List of tuples, each representing a (tipo_seccion, posicion, base_inf, base_sup, altura).
#     """
#     # Connect to SQLite database
#     conn = sqlite3.connect("piezas_creadas.db")
#     cursor = conn.cursor()

#     # Enable foreign key constraints
#     cursor.execute("PRAGMA foreign_keys = ON;")

#     try:
#         # Insert data into piezas and fetch the auto-generated pieza_id
#         cursor.execute("INSERT INTO piezas (familia, modelo) VALUES (?, ?);", pieza_data)
#         pieza_id = cursor.lastrowid  # Dynamically fetch the ID of the last inserted row

#         # Insert data into parametros using the fetched pieza_id
#         parametros_data_with_id = [(ts, tr, pieza_id) for ts, tr in parametros_data]
#         cursor.executemany(
#             "INSERT INTO parametros (tipo_seccion, trapecios, pieza_id) VALUES (?, ?, ?);",
#             parametros_data_with_id,
#         )

#         # Insert data into trapecios using the fetched pieza_id
#         trapecios_data_with_id = [(ts, pos, bi, bs, h, pieza_id) for ts, pos, bi, bs, h in trapecios_data]
#         cursor.executemany(
#             "INSERT INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id) VALUES (?, ?, ?, ?, ?, ?);",
#             trapecios_data_with_id,
#         )

#         # Commit the transaction
#         conn.commit()
#         print(f"Se insertaron los datos de: {pieza_data[0]} - {pieza_data[1]}")

#     except sqlite3.Error as e:
#         print(f"Error inserting data: {e}")
#         conn.rollback()  # Rollback in case of an error

#     finally:
#         # Close the connection
#         conn.close()


def db_insert_or_update_pieza(pieza_data, parametros_data, trapecios_data):
    """
    Inserts or updates a pieza in the database. If the pieza's modelo already exists, 
    updates the existing record and its related data.
    
    :param db_path: Path to the SQLite database file.
    :param pieza_data: Tuple containing the familia and modelo for the pieza.
    :param parametros_data: List of tuples, each representing a (tipo_seccion, trapecios).
    :param trapecios_data: List of tuples, each representing a (tipo_seccion, posicion, base_inf, base_sup, altura).
    """
    # Connect to SQLite database
    conn = sqlite3.connect("piezas_creadas.db")
    cursor = conn.cursor()

    # Enable foreign key constraints
    cursor.execute("PRAGMA foreign_keys = ON;")

    try:
        # Check if a pieza with the same modelo already exists
        cursor.execute("SELECT id FROM piezas WHERE modelo = ?;", (pieza_data[1],))
        existing_pieza = cursor.fetchone()

        if existing_pieza:
            # If pieza exists, fetch its ID
            pieza_id = existing_pieza[0]
            print(f"Pieza with modelo '{pieza_data[1]}' already exists. Updating data.")

            # Update the familia column for the existing pieza
            cursor.execute("UPDATE piezas SET familia = ? WHERE id = ?;", (pieza_data[0], pieza_id))

            # Delete existing related records in parametros and trapecios
            cursor.execute("DELETE FROM parametros WHERE pieza_id = ?;", (pieza_id,))
            cursor.execute("DELETE FROM trapecios WHERE pieza_id = ?;", (pieza_id,))
        else:
            # If pieza does not exist, insert it and get the new pieza_id
            cursor.execute("INSERT INTO piezas (familia, modelo) VALUES (?, ?);", pieza_data)
            pieza_id = cursor.lastrowid
            print(f"Inserted new pieza: {pieza_data[0]} - {pieza_data[1]}")

        # Insert data into parametros using the pieza_id
        parametros_data_with_id = [(ts, tr, pieza_id) for ts, tr in parametros_data]
        cursor.executemany(
            "INSERT INTO parametros (tipo_seccion, trapecios, pieza_id) VALUES (?, ?, ?);",
            parametros_data_with_id,
        )

        # Insert data into trapecios using the pieza_id
        trapecios_data_with_id = [(ts, pos, bi, bs, h, pieza_id) for ts, pos, bi, bs, h in trapecios_data]
        cursor.executemany(
            "INSERT INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id) VALUES (?, ?, ?, ?, ?, ?);",
            trapecios_data_with_id,
        )

        # Commit the transaction
        conn.commit()
        print(f"Data successfully inserted/updated for pieza: {pieza_data[0]} - {pieza_data[1]}")

    except sqlite3.Error as e:
        print(f"Error inserting/updating data: {e}")
        conn.rollback()  # Rollback in case of an error

    finally:
        # Close the connection
        conn.close()




# def insert_or_update_pieza(piezas_data, parametros_data, trapecios_data):
    
#     # Connect to SQLite database
#     conn = sqlite3.connect("piezas_creadas.db")
#     cursor = conn.cursor()

#     # Enable foreign key constraints
#     cursor.execute("PRAGMA foreign_keys = ON;")
    
#     # Insert or update data
#     for familia, modelo in piezas_data:
#         # Check if the pieza already exists
#         cursor.execute("SELECT id FROM piezas WHERE modelo = ?", (modelo,))
#         result = cursor.fetchone()

#         if result:
#             # If pieza exists, fetch its ID
#             pieza_id = result[0]

#             # Update the pieza (optional if familia or other data can change)
#             cursor.execute(
#                 "UPDATE piezas SET familia = ? WHERE id = ?;",
#                 (familia, pieza_id),
#             )

#             # Update related records in parametros
#             cursor.execute("DELETE FROM parametros WHERE pieza_id = ?", (pieza_id,))
#             parametros_data_with_id = [(ts, tr, pieza_id) for ts, tr in parametros_data]
#             cursor.executemany(
#                 "INSERT INTO parametros (tipo_seccion, trapecios, pieza_id) VALUES (?, ?, ?);",
#                 parametros_data_with_id,
#             )

#             # Update related records in trapecios
#             cursor.execute("DELETE FROM trapecios WHERE pieza_id = ?", (pieza_id,))
#             trapecios_data_with_id = [(ts, pos, bi, bs, h, pieza_id) for ts, pos, bi, bs, h in trapecios_data]
#             cursor.executemany(
#                 "INSERT INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id) VALUES (?, ?, ?, ?, ?, ?);",
#                 trapecios_data_with_id,
#             )

#             print(f"Pieza existente actualizada: {familia} - {modelo}")
#         else:
#             # If pieza doesn't exist, insert it and fetch the new ID
#             cursor.execute("INSERT INTO piezas (familia, modelo) VALUES (?, ?);", (familia, modelo))
#             pieza_id = cursor.lastrowid  # Dynamically fetch the ID of the last inserted row

#             # Insert data into parametros
#             parametros_data_with_id = [(ts, tr, pieza_id) for ts, tr in parametros_data]
#             cursor.executemany(
#                 "INSERT INTO parametros (tipo_seccion, trapecios, pieza_id) VALUES (?, ?, ?);",
#                 parametros_data_with_id,
#             )

#             # Insert data into trapecios
#             trapecios_data_with_id = [(ts, pos, bi, bs, h, pieza_id) for ts, pos, bi, bs, h in trapecios_data]
#             cursor.executemany(
#                 "INSERT INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id) VALUES (?, ?, ?, ?, ?, ?);",
#                 trapecios_data_with_id,
#             )

#             print(f"Se insertó una nueva pieza: {familia} - {modelo}")

#     # Commit the transaction
#     conn.commit()

#     # Close the connection
#     conn.close()

#     print("Operación completada.")