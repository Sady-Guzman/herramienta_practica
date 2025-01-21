import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from fn_calculo_propiedades import *
from fn_update_gui import *
from fn_database import *
from fn_crear_pieza import open_crear_pieza_dialog

''' 
    Generacion y eliminacion de elementos dinamicos de ventana
'''


''' Genera de manera dinamica tuplas para trapecios '''
def generate_layout(self):
    # obtiene el numero de tuplas a generar de la spinbox 'spin_cant_agregar'
    num_rows = self.ui.spin_cant_agregar.value()
    # num_rows = 1 # BTN actua como agregar trapecios de Jacena en vez de usar spinBox
    print("debug_print> SpinBox Cantidad a generar value: ", num_rows) # Debug
    tuplas_existentes = self.historial_agregados

    ''' Loop to create the frames '''
    for i in range(num_rows):
        add_rows(self, self.historial_agregados + 1)


''' genera nuevo Hlayout (dinamico) y sus elementos, Los nombra correctamente y agrega a Vlayout contenedor (layout fijo)'''
def add_rows(self, index):
    ''' Maneja vertical stretcher para solo tener 1 y que siempre esté abajo '''
    if self.ui.layout_nuevas_row.itemAt(self.ui.layout_nuevas_row.count() - 1).spacerItem():
        # Elimina el último item si es el vertical stretcher
        item = self.ui.layout_nuevas_row.takeAt(self.ui.layout_nuevas_row.count() - 1)
        del item

    ''' Crea un nuevo HLayout para agregar elementos de nueva tupla '''
    layout = QHBoxLayout()
    # Asigna nombre al layout generado dinámicamente
    layout_name = f"layout_t{index}"

    ''' Crea los widgets para la fila '''
    name_label = QLabel(f"T{index}\t    ")  # Usa tab + 4 espacios para coincidir
    bi_line = QLineEdit()
    bs_line = QLineEdit()
    altura_line = QLineEdit()
    area_line = QLineEdit()
    cg_line = QLineEdit()
    inercia_line = QLineEdit()
    op_line = QLineEdit()

    ''' Configura nombres de objetos para referencia futura '''
    name_label.setObjectName(f"t{index}_name")
    bi_line.setObjectName(f"t{index}_bi")
    bs_line.setObjectName(f"t{index}_bs")
    altura_line.setObjectName(f"t{index}_altura")
    area_line.setObjectName(f"t{index}_area")
    cg_line.setObjectName(f"t{index}_cg")
    inercia_line.setObjectName(f"t{index}_inercia")
    op_line.setObjectName(f"t{index}_op")

    ''' Haz que ciertos QLineEdits sean de solo lectura '''
    area_line.setReadOnly(True)
    cg_line.setReadOnly(True)
    inercia_line.setReadOnly(True)
    op_line.setReadOnly(True)

    ''' Agrega los widgets al layout '''
    layout.addWidget(name_label)
    layout.addWidget(bi_line)
    layout.addWidget(bs_line)
    layout.addWidget(altura_line)
    layout.addWidget(area_line)
    layout.addWidget(cg_line)
    layout.addWidget(inercia_line)
    layout.addWidget(op_line)

    ''' Inserta el layout al principio del contenedor vertical '''
    self.ui.layout_nuevas_row.insertLayout(0, layout)  # Change to insertLayout to add at the top

    ''' Vuelve a insertar el vertical stretcher en la posición inferior del layout vertical '''
    self.ui.layout_nuevas_row.addStretch()

    ''' Guarda la referencia al layout dinámico '''
    self.dynamic_layouts.insert(0, {  # Use insert(0, ...) to maintain inverted order in the list
        "bi_line": bi_line,
        "bs_line": bs_line,
        "altura_line": altura_line,
        "area_line": area_line,
        "cg_line": cg_line,
        "inercia_line": inercia_line,
        "op_line": op_line,
    })

    ''' Incrementa el contador de filas creadas dinámicamente '''
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
    # print("DEBUG del_rows() > valor de Index: ", index)
    
    # Determina cuántos borrar, usando min() para asegurar que no intente borrar más de lo que existe
    num_rows = min(index, self.historial_agregados)
    if num_rows == 0:
        return

    # print("DEBUG - del_rows > Cantidad a eliminar value: ", num_rows)  # Debug

    ''' Elimina el vertical stretcher temporalmente '''
    if self.ui.layout_nuevas_row.itemAt(self.ui.layout_nuevas_row.count() - 1).spacerItem():
        item = self.ui.layout_nuevas_row.takeAt(self.ui.layout_nuevas_row.count() - 1)
        del item  # Remove the stretcher

    ''' Itera para eliminar layouts de forma inversa '''
    for _ in range(num_rows):
        if self.ui.layout_nuevas_row.count() > 0:
            # Toma el último elemento (último layout añadido)
            last_item = self.ui.layout_nuevas_row.takeAt(0)  # Cambiar a `0` para eliminar el primer elemento (último visualmente debido a la inversión)

            # Comprueba que el item sea un layout antes de eliminarlo
            if last_item.layout():
                delete_layout_widgets(self, last_item.layout())  # Elimina los widgets dentro del layout primero
            del last_item  # Elimina el layout

            # Elimina referencia al layout dinámico (último visualmente)
            self.dynamic_layouts.pop(0)  # Elimina el primer elemento de la lista de layouts dinámicos

    # Decrementa el contador de layouts dinámicos existentes
    self.historial_agregados -= num_rows

    # Vuelve a agregar el vertical stretcher al final para mantener la estructura
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

# TODO implementar FLAG true/false para caso de uso
# TRUE -> Uso normal, aplica pieza/seccion catalogo usando id_DB
# FALSE -> Uso para pieza temporal. No hace query a DB

# def aplicar_pieza(self, es_temporal):
#     if es_temporal == False:
#         aplicar_pieza_catalogo(self)
#     else:
#         aplicar_pieza_temporal(self)



def aplicar_pieza_temporal(self):
    print("DEBUG app_pie_temp -> Se aplica seccion pieza temporal")

    # Store data from current dynamic layouts before switching sections
    self.store_dynamic_layout_data()

    # Retrieve the selected family and model
    familia = self.ui.combo_familia.currentText()
    modelo = self.ui.combo_modelo.currentText()

    # Ensure there is a selection in the list widget
    if not familia or not modelo:
        print("Debug: No family or model selected.")
        return

    # Retrieve the number of sections
    cantidad_secciones = len(self.dynamic_layouts)

    # Repopulate the dynamic layouts with stored data
    self.repopulate_dynamic_layouts(cantidad_secciones)


def aplicar_pieza_de_db(self, es_creada, dynamic_layout_data):
    # Retrieve selected family, model, and section type
    pieza_familia = self.ui.combo_familia.currentText()
    pieza_modelo = self.ui.combo_modelo.currentText()

    # Get the selected item from the ListWidget
    pieza_seccion_item = self.ui.list_tipo_seccion.currentItem()

    # Ensure there is a selection in the list widget
    if pieza_seccion_item is None:
        print("error debug aplicar_pieza_seleccion(): No section selected in the ListWidget.")
        return

    pieza_seccion = pieza_seccion_item.text()
    print("aplicar_pieza_de_db() --> Pieza seleccionada, Familia: ", pieza_familia, " - Modelo: ", pieza_modelo, " - Tipo seccion: ", pieza_seccion, "\n")  # Debug

    if not pieza_modelo:
        print("error debug aplicar_pieza_seleccion(): No se selecciona ninguna pieza/modelo")
        return

    print(" aplicar_pieza_de_db() AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ---> valor de es_creada: ", es_creada, "\n")


    ''' obtiene ID de pieza, dependiendo de la base de datos '''
    pieza_id = db_get_id_pieza(pieza_familia, pieza_modelo, es_creada)

    # Usa tabla Parametros de DB
    trapecios_necesarios = db_get_cant_trapecios(pieza_id, pieza_seccion, es_creada)

    # Obtiene informacion (dimensiones) de los trapecios de la seccion consultando tabla Trapecios
    pieza_trapecios = db_get_datos_trapecios(pieza_id, pieza_seccion, es_creada)
    print(" aplicar_pieza_de_db() BBBBBBBBBBBBBBBBBBBBBBBBBBBB: valor pieza_trapecios: ", pieza_trapecios, "\n")
    print("\n\n")

    ''' Asigna valores fijos (dimensiones) a layouts dinamicos '''
    # Iguala la cantidad de layouts dinamicos a la cantidad necesaria
    ajustar_layouts_dinamicos(self, trapecios_necesarios)

    # Aplica dimensiones de trapecios a campos        
    aplicar_dimensiones_pieza(self, pieza_trapecios)

    ''' Carga las dimensiones todas las secciones en lista dinamica para poder editar piezas que ya fueron creadas y guardadas en DB '''

    ''' Store the values of all sections (secciones) '''
    self.dynamic_layout_data = db_get_all_trapecios_data(pieza_id, es_creada)
    print("aplicar_pieza_de_db () CCCCCCCCCCCCCCCCCCCCCCCCCCC --> values secciones_data: ", self.dynamic_layout_data, "\n")
    print("\n\n")

    ''' Usa valores dinamicamente agregados a LineEdits para hacer calculos y asignarlos '''
    calcular_nuevos_valores(self)




def aplicar_pieza_de_dynamic(self, dynamic_layout_data):
    # Igual a aplicar_pieza_de_db(), Pero en vez de sacar los datos de la base de datos, los obtiene de self.dynamic_layout_data
    print("entra a aplicar_pieza_de_dynamic\n")
    print(f"aplicar_pieza_de_dynamic() --> El contenido dentro de dynamic_layout_data es: {self.dynamic_layout_data} \n\n")

    # Corresponde a la seccion seleccionada
    pieza_seccion_item = self.ui.list_tipo_seccion.currentItem()
    
    # Ensure there is a selection in the list widget
    if pieza_seccion_item is None:
        print("error debug aplicar_pieza_de_dynamic(): No section selected in the ListWidget.")
        return
    pieza_seccion = pieza_seccion_item.text()

    # Obtiene y ajusta la cantidad de trapecios para la seccion seleccionada
    trapecios_necesarios = len(self.dynamic_layout_data[pieza_seccion])
    print(f"aplicar_pieza_de_dynamic() --> len de dict: {trapecios_necesarios}")
    ajustar_layouts_dinamicos(self, trapecios_necesarios)

    # pieza_trapecios = db_get_datos_trapecios(pieza_id, pieza_seccion, es_creada)
    pieza_trapecios = self.dynamic_layout_data[pieza_seccion]
    print(f"aplicar_pieza_de_dynamic() --> trapecios para seccion en dict: {pieza_trapecios}")
    aplicar_dimensiones_pieza_dynamic(self, pieza_trapecios)


    calcular_nuevos_valores(self)












''' ============================================================================================================================ '''

''' funcion para manejar informacion ingresada por usuario en VENTANA CREACION PIEZA '''
def handle_crear_pieza(self):
    ''' Handles the logic when the "Crear Pieza" button is clicked '''
    # Open the dialog and capture the result data
    result_data = open_crear_pieza_dialog(self)

    if result_data:
        # The dialog was accepted, and result_data is returned
        print("handle_crear_pieza() --> Data from CrearPiezaDialog:", result_data, "\n")


        # Example: Process the result_data
        familia = result_data["familia"]
        modelo = result_data["modelo"]
        cantidad_secciones = result_data["cantidad_secciones"]
        secciones = result_data["secciones"]


        ''' print checkear contedino entregado por ventana de crear_pieza '''
        print(f"handle_crear_pieza() -> Familia: {familia}, Modelo: {modelo}, Cantidad de Secciones: {cantidad_secciones}")
        print("Secciones:")
        for index, seccion in enumerate(secciones, start=1):
            print(f"  Sección {index}: {seccion}")

        ''' Poblar ComboBoxes Familia/Modelo, Lista secciones '''
        poblar_datos_pieza_temporal(self, familia, modelo, secciones)


        self.es_temporal = True # Se usa para saber que comportamiento darle a btn acpt_tipo_seccion
    else:
        # The dialog was canceled
        print("No data returned. Dialog was canceled.")