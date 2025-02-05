''' 
self.tab3_horizontal_layout = QHBoxLayout()
self.tab3_horizontal_layout.setObjectName(u"tab3_horizontal_layout")
    
    self.tab3_line_pos1 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos1.setObjectName(u"tab3_line_pos1")
    self.tab3_line_pos1.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos1)

    self.tab3_combo_pos2 = QComboBox(self.verticalLayoutWidget_2)
    self.tab3_combo_pos2.addItem("")
    self.tab3_combo_pos2.setObjectName(u"tab3_combo_pos2")

    self.tab3_horizontal_layout.addWidget(self.tab3_combo_pos2)

    self.tab3_line_pos3 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos3.setObjectName(u"tab3_line_pos3")
    self.tab3_line_pos3.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos3)

    self.tab3_line_pos4 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos4.setObjectName(u"tab3_line_pos4")
    self.tab3_line_pos4.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos4)

    self.tab3_line_pos5 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos5.setObjectName(u"tab3_line_pos5")
    self.tab3_line_pos5.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos5)

    self.tab3_line_pos6 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos6.setObjectName(u"tab3_line_pos6")
    self.tab3_line_pos6.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos6)

    self.tab3_line_pos7 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos7.setObjectName(u"tab3_line_pos7")
    self.tab3_line_pos7.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos7)

    self.tab3_line_pos8 = QLineEdit(self.verticalLayoutWidget_2)
    self.tab3_line_pos8.setObjectName(u"tab3_line_pos8")
    self.tab3_line_pos8.setAlignment(Qt.AlignmentFlag.AlignCenter)

    self.tab3_horizontal_layout.addWidget(self.tab3_line_pos8)

self.tab3_Vlayout_barras.addLayout(self.tab3_horizontal_layout)
'''

'''
    Contenido de Combo Ubicacion:
        Zona Central
        Zona Extremos
        Apoyo Total
        Apoyo Media Madera

    Contenido de Combo Barras Corrugadas:
        A63-42H
        AT56-50H
'''


def setup_armadura_pasiva(self):
    ''' Se ejecuta desde main cuando inicia app '''
    armpas_llenar_combo_ubicacion(self)
    # TODO Funcionalidad para tab3_btn_aplicar_ubicacion # --> Por ahora no se implementa funcionalidad para seleccion de ubicacion

    


def armpas_llenar_combo_ubicacion(self):
    ''' Contenido fijo, Por lo tanto se hardcodea contenido'''

    self.ui.tab3_combo_ubicacion.addItem("Zona Central")
    self.ui.tab3_combo_ubicacion.addItem("Zona Extremos")
    self.ui.tab3_combo_ubicacion.addItem("Apoyo Total")
    self.ui.tab3_combo_ubicacion.addItem("Apoyo Media Madera")
