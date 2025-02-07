import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel, QComboBox
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from PySide6.QtCore import Qt
from fn_database import db_tipos_hormigon, db_id_tipo_hormigon_nombre, db_resistencias_tipo_hormigon, db_densidades_tipo_hormigon


def setup_tab_materiales(self):
    ''' Se ejecuta desde main cuando inicia app '''

    # Al iniciar se llena ComboBox de tipos de hormigon, Usando los tipos disponibles en base de datos
    mat_fill_combo_tipo_horm(self)
    self.ui.tab4_combo_tipo_horm.setCurrentIndex(-1)

    # Cuando usuario elige un tipo distinto de hormigon, se actualizan los parametros de las resistencias
    self.ui.tab4_combo_tipo_horm.currentIndexChanged.connect(
    lambda: (mat_fill_densidades_tipo_horm(self), mat_fill_resistencias_tipo_horm(self))
)



def mat_fill_combo_tipo_horm(self):
    ''' usa conteido tabla tipos_homigon en materiales.db para llenar ComboBox '''
    tipos_hormigon = db_tipos_hormigon()

    for _, tipo in tipos_hormigon:
        self.ui.tab4_combo_tipo_horm.addItem(tipo)

def mat_fill_resistencias_tipo_horm(self):
    ''' Llena LineEdits de resistencias (F'c) y (E) en TAB4 materiales segun la seleccion de tipo de hormigon en comboBox '''

    # id = [0]
    # tipo_hormigon (FOREIGN KEY) = [1]
    # ---------------------------------
    # tab4_line_horm_min_fc = [2]
    # tab4_line_horm_min_e =  [3]
    # tab4_line_horm_max_fc = [4]
    # tab4_line_horm_max_e = [5]
    # tab4_line_horm_final_fc = [6]
    # tab4_line_horm_final_e = [6]
    # tab4_line_horm_insitu_fc = [7]
    # tab4_line_horm_insitu_e = [7]

    tipo_hormigon_seleccionado = self.ui.tab4_combo_tipo_horm.currentText()

    id_hormigon = db_id_tipo_hormigon_nombre(tipo_hormigon_seleccionado)
    id_hormigon = id_hormigon[0][0]


    # usa ID obtenido como FK en tabla de resistencias
    tupla_resistencias = db_resistencias_tipo_hormigon(id_hormigon)
    tupla_resistencias = tupla_resistencias[0]


    if tupla_resistencias:  
        self.ui.tab4_line_horm_min_fc.setText(str(tupla_resistencias[2]))
        self.ui.tab4_line_horm_min_e.setText(str(tupla_resistencias[3]))
        self.ui.tab4_line_horm_max_fc.setText(str(tupla_resistencias[4]))
        self.ui.tab4_line_horm_max_e.setText(str(tupla_resistencias[5]))
        self.ui.tab4_line_horm_final_fc.setText(str(tupla_resistencias[6]))
        self.ui.tab4_line_horm_final_e.setText(str(tupla_resistencias[6]))
        self.ui.tab4_line_horm_insitu_fc.setText(str(tupla_resistencias[7]))
        self.ui.tab4_line_horm_insitu_e.setText(str(tupla_resistencias[7]))
    else:
        print(f"No se encuentran resistencias para id_hormigon: {id_hormigon}")


def mat_fill_densidades_tipo_horm(self):
    ''' Llena LineEdits de densidades HORMIGON y ACERO en TAB4 materiales segun la seleccion de tipo de hormigon en comboBox '''
    
    # id = [0]
    # tipo_hormigon (FOREIGN KEY) = [1]
    # ---------------------------------
    # self.ui.tab4_line_dens_horm  = [2]
    # self.ui.tab4_line_dens_acero = [3]

    tipo_hormigon_seleccionado = self.ui.tab4_combo_tipo_horm.currentText()
    id_hormigon = db_id_tipo_hormigon_nombre(tipo_hormigon_seleccionado)
    id_hormigon = id_hormigon[0][0]

    # usa ID obtenido como FK en tabla de resistencias
    tupla_densidades = db_densidades_tipo_hormigon(id_hormigon)

    if tupla_densidades:  
        self.ui.tab4_line_dens_horm.setText(str(tupla_densidades[0][2]))
        self.ui.tab4_line_dens_acero.setText(str(tupla_densidades[0][3]))
        
    else:
        print(f"No se encuentran densidades para id_hormigon: {id_hormigon}")





