''' 
    Maneja funcionamiento de ventana para crear una nueva pieza temporal.

    La ventana crear_pieza se invoca al hacer click en 'btn_crear_pieza_temp' en la ventana principal.

    Cumple con la funcion de obtener del usuario:
        - Nombre Familia
        - Nombre Modelo
        - Cantidad de Secciones
        - Nombre de cada Seccion que se va a agregar.
    
    Luego de que usuario ingresa datos y hace click en 'aceptar', Se almacenan los datos para insertarlos a la Base de Datos
    piezas_creadas.db y la ventana se cierra
'''

from PySide6.QtWidgets import QDialog
from ui_files.ui_crear_pieza import Ui_Dialog

from fn_elementos_gui import *
from fn_update_gui import *



class CrearPiezaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_crear = Ui_Dialog()
        self.ui_crear.setupUi(self)

        # Connect the accept button to a handler function
        self.ui_crear.btn_aceptar.clicked.connect(self.handle_accept)

    def handle_accept(self):
        # Retrieve the data entered by the user
        familia = self.ui_crear.lineEdit_familia.text()
        modelo = self.ui_crear.lineEdit_modelo.text()
        cantidad_secciones = self.ui_crear.spin_cant_agregar.value()

        # Validate inputs
        if not familia or not modelo or cantidad_secciones <= 0:
            print("Please enter valid data for all fields.")
            return

        # Close the dialog after processing
        print(f"Familia: {familia}, Modelo: {modelo}, Cantidad de Secciones: {cantidad_secciones}")
        self.accept()


def open_crear_pieza_dialog(self):
        # Open the CrearPiezaDialog
        dialog_crear = CrearPiezaDialog(self)
        if dialog_crear.exec():  # Open dialog and wait for user action
            print("Dialog accepted!")
        else:
            print("Dialog canceled.")