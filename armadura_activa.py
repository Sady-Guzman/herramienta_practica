''' codigo para manejar armaduras activas de forma finamica '''

'''
    Se generan y manejan componentes dinamicamente usando listas y diccionarios.

    En tab2 se define un Grid_Layout como contenedor para los elementos que estaran dentro de 
    nuevos layouts dinamicamente generados segun la necesidad del usario.

    Cotas se manejan en un VerticalLayout al que se le agregan dinamicamente LineEdits usando un boton 
    (El usuario puede elegir que cota agregar, Usando una lista con las cotas disponibles en el testero seleccionado, 
    Puede ser en una ventana emergente como en JACENA).
    Al agregar una cota hay que agregar un lineEdit a todos los otros VerticalLayouts que existen (Numero cordones y TPI, de cada tipo de corodon).
    Los valores de las cotas se guardan en lista self.dynamic_cotas[]

    Numero de cordones por cota se especifican en lineEdits que son agregados alineados con la posicion de las cotas. Se agregan a un VerticalLayout que es dinamicamente generado cuando el usuario agrega un tipo de cordon.
    Valores de estos lineEdits se almacenan en diccionario self.dynamic_cant_ordones{}. Un index de diccionario para cada tipo de cordon, dentro del index la lista guarda los valores de los lineEdits de esa columna (Vlayout).
    Este diccionario guarda los valores de todos los distintos tipos de cordones, Asignando un indice para cada tipo de cordon y usando la lista correspondiente a ese indice para almacenar los valores de ese cordon.

    TPI se guardan de la misma manera que numero de cordones, en su propio diccionario: self.dynamic_tpi{}, index y listas de cada indice se maneja de la misma forma que numero de cordones.

    tipos de cordones se manejan con self.dynamic_diametros_arm_act{}, donde cada indice corresponde a un tipo de cordon y dentro esta el valor actual de ComboBox
'''

from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox

def setup_armadura_activa(self):
    self.ui.tab2_btn_add_cota.clicked.connect(self.add_cota)
    self.ui.tab2_btn_add_cord.clicked.connect(self.add_cordon)

    self.ui.tab2_btn_valores.clicked.connect(lambda: print_all_values())

    def print_all_values():
        # Print all ComboBox values
        print("ComboBox Values:")
        for i, combo in enumerate(self.dynamic_diametros_arm_act):
            print(f"  ComboBox {i + 1}: {combo.currentText()}")

        # Print all values for num_cordones and tpi
        print("\nCordones and TPI Values:")
        for index, cordon in self.dynamic_cordones_arm_act.items():
            print(f"  Cordon {index + 1}:")
            
            # Print num_cordones values
            print("    Num Cordones:")
            for j, num_cordon in enumerate(cordon['num_cordones']):
                print(f"      {j + 1}: {num_cordon.text()}")

            # Print tpi values
            print("    TPI:")
            for j, tpi in enumerate(cordon['tpi']):
                print(f"      {j + 1}: {tpi.text()}")

        # Print all cota values
        print("\nCotas:")
        for i, cota in enumerate(self.dynamic_cotas):
            print(f"  Cota {i + 1}: {cota.text()}")
        

class ArmaduraActiva:
    def __init__(self):
        self.dynamic_cotas = []
        self.dynamic_diametros_arm_act = []
        self.dynamic_cordones_arm_act = {}
        self.dynamic_tpi_arm_act = {}

    # def setupUi(self, Dialog):
    #     # ...existing code...
    #     self.ui.tab2_btn_add_cota.clicked.connect(self.add_cota)
    #     self.ui.tab2_btn_add_cord.clicked.connect(self.add_cordon)
    #     # Add buttons to the layout
    #     self.verticalLayout.addWidget(self.ui.tab2_btn_add_cota)
    #     self.verticalLayout.addWidget(self.ui.tab2_btn_add_cord)
    #     # ...existing code...

    def confirmar_borrar(self, index):
        reply = QMessageBox.question(self, 'Confirmar', "Confirmar acción?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return 0
        else:
            self.del_cordon(index)

    

