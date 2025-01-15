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
        print(f"Debug print> Database error: {e}")
    finally:
        # Close the database connection
        connection.close()

    return dict_fam_mod

def db_cargar_tipos_secciones(familia, modelo):
    """
    obtiene tipos de secciones existentes para una pieza seleccionada
    """

    db_path = 'catalogo.db' 
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
        print(f"Debug print> Database error: {e}")
    finally:
        # Close the database connection
        conn.close()

    print(tipos_secciones)

    return tipos_secciones





def db_get_datos_trapecios(pieza_id, seccion):
    # Connect to the database
    conn = sqlite3.connect("catalogo.db")  # Replace with your database file
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


def db_get_cant_trapecios(pieza_id, seccion):
    # Connect to the database
    conn = sqlite3.connect("catalogo.db")  # Replace with your database file
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

def db_get_id_pieza(familia, modelo):
    # Connect to the database
    conn = sqlite3.connect("catalogo.db")  # Replace with your database file
    cursor = conn.cursor()

    # Query to get the pieza_id from the piezas table based on familia and modelo
    cursor.execute("""
        SELECT id FROM piezas WHERE familia = ? AND modelo = ?
    """, (familia, modelo))
    pieza_id = cursor.fetchone()

    # If no match is found in the piezas table
    if pieza_id is None:
        print(f"No se encontró la pieza con familia: {familia} y modelo: {modelo}")
        conn.close()
        return []
    
    print("debug.db_get_id_pieza() > id pieza: ", pieza_id)
    return pieza_id


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

def db_iniciar_catalogo(db_path):
    """
    Initializes the database by creating the required tables if they do not exist.

    Args:
        db_path (str): The path to the database file (e.g., 'catalogo.db').
    """
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    try:
        # Create the `piezas` table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS piezas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                familia TEXT NOT NULL,
                modelo TEXT NOT NULL
            )
        """)

        # Create the `parametros` table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS parametros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo_seccion INTEGER NOT NULL,
                trapecios INTEGER NOT NULL,
                pieza_id INTEGER NOT NULL, 
                FOREIGN KEY (pieza_id) REFERENCES piezas (id)
            )
        """)

        # Create the `trapecios` table
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

        print(f"Database '{db_path}' initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error initializing database '{db_path}': {e}")
    finally:
        # Ensure the connection is closed
        connection.close()

    return
