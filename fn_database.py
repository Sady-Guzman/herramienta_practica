import sqlite3

def db_cargar_familias_modelos(self, tipo_db):
    """
        Conecta la base de datos y recupera tuplas para poblar combo_familia y combo_modelo.
        Retorna un diccionario donde cada familia mapea a una lista de modelos.

        tipo_db: True -> Usa base datos catalogo.db, donde estan las piezas migradas de Jacena
                        False -> Usa base datos creada por usuario (piezas_creadas.db)
    """

    if tipo_db == True:
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

def db_cargar_tipos_secciones(familia, modelo, es_creada):
    """ obtiene tipos de secciones existentes para una pieza seleccionada """

    print("db_cargar_tipos_secciones() -> valor es_creada: ", es_creada, "\n")

    if es_creada == False:
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

    print("db_cargar_tipos_secciones() --> Contenido de tipos_secciones: ", tipos_secciones ,"\n")

    return tipos_secciones




def db_get_datos_trapecios(pieza_id, seccion, es_creada):
    '''
        Con id de pieza + seccion seleccionada en GUI en ese momento, Esta funcion retorna todos los trapecios correspondientes.
    '''

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
    '''
        Con id de pieza + seccion seleccionada, Retorna la cantidad de trapecios de esa seccion. 
        Resultado de usa principalmente como parametro para que funcion ajustar_layouts() sepa cuantas tuplas generar en GUI
    '''

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
    ''' Obtiene id de pieza usando los valores de familia + modelo seleccionados en ComboBoxes de GUI '''

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


''' print todas las familias y sus respectivos modelos de forma estructurada... Esta en desuso por cambio en db_cargar_familias_modelos()'''
def print_familias_modelos():
    def print_families_and_models(title, data):
        print(title)
        for family, models in data.items():
            print(f"Family: {family}")
            print("Models:")
            for model in models:
                print(f"  - {model}")
            print()
    

    dict_fam_mod_catalogo = db_cargar_familias_modelos()
    dict_fam_mod_creadas = db_cargar_familias_modelos()

    print_families_and_models("Piezas CATALOGO", dict_fam_mod_catalogo)
    print_families_and_models("Piezas CREADAS", dict_fam_mod_creadas)


''' ==========================================================================================================================='''
''' Funciones para iniciar estructura (esquema / schema) de bases de datos catalogo.db y piezas_creadas.db 
    -- Solo ejecuta rutinas si las bases de datos no estan iniciadas, Por lo tanto solo se usa cuando se inicia el software por primera vez'''
''' INIT para basde de datos de piezas migradas de JACENA (catalogo.db) y de piezas creadas por usuarios (piezas_creadas.db)'''
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



 
def db_insert_or_update_pieza(pieza_data, parametros_data, trapecios_data):
    '''
        Funcion usada por btn guardar pieza temporal a base de datos. En caso de ser una pieza nueva hace INSERT.
        en caso de ya existir y se este haciedo una modificacion, hace UPDATE
    '''
    conn = sqlite3.connect('piezas_creadas.db')
    cursor = conn.cursor()

    familia, modelo = pieza_data

    # Check if the pieza already exists
    cursor.execute("SELECT id FROM piezas WHERE familia = ? AND modelo = ?", (familia, modelo))
    row = cursor.fetchone()

    if row:
        pieza_id = row[0]
        print(f"Updating existing pieza: {familia} - {modelo}")
    else:
        cursor.execute("INSERT INTO piezas (familia, modelo) VALUES (?, ?)", (familia, modelo))
        pieza_id = cursor.lastrowid
        print(f"Inserted new pieza: {familia} - {modelo}")

    # Insert or update parametros
    for seccion in parametros_data:
        cursor.execute("INSERT OR IGNORE INTO parametros (tipo_seccion, trapecios, pieza_id) VALUES (?, ?, ?)", (seccion, len([t for t in trapecios_data if t[0] == seccion]), pieza_id))

    # Insert or update trapecios
    for trapecio in trapecios_data:
        seccion, posicion, base_inferior, base_superior, altura = trapecio
        cursor.execute("""
            INSERT OR REPLACE INTO trapecios (tipo_seccion, posicion, base_inf, base_sup, altura, pieza_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (seccion, posicion, base_inferior, base_superior, altura, pieza_id))

    conn.commit()
    conn.close()


''' Con id de pieza (que se obtiene anteriormente usando valores de comboBoxes Familia + Modelo) y es_creada (para saber a cual base de datos consultar)
    se obtienen todas las secciones y todos los trapecios dentro de esas secciones para una pieza.
    Este resultado luego se carga a una variable que guarda dinamicamente la inforamcion de una pieza mientras esta en uso.
'''
def db_get_all_trapecios_data(pieza_id, es_creada):
    if es_creada == False:
        conn = sqlite3.connect("catalogo.db")
    else:
        conn = sqlite3.connect("piezas_creadas.db")
    cursor = conn.cursor()

    cursor = conn.cursor()

    print(f"en db_get_all_trapecio_data() ---> value pieza_id: {pieza_id} ,,, value es_creada: {es_creada}")
    print("\n")

    try:
        # Obtener todas las secciones de la pieza
        cursor.execute("SELECT DISTINCT tipo_seccion FROM trapecios WHERE pieza_id = ?", (pieza_id[0],))
        secciones = [row[0] for row in cursor.fetchall()]

        # Crear un diccionario para organizar los datos por sección
        datos_por_seccion = {}
        for seccion in secciones:
            cursor.execute("""
                SELECT posicion, base_inf, base_sup, altura 
                FROM trapecios 
                WHERE pieza_id = ? AND tipo_seccion = ?
            """, (pieza_id[0], seccion))
            datos_por_seccion[seccion] = cursor.fetchall()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        datos_por_seccion = {}

    finally:
        conn.close()

    # print(" db_get_all_trapecios_data() ------> Valor de datos_por_seccion: ", datos_por_seccion, "\n")
    return datos_por_seccion