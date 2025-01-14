import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from ui_files.herramienta_trapecios_v6 import Ui_Dialog  # Import from the ui_files directory
from fn_database import *
from fn_calculo_propiedades import *
from fn_update_gui import *
from fn_elementos_gui import *


# QVLayout: layout_nuevas_row -> Se le agregan tuplas de valor de forma dinamica (manual y selec de catalogo)
# historial_agregados -> Contador de tuplas que se agregaron dinamicamente a QVlayout


class MyDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the dialog window
        self.dynamic_layouts = []  # Initialize dynamic layouts for row management
        self.historial_agregados = 0

        ''' >>>> Inicia variables y conexiones de elementos fijos <<<< '''

        # Carga datos de familias/modelos de DB
        self.family_model_mapping = db_cargar_familias_modelos()


        # Conecta btn genera layouts dinamicos
        self.ui.btn_acpt_agregar.clicked.connect(lambda: generate_layout(self))

        # conecta btn Elimina layouts dinamicos
        self.ui.btn_acpt_eliminar.clicked.connect(
            lambda: confirmar_borrar(self, self.ui.spin_cant_eliminar.value())
        )

        # conecta btn calcular propiedades de campos LineEdits
        self.ui.btn_calcular_nuevos_valores.clicked.connect(lambda: calcular_nuevos_valores(self))

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        self.ui.combo_familia.currentIndexChanged.connect(lambda: update_combo_modelo(self))

        # Conecta btn con funcion para usar una pieza de catalogo en calculo
        self.ui.btn_acpt_pieza.clicked.connect(lambda: aplicar_pieza_catalogo(self, 1))

        # agg btn para usar pieza temporal

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        self.ui.combo_modelo.currentIndexChanged.connect(lambda: update_combo_secciones(self))

        # Cambia tipo de seccion en layouts dinamicos
        self.ui.btn_acpt_tipo_seccion.clicked.connect(lambda: aplicar_pieza_catalogo(self, 0))

        ''' llena comboBoxes Familia/Modelo'''
        ''' Cambiar a funcion que se llama despues de hacer click en btn usar catalogo '''
        # Usa variable iniciada en def__init__()... Siempre esta 'Elegir' como placeholder
        self.ui.combo_familia.addItems(["Elegir"] + list(self.family_model_mapping.keys()))


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application
    dialog = MyDialog()            # Create the dialog window
    dialog.show()                  # Show the dialog window
    sys.exit(app.exec())           # Start the application's event loop
