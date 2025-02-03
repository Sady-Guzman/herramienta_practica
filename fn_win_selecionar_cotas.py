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

        self.add_cotas(cotas_testero, altura_pieza)
        
        # Automatically adjust the size to fit the number of checkboxes
        self.adjustSize()
        # Optionally set a minimum size for the dialog
        self.setMinimumSize(200, 100)

    ''' Btns Cancelar y Aceptar '''

    # def cancelar(self):
    #     ''' Handles the action when the cancel button is clicked '''
    #     print("Cancel button clicked. Closing window.")
    #     self.close()  # Closes the window when cancel is clicked
    
    # def aceptar(self):
    #     # Retrieve the data entered by the user
        
    #     # Recuperar datos

    #     self.accept()

    def add_cotas(self, cotas_testero, altura_pieza):
        ''' agrega dinamicamente checkBoxes para mostrar cotas disponibles a seleccionar '''

        for cota in cotas_testero:
            checkBox = QCheckBox(f"{cota[0]}", self)
            if cota[0] > altura_pieza:
                checkBox.setDisabled(True)
            self.ui_cotas.layout_cotas.addWidget(checkBox)
            self.checkBoxes_cotas.append(checkBox)
        
        
    



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