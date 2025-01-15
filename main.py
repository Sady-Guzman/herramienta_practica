import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from ui_files.herramienta_trapecios_v6 import Ui_Dialog  # Import from the ui_files directory
from fn_database import *
from fn_calculo_propiedades import *
from fn_update_gui import *
from fn_elementos_gui import *


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
        self.db_es_catalogo = 0

        ''' >>>> Inicia variables y conexiones de elementos fijos <<<< '''

        # Carga datos de familias/modelos de DB
        self.family_model_mapping_catalogo = db_cargar_familias_modelos(True)
        ''' Cambiar por funcion de DB usuario '''
        self.family_model_mapping_usuario = db_cargar_familias_modelos(False) 


        # Conecta btn genera layouts dinamicos
        self.ui.btn_acpt_agregar.clicked.connect(lambda: generate_layout(self))

        # conecta btn Elimina layouts dinamicos
        self.ui.btn_acpt_eliminar.clicked.connect(
            lambda: confirmar_borrar(self, self.ui.spin_cant_eliminar.value())
        )

        # conecta btn calcular propiedades de campos LineEdits
        self.ui.btn_calcular_nuevos_valores.clicked.connect(lambda: calcular_nuevos_valores(self))

        
        # conecta btn para poblar combo familia con piezas DB catalogo
        self.ui.btn_usar_pieza_catalogo.clicked.connect(lambda: poblar_combo_familia(self, True)) # Combo familia w/ Catalogo

        # conecta btn para poblar combo familia con piezas de DB creada por usuario
        ''' cambiar lambda a fn de catalogo creado '''
        self.ui.btn_usar_pieza_usuario.clicked.connect(lambda: poblar_combo_familia(self, False)) # Combo familia w/ piezas Creadas_usuario

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        self.ui.combo_familia.currentIndexChanged.connect(lambda: update_combo_modelo(self, self.db_es_catalogo)) # Combo Modelos

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        self.ui.combo_modelo.currentIndexChanged.connect(lambda: update_combo_secciones(self)) # Combo Secciones

        # Cambia tipo de seccion en layouts dinamicos
        self.ui.btn_acpt_tipo_seccion.clicked.connect(lambda: aplicar_pieza_catalogo(self))


if __name__ == "__main__":
    ''' Inicia base de datos catalogo solo en caso de que no exista '''
    # db_iniciar_catalogo()
    print_familias_modelos("catalogo.db") # Debug muestra todo el catalogo y piezas_creadas
    print_familias_modelos("piezas_creadas.db") # Debug muestra todo el catalogo y piezas_creadas
    app = QApplication(sys.argv)   # Crear aplicacion
    dialog = MyDialog()            # Crear ventana Dialog
    dialog.show()                  # Mostrar Dialog
    sys.exit(app.exec())           # Inicia loop de eventos app
