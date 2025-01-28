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

from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox, QSpacerItem, QHBoxLayout, QSizePolicy, QGridLayout
from PySide6.QtCore import Qt
from fn_database import db_recuperar_diametros_cordones
from utils import popup_msg

def setup_armadura_activa(self):
    self.ui.tab2_btn_add_cota.clicked.connect(add_cota)
    self.ui.tab2_btn_add_cord.clicked.connect(add_cordon)
    self.ui.tab2_btn_del_cord.clicked.connect(del_cordon)

    self.ui.tab2_btn_valores.clicked.connect(lambda: print_all_values(self))

    

def update_area_values(self):
    """Iterate through all ComboBoxes and update their corresponding area QLineEdit values."""
    print("update_area_values() -> Entra func \n")
    for index, combo in enumerate(self.dynamic_diametros_arm_act):
        if index in self.dynamic_cordones_arm_act:  # Ensure there's a corresponding cordon entry
            line_edit_area = self.dynamic_cordones_arm_act[index].get('area')

            if line_edit_area:
                diametro_value = combo.currentText()
                area_value = ac_transformar_area_cordon(self, diametro_value)
                line_edit_area.setText(area_value)

def ac_transformar_area_cordon(self, diametro_cordon):
    ''' Asigna un valor de area a cada tipo de cordon (diametro), El valor esta definido en Documentacion General 1.'''

    if diametro_cordon == "Ø 15.24 mm":
        return "1400"
    elif diametro_cordon == "Ø 12.7 mm":
        return "0.987"
    elif diametro_cordon == "Ø 9.53 mm":
        return "0.548"
    elif diametro_cordon == "Ø 4.98 mm":
        return "0.195"
    else:
        return "error"

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


def print_all_values(self):
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

    

    total_area = armact_calcular_total_area(self)

    # Assign the total to the QLineEdit
    self.ui.tab2_line_total_cordones.setText(str(total_num_cordones))
    self.ui.tab2_line_total_area.setText(str(total_area))

    update_area_values(self)
    print_cordon_values(self)

    



''' Calcula el area total de los cordones, multiplicando la cantidad de cordones por el area asignada segun el tipo de cordon '''
def armact_calcular_total_area(self):
    total_area = 0.0

    for index, cordon in self.dynamic_cordones_arm_act.items():
        # Get the ComboBox value (diameter)
        diametro_value = cordon['diametro'].currentText()
        # Get the area per cordon based on diameter
        area_per_cordon = float(ac_transformar_area_cordon(self, diametro_value))

        # Sum the number of cordones
        total_num_cordones = sum(
            int(num_cordon.text()) if num_cordon.text().isdigit() else 0
            for num_cordon in cordon['num_cordones']
        )

        # Multiply num_cordones by area per cordon
        total_area += total_num_cordones * area_per_cordon

    return round(total_area, 3)  # Round for better readability

''' ========================= metodos para manejo de generacion/eliminacion dinamica de cordones y cotas =================='''



def add_cota(self):
    ''' Maneja vertical stretcher para solo tener 1 y que siempre esté abajo '''
    if self.ui.verticalLayout.itemAt(self.ui.verticalLayout.count() - 1).spacerItem():
        # Elimina el último item si es el vertical stretcher
        item = self.ui.verticalLayout.takeAt(self.ui.verticalLayout.count() - 1)
        del item

    # Create the QLineEdit for 'cota'
    cota_line = QLineEdit()
    cota_line.setMinimumSize(70, 0)  # Set minimum width to 70 units
    cota_line.setMaximumSize(70, 16777215)  # Set maximum width to 70 units, height can be unlimited
    self.dynamic_cotas.append(cota_line)
    self.ui.verticalLayout.addWidget(cota_line)

    ''' Vuelve a insertar el vertical stretcher en la posición inferior del layout vertical '''
    self.ui.verticalLayout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    for cordon in self.dynamic_cordones_arm_act.values():
        cordon['num_cordones'].append(QLineEdit())
        cordon['tpi'].append(QLineEdit("1400"))

        # Set minimum and maximum size for the new QLineEdits
        cordon['num_cordones'][-1].setMinimumSize(70, 0)
        cordon['num_cordones'][-1].setMaximumSize(70, 16777215)
        cordon['tpi'][-1].setMinimumSize(70, 0)
        cordon['tpi'][-1].setMaximumSize(70, 16777215)

        # Remove existing spacer in the vertical layouts
        if cordon['layout_num_cordones'].itemAt(cordon['layout_num_cordones'].count() - 1).spacerItem():
            item = cordon['layout_num_cordones'].takeAt(cordon['layout_num_cordones'].count() - 1)
            del item
        if cordon['layout_tpi'].itemAt(cordon['layout_tpi'].count() - 1).spacerItem():
            item = cordon['layout_tpi'].takeAt(cordon['layout_tpi'].count() - 1)
            del item

        # Add new widgets to layouts
        cordon['layout_num_cordones'].addWidget(cordon['num_cordones'][-1], alignment=Qt.AlignmentFlag.AlignCenter)  # Align to center
        cordon['layout_tpi'].addWidget(cordon['tpi'][-1], alignment=Qt.AlignmentFlag.AlignCenter)  # Align to center

        # Re-add the spacer to ensure it is always at the bottom
        cordon['layout_num_cordones'].addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        cordon['layout_tpi'].addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))



def add_cordon(self):
    diametros_en_db = db_recuperar_diametros_cordones()
    ''' Se asegura de que no se generen mas cordones de la cantidad de tipos de cordones que existen en DB '''
    if len(self.dynamic_cordones_arm_act) >= len(diametros_en_db):
        popup_msg("Solo hay 4 tipos de cordones en base de datos")
        return 
    
    # Determine the new column index using columnCount()
    index = self.ui.gridLayout.columnCount()  # Use columnCount to get the current number of columns

    ''' elimina spacer al final de gridLayout. (No funciona bien) '''
    last_column = index - 1  # Last column index before adding a new one
    if self.ui.gridLayout.itemAtPosition(1, last_column):  # Row 1, Last column
        item = self.ui.gridLayout.itemAtPosition(1, last_column)
        if isinstance(item, QSpacerItem):
            self.ui.gridLayout.removeItem(item)

    # variable 'index' no es precisa en real cantidad de cordones
    index_para_clave = len(self.dynamic_cordones_arm_act)

    # Create a new grid layout for this column
    sub_grid_layout = QGridLayout()

    # Add the "Tipo" label at (0, 0)
    label_tipo = QLabel("Tipo")
    label_tipo.setAlignment(Qt.AlignmentFlag.AlignCenter)
    sub_grid_layout.addWidget(label_tipo, 0, 0)

    # Add the ComboBox at (1, 0)
    combo = QComboBox()
    ''' Poblar comboBox generada dimamicamente con diametros disponibles en DB '''
    for diametro in diametros_en_db:
        combo.addItem(f"Ø {diametro} mm")
    
    combo.setMinimumSize(130, 0)  # Min width: 99, height: default (0)
    combo.setMaximumSize(131, 16777215)  # Max width: 100, height: unlimited
    sub_grid_layout.addWidget(combo, 1, 0)

    # Add the "Area" label at (0, 1)
    label_area = QLabel("Area cm2")
    label_area.setAlignment(Qt.AlignmentFlag.AlignCenter)
    sub_grid_layout.addWidget(label_area, 0, 1)

    # Add a QLineEdit at (1, 1)
    line_edit_area = QLineEdit()
    line_edit_area.setMinimumSize(70, 0)
    line_edit_area.setMaximumSize(100, 16777215)
    sub_grid_layout.addWidget(line_edit_area, 1, 1)

    # Add the new sub-grid layout to the main grid layout in the new column
    self.ui.gridLayout.addLayout(sub_grid_layout, 0, index)

    # Set stretch for the new column to allow resizing
    self.ui.gridLayout.setColumnStretch(index, 1)

    # Create layouts for 'num_cordones' and 'tpi'
    layout = QHBoxLayout()
    layout_num_cordones = QVBoxLayout()
    layout_tpi = QVBoxLayout()

    # Set the spacing to 0 for the dynamically generated layouts
    layout_num_cordones.setSpacing(0)
    layout_tpi.setSpacing(0)

    # Labels for 'num_cordones' and 'tpi'
    label_num_cordones = QLabel("Nº Cordones")
    label_tpi = QLabel("TPI (N/mm2)")

    # Align the labels to the center
    label_num_cordones.setAlignment(Qt.AlignmentFlag.AlignCenter)
    label_tpi.setAlignment(Qt.AlignmentFlag.AlignCenter)

    layout_num_cordones.addWidget(label_num_cordones)
    layout_tpi.addWidget(label_tpi)

    # Create QLineEdits for each 'cota'
    num_cordones = [QLineEdit() for _ in self.dynamic_cotas]
    tpi = [QLineEdit("1400") for _ in self.dynamic_cotas]

    # Set min and max size for the QLineEdits
    for nc, tp in zip(num_cordones, tpi):
        nc.setMinimumSize(70, 0)
        nc.setMaximumSize(71, 16777215)
        tp.setMinimumSize(70, 0)
        tp.setMaximumSize(71, 16777215)

        # Add QLineEdits to the layouts with centered alignment
        layout_num_cordones.addWidget(nc, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_tpi.addWidget(tp, alignment=Qt.AlignmentFlag.AlignCenter)

    # Add spacers to ensure items align properly at the bottom
    layout_num_cordones.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
    layout_tpi.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    # Add the layouts to the main layout
    layout.addLayout(layout_num_cordones)
    layout.addLayout(layout_tpi)

    # Add the new layout to the grid layout in the new column
    self.ui.gridLayout.addLayout(layout, 1, index)

    # Set stretch for the new column to allow resizing
    self.ui.gridLayout.setColumnStretch(index, 1)

    # Ensure that the layout grows with the new column
    self.ui.gridLayoutWidget.adjustSize()
    self.ui.gridLayoutWidget.resize(self.ui.gridLayoutWidget.sizeHint())
    self.ui.gridLayoutWidget.setMinimumSize(self.ui.gridLayoutWidget.sizeHint())

    # Update the dynamic data structures
    self.dynamic_diametros_arm_act.append(combo)
    # self.dynamic_areas_arm_act.append(line_edit_area)

    # Store ComboBox, QLineEdit, and other related widgets in dynamic_cordones_arm_act dictionary
    self.dynamic_cordones_arm_act[index_para_clave] = {
        'layout': layout,
        'layout_num_cordones': layout_num_cordones,
        'layout_tpi': layout_tpi,
        'num_cordones': num_cordones,  # Store QLineEdits for num_cordones
        'tpi': tpi,  # Store QLineEdits for tpi
        'diametro': combo,  # Store ComboBox for diameter
        'area': line_edit_area,  # Store QLineEdit for area
        'label_tipo': label_tipo,  # Store QLabel for tipo
        'label_area': label_area,  # Store QLabel for area
        'label_num_cordones': label_num_cordones,  # Store QLabel for num_cordones
        'label_tpi': label_tpi  # Store QLabel for tpi
    }

    ''' Agrega nuevamente Spacer al final de GridLayout. (No funciona bien) '''
    # self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
    # self.ui.gridLayout.addItem(self.horizontalSpacer, 1, index + 1)  # Add it to the rightmost side of the grid

    # Adjust the stretch for all columns to maintain balance
    for col in range(index + 2):  # Adjusts stretching for all columns, including the new one and the spacer
        self.ui.gridLayout.setColumnStretch(col, 1)

    print("add_cordon() --> Nueva cantidad de cordones es: ", len(self.dynamic_cordones_arm_act), "\n")




def del_cordon(self):
    if self.dynamic_cordones_arm_act:
        last_index = max(self.dynamic_cordones_arm_act.keys())
        cordon = self.dynamic_cordones_arm_act.pop(last_index)

        # Delete widgets (QLineEdit and QComboBox)
        for widget in cordon['num_cordones'] + cordon['tpi']:
            widget.deleteLater()
        cordon['diametro'].deleteLater()
        cordon['area'].deleteLater()

        # Delete labels
        cordon['label_tipo'].deleteLater()
        cordon['label_area'].deleteLater()
        cordon['label_num_cordones'].deleteLater()
        cordon['label_tpi'].deleteLater()

        # Remove layout from grid
        self.ui.gridLayout.removeItem(cordon['layout'])
        cordon['layout'].deleteLater()

        # Remove from list of dynamically generated diameters
        self.dynamic_diametros_arm_act.pop()

        ''' Agrega spacer al final de GridLayout (No funciona bien) '''
        # last_column = self.ui.gridLayout.columnCount() - 1
        # self.ui.gridLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum), 1, last_column)
    else:
        print("del_cordon() --> No existen cordones que borrar \n")





# class ArmaduraActiva:
#     def __init__(self):
#         self.dynamic_cotas = []
#         self.dynamic_diametros_arm_act = []
#         self.dynamic_cordones_arm_act = {}
#         self.dynamic_tpi_arm_act = {}


#     def confirmar_borrar(self, index):
#         reply = QMessageBox.question(self, 'Confirmar', "Confirmar acción?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#         if reply == QMessageBox.No:
#             return 0
#         else:
#             self.del_cordon(index)


