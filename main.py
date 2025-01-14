import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from ui_files.herramienta_trapecios_v6 import Ui_Dialog  # Import from the ui_files directory
from db_combobox import cargar_familias_modelos_db, db_cargar_tipos_secciones, db_get_datos_trapecios, db_get_cant_trapecios, db_get_id_pieza # Recupera set de familias y respectivos modelos de DB
from funciones_calculo import *




# QVLayout: layout_nuevas_row -> Se le agregan tuplas de valor de forma dinamica (manual y selec de catalogo)
# historial_agregados -> Contador de tuplas que se agregaron dinamicamente a QVlayout


class MyDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the dialog window
        self.dynamic_layouts = []  # Initialize dynamic layouts for row management
        self.historial_agregados = 0

        ''' >>>> Inicia variables y conexiones de elementos <<<< '''

        # Carga datos de familias/modelos de DB
        self.family_model_mapping = cargar_familias_modelos_db()


        # Conecta boton que acepta agregar tuplas a func generate_layout()
        self.ui.btn_acpt_agregar.clicked.connect(self.generate_layout)


        self.ui.btn_acpt_eliminar.clicked.connect(
            lambda: self.confirmar_accion(self.ui.spin_cant_eliminar.value())
        )

        self.ui.btn_calcular_nuevos_valores.clicked.connect(lambda: self.calcular_nuevos_valores())

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        self.ui.combo_familia.currentIndexChanged.connect(self.update_combo_modelo)

        # Conecta btn con funcion para usar una pieza de catalogo en calculo
        self.ui.btn_acpt_pieza.clicked.connect(lambda: self.aplicar_pieza_catalogo(1))

        # agg btn para usar pieza temporal

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        self.ui.combo_modelo.currentIndexChanged.connect(self.update_combo_secciones)

        # Cambioa tipo de seccion en layouts dinamicos
        self.ui.btn_acpt_tipo_seccion.clicked.connect(lambda: self.aplicar_pieza_catalogo(0))

        ''' llena comboBoxes Familia/Modelo'''
        # Usa variable iniciada en def__init__()... Siempre esta 'Elegir' como placeholder
        self.ui.combo_familia.addItems(["Elegir"] + list(self.family_model_mapping.keys()))
        
    
    
    ''' en desarrollo, TIPOS DE SECCIONES PARA PIEZA '''
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


    ''' Genera de manera dinamica tuplas para trapecios '''
    def generate_layout(self):
        # obtiene el numero de tuplas a generar de la spinbox 'spin_cant_agregar'
        num_rows = self.ui.spin_cant_agregar.value()
        print("debug_print> SpinBox Cantidad a generar value: ", num_rows) # Debug

        # print("elementos dinamicamente agregados: ", self.historial_agregados) # Debug
        # Obtiene el numero de figuras(tuplas) ya existentes en el QVlayout contenedor, se usa para nombrar correctamente los nuevos elementos
        tuplas_existentes = self.historial_agregados

        ''' Loop to create the frames '''
        for i in range(num_rows):
            self.add_rows(self.historial_agregados + 1)  # Starts from trapecio 2 (T2)
        # Agrega stretch al Vertical Layout que contiene las tuplas de elementos para pegarlos al borde superior
        # self.ui.layout_nuevas_row.addStretch()

    ''' >>>> Manipula layouts dinamicos y layout contenedor <<<< '''

    ''' genera nuevo Hlayout y sus elementos, Los nombra correctamente y agrega a Vlayout contenedor'''
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

    def confirmar_accion(self, index):
        # Pide confirmacion de usuario antes de borrar layouts
        reply = QMessageBox.question(self, 'Confirmar', 
                                    "Confirmar acción?", 
                                    QMessageBox.Yes  | QMessageBox.No, 
                                    QMessageBox.No)
        # Opcion si/no, Y opcion por defecto es NO
        if reply == QMessageBox.No:
            return 0
        
        print("DEBUG confirmar_accion() > valor de Index: ", index)

        self.del_rows(index)

    ''' Elimina tuplas que fueron creadas dinamicamente dentro del layout vertical '''
    def del_rows(self, index):
        print("DEBUG del_rows() > valor de Index: ", index)

        # Determine the number of rows to delete, using the spinner or the passed index
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
                    self.delete_layout_widgets(last_item.layout())  # Elimina los widgets dentro del layout primero
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


    ''' >>>> Usa pieza de catalogo seleccionada con comboBoxes <<<< '''


    ''' Settea la cantidad correcta de layout dinamicos en layout dinamico '''
    ''' tipo_boton -> 0: usa btn seccion (No pide confirmacion), 1: usa btn pieza (Pide confirmacion) '''
    def aplicar_pieza_catalogo(self, tipo_boton):
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
        self.ajustar_layouts_dinamicos(trapecios_necesarios, tipo_boton)

        # Aplicar dimensione de trapecios a campos        
        self.aplicar_dimensiones_pieza(pieza_trapecios)


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

        # Aplica resultados a layouts dinamicos + layouts fijos
        self.aplicar_valores_calculados(valores_areas, valores_cg, valores_inercia, valores_op, suma_areas, altura_acumulada, producto_ponderado)

        


    def ajustar_layouts_dinamicos(self, cantidad_trapecios, tipo_boton):
        # Tipo boton: 0: Cambia seccion, 1: Cambia pieza
        # Usa 99 para eliminar layouts para eliminar todos los layouts existentes (No hay caso de uso en el que se necesitan mas de 99 secciones para una pieza)
        print("DEBUG - ajustar_layouts_dinamicos > valor cantidad_trapecios: ", cantidad_trapecios)
        if tipo_boton == 0:
            self.del_rows(99) # No pide confirmacion
        else: 
            confirmacion = self.confirmar_accion(99) # Pide confirmacion 
            if confirmacion == 0:
                return

        ''' Loop to create the frames '''
        for i in range(cantidad_trapecios):
            self.add_rows(self.historial_agregados + 1)
        
        
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

    
    ''' Lee valores de todos los LineEdits dinamicos existentes y calcula nuevo resultado de area,I,cg,OP '''
    def calcular_nuevos_valores(self):
        ''' Obtiene valores de dimensiones '''
        valores_dimensiones_dinamicas = []

        if not self.dynamic_layouts:
            return

        for layout in self.dynamic_layouts:
            bi = layout["bi_line"].text()
            bs = layout["bs_line"].text()
            altura = layout["altura_line"].text()

            if not bi or not bs or not altura:
                print("Error calcular_nuevos_valores(): Missing values in one or more of the LineEdits.")
                return

            try:
                # Se agregan 0 antes y despues de valores de dimensiones para mantener consistencia en calculos
                valores_dimensiones_dinamicas.append((0, 0, 0, float(bi), float(bs), float(altura), 0))
            except Exception as e:
                print("Error calcular_nuevos_valores(): ", e)

        print("Debug calcular_nuevos_valores() -> los valores recuperados son: ", valores_dimensiones_dinamicas)

        ''' calcular valores area, CentroGravedad, Inercia, Op, Sumatorias, Prod Ponderado '''
        valores_areas = calcular_area(valores_dimensiones_dinamicas)
        altura_acumulada = calcular_altura_acumulada(valores_dimensiones_dinamicas)
        valores_inercia = calcular_inercia(valores_dimensiones_dinamicas)
        valores_cg = calcular_centro_gravedad(valores_dimensiones_dinamicas)
        suma_areas = calcular_suma_areas(valores_areas)
        producto_ponderado = calcular_producto_ponderado(valores_areas, valores_cg, suma_areas)
        valores_op = calcular_op(valores_areas, valores_cg, valores_inercia, producto_ponderado)

        # Aplica resultados a layouts dinamicos + layouts fijos
        self.aplicar_valores_calculados(valores_areas, valores_cg, valores_inercia, valores_op, suma_areas, altura_acumulada, producto_ponderado)

        return 

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



if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application
    dialog = MyDialog()            # Create the dialog window
    dialog.show()                  # Show the dialog window
    sys.exit(app.exec())           # Start the application's event loop
