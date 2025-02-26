import sys
import math

from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel, QComboBox
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from PySide6.QtCore import Qt

def setup_tab_calc_parcial(self):
    ''' Se ejecuta desde main cuando inicia app '''

    self.ui.tab5_btn_calcular.clicked.connect(lambda: calc_propiedades_tabla(self))
    


''' Calculo Parcial Bruta t = 0 '''
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

    ''' Hace calculos para simple t = 0 '''
    calc_seccion_neta_inicial(self) # Primer paso
    calc_seccion_homogeneizada_inicial(self)  # segundo paso (final) para t = 0

    calc_t00(self) # Paso 1 y Paso 2 para calcular T=00. Basado en tablas 5 y 6 de EXCEL CLAUDIO





''' Calculo Parcial Primer paso para Simple t= 0 '''
def calc_seccion_neta_inicial(self):
    ''' Usa formulas de hoja calculos JOAQUIN. Pen-ultima tabla'''

    print("\t\t\t\n\n\n>>Datos usados para simple t = 0<<\n")

    try: 
        print(f"Areas:")
        self.viga_area = self.ui.result_sum_area.text()
        self.cordones_area =self.ui.tab2_line_total_area.text()
        self.cordones_area = float(self.cordones_area) / 10000 # Pasa a metros
        self.barras_area = self.ui.tab3_line_area_barras.text()
        print(f"\t VIGA: {self.viga_area} m2")
        print(f"\t Arm. Activa: {self.cordones_area} m2")
        print(f"\t Arm. pasiva: {self.barras_area} mm2")
    except:
        print("Falta calcular valor de area en geometria, cordones o barras para hacer calculo de seccion_neta_inicial.")
        return

    try:
        print(f"\nY_inf:")
        self.viga_cg =self.ui.result_sum_ponderado.text()
        self.cordones_cg = self.ui.tab2_line_total_cdg_area.text()
        self.barras_cg = self.ui.tab3_line_yinf_barras.text()
        print(f"\t VIGA: {self.viga_cg} m")
        print(f"\t Arm. Activa (sin tpi): {self.cordones_cg} m")
        print(f"\t Arm. pasiva: {self.barras_cg} mm")
    except:
        print("Falta calcular Y_inf en geometria, cordones o barras para hacer calculo de seccion_neta_inicial.")
        return

    try:
        print(f"\nInercia:")
        self.viga_inercia = self.ui.result_sum_op.text()
        self.cordones_inercia = self.ui.tab2_line_total_inercia.text()
        self.barras_inercia = self.ui.tab3_line_inercia_barras.text()
        print(f"\t VIGA: {self.viga_inercia} [?]")
        print(f"\t Arm. Activa (sin tpi): {self.cordones_inercia} m4")
        print(f"\t Arm. pasiva: {self.barras_inercia} m4")
    except:
        print("Falta calcular Inercia en geometria, cordones o barras para hacer calculo de seccion_neta_inicial.")
        return
    

    try:
        print("A*cg de cada tipo:")
        # TODO que nombre usar para esta variable ??
        self.viga_a_cg = float(self.viga_area) * float(self.viga_cg)
        self.cordones_a_cg = float(self.cordones_area) * float(self.cordones_cg)
        self.barras_a_cg = float(self.barras_area) * float(self.barras_cg)
        print(f"\tA*Cg de viga: {self.viga_a_cg}")
        print(f"\tA*Cg de cordones: {self.cordones_a_cg}")
        print(f"\tA*Cg de barras: {self.barras_a_cg}")
    except:
        print("Falta calcular A*cg en geometria, cordones o barras para hacer calculo de seccion_neta_inicial.")
        return

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


''' Calculo Parcial simple t = 0 paso final'''
def calc_seccion_homogeneizada_inicial(self):
    ''' ultima tabla excel Joaquin '''

    ''' F'c y Ec son obtenidos de PESTANA MATERIALES '''
    # Ingresado por usr (o puede usar valor por defecto segun tipo de hormigon seleccionado en Cobmbo)
    try:
        fc_ini = float(self.ui.tab4_line_horm_min_fc.text())
        
        # Usa formula pedida por claudio
        ec_ini = float(self.ui.tab4_line_horm_min_e.text())
    except:
        print("Faltan datos f'c y/o Ec para poder hacer calculo.")
        return



    ''' CONSTANTES '''
    # cons_es = 200000 # unidad: MPa
    # cons_eps = 198569 # Unidad: MPa ... = 28800 KSI
    cons_es = float(self.ui.tab3_line_cons_es.text())
    cons_eps = float(self.ui.tab3_line_cons_eps.text())

    ns =  cons_es / ec_ini # Para steel -> Barras Pasivas
    nps = cons_eps / ec_ini # Para preStressed Steel -> Cordones Activos

    print(f"\nCalulo Parcial. calc_seccion_homogeneizada_inicial() --> Valores usados para f'c = {fc_ini}, ec = {ec_ini}, ns = {ns}, nps = {nps}\n")

    ''' Col area m2'''
    try:
        homo_area_viga_barra_cable = float(self.viga_area) - (float(self.barras_area) + float(self.cordones_area))
        homo_area_barras = float(self.barras_area) * ns
        homo_area_cordones = float(self.cordones_area) * nps

        homo_suma_areas = homo_area_viga_barra_cable + homo_area_cordones + homo_area_barras

        print("Valores equivalente COL AREA:")
        print("\t\t Area Viga-Barras-Cordones: ", homo_area_viga_barra_cable)
        print("\t\t Area barras: ", homo_area_barras)
        print("\t\t Area Cordones: ", homo_area_cordones)
        print("\t\t Area sumatoria: ", homo_suma_areas)
    except:
        print("Faltan datos para hacer calculo de seccion_homogeneizada_inicial.")
        return


    '''Col Y_inf'''
    try:
        print("\n\nValores equivalente COL Y_inf")
        homo_yinf_viga_barra_cable = self.total_area_cg / self.area_final
        homo_yinf_barra = float(self.barras_cg)
        homo_yinf_cordones = float(self.cordones_cg)

        print("\t\tY_inf viga-barras-cordones: ", homo_yinf_viga_barra_cable)
        print("\t\tY_inf barras: ", homo_yinf_barra)
        print("\t\tY_inf cordones: ", homo_yinf_cordones)
    except:
        print("Faltan datos para hacer calculo de seccion_homogeneizada_inicial.")
        return

    ''' COL Area * Cg de cada tipo '''
    try:
        homo_viga_barra_cordon_a_cg = homo_area_viga_barra_cable * homo_yinf_viga_barra_cable
        homo_barras_a_cg = homo_area_barras * homo_yinf_barra
        homo_cordones_a_cg = homo_area_cordones * homo_yinf_cordones

        homo_suma_a_cg = homo_viga_barra_cordon_a_cg + homo_barras_a_cg + homo_cordones_a_cg

        print("\n\nValores equivalente COL Area * Cg")
        print("\t\tA * Cg Vigas-Barras-Cables: ", homo_viga_barra_cordon_a_cg)
        print("\t\tA * Cg Barras: ", homo_barras_a_cg)
        print("\t\tA * Cg Cables: ", homo_cordones_a_cg)
        print("\t\tA * Cg SUMATORIA: ", homo_suma_a_cg)
    except:
        print("Faltan datos para hacer calculo de seccion_homogeneizada_inicial.")
        return


    ''' Col Yinf. ultima fila '''
    try:
        homo_total_yinf = homo_suma_a_cg / homo_suma_areas # No es realmente la sumatoria de col Y_inf TODO Que nombre asignarle ???
        print("\tCelda Y_inf: ", homo_total_yinf)
    except:
        print("Faltan datos para hacer calculo de seccion_homogeneizada_inicial.")
        return


    ''' COL Inercia tipo '''
    try:
        homo_inercia_viga_barra_cordon = float(self.operacion_final)
        homo_inercia_barras = float(self.barras_inercia) * ns
        homo_inercia_cordones = float(self.cordones_inercia) * nps

        print("\n\nValores equivalentes a COL Inercia")
        print("\t\t Inercia Viga-Barras-Cables: ", homo_inercia_viga_barra_cordon)
        print("\t\t Inercia Barras: ", homo_inercia_barras)
        print("\t\t Inercia Cables: ", homo_inercia_cordones)
    except:
        print("Faltan datos para hacer calculo de seccion_homogeneizada_inicial.")
        return
    
    ''' Col Operacion final '''
    try:
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
    except:
        print("Faltan datos para hacer calculo de seccion_homogeneizada_inicial.")
        return

    self.ui.tab5_line_area_t0.setText(f"{round(homo_suma_areas, 7)}")
    self.ui.tab5_line_cdg_t0.setText(f"{round(homo_total_yinf, 7)}")
    self.ui.tab5_line_inercia_t0.setText(f"{round(homo_operacion_final, 7)}")



''' ===================================================================================================================== '''

def calc_t00(self):

    ''' Valores para concreto insitu, VIGA,Lc, Sw, e, voladizo '''
    try:
        valor_luz_calculo = float(self.ui.tab6_line_luz_calculo.text())
        valor_sw = float(self.ui.tab6_line_sw.text())
        valor_espesor_losa = float(self.ui.tab6_line_espesor.text())
        # valor_voladizo = float(self.ui.tab6_line_voladizo.text())
    except:
        print("Falta uno o mas de los siguientes valores: Luz de Calculo, Sw, Espesor losa insitu. Por lo que no se puede calcular t=00.\n")
        return

    print(f"\n🔹 Valores de inputs en pestana LUZ DE CALCULO:")
    print(f"\tLc (Luz calculo) = {valor_luz_calculo} m")
    print(f"\tSw (Dist. entre Almas) = {valor_sw} m")
    print(f"\te (Espesor de losa) = {valor_espesor_losa}m ")
    # print(f"\tD (largo de voladizo) = {valor_voladizo} m")



    ''' Trapecios de hormigon insitu existentes '''
    for i, layout in enumerate(self.dynamic_layouts):
        tipo_hormigon = layout['combo_insitu'].currentText()

        if tipo_hormigon == "Insitu":
            # print(f"\n🔹 Para layout {i}")
            print("\tTrapecio de hormigon INSITU en GEOMETRIA:")
            print(f"\tNombre: {layout['name_label'].text()}")
            print(f"\tBi: {layout['bi_line'].text()}")
            print(f"\tAltura: {layout['altura_line'].text()}")
            print(f"\tÁrea: {layout['area_line'].text()}")



    ''' Encuentra ancho de alma (Trapecio mas angosto en self.dynamic_layouts, que tenga Bi y Bs iguales, y que no esta ni en el primer ni ultimo lugar del diciconario) '''
    print("\n\n🔹 Ancho de alma:")
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
        print(f"No se encontró ancho de alma.")
        # return
    else:
        print(f"\tAncho de alma mas angosto: {menor_ancho} m, en layout {nombre}")



    ''' Recupera valores de F'c para viga y para insitu '''
    fc_viga = float(self.ui.tab4_line_horm_final_fc.text())
    fc_losa = float(self.ui.tab4_line_horm_insitu_fc.text())
    n_compresion = math.sqrt(fc_viga/fc_losa)

    print(f"\n🔹 Valores de f'c en TAB MATERIALES:")
    print(f"\tf'c final (viga) = {fc_viga} N/mm2")
    print(f"\tf'c insitu (losa) = {fc_losa} N/mm2")
    print(f"\tResultado de SQRT (f'c(Viga) / F'c(Losa)) = {n_compresion} [? unidad]")




    ''' Propiedades de viga bruta. '''
    viga_altura = float(self.ui.result_sum_altura.text())
    viga_area = float(self.ui.result_sum_area.text())
    viga_yinf = float(self.ui.result_sum_ponderado.text())
    viga_inercia = float(self.ui.result_sum_op.text())

    print(f"\n🔹 Propiedades de VIGA BRUTA:")
    print(f"\t Altura = {viga_altura} m")
    print(f"\t Area = {viga_area} m2")
    print(f"\t Y_inf = {viga_yinf} m")
    print(f"\t Inercia = {viga_inercia} m4")



    ''' Valores para tabla ACI 6.3.2.1 '''
    ''' B_eff de losa '''

    print(f"\n🔹 Comparaciones TABLA ACI 6.3.2.1 de valor minimo:")
    ''' Ambos lados'''
    print(f"\tAMBOS LADOS -> ")
    print(f"\t\t 8*h (espesor losa)->({valor_espesor_losa} * 8) =\t{round(valor_espesor_losa * 8, 3)} m")
    print(f"\t\t Sw/2 (separacion almas->({valor_sw} / 2) =\t{round(valor_sw / 2, 3)} m")
    print(f"\t\t Lc/8 (luz calculo)->({valor_luz_calculo} / 8) =\t{round(valor_luz_calculo / 8, 3)} m")

    print(f"\tSOLO UN LADO -> ")
    print(f"\t\t 6*h (espesor losa)->({valor_espesor_losa} * 6) =\t{round(valor_espesor_losa * 6, 3)} m")
    print(f"\t\t Sw/2 (separacion almas)->({valor_sw} / 2) =\t{round(valor_sw / 2, 3)} m")
    print(f"\t\t Lc/12 (luz calculo)->({valor_luz_calculo} / 12) =\t{round(valor_luz_calculo / 12, 3)} m")

    ancho_efectivo_losa_ambos = float(min(valor_espesor_losa * 8, valor_sw / 2, valor_luz_calculo / 8))
    ancho_efectivo_losa_uno = float(min(valor_espesor_losa * 6, valor_sw / 2, valor_luz_calculo / 12))

    self.ui.tab5_line_beff_ambos.setText(f"{round(ancho_efectivo_losa_ambos, 4)}")
    self.ui.tab5_line_beff_uno.setText(f"{round(ancho_efectivo_losa_uno, 4)}")

    print(f"\n🔹 Por lo tanto ANCHO EFECTIVO:")
    print(f"\t\t B_eff (Valor minimo para ambos lados) = {ancho_efectivo_losa_ambos} m")
    print(f"\t\t B_eff (Valor minimo para un lado) = {ancho_efectivo_losa_uno} m")



    ''' Area losa '''
    ''' Area de trapecio insitu '''
    ''' Solo sirve si se usa un solo trapecio insitu (Osea una sola losa) No se esta controlando que usuario no agregue mas de un trapecio insitu '''

    ''' TODO altura de trapecio tipo insitu y valor ingresado en tab6 'espesor' Son lo mismo ??? '''
    existe_insitu = False

    for i, layout in enumerate(self.dynamic_layouts):
        tipo_hormigon = layout['combo_insitu'].currentText()

        if tipo_hormigon == "Insitu":
            # print(f"\n🔹 Para layout {i}")
            # print("\tTrapecio de hormigon Insitu:")
            # print(f"\tNombre: {layout['name_label'].text()}")
            # print(f"\tBi: {layout['bi_line'].text()}")
            # print(f"\tAltura: {layout['altura_line'].text()}")
            # print(f"\tÁrea: {layout['area_line'].text()}")
            ancho_real_losa = float(layout['bi_line'].text())
            existe_insitu = True
    
    if existe_insitu == False:
        print("No se encuentra ningun bloque de hormigon insitu en la geometria, No se continua con calculo t = 00.\n")
        return

    area_losa = ancho_real_losa * valor_espesor_losa
    print(f"\n🔹 Area de losa (Ancho real losa * Espesor losa) -> ({ancho_real_losa} * {valor_espesor_losa}) = {area_losa} m2")
    
    area_equivalente_losa = (ancho_efectivo_losa_ambos * valor_espesor_losa) / n_compresion
    print(f"\n🔹 Area equivalente solo losa (B_eff (Ambos Lados * espesor) / n) ({ancho_efectivo_losa_ambos} * {valor_espesor_losa}) / {n_compresion} = {area_equivalente_losa} m2")


    ''' A_eq viga/losa '''
    ''' A_eq = A_viga + ((B_eff * espesor_losa) / n_compresion)'''

    print(f"\n🔹 Area equivalente viga/losa:")
    print(f"\tA_eq = A_viga + ((B_eff->(ambos lados) * espesor_losa) / n_compresion")
    area_equivalente_viga_losa = viga_area + ((ancho_efectivo_losa_ambos * valor_espesor_losa) / n_compresion)
    print(f"\tA_eq = {area_equivalente_viga_losa} m2")



    ''' Inercia de losa '''
    ''' I_losa = ((B_eff/n_compresion) * h ^3) / 12 '''

    print(f"\n🔹 Inercia de losa:")
    print(f"\tI_losa = ((B_eff->(Ambos Lados) / n_compresion) * h^3->(Espesor Losa)) / 12 ")
    print(f"\tI_losa = (({ancho_efectivo_losa_ambos} / {n_compresion}) * {valor_espesor_losa}^3) / 12")
    losa_inercia = ((ancho_efectivo_losa_ambos / n_compresion) * pow(valor_espesor_losa, 3)) / 12
    print(f"\tInercia de losa = {losa_inercia} [? Unidad]")


    ''' Centro de gravedad de losa Y_cl '''
    ''' Y_inf de losa desde base de losa + Altura total de viga '''

    print(f"\n🔹 Centro de gravedad de losa:")
    print(f"\tY_inf de losa desde base de losa + Altura total de viga")
    losa_yinf = viga_altura + (valor_espesor_losa / 2)
    print(f"\tY_inf losa = {viga_altura} + ({valor_espesor_losa} / 2)")
    print(f"\tCentro de gravedad losa (+ altura vida) = {losa_yinf}")

    ''' Centro de gravedad compuesto '''
    ''' Y_c = (Area_viga * Centroide_viga + Area_eq_losa * Centroide_losa) / Area_eq_viga_losa'''

    print(f"\n🔹 Centro de gravedad compuesto:")
    centro_gravedad_compuesto = (viga_area * viga_yinf + area_equivalente_losa * losa_yinf) / (area_equivalente_viga_losa)
    print("\tY_c = (Area_viga * Centroide_viga + Area_eq_losa * Centroide_losa) / Area_eq_viga_losa")
    print(f"\tY_c = ({viga_area} * {viga_yinf} + {area_equivalente_losa} * {losa_yinf}) / {area_equivalente_viga_losa}")
    print(f"\tCentro de gravedad compuesto = {centro_gravedad_compuesto}")

    ''' Inercia compuesta '''
    ''' I_c = I_viga + I_losa + (Area_viga * (Y_c - Y_viga) ^2) + (Area_eq_losa * (Y_c - Y_losa) ^2) '''
    ''' I_c = I_viga + I_losa + Inercia_viga_prima + Inercia_losa_prima '''


    print(f"\n🔹 Inercia compuesta:")
    Inercia_viga_prima = viga_area * pow((viga_yinf - centro_gravedad_compuesto), 2)
    Inercia_losa_prima = area_equivalente_losa * pow((losa_yinf - centro_gravedad_compuesto), 2)

    print(f"\tInercia_viga_prima (Area_viga * (Y_c - Y_viga) ^2) -> {viga_area} * ({viga_yinf} - {centro_gravedad_compuesto})^2 = {Inercia_viga_prima}")
    print(f"\tInercia_viga_prima (Area_viga * (Y_c - Y_viga) ^2) -> {area_equivalente_losa} * ({losa_yinf} - {centro_gravedad_compuesto})^2 = {Inercia_losa_prima}")

    inercia_compuesta = viga_inercia + losa_inercia + Inercia_viga_prima + Inercia_losa_prima
    print(f"\tInercia_compuesta (Final) = (I_viga + I_losa + Inercia_viga_prima + Inercia_losa_prima) -> {viga_inercia} + {losa_inercia} + {Inercia_viga_prima} + {Inercia_losa_prima}.")
    print(f"\tInercia compuesta = {inercia_compuesta} m4")




    ''' ================================================================================================================================================================== '''
    ''' ============================     PASO 2 PARA T=00, Tabla   6) Propiedades Sección Viga homogenizada compuesta Final EXCEL CLAUDIO     ============================ '''
    ''' ================================================================================================================================================================== '''

    ''' Los nombres de las variables estan basados en los nombres que estan asignadps a tabla 6 en Plantilla claudio '''

    modulo_elasticidad = float(self.ui.tab3_line_cons_es.text()) / float(self.ui.tab4_line_horm_final_e.text()) # TODO Preguntar IGNACIO si esta bie usar Ec como horm_final_e

    ''' COL area'''
    ani_viga_comp = area_equivalente_viga_losa # Area equivalente total de todo el hormigon

    # Area total de cables * modulo (Es / Ec) (Es, Ec son ingresados por usuario en TAB materiales, Pero toman valores por defecto al iniciar programa.)
    area_total_cables = float(self.ui.tab2_line_total_area.text()) / 100 # Variable original esta en CM, Por eso se pasa a METROS
    ani_cables = float(area_total_cables) * float(modulo_elasticidad)

    area_neta_ini = ani_viga_comp + ani_cables

    ''' COL Y cdg '''
    ycdg_viga_comp = centro_gravedad_compuesto
    ycdg_cables = float(self.ui.tab2_line_total_cdg_fuerza.text()) # USA centro de gravedad calculado por fuerza (CON TPI), Se puede cambiar a usar por AREA
    
    ''' COL li INERCIA '''
    inercia_viga_comp = inercia_compuesta
    inercia_cables = float(self.ui.tab2_line_total_inercia.text()) * modulo_elasticidad

    ''' COL Ani * Ycg i'''
    ani_Y_viga_comp = ani_viga_comp * ycdg_viga_comp
    ani_Y_cables = ani_cables * ycdg_cables

    # 3ra fila en columna, suma de ambos resultados
    ani_Y_total = ani_Y_viga_comp + ani_Y_cables

    ''' Yc.g neta ini (En Primera Columna) '''
    Ycg_neta_ini = ani_Y_total / area_neta_ini

    ''' COL Ani * li (O Ani * D^2 segun IGNACIO) '''
    ani_d2_viga_comp = ani_viga_comp * pow((ycdg_viga_comp - Ycg_neta_ini), 2)
    ani_d2_cables = ani_cables * pow((ycdg_cables - Ycg_neta_ini), 2)

    ''' COL IT (ultima col) '''
    it_viga_comp = inercia_viga_comp + ani_d2_viga_comp
    it_cables = inercia_cables + ani_d2_cables

    it_total = it_viga_comp + it_cables
    inercia_neta_ini = it_total # Son la misma variable, Pero se hace asi para mantener consistencia con excel claudio

    ''' ASIGNA RESULTADOS DE PROPIEDADES A LINEEDITS DE T = 00 en TAB CALC. PARCIAL '''
    area_neta_ini = round(area_neta_ini, 7)
    Ycg_neta_ini = round(Ycg_neta_ini, 7)
    inercia_neta_ini = round(inercia_neta_ini, 7)

    self.ui.tab5_line_area_t00.setText(f"{area_neta_ini}")
    self.ui.tab5_line_cdg_t00.setText(f"{Ycg_neta_ini}")
    self.ui.tab5_line_inercia_t00.setText(f"{inercia_neta_ini}")
