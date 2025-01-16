import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from ui_files.herramienta_trapecios_v7 import Ui_Dialog  # Import from the ui_files directory
from fn_database import *
from fn_calculo_propiedades import *
from fn_update_gui import *
from fn_elementos_gui import *
from fn_crear_pieza import open_crear_pieza_dialog


# QVLayout: layout_nuevas_row  -> Se le agregan Layouts dinamicos (manual y selec de catalogo)
# historial_agregados          -> Contador de tuplas que se agregaron dinamicamente a QVlayout
# family_model_mapping_(catalogo or usuario)        -> Diccionario que mapea cada familia de piezas con sus respectivos modelos
# db_es_catalogo -> guarda que tipo de catalogo se esta usando (True -> catalogo, False -> usuario)

class MyDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()          # Crea instancia de clase UI
        self.ui.setupUi(self)         # Aplica UI a Dialog (ventana)
        self.dynamic_layouts = []    # Inicia variable para guardar layouts dinamicos
        self.historial_agregados = 0
        self.es_creada = False # identifica que boton se usa para poblar ComboBoxes de familia/modelo, y luego a cual db hacer query
        self.es_temporal = False # Se usa para saber si la pieza actual esta en base de datos o no (Maneja accion btn_acpt_tipo_seccion)
        self.valores_creacion = [] # Almacena valores ingresados por usuario en ventana de creacion de pieza
        
        # Initialize storage for dynamic layout data
        self.dynamic_layout_data = {}

        ''' >>>> Inicia variables y conexiones de elementos fijos <<<< '''

        # Carga datos de familias/modelos de DB
        self.family_model_mapping_catalogo = db_cargar_familias_modelos(True) # Usa DB CATALOGO
        self.family_model_mapping_usuario = db_cargar_familias_modelos(False) # Usa DB PIEZAS_CREADAS


        # Conecta btn genera layouts dinamicos
        self.ui.btn_acpt_agregar.clicked.connect(lambda: generate_layout(self))

        # conecta btn Elimina layouts dinamicos
        self.ui.btn_acpt_eliminar.clicked.connect(
            lambda: confirmar_borrar(self, self.ui.spin_cant_eliminar.value())
        )

        # conecta btn calcular propiedades de campos LineEdits
        self.ui.btn_calcular_nuevos_valores.clicked.connect(lambda: calcular_nuevos_valores(self))

        # conecta btn para usar nueva pieza CATALOGO
        self.ui.btn_usar_pieza_catalogo.clicked.connect(lambda: poblar_combo_familia(self, True)) # Combo familia w/ Catalogo

        # Invoca ventana para CREAR NUEVA PIEZA
        self.ui.btn_crear_pieza_temp.clicked.connect(lambda: handle_crear_pieza(self)) # CREAR
        
        # conecta btn para poblar combo familia con piezas DB catalogo
        self.ui.btn_usar_pieza_catalogo.clicked.connect(lambda: poblar_combo_familia(self, True)) # Combo familia w/ Catalogo

        # conecta btn para poblar combo familia con piezas de DB creada por usuario
        ''' TODO cambiar lambda a fn de catalogo creado '''
        self.ui.btn_usar_pieza_usuario.clicked.connect(lambda: poblar_combo_familia(self, False)) # Combo familia w/ piezas Creadas_usuario

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        self.ui.combo_familia.currentIndexChanged.connect(lambda: update_combo_modelo(self, self.db_es_catalogo)) # Combo Modelos

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        # self.ui.combo_modelo.currentIndexChanged.connect(lambda: update_combo_secciones(self)) # Combo Secciones
        self.ui.combo_modelo.currentIndexChanged.connect(lambda: update_list_secciones(self)) # Lista Secciones

        # Cambia tipo de seccion en layouts dinamicos
        self.ui.btn_acpt_tipo_seccion.clicked.connect(lambda: self.aplicar_pieza(self.es_temporal)) # Aplica pieza/seccion

        # Conectar botones a sus métodos
        # self.ui.btn_acpt_tipo_seccion.clicked.connect(self.load_section_data)  # Cargar datos de sección
        self.ui.btn_save_seccion.clicked.connect(self.save_section_data)       # Guardar datos de sección


    def aplicar_pieza(self, es_temporal):
        if es_temporal == False:
            aplicar_pieza_catalogo(self)
        else:
            # self.aplicar_pieza_temporal()
            self.load_section_data()

    def aplicar_pieza_temporal(self):
        print("DEBUG app_pie_temp -> Se aplica seccion pieza temporal")

        # Retrieve the selected family, model, and section
        familia = self.ui.combo_familia.currentText()
        modelo = self.ui.combo_modelo.currentText()
        pieza_seccion_item = self.ui.list_tipo_seccion.currentItem()  # variable tipo obj/mem

        # Ensure there is a selection in the list widget
        if not familia or not modelo or not pieza_seccion_item:
            print("Debug: No family, model, or section selected.")
            return

        pieza_seccion = pieza_seccion_item.text()  # obtiene sección de lista
        print(f"DEBUG ap_pie_temp() --> contenido pieza_seccion_item: {pieza_seccion_item}, contenido pieza_seccion: {pieza_seccion}")

        # Retrieve the number of sections
        cantidad_secciones = self.ui.list_tipo_seccion.count()
        cantidad_trapecios = len(self.dynamic_layouts)
        print(f"DEBUG ap_pie_temp() -> cantidad secciones: {cantidad_secciones} ... cantidad_trapecios: {cantidad_trapecios}")

        # Store data from the current dynamic layouts before switching sections
        self.store_dynamic_layout_data(pieza_seccion)

        # Repopulate the dynamic layouts with the data for the selected section
        self.repopulate_dynamic_layouts(pieza_seccion, cantidad_secciones, cantidad_trapecios)


    def store_dynamic_layout_data(self, pieza_seccion):
        ''' Stores the data from the current dynamic layouts '''
        if not hasattr(self, "dynamic_layout_data"):  # Initialize the storage dictionary if it doesn't exist
            self.dynamic_layout_data = {}

        # print("DEBUG store_d_l() -->\t\t valor actual de self.dynamic_layouts: ", self.dynamic_layouts)
        # Collect data for the current section
        current_section_data = []
        i = 0 # TODO Eliminar i
        for layout in self.dynamic_layouts:
            print("*** *** STORE Dyn Lay *** *** ", i)
            i += 1
            data = {
                "bi_line": layout["bi_line"].text(),
                "bs_line": layout["bs_line"].text(),
                "altura_line": layout["altura_line"].text()
            }
            current_section_data.append(data)

        # Store the data associated with the current section
        self.dynamic_layout_data[pieza_seccion] = current_section_data
        # print(f"DEBUG store_dynamic_layout_data -> Stored data for section '{pieza_seccion}': {self.dynamic_layout_data[pieza_seccion]}")


    def repopulate_dynamic_layouts(self, pieza_seccion, cantidad_secciones, cantidad_trapecios):
        ''' Repopulates the dynamic layouts with stored data for the selected section '''
        # Clear the current layouts and adjust for the selected section
        ajustar_layouts_dinamicos(self, cantidad_trapecios)

        # Retrieve data for the selected section
        if pieza_seccion in self.dynamic_layout_data:
            section_data = self.dynamic_layout_data[pieza_seccion]
        else:
            section_data = []  # If no data exists for the section, use an empty list

        # print("DEBUG repopulate_d_l() -->\t\t valor actual de self.dynamic_layouts: ", self.dynamic_layouts)
        # Populate the dynamic layouts with the corresponding data
        # for i, layout in enumerate(self.dynamic_layouts):
        for i, layout in range(cantidad_trapecios):
            print("*** *** REPOPULATE Dyn Lay *** *** ", i)
            if i < len(section_data):
                data = section_data[i]
                layout["bi_line"].setText(data["bi_line"])
                layout["bs_line"].setText(data["bs_line"])
                layout["altura_line"].setText(data["altura_line"])
            else:
                # Clear the fields if no data exists for this index
                layout["bi_line"].setText("")
                layout["bs_line"].setText("")
                layout["altura_line"].setText("")

        # print(f"DEBUG repopulate_dynamic_layouts -> Loaded data for section '{pieza_seccion}': {section_data}")
        
    def save_section_data(self):
        """
        Save the current dynamic layout data associated with the selected section.
        """
        pieza_seccion_item = self.ui.list_tipo_seccion.currentItem()
        if not pieza_seccion_item:
            print("Debug: No section selected to save.")
            return

        pieza_seccion = pieza_seccion_item.text()
        current_section_data = []

        # Collect data from the dynamic layouts
        # TODO Eliminar i
        i = 0
        for layout in self.dynamic_layouts:
            print("*** *** SAVE SECTION *** *** ", i)
            i += 1
            data = {
                "bi_line": layout["bi_line"].text(),
                "bs_line": layout["bs_line"].text(),
                "altura_line": layout["altura_line"].text()
            }
            current_section_data.append(data)

        # Store the data under the selected section name
        self.dynamic_layout_data[pieza_seccion] = current_section_data
        # print(f"DEBUG save_section_data -> Saved data for section '{pieza_seccion}': {self.dynamic_layout_data[pieza_seccion]}")

    def load_section_data(self):
        """
        Load the dynamic layout data associated with the selected section.
        """
        pieza_seccion_item = self.ui.list_tipo_seccion.currentItem()
        if not pieza_seccion_item:
            print("Debug: No section selected to load.")
            return

        pieza_seccion = pieza_seccion_item.text()

        # Retrieve the data for the selected section
        section_data = self.dynamic_layout_data.get(pieza_seccion, [])
        cantidad_trapecios_seccion = len(section_data)  # The number of rows in the selected section

        print(f"DEBUG: Selected section '{pieza_seccion}' has {cantidad_trapecios_seccion} trapecios.")

        # Adjust the dynamic layouts to match the number of trapecios in the selected section
        ajustar_layouts_dinamicos(self, cantidad_trapecios_seccion)

        # Populate the dynamic layouts with the data for the selected section
        for i in range(cantidad_trapecios_seccion):
            if i < len(self.dynamic_layouts):  # Ensure we don’t access out-of-range layouts
                layout = self.dynamic_layouts[i]
                if i < len(section_data):  # Populate with stored data if available
                    data = section_data[i]
                    layout["bi_line"].setText(data.get("bi_line", ""))
                    layout["bs_line"].setText(data.get("bs_line", ""))
                    layout["altura_line"].setText(data.get("altura_line", ""))
                else:  # Clear the layout fields if no data is available
                    layout["bi_line"].setText("")
                    layout["bs_line"].setText("")
                    layout["altura_line"].setText("")

if __name__ == "__main__":
    ''' Inicia base de datos catalogo solo en caso de que no exista '''
    db_iniciar_database("catalogo.db")
    db_iniciar_database("piezas_creadas.db")

    print_familias_modelos() # Debug muestra todo el catalogo y piezas_creadas

    # Example of a pieza with dynamic sections and trapezoids
    pieza_data = ("test-familia1", "test-modelo1")  # This comes from your GUI
    parametros_data = [
        (1, 4),  # First section has 2 trapezoids
        # (2, 3),  # Second section has 3 trapezoids
        # Add more sections dynamically based on GUI inputs
    ]
    trapecios_data = [
        # First section's trapezoids
        (1, 1, 11, 22, 33),  # tipo_seccion, posicion, base_inf, base_sup, altura
        (1, 2, 44, 55, 66),  # tipo_seccion, posicion, base_inf, base_sup, altura
        (1, 3, 1111, 2222, 3333),
        (1, 4, 11, 22, 33)
        # Second section's trapezoids
        # (2, 1, 0.400, 0.400, 0.100),
        # (2, 2, 0.400, 0.300, 0.200),
        # (2, 3, 0.300, 0.300, 0.150),
        # Add more trapezoids dynamically based on GUI inputs
    ]

    # Call the function to insert data
    # insert_pieza_dynamically(pieza_data, parametros_data, trapecios_data)

    insert_or_update_pieza(pieza_data, parametros_data, trapecios_data)


    app = QApplication(sys.argv)   # Crear aplicacion
    dialog = MyDialog()            # Crear ventana Dialog
    dialog.show()                  # Mostrar Dialog
    sys.exit(app.exec())           # Inicia loop de eventos app
