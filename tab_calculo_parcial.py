import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel, QComboBox
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from PySide6.QtCore import Qt

def setup_tab_calc_parcial(self):
    ''' Se ejecuta desde main cuando inicia app '''

    self.ui.tab5_btn_calcular.clicked.connect(lambda: calc_bruta(self))



def calc_bruta(self):
    ''' Asigna valores a LineEdits Area, cdg, inercia para Bruta t=0. '''
    ''' Son los mismos valores calculados en Tab1. Solo recupera .text() de lineEdits tab1 (Geometria) '''
    '''
        result_sum_area = area
        result_sum_ponderado = cdg
        result_sum_op = inercia
    '''

    valor_bruta_area = self.ui.result_sum_area.text()
    valor_bruta_cdg = self.ui.result_sum_ponderado.text()
    valor_bruta_inercia = self.ui.result_sum_op.text()

    self.ui.tab5_line_area_bruta.setText(valor_bruta_area)
    self.ui.tab5_line_cdg_bruta.setText(valor_bruta_cdg)
    self.ui.tab5_line_inercia_bruta.setText(valor_bruta_inercia)

    ''' Variables corresponden a resultados celdas en Excel Joaquin'''
    # TODO nombre variables 
    self.viga_area = 0
    self.barras_area = 0
    self.cordones_area = 0

    self.viga_cg = 0
    self.barras_cg = 0
    self.cordones_cg = 0

    self.viga_a_cg = 0
    self.barras_a_cg = 0
    self.cordones_a_cg = 0

    self.area_final = 0
    self.yinf_final = 0
    self.total_area_cg = 0

    self.operacion_tipo_viga = 0
    self.operacion_tipo_barras = 0
    self.operacion_tipo_cordones = 0
    self.operacion_final = 0

    calc_seccion_neta_inicial(self)
    seccion_homogeneizada_inicial(self)






def calc_seccion_neta_inicial(self):
    ''' Usa formulas de hoja calculos JOAQUIN. Pen-ultima tabla'''

    print("\t\t\t\n\n\n>>Datos usados para simple t = 0<<\n")

    print(f"Areas:")
    self.viga_area = self.ui.result_sum_area.text()
    self.cordones_area =self.ui.tab2_line_total_area.text()
    self.cordones_area = float(self.cordones_area) / 10000 # Pasa a metros
    self.barras_area = self.ui.tab3_line_area_barras.text()
    print(f"\t VIGA: {self.viga_area} m2")
    print(f"\t Arm. Activa: {self.cordones_area} m2")
    print(f"\t Arm. pasiva: {self.barras_area} mm2")

    print(f"\nY_inf:")
    self.viga_cg =self.ui.result_sum_ponderado.text()
    self.cordones_cg = self.ui.tab2_line_total_cdg_area.text()
    self.barras_cg = self.ui.tab3_line_yinf_barras.text()
    print(f"\t VIGA: {self.viga_cg} m")
    print(f"\t Arm. Activa (sin tpi): {self.cordones_cg} m")
    print(f"\t Arm. pasiva: {self.barras_cg} mm")

    print(f"\nInercia:")
    self.viga_inercia = self.ui.result_sum_op.text()
    self.cordones_inercia = self.ui.tab2_line_total_inercia.text()
    self.barras_inercia = self.ui.tab3_line_inercia_barras.text()
    print(f"\t VIGA: {self.viga_inercia} [?]")
    print(f"\t Arm. Activa (sin tpi): {self.cordones_inercia} m4")
    print(f"\t Arm. pasiva: {self.barras_inercia} m4")

    print("\n\n\n\n")

    print("A*cg de cada tipo:")
    # TODO que nombre usar para esta variable ??
    self.viga_a_cg = float(self.viga_area) * float(self.viga_cg)
    self.cordones_a_cg = float(self.cordones_area) * float(self.cordones_cg)
    self.barras_a_cg = float(self.barras_area) * float(self.barras_cg)
    print(f"\tA*Cg de viga: {self.viga_a_cg}")
    print(f"\tA*Cg de cordones: {self.cordones_a_cg}")
    print(f"\tA*Cg de barras: {self.barras_a_cg}")

    print("\n\n\n\n")

    self.area_final = float(self.viga_area) - (float(self.barras_area) + float(self.cordones_area))
    print(f"Area final con viga-barras-cordones: {self.area_final}")

    self.total_area_cg = float(self.viga_a_cg) + float(self.barras_a_cg) + float(self.cordones_a_cg)
    print(f"Sumatoria de Areas * Cg's: {self.total_area_cg}")

    self.yinf_final = float(self.total_area_cg) / float(self.area_final)
    print(f"Y_inf final: {self.yinf_final}")

    # TODO nombre de variables
    self.operacion_tipo_viga = float(self.viga_inercia) + float(self.viga_area) * pow((float(self.viga_cg) - float(self.yinf_final)), 2)
    print("Operacion para viga: ", self.operacion_tipo_viga)

    self.operacion_tipo_barras = float(self.barras_inercia) + float(self.barras_area) * pow((float(self.barras_cg) - float(self.yinf_final)), 2)
    print("Operacion para barras: ", self.operacion_tipo_viga)

    self.operacion_tipo_cordones = float(self.cordones_inercia) + float(self.cordones_area) * pow((float(self.cordones_cg) - float(self.yinf_final)), 2)
    print("Operacion para cordones: ", self.operacion_tipo_viga)

    self.operacion_final = float(self.operacion_tipo_viga) - (float(self.operacion_tipo_barras) + float(self.operacion_tipo_cordones))
    print("Resultado de operacion_final (Inercia de todo?): ", self.operacion_final)



def seccion_homogeneizada_inicial(self):
    ''' ultima tabla excel Joaquin '''

    # Ingresado por usr (o puede usar valor por defecto segun tipo de hormigon seleccionado en Cobmbo)
    # fc_ini = float(self.ui.tab4_line_horm_min_fc.text())
    fc_ini = 49.64448 # Valor en excel, Cambiar por LineEdit en Tab-Materiales # TODO usar fc variable
    
    # Usa formula pedida por claudio
    # ec_ini = float(self.ui.tab4_line_horm_min_e.text())
    ec_ini = 35622 # Valor en excel, Cambiar por LineEdit en Tab-Materiales # TODO usar ec variable

    cons_es = 200000 # unidad: MPa
    cons_eps = 198569 # Unidad: N/mm2 ... = 28800 KSI

    ns =  cons_es / ec_ini # Para steel -> Barras Pasivas
    nps = cons_eps / ec_ini # Para preStressed Steel -> Cordones Activos

    ''' Col area m2'''
    homo_area_viga_barra_cable = float(self.viga_area) - (float(self.barras_area) + float(self.cordones_area))
    homo_area_barras = float(self.barras_area) * ns
    homo_area_cordones = float(self.cordones_area) * nps

    homo_suma_areas = homo_area_viga_barra_cable + homo_area_cordones + homo_area_barras

    print("Valores equivalente COL AREA:")
    print("\t\t Area Viga-Barras-Cordones: ", homo_area_viga_barra_cable)
    print("\t\t Area barras: ", homo_area_barras)
    print("\t\t Area Cordones: ", homo_area_cordones)
    print("\t\t Area sumatoria: ", homo_suma_areas)

    '''Col Y_inf'''
    print("\n\nValores equivalente COL Y_inf")
    homo_yinf_viga_barra_cable = self.total_area_cg / self.area_final
    homo_yinf_barra = float(self.barras_cg)
    homo_yinf_cordones = float(self.cordones_cg)

    print("\t\tY_inf viga-barras-cordones: ", homo_yinf_viga_barra_cable)
    print("\t\tY_inf barras: ", homo_yinf_barra)
    print("\t\tY_inf cordones: ", homo_yinf_cordones)

    ''' COL Area * Cg de cada tipo '''
    homo_viga_barra_cordon_a_cg = homo_area_viga_barra_cable * homo_yinf_viga_barra_cable
    homo_barras_a_cg = homo_area_barras * homo_yinf_barra
    homo_cordones_a_cg = homo_area_cordones * homo_yinf_cordones

    homo_suma_a_cg = homo_viga_barra_cordon_a_cg + homo_barras_a_cg + homo_cordones_a_cg

    print("\n\nValores equivalente COL Area * Cg")
    print("\t\tA * Cg Vigas-Barras-Cables: ", homo_viga_barra_cordon_a_cg)
    print("\t\tA * Cg Barras: ", homo_barras_a_cg)
    print("\t\tA * Cg Cables: ", homo_cordones_a_cg)
    print("\t\tA * Cg SUMATORIA: ", homo_suma_a_cg)


    ''' Col Yinf. ultima fila '''
    homo_total_yinf = homo_suma_a_cg / homo_suma_areas # No es realmente la sumatoria de col Y_inf TODO Que nombre asignarle ???
    print("\n\n COL Y_inf Ultima celda")
    print("\t\tUltima celda Y_inf: ", homo_total_yinf)


    ''' COL Inercia tipo '''
    homo_inercia_viga_barra_cordon = float(self.operacion_final)
    homo_inercia_barras = float(self.barras_inercia) * ns
    homo_inercia_cordones = float(self.cordones_inercia) * nps

    print("\n\nValores equivalentes a COL Inercia")
    print("\t\t Inercia Viga-Barras-Cables: ", homo_inercia_viga_barra_cordon)
    print("\t\t Inercia Barras: ", homo_inercia_barras)
    print("\t\t Inercia Cables: ", homo_inercia_cordones)

    ''' Col Operacion final '''
    homo_operacion_viga_barra_cordon = homo_inercia_viga_barra_cordon + homo_area_viga_barra_cable * pow((homo_yinf_viga_barra_cable - homo_total_yinf), 2)
    homo_operacion_barras = homo_inercia_barras + homo_area_barras * pow((homo_yinf_barra - homo_total_yinf), 2)
    homo_operacion_cordones = homo_inercia_cordones + homo_area_cordones * pow((homo_yinf_cordones - homo_total_yinf), 2)

    # SUMATORIA DE TODAS OPERACIONES
    homo_operacion_final = homo_operacion_viga_barra_cordon + homo_operacion_barras + homo_operacion_cordones

    print("\n\nValores equivalentes COL Operacion I + A*r^2")
    print("\t\tOperacion vigas-barras-cables: ", homo_operacion_viga_barra_cordon)
    print("\t\tOperacion barras: ", homo_operacion_barras)
    print("\t\tOperacion cables: ", homo_operacion_cordones)

    print("\n\t\t\t >> Tabla seccion homogeneizada inicial<<\n")
    print("resultado de operacion final en seccion homogenea: ", homo_operacion_final) # Inercia

    self.ui.tab5_line_area_t0.setText(f"{homo_suma_areas}")
    self.ui.tab5_line_cdg_t0.setText(f"{homo_total_yinf}")
    self.ui.tab5_line_inercia_t0.setText(f"{homo_operacion_final}")






















    