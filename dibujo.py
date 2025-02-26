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




def plot_trapecios(self):

    try:
        # print("Valor de seccion seleccionada:", self.seccion_pieza_cargada)

        trapecios = self.dynamic_layout_data[self.seccion_pieza_cargada]
        trapecios = list(trapecios)

        # print("Trapecios data:", trapecios)  # Debugging

        # Process correctly based on tuple size
        trapecios = [
            (float(t[1]), float(t[2]), float(t[3]), 0)  # Default h=0 if missing
            if len(t) == 4 else (float(t[1]), float(t[2]), float(t[3]), int(t[4]))  # Use 7th column if it exists
            for t in trapecios
        ]

        # print("trapecios procesados:", trapecios)

    except Exception as e:
        print(">Error en Dibujo ___ Except:", e)
        return



    # Crea figura y axis 
    fig, ax = plt.subplots()

    y_offset = 0  # Offset para alinear los trapecios verticalmente (acumula altura de cada trap.)
    max_base_inf = max(base_inf for base_inf, _, _, _ in trapecios)  # encuentra el trapecio con la base mas grande para centrar fig

    tono_color = 0.55
    # Itera todos lso trapecios para 
    for base_inf, base_sup, altura, es_insitu in trapecios:

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
        # print("\n---->Es insitu:", es_insitu)

        # INSITU USA COLOR GRIS
        if es_insitu == 1:
            color = (0.62, 0.62, 0.62)
        else:
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
