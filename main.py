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
from fn_pieza_temporal import *


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
        self.es_catalogo = 0
        
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

        # conecta btn para poblar combo familia con piezas de DB creada por usuario
        self.ui.btn_usar_pieza_usuario.clicked.connect(lambda: poblar_combo_familia(self, False)) # Combo familia w/ piezas Creadas_usuario

        # Invoca ventana para CREAR NUEVA PIEZA
        self.ui.btn_crear_pieza_temp.clicked.connect(lambda: handle_crear_pieza(self)) # CREAR

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        self.ui.combo_familia.currentIndexChanged.connect(lambda: update_combo_modelo(self, self.db_es_catalogo)) # Combo Modelos

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        self.ui.combo_modelo.currentIndexChanged.connect(lambda: update_list_secciones(self, self.db_es_catalogo)) # Lista Secciones

        # Cambia tipo de seccion en layouts dinamicos
        self.ui.btn_acpt_tipo_seccion.clicked.connect(lambda: self.aplicar_pieza(self.es_temporal, self.es_creada)) # Aplica pieza/seccion

        # Conectar botones a sus métodos
        # self.ui.btn_acpt_tipo_seccion.clicked.connect(self.load_section_data)  # Cargar datos de sección
        self.ui.btn_save_seccion.clicked.connect(lambda: save_section_data(self))       # Guardar datos de sección

        # Conectar btn GUARDAR PIEZA A DB (piezas_creadas)
        self.ui.btn_save_pieza.clicked.connect(lambda: save_pieza_data(self, self.es_temporal)) # Guardar Pieza TEMP en DB




    def aplicar_pieza(self, es_temporal, es_creada):
        if es_temporal == False:
            aplicar_pieza_catalogo(self, es_creada)
        else:
            # self.aplicar_pieza_temporal()
            load_section_data(self)







    








if __name__ == "__main__":
    ''' Inicia base de datos catalogo solo en caso de que no exista '''
    db_iniciar_database("catalogo.db")
    db_iniciar_database("piezas_creadas.db")

    print_familias_modelos() # Debug muestra todo el catalogo y piezas_creadas


    app = QApplication(sys.argv)   # Crear aplicacion
    dialog = MyDialog()            # Crear ventana Dialog
    dialog.show()                  # Mostrar Dialog
    sys.exit(app.exec())           # Inicia loop de eventos app
