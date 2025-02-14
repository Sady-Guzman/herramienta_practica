import sqlite3
import os
import sys
import shutil

# Define PATH a carpeta para bases de datos
# DB_DIR = os.path.join(os.path.dirname(__file__), "databases") # Version que usa app interpretada. get_db_path se adapta a interpretado / empaquetado


# def get_db_path(db_filename):
#     """
#     Devuelve la ruta correcta de la base de datos, asegurando compatibilidad con PyInstaller.
#     """
#     if getattr(sys, 'frozen', False):  # Si está empaquetado con PyInstaller
#         base_path = sys._MEIPASS  # Carpeta temporal de PyInstaller
#     else:
#         base_path = os.path.dirname(os.path.abspath(__file__))  # Directorio en ejecución normal

#     db_dir = os.path.join(base_path, "databases")

#     # Asegurar que el directorio de la base de datos existe
#     if not os.path.exists(db_dir):
#         os.makedirs(db_dir, exist_ok=True)

#     return os.path.join(db_dir, db_filename)

def copy_database_files():
    # If not packed, use the local _internal folder
    if getattr(sys, 'frozen', False):
        # source_dir = os.path.join(os.path.dirname(sys.executable), '_internal', 'databases')
        source_dir = os.path.join(os.path.dirname(sys.executable), 'databases')
    else:
        # source_dir = os.path.join(os.path.dirname(__file__), '_internal', 'databases')
        source_dir = os.path.join(os.path.dirname(__file__), 'databases')
        # return

    target_dir = os.path.expanduser('~/.myapp/databases')

    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # db_path = get_db_path('catalogo.db')
    # abs_db_path = os.path.abspath(db_path)  # Get absolute path
    # print(f"Using database at: {abs_db_path}")

    # Ensure the source directory exists
    if os.path.exists(source_dir):
        # List the files in the source directory
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            target_file = os.path.join(target_dir, filename)

            # Only copy the file if it doesn't exist in the target or if it's different
            if not os.path.exists(target_file) or os.path.getmtime(source_file) > os.path.getmtime(target_file):
                shutil.copy2(source_file, target_file)
                print(f"Copied {filename} to {target_dir}")
    else:
        print(f"Source directory {source_dir} does not exist.")


def get_db_path(db_filename):
    """
    Devuelve la ruta correcta de la base de datos y la almacena en un directorio persistente.
    """
    if getattr(sys, 'frozen', False):  # Si está empaquetado con PyInstaller
        base_path = os.path.expanduser("~/.myapp")  # Carpeta persistente en el home del usuario
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    db_dir = os.path.join(base_path, "databases")

    # Asegurar que el directorio existe
    if not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)

    return os.path.join(db_dir, db_filename)


''' En caso de no existir archivos tipo db 'catalogo.db' ni 'piezas_credas.db' Se crean y asigna schema'''
# def db_iniciar_database(db_path):
#     """
#     Inicializa la base de datos creando las tablas requeridas si no existen.

#     Args:
#         db_path (str): Nombre del archivo de base de datos (ej., 'catalogo.db').
#     """

#     db_path_con_dir = get_db_path(db_path)
#     connection = sqlite3.connect(db_path_con_dir)
#     cursor = connection.cursor()

#     def table_exists(table_name):
#         cursor.execute("""
#             SELECT name FROM sqlite_master WHERE type='table' AND name=?
#         """, (table_name,))
#         return cursor.fetchone() is not None

#     try:
#         if not table_exists("piezas"):
#             cursor.execute("""
#                 CREATE TABLE piezas (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     familia TEXT NOT NULL,
#                     modelo TEXT NOT NULL UNIQUE
#                 )
#             """)
#             print(f"init_db {db_path} > Tabla 'piezas' creada.")
#         else:
#             print(f"init_db {db_path} > La relacion 'piezas' ya existe. No se realizaron cambios.")

#         if not table_exists("parametros"):
#             cursor.execute("""
#                 CREATE TABLE parametros (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     tipo_seccion INTEGER NOT NULL,
#                     trapecios INTEGER NOT NULL,
#                     pieza_id INTEGER NOT NULL, 
#                     FOREIGN KEY (pieza_id) REFERENCES piezas (id)
#                 )
#             """)
#             print(f"init_db {db_path} > Tabla 'parametros' creada")
#         else:
#             print(f"init_db {db_path} > La relacion 'parametros' ya existe. No se realizaron cambios.")

#         if not table_exists("trapecios"):
#             cursor.execute("""
#                 CREATE TABLE trapecios (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     tipo_seccion TEXT NOT NULL,
#                     posicion INTEGER NOT NULL,
#                     base_inf REAL NOT NULL,
#                     base_sup REAL NOT NULL,
#                     altura REAL NOT NULL,
#                     pieza_id INTEGER NOT NULL,
#                     FOREIGN KEY (pieza_id) REFERENCES piezas (id)
#                 )
#             """)
#             print(f"init_db {db_path} > Tabla 'trapecios' creada.")
#         else:
#             print(f"init_db {db_path} > La relacion 'trapecios' ya existe. No se realizaron cambios.")

#     except sqlite3.Error as e:
#         print(f"DEBUG error al inicializar DB '{db_path}': {e}")
#     finally:
#         connection.close()

#     return

''' ======================================================================================== '''
''' ======================================================================================== '''
''' ======================================================================================== '''


def db_cargar_familias_modelos(self, tipo_db):
    """
        Conecta la base de datos y recupera tuplas para poblar combo_familia y combo_modelo.
        Retorna un diccionario donde cada familia mapea a una lista de modelos.

        tipo_db: True -> Usa base datos catalogo.db, donde estan las piezas migradas de Jacena
                        False -> Usa base datos creada por usuario (piezas_creadas.db)
    """

    if tipo_db == True:
        # db_path = os.path.join(DB_DIR, "catalogo.db")
        db_path = get_db_path("catalogo.db")
    else:
        # db_path = 'piezas_creadas.db'
        # db_path = os.path.join(DB_DIR, "piezas_creadas.db")
        db_path = get_db_path("piezas_creadas.db")
    
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
        # db_path = 'catalogo.db' 
        # db_path = os.path.join(DB_DIR, "catalogo.db")
        db_path = get_db_path("catalogo.db")
    else:
        # db_path = 'piezas_creadas.db'
        # db_path = os.path.join(DB_DIR, "piezas_creadas.db")
        db_path = get_db_path("piezas_creadas.db")
    
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
        # conn = sqlite3.connect("catalogo.db")
        # db_path = os.path.join(DB_DIR, "catalogo.db")
        db_path = get_db_path("catalogo.db")
    else:
        # conn = sqlite3.connect("piezas_creadas.db")
        # db_path = os.path.join(DB_DIR, "piezas_creadas.db")
        db_path = get_db_path("piezas_creadas.db")

    conn = sqlite3.connect(db_path)
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
        # conn = sqlite3.connect("catalogo.db")
        # db_path = os.path.join(DB_DIR, "catalogo.db")
        db_path = get_db_path("catalogo.db")
    else:
        # conn = sqlite3.connect("piezas_creadas.db")
        # db_path = os.path.join(DB_DIR, "piezas_creadas.db")
        db_path = get_db_path("piezas_creadas.db")

    conn = sqlite3.connect(db_path)
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
        # db_path = os.path.join(DB_DIR, "catalogo.db")
        db_path = get_db_path("catalogo.db")
    else:
        # conn = sqlite3.connect("piezas_creadas.db")
        # db_path = os.path.join(DB_DIR, "piezas_creadas.db")
        db_path = get_db_path("piezas_creadas.db")

    conn = sqlite3.connect(db_path)
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


# ''' ==========================================================================================================================='''
# ''' Funciones para iniciar estructura (esquema / schema) de bases de datos catalogo.db y piezas_creadas.db 
#     -- Solo ejecuta rutinas si las bases de datos no estan iniciadas, Por lo tanto solo se usa cuando se inicia el software por primera vez'''
# ''' INIT para basde de datos de piezas migradas de JACENA (catalogo.db) y de piezas creadas por usuarios (piezas_creadas.db)'''
# def db_iniciar_database(db_path):
#     """
#     Inicializa la base de datos creando las tablas requeridas si no existen.

#     Args:
#         db_path (str): Path al archivo base de datos (ej., 'catalogo.db').
#     """
    
#     db_path_con_dir = os.path.join(DB_DIR, db_path)    
#     connection = sqlite3.connect(db_path_con_dir)
#     cursor = connection.cursor()

#     # Revisa si existe la relacion
#     def table_exists(table_name):
#         cursor.execute("""
#             SELECT name FROM sqlite_master WHERE type='table' AND name=?
#         """, (table_name,))
#         return cursor.fetchone() is not None

#     try:
#         # REVISAR RELACION PIEZAS
#         if not table_exists("piezas"):
#             cursor.execute("""
#                 CREATE TABLE piezas (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     familia TEXT NOT NULL,
#                     modelo TEXT NOT NULL UNIQUE
#                 )
#             """)
#             print(f"init_db {db_path} > Tabla 'piezas' creada.")
#         else:
#             print(f"init_db {db_path} > La relacion 'piezas' ya existe. No se realizaron cambios.")

#         # REVISAR RELACION PARAMETROS
#         if not table_exists("parametros"):
#             cursor.execute("""
#                 CREATE TABLE parametros (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     tipo_seccion INTEGER NOT NULL,
#                     trapecios INTEGER NOT NULL,
#                     pieza_id INTEGER NOT NULL, 
#                     FOREIGN KEY (pieza_id) REFERENCES piezas (id)
#                 )
#             """)
#             print(f"init_db {db_path} > Tabla 'parametros' creada")
#         else:
#             print(f"init_db {db_path} > La relacion 'parametros' ya existe. No se realizaron cambios.")

#         # REVISAR RELACION TRAPECIOS
#         if not table_exists("trapecios"):
#             cursor.execute("""
#                 CREATE TABLE trapecios (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     tipo_seccion TEXT NOT NULL,
#                     posicion INTEGER NOT NULL,
#                     base_inf REAL NOT NULL,
#                     base_sup REAL NOT NULL,
#                     altura REAL NOT NULL,
#                     pieza_id INTEGER NOT NULL,
#                     FOREIGN KEY (pieza_id) REFERENCES piezas (id)
#                 )
#             """)
#             print(f"init_db {db_path} > Tabla 'trapecios' creada.")
#         else:
#             print(f"init_db {db_path} > La relacion 'trapecios' ya existe. No se realizaron cambios.")

#     except sqlite3.Error as e:
#         print(f"DEBUG error al inicializar DB '{db_path}': {e}")
#     finally:
#         connection.close()

#     return


# ''' Para version distributable de programa creada con Pyinstaller '''
# def get_db_path(db_filename):
#     """
#     Devuelve la ruta absoluta correcta para la base de datos,
#     asegurando compatibilidad con PyInstaller (--onefile y --onedir).
#     """
#     if getattr(sys, 'frozen', False):  # Si está empaquetado con PyInstaller
#         base_path = sys._MEIPASS  # Directorio temporal donde PyInstaller extrae archivos
#     else:
#         base_path = os.path.dirname(os.path.abspath(__file__))  # Ruta normal en desarrollo

#     return os.path.join(base_path, db_filename)


 
def db_insert_or_update_pieza(pieza_data, parametros_data, trapecios_data):
    '''
        Funcion usada por btn guardar pieza temporal a base de datos. En caso de ser una pieza nueva hace INSERT.
        en caso de ya existir y se este haciedo una modificacion, hace UPDATE
    '''
    
    # db_path = os.path.join(DB_DIR, "piezas_creadas.db")
    db_path = get_db_path("piezas_creadas.db")
    conn = sqlite3.connect(db_path)
    # conn = sqlite3.connect('piezas_creadas.db')
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
        # db_path = os.path.join(DB_DIR, "catalogo.db")
        db_path = get_db_path("catalogo.db")
    else:
        # db_path = os.path.join(DB_DIR, "piezas_creadas.db")
        db_path = get_db_path("piezas_creadas.db")

    conn = sqlite3.connect(db_path)
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

''' ========================================= consulta para TAB2 Armdura Activa ================================================='''

def db_recuperar_diametros_cordones():
    ''' Retorna la cantidad de tuplas que hay en tabla propiedades_armadura_activa en armaduras.db '''
    
    # db_path = os.path.join(DB_DIR, "armaduras.db")
    db_path = get_db_path("armaduras.db")
    conn = sqlite3.connect(db_path)
    # conn = sqlite3.connect("armaduras.db")
    cursor = conn.cursor()

    try:
        # Obtener todas las secciones de la pieza
        cursor.execute("SELECT DISTINCT diametro FROM propiedades_armadura_activa")
        diametros = [row[0] for row in cursor.fetchall()]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        diametros = []

    finally:
        conn.close()

    # print("db_recuperar_diametros_cordones() -> contenido de consulta: ", diametros, "\n")
    return diametros


def db_area_cordon(diametro):

    # db_path = os.path.join(DB_DIR, "armaduras.db")
    db_path = get_db_path("armaduras.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Obtener todas las secciones de la pieza
        cursor.execute("SELECT area FROM propiedades_armadura_activa WHERE diametro = ?", (diametro,))
        area = cursor.fetchone()
        area = area[0]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        area = 0

    finally:
        conn.close()

    # print("db_area_de_cordon() -> contenido de consulta: ", area, "\n")
    return area


''' Consulta cotas existente en testero seleccionado en ComboBox '''
def db_cotas_testero(testero):
    # db_path = os.path.join(DB_DIR, "armaduras.db")
    db_path = get_db_path("armaduras.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Use a parameterized query to avoid SQL syntax issues
        query = "SELECT cota FROM testeros WHERE testero = ?"
        cursor.execute(query, (testero,))  # Pass testero as a parameter
        cotas = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        cotas = 0
    finally:
        conn.close()

    # print(f"db_cotas_testero() -> contenido de consulta: {cotas} \n")
    return cotas

''' fetch los testeros distintos en tabla testeros '''
def db_testeros_existentes():
    # db_path = os.path.join(DB_DIR, "armaduras.db")
    db_path = get_db_path("armaduras.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        query = "SELECT DISTINCT testero FROM testeros"
        cursor.execute(query)
        testeros = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        testeros = 0
    finally:
        conn.close()

    # print(f"db_cotas_testero() -> contenido de consulta: {testeros} \n")
    return testeros

import os
import sqlite3

''' DEBUG problema testeros en distributable '''
def db_testeros_existentes():
    db_path = get_db_path("armaduras.db")  # Ensure this resolves to the correct path
    abs_db_path = os.path.abspath(db_path)  # Get absolute path
    # print(f"🔍 Using database at: {abs_db_path}")

    if not os.path.exists(db_path):
        print("⚠️ ERROR: Database file does not exist at expected path!")
        return 0  # Prevent further errors

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        # print(f"📋 Tables in database: {tables}")  # Check if 'testeros' is missing

        query = "SELECT DISTINCT testero FROM testeros"
        cursor.execute(query)
        testeros = cursor.fetchall()
        # print(f"✅ Query Result: {testeros}")  # Show fetched rows

    except sqlite3.Error as e:
        # print(f"❌ Database error: {e}")
        testeros = 0
    finally:
        conn.close()

    return testeros

''' ================================================================================================================================================================= '''
''' ============================   Funciones para feature de presets de armadura activa (Tipos Cableados, T2, T4, T6)  ============================================== '''

def db_tipos_cableado_pieza(familia, modelo):
    ''' Obtiene los tipos de cableado que existen como Preset para una pieza '''

    # db_path = os.path.join(DB_DIR, "armaduras.db")
    db_path = get_db_path("armaduras.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # print(f"en db_tipos: Contenido de familia: {familia}, contenido de modelo: {modelo}")

    try:
        query = "SELECT DISTINCT tipo_cableado FROM cableado_tipos WHERE familia = ? AND modelo = ?"
        cursor.execute(query, (familia, modelo,))
        tipos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        tipos = 0
    finally:
        conn.close()

    print(f"db_tipos_cableados_pieza() -> contenido de consulta: {tipos} \n")
    return tipos

def db_id_tipo_cableado_pieza(familia, modelo, seleccion):
    " Usando familia, modelo, y seleccion en comboBox obtiene ID correspondiente a ese tipo de cableado para esa pieza "
    
    # db_path = os.path.join(DB_DIR, "armaduras.db")
    db_path = get_db_path("armaduras.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print(f"en db_tipos: Contenido de familia: {familia}, contenido de modelo: {modelo}, seleccion es: {seleccion}\n\n\n\n")

    try:
        query = "SELECT id FROM cableado_tipos WHERE familia = ? AND modelo = ? AND tipo_cableado = ?"
        cursor.execute(query, (familia, modelo, seleccion,))
        id_tipo = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        id_tipo = 0
    finally:
        conn.close()

    print(f"db_id_tipo_cableado_pieza() -> ID de tipo cableado seleccionado : {id_tipo} \n")
    return id_tipo




def db_cables_tipo_cableado(tipo_cableado, familia, modelo):
    ''' usa ID de tipo cableado obtenido de cableado_tipos y compara en col tipo_cableado de cableado_cables '''

    # db_path = os.path.join(DB_DIR, "armaduras.db")
    db_path = get_db_path("armaduras.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        query = """
        SELECT cota, diametro, num_cord, tpi 
        FROM cableado_cables 
        JOIN cableado_tipos ON cableado_cables.tipo_cableado = cableado_tipos.id
        WHERE cableado_tipos.tipo_cableado = ? AND familia = ? and modelo = ?;
        """
        cursor.execute(query, (tipo_cableado, familia, modelo))
        tipos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        tipos = 0
    finally:
        conn.close()

    # print(f"db_cables_tipo_cableado() -> contenido de consulta dentro de tuplas:")
    # for cota, diametro, num_cord, tpi in tipos:
    #     print(f"Cableado: cota={cota}, diametro={diametro}, num_cord={num_cord}, tpi={tpi}")

    return tipos


def db_cantidad_cotas_tipo_cableado(id_tipo_cableado):
    ''' Usa como parametro ID de cableado_tipos '''

    # db_path = os.path.join(DB_DIR, "armaduras.db")
    db_path = get_db_path("armaduras.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        query = """
        SELECT DISTINCT cota 
        FROM cableado_cables 
        JOIN cableado_tipos ON cableado_cables.tipo_cableado = cableado_tipos.id
        WHERE cableado_tipos.id = ?;
        """
        cursor.execute(query, (id_tipo_cableado,))
        cotas = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        cotas = 0
    finally:
        conn.close()

    print(f"db_cantidad_cotas_tipo_cableado() -> contenido de consulta: {cotas}")
    return cotas

def db_cantidad_cordones_tipo_cableado(id_tipo_cableado):
    ''' Usa como parametro ID de cableado_tipos '''

    # db_path = os.path.join(DB_DIR, "armaduras.db")
    db_path = get_db_path("armaduras.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        query = """
        SELECT COUNT(DISTINCT diametro)
        FROM cableado_cables 
        JOIN cableado_tipos ON cableado_cables.tipo_cableado = cableado_tipos.id
        WHERE cableado_tipos.id = ?;
        """
        cursor.execute(query, (id_tipo_cableado,))
        cotas = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        cotas = 0
    finally:
        conn.close()

    print(f"db_cantidad_cordones_tipo_cableado() -> contenido de consulta: {cotas}")
    return cotas

''' ======================================================================================================================== '''

def db_tipos_arm_pasiva():
    ''' retorna todaos los tipos de armaduras pasivas '''

    # db_path = os.path.join(DB_DIR, "armaduras.db")
    db_path = get_db_path("armaduras.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        query = """
        SELECT nombre_tipo FROM apasiva_tipos;
        """
        cursor.execute(query)
        tipos_armaduras_pasivas = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        tipos_armaduras_pasivas = 0
    finally:
        conn.close()

    print(f"db_tipos_arm_pasiva() -> contenido de consulta: {tipos_armaduras_pasivas}")
    return tipos_armaduras_pasivas

def db_materiales_arm_pasiva():
    ''' retorna todaos los tipos de armaduras pasivas '''

    # db_path = os.path.join(DB_DIR, "armaduras.db")
    db_path = get_db_path("armaduras.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        query = """
        SELECT nombre_material FROM apasiva_materiales;
        """
        cursor.execute(query)
        materiales_armaduras_pasivas = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        materiales_armaduras_pasivas = 0
    finally:
        conn.close()

    # print(f"db_materiales_arm_pasiva() -> contenido de consulta: {materiales_armaduras_pasivas}")
    return materiales_armaduras_pasivas


def db_usos_arm_pasiva():
    ''' retorna todos los usos de armaduras pasivas '''
    ''' Flexion, Cortante, Varios, Flexion Aleta, Cortante Aleta '''

    # db_path = os.path.join(DB_DIR, "armaduras.db")
    db_path = get_db_path("armaduras.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        query = """
        SELECT nombre_uso FROM apasiva_usos;
        """
        cursor.execute(query)
        usos_armaduras_pasivas = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        usos_armaduras_pasivas = 0
    finally:
        conn.close()

    # print(f"db_usos_arm_pasiva() -> contenido de consulta: {usos_armaduras_pasivas}")
    return usos_armaduras_pasivas


''' ============================================================================================================== '''
'''    QUERIES para DB materiales.db     '''


def db_tipos_hormigon():
    ''' Obtiene todos los tipos de hormigon que hay disponibles '''
    ''' Tabla tipos_hormigon de materiales.db'''
    # db_path = os.path.join(DB_DIR, "materiales.db")
    db_path = get_db_path("materiales.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        query = """
        SELECT * FROM tipos_hormigon;
        """
        cursor.execute(query)
        tipos_hormigon = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        tipos_hormigon = 0
    finally:
        conn.close()

    # print(f"db_tipos_hormigon() -> contenido de consulta: {tipos_hormigon}")
    return tipos_hormigon


def db_id_tipo_hormigon_nombre(nombre_hormigon):
    ''' Dado un nombre de un tipo de hormigon (str) se obtiene su id PK correspondiente '''
    ''' Resultado se usa para queries donde ID es PK en otra tabla '''
    # db_path = os.path.join(DB_DIR, "materiales.db")
    db_path = get_db_path("materiales.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        query = """
        SELECT id FROM tipos_hormigon WHERE nombre_tipo = ?;
        """
        cursor.execute(query, (nombre_hormigon,))
        id_hormigon = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        id_hormigon = 0
    finally:
        conn.close()

    # print(f"db_id_tipo_hormigon_nombre() -> contenido de consulta: {id_hormigon}")
    return id_hormigon



def db_resistencias_tipo_hormigon(tipo_hormigon):
    ''' Obtiene parametros de resistencias para un tipo de hormigon dado '''
    ''' tipo de hormigon es valor de id para un string de tipo de hormigon que se usa como PK en tipos_hormigon y FK en resistencias_hormigon '''
    # db_path = os.path.join(DB_DIR, "materiales.db")
    db_path = get_db_path("materiales.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        query = """
        SELECT * FROM resistencias_hormigon WHERE tipo_hormigon = ?;
        """
        cursor.execute(query, (tipo_hormigon,))
        resistencias_hormigon = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        resistencias_hormigon = 0
    finally:
        conn.close()

    # print(f"db_resistencias_tipo_hormigon() -> contenido de consulta: {resistencias_hormigon}")
    return resistencias_hormigon


def db_densidades_tipo_hormigon(tipo_hormigon):
    ''' Obtiene parametros de desidades HORMIGON/ACERO para un tipo de hormigon dado '''
    ''' tipo de hormigon es valor de id para un string de tipo de hormigon que se usa como PK en tipos_hormigon y FK en densidades '''
    # db_path = os.path.join(DB_DIR, "materiales.db")
    db_path = get_db_path("materiales.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        query = """
        SELECT * FROM densidades WHERE tipo_hormigon = ?;
        """
        cursor.execute(query, (tipo_hormigon,))
        densidades = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        densidades = 0
    finally:
        conn.close()

    # print(f"db_densidades_tipo_hormigon() -> contenido de consulta: {densidades}")
    return densidades

''' from fn_database import db_tipos_hormigon, db_id_tipo_hormigon_nombre, db_resistencias_tipo_hormigon, db_densidades_tipo_hormigon '''
