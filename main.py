import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from ui_files.herramienta_trapecios_v6 import Ui_Dialog  # Import from the ui_files directory
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
        self.db_es_catalogo = 0 # Se usa para saber con cual variable de mapping poblar ComboBox Modelos
        self.es_temporal = 0 # Se usa para saber si la pieza actual esta en base de datos o no (Maneja accion btn_acpt_tipo_seccion)
        self.valores_creacion = [] # Almacena valores ingresados por usuario en ventana de creacion de pieza

        ''' >>>> Inicia variables y conexiones de elementos fijos <<<< '''

        # Carga datos de familias/modelos de DB
        self.family_model_mapping_catalogo = db_cargar_familias_modelos(True)
        ''' ========================================= Cambiar por funcion de DB usuario =============================== '''
        # TODO Cambiar True ---> False 
        self.family_model_mapping_usuario = db_cargar_familias_modelos(True) 


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
        ''' cambiar lambda a fn de catalogo creado '''
        self.ui.btn_usar_pieza_usuario.clicked.connect(lambda: poblar_combo_familia(self, False)) # Combo familia w/ piezas Creadas_usuario

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        self.ui.combo_familia.currentIndexChanged.connect(lambda: update_combo_modelo(self, self.db_es_catalogo)) # Combo Modelos

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        # self.ui.combo_modelo.currentIndexChanged.connect(lambda: update_combo_secciones(self)) # Combo Secciones
        self.ui.combo_modelo.currentIndexChanged.connect(lambda: update_list_secciones(self)) # Lista Secciones

        # Cambia tipo de seccion en layouts dinamicos
        self.ui.btn_acpt_tipo_seccion.clicked.connect(lambda: self.aplicar_pieza(self.es_temporal)) # Aplica pieza/seccion

    def aplicar_pieza(self, es_temporal):
        if es_temporal == False:
            aplicar_pieza_catalogo(self)
        else:
            self.aplicar_pieza_temporal()

    def aplicar_pieza_temporal(self):
        print("DEBUG app_pie_temp -> Se aplica seccion pieza temporal")

        # Store data from current dynamic layouts before switching sections
        self.store_dynamic_layout_data()

        # Retrieve the selected family and model
        familia = self.ui.combo_familia.currentText()
        modelo = self.ui.combo_modelo.currentText()

        # Ensure there is a selection in the list widget
        if not familia or not modelo:
            print("Debug: No family or model selected.")
            return

        # Retrieve the number of sections
        cantidad_secciones = len(self.dynamic_layouts)

        # Repopulate the dynamic layouts with stored data
        self.repopulate_dynamic_layouts(cantidad_secciones)

    def store_dynamic_layout_data(self):
        ''' Stores the data from the current dynamic layouts '''
        self.dynamic_layout_data = []
        for layout in self.dynamic_layouts:
            data = {
                "bi_line": layout["bi_line"].text(),
                "bs_line": layout["bs_line"].text(),
                "altura_line": layout["altura_line"].text(),
                "area_line": layout["area_line"].text(),
                "cg_line": layout["cg_line"].text(),
                "inercia_line": layout["inercia_line"].text(),
                "op_line": layout["op_line"].text(),
            }
            self.dynamic_layout_data.append(data)

    def repopulate_dynamic_layouts(self, cantidad_secciones):
        ''' Repopulates the dynamic layouts with stored data '''
        ajustar_layouts_dinamicos(self, cantidad_secciones)
        for i, layout in enumerate(self.dynamic_layouts):
            if i < len(self.dynamic_layout_data):
                data = self.dynamic_layout_data[i]
                layout["bi_line"].setText(data["bi_line"])
                layout["bs_line"].setText(data["bs_line"])
                layout["altura_line"].setText(data["altura_line"])
                layout["area_line"].setText(data["area_line"])
                layout["cg_line"].setText(data["cg_line"])
                layout["inercia_line"].setText(data["inercia_line"])
                layout["op_line"].setText(data["op_line"])


if __name__ == "__main__":
    ''' Inicia base de datos catalogo solo en caso de que no exista '''
    db_iniciar_database("catalogo.db")
    db_iniciar_database("piezas_creadas.db")

    print_familias_modelos() # Debug muestra todo el catalogo y piezas_creadas

    app = QApplication(sys.argv)   # Crear aplicacion
    dialog = MyDialog()            # Crear ventana Dialog
    dialog.show()                  # Mostrar Dialog
    sys.exit(app.exec())           # Inicia loop de eventos app
