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

# def calcular_centro_gravedad_sup(trapecios):
#     ''' formula excel con columnas C: bi D: bs E: h
#     IF(D4≤C4;E4*(2*MAX(D4;C4)+MIN(C4;D4))÷(3*(D4+C4));E4-E4*(2*MAX(D4;C4)+MIN(C4;D4))÷(3*(D4+C4)))+SUM($E$3:E3)
    
#     Identado: 
#         if true:
#             E4 × (2 × MAX(D4; C4) + MIN(C4; D4)) ÷ (3 × (D4 + C4))
#         else:
#             E4 − E4 × (2 × MAX(D4; C4) + MIN(C4; D4)) ÷ (3 × (D4 + C4))
    
#     en codigo:
#         IF base_sup <= base_inf:
#             h × (2 × MAX(base_sup, base_inf) + MIN(base_sup, base_inf)) ÷ (3 × (base_sup + base_inf))
#         ELSE:
#             h − h × (2 × MAX(base_sup, base_inf) + MIN(base_sup, base_inf)) ÷ (3 × (base_sup + base_inf))


#     b_i = trapecios[0][3]
#     b_s = trapecios[0][4]
#     h = trapecios[0][5]
#     '''

#     print("Contenido trapecios: ", trapecios)

#     centro_gravedad_superior = 0  # guarda suma acumulada
#     acumulado = 0  #  (SUM($E$3:E3))

#     for trapecio in trapecios:
#         b_i = trapecio["base_inf"]  # base inferior
#         b_s = trapecio["base_sup"]  # base superior
#         h = trapecio["altura"]     # altura

#         if b_s <= b_i:
#             centro = h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s))
#         else:
#             centro = h - h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s))

#         acumulado += centro
#         print(f"Trapezoid {trapecio['id']} - Centro de gravedad superior: {acumulado}")
    
#     print("Centro de gravedad superior: ", acumulado)

#     return acumulado



# def calcular_centro_gravedad_sup(trapecios):
#     """
#     Calculates the weighted upper center of gravity for multiple trapezoids.
#     Considers the cumulative height of trapezoids progressively in each iteration.
#     """

#     '''
#         For de C:

#         for (i = 0; i++; i < len(list)) { 
#             for (x = i; x--; x >= 0) {
#                 // Do something
#             }
#         }

#         en python:

#         for i in range(len(my_list)):  # Loop with i from 0 to len(list)-1
#             for x in range(i, -1, -1):  # Loop with x from i down to 0 (inclusive)
#                 # Do something

#     '''
#     print("Contenido trapecios: ", trapecios)

#     acumulado = 0  # Total weighted center of gravity
#     altura_acumulada = 0  # Cumulative height sum

#     for i, trapecio in enumerate(trapecios):
#         # Access tuple indices
#         b_i = trapecio[3]  # base_inf
#         b_s = trapecio[4]  # base_sup
#         h = trapecio[5]    # altura

#         # Add the height of the current trapezoid to the cumulative height
#         altura_acumulada += h

#         # Apply the formula for individual trapezoid
#         if b_s <= b_i:
#             centro = h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s))
#         else:
#             centro = h - h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s))

#         # Accumulate the weighted center of gravity
#         acumulado += centro * h  # Weight by height

#         # Print progress at each step
#         print(f"Iteration {i+1} - Trapezoid {trapecio[0]}:")
#         print(f"  Altura acumulada: {altura_acumulada:.2f}")
#         print(f"  Acumulado ponderado: {acumulado:.2f}")

#     ''' forma 2 '''

#     altura_acumulada = 0

#     for i in range(len(trapecios)):  # itera i de 0 a largo dict - 1
#         for x in range(i, -1, -1):  # itera x de i hasta 0
#             altura_acumulada = trapecios[i][x] + altura_acumulada

    
#     print("Altura acumulada = ", altura_acumulada)
    

#     # Compute the final weighted center of gravity
#     if altura_acumulada > 0:
#         centro_gravedad_superior = acumulado / altura_acumulada
#     else:
#         centro_gravedad_superior = 0

#     print("Centro de gravedad superior total ponderado: ", centro_gravedad_superior)
#     return centro_gravedad_superior


def test(trapecios, target):

    '''
        IF(D4≤C4;E4*(2*MAX(D4;C4)+MIN(C4;D4))÷(3*(D4+C4));E4-E4*(2*MAX(D4;C4)+MIN(C4;D4))÷(3*(D4+C4)))+SUM($E$3:E3)
        
        Identado: 
            if true:
                E4 × (2 × MAX(D4; C4) + MIN(C4; D4)) ÷ (3 × (D4 + C4)) + SUM($E$3:E3)
            else:
                E4 − E4 × (2 × MAX(D4; C4) + MIN(C4; D4)) ÷ (3 × (D4 + C4)) + SUM($E$3:E3)
        
        en codigo:
            IF base_sup <= base_inf:
                h × (2 × MAX(base_sup, base_inf) + MIN(base_sup, base_inf)) ÷ (3 × (base_sup + base_inf)) + altura_acumulada
            ELSE:
                h − h × (2 × MAX(base_sup, base_inf) + MIN(base_sup, base_inf)) ÷ (3 × (base_sup + base_inf)) + altura_acumulada
    
    '''

    b_i = trapecios[target][3]  # base_inf
    b_s = trapecios[target][4]  # base_sup
    h = trapecios[target][5]    # altura
    
    altura_acumulada = 0

    print(trapecios)

    print("debug CG -> Len trapecios: ", len(trapecios))

    '''
    for i in range(len(trapecios)):  # itera i de 0 a largo dict - 1
        print(" FOR n1 >>> Valor de i -> ", i)
        for x in range(i, -1, -1):  # itera x de i hasta 0
            print(" FOR n2 >>> Valor de x -> ", x)
            print(f"Sumando altura_acumulada = {altura_acumulada} + trapecios[{x}][5] = {trapecios[x][5]}")
            altura_acumulada = trapecios[x][5] + altura_acumulada
    '''

    ''' Suma altura acumulada '''
    for i in range(target, -1, -1):  # itera i de target hasta 0 (inclusivo)
        print(" Iteracion for calc_altura >>> Valor de i -> ", i)
        print(f"Sumando altura_acumulada = {altura_acumulada} + trapecios[{i}][5] = {trapecios[i][5]}")
        altura_acumulada = trapecios[i][5] + altura_acumulada

    print("Debug CG -> Altura acumulada final = ", altura_acumulada)
    
    # # formula Joaquin
    # if b_s <= b_i:
    #     centro_0 = h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s)) + altura_acumulada
    # else:
    #     centro_0 = h - h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s)) + altura_acumulada

    
    # formula libro
    centro_libro = (h * ((2 * b_i) + b_s)) / (3 * (b_i + b_s))

    # Formulas Joaquin
    centro_1 = h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s)) + altura_acumulada
    centro_2 = h - h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s)) + altura_acumulada
    
    # Formulas joaquin c/ Condicional
    centro_0 = 0
    if b_s <= b_i:
        centro_0 = h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s))
    else:
        centro_0 = h - h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s))

    # Agrega altura acumulada a resultado
    centro_0 += altura_acumulada

    print(f"Para trapecio -> Bi: {b_i} -- Bs: {b_s} -- H: {h}")
    print(f"Centro de gravedad para trapecio en pos [{target}] ->")
    print("centro_0: ", centro_0)
    print("Centro 1: ", centro_1)
    print("Centro 2: ", centro_2)
    print("Centro Libro: ", centro_libro)



# def calculate_formula(trapecios):
#     altura_acumulada = 0  # This represents SUM($E$3:E3)
#     resultados = []       # To store results for each trapezoid

#     for i, trapecio in enumerate(trapecios):
#         b_i = trapecio[3]  # Base inferior
#         b_s = trapecio[4]  # Base superior
#         h = trapecio[5]    # Altura

#         # Apply the formula conditionally
#         if b_s <= b_i:
#             centro = h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s))
#         else:
#             centro = h - h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s))

#         # Add the cumulative height (SUM($E$3:E3))
#         altura_acumulada += h
#         resultado = centro + altura_acumulada

#         resultados.append(resultado)
#         print(f"Trapezoid {trapecio[0]} - Resultado: {resultado:.10f}")
    
#     return resultados


def calculate_formula(trapecios):
    altura_acumulada = 0  # representa SUM($E$3:E3)
    resultados = []       # Guarda cada valor de Cg

    for i, trapecio in enumerate(trapecios):
        b_i = trapecio[3]  # Base inferior
        b_s = trapecio[4]  # Base superior
        h = trapecio[5]    # Altura

        if i > 0:
            altura_acumulada += trapecios[i - 1][5]  # Suma altura de trapecios anteriores

        # Formula condicional Joaquin
        if b_s <= b_i:
            centro = h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s))
        else:
            centro = h - h * (2 * max(b_i, b_s) + min(b_i, b_s)) / (3 * (b_i + b_s))

        # paso final: agregar valor de altura acumulada
        resultado = centro + altura_acumulada
        resultados.append(resultado)
        print(f"Trapezoid {trapecio[0]} - Resultado: {resultado:.7f}") # 7 decimales
    
    return resultados