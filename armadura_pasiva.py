import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel, QComboBox
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from PySide6.QtCore import Qt
from fn_database import db_tipos_arm_pasiva, db_materiales_arm_pasiva


def setup_armadura_pasiva(self):
    ''' Se ejecuta desde main cuando inicia app '''
    armpas_llenar_combo_ubicacion(self)
    armpas_llenar_combos_materiales(self)

    self.ui.tab3_btn_add_barras.clicked.connect(lambda: apasiva_add_barra_corrugada(self))




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


''' ====== '''
''' STRCUTURE WANTED FOR EACH ROW (BARRA CORRUGADA '''
''' tab3_horizontal_layout would be the name of the horizontal layout being added to the vertical layout. It doesnt need that name, Because its reference will be stored in a variable'''
''' tab3_Vlayout_barras is the VerticalLayout that will contain all the other HorizontalLayouts for each Barra Corrugada. The Equivalent in the example code is self.ui.layout_nuevas_row '''



''' 
self.tab3_horizontal_layout = QHBoxLayout()
self.tab3_horizontal_layout.setObjectName(u"tab3_horizontal_layout")
    
    self.tab3_line_pos1 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos1.setObjectName(u"tab3_line_pos1")
    self.tab3_line_pos1.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos1)

    self.tab3_combo_pos2 = QComboBox(self.verticalLayoutWidget_2)
    self.tab3_combo_pos2.addItem("")
    self.tab3_combo_pos2.setObjectName(u"tab3_combo_pos2")

    self.tab3_horizontal_layout.addWidget(self.tab3_combo_pos2)

    self.tab3_line_pos3 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos3.setObjectName(u"tab3_line_pos3")
    self.tab3_line_pos3.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos3)

    self.tab3_line_pos4 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos4.setObjectName(u"tab3_line_pos4")
    self.tab3_line_pos4.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos4)

    self.tab3_line_pos5 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos5.setObjectName(u"tab3_line_pos5")
    self.tab3_line_pos5.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos5)

    self.tab3_line_pos6 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos6.setObjectName(u"tab3_line_pos6")
    self.tab3_line_pos6.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos6)

    self.tab3_line_pos7 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos7.setObjectName(u"tab3_line_pos7")
    self.tab3_line_pos7.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos7)

    self.tab3_line_pos8 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos8.setObjectName(u"tab3_line_pos8")
    self.tab3_line_pos8.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos8)

self.tab3_Vlayout_barras.addLayout(self.tab3_horizontal_layout)
'''



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

    line_pos1 = QLineEdit()
    line_pos2 = QLineEdit()
    combo_pos3 = QComboBox()
    line_pos4 = QLineEdit()
    line_pos5 = QLineEdit()
    line_pos6 = QLineEdit()
    line_pos7 = QLineEdit()
    line_pos8 = QLineEdit()

    ''' ajusta centrado '''
    line_pos1.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_pos2.setAlignment(Qt.AlignmentFlag.AlignCenter)
    # combo_pos3.setAlignment(Qt.AlignmentFlag.AlignCenter) # No aplica centrado de texto en ComboBox
    line_pos4.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_pos5.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_pos6.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_pos7.setAlignment(Qt.AlignmentFlag.AlignCenter)
    line_pos8.setAlignment(Qt.AlignmentFlag.AlignCenter)

    ''' Agrega componentes a layout horizontal '''
    layout.addWidget(line_pos1)
    layout.addWidget(line_pos2)
    layout.addWidget(combo_pos3)
    layout.addWidget(line_pos4)
    layout.addWidget(line_pos5)
    layout.addWidget(line_pos6)
    layout.addWidget(line_pos7)
    layout.addWidget(line_pos8)
    

    ''' Inserta horizontal layout recien generado a Vertical layout tab3_Vlayout_barras '''
    self.ui.tab3_Vlayout_barras.insertLayout(0, layout)

    ''' Vuelve a insertar el vertical stretcher en la posición inferior del layout vertical '''
    self.ui.tab3_Vlayout_barras.addStretch()




''' ================================================================================================================================================ '''
''' ================================================================================================================================================ '''
''' ================================================================================================================================================ '''
'''                                                             REFERENCIA                                                                           '''
''' ================================================================================================================================================ '''
''' ================================================================================================================================================ '''
''' ================================================================================================================================================ '''
# ''' genera nuevo Hlayout (dinamico) y sus elementos, Los nombra correctamente y agrega a Vlayout contenedor (layout fijo)'''
# def add_rows(self, index):
#     ''' Maneja vertical stretcher para solo tener 1 y que siempre esté abajo '''
#     if self.ui.layout_nuevas_row.itemAt(self.ui.layout_nuevas_row.count() - 1).spacerItem():
#         # Elimina el último item si es el vertical stretcher
#         item = self.ui.layout_nuevas_row.takeAt(self.ui.layout_nuevas_row.count() - 1)
#         del item

#     ''' Crea un nuevo HLayout para agregar elementos de nueva tupla '''
#     layout = QHBoxLayout()

#     ''' Crea los widgets para la fila '''
#     name_label = QLabel(f"T{index}\t    ")  # Usa tab + 4 espacios para coincidir
#     bi_line = QLineEdit()
#     bs_line = QLineEdit()
#     altura_line = QLineEdit()
#     area_line = QLineEdit()
#     cg_line = QLineEdit()
#     inercia_line = QLineEdit()
#     op_line = QLineEdit()

#     ''' Configura nombres de objetos para referencia futura '''
#     name_label.setObjectName(f"t{index}_name")
#     bi_line.setObjectName(f"t{index}_bi")
#     bs_line.setObjectName(f"t{index}_bs")
#     altura_line.setObjectName(f"t{index}_altura")
#     area_line.setObjectName(f"t{index}_area")
#     cg_line.setObjectName(f"t{index}_cg")
#     inercia_line.setObjectName(f"t{index}_inercia")
#     op_line.setObjectName(f"t{index}_op")

#     ''' Haz que ciertos QLineEdits sean de solo lectura '''
#     area_line.setReadOnly(True)
#     cg_line.setReadOnly(True)
#     inercia_line.setReadOnly(True)
#     op_line.setReadOnly(True)

#     ''' Agrega los widgets al layout '''
#     layout.addWidget(name_label)
#     layout.addWidget(bi_line)
#     layout.addWidget(bs_line)
#     layout.addWidget(altura_line)
#     layout.addWidget(area_line)
#     layout.addWidget(cg_line)
#     layout.addWidget(inercia_line)
#     layout.addWidget(op_line)

#     ''' Inserta el layout al principio del contenedor vertical '''
#     self.ui.layout_nuevas_row.insertLayout(0, layout)  # Change to insertLayout to add at the top

#     ''' Vuelve a insertar el vertical stretcher en la posición inferior del layout vertical '''
#     self.ui.layout_nuevas_row.addStretch()

#     ''' Guarda la referencia al layout dinámico '''
#     self.dynamic_layouts.insert(0, {  # Use insert(0, ...) to maintain inverted order in the list
#         "bi_line": bi_line,
#         "bs_line": bs_line,
#         "altura_line": altura_line,
#         "area_line": area_line,
#         "cg_line": cg_line,
#         "inercia_line": inercia_line,
#         "op_line": op_line,
#     })

#     ''' Incrementa el contador de filas creadas dinámicamente '''
#     self.historial_agregados += 1





# ''' Elimina trapecio seleccionado en ListWidget '''
# def del_rows(self):
#     """ Deletes the corresponding row from VLayout based on the label text. """
    
#     try:
#         trapecio_para_borrar = self.ui.tab1_list_trapecios_existentes.currentItem().text()
#     except:
#         print("Error: No hay ningun trapecio seleccionado para eliminar.")
#         return
#     # Find the matching row dynamically
#     row_to_delete = None
#     for row in self.dynamic_layouts:

#         if row["name_label"].text().strip() == trapecio_para_borrar:
#             row_to_delete = row
#             break

#     if not row_to_delete:
#         print(f"Error: Could not find row with label {trapecio_para_borrar}")
#         return

#     # Remove the row's layout from the VLayout
#     for i in range(self.ui.layout_nuevas_row.count()):
#         item = self.ui.layout_nuevas_row.itemAt(i)
#         if isinstance(item, QHBoxLayout) and row_to_delete["name_label"] in [item.itemAt(j).widget() for j in range(item.count())]:
#             layout_to_remove = self.ui.layout_nuevas_row.takeAt(i)
#             # Delete all widgets inside the layout
#             while layout_to_remove.count():
#                 item = layout_to_remove.takeAt(0)
#                 widget = item.widget()
#                 if widget:
#                     widget.deleteLater()  # Ensure Qt properly removes it
#             del layout_to_remove
#             break

#     # Remove from tracking list
#     self.dynamic_layouts.remove(row_to_delete)
#     self.historial_agregados -= 1
#     self.ui.tab1_list_trapecios_existentes.takeItem(int(trapecio_para_borrar[1])-1)


#     self.ui.tab1_list_trapecios_existentes.clear()
#     for index, row in enumerate(reversed(self.dynamic_layouts)):
#         # Ajusta name_label de todos los trapecios
#         row["name_label"].setText(f"T{index+1}\t    ")

#         # Agrega name_label de trapecio a LIST para luego poder seleccionalo y borrarlo
#         self.ui.tab1_list_trapecios_existentes.addItem(f"T{index+1}")



#     print(f"Se elimina trapecio correctamente")