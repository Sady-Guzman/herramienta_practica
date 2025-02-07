import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from PySide6.QtWidgets import QApplication, QDialog, QHBoxLayout, QLineEdit, QLabel, QComboBox
from PySide6.QtWidgets import QMessageBox, QApplication, QDialog
from PySide6.QtCore import Qt
from fn_database import db_tipos_hormigon, db_id_tipo_hormigon_nombre, db_resistencias_tipo_hormigon, db_densidades_tipo_hormigon


def setup_tab_materiales(self):
    ''' Se ejecuta desde main cuando inicia app '''
    
    # self.ui.tab3_btn_del_barras.clicked.connect(lambda: apasiva_del_barra_corrugada(self))
    db_tipos_hormigon()
    db_id_tipo_hormigon_nombre("f'c 450/10")
    db_resistencias_tipo_hormigon("f'c 450/10")
    db_densidades_tipo_hormigon("f'c 450/10")




