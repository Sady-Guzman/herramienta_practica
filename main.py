import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel
from ui_files.agrega_trapecios_c_layout import Ui_Dialog  # Import from the ui_files directory

# QVLayout: layout_nuevas_row -> Se le agregan tuplas de valor de forma dinamica (manual y selec de catalogo)

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the dialog window
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the dialog window
        self.dynamic_layouts = []  # Initialize dynamic layouts for row management
        self.historial_agregados = 0

        # Connect the signal here
        self.ui.btn_acpt_cant.clicked.connect(self.generate_layout)


    def generate_layout(self):
        # Get the number of frames to generate from the spinbox
        num_rows = self.ui.spin_cant.value()
        print("SpinBox Cantidad a generar value: ", num_rows) # Debug

        # print("elementos dinamicamente agregados: ", self.historial_agregados) # Debug
        # Obtiene el numero de figuras(tuplas) ya existentes en el QVlayout contenedor, se usa para nombrar correctamente los nuevos elementos
        tuplas_existentes = self.historial_agregados

        ''' Loop to create the frames '''
        for i in range(num_rows):
            self.add_rows(self.historial_agregados + 2)  # Starts from trapecio 2 (T2)
        # Agrega stretch al Vertical Layout que contiene las tuplas de elementos para pegarlos al borde superior
        self.ui.layout_nuevas_row.addStretch()

    ''' genera nuevo Hlayout y sus elementos, Los nombra correctamente y agrega a Vlayout contenedor'''
    def add_rows(self, index):
        # Create a new horizontal layout
        layout = QHBoxLayout()
        


        ''' Create the widgets for the row '''
        name_label = QLabel(f"T{index}\t    ")  # usa tab + 4 espacios( 1/2 tab) para coincidir, Aumenta el numero mostrado iterativamente
        bi_line = QLineEdit()
        bs_line = QLineEdit()
        altura_line = QLineEdit()
        area_line = QLineEdit()
        cg_line = QLineEdit()
        inercia_line = QLineEdit()
        op_line = QLineEdit()


        ''' Set object names to refer to them later '''
        name_label.setObjectName(f"t{index}_name")
        bi_line.setObjectName(f"t{index}_bs")
        bs_line.setObjectName(f"t{index}_bi")
        altura_line.setObjectName(f"t{index}_altura")
        area_line.setObjectName(f"t{index}_area")
        cg_line.setObjectName(f"t{index}_cg")
        inercia_line.setObjectName(f"t{index}_inercia")
        op_line.setObjectName(f"t{index}_op")

        ''' Add the widgets to the layout '''
        layout.addWidget(name_label)
        layout.addWidget(bi_line)
        layout.addWidget(bs_line)
        layout.addWidget(altura_line)
        layout.addWidget(area_line)
        layout.addWidget(cg_line)
        layout.addWidget(inercia_line)
        layout.addWidget(op_line)

        ''' Add the layout to the vertical layout container '''
        # Este layout vertical esta bajo el layour horizontal predeterminado de T1.
        self.ui.layout_nuevas_row.addLayout(layout)

        # Store the layout reference to avoid duplicates
        self.dynamic_layouts.append(layout)
        # self.historial_agregados.append(name_label) # Originalmente se guardaba informacion de Label de cada nueva row, Ahora solo se usa un contador += 1
        self.historial_agregados += 1
        print("elementos dinamicamente agregados: ", self.historial_agregados) # Debug
        print("Numero recibido por tuplas_existentes: ", index) # Debug


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application
    dialog = MyDialog()            # Create the dialog window
    dialog.show()                  # Show the dialog window
    sys.exit(app.exec())           # Start the application's event loop


