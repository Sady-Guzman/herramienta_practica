import sys
import math

from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel, QComboBox
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from PySide6.QtCore import Qt

def setup_tab_calc_parcial(self):
    ''' Se ejecuta desde main cuando inicia app '''

    self.ui.tab5_btn_calcular.clicked.connect(lambda: calc_propiedades_tabla(self))
    


''' Calculo para Bruta, Simple t = 0, Simple t = 00 '''
def calc_propiedades_tabla(self):
    ''' Asigna valores a LineEdits Area, cdg, inercia para Bruta t=0. '''
    ''' Son los mismos valores calculados en Tab1. Solo recupera .text() de lineEdits tab1 (Geometria) '''
    '''
        result_sum_area = area
        result_sum_ponderado = cdg
        result_sum_op = inercia
    '''

    ''' Asigna resultados para seccion Bruta t = 0'''
    valor_bruta_area = self.ui.result_sum_area.text()
    valor_bruta_cdg = self.ui.result_sum_ponderado.text()
    valor_bruta_inercia = self.ui.result_sum_op.text()

    self.ui.tab5_line_area_bruta.setText(valor_bruta_area)
    self.ui.tab5_line_cdg_bruta.setText(valor_bruta_cdg)
    self.ui.tab5_line_inercia_bruta.setText(valor_bruta_inercia)

    ''' Variables corresponden a resultados celdas en Excel Joaquin'''
    ''' Se usan para calcular Simple t = 0 '''
    # TODO Preguntar por nombres mas descriptivos a Joaquin cuando tenga tiempo
    #  
    self.viga_area = 0
    self.barras_area = 0
    self.cordones_area = 0

    self.viga_cg = 0
    self.barras_cg = 0
    self.cordones_cg = 0

    self.viga_a_cg = 0
    self.barras_a_cg = 0
    self.cordones_a_cg = 0

    self.area_final = 0 # Para t= 0 (Hormigon presentaso + Armadura activa + Armadura Pasiva)
    self.yinf_final = 0 # Para t= 0 (Hormigon presentaso + Armadura activa + Armadura Pasiva)
    self.total_area_cg = 0 # Para t= 0 (Hormigon presentaso + Armadura activa + Armadura Pasiva)

    self.operacion_tipo_viga = 0
    self.operacion_tipo_barras = 0
    self.operacion_tipo_cordones = 0
    self.operacion_final = 0

    

    print("\n\n\n\n\t\t --------------------------------------------------------------------------------------------------------------------")
    print("\t\t ----------------------------------------     DATOS CALCULO PARCIAL      --------------------------------------------")
    print("\t\t --------------------------------------------------------------------------------------------------------------------\n\n")

    print("\n\n\n\n ----------------------------------------------------------------------------------")
    print(" -----------------------   CALCULO SECCION BRUTA T=0  ------------------------------")
    print(" -----------------------------------------------------------------------------------")
    
    print("\t Calculos de altura, area, CDG, inercia registrados en pestana geometria.\n")
    

    ''' Hace calculos para simple t = 0 '''

    ''' Implementacion de pasos para calcular t = 0 estan separados en 2 metodos, comunicados por variables accesibles usando self. 
        / Resultados de estos 2 pasos tambien son usados en calculos para t = 00.
        / Estos calculos estan basados e EXCEL de JOAQUIN.
    '''

    calc_seccion_neta_inicial(self) # Primer paso t = 0
    calc_seccion_homogeneizada_inicial(self)  # segundo paso (final) para t = 0

    ''' Pasos 1 y 2 para t = 00 estan implementados en un mismo metodo para simplificar uso de resultados entre los pasos. '''
    calc_t00(self) # Paso 1 y Paso 2 para calcular T=00. Basado en tablas 5 y 6 de EXCEL CLAUDIO





''' Calculo Parcial Primer paso para Simple t = 0 '''
def calc_seccion_neta_inicial(self):
    ''' Usa formulas de hoja calculos JOAQUIN. Pen-ultima tabla'''

    print("\n\n\n\n ------------------------------------------------------------------------------------")
    print(" ----------------------- CALCULO SECCION SIMPLE T = 0  ------------------------------")
    print(" ------------------------------------------------------------------------------------\n")

    print("\n\n-----------------------------------------")
    print("----> PASO 1: SECCION NETA INICIAL: <---- \n")


    try: 
        print(f"AREAS:")
        self.viga_area = self.ui.result_sum_area.text()
        self.cordones_area =self.ui.tab2_line_total_area.text()
        self.cordones_area = float(self.cordones_area) / 10000 # Pasa a metros^2 AREA ARMADURA ACTIVA, que en pestana esta originalmente en cm2
        self.barras_area = self.ui.tab3_line_area_barras.text()
        print(f"\t VIGA: {self.viga_area} m2")
        print(f"\t Arm. Activa: {self.cordones_area} m2")
        print(f"\t Arm. pasiva: {self.barras_area} m2\n")
    except:
        print("\t>>> Falta valor de area en una o mas de las siguienes pestanas: (GEOMETRIA, ARM. ACTIVA, ARM. PASIVA) para hacer calculo de seccion_neta_inicial.")
        return

    try:
        print(f"\nCENTRO DE GRAVEDAD:")
        self.viga_cg =self.ui.result_sum_ponderado.text()
        self.cordones_cg = self.ui.tab2_line_total_cdg_area.text()
        self.barras_cg = self.ui.tab3_line_yinf_barras.text()
        print(f"\t VIGA: {self.viga_cg} m")
        print(f"\t Arm. Activa (sin tpi): {self.cordones_cg} m")
        print(f"\t Arm. pasiva: {self.barras_cg} m\n")
    except:
        print("\t>>> Falta calcular Y_inf en una o mas de las siguienes pestanas: (GEOMETRIA, ARM. ACTIVA, ARM. PASIVA) para hacer calculo de seccion_neta_inicial.")
        return

    try:
        print(f"\nINERCIA:")
        self.viga_inercia = self.ui.result_sum_op.text()
        self.cordones_inercia = self.ui.tab2_line_total_inercia.text()
        self.barras_inercia = self.ui.tab3_line_inercia_barras.text()
        print(f"\t VIGA: {self.viga_inercia} m4")
        print(f"\t Arm. Activa (sin tpi): {self.cordones_inercia} m4")
        print(f"\t Arm. pasiva: {self.barras_inercia} m4\n")
    except:
        print("\t>>> Falta calcular Inercia en una o mas de las siguienes pestanas: (GEOMETRIA, ARM. ACTIVA, ARM. PASIVA) para hacer calculo de seccion_neta_inicial.")
        return
    

    try:
        print("\nOPERACION: (A * cg) para cada tipo:")

        # TODO que nombre usar para esta variable ??, Solo dejar expresada operacion ?

        self.viga_a_cg = float(self.viga_area) * float(self.viga_cg)
        self.cordones_a_cg = float(self.cordones_area) * float(self.cordones_cg)
        self.barras_a_cg = float(self.barras_area) * float(self.barras_cg)

        print(f"\t A * Cg de viga     --> {float(self.viga_area)} m2 * {float(self.viga_cg)} m = {self.viga_a_cg} m3")
        print(f"\t A * Cg de cordones --> {float(self.cordones_area)} m2 * {float(self.cordones_cg)} m = {self.cordones_a_cg} m3")
        print(f"\t A * Cg de barras   --> {float(self.barras_area)} m2 * {float(self.barras_cg)} m = {self.barras_a_cg} m3\n")
    except:
        print("\t>>> Falta calcular A*cg en geometria, cordones o barras para hacer calculo de seccion_neta_inicial.")
        return

    
    ''' TOTAL de AREA * CDG'''
    self.total_area_cg = float(self.viga_a_cg) + float(self.barras_a_cg) + float(self.cordones_a_cg)
    print(f"\t SUMATORIA de resultados OPERACION (Areas * Cg's) --> {float(self.viga_a_cg)} m3 + {float(self.barras_a_cg)} m3 + {float(self.cordones_a_cg)} m3 = {self.total_area_cg} m3 \n")

    ''' TOTAL AREA EQUIVALENTE VIGA, CORDONES, BARRAS '''
    self.area_final = float(self.viga_area) - (float(self.barras_area) + float(self.cordones_area))
    print(f"Area final considerando viga, arm. activa/pasiva: AREA_viga - (Area_barras + AREA_cordones) --> {float(self.viga_area)} m2 - ({float(self.barras_area)} m2 + {float(self.cordones_area)} m2) = {self.area_final} m2 \n")

    ''' CENTRO DE GRAVEDAD FINAL COMPUESTO CONSIDERANDO VIGA, CORDONES, BARRAS '''
    self.yinf_final = float(self.total_area_cg) / float(self.area_final)
    print(f"CENTRO DE GRAVEDAD FINAL COMPUESTO (considerando viga, arm. activa/pasiva): SUM(Operacion_Area * CG) / Area_eq --> {float(self.total_area_cg)} m3 / {float(self.area_final)} m2 = {self.yinf_final} m \n")


    # TODO pedir nombre de variables de operacion I + A*r^2 w/ unidad: [m4]

    print("\nOperacion (I + A * r^2) para cada tipo de material: \n")

    ''' VIGA '''
    self.operacion_tipo_viga = float(self.viga_inercia) + float(self.viga_area) * pow((float(self.viga_cg) - float(self.yinf_final)), 2)
    print(f"\t Para viga: Inercia_viga + Area_viga * (Y_inf_viga - Y_inf_compuesto) ^ 2 -> {float(self.viga_inercia)} m4 + {float(self.viga_area)} m2 * ({float(self.viga_cg)} m - {float(self.yinf_final)} m)^2 = {self.operacion_tipo_viga} m4 \n")

    ''' BARRAS (arm. pasiva) '''
    self.operacion_tipo_barras = float(self.barras_inercia) + float(self.barras_area) * pow((float(self.barras_cg) - float(self.yinf_final)), 2)
    print(f"\t Para barras: Inercia_barras + Area_barras * (Y_inf_barras - Y_inf_compuesto) ^ 2 -> {float(self.barras_inercia)} m4 + {float(self.barras_area)} m2 * ({float(self.barras_cg)} m - {float(self.yinf_final)} m)^2 = {self.operacion_tipo_viga} m4 \n")

    ''' CORDONES (arm. activa)'''
    self.operacion_tipo_cordones = float(self.cordones_inercia) + float(self.cordones_area) * pow((float(self.cordones_cg) - float(self.yinf_final)), 2)
    print(f"\t Para cordones: Inercia_cordones + Area_cordones * (Y_inf_cordones - Y_inf_compuesto) ^ 2 -> {float(self.cordones_inercia)} m4 + {float(self.cordones_area)} m2 * ({float(self.cordones_cg)} m - {float(self.yinf_final)} m)^2 = {self.operacion_tipo_viga} m4 \n")

    ''' OPERACION PARA RESULTADO COMPUESTO '''
    self.operacion_final = float(self.operacion_tipo_viga) - (float(self.operacion_tipo_barras) + float(self.operacion_tipo_cordones))
    print(f"\n\t ---> RESULTADO COMPUESTO considerando (Viga, Arm. pasiva/activa) (R: result): R_viga - (R_barras + R_cordones) -> {float(self.operacion_tipo_viga)} m4 - ({float(self.operacion_tipo_barras)} m4 + {float(self.operacion_tipo_cordones)} m4) = {self.operacion_final} m4 <---\n")




''' Calculo Parcial simple t = 0 paso final'''
def calc_seccion_homogeneizada_inicial(self):
    ''' ultima tabla excel Joaquin '''

    print("\n\n-------------------------------------------------- \n")
    print("----> PASO 2: SECCION HOMOGENEIZADA INICIAL: <---- \n")


    ''' F'c y Ec son obtenidos de PESTANA MATERIALES '''
    # Ingresado por usr (o puede usar valor por defecto segun tipo de hormigon seleccionado en Cobmbo)
    try:
        fc_ini = float(self.ui.tab4_line_horm_min_fc.text())
        
        # Usa formula pedida por claudio
        ec_ini = float(self.ui.tab4_line_horm_min_e.text())
    except:
        print("Faltan datos f'c y/o Ec para poder hacer calculo.")
        return



    ''' CONSTANTES definidas por usuario en GUI pestana materiales '''
    cons_es = float(self.ui.tab3_line_cons_es.text())
    cons_eps = float(self.ui.tab3_line_cons_eps.text())

    ns =  cons_es / ec_ini # Para steel -> Barras Pasivas
    nps = cons_eps / ec_ini # Para preStressed Steel -> Cordones Activos


    print(f"Valores de resistencia y modulos\n")
    print(f"\t Valor F'c (prefabricado INICIAL MINIMO): {fc_ini} (N/mm2)")
    print(f"\t Valor Ec (prefabricado INICIAL MINIMO) : {ec_ini} (N/mm2) (Resultado calculo en pestana materiales)")
    print(f"\t Valor ns: constante_Es / Ec_inicial   --> {cons_es} / {ec_ini} = {ns}")
    print(f"\t Valor nps: constante_Eps / Ec_inicial --> {cons_eps} / {ec_ini} = {nps}\n")


    ''' -- Col area m2 -- '''
    print("\nAREAS:\n")
    try:
        homo_area_viga_barra_cable = float(self.viga_area) - (float(self.barras_area) + float(self.cordones_area))
        homo_area_barras = float(self.barras_area) * ns
        homo_area_cordones = float(self.cordones_area) * nps

        homo_suma_areas = homo_area_viga_barra_cable + homo_area_cordones + homo_area_barras

        print(f"\t Area Viga - (Barras + Cordones) -> {float(self.viga_area)} m2 - ({float(self.barras_area)} m2 + {float(self.cordones_area)} m2) = {homo_area_viga_barra_cable} m2 \n")
        print(f"\t Area solo barras: Area * ns -> {float(self.barras_area)} m2 * {ns} = {homo_area_barras} m2")
        print(f"\t Area solo cordones: Area * nps -> {float(self.cordones_area)} m2 * {nps} = {homo_area_cordones} m2\n")
        print(f"\t Area SUMATORIA: A_viga + A_barras + A_cordones -> {homo_area_viga_barra_cable} m2 + {homo_area_barras} m2 + {homo_area_cordones} m2 = {homo_suma_areas} m2 \n")
    except:
        print("\t>>> Faltan datos para hacer calculo de seccion_homogeneizada_inicial.\n")
        return


    ''' -- Col Y_inf -- '''
    print("\nCentros de Gravedad:\n")
    try:
        homo_yinf_viga_barra_cable = self.total_area_cg / self.area_final
        homo_yinf_barra = float(self.barras_cg)
        homo_yinf_cordones = float(self.cordones_cg)

        print(f"\t CDG viga, barras, cordones (Usa resultados PASO 1: Secc NETA INI): SUM(A * CDG) / Area eq -> {self.total_area_cg} m3 / {self.area_final} m2 = {homo_yinf_viga_barra_cable} m\n")
        print(f"\t Y_inf solo barras: Valor calculado en pestana ARM. PASIVA. -> {homo_yinf_barra} m")
        print(f"\t Y_inf solo cordones: Valor calculado en pestana ARM. ACTIVA. -> {homo_yinf_cordones} m\n")
    except:
        print("\t>>> Faltan datos para hacer calculo de seccion_homogeneizada_inicial. \n")
        return

    ''' -- COL Area * Cg de cada tipo -- '''
    print("OPERACION AREA * CG para cada tipo\n")
    try:
        homo_viga_barra_cordon_a_cg = homo_area_viga_barra_cable * homo_yinf_viga_barra_cable
        homo_barras_a_cg = homo_area_barras * homo_yinf_barra
        homo_cordones_a_cg = homo_area_cordones * homo_yinf_cordones

        homo_suma_a_cg = homo_viga_barra_cordon_a_cg + homo_barras_a_cg + homo_cordones_a_cg


        print(f"\t Vigas - (Barras + Cables): A_viga * CDG_viga -> {homo_area_viga_barra_cable} m2 * {homo_yinf_viga_barra_cable} m = {homo_viga_barra_cordon_a_cg} m3")

        print(f"\t Barras: A_barra * CDG_barra -> {homo_area_barras} m2 * {homo_yinf_barra} m = {homo_barras_a_cg} m3")

        print(f"\t Cables: A_cables * CDG_cables -> {homo_area_cordones} m2 * {homo_yinf_cordones} m = {homo_cordones_a_cg} m3 \n")

        print(f"\n\t SUMATORIA de resultados -> {homo_viga_barra_cordon_a_cg} m3 + {homo_barras_a_cg} m3 + {homo_cordones_a_cg} m3 = {homo_suma_a_cg} m3\n")
    except:
        print("\t>>> Faltan datos para hacer calculo de seccion_homogeneizada_inicial.\n")
        return


    ''' Col Yinf. ultima fila (En excel joaquin) '''
    print("OPERACION SUM(A * CDG) / SUM(AREAS)\n")
    try:
        homo_total_yinf = homo_suma_a_cg / homo_suma_areas
        print(f"\t-> {homo_suma_a_cg} m3 / {homo_suma_areas} m2 = {homo_total_yinf} m \n")
    except:
        print("\t>>> Faltan datos para hacer calculo de seccion_homogeneizada_inicial.\n")
        return


    ''' COL Inercia tipo '''
    print("INERCIAS:\n")
    try:
        homo_inercia_viga_barra_cordon = float(self.operacion_final)
        homo_inercia_barras = float(self.barras_inercia) * ns
        homo_inercia_cordones = float(self.cordones_inercia) * nps

        print(f"\t Viga-Barras-Cables: Inercia final de PASO 1: Secc NETA INI -> {homo_inercia_viga_barra_cordon} m4")
        print(f"\t Barras: I_barra (de paso1) * ns -> {float(self.barras_inercia)} m4 * {ns} = {homo_inercia_barras} m4 ")
        print(f"\t Cordones: I_cordon (de paso1) * nps -> {float(self.cordones_inercia)} m4 * {nps} = {homo_inercia_cordones} m4 \n")
    except:
        print("\t>>> Faltan datos para hacer calculo de seccion_homogeneizada_inicial.\n")
        return
    

    ''' Col Operacion final '''
    print("OPERACION I + A * (tipo_CDG - (SUM(A * CDG) / SUM(AREAS)) ^ 2")
    try:
        homo_operacion_viga_barra_cordon = homo_inercia_viga_barra_cordon + homo_area_viga_barra_cable * pow((homo_yinf_viga_barra_cable - homo_total_yinf), 2)
        homo_operacion_barras = homo_inercia_barras + homo_area_barras * pow((homo_yinf_barra - homo_total_yinf), 2)
        homo_operacion_cordones = homo_inercia_cordones + homo_area_cordones * pow((homo_yinf_cordones - homo_total_yinf), 2)

        # SUMATORIA DE TODAS OPERACIONES
        homo_operacion_final = homo_operacion_viga_barra_cordon + homo_operacion_barras + homo_operacion_cordones

        print(f"\t vigas-barras-cordones -> {homo_inercia_viga_barra_cordon} m4 + {homo_area_viga_barra_cable} m2 * ({homo_yinf_viga_barra_cable} m - {homo_total_yinf} m) ^ 2 = {homo_operacion_viga_barra_cordon} m4 ")
        print(f"\t barras -> {homo_inercia_barras} m4 + {homo_area_barras} m2 * ({homo_yinf_barra} m - {homo_total_yinf} m) ^ 2 = {homo_operacion_barras} m4 ")
        print(f"\t cordones -> {homo_inercia_cordones} m4 + {homo_area_cordones} m2 * ({homo_yinf_cordones} m - {homo_total_yinf} m) ^ 2 = {homo_operacion_cordones} m4 \n")


        print(f"\t SUMATORIA resultados -> {homo_operacion_viga_barra_cordon} m4 + {homo_operacion_barras} m4 + {homo_operacion_cordones} m4 = {homo_operacion_final} m4\n") # Inercia
    except:
        print("\t>>> Faltan datos para hacer calculo de seccion_homogeneizada_inicial.\n")
        return

    print("RESULTADOS DE PROPIEDADES para SIMPLE t = 0:")
    print(f"\t AREA final    -> {homo_suma_areas} m2")
    print(f"\t CDG final     -> {homo_total_yinf} m")
    print(f"\t INERCIA final -> {homo_operacion_final} m4\n\n")

    self.ui.tab5_line_area_t0.setText(f"{round(homo_suma_areas, 7)}")
    self.ui.tab5_line_cdg_t0.setText(f"{round(homo_total_yinf, 7)}")
    self.ui.tab5_line_inercia_t0.setText(f"{round(homo_operacion_final, 7)}")


''' ===================================================================================================================== '''

''' CALCULO SECCION SIMPLE t = 00'''
def calc_t00(self):

    print("\n\n--------------------------------------------------- ")
    print("----> PASO 1: SECCION COMPUESTA NETA INICIAL: <---- \n")

    ''' Valores para concreto insitu, VIGA,Lc, Sw, e, voladizo '''
    try:
        valor_luz_calculo = float(self.ui.tab6_line_luz_calculo.text())
        valor_sw = float(self.ui.tab6_line_sw.text())
        valor_espesor_losa = float(self.ui.tab6_line_espesor.text())
        # valor_voladizo = float(self.ui.tab6_line_voladizo.text())
    except:
        print("\n>>> Falta uno o mas de los siguientes valores: Luz de Calculo, Sw, Espesor losa insitu. Por lo que no se puede calcular t=00. \n")
        return

    print(f"\nValores de inputs en pestana LUZ DE CALCULO:")
    print(f"\tLc (Luz calculo) = {valor_luz_calculo} m")
    print(f"\tSw (Dist. entre Almas) = {valor_sw} m")
    print(f"\te (Espesor de losa) = {valor_espesor_losa}m \n")
    # print(f"\tD (largo de voladizo) = {valor_voladizo} m")



    ''' Trapecios de hormigon insitu existentes '''
    print("\nTrapecio de hormigon INSITU en GEOMETRIA:")
    for i, layout in enumerate(self.dynamic_layouts):
        tipo_hormigon = layout['combo_insitu'].currentText()

        if tipo_hormigon == "Insitu":
            print(f"\tNombre: {layout['name_label'].text()}")
            print(f"\tBi: {layout['bi_line'].text()}")
            print(f"\tAltura: {layout['altura_line'].text()}")
            print(f"\tÁrea: {layout['area_line'].text()} \n")



    ''' Encuentra ancho de alma (Trapecio mas angosto en self.dynamic_layouts, que tenga Bi y Bs iguales, y que no esta ni en el primer ni ultimo lugar del diciconario) '''
    print("\n Ancho de alma:")
    menor_ancho = 99999
    for i, layout in enumerate(self.dynamic_layouts):
        if i == 0 or i == len(self.dynamic_layouts) - 1:
            continue

        if layout['bi_line'].text() == layout['bs_line'].text():
            ancho = float(layout['bi_line'].text())
            if ancho < menor_ancho:
                menor_ancho = ancho
                nombre = layout['name_label'].text()
    
    ''' Si se entra a este IF, significa que hay un problema al encontrar el trapecio que corresponde al ALMA. (Problema de geometria) '''
    if menor_ancho == 99999:
        print(f"No se encontró ancho de alma.  (POR AHORA ANCHO_ALMA NO SE USA EN NINGUN CALCULO.)\n")
        # return # No se usa return porque ancho de alma no se usa, Por lo tanto no va a haber ningun crash si la funcion sigue avanzando.
    else:
        print(f"\t Ancho de alma: Trapecio mas angosto en geometria -> {menor_ancho} m, en layout {nombre}. (POR AHORA ANCHO_ALMA NO SE USA EN NINGUN CALCULO.)\n")



    ''' Recupera valores de F'c para viga y para insitu '''
    fc_viga = float(self.ui.tab4_line_horm_final_fc.text())
    fc_losa = float(self.ui.tab4_line_horm_insitu_fc.text())
    n_compresion = math.sqrt(fc_viga/fc_losa)

    print(f"\nValores de f'c VIGA, LOSA y razon 'n' en TAB MATERIALES:")
    print(f"\t f'c hormigon prefabricado FINAL (VIGA) = {fc_viga} (N/mm2) ")
    print(f"\t f'c hormigon insitu (LOSA) = {fc_losa} (N/mm2) ")
    print(f"\t n_compresion: SQRT(f'c(Viga) / F'c(Losa)) = {n_compresion}\n")


    ''' Propiedades de viga bruta. '''
    viga_altura = float(self.ui.result_sum_altura.text())
    viga_area = float(self.ui.result_sum_area.text())
    viga_yinf = float(self.ui.result_sum_ponderado.text())
    viga_inercia = float(self.ui.result_sum_op.text())

    print(f"\nPropiedades de VIGA BRUTA:")
    print(f"\t Altura = {viga_altura} m")
    print(f"\t Area = {viga_area} m2")
    print(f"\t Y_inf = {viga_yinf} m")
    print(f"\t Inercia = {viga_inercia} m4\n")



    ''' Valores para tabla ACI 6.3.2.1 '''
    ''' B_eff de losa '''

    print(f"\nComparaciones TABLA ACI 6.3.2.1 de valor minimo:")
    
    ''' Beff AMBOS LADOS '''
    print(f"\tAMBOS LADOS: (Minimo de estos valores)  ")
    print(f"\t\t 8*h (espesor losa)     -> ({valor_espesor_losa} * 8) =\t{round(valor_espesor_losa * 8, 3)} m")
    print(f"\t\t Sw/2 (separacion almas -> ({valor_sw} / 2) =\t{round(valor_sw / 2, 3)} m")
    print(f"\t\t Lc/8 (luz calculo)     -> ({valor_luz_calculo} / 8) =\t{round(valor_luz_calculo / 8, 3)} m\n")

    ''' Beff UN LADO '''
    print(f"\tSOLO UN LADO: (Minimo de estos valores) ")
    print(f"\t\t 6*h (espesor losa)->({valor_espesor_losa} * 6) =\t{round(valor_espesor_losa * 6, 3)} m")
    print(f"\t\t Sw/2 (separacion almas)->({valor_sw} / 2) =\t{round(valor_sw / 2, 3)} m")
    print(f"\t\t Lc/12 (luz calculo)->({valor_luz_calculo} / 12) =\t{round(valor_luz_calculo / 12, 3)} m\n")

    ancho_efectivo_losa_ambos = float(min(valor_espesor_losa * 8, valor_sw / 2, valor_luz_calculo / 8))
    ancho_efectivo_losa_uno = float(min(valor_espesor_losa * 6, valor_sw / 2, valor_luz_calculo / 12))

    self.ui.tab5_line_beff_ambos.setText(f"{round(ancho_efectivo_losa_ambos, 4)}")
    self.ui.tab5_line_beff_uno.setText(f"{round(ancho_efectivo_losa_uno, 4)}")

    print(f"\nANCHO EFECTIVO:")
    print(f"\t B_eff (Valor minimo para ambos lados) = {ancho_efectivo_losa_ambos} m")
    print(f"\t B_eff (Valor minimo para un lado) = {ancho_efectivo_losa_uno} m\n")



    ''' Area losa '''
    ''' Area de trapecio insitu '''
    ''' Solo sirve si se usa un solo trapecio insitu (Osea una sola losa) No se esta controlando que usuario no agregue mas de un trapecio insitu '''

    ''' TODO altura de trapecio tipo insitu y valor ingresado en tab6 'espesor' Son lo mismo ??? '''
    existe_insitu = False

    for i, layout in enumerate(self.dynamic_layouts):
        tipo_hormigon = layout['combo_insitu'].currentText()

        if tipo_hormigon == "Insitu":
            # print(f"\n Para layout {i}")
            # print("\tTrapecio de hormigon Insitu:")
            # print(f"\tNombre: {layout['name_label'].text()}")
            # print(f"\tBi: {layout['bi_line'].text()}")
            # print(f"\tAltura: {layout['altura_line'].text()}")
            # print(f"\tÁrea: {layout['area_line'].text()}")
            ancho_real_losa = float(layout['bi_line'].text())
            existe_insitu = True
    
    if existe_insitu == False:
        print(">>> No se encuentra ningun bloque de hormigon insitu en la geometria, No se continua con calculo t = 00. \n")
        return

    area_losa = ancho_real_losa * valor_espesor_losa
    print("\nSe condisidera valor ingresado en pestana Luz de Calculo para Espesor de Losa para calculos, NO alto de trapecio insitu en pestana Geometria. ANCHO corresponde a Bi en Geometria.\n")
    print(f"AREA DE LOSA: (Ancho real losa * Espesor losa) -> ({ancho_real_losa} m * {valor_espesor_losa} m) = {area_losa} m2")
    
    area_equivalente_losa = (ancho_efectivo_losa_ambos * valor_espesor_losa) / n_compresion
    print(f"\nAREA EQUIVALENTE SOLO LOSA (con B_eff): (B_eff (Ambos Lados) * espesor_losa) / n_compresion):")
    print(f"\t({ancho_efectivo_losa_ambos} * {valor_espesor_losa}) / {n_compresion} = {area_equivalente_losa} m2 \n")


    ''' A_eq viga/losa '''
    ''' A_eq = A_viga + ((B_eff * espesor_losa) / n_compresion)'''

    print(f"\nAREA EQUIVALENTE COMPUESTA VIGA/LOSA:")
    print(f"\tA_eq_viga_losa = A_viga m2 + ((B_eff->(ambos lados) m * espesor_losa m) / n_compresion: ")
    area_equivalente_viga_losa = viga_area + ((ancho_efectivo_losa_ambos * valor_espesor_losa) / n_compresion)
    print(f"\t{viga_area} + (({ancho_efectivo_losa_ambos} * {valor_espesor_losa}) / {n_compresion}) = {area_equivalente_viga_losa} m2 \n")



    ''' Inercia de losa '''
    ''' I_losa = ((B_eff/n_compresion) * h ^3) / 12 '''

    print(f"\nINERCIA DE LOSA:")
    print(f"\tI_losa = ((B_eff(Ambos Lados) m / n_compresion) * espesor_losa[m]^3 ) / 12: ")
    print(f"\tI_losa = (({ancho_efectivo_losa_ambos} / {n_compresion}) * {valor_espesor_losa}^3) / 12")
    losa_inercia = ((ancho_efectivo_losa_ambos / n_compresion) * pow(valor_espesor_losa, 3)) / 12
    print(f"\tInercia de losa = {losa_inercia} [m4] \n")


    ''' Centro de gravedad de losa Y_cl '''
    ''' Y_inf de losa desde base de losa + Altura total de viga '''

    print(f"\nCentro de gravedad de losa:")
    print(f"\tY_inf de losa desde base de losa + Altura total de viga")
    losa_yinf = viga_altura + (valor_espesor_losa / 2)
    print(f"\tY_inf losa = {viga_altura} m + ({valor_espesor_losa} m / 2)")
    print(f"\tCentro de gravedad losa (+ altura viga) = {losa_yinf} m \n")

    ''' Centro de gravedad compuesto '''
    ''' Y_c = (Area_viga * Centroide_viga + Area_eq_losa * Centroide_losa) / Area_eq_viga_losa'''
    print(f"\nCENTRO DE GRAVEDAD COMPUESTO:")
    centro_gravedad_compuesto = (viga_area * viga_yinf + area_equivalente_losa * losa_yinf) / (area_equivalente_viga_losa)
    print("\t Y_c = (Area_viga m2 * Centroide_viga m + Area_eq_losa m2 * Centroide_losa m) / Area_eq_viga_losa m")
    print(f"\t Y_c = ({viga_area} * {viga_yinf} + {area_equivalente_losa} * {losa_yinf}) / {area_equivalente_viga_losa}")
    print(f"\t Centro de gravedad compuesto = {centro_gravedad_compuesto} m")

    ''' Inercia compuesta '''
    ''' I_c = I_viga + I_losa + (Area_viga * (Y_c - Y_viga) ^2) + (Area_eq_losa * (Y_c - Y_losa) ^2) '''
    ''' I_c = I_viga + I_losa + Inercia_viga_prima + Inercia_losa_prima '''

    print(f"\nINERCIA COMPUESTA:")
    Inercia_viga_prima = viga_area * pow((viga_yinf - centro_gravedad_compuesto), 2)
    Inercia_losa_prima = area_equivalente_losa * pow((losa_yinf - centro_gravedad_compuesto), 2)

    print(f"\t Inercia VIGA prima (Area_viga * (Y_viga - Y_compuesto) ^2) -> {viga_area} m2 * ({viga_yinf} m - {centro_gravedad_compuesto} m) ^2 = {Inercia_viga_prima} m4")
    print(f"\t Inercia LOSA prima (Area_losa * (Y_losa - Y_compuesto) ^2) -> {area_equivalente_losa} m2 * ({losa_yinf} m - {centro_gravedad_compuesto} m) ^2 = {Inercia_losa_prima} m4\n")

    inercia_compuesta = viga_inercia + losa_inercia + Inercia_viga_prima + Inercia_losa_prima
    print(f"\t Inercia_compuesta (Final) = (I_viga + I_losa + Inercia_viga_prima + Inercia_losa_prima) ->")
    print(f"{viga_inercia} m4 + {losa_inercia} m4 + {Inercia_viga_prima} m4 + {Inercia_losa_prima} m4 ->")
    print(f"\t Inercia compuesta = {inercia_compuesta} m4 \n")




    ''' ================================================================================================================================================================== '''
    ''' ============================     PASO 2 PARA T=00, Tabla   6) Propiedades Sección Viga homogenizada compuesta Final EXCEL CLAUDIO     ============================ '''
    ''' ================================================================================================================================================================== '''

    print("--\n\n-------------------------------------------------------------")
    print("----> PASO 2: SECCION VIGA HOMOGENEIZADA COMPUESTA FINAL: <---- \n")
    print("Solo considera cordones activos. (EXCEL no considera barras pasivas).\n\n")

    ''' Los nombres de las variables estan basados en los nombres que estan asignadps a tabla 6 en Plantilla claudio '''

    modulo_elasticidad = float(self.ui.tab3_line_cons_es.text()) / float(self.ui.tab4_line_horm_final_e.text())
    print(f"MODULO ELASTICIDAD: constante_Es [MPa] / Ec_hormigon_final [N/mm2] -> {float(self.ui.tab3_line_cons_es.text())} MPa / {float(self.ui.tab4_line_horm_final_e.text())} N/mm2 = {modulo_elasticidad}\n")

    ''' COL area'''
    ani_viga_comp = area_equivalente_viga_losa # Area equivalente total de todo el hormigon
    print(f"AREA VIGA COMPUESTA (Todo el hormigion. resultado de PASO1) = {area_equivalente_viga_losa} m2\n")

    # Area total de cables * modulo (Es / Ec) (Es, Ec son ingresados por usuario en TAB materiales, Pero toman valores por defecto al iniciar programa.)
    area_total_cables = float(self.ui.tab2_line_total_area.text()) / 100 # Variable original esta en CM, Por eso se pasa a METROS
    ani_cables = float(area_total_cables) * float(modulo_elasticidad)
    print(f"AREA CABLES: A_cables * modulo_elasticidad -> {area_total_cables} m2 * {modulo_elasticidad} = {ani_cables} m2\n")

    area_neta_ini = ani_viga_comp + ani_cables
    print(f"AREA NETA (viga + cables) -> {ani_viga_comp} m2 + {ani_cables} m2 = {area_neta_ini} m2\n")

    ''' COL Y cdg '''
    ycdg_viga_comp = centro_gravedad_compuesto
    ycdg_cables = float(self.ui.tab2_line_total_cdg_fuerza.text()) # Usa centro de gravedad calculado por fuerza (CON TPI), Se puede cambiar a usar por AREA
    print(f"\nCENTRO DE GRAVEDAD:")
    print(f"\t CDG viga compuesta: {ycdg_viga_comp} m")
    print(f"\t CDG Cables activos: {ycdg_cables} m \n")
    
    ''' COL li INERCIA '''
    inercia_viga_comp = inercia_compuesta
    inercia_cables = float(self.ui.tab2_line_total_inercia.text()) * modulo_elasticidad
    print(f"\nINERCIA:")
    print(f"\t INERCIA viga compuesta: {inercia_viga_comp} m4")
    print(f"\t INERCIA cables activos: I_cables * modulo_elasticidad -> {float(self.ui.tab2_line_total_inercia.text())} m4 * {modulo_elasticidad} = {inercia_cables} m4\n")

    ''' COL Ani * Ycg i'''
    ani_Y_viga_comp = ani_viga_comp * ycdg_viga_comp
    ani_Y_cables = ani_cables * ycdg_cables
    print(f"\nOperacion Area * CDG")
    print(f"\t A_viga_comp * CDG_viga_comp -> {ani_viga_comp} m2 * {ycdg_viga_comp} m = {ani_Y_viga_comp} m3")
    print(f"\t A_cables_activos * CDG_cables_activos -> {ani_cables} m2 * {ycdg_cables} m = {ani_Y_cables} m3 \n")

    # 3ra fila en columna, suma de ambos resultados
    ani_Y_total = ani_Y_viga_comp + ani_Y_cables
    print(f"SUMATORIA resultados anteriores -> ani_Y_viga_comp m3 + {ani_Y_cables} m3 = {ani_Y_total} m3\n")

    ''' Yc.g neta ini (En Primera Columna) '''
    Ycg_neta_ini = ani_Y_total / area_neta_ini
    print(f"\n CDG neta ini: CDG total / Area neta ini -> {ani_Y_total} 3m / {area_neta_ini} m2 = {Ycg_neta_ini} m \n")

    ''' COL Ani * li (O Ani * D^2 segun IGNACIO) '''
    ani_d2_viga_comp = ani_viga_comp * pow((ycdg_viga_comp - Ycg_neta_ini), 2)
    ani_d2_cables = ani_cables * pow((ycdg_cables - Ycg_neta_ini), 2)
    print(f"\nOPERACION (Area * (CDG - CDG neta ini)^2 )")
    print(f"\tPara viga   -> {ani_viga_comp} m2 * ({ycdg_viga_comp} m - {Ycg_neta_ini} m)^2 ) = {ani_d2_viga_comp} m4")
    print(f"\tPara cables -> {ani_cables} m2 * ({ycdg_cables} m - {Ycg_neta_ini} m)^2 ) = {ani_d2_cables} m4\n")

    ''' COL IT (ultima col) '''
    it_viga_comp = inercia_viga_comp + ani_d2_viga_comp
    it_cables = inercia_cables + ani_d2_cables
    print(f"\INERCIA TOTAL")
    print(f"\t Viga: I_viga_comp + Operacion_anterior (A * (cdg_viga * cdg_total)^2) -> {inercia_viga_comp} m4 + {ani_d2_viga_comp} m4 = {it_viga_comp} m4")
    print(f"\t Viga: I_cable_activo + Operacion_anterior (A * (cdg_cable * cdg_total)^2) -> {inercia_cables} m4 + {ani_d2_cables} m4 = {it_cables} m4 \n")

    it_total = it_viga_comp + it_cables
    inercia_neta_ini = it_total # Son la misma variable, Pero se hace asi para mantener consistencia con excel claudio
    print(f"\tSUMATORIA INERCIAS TOTALES -> {it_viga_comp} m4 + {it_cables} m4 = {it_total} m4\n")

    print(f"\nRESULTADOS DE SIMPLE T=00 (Sin redondear):")
    print(f"\t AREA: {area_neta_ini} m2")
    print(f"\t CDG: {Ycg_neta_ini} m")
    print(f"\t INERCIA: {inercia_neta_ini} m4\n\n")

    ''' ASIGNA RESULTADOS DE PROPIEDADES A LINEEDITS DE T = 00 en TAB CALC. PARCIAL '''
    area_neta_ini = round(area_neta_ini, 7)
    Ycg_neta_ini = round(Ycg_neta_ini, 7)
    inercia_neta_ini = round(inercia_neta_ini, 7)

    self.ui.tab5_line_area_t00.setText(f"{area_neta_ini}")
    self.ui.tab5_line_cdg_t00.setText(f"{Ycg_neta_ini}")
    self.ui.tab5_line_inercia_t00.setText(f"{inercia_neta_ini}")
