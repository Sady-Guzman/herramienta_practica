from PySide6.QtWidgets import QDialog, QCheckBox  
from ui_files.ui_seleccionar_cotas import Ui_Dialog

from fn_elementos_gui import *
from fn_update_gui import *

class CotasDialog(QDialog):
    """Base class for handling Cotas selection dialogs."""
    def __init__(self, cotas, parent=None):
        super().__init__(parent)
        self.ui_cotas = Ui_Dialog()
        self.ui_cotas.setupUi(self)
        self.checkBoxes_cotas = []
        self.result_data = []
        
        y_position = 60  # Variable de Offset inicial para agregrar CheckBoxes bajo de Label/Btns y espacio entre ellas
        self.setup_cotas(cotas, y_position)

        # Adjust window size
        self.adjustSize()
        self.setMinimumSize(380, 340)

        # Connect buttons
        self.ui_cotas.btn_aceptar.clicked.connect(self.aceptar)
        self.ui_cotas.btn_cancelar.clicked.connect(self.cancelar)

    def cancelar(self):
        ''' btn cancelar no hace nada (solo cierra ventana)'''
        self.close()

    def aceptar(self):
        ''' maneja btn aceptar. Obtiene checkboxes marcadas para retornarlas a armadura_activa.py'''
        self.result_data = [cb.text() for cb in self.checkBoxes_cotas if cb.isChecked()]
        # print("Checkboxes seleccionadas:", self.result_data)
        self.accept()

    def setup_cotas(self, cotas, y_position):
        ''' Metodo implementado en subclases'''
        raise NotImplementedError("Este metodo se implementa en sub-clases")





class AddCotasTesteroDialog(CotasDialog):
    ''' Dialogo (ventana) para anadir cotas, se dejan sombreadas las cotas que exceden el alto total de la pieza o que ya estan agregadas'''
    def __init__(self, cotas_testero, altura_pieza, cotas_existentes, parent=None):
        self.altura_pieza = altura_pieza
        self.cotas_existentes = [float(c) for c in cotas_existentes]
        super().__init__(cotas_testero, parent)

    def setup_cotas(self, cotas_testero, y_position):
        ''' genera checkboxes '''
        # print("Contenido de cotas_existentes:", self.cotas_existentes)
        # print("Contenido de cotas_testero:", cotas_testero)

        for cota in cotas_testero:
            checkBox = QCheckBox(f"{cota[0]:.3f}", self)

            # Disable checkbox if the cota already exists or exceeds the height limit
            if cota[0] > self.altura_pieza or cota[0] in self.cotas_existentes:
                checkBox.setDisabled(True)

            checkBox.setGeometry(20, y_position, 150, 30)
            self.checkBoxes_cotas.append(checkBox)
            y_position += 20  

        self.adjustSize()






class DelCotasTesteroDialog(CotasDialog):
    ''' Dialogo (ventana) para borrar cotas, Muestra cotas que ya existen en GUI'''
    def __init__(self, cotas_existentes, parent=None):
        self.cotas_existentes = [float(c) for c in cotas_existentes]
        super().__init__(self.cotas_existentes, parent)

    def setup_cotas(self, cotas_existentes, y_position):
        ''' Genera checkboxes '''
        print("Contenido de cotas_existentes:", cotas_existentes)

        for cota in cotas_existentes:
            checkBox = QCheckBox(f"{cota:.3f}", self)
            checkBox.setGeometry(20, y_position, 150, 30)
            self.checkBoxes_cotas.append(checkBox)
            y_position += 20  

        self.adjustSize()







''' Se llama esta funcion para agregar cotas'''
def open_add_cotas_dialog(parent, cotas_testero, altura_pieza, cotas_existentes):
    dialog_cotas = AddCotasTesteroDialog(cotas_testero, altura_pieza, cotas_existentes, parent)
    if dialog_cotas.exec():
        # print("Dialog accepted!")
        return dialog_cotas.result_data
    # print("Dialog canceled.")
    return None

''' Dialogo para borrar cotas'''
def open_del_cotas_dialog(parent, cotas_existentes):
    dialog_cotas = DelCotasTesteroDialog(cotas_existentes, parent)
    if dialog_cotas.exec():
        # print("Dialog accepted!")
        return dialog_cotas.result_data
    # print("Dialog canceled.")
    return None
