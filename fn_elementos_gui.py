import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from fn_calculo_propiedades import *
from fn_update_gui import *
from fn_database import *

''' 
    Generacion y eliminacion de elementos dinamicos de ventana
'''


''' Genera de manera dinamica tuplas para trapecios '''
def generate_layout(self):
    # obtiene el numero de tuplas a generar de la spinbox 'spin_cant_agregar'
    num_rows = self.ui.spin_cant_agregar.value()
    print("debug_print> SpinBox Cantidad a generar value: ", num_rows) # Debug

    tuplas_existentes = self.historial_agregados

    ''' Loop to create the frames '''
    for i in range(num_rows):
        add_rows(self, self.historial_agregados + 1)


''' genera nuevo Hlayout (dinamico) y sus elementos, Los nombra correctamente y agrega a Vlayout contenedor (layout fijo)'''
def add_rows(self, index):
    
    ''' maneja vertical stretcher para solo tener 1 y que siempre este abajo'''
    if self.ui.layout_nuevas_row.itemAt(self.ui.layout_nuevas_row.count()-1).spacerItem():
        # item = ultimo que se encuentra (vertical stretcher)
        # Lo elimina mientras agrega nuevas tuplas, Lo vuelve a ingresar despues.
        item = self.ui.layout_nuevas_row.takeAt(self.ui.layout_nuevas_row.count()-1)
        del item
    
    ''' crea un nuevo Hlayout para agregar elementos de nueva tupla '''
    layout = QHBoxLayout()
    # Asigna nombre a layout generado dinamicamente
    layout_name = f"layout_t{index}"
    

    ''' Create the widgets for the row '''
    name_label = QLabel(f"T{index}\t    ")  # usa tab + 4 espacios( 1/2 tab) para coincidir, Aumenta el numero mostrado iterativamente
    bi_line = QLineEdit()
    bs_line = QLineEdit()
    altura_line = QLineEdit()
    area_line = QLineEdit()
    cg_line = QLineEdit()
    inercia_line = QLineEdit()
    op_line = QLineEdit()


    ''' Set object names to refer to them later '''
    name_label.setObjectName(f"t{index}_name")
    bi_line.setObjectName(f"t{index}_bs")
    bs_line.setObjectName(f"t{index}_bi")
    altura_line.setObjectName(f"t{index}_altura")
    area_line.setObjectName(f"t{index}_area")
    cg_line.setObjectName(f"t{index}_cg")
    inercia_line.setObjectName(f"t{index}_inercia")
    op_line.setObjectName(f"t{index}_op")

    ''' Make specific QLineEdits read-only '''
    # Resultados calculos
    area_line.setReadOnly(True)
    cg_line.setReadOnly(True)
    inercia_line.setReadOnly(True)
    op_line.setReadOnly(True)

    ''' Add the widgets to the layout '''
    layout.addWidget(name_label)
    layout.addWidget(bi_line)
    layout.addWidget(bs_line)
    layout.addWidget(altura_line)
    layout.addWidget(area_line)
    layout.addWidget(cg_line)
    layout.addWidget(inercia_line)
    layout.addWidget(op_line)

    ''' Add the layout to the vertical layout container '''
    # Este layout vertical esta bajo el layout horizontal predeterminado de T1.
    self.ui.layout_nuevas_row.addLayout(layout)

    ''' se vuelve a insertar vertical stretcher en posicion inferior de layout vertical '''
    self.ui.layout_nuevas_row.addStretch()

    # Store the layout reference to avoid duplicates
    # self.dynamic_layouts.append(layout) # Antiguo

    self.dynamic_layouts.append({
        "bi_line": bi_line,
        "bs_line": bs_line,
        "altura_line": altura_line,
        "area_line": area_line,
        "cg_line": cg_line,
        "inercia_line": inercia_line,
        "op_line": op_line,
    })
    
    # self.historial_agregados.append(name_label) # Originalmente se guardaba informacion de Label de cada nueva row, Ahora solo se usa un contador += 1
    self.historial_agregados += 1


def confirmar_borrar(self, index):
    # Pide confirmacion de usuario antes de borrar layouts
    reply = QMessageBox.question(self, 'Confirmar', 
                                "Confirmar acción?", 
                                QMessageBox.Yes  | QMessageBox.No, 
                                QMessageBox.No)
    # Opcion si/no, Y opcion por defecto es NO
    if reply == QMessageBox.No:
        return 0
    else:
        del_rows(self, index)
    

''' Elimina tuplas que fueron creadas dinamicamente dentro del layout vertical '''
def del_rows(self, index):
    print("DEBUG del_rows() > valor de Index: ", index)
    
    # Determina cuantos borrar, una MIN para asegurar no intentar borrar mas de lo que existe
    num_rows = min(index, self.historial_agregados)
    if num_rows == 0:
        return

    print("DEBUG - del_rows > Cantidad a eliminar value: ", num_rows)  # Debug

    ''' Elimina Vertical stretcher temporalmente '''
    if self.ui.layout_nuevas_row.itemAt(self.ui.layout_nuevas_row.count() - 1).spacerItem():
        item = self.ui.layout_nuevas_row.takeAt(self.ui.layout_nuevas_row.count() - 1)
        del item  # Remove the stretcher


    ''' Itera para eliminar layouts y referencias a layouts'''
    for _ in range(num_rows):
        if self.ui.layout_nuevas_row.count() > 0:
            last_item = self.ui.layout_nuevas_row.takeAt(self.ui.layout_nuevas_row.count() - 1)


            # Comprueba que el item sea un layout (Pero siempre deberia ser)
            if last_item.layout():
                delete_layout_widgets(self, last_item.layout())  # Elimina los widgets dentro del layout primero
            del last_item  # Elimina layout

            # Elimina referencia del layout dinamico
            self.dynamic_layouts.pop()  # elimina el mas reciente

    # Se disminuye contador de dinamicos existes
    self.historial_agregados -= num_rows

    # Vuelve a agregar stretcher al final para pegar LineEdits a borde superior
    self.ui.layout_nuevas_row.addStretch()


''' Elimina los widgets dentro de un layout '''
def delete_layout_widgets(self, layout):
    # Iterate through all the widgets in the layout and delete them
    while layout.count():
        item = layout.takeAt(0)  # Take the first item
        if item.widget():  # If it's a widget, delete it
            item.widget().deleteLater()
        elif item.layout():  # If it's another layout, recursively delete its widgets
            self.delete_layout_widgets(item.layout())  # Recursive call to delete nested layouts


''' hace gen/del de layouts dinamicamente para hacerlos coincidir con la cantidad de trapecios que usa la pieza '''
def ajustar_layouts_dinamicos(self, cantidad_trapecios):
    # Tipo boton: 0: Cambia seccion, 1: Cambia pieza
    # Usa 99 para eliminar layouts para eliminar todos los layouts existentes (No hay caso de uso en el que se necesitan mas de 99 secciones para una pieza)
    print("DEBUG - ajustar_layouts_dinamicos > valor cantidad_trapecios: ", cantidad_trapecios)
    del_rows(self, 99) # No pide confirmacion

    ''' Loop to create the frames '''
    for i in range(cantidad_trapecios):
        add_rows(self, self.historial_agregados + 1)


''' >>>> Usa pieza de catalogo seleccionada con comboBoxes <<<< '''

''' Settea la cantidad correcta de layout dinamicos en layout dinamico '''
''' tipo_boton -> 0: usa btn seccion (No pide confirmacion), 1: usa btn pieza (Pide confirmacion) '''
def aplicar_pieza_catalogo(self):
    # Determina la pieza seleccionada
    pieza_familia = self.ui.combo_familia.currentText()
    pieza_modelo = self.ui.combo_modelo.currentText()
    pieza_seccion = self.ui.combo_tipo_seccion.currentText()
    print("debug_print> Pieza seleccionada, Familia: ", pieza_familia, " - Modelo: ", pieza_modelo, " - Tipo seccion: ", pieza_seccion) # Debug

    if not pieza_modelo:
        print("Debug: No se selecciona ninguna pieza/modelo")
        return

    ''' Obtiene informacion de pieza '''        
    # Obtiene Primary Key de la pieza (ID)
    pieza_id = db_get_id_pieza(pieza_familia, pieza_modelo)
    
    # Usa tabla Parametros de DB
    trapecios_necesarios = db_get_cant_trapecios(pieza_id, pieza_seccion)

    # Obtiene informacion (dimensiones) de los trapecios de la seccion consultando tabla Trapecios
    pieza_trapecios = db_get_datos_trapecios(pieza_id, pieza_seccion)

    ''' asigna valores fijos (dimensiones) a layouts dinamicos '''
    # iguala la cantidad de layouts dinamicos a la cantidad necesaria
    ajustar_layouts_dinamicos(self, trapecios_necesarios)

    # Aplicar dimensione de trapecios a campos        
    aplicar_dimensiones_pieza(self, pieza_trapecios)


    '''   Funciones de calculo  '''
    ''' Area, Centro de Gravedad, Inercia, Sumatoria area, Suma Producto (area, Cg / SUM(area)), OP '''

    # Calcula cada variable
    valores_areas = calcular_area(pieza_trapecios)
    altura_acumulada = calcular_altura_acumulada(pieza_trapecios)
    valores_inercia = calcular_inercia(pieza_trapecios)
    valores_cg = calcular_centro_gravedad(pieza_trapecios)
    suma_areas = calcular_suma_areas(valores_areas)
    producto_ponderado = calcular_producto_ponderado(valores_areas, valores_cg, suma_areas)
    valores_op = calcular_op(valores_areas, valores_cg, valores_inercia, producto_ponderado)


    print("DEBUG aplicar_pieza_catalogo() -- producto_ponderado: ", producto_ponderado)
    # Aplica resultados a layouts dinamicos + layouts fijos
    aplicar_valores_calculados(self, valores_areas, valores_cg, valores_inercia, valores_op, suma_areas, altura_acumulada, producto_ponderado)