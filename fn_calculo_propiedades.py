import numpy as np
from fn_update_gui import aplicar_valores_calculados

''' 
    Funciones para calcular propiedades en base a dimensiones de piezas
    Como: Area, Centro de Gravedad, Inercia, Sumatorias de valores para todos los trapecios, Producto ponderado, C.G. Pieza
'''

''' 
    bi = Base inferior
    bs = Base superior
    h = Altura

    
    En lista (de listas) que es Trapecios[] se tiene que:
    esta lista se saca de tuplas de DB catalogo.db en tabla Trapecios
    [0]: id
    [1]: seccion
    [2]: pos
    [3]: bi
    [4]: bs
    [5]: h
    [6]: FK pieza_id
'''

def calcular_area(trapecios):
    ''' ( (base_inf + base_sup) * Altura ) / 2'''
    resultados = []

    for i in range(len(trapecios)):
        b_i = trapecios[i][3]
        b_s = trapecios[i][4]
        h = trapecios[i][5]

        area = ((b_i + b_s) * h) / 2
        
        print(f"Para trapecio -> Bi: {b_i} -- Bs: {b_s} -- H: {h}")
        print("AREA: ", area)

        area = round(area, 9)
        resultados.append(area)

    print("Areas calculadas: ", resultados)
    return resultados

def calcular_inercia(trapecios):
    ''' (altura^3) * ((MAX(bi,bs)^2)+4*bi*bs+(MIN(bi,bs)^2)) / (36*(bi+bs))'''

    resultados = []

    for i in range(len(trapecios)):
        b_i = trapecios[i][3]
        b_s = trapecios[i][4]
        h = trapecios[i][5]

        h_cubed = h ** 3
    
        # pre-calcular max y min de bases de trapecio
        max_base = max(b_i, b_s)
        min_base = min(b_i, b_s)
        sum_bases = b_i + b_s
        
        # calculo final
        result = (h_cubed * (max_base**2 + 4 * b_i * b_s + min_base**2)) / (36 * sum_bases)


        print(f"Para trapecio -> Bi: {b_i} -- Bs: {b_s} -- H: {h}")
        print("Inercia: ", result)

        result = round(result, 9)
        resultados.append(result)


    print("Valores lista Inercia: ", resultados)
    return resultados


def calcular_centro_gravedad(trapecios):
    '''
        --> FORMULA HOJA DE CALCULU JOAQUIN

        IF(D4≤C4;E4*(2*MAX(D4;C4)+MIN(C4;D4))÷(3*(D4+C4));E4-E4*(2*MAX(D4;C4)+MIN(C4;D4))÷(3*(D4+C4)))+SUM($E$3:E3)
        
        Identado: 
            if true:
                E4 * (2 * MAX(D4; C4) + MIN(C4; D4)) ÷ (3 * (D4 + C4)) + SUM($E$3:E3)
            else:
                E4 - E4 * (2 * MAX(D4; C4) + MIN(C4; D4)) ÷ (3 * (D4 + C4)) + SUM($E$3:E3)
        
        Con nombre de variable en vez de columnas:
            IF base_sup <= base_inf:
                h * (2 * MAX(base_sup, base_inf) + MIN(base_sup, base_inf)) ÷ (3 * (base_sup + base_inf)) + altura_acumulada
            ELSE:
                h - h * (2 * MAX(base_sup, base_inf) + MIN(base_sup, base_inf)) ÷ (3 * (base_sup + base_inf)) + altura_acumulada
    '''
    altura_acumulada = 0  # representa SUM($E$3:E3)
    resultados = []       # Guarda cada valor de Cg

    for i, trapecio in enumerate(trapecios):
        b_i = trapecio[3]  # Base inferior
        b_s = trapecio[4]  # Base superior
        h = trapecio[5]    # Altura

        if i > 0:
            altura_acumulada += trapecios[i - 1][5]  # Suma altura de trapecios anteriores

        # Formula condicional excel Joaquin 'traducida' a python (Considerar tambien suma h_acumulada)
        if b_s <= b_i:
            centro = h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s))
        else:
            centro = h - h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s))

        # paso final: agregar valor de altura acumulada
        resultado = centro + altura_acumulada
        resultado = round(resultado, 9)
        resultados.append(resultado)
        print("valor de var resultado: ", resultado)
        print("Valor de var altura_acumulada: ", altura_acumulada)

    print(f"Debug calc_Cg -> Para trapecio -> Bi: {b_i} -- Bs: {b_s} -- H: {h}")
    print(f"Debug calc_Cg -> Trapezoid {trapecio[0]} - Resultado: {resultado:.7f}") # 7 decimales
    
    print("Resultados CG's: ", resultados)
    return resultados


def calcular_suma_areas(areas):
    suma_areas = 0

    for i in range(len(areas)):
        suma_areas += areas[i]
    print("debug fn_calculos -> La suma de todas las areas es: ", suma_areas)
    
    return suma_areas

# Se usa en calculo centro gravedad pieza
def calcular_producto_ponderado(areas, centros_gravedad, suma_areas):
    '''
        =+SUMPRODUCT(F3:F7;G3:G7)/F9

        Columnas -> F: Area, G: Centro Gravedad, (F9: Suma de todas las areas)
    '''

    resultado = 0

    for i in range(len(areas)):
        resultado += areas[i] * centros_gravedad[i]
    
    resultado = resultado / suma_areas

    print("Resultado suma ponderada: ", resultado)
    return resultado


# Centro de gravedad de pieza completa (o hasta el trapecio que actual)
# Por cada trapecio que se agrega al calculo, el centro de gravedad se mueve
# Lista de resultados entrega el CG hasta el trapecio al que corresponde el indice
''' Confirmar definicion con Joaquin/Ignacio '''
def calcular_op(areas, centros_gravedad, inercias, producto_ponderado):
    '''
        =+H4+F4*(G4-$G$9)^2

        Columnas ->
        H: Inercias
        F: Areas
        G: Centros de Gravedad
        $G$9: Producto ponderado
    '''

    resultados = []

    for i in range(len(areas)):
        result = inercias[i] + (areas[i] * (centros_gravedad[i] - producto_ponderado) ** 2)
        resultados.append(result)

    print("Resultados OP: ", resultados)
    return resultados

# 0,002180267 ; 0,000585973 ; 0,000164640 ; 0,000585973 ; 0,002180267

def calcular_altura_acumulada(trapecios):
    # trapecio[5] # 5: Posicion altura

    altura_acumulada = 0

    for i in range(len(trapecios)):
            altura_acumulada += trapecios[i][5]
    
    print("Altura acumulada: ", altura_acumulada)
    return altura_acumulada


''' Lee valores de todos los LineEdits dinamicos existentes y calcula nuevo resultado de area,I,cg,OP '''
# Se usa en caso de que usuario agregue mas trapecios a una figura, para recalcular propiedades de pieza contemplando nuevos trapecios
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
    # valores_cg = altura_acumulada - calcular_centro_gravedad(valores_dimensiones_dinamicas) # Y sup ?
    valores_cg = calcular_centro_gravedad(valores_dimensiones_dinamicas) # Y inf ?
    suma_areas = calcular_suma_areas(valores_areas)
    producto_ponderado = calcular_producto_ponderado(valores_areas, valores_cg, suma_areas)
    valores_op = calcular_op(valores_areas, valores_cg, valores_inercia, producto_ponderado)

    # Aplica resultados a layouts dinamicos + layouts fijos
    aplicar_valores_calculados(self, valores_areas, valores_cg, valores_inercia, valores_op, suma_areas, altura_acumulada, producto_ponderado)

    return 