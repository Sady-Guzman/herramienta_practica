import sqlite3
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import random

# Genera colores en gradientes de verde
def color_personalizado():
    green_intensity = random.uniform(0.6, 0.9)  # varia entre verde oscuro a verde claro
    red_intensity = green_intensity * random.uniform(0.0, 0.15)  
    blue_intensity = green_intensity * random.uniform(0.0, 0.15) 
    return [red_intensity, green_intensity, blue_intensity]
    # return [random.random(), random.random(), random.random()] # completamente random


def plot_trapecios(pieza_id, seccion, familia, modelo, es_creada):

    # conecta a DB dependiendo de flag
    if es_creada == False:
        conn = sqlite3.connect("catalogo.db")
    else:
        conn = sqlite3.connect("piezas_creadas.db")

    cursor = conn.cursor()
    print(pieza_id, seccion)
    cursor.execute("SELECT base_inf, base_sup, altura FROM trapecios WHERE pieza_id = ? AND tipo_seccion = ? ORDER BY posicion", (pieza_id, seccion))
    trapecios = cursor.fetchall()
    conn.close()


    # Crea figura y axis 
    fig, ax = plt.subplots()

    y_offset = 0  # Offset para alinear los trapecios verticalmente (acumula altura de cada trap.)
    max_base_inf = max(base_inf for base_inf, _, _ in trapecios)  # encuentra el trapecio con la base mas grande para centrar fig

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


        # Usa funcion de color todo de verde
        color = color_personalizado()


        # Agrega el trapecio al plot
        trapezoid = Polygon(vertices, closed=True, edgecolor='blue', facecolor=color)
        ax.add_patch(trapezoid)


        # Acumula la altura del trapecio en offset para ajustar el proximo trapecio
        y_offset += altura

    # settea limite de plot
    ax.set_xlim(0, max_base_inf + 0.1)
    ax.set_ylim(0, y_offset + 0.1)
    ax.set_aspect('equal')
    plt.title(f"Familia: {familia}, Modelo: {modelo}")
    plt.grid(True)
    plt.show()