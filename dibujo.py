import sqlite3
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import random


conn = sqlite3.connect("catalogo.db")
cursor = conn.cursor()
cursor.execute("SELECT base_inf, base_sup, altura FROM trapecios WHERE pieza_id = 4 AND tipo_seccion = 5140 ORDER BY posicion")  # Fetch rows with tipo_seccion = 2 and order by posicion
trapecios = cursor.fetchall()
conn.close()

# inicia plot
fig, ax = plt.subplots()


# offset para alinear verticalmente los trapecios
y_offset = 0


# encuentra el ancho del trapecio mas grande para centrar el resto
max_base_inf = max(base_inf for base_inf, _, _ in trapecios)


# Genera color random
def random_color():
    return [random.random(), random.random(), random.random()]


# Itera por todos los trapecios para dibujar la pieza completa
for base_inf, base_sup, altura in trapecios:
    # Calculate the horizontal offset to center the trapezoid
    horizontal_offset = (max_base_inf - base_inf) / 2

    # Calcula coordenadas de trapecio con valores de tuplas
    vertices = [
        (horizontal_offset, y_offset),  # Bottom-left
        (horizontal_offset + base_inf, y_offset),  # Bottom-right
        (horizontal_offset + base_inf - (base_inf - base_sup) / 2, y_offset + altura),  # Top-right
        (horizontal_offset + (base_inf - base_sup) / 2, y_offset + altura)  # Top-left
    ]
    
    # Color random para cada trapecio (Considerar usar paleta fija)
    color = random_color()

    # Agrega trapecio formado a plot con su color aleatorio
    trapezoid = Polygon(vertices, closed=True, edgecolor='blue', facecolor=color)
    ax.add_patch(trapezoid)


    # Mueve offset al tope superior del trapecio recien agregado
    y_offset += altura

# Settea los limited + 0.1 desde el final de la pieza en X,Y
ax.set_xlim(0, max_base_inf + 0.1) 
ax.set_ylim(0, y_offset + 0.1)
ax.set_aspect('equal')
plt.grid(True)
plt.show()




''' ================================================================================================================== '''

# import sqlite3
# import matplotlib.pyplot as plt
# from matplotlib.patches import Polygon
# import random

# # Connect to SQLite and fetch trapezoid data where tipo_seccion = 2
# conn = sqlite3.connect("catalogo.db")  # Replace with your actual database path
# cursor = conn.cursor()
# cursor.execute("SELECT base_inf, base_sup, altura FROM trapecios WHERE pieza_id = 1 AND tipo_seccion = 2 ORDER BY posicion")  
# trapecios = cursor.fetchall()  # Fetch all rows
# conn.close()

# # Initialize plot
# fig, ax = plt.subplots()

# # Variable to track the y-offset for stacking the trapezoids
# y_offset = 0

# # Function to generate random color
# def random_color():
#     return [random.random(), random.random(), random.random()]

# # Iterate through each trapezoid and draw it with a unique color
# for base_inf, base_sup, altura in trapecios:
#     # Calculate trapezoid coordinates based on the database values
#     vertices = [
#         (0.0, y_offset),  # Bottom-left
#         (0.0 + base_inf, y_offset),  # Bottom-right
#         (0.0 + base_inf - (base_inf - base_sup) / 2, y_offset + altura),  # Top-right
#         (0.0 + (base_inf - base_sup) / 2, y_offset + altura)  # Top-left
#     ]
    
#     # Generate a random color for the trapezoid
#     color = random_color()

#     # Create and add the trapezoid to the plot with a unique color
#     trapezoid = Polygon(vertices, closed=True, edgecolor='blue', facecolor=color)
#     ax.add_patch(trapezoid)

#     # Update the y_offset for the next trapezoid
#     y_offset += altura

# # Set plot limits and display
# ax.set_xlim(0, max(base_inf for base_inf, _, _ in trapecios) + 0.2)  # Width adjusted to accommodate the largest trapezoid
# ax.set_ylim(0, y_offset + 0.2)  # Height adjusted to accommodate all trapezoids
# ax.set_aspect('equal')
# plt.grid(True)
# plt.title('Stacked Trapezoids with Different Colors')
# plt.show()

# print(trapecios)

