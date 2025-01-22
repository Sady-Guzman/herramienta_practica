from PySide6.QtWidgets import QMessageBox
from fn_database import *
from fn_elementos_gui import *
from fn_update_gui import *

''' Guarda informacion de pieza creada de forma temporal en base de datos piezas_creadas.db '''
def save_pieza_data(self):
    """
    Save the current piece data to the database.
    """
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


def popup_temp(message):
    ''' Displays a popup message with the given message '''
    popup = QMessageBox()
    popup.setIcon(QMessageBox.Warning)  # Warning icon
    popup.setWindowTitle("Alerta")  # Popup window title
    popup.setText(message)  # Main message text
    popup.setStandardButtons(QMessageBox.Ok)  # Adds an "OK" button
    popup.exec()  # Displays the popup





''' Carga la informacion correpondiente de a la seccion de la pieza temporal a layouts dinamicos '''
def load_section_data(self):
    """
    Load the dynamic layout data associated with the selected section.
    """
    pieza_seccion_item = self.ui.list_tipo_seccion.currentItem()
    if not pieza_seccion_item:
        print("Debug: No section selected to load.")
        return

    pieza_seccion = pieza_seccion_item.text()

    # Retrieve the data for the selected section
    section_data = self.dynamic_layout_data.get(pieza_seccion, [])
    cantidad_trapecios_seccion = len(section_data)  # The number of rows in the selected section

    print(f"DEBUG: Selected section '{pieza_seccion}' has {cantidad_trapecios_seccion} trapecios.")

    # Adjust the dynamic layouts to match the number of trapecios in the selected section
    ajustar_layouts_dinamicos(self, cantidad_trapecios_seccion)

    # Populate the dynamic layouts with the data for the selected section
    for i in range(cantidad_trapecios_seccion):
        if i < len(self.dynamic_layouts):  # Ensure we don’t access out-of-range layouts
            layout = self.dynamic_layouts[i]
            if i < len(section_data):  # Populate with stored data if available
                data = section_data[i]
                layout["bi_line"].setText(str(data[1]))
                layout["bs_line"].setText(str(data[2]))
                layout["altura_line"].setText(str(data[3]))
            else:  # Clear the layout fields if no data is available
                layout["bi_line"].setText("")
                layout["bs_line"].setText("")
                layout["altura_line"].setText("")

    print(f"DEBUG load_section_data -> Loaded data for section '{pieza_seccion}': {section_data}")




def save_section_data(self, es_temporal, es_creada, es_primera_vez):
    ''' Save the content of all sections into dynamic_layout_data '''

    # Only process all sections if es_primera_vez is True
    if es_primera_vez:
        print("====================================================================================================")
        print("DEBUG!!!! save_section_data() ----> valor de es_primera_vez: ", es_primera_vez)
        print("\n")
        self.es_primera_vez = False
        # Fetch all section data from the database
        if not es_temporal:
            print("save_section_data() ----> valor de es_temporal: ", es_temporal)
            pieza_familia = self.ui.combo_familia.currentText()
            pieza_modelo = self.ui.combo_modelo.currentText()
            pieza_id = db_get_id_pieza(pieza_familia, pieza_modelo, es_creada)
            all_section_data = db_get_all_trapecios_data(pieza_id, es_creada)

        # Check if there are any sections to save
        if not all_section_data:
            print("Debug: No sections found to save.")
            return

        # Initialize a variable to indicate changes were saved
        self.se_guardaron_cambios = False

        # Iterate through each section and its data
        for seccion, trapecios in all_section_data.items():
            current_section_data = []

            # Iterate through the trapecios for this section
            for idx, trapecio in enumerate(trapecios):
                print(f"*** Processing section '{seccion}' - Trapecio {idx + 1} ***")
                
                # Create data dictionary for each layout
                data = {
                    "bi_line": str(trapecio[1]),  # Convert database values to strings
                    "bs_line": str(trapecio[2]),
                    "altura_line": str(trapecio[3])
                }
                current_section_data.append(data)

            # Save the collected data for this section in dynamic_layout_data
            self.dynamic_layout_data[seccion] = current_section_data
            print(f"Saved data for section '{seccion}':", current_section_data)

        # Update the flag to indicate changes were saved
        self.se_guardaron_cambios = True
        print("All sections have been successfully saved into dynamic_layout_data.")

    else:
        print("====================================================================================================")
        print("DEBUG!!!! save_section_data() ----> valor de es_primera_vez: ", es_primera_vez)
        print("\n")
        # If es_primera_vez is False, retain the previous logic (current section only)
        pieza_seccion_item = self.ui.list_tipo_seccion.currentItem()
        if not pieza_seccion_item:
            print("Debug: No section selected to save.")
            return

        pieza_seccion = pieza_seccion_item.text()
        current_section_data = []

        # Collect data from the dynamic layouts
        for layout in self.dynamic_layouts:
            data = {
                "bi_line": layout["bi_line"].text(),
                "bs_line": layout["bs_line"].text(),
                "altura_line": layout["altura_line"].text()
            }
            current_section_data.append(data)

        # Save the collected data for the currently selected section
        self.dynamic_layout_data[pieza_seccion] = current_section_data
        self.se_guardaron_cambios = True

        print(f"Saved section data for '{pieza_seccion}':", current_section_data)

