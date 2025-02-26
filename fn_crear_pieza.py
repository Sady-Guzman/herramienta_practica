''' 
    Maneja funcionamiento de ventana para crear una nueva pieza temporal.

    La ventana crear_pieza se invoca al hacer click en 'btn_crear_pieza_temp' en la ventana principal.

    Cumple con la funcion de obtener del usuario:
        - Nombre Familia
        - Nombre Modelo
        - Cantidad de Secciones
        - Nombre de cada Seccion que se va a agregar.
    
    Luego de que usuario ingresa datos y hace click en 'aceptar', Se almacenan los datos para insertarlos a la Base de Datos
    piezas_creadas.db y la ventana se cierra.

    Desde este archivo se crea la ventana, y se maneja la logica front/back-end, con apoyo de funciones de imports.
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
        self.ventana_crear_secciones_dinamicas = 0
        self.ventana_crear_historial_agregados = 0
        self.ventana_crear_dynamic_layouts = []


        self.ui_crear.btn_aceptar.clicked.connect(self.aceptar) # btn Aceptar
        self.ui_crear.btn_cancelar.clicked.connect(self.cancelar) # btn Cancelar

        self.ui_crear.btn_agregar_seccion.clicked.connect(self.add_dynamic_layout) # Btn Agregar
        self.ui_crear.btn_eliminar_seccion.clicked.connect(self.remove_dynamic_layout) # Btn eliminar

    
    
    

    ''' Btns Cancelar y Aceptar '''

    def cancelar(self):
        ''' Handles the action when the cancel button is clicked '''
        print("Cancel button clicked. Closing window.")
        self.close()  # Closes the window when cancel is clicked
    
    def aceptar(self):
        # Retrieve the data entered by the user
        familia = self.ui_crear.lineEdit_familia.text()
        modelo = self.ui_crear.lineEdit_modelo.text()
        cantidad_secciones = self.ventana_crear_secciones_dinamicas

        # Validate inputs
        if not familia or not modelo or cantidad_secciones <= 0 or not self.validate_dynamic_layouts():
            print("DEBUG crear_pieza -> Please enter valid data for all fields.")
            self.show_popup("Ingresar todos los valores requeridos.")
            return

        # Collect the content of the dynamic QLineEdit widgets
        secciones = [layout["line_edit"].text() for layout in self.ventana_crear_dynamic_layouts]

        # Close the dialog after processing
        # print(f"Familia: {familia}, Modelo: {modelo}, Cantidad de Secciones: {cantidad_secciones}, Contenido Secciones: {secciones}")
        self.result_data = {
            "familia": familia,
            "modelo": modelo,
            "cantidad_secciones": cantidad_secciones,
            "secciones": secciones
        }
        print("fn_crear_pieza() --> Contenido que se entrega a main dialog: ", self.result_data)
        self.accept()

    def validate_dynamic_layouts(self):
        ''' Validates that all dynamic QLineEdit widgets have text '''
        for layout in self.ventana_crear_dynamic_layouts:
            line_edit = layout.get("line_edit")
            if line_edit and not line_edit.text().strip():
                return False
        return True

    ''' Logica agregar / eliminar '''

    def add_dynamic_layout(self):
        ''' Adds a dynamic layout when the "Agregar" button is clicked '''
        index = self.ventana_crear_secciones_dinamicas + 1  # Set the new section index

        # Call the function to add the row (dynamic layout)
        self.add_rows_simple(index)

        # Update the number of dynamic sections
        self.ventana_crear_secciones_dinamicas += 1
        print(f"DEBUG crear_pieza -> Added section {index}. Total sections now: {self.ventana_crear_secciones_dinamicas}")
    
    def remove_dynamic_layout(self):
        ''' Removes a dynamic layout when the "Eliminar" button is clicked '''
        
        if self.ventana_crear_secciones_dinamicas > 0:
            # Call the function to remove the row (dynamic layout)
            self.del_rows_create_piezas(1)

            # Update the number of dynamic sections
            print(f"DEBUG crear_pieza -> Removed section. Total sections now: {self.ventana_crear_secciones_dinamicas}")
        else:
            print("DEBUG crear_pieza -> No more sections to remove.")
    
    def delete_layout_widgets(self, layout):
        ''' Deletes all widgets in a layout '''
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                elif item.layout() is not None:
                    self.delete_layout_widgets(item.layout())

   

    ''' Funciones para VENTANA CREAR PIEZA '''
    def add_rows_simple(self, index):
        ''' Adds a single row with one QLineEdit to the layout '''
        # Remove the vertical stretcher if present
        if self.ui_crear.layout_nuevas_row.itemAt(self.ui_crear.layout_nuevas_row.count() - 1).spacerItem():
            item = self.ui_crear.layout_nuevas_row.takeAt(self.ui_crear.layout_nuevas_row.count() - 1)
            del item

        # Create a horizontal layout for the row
        layout = QHBoxLayout()
        layout_name = f"layout_s{index}"

        # Create the QLineEdit
        name_label = QLabel(f"Sección {index}")  # Usa tab + 4 espacios para coincidir
        line_edit = QLineEdit()

        name_label.setObjectName(f"t{index}_name")
        line_edit.setObjectName(f"s{index}_name")  # Assign a unique object name

        # Add the QLineEdit to the layout
        layout.addWidget(name_label)
        layout.addWidget(line_edit)

        # Insert the layout at the end (instead of the beginning)
        self.ui_crear.layout_nuevas_row.addLayout(layout)

        # Add the vertical stretcher back to the bottom
        self.ui_crear.layout_nuevas_row.addStretch()

        # Keep a reference to the line_edit for future access if needed
        self.ventana_crear_dynamic_layouts.append({"line_edit": line_edit})

    def del_rows_create_piezas(self, num_rows):
        ''' Removes a dynamic layout '''
        print(f"DEBUG del_rows_create_piezas() > Removing {num_rows} layout(s)")

        if num_rows == 0:
            return

        ''' Removes the vertical stretcher temporarily '''
        if self.ui_crear.layout_nuevas_row.itemAt(self.ui_crear.layout_nuevas_row.count() - 1).spacerItem():
            item = self.ui_crear.layout_nuevas_row.takeAt(self.ui_crear.layout_nuevas_row.count() - 1)
            del item

        ''' Removes layouts starting from the end '''
        for _ in range(num_rows):
            if self.ui_crear.layout_nuevas_row.count() > 0:
                # Take the last layout item (last visually, last logically)
                last_index = self.ui_crear.layout_nuevas_row.count() - 1
                last_item = self.ui_crear.layout_nuevas_row.takeAt(last_index)

                if last_item.layout():
                    self.delete_layout_widgets(last_item.layout())

                del last_item  # Delete the layout from the container

                # Remove the reference to the layout from the dynamic layouts list
                self.ventana_crear_dynamic_layouts.pop()

                # Decrement the dynamic section counter
                self.ventana_crear_secciones_dinamicas -= 1
                print(f"DEBUG crear_pieza -> Current number of sections: {self.ventana_crear_secciones_dinamicas}")

        ''' Add the vertical stretcher back to the layout '''
        self.ui_crear.layout_nuevas_row.addStretch()

    ''' TODO Cambiar nombre a caso especifico '''
    def show_popup(self, message):
        ''' Displays a popup message with the given message '''
        popup = QMessageBox()
        popup.setIcon(QMessageBox.Warning)  # Warning icon
        popup.setWindowTitle("Alerta")  # Popup window title
        popup.setText(message)  # Main message text
        popup.setStandardButtons(QMessageBox.Ok)  # Adds an "OK" button
        popup.exec_()  # Displays the popup


''' Se llama por btn desde main.py '''
def open_crear_pieza_dialog(self):
    # Open the CrearPiezaDialog
    dialog_crear = CrearPiezaDialog(self)
    if dialog_crear.exec():  # Open dialog and wait for user action
        print("Dialog accepted!")
        return dialog_crear.result_data
    else:
        print("Dialog canceled.")
        return None