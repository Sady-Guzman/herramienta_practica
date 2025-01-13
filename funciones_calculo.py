import numpy as np

''' 
bi = Base inferior
bs = Base superior
h = Altura
'''

def calcular_area(trapecios, target):
    ''' ( (base_inf + base_sup) * Altura ) / 2'''

    b_i = trapecios[target][3]
    b_s = trapecios[target][4]
    h = trapecios[target][5]

    area = ((b_i + b_s) * h) / 2

    print(f"Para trapecio -> Bi: {b_i} -- Bs: {b_s} -- H: {h}")
    print("AREA: ", area)
    
    return 1

def calcular_inercia(trapecios, target):
    ''' (altura^3) * ((MAX(bi,bs)^2)+4*bi*bs+(MIN(bi,bs)^2)) / (36*(bi+bs))'''

    b_i = trapecios[target][3]
    b_s = trapecios[target][4]
    h = trapecios[target][5]

    inercia = (h**3) * ((max(b_i,b_s)**2)+4*b_i*b_s+(min(b_i,b_s)**2)) / (36*(b_i+b_s))

    h_cubed = h ** 3
    
    # Calculating the max, min, and sum of the bases
    max_base = max(b_i, b_s)
    min_base = min(b_i, b_s)
    sum_bases = b_i + b_s
    
    # Applying the formula
    result = (h_cubed * (max_base**2 + 4 * b_i * b_s + min_base**2)) / (36 * sum_bases)

    print(f"Para trapecio -> Bi: {b_i} -- Bs: {b_s} -- H: {h}")
    print("Inercia: ", result)

    return inercia


def calculate_formula(trapecios):
    '''
        FORMULA HOJA DE CALCULU JOAQUIN

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
        resultados.append(resultado)

    print(f"Debug calc_Cg -> Para trapecio -> Bi: {b_i} -- Bs: {b_s} -- H: {h}")
    print(f"Debug calc_Cg -> Trapezoid {trapecio[0]} - Resultado: {resultado:.7f}") # 7 decimales
    
    return resultados