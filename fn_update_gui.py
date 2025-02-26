from fn_database import * 

'''
    Funciones que modifican elementos que ya existen en la interfaz.
    Como contenido de Comboboxes, LineEdits
'''

''' ======================== Pobla conetenido de comboboxes ================================== '''

''' Poblar combobox famila '''
def poblar_combo_familia(self, tipo_db):
    # tipo_db: true -> catalogo, false -> usuario pieza_creada
    
    ''' Resetea es_temporal, ultima_pieza, y dyn_lay_dat por cambio de tipo de pieza (temporal o no temporal)
        En este caso no es temporal, y este reset es necesario en caso de que antes de hacer click en un boton
        de usar piezas de db (de catalogo o creadas por usuario, osea catalogo.db o piezas_creadas.db) el usuario hiciera
        uso de la funcion de creacion de pieza
    '''
    self.es_temporal = False
    self.dynamic_layout_data = {}
    self.ultima_pieza = ['0', '0']

    self.family_model_mapping_usuario = db_cargar_familias_modelos(self, False) # Carga nuevamente mapeo de fam/mod ya que se puede haber creado una pieza nueva

    self.ui.combo_familia.clear()
    if tipo_db == True:
        self.es_creada = False
        # self.es_catalogo = True
        self.es_temporal = False
        ''' usa DB catalogo '''
        self.ui.combo_familia.addItems(["Elegir"] + list(self.family_model_mapping_catalogo.keys()))
    else:
        self.db_es_catalogo = False
        self.es_creada = True
        self.es_temporal = False
        # self.es_catalogo = False
        ''' usa DB piezas_creadas '''
        self.ui.combo_familia.addItems(["Elegir"] + list(self.family_model_mapping_usuario.keys()))


''' TIIPOS DE SECCIONES PARA PIEZA '''
''' FUNCION ANTIGUA SIN USAR, AHORA SE USA update_list_seccines para lo mismo '''
def update_combo_secciones(self):
    familia_seleccionada = self.ui.combo_familia.currentText()
    modelo_seleccionado = self.ui.combo_modelo.currentText()

    tipos_secciones = db_cargar_tipos_secciones(familia_seleccionada, modelo_seleccionado)
    # print(tipos_secciones)

    # Extract values from the tuples and convert them to strings
    tipos_secciones_str = [str(item[0]) for item in tipos_secciones]

    self.ui.combo_tipo_seccion.clear()

    if tipos_secciones:
        # print("El contenido de la lista tipos_Secciones es: ", tipos_secciones_str)
        self.ui.combo_tipo_seccion.addItems(tipos_secciones_str)
    else:
        self.ui.combo_tipo_seccion.addItems(["Sin secciones disponibles"])

def update_list_secciones(self, es_creada):
    # Retrieve the selected family and model
    familia_seleccionada = self.ui.combo_familia.currentText()
    modelo_seleccionado = self.ui.combo_modelo.currentText()

    # Load the types of sections from the database
    if es_creada == False:
        tipos_secciones = db_cargar_tipos_secciones(familia_seleccionada, modelo_seleccionado, False)
    else:
        tipos_secciones = db_cargar_tipos_secciones(familia_seleccionada, modelo_seleccionado, True)
    # print(tipos_secciones)

    # Extract values from the tuples and convert them to strings
    tipos_secciones_str = [str(item[0]) for item in tipos_secciones]

    # Clear the current contents of the list widget
    self.ui.list_tipo_seccion.clear()

    # Add the retrieved section types to the list widget
    if tipos_secciones:
        # print("El contenido de la lista tipos_Secciones es: ", tipos_secciones_str)
        self.ui.list_tipo_seccion.addItems(tipos_secciones_str)
    else:
        self.ui.list_tipo_seccion.addItem("Sin secciones disponibles")


''' actualiza contenido de comboBox Modelos en base a seleccion comboBox Familia'''
def update_combo_modelo(self, es_creada):
    # tipo_db: true -> catalogo, false -> usuario

    # Obtiene familia seleccionada
    selected_family = self.ui.combo_familia.currentText()

    # obtiene los modelos respectivos de la familia seleccionada
    if es_creada == False:
        models = self.family_model_mapping_catalogo.get(selected_family, [])
    else:
        models = self.family_model_mapping_usuario.get(selected_family, [])


    self.ui.combo_modelo.clear()
    self.ui.combo_modelo.addItems(models)


''' ======================== Pobla campos LineEdits con dimensiones y valores de propiedades ================================== '''


''' Asigna dimensiones de una pieza de catalogo usando datos tuplas de DB trapecios '''
def aplicar_dimensiones_pieza(self, pieza_trapecios):
    # Check if the number of trapecios matches the layouts
    if not pieza_trapecios or len(pieza_trapecios) != len(self.dynamic_layouts):
        print("Error: No coinciden datos de los trapecios y los layouts dinámicos existentes. [A]")
        return

    # Print for debugging
    # for trapecio in pieza_trapecios:
    #     print(f"ID: {trapecio[0]}, Tipo Sección: {trapecio[1]}, Posición: {trapecio[2]}, "
    #         f"Base Inferior: {trapecio[3]:.2f}, Base Superior: {trapecio[4]:.2f}, "
    #         f"Altura: {trapecio[5]:.2f}, Pieza ID: {trapecio[6]}")

    # Iterate over layouts in reverse order and update widgets
    for i, trapecio in enumerate(pieza_trapecios):
        layout = self.dynamic_layouts[len(pieza_trapecios) - 1 - i]

        # Check if the widget is valid (exists)
        if not layout["bi_line"]:  # You can add similar checks for other widgets if necessary
            print(f"Error: Widget for layout {i} is missing or deleted.")
            continue

        # Assign values to QLineEdit widgets
        layout["bi_line"].setText(f"{trapecio[3]:.3f}")  # Base Inferior
        layout["bs_line"].setText(f"{trapecio[4]:.3f}")  # Base Superior
        layout["altura_line"].setText(f"{trapecio[5]:.3f}")  # Altura
        layout["area_line"].setText("")  # Placeholder
        layout["cg_line"].setText("")  # Placeholder
        layout["inercia_line"].setText("")  # Placeholder
        layout["op_line"].setText("")  # Placeholder
        if trapecio[7] == 0:
            layout["combo_insitu"].setCurrentIndex(0)  # Default es NORMAL 
        else:
            layout["combo_insitu"].setCurrentIndex(1) # ES INSITU


    # Store the data in the correct format
    self.dynamic_layout_data = {
        trapecio[1]: [(trapecio[2], trapecio[3], trapecio[4], trapecio[5]) for trapecio in pieza_trapecios]
    }

def aplicar_dimensiones_pieza_dynamic(self, pieza_trapecios):
    # Check if the number of trapecios matches the layouts
    if not pieza_trapecios or len(pieza_trapecios) != len(self.dynamic_layouts):
        print("Error: No coinciden datos de los trapecios y los layouts dinámicos existentes. [B]")
        return

    # Print for debugging
    print(f"aplicar_dimensiones_pieza_DYNAMIC() --> valor en pieza_trapecios: {pieza_trapecios}\n")
    print(f"para DYNAMIC -> Base Inferior: {float(pieza_trapecios[0][0]):.2f}, Base Superior: {float(pieza_trapecios[0][1]):.2f},Altura: {float(pieza_trapecios[0][3]):.2f} ")
    # for trapecio in pieza_trapecios:
        # print(f"Base Inferior: {float(trapecio[1]):.2f}, Base Superior: {float(trapecio[2]):.2f}, Altura: {float(trapecio[3]):.2f}")

    # Iterate over layouts in reverse order and update widgets
    for i, trapecio in enumerate(pieza_trapecios):
        layout = self.dynamic_layouts[len(pieza_trapecios) - 1 - i]

        # Check if the widget is valid (exists)
        if not layout["bi_line"]:  # You can add similar checks for other widgets if necessary
            print(f"Error: Falta widget para layout {i}.")
            continue

        # Assign values to QLineEdit widgets
        layout["bi_line"].setText(f"{float(trapecio[1]):.3f}")  # Base Inferior
        layout["bs_line"].setText(f"{float(trapecio[2]):.3f}")  # Base Superior
        layout["altura_line"].setText(f"{float(trapecio[3]):.3f}")  # Altura
        layout["area_line"].setText("")  # Placeholder
        layout["cg_line"].setText("")  # Placeholder
        layout["inercia_line"].setText("")  # Placeholder
        layout["op_line"].setText("")  # Placeholder

    
''' Asignar valores calculados en LineEdits dinamicos '''
def aplicar_valores_calculados(self, valores_areas, valores_cg, valores_inercia, valores_op, suma_areas, altura_acumulada, producto_ponderado):
    j = 0  # Indice separado para manejar resultados de calculos. (i es indice de trapecios existentes)

    for i, layout in enumerate(self.dynamic_layouts):
        # Salta esta row (trapecio) en caso de ser hormigon tipo insitu
        # print(f"aplicar_valores_calculados() --> Valor en combo_insitu actual: {layout['combo_insitu'].currentText()}")
        if layout["combo_insitu"].currentText() == "Insitu":
            continue # Skipea esta iteracion y pasa a la siguiente

        # Asegura que no se pase de los limites de las listas de valores
        if j >= len(valores_areas):
            print(f"Warning: No hay suficientes valores calculados para layout {i}.")
            break  

        # Asigna valores a widgets LineEdtis
        layout["area_line"].setText(f"{valores_areas[j]}")
        layout["cg_line"].setText(f"{valores_cg[j]:.7f}")
        layout["inercia_line"].setText(f"{valores_inercia[j]:.7f}")
        layout["op_line"].setText(f"{valores_op[j]:.7f}")

        j += 1  # Solo incrementa valor de indice J en caso de ser usado. (Para manejar trapecios de tipo INSITU correctamente en GUI)


    ''' valores en layout NO-dinamico de ventana (resultados totales en lineEdits esquina superior derecha) '''
    sumatoria_op = sum(valores_op)

    self.ui.result_sum_altura.setText(f"{altura_acumulada:.7f}")
    self.ui.result_sum_area.setText(f"{suma_areas:.7f}")
    self.ui.result_sum_ponderado.setText(f"{producto_ponderado:.7f}")  # Y _ inf
    self.ui.result_sum_op.setText(f"{sumatoria_op:.7f}")




''' Poblar campos de ventana principal para pieza 'temporal' con datos de ventana de creacion '''
''' Una pieza temporal es una pieza que existe despues de crearla con ventana de creacion pero aun no es guardada en base de datos '''
def poblar_datos_pieza_temporal(self, familia, modelo, secciones):
    
    # print(f"poblar_datos_pieza_temporal() -> Familia: {familia}, Modelo: {modelo}")
    # print("Secciones:")
    # for index, seccion in enumerate(secciones, start=1):
        # print(f"  Sección {index}: {seccion}")


    ''' limpia y asigna nuevo valor a ComboBox de Familia '''
    self.ui.combo_familia.clear()
    self.ui.combo_familia.addItems([familia])

    ''' limpia y asigna nuevo valor a ComboBox de Modelo '''
    self.ui.combo_modelo.clear()
    self.ui.combo_modelo.addItems([modelo])

    ''' limpiar y asignar secciones a lista secciones '''
    self.ui.list_tipo_seccion.clear()
    if secciones:
        # print("El contenido de la lista tipos_Secciones es: ", secciones)
        self.ui.list_tipo_seccion.addItems(secciones)
    else:
        self.ui.list_tipo_seccion.addItem("Sin secciones disponibles")
