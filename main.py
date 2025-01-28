import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel, QSpacerItem, QSizePolicy
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog, QComboBox, QGridLayout
from ui_files.herramienta_trapecios_v8 import Ui_Dialog  # Import from the ui_files directory
from fn_database import *
from fn_calculo_propiedades import *
from fn_update_gui import *
from fn_elementos_gui import *
from fn_crear_pieza import open_crear_pieza_dialog
from fn_pieza_temporal import *
from armadura_activa import setup_armadura_activa
from PySide6.QtCore import Qt

# QVLayout: layout_nuevas_row  -> Se le agregan Layouts dinamicos (manual y selec de catalogo)
# historial_agregados          -> Contador de tuplas que se agregaron dinamicamente a QVlayout. Se usa para sabe en que numero iterar para la creacion de layouts dinamicos
# family_model_mapping_(catalogo or usuario)        -> Diccionario que mapea cada familia de piezas con sus respectivos modelos
# es_creada -> guarda que tipo de catalogo se esta usando (False -> catalogo, True -> usuario)
# db_es_catalogo se cambia por es_creada (es_creada = TRUE = es de DB piezas_creadas.db, FALSE = es DB catalogo.db)

class MyDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()          # Crea instancia de clase UI
        self.ui.setupUi(self)         # Aplica UI a Dialog (ventana)

        self.dynamic_layouts = []    # Inicia variable para guardar layouts dinamicos
        self.dynamic_layouts_data = []
        self.historial_agregados = 0 # Se usa para llevar la cuenta de cuantos layouts dinamicos hay generados actualmente
        self.valores_creacion = [] # Almacena valores ingresados por usuario en ventana de creacion de pieza

        self.es_creada = False # identifica que boton se usa para poblar ComboBoxes de familia/modelo, y luego a cual db hacer query
        self.es_temporal = False # Se usa para saber si la pieza actual esta en base de datos o no (Maneja accion btn_acpt_tipo_seccion)
        # self.es_catalogo = 3 # identifica que boton se usa para poblar ComboBoxes de familia/modelo, y luego a cual db hacer query
        self.ultima_pieza = ['0', '0'] # Lista que recuerda cual fue la ultima pieza (combinacion de familia/modelo) que el usuario selecciona.

        self.se_guardaron_cambios = False
        self.es_primera_vez = True
        
        # Initialize storage for dynamic layout data
        self.dynamic_layout_data = {}

        ''' Inicia variables para guardar informacion dinamica de pestana armaduras activas '''
        self.dynamic_cotas = []
        self.dynamic_diametros_arm_act = []
        self.dynamic_cordones_arm_act = {}
        self.dynamic_tpi_arm_act = {}

        ''' >>>> Inicia variables y conexiones de elementos fijos <<<< '''

        # Carga datos de familias/modelos de DB
        self.family_model_mapping_catalogo = db_cargar_familias_modelos(self, True) # Usa DB CATALOGO
        self.family_model_mapping_usuario = db_cargar_familias_modelos(self, False) # Usa DB PIEZAS_CREADAS


        # Conecta btn genera layouts dinamicos
        self.ui.btn_acpt_agregar.clicked.connect(lambda: generate_layout(self)) # Agrega Dynamic Row

        # conecta btn Elimina layouts dinamicos
        self.ui.btn_acpt_eliminar.clicked.connect(
            lambda: confirmar_borrar(self, self.ui.spin_cant_eliminar.value())
        ) # Elimina Dynamic Row

        self.ui.btn_salto_linea.clicked.connect(lambda: print("\n\n"))

        
        # conecta btn para usar nueva pieza CATALOGO
        self.ui.btn_usar_pieza_catalogo.clicked.connect(lambda: poblar_combo_familia(self, True)) # Combo familia w/ CATALOGO

        # conecta btn para poblar combo familia con piezas de DB creada por usuario
        self.ui.btn_usar_pieza_usuario.clicked.connect(lambda: poblar_combo_familia(self, False)) # Combo familia w/ PIEZAS_CREADAS

        # conecta btn calcular propiedades de campos LineEdits
        self.ui.btn_calcular_nuevos_valores.clicked.connect(lambda: calcular_nuevos_valores(self)) # Calcular nuevos valores

        # Invoca ventana para CREAR NUEVA PIEZA
        self.ui.btn_crear_pieza_temp.clicked.connect(lambda: handle_crear_pieza(self)) # CREAR pieza

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        self.ui.combo_familia.currentIndexChanged.connect(lambda: update_combo_modelo(self, self.es_creada)) # Combo Modelos

        # Conecta senal de cambio de seleccion en 'comboFamilia' a 'update_combo_modelo'
        self.ui.combo_modelo.currentIndexChanged.connect(lambda: update_list_secciones(self, self.es_creada)) # Lista Secciones

        # Cambia tipo de seccion en layouts dinamicos
        self.ui.btn_acpt_tipo_seccion.clicked.connect(lambda: self.aplicar_pieza(self.es_temporal, self.es_creada)) # Aplica pieza/seccion

        # Conectar botones a sus métodos
        self.ui.btn_save_seccion.clicked.connect(lambda: save_current_section_data(self))     # Guardar datos de sección

        # Conectar btn GUARDAR PIEZA A DB (piezas_creadas)
        self.ui.btn_save_pieza.clicked.connect(lambda: save_pieza_data(self)) # Guardar Pieza TEMP en DB

        ''' ===============================================  TAB2  Armaduras Activas  ================================================== '''
        setup_armadura_activa(self) # Inicia las variabes que se usan en pestana 2 (Armadura Activa)
        self.ui.tab2_relleno_layout_armaduras.setVisible(False) # ESCONDE BOTON DE RELLENO PARA CUADRAR GRID









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
            cordon['num_cordones'].append(QLineEdit())
            cordon['tpi'].append(QLineEdit())

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
        
        print("add_cordon() --> Cantidad de cordones es: ", len(self.dynamic_cordones_arm_act), "\n")
        # Se asegura de que no se generen mas d4 tipos de corodnes (porque en documentacion solo existen 4)
        if len(self.dynamic_cordones_arm_act) >= len(diametros_en_db):
            popup_msg("Solo hay 4 tipos de cordones en base de datos")
            return 


        # First, delete the existing horizontal spacer in the grid
        if self.ui.gridLayout.itemAtPosition(1, 1):  # Checking if there is an item at position (1, 1)
            item = self.ui.gridLayout.itemAtPosition(1, 1)  # Remove the item at this position (the horizontal spacer)
            if item:
                self.ui.gridLayout.removeItem(item)  # Remove the item from the layout
                del item  # Remove the item from memory

        # Determine the new column index using columnCount()
        index = self.ui.gridLayout.columnCount()  # Use columnCount to get the current number of columns

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
        num_cordones = [QLineEdit() for _ in self.dynamic_cotas]
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

        # Re-add the horizontal spacer to the rightmost position in the grid layout
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.ui.gridLayout.addItem(self.horizontalSpacer, 1, index + 1)  # Add it to the rightmost side of the grid

        # Adjust the stretch for all columns to maintain balance
        for col in range(index + 2):  # Adjusts stretching for all columns, including the new one and the spacer
            self.ui.gridLayout.setColumnStretch(col, 1)


    ''' ====================================================================================================================================================== '''


    def del_cordon(self, index):
        if self.dynamic_cordones_arm_act:
            # Get the last cordon
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

            # Remove layout from the grid
            self.ui.gridLayout.removeItem(cordon['layout'])
            cordon['layout'].deleteLater()

            # Remove the entry from the list of dynamically generated diameters
            self.dynamic_diametros_arm_act.pop()

            # Remove the column from the grid layout
            for i in reversed(range(self.ui.gridLayout.count())):
                item = self.ui.gridLayout.itemAt(i)
                if item and item.widget() in cordon.values():
                    self.ui.gridLayout.removeWidget(item.widget())
                    item.widget().deleteLater()


    # Boton aplicar seccion
    ''' Aplica pieza en espacio dinamico de trapecios. Maneja el caso de pieza de catalogo, creada por usuario, o temporal'''
    # Diferencia entre creada por usuario y temporal es que las piezas en base de datos 'piezas_creadas.db' fueron temporales en algun momento y fueron guardadas a la base de datos con btn de guardado
    def aplicar_pieza(self, es_temporal, es_creada):
        if self.es_temporal == False:
            print("MAIN.aplicar_pieza() entra en IF porque self.es_temporal = ", self.es_temporal, "\n")

            familia_seleccionada = self.ui.combo_familia.currentText()
            modelo_seleccionado = self.ui.combo_modelo.currentText()

            if familia_seleccionada != self.ultima_pieza[0] or modelo_seleccionado != self.ultima_pieza[1]:
                print("\n\n\n\n \t\t\t >>>>>>>>>>MAIN.aplicar_pieza() -> fig actual =!!= LAST<<<<\n")
                print(f"familia seleccionada: {familia_seleccionada} -- modelo seleccionado: {modelo_seleccionado} -- ultima_pieza[0]: {self.ultima_pieza[0]} -- ultima_pieza[1]: {self.ultima_pieza[1]}\n")

                ''' # Recuerda la pieza que fue seleccionada por ultima vez '''
                self.ultima_pieza[0] = familia_seleccionada
                self.ultima_pieza[1] = modelo_seleccionado
                print(f"MAIN.aplicar_pieza() --> Valor de self.ultima_pieza[0]y[1]: {self.ultima_pieza} \n")

                aplicar_pieza_de_db(self, es_creada, self.dynamic_layout_data)

                print("MAIN.aplicar_pieza() despues de terminar aplicar pieza ---> valor de dynamic_layout_data: ", self.dynamic_layout_data)
            else:
                print("\n\n\n\n\n\n \t\t\t >>>>>>>>>>MAIN.aplicar_pieza() -> fig actual === LAST<<<< \n")
                print(f"familia seleccionada: {familia_seleccionada} -- modelo seleccionado: {modelo_seleccionado} -- ultima_pieza[0]: {self.ultima_pieza[0]} -- ultima_pieza[1]: {self.ultima_pieza[1]}\n")
                aplicar_pieza_de_dynamic(self)
        else:
            print("MAIN.aplicar_pieza() entra en ELSE porque es una pieza_temporal, es_temporal: ", self.es_temporal, "\n")
            aplicar_pieza_de_dynamic(self)






    ''' ======================================================================================================================================================'''

''' Muestra mensaje en ventana emergente al usuario'''
def popup_msg(message):
    popup = QMessageBox()
    popup.setIcon(QMessageBox.Warning)  # ICONO
    popup.setWindowTitle("Mensaje")  # title
    popup.setText(message)  # Main message text
    popup.setStandardButtons(QMessageBox.Ok)  # agrega btn OK
    popup.exec()  # muestra ventana PopUp


if __name__ == "__main__":
    ''' Inicia estructura bases de datos catalogo/piezas_creadas solo en caso de que no exista '''
    db_iniciar_database("catalogo.db")
    db_iniciar_database("piezas_creadas.db")

    # print_familias_modelos() # Debug muestra todo el catalogo y piezas_creadas


    app = QApplication(sys.argv)   # Crear aplicacion
    dialog = MyDialog()            # Crear ventana Dialog
    dialog.show()                  # Mostrar Dialog
    sys.exit(app.exec())           # Inicia loop de eventos app
