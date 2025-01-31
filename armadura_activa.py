''' codigo para manejar armaduras activas de forma dinamica '''

'''
    Se generan y manejan componentes dinamicamente usando diccionario self.dynamic_cordones_arm_act = {} que guarda las referencias necesarias a los widgets generados para cada cota/cordon de armadura

    tambien se usan listas y diccionarios: 
        self.dynamic_cotas = []
        self.dynamic_diametros_arm_act = []
        self.dynamic_tpi_arm_act = {}
        self.dynamic_cordones_arm_act = {}
    para guardar los valores ingresados por el usuario en los campos de cada variable.
'''

from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox, QSpacerItem, QHBoxLayout, QSizePolicy, QGridLayout
from PySide6.QtCore import Qt
from fn_database import db_recuperar_diametros_cordones, db_area_cordon
from utils import popup_msg
import re




def setup_armadura_activa(self):
    self.ui.tab2_btn_add_cota_custom.clicked.connect(lambda: add_cota(self))
    self.ui.tab2_btn_add_cord.clicked.connect(lambda: add_cordon(self))
    self.ui.tab2_btn_del_cord.clicked.connect(lambda: del_cordon(self))

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
    ''' diametros se obtienen en formato: Ø 15.24 mm
        primero se transformar a formato con solo numero: 15.24 y se entrega como parametro a db_area_cordon para hacer consulta en DB'''
    # Extraer solo el numero de seleccion de comboBox
    diametro_numerico = re.search(r"[\d.]+", diametro_cordon)
    
    if diametro_numerico:
        diametro_numerico = diametro_numerico.group()  # extrae numero
    else:
        return "error" 
    
    area = db_area_cordon(diametro_numerico)

    if area:
        return str(area)

    # En caso de probleas con base de datos usar valores fijos
    # if diametro_cordon == "Ø 15.24 mm":
    #     return "1400"
    # elif diametro_cordon == "Ø 12.7 mm":
    #     return "0.987"
    # elif diametro_cordon == "Ø 9.53 mm":
    #     return "0.548"
    # elif diametro_cordon == "Ø 4.98 mm":
    #     return "0.195"
    # else:
    #     return "error"



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

    if not self.dynamic_cotas:
        print("ERROR: No se encontrarron cotas en GUI")
        return
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
    # arm_act_obtener_datos_formula(self)
    arm_act_cdg(self)
    armact_cargar_datos_dict(self)

def arm_act_cdg(self):

    ''' Calcula el centro de gravedad de los cordones de armadura activa (ignora concreto en calculo) 
        Calcula cdg con y sin TPI considerado en formula
    '''
    ''' calculo: ((area para tipo de cordon * cota * tpi) * cantidad cordones de ese tipo en esa cota) +... (repite para cada tipo de cordon que existe agregado) / area de cordon * cantidad de cordones * tpi ... repetir para cada tipo de cordon'''
    ''' Ejemplo: 1 cordon de 9.52mm en cota 0.170 m con un tpi de 900 y 2 cordones 15.24 mm en cota 0.05 m con tpi 1200

        se calcula: (((0.548 * 0.170 * 900) * 1) + ((1.400 * 0.05 * 1200) * 2)) / ((1.400 * 2 * 1200) + (0.548 * 1 * 900))

         # 0.548 cm2 y 1.400 cm2 son areas correspondientes para esos cordones en documentacion general

        Formula para calcular sin tpi es igual, solo hay que sacar tpi de parentesis
    '''

    print("\n************************************************************\n")
    print("************************************************************\n")
    cant_cotas = len(self.dynamic_cotas)
    # print(f"Cantidad Cotas: {cant_cotas}\n")

    cant_tipos_cordones = len(self.dynamic_cordones_arm_act)
    # print(f"Cantidad tipo cordones: {cant_tipos_cordones}\n")

    numerador = 0
    numerador_acum = 0

    denominador = 0
    denominador_acum = 0

    cdg = 0

    ''' -------------------------------------'''
    ''' calculo considerando TPI '''
    for y in range(cant_cotas):
        # print("\n")
        for x in range(cant_tipos_cordones):
            # print(f"**************** \nen cota:{y} en cordon:{x}\n")

            cordon = self.dynamic_cordones_arm_act.get(x)
            cota = self.dynamic_cotas[y].text()
            
            area = cordon['area'].text()
            n_cords = cordon['num_cordones'][y].text()
            tpi = cordon['tpi'][y].text()

            try:
                # print(f"cota:{cota}, area:{area}, num_cords:{n_cords}, tpi:{tpi} ", end=" | ")
                numerador = (float(cota) * (float(n_cords))*(float(tpi))*float(area))
                # print(f"Valor numerador: {numerador}")
                numerador_acum += numerador
                # print(f"Valor numerador acumulado: {numerador_acum}\n")

                denominador = (float(area) * float(n_cords) * float(tpi))
                # print(f"valor de denominador: {denominador}")
                denominador_acum += denominador
                # print(f"valor de denominador acumulado: {denominador_acum}\n")
            except Exception as error:
                print("Se encuentra error en calculo: ", error, "\n")

    try:
        cdg = (numerador_acum / denominador_acum)
    except Exception as error:
        cdg = 0
        print("Se encuentra error en calculo: ", error, "\n")
    print("\n><<><><><><><><><><><><><><><><><><><><><><><><><><><\n")
    print("\t\t\t RESULTADO CDG con TPI")
    print(f"CDG = {cdg}\n\n\n")
    
    self.ui.tab2_line_total_cdg_fuerza.setText(str(round(cdg, 4)))
    
    numerador = 0
    numerador_acum = 0

    denominador = 0
    denominador_acum = 0

    cdg = 0

    ''' -------------------------------------'''
    ''' calculo SIN  TPI '''
    for y in range(cant_cotas):
        # print("\n")
        for x in range(cant_tipos_cordones):
            # print(f"**************** \nen cota:{y} en cordon:{x}\n")

            cordon = self.dynamic_cordones_arm_act.get(x)
            cota = self.dynamic_cotas[y].text()
            
            area = cordon['area'].text()
            n_cords = cordon['num_cordones'][y].text()
            try:
                numerador = (float(cota) * (float(n_cords))*float(area))
                # print(f"Valor numerador: {numerador}")
                numerador_acum += numerador
                # print(f"Valor numerador acumulado: {numerador_acum}\n")

                denominador = (float(area) * float(n_cords))
                # print(f"valor de denominador: {denominador}")
                denominador_acum += denominador
                # print(f"valor de denominador acumulado: {denominador_acum}\n")
            except Exception as error:
                print("Se encuentra error en calculo: ", error, "\n")
    
    try:
        cdg = (numerador_acum / denominador_acum)
    except Exception as error:
        cdg = 0
        print("Se encuentra error en calculo: ", error, "\n")

    print("\n><<><><><><><><><><><><><><><><><><><><><><><><><><><\n")
    print("\t\t\t RESULTADO CDG sin TPI")
    print(f"CDG = {cdg}\n\n\n")
    self.ui.tab2_line_total_cdg_area.setText(str(round(cdg, 4)))



# def arm_act_obtener_datos_formula(self):
#     print("******************************\n")

#     cant_cotas = len(self.dynamic_cotas)
#     print(f"Cantidad Cotas: {cant_cotas}\n")

#     cant_tipos_cordones = len(self.dynamic_cordones_arm_act)
#     print(f"Cantidad tipo cordones: {cant_tipos_cordones}\n")


#     for z in range(cant_cotas):
#         print("\n")
#         for x in range(cant_tipos_cordones):
#             cordon = self.dynamic_cordones_arm_act.get(x)
#             cota = self.dynamic_cotas[z].text()
            
#             area = cordon['area'].text()
#             n_cords = cordon['num_cordones'][z].text()
#             tpi = cordon['tpi'][z].text()

#             print(f"cota:{cota}, area:{area}, num_cords:{n_cords}, tpi:{tpi} ", end=" | ")


def armact_cargar_datos_dict(self):
    ''' Carga todos los datos de armaduras activas a una lista para cotas y 
        un diccionario para n_cordones y tpi, ordenándolos por cota.
    '''
    print("[][][][][][][][][][][][][][][[][][][][][][]")
    print_dynamic_cordones_values(self)
    print("[][][][][][][][][][][][][][][[][][][][][][]")

    lista_cotas = []  # Lista que guarda solo los valores de cotas
    dict_cordones = {}  # Diccionario con el índice del cordón como clave

    cant_cotas = len(self.dynamic_cotas)
    cant_tipos_cordones = len(self.dynamic_cordones_arm_act)

    print(f"Cantidad Cotas: {cant_cotas} \n")
    print(f"Cantidad tipo cordones: {cant_tipos_cordones} \n")

    # Extraer valores de las cotas
    for i in range(cant_cotas):
        lista_cotas.append(self.dynamic_cotas[i].text())

    print(f"Contenido de lista_cotas antes de ordenar: {lista_cotas} \n")

    # Ordenar lista_cotas en orden descendente
    lista_cotas.sort(key=lambda x: float(x), reverse=True)  

    print(f"Contenido de lista_cotas ordenado de mayor a menor: {lista_cotas} \n")

    # Crear diccionario de cordones ordenados por cota, usando el índice como clave
    for x in range(cant_tipos_cordones):
        cordon = self.dynamic_cordones_arm_act.get(x)
        tipo_cordon = cordon['area'].text()  # Se sigue utilizando solo para obtener el texto, no como clave del diccionario
        
        # Usar el índice como la clave del diccionario
        dict_cordones[x] = []

        # Asociar valores de num_cordones y tpi con cota
        for z in range(cant_cotas):
            cota = self.dynamic_cotas[z].text()
            num_cords = cordon['num_cordones'][z].text()
            tpi = cordon['tpi'][z].text()
            dict_cordones[x].append((cota, num_cords, tpi))

    print("\nContenido de dict_cordones ORIGINAL:")
    for tipo_cordon, valores in dict_cordones.items():
        print(f"Índice {tipo_cordon}: {valores}")

    # Ordenar valores dentro del diccionario por cota (de mayor a menor)
    for tipo_cordon in dict_cordones:
        dict_cordones[tipo_cordon] = sorted(dict_cordones[tipo_cordon], key=lambda x: float(x[0]), reverse=True)

    print("\nContenido de dict_cordones ordenado de mayor a menor:")
    for tipo_cordon, valores in dict_cordones.items():
        print(f"Índice {tipo_cordon}: {valores}")

    # Asignar los valores ordenados a los QLineEdit en la GUI
    for i, cota in enumerate(lista_cotas):
        self.dynamic_cotas[i].setText(cota)

    print("[][][][][][][][][][][][][][][[][][][][][][]")
    print_dynamic_cordones_values(self)
    print("[][][][][][][][][][][][][][][[][][][][][][]")
    

    # Reasignar los valores de num_cordones y tpi a las posiciones correctas según el nuevo orden de las cotas
    for tipo_cordon, valores in dict_cordones.items():
        print(f"Procesando índice {tipo_cordon}")
        
        # Obtener el cordón correcto para este índice
        cordon = self.dynamic_cordones_arm_act.get(tipo_cordon)
        if cordon is None:
            print(f"No se encontró el cordón con índice {tipo_cordon}")
            continue
        
        # Acceder a los QLineEdits de num_cordones y tpi para este cordón
        for i, (cota, num_cords, tpi) in enumerate(valores):
            print(f"Iteración {i}: Cota {cota}, Num_Cordones {num_cords}, TPI {tpi}")

            # Acceder a los QLineEdits de num_cordones y tpi para este cordón
            num_cord = cordon['num_cordones'][i]  # i para acceder al elemento correcto
            tpi_cord = cordon['tpi'][i]  # i para acceder al elemento correcto
            
            # Actualizar los valores de num_cordones y tpi en la GUI
            print(f"Actualizando QLineEdit: num_cord {num_cords} y tpi {tpi}")
            num_cord.setText(num_cords)  # Actualiza el valor de num_cordones
            tpi_cord.setText(tpi)  # Actualiza el valor de tpi


    # Verificar si las actualizaciones a la GUI se han realizado correctamente
    print("[][][][][][][][][][][][][][][[][][][][][][]")
    print_dynamic_cordones_values(self)
    print("[][][][][][][][][][][][][][][[][][][][][][]")
    print(f"\nSe han reasignado los valores en la GUI en el nuevo orden.\n")



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







''' ================================================================================================================================ '''
''' ============================ metodos para manejo de generacion/eliminacion dinamica de cordones y cotas ======================== '''



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
        cordon['num_cordones'].append(QLineEdit("0"))
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
    num_cordones = [QLineEdit("0") for _ in self.dynamic_cotas]
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

def print_dynamic_cordones_values(self):
    """Print the actual text content of QLineEdits in self.dynamic_cordones_arm_act."""
    for index, cordon in self.dynamic_cordones_arm_act.items():
        print(f"Cordon {index + 1}:")
        for i, num_cordon in enumerate(cordon['num_cordones']):
            print(f"  Num Cordones {i + 1}: {num_cordon.text()}")
        for i, tpi in enumerate(cordon['tpi']):
            print(f"  TPI {i + 1}: {tpi.text()}")




