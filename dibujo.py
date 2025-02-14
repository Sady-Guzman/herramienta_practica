import sqlite3
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import random
import os

# DB_DIR = os.path.join(os.path.dirname(__file__), "databases")
from fn_database import get_db_path

# Genera colores en gradientes de verde
def color_personalizado(tono_verde):
    green_intensity = tono_verde  # varia entre verde oscuro a verde claro
    red_intensity = green_intensity * random.uniform(0.0, 0.15)  
    blue_intensity = green_intensity * random.uniform(0.0, 0.15) 
    return [red_intensity, green_intensity, blue_intensity]
    # return [random.random(), random.random(), random.random()] # completamente random


# def plot_trapecios(pieza_id, seccion, familia, modelo, es_creada, self):

#     print(f"{familia} -- {modelo} -- {seccion}")
#     if familia == 0 or modelo == 0 or seccion == 0:
#         return

#     # conecta a DB dependiendo de flag
#     if es_creada == False:
#         # conn = sqlite3.connect("catalogo.db")
#         # db_path = os.path.join(DB_DIR, "catalogo.db")
#         db_path = get_db_path("catalogo.db")
#     else:
#         # conn = sqlite3.connect("piezas_creadas.db")
#         # db_path = os.path.join(DB_DIR, "catalogo.db")
#         db_path = get_db_path("piezas_creadas.db") # Eventualmente cambiar a piezas_creadas cuando se implemente grafico con datos dinamicos
#         return

#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
    
#     print(pieza_id, seccion)
#     cursor.execute("SELECT base_inf, base_sup, altura FROM trapecios WHERE pieza_id = ? AND tipo_seccion = ? ORDER BY posicion", (pieza_id, seccion))
#     trapecios = cursor.fetchall()
#     conn.close()

#     print("\n\n\t\t Informacion de tuplas en dibujo.py para trapecios [] ---> ", trapecios)
#     try:
#         print("\n\n\t\t Informacion de tuplas en dibujo.py para self.dynamic_layout_data [] ---> ", self.dynamic_layout_data[seccion])
#         trapecios = self.dynamic_layout_data[seccion]
#         trapecios = list(reversed(trapecios))
#         # Strip the first item from each tuple
#         trapecios = [(b, c, d) for _, b, c, d in trapecios]
#         print("\n\n\t\t Informacion de tuplas en dibujo.py para trapecios invertidos[] ---> ", trapecios)
#     except:
#         pass



#     # Crea figura y axis 
#     fig, ax = plt.subplots()

#     y_offset = 0  # Offset para alinear los trapecios verticalmente (acumula altura de cada trap.)
#     max_base_inf = max(base_inf for base_inf, _, _ in trapecios)  # encuentra el trapecio con la base mas grande para centrar fig

#     tono_color = 0.55
#     # Itera todos lso trapecios para 
#     for base_inf, base_sup, altura in trapecios:

#         # Calculo el offset horizontal hasta el centro del trapecio
#         horizontal_offset = (max_base_inf - base_inf) / 2


#         # Def coordenadas de los trapecios
#         vertices = [
#             (horizontal_offset, y_offset),  # Bottom-left
#             (horizontal_offset + base_inf, y_offset),  # Bottom-right
#             (horizontal_offset + base_inf - (base_inf - base_sup) / 2, y_offset + altura),  # Top-right
#             (horizontal_offset + (base_inf - base_sup) / 2, y_offset + altura)  # Top-left
#         ]

#         # Asegura que no se pase de 0.99 en alpha de color verde
#         if tono_color > 0.99:
#             tono_color = 0.7

#         # Usa funcion de color todo de verde
#         color = color_personalizado(tono_color)
#         tono_color += 0.04


#         # Agrega el trapecio al plot
#         trapezoid = Polygon(vertices, closed=True, edgecolor='blue', facecolor=color)
#         ax.add_patch(trapezoid)


#         # Acumula la altura del trapecio en offset para ajustar el proximo trapecio
#         y_offset += altura

#     # settea limite de plot
#     ax.set_xlim(0, max_base_inf + 0.1)
#     ax.set_ylim(0, y_offset + 0.1)
#     ax.set_aspect('equal')
#     plt.title(f"Familia: {familia}, Modelo: {modelo}")
#     plt.grid(True)
#     plt.show()





def plot_trapecios(self):

    try:
        print("Valor de seccion seleccionada: ", self.seccion_pieza_cargada)
    except:
        print("no existe seccion pieza cargada en variable")
        pass
    try:
        trapecios = self.dynamic_layout_data[self.seccion_pieza_cargada]
        trapecios = list(trapecios)
        # Strip the first item from each tuple
        trapecios = [(float(b), float(c), float(d)) for _, b, c, d in trapecios]
        if self.es_temporal == False and self.es_creada == False:
            print("Se invierte lista porque es_temporal = FALSE, es_creada = FALSE")
            # trapecios = list(reversed(trapecios))
        else:
            print("No se invierte la lista porque no se cumple con: es_temporal = FALSE, es_creada = FALSE")
            # trapecios = list(reversed(trapecios))
    except:
        print("En Dibujo ___ Execept: Return")
        return



    # Crea figura y axis 
    fig, ax = plt.subplots()

    y_offset = 0  # Offset para alinear los trapecios verticalmente (acumula altura de cada trap.)
    max_base_inf = max(base_inf for base_inf, _, _ in trapecios)  # encuentra el trapecio con la base mas grande para centrar fig

    tono_color = 0.55
    # Itera todos lso trapecios para 
    for base_inf, base_sup, altura in trapecios:

        # Calculo el offset horizontal hasta el centro del trapecio
        horizontal_offset = (max_base_inf - base_inf) / 2


        # Def coordenadas de los trapecios
        vertices = [
            (horizontal_offset, y_offset),  # Bottom-left
            (horizontal_offset + base_inf, y_offset),  # Bottom-right
            (horizontal_offset + base_inf - (base_inf - base_sup) / 2, y_offset + altura),  # Top-right
            (horizontal_offset + (base_inf - base_sup) / 2, y_offset + altura)  # Top-left
        ]

        # Asegura que no se pase de 0.99 en alpha de color verde
        # if tono_color > 0.99:
            # tono_color = 0.7

        # Usa funcion de color todo de verde
        # color = color_personalizado(tono_color)
        # tono_color += 0.04
        color = (0.1, 0.9, 0.1)


        # Agrega el trapecio al plot
        trapezoid = Polygon(vertices, closed=True, edgecolor='blue', facecolor=color)
        ax.add_patch(trapezoid)


        # Acumula la altura del trapecio en offset para ajustar el proximo trapecio
        y_offset += altura

    # settea limite de plot
    ax.set_xlim(0, max_base_inf + 0.1)
    ax.set_ylim(0, y_offset + 0.1)
    ax.set_aspect('equal')
    plt.title(f"Familia: {self.familia_pieza_cargada}, Modelo: {self.modelo_pieza_cargada}")
    plt.grid(True)
    plt.show()
