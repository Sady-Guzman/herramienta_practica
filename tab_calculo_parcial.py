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

    calc_inercia_cordones(self)



def calc_inercia_cordones(self):
    ''' Calculo inercia de armadura activa. '''
    ''' No se calcula inercia por 'seccion' porque la inercia de un solo cordon es despreciable '''
    ''' Se calcula firectamente (I + A * r^2 [m4]) '''
    ''' I(no existe) + Area(en seccion -> Se calcula con Cantidad*AreaCordon) * ((Y_inf(seccion) - CDG)^2)'''

    ''' Inercia total = SUM((Cg_cota - Cg_total)^2)'''

    print("\n\n\n\n \t\t\t CALC_INERCIA_CORDONES() \n\n")

    dict_areas_cota = {}

    for index_cota, cota in enumerate(self.dynamic_cotas):
        cota_value = float(self.dynamic_cotas[index_cota].text())  # Convert to float
        dict_areas_cota[cota_value] = 0  # Initialize total area for this cota

        print(f"\n\nPara cota {cota_value}:")

        for index_cord, cordon in enumerate(self.dynamic_cordones_arm_act):
            cordon = self.dynamic_cordones_arm_act[index_cord]

            num_cords = int(cordon['num_cordones'][index_cota].text())  # Convert to int
            area_cordon = float(cordon['area'].text())  # Convert to float

            total_area = num_cords * area_cordon  # Compute total area

            dict_areas_cota[cota_value] += total_area  # Add to total for this cota

            print(f"  - Cordon {index_cord} --> Num_cords = {num_cords}, Área Cordon = {area_cordon}, Total_Area = {total_area}")

    # Print summarized results
    print("\n\nResumen de áreas por cota:")
    for cota, area_total in dict_areas_cota.items():
        print(f"Cota {cota}m → Área total = {area_total} cm²")























def calc_simple_t0(self):
    ''' Usa formulas de hoja calculos JOAQUIN. '''

    