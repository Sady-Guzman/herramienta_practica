import sqlite3

def cargar_familias_modelos_db():
    """
    Connects to the database and fetches data to populate combo_familia and combo_modelo.
    Returns a dictionary where each familia maps to a list of modelos.
    """

    db_path = 'catalogo.db' 
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


import sqlite3

def db_get_trapecios_por_nombre(familia, modelo):
    """
    Conecta a DB y obtiene cantidad de trapecios en cada seccion
    """

    conn = sqlite3.connect("catalogo.db")  # Replace with your database file
    cursor = conn.cursor()

    # Enable foreign key constraints
    cursor.execute("PRAGMA foreign_keys = ON;")

    # SQL query to join the tables and fetch trapecios
    query = """
        SELECT parametros.trapecios
        FROM parametros
        JOIN piezas ON parametros.pieza_id = piezas.id
        WHERE piezas.familia = ? AND piezas.modelo = ?;
    """

    # Execute the query with the provided familia and modelo
    cursor.execute(query, (familia, modelo))

    # Fetch all matching rows
    trapecios = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Return the results as a list of trapecios
    return [row[0] for row in trapecios]


''' print todas las familias y sus respectivos modelos de forma estructurada'''
def print_familias_modelos():
    dict_fam_mod = cargar_familias_modelos_db()

    for familias, modelos in dict_fam_mod.items():
        print(f"Family: {familias}")
        print("Models:")
        for model in modelos:
            print(f"  - {model}")
        print()
