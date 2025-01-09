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


''' print todas las familias y sus respectivos modelos de forma estructurada'''
def print_familias_modelos():
    dict_fam_mod = cargar_familias_modelos_db()

    for familias, modelos in dict_fam_mod.items():
        print(f"Family: {familias}")
        print("Models:")
        for model in modelos:
            print(f"  - {model}")
        print()
