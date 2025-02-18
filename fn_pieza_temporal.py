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

''' Guarda la informacion en los layout dinamicos de la seccion cargada actualemente a la variable que guarda los datos de los trapecios de todas las secciones de la pieza cargada. Se usa principalmente para guardar cambios 'insitu' a la pieza '''
def save_current_section_data(self):

    pieza_seccion_item = self.ui.list_tipo_seccion.currentItem()
    if not pieza_seccion_item:
        print("Debug: No section selected to save.")
        return
    
    pieza_seccion = pieza_seccion_item.text()
    self.seccion_pieza_cargada = pieza_seccion
    current_section_data = []
    
    self.seccion_pieza_cargada = pieza_seccion

    # Collect data from the dynamic layouts
    for i, layout in enumerate(reversed(self.dynamic_layouts)):


        bi = layout["bi_line"].text()
        bs = layout["bs_line"].text()
        altura = layout["altura_line"].text()
        # es_insitu = layout["combo_insitu"].currentText()
        es_insitu = 0 # Por defecto no es Insitu, asigna 0

        print(f"save_current_section_data() -> bi: {bi}, bs: {bs}, altura: {altura} \n")

        if layout["combo_insitu"].currentText() == "Insitu":
            bs = bi
            layout["bs_line"].setText(str(bs))
            es_insitu = 1 # En caso de ser insitu asigna 1


        data = (
            i + 1,  # Position index
            bi,
            bs,
            altura,
            es_insitu
        )
        current_section_data.append(data)

    # Store the data under the selected section name
    self.dynamic_layout_data[pieza_seccion] = current_section_data
    print(f"save_current_section_data() -> Saved data for section '{pieza_seccion}': {self.dynamic_layout_data[pieza_seccion]} \n\n")

    print(f"save_current_section_data() --> El contenido dentro d e dynamic_layout_data es: {self.dynamic_layout_data} \n\n")
