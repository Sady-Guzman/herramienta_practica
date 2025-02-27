import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel, QComboBox
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from PySide6.QtCore import Qt
from fn_database import db_tipos_hormigon, db_id_tipo_hormigon_nombre, db_resistencias_tipo_hormigon, db_densidades_tipo_hormigon

import math

def setup_tab_materiales(self):
    ''' Se ejecuta desde main cuando inicia app '''

    # Al iniciar se llena ComboBox de tipos de hormigon, Usando los tipos disponibles en base de datos
    mat_fill_combo_tipo_horm(self)
    self.ui.tab4_combo_tipo_horm.setCurrentIndex(-1)

    ''' Asigna valor por defecto para variables de elasticidad de acero y '''
    self.ui.tab3_line_cons_es.setText("200000") # MPa
    self.ui.tab3_line_cons_eps.setText("198569") # MPa

    # Cuando usuario elige un tipo distinto de hormigon, se actualizan los parametros de las resistencias
    self.ui.tab4_combo_tipo_horm.currentIndexChanged.connect(
        lambda: (mat_fill_densidades_tipo_horm(self), mat_fill_resistencias_tipo_horm(self))
    )

    self.ui.tab4_btn_guardar_valores.clicked.connect(lambda: mat_calc_save_ec(self))



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

        print("\n\n\n\n\t\t -----------------------------------------------------------------------------------------------------------------------------")
        print("\t\t -------------------------------------        CALCULOS PESTANA MATERIALES        ---------------------------------------------")
        print("\t\t -----------------------------------------------------------------------------------------------------------------------------\n\n")

        

        self.ui.tab4_line_horm_min_fc.setText(str(tupla_resistencias[2]))
        self.ui.tab4_line_horm_min_e.setText(str(tupla_resistencias[3]))

        self.ui.tab4_line_horm_max_fc.setText(str(tupla_resistencias[4]))
        self.ui.tab4_line_horm_max_e.setText(str(tupla_resistencias[5]))

        self.ui.tab4_line_horm_final_fc.setText(str(tupla_resistencias[6]))
        self.ui.tab4_line_horm_final_e.setText(str(tupla_resistencias[7]))

        self.ui.tab4_line_horm_insitu_fc.setText(str(tupla_resistencias[8]))
        self.ui.tab4_line_horm_insitu_e.setText(str(tupla_resistencias[9]))

        print(f"--------------------------------------------")
        print(f"---   Usando valores de formula JACENA   ---\n\n")

        print("\n\tSe asigna densidad de concreto (Wc) de 2400 (kg/m3) por defecto.\n")


        print(f"\t E (N/mm2) hormigon prefabricado INICIO MIN: 4700 * sqrt(f'c) --> 4700 * sqrt({self.ui.tab4_line_horm_min_fc.text()}) = {self.ui.tab4_line_horm_min_e.text()} (N/mm2)")
        print(f"\t E (N/mm2) hormigon prefabricado INICIO MAX: 4700 * sqrt(f'c) --> 4700 * sqrt({self.ui.tab4_line_horm_max_fc.text()}) = {self.ui.tab4_line_horm_max_e.text()} (N/mm2)")
        print(f"\t E (N/mm2) hormigon prefabricado INICIO MIN: 4700 * sqrt(f'c) --> 4700 * sqrt({self.ui.tab4_line_horm_final_fc.text()}) = {self.ui.tab4_line_horm_final_e.text()} (N/mm2)")
        print(f"\t E (N/mm2) hormigon prefabricado INICIO MIN: 4700 * sqrt(f'c) --> 4700 * sqrt({self.ui.tab4_line_horm_insitu_fc.text()}) = {self.ui.tab4_line_horm_insitu_e.text()} (N/mm2)")
    else:
        print(f"No se encuentran resistencias para id_hormigon: {id_hormigon}")


def mat_fill_densidades_tipo_horm(self):
    ''' Llena LineEdits de densidades HORMIGON y ACERO en TAB4 materiales segun la seleccion de tipo de hormigon en comboBox '''
    '''
        * Densidad de hormigon depende de seleccion en ComboBox tipo hormigon
        * Densidad de acero depende de seleccion en ComboBox tipo hormigon
        * Densidad de concreto es siempre por defecto 2400 (kg/m3)
    '''
    
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
    
    self.ui.tab4_line_dens_concreto.setText(str(2400))



def mat_calc_save_ec(self):
    ''' calculo el valor de E_c usando valores de W_c y f'c. Despues guarda en variables los nuevos valores '''
    ''' Post-it naranja: 1440 (kg/m3) <= W_c <= 2560 (kg/m3) ''' # ?????

    ''' Formula E_c = W_c^(1.5) * 0.043 * sqrt(f'c)'''
    
    try:
        fc_pref_ini_min = float(self.ui.tab4_line_horm_min_fc.text())
        fc_pref_ini_max = float(self.ui.tab4_line_horm_max_fc.text())
        fc_pref_final = float(self.ui.tab4_line_horm_final_fc.text())
        fc_insitu = float(self.ui.tab4_line_horm_insitu_fc.text())
    except:
        print("Falta asignar valor algun para f'c\n")
        return
    try:
        valor_wc = float(self.ui.tab4_line_dens_concreto.text())
    except:
        print("Falta asignar valor para Wc\n")
        return

    print(f"\n\n--------------------------------------------")
    print(f"--------     Usando formula ACI     --------\n\n")
    
    print(f"\tValor considerado para Wc = {valor_wc}\n")

    print(f"\tValores para campos F'c\n")
    print(f"\t\tF'c horm. pref. ini. MIN = {fc_pref_ini_min}")
    print(f"\t\tF'c horm. pref. ini. MAX = {fc_pref_ini_max}")
    print(f"\t\tF'c horm. pref. FINAL = {fc_pref_final}")
    print(f"\t\tF'c horm. INSITU = {fc_insitu}\n")

    print(f"\n\tSe usa formula --> Ec =  Wc ^ 1.5 * 0.043 * sqrt(f'c). Con Wc = {valor_wc} (kg/m3) \n")


    ''' Calcula distintos Ec'''
    # Horm. Pref. Ini. MIN
    ec_horm_ini_min = (pow(valor_wc, 1.5) * 0.043 * math.sqrt(fc_pref_ini_min))
    ec_horm_ini_min = round(ec_horm_ini_min, 1)
    print(f"\tValor calculado para E_c usando [{valor_wc}^(1.5) * 0.043 * sqrt({fc_pref_ini_min})] = {ec_horm_ini_min} (N/mm2)")

    # Horm. Pref. Ini. MAX
    ec_horm_ini_max = (pow(valor_wc, 1.5) * 0.043 * math.sqrt(fc_pref_ini_max))
    ec_horm_ini_max = round(ec_horm_ini_max, 1)
    print(f"\tValor calculado para E_c usando [{valor_wc}^(1.5) * 0.043 * sqrt({fc_pref_ini_max})] = {ec_horm_ini_max} (N/mm2)")

    # Horm. Pref. FINAL
    ec_horm_final = (pow(valor_wc, 1.5) * 0.043 * math.sqrt(fc_pref_final))
    ec_horm_final = round(ec_horm_final, 1)
    print(f"\tValor calculado para E_c usando [{valor_wc}^(1.5) * 0.043 * sqrt({fc_pref_final})] = {ec_horm_final} (N/mm2)")

    # Horm. Insitu
    ec_horm_insitu = (pow(valor_wc, 1.5) * 0.043 * math.sqrt(fc_insitu))
    ec_horm_insitu = round(ec_horm_insitu, 1)
    print(f"\tValor calculado para E_c usando [{valor_wc}^(1.5) * 0.043 * sqrt({fc_insitu})] = {ec_horm_insitu} (N/mm2)")
    
    ''' Asigna rsultados a LineEdits'''
    self.ui.tab4_line_horm_min_e.setText(str(ec_horm_ini_min))
    self.ui.tab4_line_horm_max_e.setText(str(ec_horm_ini_max))
    self.ui.tab4_line_horm_final_e.setText(str(ec_horm_final))
    self.ui.tab4_line_horm_insitu_e.setText(str(ec_horm_insitu))