import math

''' Se usan parametros cargados de base de datos a elementos de tab4 (MATERIALES) para hacer calculos de resistencia '''

# Pedir joaquin mejores nombres para describir funciones
# Y significado eps, es, ec

valor_es = 200000 # MegaPascales

def resistencia_valor_eps(unidad):
    ''' E_ps = 28800 ksi = 198569 MPa'''

    ''' No creo que sea util '''
    if unidad == "ksi":
        return 28800
    elif unidad == "mpa":
        return 198569


def resistencia_ec(self):
    ''' E_c = W_c^(1.5) * 0.043 * sqrt(f'c)'''
    ec = 0

    ec = (pow(float(self.ui.tab4_line_dens_horm.text()), 1.5) * 0.043 * math.sqrt(float(''' f'c ''')))

    ''' En postIt naranja: 1440 kg/m^3 <= W_c <= 2560 kg/m^3'''

