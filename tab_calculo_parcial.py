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

    calc_simple_t0(self)




def calc_simple_t0(self):
    ''' Usa formulas de hoja calculos JOAQUIN. '''

    print("\t\t\t\n\n\n>>Datos usados para simple t = 0<<\n")

    print(f"Areas:")
    viga_area = self.ui.result_sum_area.text()
    cordones_area =self.ui.tab2_line_total_area.text()
    barras_area = self.ui.tab3_line_area_barras.text()
    print(f"\t VIGA: {viga_area} m2")
    print(f"\t Arm. Activa: {cordones_area} m2")
    print(f"\t Arm. pasiva: {barras_area} mm2")

    print(f"\nY_inf:")
    viga_cg =self.ui.result_sum_ponderado.text()
    cordones_cg = self.ui.tab2_line_total_cdg_area.text()
    barras_cg = self.ui.tab3_line_yinf_barras.text()
    print(f"\t VIGA: {viga_cg} m")
    print(f"\t Arm. Activa (sin tpi): {cordones_cg} m")
    print(f"\t Arm. pasiva: {barras_cg} mm")

    print(f"\nInercia:")
    viga_inercia = self.ui.result_sum_op.text()
    cordones_inercia = self.ui.tab2_line_total_inercia.text()
    barras_inercia = self.ui.tab3_line_inercia_barras.text()
    print(f"\t VIGA: {viga_inercia} [?]")
    print(f"\t Arm. Activa (sin tpi): {cordones_inercia} m4")
    print(f"\t Arm. pasiva: {barras_inercia} m4")

    print("\n\n\n\n")

    print("A*cg de cada tipo:")
    viga_a_cg = viga_area * viga_a_cg
    cordones_a_cg = cordones_area * cordones_cg
    barras_a_cg = barras_area * barras_inercia
    print(f"\tA*Cg de viga: {viga_a_cg}")
    print(f"\tA*Cg de cordones: {cordones_a_cg}")
    print(f"\tA*Cg de barras: {barras_a_cg}")

    





    