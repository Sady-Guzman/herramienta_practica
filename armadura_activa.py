''' codigo para manejar armaduras activas de forma finamica '''

'''
    Se generan y manejan componentes dinamicamente usando listas y diccionarios.

    En tab2 se define un Grid_Layout como contenedor para los elementos que estaran dentro de 
    nuevos layouts dinamicamente generados segun la necesidad del usario.

    Cotas se manejan en un VerticalLayout al que se le agregan dinamicamente LineEdits usando un boton 
    (El usuario puede elegir que cota agregar, Usando una lista con las cotas disponibles en el testero seleccionado, 
    Puede ser en una ventana emergente como en JACENA).
    Al agregar una cota hay que agregar un lineEdit a todos los otros VerticalLayouts que existen (Numero cordones y TPI, de cada tipo de corodon).
    Los valores de las cotas se guardan en lista self.dynamic_cotas[]

    Numero de cordones por cota se especifican en lineEdits que son agregados alineados con la posicion de las cotas. Se agregan a un VerticalLayout que es dinamicamente generado cuando el usuario agrega un tipo de cordon.
    Valores de estos lineEdits se almacenan en diccionario self.dynamic_cant_ordones{}. Un index de diccionario para cada tipo de cordon, dentro del index la lista guarda los valores de los lineEdits de esa columna (Vlayout).
    Este diccionario guarda los valores de todos los distintos tipos de cordones, Asignando un indice para cada tipo de cordon y usando la lista correspondiente a ese indice para almacenar los valores de ese cordon.

    TPI se guardan de la misma manera que numero de cordones, en su propio diccionario: self.dynamic_tpi{}, index y listas de cada indice se maneja de la misma forma que numero de cordones.

    tipos de cordones se manejan con self.dynamic_diametros_arm_act{}, donde cada indice corresponde a un tipo de cordon y dentro esta el valor actual de ComboBox
'''

from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox

def setup_armadura_activa(self):
    self.ui.tab2_btn_add_cota.clicked.connect(self.add_cota)
    self.ui.tab2_btn_add_cord.clicked.connect(self.add_cordon)

    self.ui.tab2_btn_valores.clicked.connect(lambda: print_all_values())

    def print_all_values():
        # Print all ComboBox values
        print("ComboBox Values:")
        for i, combo in enumerate(self.dynamic_diametros_arm_act):
            print(f"  ComboBox {i + 1}: {combo.currentText()}")

        # Print all values for num_cordones and tpi
        print("\nCordones and TPI Values:")
        for index, cordon in self.dynamic_cordones_arm_act.items():
            print(f"  Cordon {index + 1}:")
            
            # Print num_cordones values
            print("    Num Cordones:")
            for j, num_cordon in enumerate(cordon['num_cordones']):
                print(f"      {j + 1}: {num_cordon.text()}")

            # Print tpi values
            print("    TPI:")
            for j, tpi in enumerate(cordon['tpi']):
                print(f"      {j + 1}: {tpi.text()}")

        # Print all cota values
        print("\nCotas:")
        for i, cota in enumerate(self.dynamic_cotas):
            print(f"  Cota {i + 1}: {cota.text()}")

        # Calculate and print the total sum of num_cordones
        total_num_cordones = calculate_total_num_cordones(self)
        print(f"\nTotal Num Cordones: {total_num_cordones}")

        # Assign the total to the QLineEdit
        self.ui.tab2_line_total_cordones.setText(str(total_num_cordones))
        print_cordon_values(self)

        ''' EN DESARROLLO ASIGNAR AREA SEGUN COMBO '''
        def update_area_value(self, index):
            # Get the ComboBox for diametro and the corresponding QLineEdit for area
            combo_value = self.dynamic_diametros_arm_act['area'][index]
            line_edit_area = self.dynamic_cordones_arm_act[index].get('area')

            # Define a mapping of ComboBox values to Area values (customize this logic as needed)
            diametro_value = combo.currentText()
            area_value = self.get_area_value_from_diametro(diametro_value)

            # Update the QLineEdit with the new value
            if line_edit_area:
                line_edit_area.setText(area_value)


def calculate_total_num_cordones(self):
    total = 0
    for cordon in self.dynamic_cordones_arm_act.values():
        for num_cordon in cordon['num_cordones']:
            try:
                total += int(num_cordon.text())
            except ValueError:
                pass  # Ignore non-integer values
    return total

def print_cordon_values(self):
    print("Cordones Values:")
    for index, data in self.dynamic_cordones_arm_act.items():
        diametro = data['diametro'].currentText()
        line_edit_value = data['area'].text()
        print(f"Cordon {index + 1}: Diametro = {diametro}, Area = {line_edit_value}")

''' EN DESARROLLO ASIGNAR AREA SEGUN COMBO '''
def get_area_value_from_diametro(self, diametro_value):
    # Logic to determine the area value based on diametro (can be customized as needed)
    if diametro_value == "Ø 15.24 mm":
        return "100"  # Example value, adjust logic as needed
    elif diametro_value == "Ø 12.7 mm":
        return "80"
    elif diametro_value == "Ø 9.53 mm":
        return "60"
    elif diametro_value == "Ø 4.98 mm":
        return "40"
    return ""  # Default value


class ArmaduraActiva:
    def __init__(self):
        self.dynamic_cotas = []
        self.dynamic_diametros_arm_act = []
        self.dynamic_cordones_arm_act = {}
        self.dynamic_tpi_arm_act = {}

    # def setupUi(self, Dialog):
    #     # ...existing code...
    #     self.ui.tab2_btn_add_cota.clicked.connect(self.add_cota)
    #     self.ui.tab2_btn_add_cord.clicked.connect(self.add_cordon)
    #     # Add buttons to the layout
    #     self.verticalLayout.addWidget(self.ui.tab2_btn_add_cota)
    #     self.verticalLayout.addWidget(self.ui.tab2_btn_add_cord)
    #     # ...existing code...

    def confirmar_borrar(self, index):
        reply = QMessageBox.question(self, 'Confirmar', "Confirmar acción?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return 0
        else:
            self.del_cordon(index)





'''
def add_cordon(self):
    # Remove existing horizontal spacer if present
    if self.ui.gridLayout.itemAtPosition(1, 1):  # Check position (1, 1)
        item = self.ui.gridLayout.itemAtPosition(1, 1)
        if item:
            self.ui.gridLayout.removeItem(item)
            del item

    # Determine the new column index
    index = len(self.dynamic_cordones_arm_act)  # Use length of dictionary for the new index

    # Create a new grid layout for this cordon
    sub_grid_layout = QGridLayout()

    # Add the "Tipo" label
    label_tipo = QLabel("Tipo")
    label_tipo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    sub_grid_layout.addWidget(label_tipo, 0, 0)

    # Add the ComboBox for diametro
    combo = QComboBox()
    combo.addItems(["Ø 15.24 mm", "Ø 12.7 mm", "Ø 9.53 mm", "Ø 4.98 mm"])
    combo.setMinimumSize(130, 0)
    combo.setMaximumSize(131, 16777215)
    sub_grid_layout.addWidget(combo, 1, 0)

    # Add the "Area" label
    label_area = QLabel("Area")
    label_area.setAlignment(Qt.AlignmentFlag.AlignCenter)
    sub_grid_layout.addWidget(label_area, 0, 1)

    # Add the QLineEdit for area
    line_edit_area = QLineEdit()
    line_edit_area.setMinimumSize(70, 0)
    line_edit_area.setMaximumSize(100, 16777215)
    sub_grid_layout.addWidget(line_edit_area, 1, 1)

    # Add the new sub-grid layout to the main grid layout
    self.ui.gridLayout.addLayout(sub_grid_layout, 0, index)

    # Store references in the dictionary
    self.dynamic_cordones_arm_act[index] = {
        'diametro': combo,        # Reference to the ComboBox
        'line_edit_area': line_edit_area  # Reference to the QLineEdit
    }

    # Add horizontal spacer back to the grid layout
    self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
    self.ui.gridLayout.addItem(self.horizontalSpacer, 1, index + 1)

'''