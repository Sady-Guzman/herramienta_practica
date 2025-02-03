''' 
    Maneja funcionamiento de ventana para seleccionar cotas a agregar en TAB2 (Armadura Activa).
    Lista de cotas depende de Testero seleccionado en ese momento en ComboBox

    La ventana crear_pieza se invoca al hacer click en btn para cargar cotas de testero (En vez de custom, osea sin cota pre-definida) en la ventana principal-TAB2.

    obtiene las cotas mostradas de query a base de datos.
    
    Luego de que el usuario elige las cotas y usa btn aceptar, Los checkboxes marcados se pasan a funcion que invoca esta clase
'''

from PySide6.QtWidgets import QDialog, QCheckBox  # Add QCheckBox to the import statement
from ui_files.ui_seleccionar_cotas import Ui_Dialog

from fn_elementos_gui import *
from fn_update_gui import *


class cotasTesteroDialog(QDialog):
    def __init__(self, cotas_testero, altura_pieza, parent=None):
        super().__init__(parent)
        self.ui_cotas = Ui_Dialog()
        self.ui_cotas.setupUi(self)
        self.checkBoxes_cotas = []
        self.result_data = []

        y_position = 60 # OFFSET desde donde se agregan los widgets. (bajo de label y botones)
        self.add_cotas(cotas_testero, altura_pieza, y_position)
        
        # Ajusta tamano ventana
        self.adjustSize()
        # Tamano minimo que puede tener la ventana
        self.setMinimumSize(380, 340)

        self.ui_cotas.btn_aceptar.clicked.connect(lambda: self.aceptar())
        self.ui_cotas.btn_cancelar.clicked.connect(lambda: self.cancelar())

    ''' Btns Cancelar y Aceptar '''

    def cancelar(self):
        ''' Handles the action when the cancel button is clicked '''
        print("Cancel button clicked. Closing window.")
        self.close()  # Closes the window when cancel is clicked
    
    def aceptar(self):
        # Retrieve the data entered by the userss
        # Function to check which checkboxes are selected

        selected = []
        for checkbox in self.checkBoxes_cotas:
            if checkbox.isChecked():  # Check if the checkbox is selected
                selected.append(checkbox.text())

        # Print selected checkboxes after the GUI is shown
        print("Selected checkboxes:", selected)
        
        # Recuperar datos
        self.result_data = selected
        self.accept()

    def add_cotas(self, cotas_testero, altura_pieza, y_position):
        ''' Agrega dinamicamente checkBoxes para mostrar cotas disponibles a seleccionar '''
        
        for cota in cotas_testero:
            checkBox = QCheckBox(f"{cota[0]}", self)
            if cota[0] > altura_pieza:
                checkBox.setDisabled(True)

            # NO se usa verticalLayout para adaptar dinamicamente el tamano de la vetana al necesario (segun la cantidad de cotas en testero)
            checkBox.setGeometry(20, y_position, 150, 30)  # Set x=20, y=y_position, width=150, height=30
            
            # Agrega checkBox generada a lista de referencia
            self.checkBoxes_cotas.append(checkBox)
            
            y_position += 20  # Increment Y to position the next checkbox below

        # Ajusta tamano vetana
        self.adjustSize()
        
    



''' Se llama por btn desde armaduras_activas.py '''
def open_cotas_dialog(parent, cotas_testero, altura_pieza):
    # Open the CrearPiezaDialog
    dialog_cotas = cotasTesteroDialog(cotas_testero, altura_pieza, parent)
    if dialog_cotas.exec():  # Open dialog and wait for user action
        print("Dialog accepted!")
        return dialog_cotas.result_data
    else:
        print("Dialog canceled.")
        return None