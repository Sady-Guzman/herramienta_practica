'''
    Funciones que modifican elementos que ya existen en la interfaz.
    Como contenido de Comboboxes, LineEdits
'''

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