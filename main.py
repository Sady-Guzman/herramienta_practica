#  IMPORTS DE DEPENDENCIAS
import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QMessageBox, QComboBox, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

import matplotlib.pyplot as plt  # Add this import statement
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Polygon

import sqlite3
import random

#  IMPORTS DE OTROS ARCHIVOS
from ui_files.herramienta_trapecios_windows import Ui_Dialog  # Import codigo GUI (Construido usando QTDesigner)

from fn_database import *
from fn_calculo_propiedades import *
from fn_update_gui import *
from fn_elementos_gui import *

from fn_crear_pieza import open_crear_pieza_dialog
from fn_pieza_temporal import *
from utils import popup_msg
from dibujo import plot_trapecios
from armadura_activa import setup_armadura_activa # TAB 2
from armadura_pasiva import setup_armadura_pasiva # TAB 3
from tab_materiales import setup_tab_materiales # TAB 4
from tab_calculo_parcial import setup_tab_calc_parcial # TAB 5



# QVLayout: layout_nuevas_row  -> Se le agregan Layouts dinamicos (manual y selec de catalogo)
# historial_agregados          -> Contador de tuplas que se agregaron dinamicamente a QVlayout. Se usa para sabe en que numero iterar para la creacion de layouts dinamicos
# family_model_mapping_(catalogo or usuario)        -> Diccionario que mapea cada familia de piezas con sus respectivos modelos
# es_creada -> guarda que tipo de catalogo se esta usando (False -> catalogo, True -> usuario)
# db_es_catalogo se cambia por es_creada (es_creada = TRUE = es de DB piezas_creadas.db, FALSE = es DB catalogo.db)

class MyDialog(QDialog):

    ''' Previene cierre de aplicacion al presionar tecla escape '''
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            print("Escape key.")
        else:
            super().keyPressEvent(event)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()          # Crea instancia de clase UI
        self.ui.setupUi(self)         # Aplica UI a Dialog (ventana)

        self.familia_pieza_cargada = 0
        self.modelo_pieza_cargada = 0
        self.seccion_pieza_cargada = 0

        self.dynamic_layouts = []    # Inicia variable para guardar layouts dinamicos
        self.dynamic_layouts_data = []
        self.historial_agregados = 0 # Se usa para llevar la cuenta de cuantos layouts dinamicos hay generados actualmente
        self.valores_creacion = [] # Almacena valores ingresados por usuario en ventana de creacion de pieza

        ''' ---------------------- '''
        self.dynamic_apasiva_barras = [] # Guarda referencias de layouts generados dinamicamente como barras_corrugadas de armadura pasiva

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
        self.dynamic_tpi_arm_act = {}
        self.dynamic_cordones_arm_act = {}

        ''' >>>> Inicia variables y conexiones de elementos fijos <<<< '''

        

        # Connect tab change signal to function
        # self.ui.tabWidget.currentChanged.connect(lambda index: self.set_default_button(index))
        ''' Default pushBtn en cada TAB '''
        self.ui.btn_calcular_nuevos_valores.setDefault(True)
        self.ui.tabWidget.currentChanged.connect(self.set_default_button)


        # Carga datos de familias/modelos de DB
        self.family_model_mapping_catalogo = db_cargar_familias_modelos(self, True) # Usa DB CATALOGO
        self.family_model_mapping_usuario = db_cargar_familias_modelos(self, False) # Usa DB PIEZAS_CREADAS


        # Conecta btn genera layouts dinamicos
        self.ui.btn_acpt_agregar.clicked.connect(lambda: generate_layout(self)) # Agrega Dynamic Row

        # conecta btn Elimina layouts dinamicos
        self.ui.btn_acpt_eliminar.clicked.connect(
            # lambda: confirmar_borrar(self, self.ui.spin_cant_eliminar.value())
            lambda: confirmar_borrar(self)
        ) # Elimina Dynamic Row        
        

        
        # conecta btn para usar nueva pieza CATALOGO
        self.ui.btn_usar_pieza_catalogo.clicked.connect(lambda: poblar_combo_familia(self, True)) # Combo familia w/ CATALOGO

        # conecta btn para poblar combo familia con piezas de DB creada por usuario
        self.ui.btn_usar_pieza_usuario.clicked.connect(lambda: poblar_combo_familia(self, False)) # Combo familia w/ PIEZAS_CREADAS

        # conecta btn calcular propiedades de campos LineEdits
        self.ui.btn_calcular_nuevos_valores.clicked.connect(lambda: calcular_nuevos_valores(self)) #  nuevos valores CALCULAR
        self.ui.btn_calcular_nuevos_valores.clicked.connect(lambda: plot_trapecios(self))# Invoca dibujo de pieza seleccionada DIBUJO

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

        ''' ===============================================  SETUP para tabs  ================================================== '''
        setup_armadura_activa(self) # Inicia las variabes que se usan en pestana 2 (Armadura Activa)
        self.ui.tab2_relleno_layout_armaduras.setVisible(False) # ESCONDE BOTON DE RELLENO PARA CUADRAR GRIDLAYOUT

        setup_armadura_pasiva(self) # Inicia TAB3 (Armadura Pasiva)
        setup_tab_materiales(self) # inicia TAB4 (Materiales)
        setup_tab_calc_parcial(self) # Inicia/maneja tab de Calculo Parcial (Tab5)

        ''' Inicia App en tab 0 (GEOMETRIA) '''
        self.ui.tabWidget.setCurrentIndex(0) 



    ''' ====================================================================================================================================================== '''

    


    # Boton aplicar seccion
    ''' Aplica pieza en espacio dinamico de trapecios. Maneja el caso de pieza de catalogo, creada por usuario, o temporal'''
    # Diferencia entre creada por usuario y temporal es que las piezas en base de datos 'piezas_creadas.db' fueron temporales en algun momento y fueron guardadas a la base de datos con btn de guardado
    def aplicar_pieza(self, es_temporal, es_creada):
        if self.es_temporal == False:
            # print("MAIN.aplicar_pieza() entra en IF porque self.es_temporal = ", self.es_temporal, "\n")

            ''' Juntar variables eventualmente. Por ahora se sigue con desarrollo por tiempo '''
            try:
                familia_seleccionada = self.ui.combo_familia.currentText()
                self.familia_pieza_cargada = self.ui.combo_familia.currentText()
            except:
                familia_seleccionada = 0
                self.familia_pieza_cargada = 0
            
            try:
                modelo_seleccionado = self.ui.combo_modelo.currentText()
                self.modelo_pieza_cargada = self.ui.combo_modelo.currentText()
            except:
                modelo_seleccionado = 0
                self.modelo_pieza_cargada = 0
            
            try:
                seccion_seleccionada = self.ui.list_tipo_seccion.currentItem().text()
                self.seccion_pieza_cargada = self.ui.list_tipo_seccion.currentItem().text()
            except:
                seccion_seleccionada = 0
                self.seccion_pieza_cargada = 0            
            
            

            pieza_id = db_get_id_pieza(familia_seleccionada, modelo_seleccionado, es_creada)
            # plot_trapecios(pieza_id[0], seccion_seleccionada, familia_seleccionada, modelo_seleccionado, self.es_creada, self)# Invoca dibujo de pieza seleccionada


            if familia_seleccionada != self.ultima_pieza[0] or modelo_seleccionado != self.ultima_pieza[1]:
                # print("\n\n\n\n \t\t\t >>>>>>>>>>MAIN.aplicar_pieza() -> fig actual =!!= LAST<<<<\n")
                # print(f"familia seleccionada: {familia_seleccionada} -- modelo seleccionado: {modelo_seleccionado} -- ultima_pieza[0]: {self.ultima_pieza[0]} -- ultima_pieza[1]: {self.ultima_pieza[1]}\n")

                ''' # Recuerda la pieza que fue seleccionada por ultima vez '''
                self.ultima_pieza[0] = familia_seleccionada
                self.ultima_pieza[1] = modelo_seleccionado
                # print(f"MAIN.aplicar_pieza() --> Valor de self.ultima_pieza[0]y[1]: {self.ultima_pieza} \n")

                aplicar_pieza_de_db(self, es_creada, self.dynamic_layout_data)

                # print("MAIN.aplicar_pieza() despues de terminar aplicar pieza ---> valor de dynamic_layout_data: ", self.dynamic_layout_data)
            else:
                # print("\n\n\n\n\n\n \t\t\t >>>>>>>>>>MAIN.aplicar_pieza() -> fig actual === LAST<<<< \n")
                # print(f"familia seleccionada: {familia_seleccionada} -- modelo seleccionado: {modelo_seleccionado} -- ultima_pieza[0]: {self.ultima_pieza[0]} -- ultima_pieza[1]: {self.ultima_pieza[1]}\n")
                aplicar_pieza_de_dynamic(self)
        else:
            # print("MAIN.aplicar_pieza() entra en ELSE porque es una pieza_temporal, es_temporal: ", self.es_temporal, "\n")
            aplicar_pieza_de_dynamic(self)

            # plot_trapecios(pieza_id[0], seccion_seleccionada, familia_seleccionada, modelo_seleccionado, self.es_creada)# Invoca dibujo de pieza seleccionada



    ''' Maneja Btn por defecto segun TAB seleccinada '''
    def set_default_button(self, index):
        # Remueve defecto de otras tabs primero
        self.ui.btn_calcular_nuevos_valores.setDefault(False)
        self.ui.tab2_btn_valores.setDefault(False)
        self.ui.tabWidget.widget(index).setFocus()

        # Asigna btn por defecto segun pestana seleccionada
        if index == 0:
            self.ui.btn_calcular_nuevos_valores.setDefault(True)
            self.ui.btn_calcular_nuevos_valores.setAutoDefault(True)
        elif index == 1:
            self.ui.tab2_btn_valores.setDefault(True)
            self.ui.tab2_btn_valores.setAutoDefault(True)
        elif index == 2:
            self.ui.tab3_btn_calcular.setDefault(True)
        elif index == 3:
            self.ui.tab4_btn_guardar_valores.setDefault(True)
        elif index == 4:
            self.ui.tab5_btn_calcular.setDefault(True)
    

        

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
    print("=========================================================================================================")
    print("=========================================================================================================\n\n\n")


    app = QApplication(sys.argv)   # Crear aplicacion
    dialog = MyDialog()            # Crear ventana Dialog
    dialog.setWindowTitle("Herramienta de Calculo PREANSA") # TITULO VENTANA
    dialog.show()                  # Mostrar Dialog
    sys.exit(app.exec())           # Inicia loop de eventos app
