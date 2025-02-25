import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel, QComboBox
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from fn_calculo_propiedades import *
from fn_update_gui import *
from fn_database import *
from fn_crear_pieza import open_crear_pieza_dialog

''' 
    Generacion y eliminacion de elementos dinamicos de pestana geometria
'''


''' Genera de manera dinamica tuplas para trapecios '''
def generate_layout(self):
    # obtiene el numero de tuplas a generar de la spinbox 'spin_cant_agregar'
    num_rows = 1
    # num_rows = 1 # BTN actua como agregar trapecios de Jacena en vez de usar spinBox
    # print("debug_print> SpinBox Cantidad a generar value: ", num_rows) # Debug
    # tuplas_existentes = self.historial_agregados

    ''' Loop to create the frames '''
    for i in range(num_rows):
        add_rows(self, self.historial_agregados + 1)

''' Comprueba tipo de hormigon en tab GEOMETRIA '''
def on_combo_changed(self, combo_box, index):
    ''' Funcion para manejar respuesta de ComboBoxes dinamicamente generadas en TAB GEOMETRIA. NORMAL / INSITU '''
    # Mensaje para comprobar en terminal cambio
    # print(f"🔄 ComboBox in row {index} changed to: {combo_box.currentText()}")


    # Find the row dictionary in dynamic_layouts
    row_data = next((row for row in self.dynamic_layouts if row["name_label"].objectName() == f"t{index}_name"), None)
    
    if row_data:
        is_insitu = combo_box.currentText() == "Insitu"

        # Para secciones insitu se tiene siempre mismo ancho en base sup y base inf. No se le calcula propiedades.

        # row_data["bi_line"].setDisabled(is_insitu) # Se mantiene solo un campo de ancho porque bloques INSITU siempre tienen mismo ancho inf y sup
        row_data["bs_line"].setDisabled(is_insitu)
        # row_data["altura_line"].setDisabled(is_insitu) # Altura no se desactiva
        row_data["area_line"].setDisabled(is_insitu)
        row_data["cg_line"].setDisabled(is_insitu)
        row_data["op_line"].setDisabled(is_insitu)

        row_data["bs_line"].setText("")
        row_data["area_line"].setText("")
        row_data["cg_line"].setText("")
        row_data["op_line"].setText("")


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
    name_label = QLabel(f"T{index}    ")  # Usa  + 4 espacios para coincidir --> OJO en del_rows. Tambien se cambia label de row
    bi_line = QLineEdit()
    bs_line = QLineEdit()
    altura_line = QLineEdit()
    area_line = QLineEdit()
    cg_line = QLineEdit()
    inercia_line = QLineEdit()
    op_line = QLineEdit()
    combo_insitu = QComboBox()

    ''' Configura nombres de objetos para referencia futura '''
    name_label.setObjectName(f"t{index}_name")
    bi_line.setObjectName(f"t{index}_bi")
    bs_line.setObjectName(f"t{index}_bs")
    altura_line.setObjectName(f"t{index}_altura")
    area_line.setObjectName(f"t{index}_area")
    cg_line.setObjectName(f"t{index}_cg")
    inercia_line.setObjectName(f"t{index}_inercia")
    op_line.setObjectName(f"t{index}_op")
    combo_insitu.setObjectName(f"t{index}_insitu")

    ''' ciertos QLineEdits son de solo lectura '''
    area_line.setReadOnly(True)
    cg_line.setReadOnly(True)
    inercia_line.setReadOnly(True)
    op_line.setReadOnly(True)

    ''' Agrega opciones a comboBox insitu '''
    combo_insitu.addItem("Normal")
    combo_insitu.addItem("Insitu")

    ''' Agrega los widgets al layout '''
    layout.addWidget(name_label)
    layout.addWidget(bi_line)
    layout.addWidget(bs_line)
    layout.addWidget(altura_line)
    layout.addWidget(area_line)
    layout.addWidget(cg_line)
    layout.addWidget(inercia_line)
    layout.addWidget(op_line)
    layout.addWidget(combo_insitu)

    ''' Inserta el layout al principio del contenedor vertical '''
    self.ui.layout_nuevas_row.insertLayout(0, layout)  # Change to insertLayout to add at the top

    ''' Vuelve a insertar el vertical stretcher en la posición inferior del layout vertical '''
    self.ui.layout_nuevas_row.addStretch()


    ''' Connect comboBox signal dynamically '''
    # combo_insitu.currentIndexChanged.connect(lambda _, cb=combo_insitu, i=index: self.on_combo_changed(cb, i)) # Para saber si cambia tipo hormigon en Combo
    combo_insitu.currentIndexChanged.connect(lambda _, cb=combo_insitu, i=index: on_combo_changed(self, cb, i))

    ''' Guarda la referencia al layout dinámico '''
    self.dynamic_layouts.insert(0, {  # Use insert(0, ...) to maintain inverted order in the list
        "bi_line": bi_line,
        "bs_line": bs_line,
        "altura_line": altura_line,
        "area_line": area_line,
        "cg_line": cg_line,
        "inercia_line": inercia_line,
        "op_line": op_line,
        "name_label": name_label, # Para identificar trapecios
        "combo_insitu": combo_insitu, # Para identificar tipo de hormigon usado.
    })

    ''' Incrementa el contador de filas creadas dinámicamente '''
    self.historial_agregados += 1

    ''' Agrega name_label de trapecio a LIST para luego poder seleccionalo y borrarlo '''
    self.ui.tab1_list_trapecios_existentes.addItem(f"T{index}")


''' mensaje POP UP '''
def confirmar_borrar(self):
    # Pide confirmacion de usuario antes de borrar layouts
    reply = QMessageBox.question(self, 'Confirmar', 
                                "Confirmar acción?", 
                                QMessageBox.Yes  | QMessageBox.No, 
                                QMessageBox.No)
    # Opcion si/no, Y opcion por defecto es NO
    if reply == QMessageBox.No:
        return 0
    else:
        del_rows(self)
    


''' Elimina trapecio seleccionado en ListWidget '''
def del_rows(self):
    """ Deletes the corresponding row from VLayout based on the label text. """
    
    try:
        trapecio_para_borrar = self.ui.tab1_list_trapecios_existentes.currentItem().text()
    except:
        print("Error: No hay ningun trapecio seleccionado para eliminar.")
        return
    # Find the matching row dynamically
    row_to_delete = None
    for row in self.dynamic_layouts:

        if row["name_label"].text().strip() == trapecio_para_borrar:
            row_to_delete = row
            break

    if not row_to_delete:
        print(f"Error: Could not find row with label {trapecio_para_borrar}")
        return

    # Remove the row's layout from the VLayout
    for i in range(self.ui.layout_nuevas_row.count()):
        item = self.ui.layout_nuevas_row.itemAt(i)
        if isinstance(item, QHBoxLayout) and row_to_delete["name_label"] in [item.itemAt(j).widget() for j in range(item.count())]:
            layout_to_remove = self.ui.layout_nuevas_row.takeAt(i)
            # Delete all widgets inside the layout
            while layout_to_remove.count():
                item = layout_to_remove.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()  # Ensure Qt properly removes it
            del layout_to_remove
            break

    # Remove from tracking list
    self.dynamic_layouts.remove(row_to_delete)
    self.historial_agregados -= 1
    self.ui.tab1_list_trapecios_existentes.takeItem(int(trapecio_para_borrar[1])-1)


    self.ui.tab1_list_trapecios_existentes.clear()
    for index, row in enumerate(reversed(self.dynamic_layouts)):
        # Ajusta name_label de todos los trapecios
        row["name_label"].setText(f"T{index+1}    ")

        # Agrega name_label de trapecio a LIST para luego poder seleccionalo y borrarlo
        self.ui.tab1_list_trapecios_existentes.addItem(f"T{index+1}")



    print(f"Se elimina trapecio correctamente")



''' Elimina tuplas que fueron creadas dinamicamente dentro del layout vertical '''
def del_all_trapecios(self):
    index = 99 # Se asegura de borrar todos los trapecios
    
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
    # print("ajustar_layouts_dinamicos() -> valor cantidad_trapecios: ", cantidad_trapecios)
    # del_rows(self, 99) # No pide confirmacion
    del_all_trapecios(self)

    ''' Loop to create the frames '''
    for i in range(cantidad_trapecios):
        add_rows(self, self.historial_agregados + 1)


''' >>>> Usa pieza de catalogo seleccionada con comboBoxes <<<< '''

''' Settea la cantidad correcta de layout dinamicos en layout dinamico '''
''' tipo_boton -> 0: usa btn seccion (No pide confirmacion), 1: usa btn pieza (Pide confirmacion) '''



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
        print("error debug aplicar_pieza_seleccion(): No hay sección de pieza seleccinada.")
        return

    pieza_seccion = pieza_seccion_item.text()
    # print("aplicar_pieza_de_db() --> Pieza seleccionada, Familia: ", pieza_familia, " - Modelo: ", pieza_modelo, " - Tipo seccion: ", pieza_seccion, "\n")  # Debug

    if not pieza_modelo:
        print("error debug aplicar_pieza_seleccion(): No se selecciona ninguna pieza/modelo")
        return

    # print(" aplicar_pieza_de_db()  ---> valor de es_creada: ", es_creada, "\n")


    ''' obtiene ID de pieza, dependiendo de la base de datos '''
    pieza_id = db_get_id_pieza(pieza_familia, pieza_modelo, es_creada)

    # Usa tabla Parametros de DB
    trapecios_necesarios = db_get_cant_trapecios(pieza_id, pieza_seccion, es_creada)

    # Obtiene informacion (dimensiones) de los trapecios de la seccion consultando tabla Trapecios
    pieza_trapecios = db_get_datos_trapecios(pieza_id, pieza_seccion, es_creada)
    # print(" aplicar_pieza_de_db() : valor pieza_trapecios: ", pieza_trapecios, "\n")
    # print("\n\n")

    ''' Asigna valores fijos (dimensiones) a layouts dinamicos '''
    # Iguala la cantidad de layouts dinamicos a la cantidad necesaria
    ajustar_layouts_dinamicos(self, trapecios_necesarios)

    # Aplica dimensiones de trapecios a campos        
    aplicar_dimensiones_pieza(self, pieza_trapecios)

    ''' Carga las dimensiones todas las secciones en lista dinamica para poder editar piezas que ya fueron creadas y guardadas en DB '''

    ''' Store the values of all sections (secciones) '''
    self.dynamic_layout_data = db_get_all_trapecios_data(pieza_id, es_creada)
    # print("aplicar_pieza_de_db ()  --> values secciones_data original: ", self.dynamic_layout_data, "\n")

    ''' Sort the data based on the POSITION column '''
    self.dynamic_layout_data = {key: sorted(value, key=lambda x: x[0]) for key, value in self.dynamic_layout_data.items()}

    # print("aplicar_pieza_de_db ()  --> values secciones_data Despues de aplicar SORT en base a columna POSICION de tupla: ", self.dynamic_layout_data, "\n")
    # print("\n\n")


    ''' Usa valores dinamicamente agregados a LineEdits para hacer calculos y asignarlos '''
    # calcular_nuevos_valores(self) # Se comenta para manejo de dibujo # Automaticamente calcula valores de propiedades de trapecio

    ''' Anade todos los trapecios a listWidget que se usa para borrar'''
    self.ui.tab1_list_trapecios_existentes.clear()
    for index, row in enumerate(reversed(self.dynamic_layouts)):
        # Agrega name_label de trapecio a LIST para luego poder seleccionalo y borrarlo
        self.ui.tab1_list_trapecios_existentes.addItem(f"T{index+1}")




def aplicar_pieza_de_dynamic(self):
    ''' Igual a aplicar_pieza_de_db(), Pero en vez de sacar los datos de la base de datos, los obtiene de self.dynamic_layout_data '''

    # print(f"aplicar_pieza_de_dynamic() --> El contenido dentro d e dynamic_layout_data es: {self.dynamic_layout_data} \n\n")

    # Corresponde a la seccion seleccionada
    pieza_seccion_item = self.ui.list_tipo_seccion.currentItem()
    
    # Ensure there is a selection in the list widget
    if pieza_seccion_item is None:
        print("error debug aplicar_pieza_de_dynamic(): No hay seccón de pieza seleccionada.")
        return
    pieza_seccion = pieza_seccion_item.text()

    # Obtiene y ajusta la cantidad de trapecios para la seccion seleccionada
    try:
        trapecios_necesarios = len(self.dynamic_layout_data[pieza_seccion])
        # print(f"aplicar_pieza_de_dynamic() --> len de dict: {trapecios_necesarios}")
        ajustar_layouts_dinamicos(self, trapecios_necesarios)
    except:
        # print(f"aplicar_pieza_de_dynamic() --> len de dict: error. Se asume que es una pieza temporal")
        ajustar_layouts_dinamicos(self, 0)

    # pieza_trapecios = db_get_datos_trapecios(pieza_id, pieza_seccion, es_creada)

    try:
        pieza_trapecios = self.dynamic_layout_data[pieza_seccion]
        # print(f"aplicar_pieza_de_dynamic() --> trapecios para seccion en dict: {pieza_trapecios}")
        aplicar_dimensiones_pieza_dynamic(self, pieza_trapecios)
        # calcular_nuevos_valores(self) # Se comenta para manejo de dibujo
    except:
        print("No existe datos para self.dyn_layout_data[pieza_seccion]... Por lo tanto se asume pieza temporal")
    
    self.ui.tab1_list_trapecios_existentes.clear()
    for index, row in enumerate(reversed(self.dynamic_layouts)):
        # Agrega name_label de trapecio a LIST para luego poder seleccionalo y borrarlo
        self.ui.tab1_list_trapecios_existentes.addItem(f"T{index+1}")
        

    


''' ============================================================================================================================ '''

''' funcion para manejar informacion ingresada por usuario en VENTANA CREACION PIEZA '''
def handle_crear_pieza(self):
    ''' Handles the logic when the "Crear Pieza" button is clicked '''
    # Open the dialog and capture the result data
    result_data = open_crear_pieza_dialog(self)

    if result_data:

        self.dynamic_layout_data = {}

        # The dialog was accepted, and result_data is returned
        # print("handle_crear_pieza() --> Data from CrearPiezaDialog:", result_data, "\n")


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
