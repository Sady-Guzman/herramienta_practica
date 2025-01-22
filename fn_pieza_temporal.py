from PySide6.QtWidgets import QMessageBox
from fn_database import *
from fn_elementos_gui import *
from fn_update_gui import *

''' Guarda informacion de pieza creada de forma temporal en base de datos piezas_creadas.db '''
def save_pieza_data(self):
    # Ensure there is data to save
    if not self.dynamic_layout_data:
        print("Debug: No data to save.")
        return

    # Retrieve the selected family and model
    familia = self.ui.combo_familia.currentText()
    modelo = self.ui.combo_modelo.currentText()

    # Ensure there is a selection in the combo boxes
    if not familia or not modelo:
        print("Debug: No family or model selected.")
        return

    # Prepare the data for insertion
    secciones_data = list(self.dynamic_layout_data.keys())
    trapecios_data = []

    for seccion, trapecios in self.dynamic_layout_data.items():
        for trapecio in trapecios:
            trapecios_data.append((
                seccion,
                trapecio[0],  # Position index
                float(trapecio[1]),  # Base Inferior
                float(trapecio[2]),  # Base Superior
                float(trapecio[3])   # Altura
            ))

    # Call the database insertion function
    db_insert_or_update_pieza(
        pieza_data=(familia, modelo),
        parametros_data=secciones_data,
        trapecios_data=trapecios_data
    )

    print(f"save_pieza_data() -> Saved data for family '{familia}', model '{modelo}' to the database.")


''' Muestra mensaje en ventana emergente al usuario'''
def popup_temp(message):
    popup = QMessageBox()
    popup.setIcon(QMessageBox.Warning)  # Warning icon
    popup.setWindowTitle("Alerta")  # Popup window title
    popup.setText(message)  # Main message text
    popup.setStandardButtons(QMessageBox.Ok)  # Adds an "OK" button
    popup.exec()  # Displays the popup
    