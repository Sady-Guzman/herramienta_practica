from fn_database import * 

'''
    Funciones que modifican elementos que ya existen en la interfaz.
    Como contenido de Comboboxes, LineEdits
'''

''' ======================== Pobla conetenido de comboboxes ================================== '''

''' TIIPOS DE SECCIONES PARA PIEZA '''
def update_combo_secciones(self):
    familia_seleccionada = self.ui.combo_familia.currentText()
    modelo_seleccionado = self.ui.combo_modelo.currentText()

    tipos_secciones = db_cargar_tipos_secciones(familia_seleccionada, modelo_seleccionado)
    print(tipos_secciones)

    # Extract values from the tuples and convert them to strings
    tipos_secciones_str = [str(item[0]) for item in tipos_secciones]

    self.ui.combo_tipo_seccion.clear()

    if tipos_secciones:
        print("El contenido de la lista tipos_Secciones es: ", tipos_secciones_str)
        self.ui.combo_tipo_seccion.addItems(tipos_secciones_str)
    else:
        self.ui.combo_tipo_seccion.addItems(["Sin secciones disponibles"])


''' actualiza contenido de comboBox Modelos en base a seleccion comboBox Familia'''
def update_combo_modelo(self):
    # Obtiene familia seleccionada
    selected_family = self.ui.combo_familia.currentText()

    # obtiene los modelos respectivos de la familia seleccionada
    models = self.family_model_mapping.get(selected_family, [])

    self.ui.combo_modelo.clear()
    self.ui.combo_modelo.addItems(models)


''' ======================== Pobla campos LineEdits con dimensiones y valores de propiedades ================================== '''


''' Asigna dimensiones de una pieza de catalogo usando datos tuplas de DB trapecios '''
def aplicar_dimensiones_pieza(self, pieza_trapecios):
    # Check if the number of trapecios matches the layouts
    if not pieza_trapecios or len(pieza_trapecios) != len(self.dynamic_layouts):
        print("Error: No coinciden datos de los trapecios y los layouts dinámicos existentes.")
        return

    # Print for debugging
    for trapecio in pieza_trapecios:
        print(f"ID: {trapecio[0]}, Tipo Sección: {trapecio[1]}, Posición: {trapecio[2]}, "
            f"Base Inferior: {trapecio[3]:.2f}, Base Superior: {trapecio[4]:.2f}, "
            f"Altura: {trapecio[5]:.2f}, Pieza ID: {trapecio[6]}")

    # Iterate over layouts and update widgets
    for i, trapecio in enumerate(pieza_trapecios):
        layout = self.dynamic_layouts[i]

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


    
''' Asignar valores calculados en LineEdits dinamicos '''
def aplicar_valores_calculados(self, valores_areas, valores_cg, valores_inercia, valores_op, suma_areas, altura_acumulada, producto_ponderado):

    # asegeura que numero de indices en parametros sea igual a cant de layouts dinamicos
    if not valores_areas or len(valores_areas) != len(self.dynamic_layouts):
        print("Error: No coinciden datos de los trapecios y los layouts dinámicos existentes.")
        return

    # Itera sobre layouts y asigna valores a widgets LineEdits
    for i, trapecio in enumerate(valores_areas):
        layout = self.dynamic_layouts[i]

        # asegura que el widget existe
        if not layout["area_line"] or not layout["cg_line"] or not layout["inercia_line"] or not layout["op_line"]:
            print(f"Error: Widget for layout {i} is missing or deleted.")
            continue

        layout["area_line"].setText(f"{valores_areas[i]}")
        layout["cg_line"].setText(f"{valores_cg[i]:.7f}")
        layout["inercia_line"].setText(f"{valores_inercia[i]:.7f}")
        layout["op_line"].setText(f"{valores_op[i]:.7f}")
    
    ''' valores en layout NO-dinamico de ventana '''

    sumatoria_op = sum(valores_op)

    self.ui.result_sum_altura.setText(f"{altura_acumulada:.7f}")
    self.ui.result_sum_area.setText(f"{suma_areas:.7f}")
    self.ui.result_sum_ponderado.setText(f"{producto_ponderado:.7f}")
    self.ui.result_sum_op.setText(f"{sumatoria_op:.7f}")