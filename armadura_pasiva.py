import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel, QComboBox
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from PySide6.QtCore import Qt
from fn_database import db_tipos_arm_pasiva, db_materiales_arm_pasiva, db_usos_arm_pasiva
import math

def setup_armadura_pasiva(self):
    ''' Se ejecuta desde main cuando inicia app '''
    armpas_llenar_combo_ubicacion(self)
    armpas_llenar_combos_materiales(self)

    self.ui.tab3_btn_add_barras.clicked.connect(lambda: apasiva_add_barra_corrugada(self))
    self.ui.tab3_btn_del_barras.clicked.connect(lambda: apasiva_del_barra_corrugada(self))
    self.ui.tab3_btn_calcular.clicked.connect(lambda: apasiva_calcular(self))



def apasiva_calcular(self):
    ''' Solo imprime valores ingresados a campos dinamicos. No es necesario usar btn para anadir valores a calculo '''

    print("----------------  Datos Arm. Pasiva  ----------------")
    # for index, barra in enumerate(self.dynamic_apasiva_barras):
        # print(f"VALOR BARRA {barra}")
        # print(f"posicion: {barra['posicion'].text()}; Num_Min: {barra['n_min'].text()}; Diametro_min: {barra['diametro_min'].text()}")
    
    
    try:
        print("----------------  Areas Arm. Pasiva  ----------------")
        area_acumulada = 0
        area = 0

        for _, barra in enumerate(self.dynamic_apasiva_barras):
            area = float(barra['n_min'].text()) * pow((float(barra['diametro_min'].text())/2000), 2) * math.pi
            area_acumulada += area
            print(f"valor area en posicion: {barra['posicion'].text()} es = {area}")
            print(f"Valor de area acumulada = {area_acumulada}\n")
        
        area_acumulada = round(area_acumulada, 4)
        self.ui.tab3_line_area_barras.setText(f"{area_acumulada}")
    except:
        self.ui.tab3_line_area_barras.setText(f"{0}")
        print("Faltan datos para hacer calculo de area total de barras corrugadas. Valor por defecto 0.")

    
    try:
        print("----------------  Y_inf Arm. Pasiva  ----------------")
        ''' Se calculo igual que centro de gravedad inferior para armaduras activas peros in tpi porque esta armadura no se tensa.'''

        cant_barras = len(self.dynamic_apasiva_barras)
        print(f"cantidad de barras: {cant_barras}")

        numerador_acum = 0
        denominador_acum = 0

        for _, barra in enumerate(self.dynamic_apasiva_barras):
            numerador_barra_actual = (float(barra['n_min'].text()) * (float(barra['diametro_min'].text()) * float(barra['cota'].text())))
            numerador_acum += numerador_barra_actual

            print(f"Valor de barra actual numerador: {numerador_barra_actual}")

            denominador_barra_actual = (float(barra['n_min'].text()) * float(barra['diametro_min'].text()))
            denominador_acum += denominador_barra_actual
        
            print(f"Valor de barra actual denominador: {numerador_barra_actual}\n\n")


        cdg_barras = numerador_acum / denominador_acum
        print(f"resultado de CDG barras = {cdg_barras}")

        cdg_barras = round(cdg_barras, 4)
        self.ui.tab3_line_yinf_barras.setText(f"{cdg_barras}")
    except:
        cdg_barras = 0
        self.ui.tab3_line_yinf_barras.setText(f"{cdg_barras}")
        print(f"Faltan datos en barras corrugadas para hacer calculo de Y_inf. Se asigna por defecto Yinf = 0 para barras corrugadas !\n")

    
    try:
        print("----------------  Inercia Arm. Pasiva  ----------------")
        ''' primero se calcula la inercia de cada barra y luego se suman los resultados '''

        inercia_barra_especifica = 0
        inercia_total_barras = 0

        # Inercia por barra
        for _, barra in enumerate(self.dynamic_apasiva_barras):
            inercia_barra_especifica = math.pi * (pow((float(barra['diametro_min'].text())) / 1000, 4)) / 64

            print(f"Valor de inercia especifica barra actual: {inercia_barra_especifica}")

            inercia_total_barras += inercia_barra_especifica

            # print(f"Valor de inercia acumulada barras actual: {inercia_barra_especifica}\n\n")

        print("valor inercia total", inercia_total_barras)
        inercia_total_barras = round(inercia_total_barras, 6)
        print("valor inercia total", inercia_total_barras)
        self.ui.tab3_line_inercia_barras.setText(f"{inercia_total_barras}")
    except:
        self.ui.tab3_line_inercia_barras.setText(f"{0}")
        print("Faltan datos para hacer calculo de inercia para barras corrugadas. Valor por defecto 0.")









def armpas_llenar_combo_ubicacion(self):
    ''' Contenido fijo, Por lo tanto se hardcodea contenido'''

    self.ui.tab3_combo_ubicacion.addItem("Zona Central")
    self.ui.tab3_combo_ubicacion.addItem("Zona Extremos")
    self.ui.tab3_combo_ubicacion.addItem("Apoyo Total")
    self.ui.tab3_combo_ubicacion.addItem("Apoyo Media Madera")

def armpas_llenar_combos_materiales(self):
    ''' Contenido se obtiene de base de datos '''
    ''' Hay mas materiales en Jacena, Joaquin indida solo usar A63-42H, AT56-50H '''
    materiales_arm_pasiva = db_materiales_arm_pasiva()

    for i, tipo in enumerate(materiales_arm_pasiva):
        self.ui.tab3_combo_tipo_barras.addItem(f"{materiales_arm_pasiva[i][0]}")
        self.ui.tab3_combo_tipo_cercos.addItem(f"{materiales_arm_pasiva[i][0]}")
        self.ui.tab3_combo_tipo_mallas.addItem(f"{materiales_arm_pasiva[i][0]}")

def armpas_llenar_combo_usos(self, comboBox):
    ''' Contenido se obtiene de base de datos'''
    ''' Flexion, Cortante, Varios, Flexion Aleta, Cortante Aleta '''

    usos_arm_pasiva = db_usos_arm_pasiva()
    # print(f"Usos recuperados: {usos_arm_pasiva}\n\n")

    for j in range(len(usos_arm_pasiva)):
            comboBox.addItem(usos_arm_pasiva[j][0])

    # ''' Recorre todos las barras y asigna en comboBox tipos de uso '''
    # ''' Asigna tipos de usos a comboBox de uso en posicion 3 de Horizontal Layout (["uso"]) '''
    # for index, barra in enumerate(self.dynamic_apasiva_barras):
    #     barra = self.dynamic_apasiva_barras[index]

    #     for j in range(len(usos_arm_pasiva)):
     #         barra["uso"].addItem(usos_arm_pasiva[j][0])




def apasiva_add_barra_corrugada(self):
    ''' Anade una row de barra corrugada en su respectivo contenedor tab3_Vlayout_barras '''
    ''' Cada row (otras formas de referirse a row puede ser: fila, tuplas, posicion, barra) se compone de un HorizontalLayout con varios widgets predeterminados dentro'''
    ''' Se guarda referencia a estas barras generadas dinamicamente en una variable definida en main: self.dynamic_apasiva_barras'''
    
    ''' Maneja vertical stretcher para solo tener 1 y que siempre esté abajo '''    
    if self.ui.tab3_Vlayout_barras.count() > 0:  # Ensure there is at least one item
        last_item = self.ui.tab3_Vlayout_barras.itemAt(self.ui.tab3_Vlayout_barras.count() - 1)
        if last_item and last_item.spacerItem():  # Ensure it's a valid spacer
            item = self.ui.tab3_Vlayout_barras.takeAt(self.ui.tab3_Vlayout_barras.count() - 1)
            del item

    ''' Crea un nuevo HLayout para agregar elementos de nueva tupla '''
    layout = QHBoxLayout()
    
    ''' Crea los widgets para la fila '''

    line_pos1 = QLineEdit("0")
    combo_pos2 = QComboBox()
    line_pos3 = QLineEdit("0")
    line_pos4 = QLineEdit("0")
    line_pos5 = QLineEdit("0")
    line_pos6 = QLineEdit("0")
    line_pos7 = QLineEdit("0")
    line_pos8 = QLineEdit("0")

    ''' ajusta centrado '''
    line_pos1.setAlignment(Qt.AlignmentFlag.AlignCenter)
    # combo_pos2.setAlignment(Qt.AlignmentFlag.AlignCenter) # No aplica centrado de texto en ComboBox
    line_pos3.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_pos4.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_pos5.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_pos6.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_pos7.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_pos8.setAlignment(Qt.AlignmentFlag.AlignCenter)

    ''' Agrega componentes a layout horizontal '''
    layout.addWidget(line_pos1)
    layout.addWidget(combo_pos2)
    layout.addWidget(line_pos3)
    layout.addWidget(line_pos4)
    layout.addWidget(line_pos5)
    layout.addWidget(line_pos6)
    layout.addWidget(line_pos7)
    layout.addWidget(line_pos8)

    ''' Anade al final de diccionario la nueva barra '''
    self.dynamic_apasiva_barras.append({
        "posicion": line_pos1,
        "uso": combo_pos2,
        "n_min": line_pos3,
        "n_max": line_pos4,
        "diametro_min": line_pos5,
        "diametro_max": line_pos6,
        "cota": line_pos7,
        "longitud": line_pos8,
    })
    

    ''' Inserta horizontal layout recien generado a Vertical layout tab3_Vlayout_barras '''
    # self.ui.tab3_Vlayout_barras.insertLayout(0, layout)
    self.ui.tab3_Vlayout_barras.addLayout(layout)

    ''' Vuelve a insertar el vertical stretcher en la posición inferior del layout vertical '''
    self.ui.tab3_Vlayout_barras.addStretch()

    armpas_llenar_combo_usos(self, combo_pos2)



def apasiva_del_barra_corrugada(self):
    
    ''' Elimina el vertical stretcher temporalmente '''
    if self.ui.tab3_Vlayout_barras.itemAt(self.ui.tab3_Vlayout_barras.count() - 1).spacerItem():
        item = self.ui.tab3_Vlayout_barras.takeAt(self.ui.tab3_Vlayout_barras.count() - 1)
        del item  # Remove the stretcher
    
    if self.ui.tab3_Vlayout_barras.count() > 0:
        # Posicion de ultimo item en layout veretical
        last_index = self.ui.tab3_Vlayout_barras.count() - 1

        # Toma el último elemento (último layout añadido)
        last_item = self.ui.tab3_Vlayout_barras.takeAt(last_index) # Should be last element !

        # Comprueba que el item sea un layout antes de eliminarlo
        if last_item.layout():
            delete_layout_widgets(self, last_item.layout())  # Elimina los widgets dentro del layout primero
        del last_item  # Elimina el layout

        # Elimina referencia al layout dinámico (último visualmente)
        # self.dynamic_layouts.pop(0)  # Elimina el primer elemento de la lista de layouts dinámicos
        self.dynamic_apasiva_barras.pop()

        # Vuelve a agregar Vertical spacer
        self.ui.tab3_Vlayout_barras.addStretch()


''' Elimina los widgets dentro de un layout '''
def delete_layout_widgets(self, layout):
    # Iterate through all the widgets in the layout and delete them
    while layout.count():
        item = layout.takeAt(0)  # Take the first item
        if item.widget():  # If it's a widget, delete it
            item.widget().deleteLater()
        elif item.layout():  # If it's another layout, recursively delete its widgets
            self.delete_layout_widgets(item.layout())  # Recursive call to delete nested layouts



# def armpas_llenar_combo_usos(self):
#     ''' Contenido se obtiene de base de datos'''
#     ''' Flexion, Cortante, Varios, Flexion Aleta, Cortante Aleta '''

#     usos_arm_pasiva = db_usos_arm_pasiva()
#     # print(f"Usos recuperados: {usos_arm_pasiva}\n\n")

#     ''' Asigna tipos de usos a comboBox de uso en posicion 3 de Horizontal Layout (["uso"]) '''
#     for index, barra in enumerate(self.dynamic_apasiva_barras):
#         barra = self.dynamic_apasiva_barras[index]

#         for j in range(len(usos_arm_pasiva)):
            # barra["uso"].addItem(usos_arm_pasiva[j][0])

