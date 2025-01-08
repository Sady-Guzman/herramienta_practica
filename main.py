import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from ui_files.agrega_trapecios_v2 import Ui_Dialog  # Import from the ui_files directory


# QVLayout: layout_nuevas_row -> Se le agregan tuplas de valor de forma dinamica (manual y selec de catalogo)
# historial_agregados -> Contador de tuplas que se agregaron dinamicamente a QVlayout
        

class MyDialog(QDialog):
    # def __init__(self):
    #     super().__init__()
    #     self.ui = Ui_Dialog()  # Create an instance of the UI class
    #     self.ui.setupUi(self)  # Set up the UI on the dialog window
        
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the dialog window
        self.dynamic_layouts = []  # Initialize dynamic layouts for row management
        self.historial_agregados = 0

        # Conecta boton que acepta agregar tuplas a func generate_layout()
        self.ui.btn_acpt_agregar.clicked.connect(self.generate_layout)

        # Conecta boton que aceptar eliminar tuplas func del_rows()
        self.ui.btn_acpt_eliminar.clicked.connect(self.del_rows)


    def generate_layout(self):
        # obtiene el numero de tuplas a generar de la spinbox 'spin_cant_agregar'
        num_rows = self.ui.spin_cant_agregar.value()
        print("debug_print> SpinBox Cantidad a generar value: ", num_rows) # Debug

        # print("elementos dinamicamente agregados: ", self.historial_agregados) # Debug
        # Obtiene el numero de figuras(tuplas) ya existentes en el QVlayout contenedor, se usa para nombrar correctamente los nuevos elementos
        tuplas_existentes = self.historial_agregados

        ''' Loop to create the frames '''
        for i in range(num_rows):
            self.add_rows(self.historial_agregados + 2)  # Starts from trapecio 2 (T2)
        # Agrega stretch al Vertical Layout que contiene las tuplas de elementos para pegarlos al borde superior
        # self.ui.layout_nuevas_row.addStretch()


    ''' genera nuevo Hlayout y sus elementos, Los nombra correctamente y agrega a Vlayout contenedor'''
    def add_rows(self, index):
        
        ''' maneja vertical stretcher para solo tener 1 y que siempre este abajo'''
        if self.ui.layout_nuevas_row.itemAt(self.ui.layout_nuevas_row.count()-1).spacerItem():
            # item = ultimo que se encuentra (vertical stretcher)
            # Lo elimina mientras agrega nuevas tuplas, Lo vuelve a ingresar despues.
            item = self.ui.layout_nuevas_row.takeAt(self.ui.layout_nuevas_row.count()-1)
            del item
        
        ''' crea un nuevo Hlayout para agregar elementos de nueva tupla '''
        layout = QHBoxLayout()
        # Asigna nombre a layout generado dinamicamente
        layout_name = f"layout_t{index}"
        

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
        # Este layout vertical esta bajo el layout horizontal predeterminado de T1.
        self.ui.layout_nuevas_row.addLayout(layout)

        ''' se vuelve a insertar vertical stretcher en posicion inferior de layout vertical '''
        self.ui.layout_nuevas_row.addStretch()

        # Store the layout reference to avoid duplicates
        self.dynamic_layouts.append(layout)
        # self.historial_agregados.append(name_label) # Originalmente se guardaba informacion de Label de cada nueva row, Ahora solo se usa un contador += 1
        self.historial_agregados += 1


    ''' Elimina tuplas que fueron creadas dinamicamente dentro del layout vertical '''
    def del_rows(self, index):
        # obtiene el numero de tuplas a generar de la spinbox 'spin_cant_agregar'
        num_rows = self.ui.spin_cant_eliminar.value()

        # Asegura que la cantidad de layouts dinamicos que se van a intentar borrar no superen a la cantidad existente
        # Si usa boton mientras spin=0, sale para evitar bug en contador dinamico
        if num_rows > self.historial_agregados:
            num_rows = self.historial_agregados
        elif num_rows == 0:
            return
        
        # Pide confirmacion de usuario antes de borrar layouts
        reply = QMessageBox.question(self, 'Confirmar', 
                                    "Confirmar: Eliminar cantidad de tuplas seleccionadas?", 
                                    QMessageBox.Yes  | QMessageBox.No, 
                                    QMessageBox.No)
        if reply == QMessageBox.No:
            return  # escapa con NO
        
        print("debug_print> SpinBox Cantidad a eliminar value: ", num_rows) # Debug

        
        ''' Elimina stretcher vertical en ultima posicion, se inserta nuevamente al final de proceso'''
        if self.ui.layout_nuevas_row.itemAt(self.ui.layout_nuevas_row.count()-1).spacerItem():
            # item = ultimo que se encuentra (vertical stretcher)
            # Lo elimina mientras agrega nuevas tuplas, Lo vuelve a ingresar despues.
            item = self.ui.layout_nuevas_row.takeAt(self.ui.layout_nuevas_row.count()-1)
            del item


        ''' Itera por los elementos de layout contenedor 'layout_nuevas_row' eliminando ultimos agregados'''
        # Usa funcion 'delete_layout_widgets()
        for _ in range(num_rows):
            # Elimina la ultima tupla (layout) del layout contenedor
            if self.ui.layout_nuevas_row.count() > 0:
                last_item = self.ui.layout_nuevas_row.takeAt(self.ui.layout_nuevas_row.count() - 1)
                
                # comprueba que sea un layout (siempre deberia serlo) y usa funcion para eliminar iterando por sus elementos
                if last_item.layout():
                    self.delete_layout_widgets(last_item.layout())
                del last_item  # elimina layout

        ''' disminuye el contador de layouts que existen dinamicamente '''
        self.historial_agregados -= num_rows

        ''' se vuelve a insertar vertical stretcher en posicion inferior de layout vertical '''
        self.ui.layout_nuevas_row.addStretch()

    
    
    ''' Elimina los widgets dentro de un layout '''
    def delete_layout_widgets(self, layout):
        # Iterate through all the widgets in the layout and delete them
        while layout.count():
            item = layout.takeAt(0)  # Take the first item
            if item.widget():  # If it's a widget, delete it
                item.widget().deleteLater()
            elif item.layout():  # If it's another layout, recursively delete its widgets
                self.delete_layout_widgets(item.layout())  # Recursive call to delete nested layouts



if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application
    dialog = MyDialog()            # Create the dialog window
    dialog.show()                  # Show the dialog window
    sys.exit(app.exec())           # Start the application's event loop



