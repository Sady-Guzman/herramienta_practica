# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'herramienta_trapecios_v9.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1125, 680)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setBold(False)
        font.setItalic(False)
        Dialog.setFont(font)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 1101, 661))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.btn_save_pieza = QPushButton(self.tab)
        self.btn_save_pieza.setObjectName(u"btn_save_pieza")
        self.btn_save_pieza.setGeometry(QRect(10, 591, 221, 31))
        self.btn_save_pieza.setAutoDefault(False)
        self.verticalLayoutWidget_5 = QWidget(self.tab)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(290, 240, 751, 351))
        self.layout_nuevas_row = QVBoxLayout(self.verticalLayoutWidget_5)
        self.layout_nuevas_row.setObjectName(u"layout_nuevas_row")
        self.layout_nuevas_row.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_nuevas_row.addItem(self.verticalSpacer)

        self.label_guardar_pieza = QLabel(self.tab)
        self.label_guardar_pieza.setObjectName(u"label_guardar_pieza")
        self.label_guardar_pieza.setGeometry(QRect(10, 570, 221, 21))
        self.horizontalLayoutWidget = QWidget(self.tab)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(290, 210, 751, 31))
        self.Hlayout_label_variables = QHBoxLayout(self.horizontalLayoutWidget)
        self.Hlayout_label_variables.setObjectName(u"Hlayout_label_variables")
        self.Hlayout_label_variables.setContentsMargins(0, 0, 0, 0)
        self.label_name = QLabel(self.horizontalLayoutWidget)
        self.label_name.setObjectName(u"label_name")

        self.Hlayout_label_variables.addWidget(self.label_name)

        self.label_bi = QLabel(self.horizontalLayoutWidget)
        self.label_bi.setObjectName(u"label_bi")

        self.Hlayout_label_variables.addWidget(self.label_bi)

        self.label_bs = QLabel(self.horizontalLayoutWidget)
        self.label_bs.setObjectName(u"label_bs")

        self.Hlayout_label_variables.addWidget(self.label_bs)

        self.label_altura = QLabel(self.horizontalLayoutWidget)
        self.label_altura.setObjectName(u"label_altura")

        self.Hlayout_label_variables.addWidget(self.label_altura)

        self.label_area = QLabel(self.horizontalLayoutWidget)
        self.label_area.setObjectName(u"label_area")

        self.Hlayout_label_variables.addWidget(self.label_area)

        self.label_cg = QLabel(self.horizontalLayoutWidget)
        self.label_cg.setObjectName(u"label_cg")

        self.Hlayout_label_variables.addWidget(self.label_cg)

        self.label_inercia = QLabel(self.horizontalLayoutWidget)
        self.label_inercia.setObjectName(u"label_inercia")

        self.Hlayout_label_variables.addWidget(self.label_inercia)

        self.label_op = QLabel(self.horizontalLayoutWidget)
        self.label_op.setObjectName(u"label_op")

        self.Hlayout_label_variables.addWidget(self.label_op)

        self.verticalLayoutWidget_4 = QWidget(self.tab)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(950, 10, 131, 116))
        self.Vlayout_resultados = QVBoxLayout(self.verticalLayoutWidget_4)
        self.Vlayout_resultados.setObjectName(u"Vlayout_resultados")
        self.Vlayout_resultados.setContentsMargins(0, 0, 0, 0)
        self.result_sum_altura = QLineEdit(self.verticalLayoutWidget_4)
        self.result_sum_altura.setObjectName(u"result_sum_altura")
        self.result_sum_altura.setReadOnly(True)

        self.Vlayout_resultados.addWidget(self.result_sum_altura)

        self.result_sum_area = QLineEdit(self.verticalLayoutWidget_4)
        self.result_sum_area.setObjectName(u"result_sum_area")
        self.result_sum_area.setReadOnly(True)

        self.Vlayout_resultados.addWidget(self.result_sum_area)

        self.result_sum_ponderado = QLineEdit(self.verticalLayoutWidget_4)
        self.result_sum_ponderado.setObjectName(u"result_sum_ponderado")
        self.result_sum_ponderado.setReadOnly(True)

        self.Vlayout_resultados.addWidget(self.result_sum_ponderado)

        self.result_sum_op = QLineEdit(self.verticalLayoutWidget_4)
        self.result_sum_op.setObjectName(u"result_sum_op")
        self.result_sum_op.setReadOnly(True)

        self.Vlayout_resultados.addWidget(self.result_sum_op)

        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(290, 10, 337, 91))
        self.Glayout_edita_tuplas = QGridLayout(self.gridLayoutWidget)
        self.Glayout_edita_tuplas.setObjectName(u"Glayout_edita_tuplas")
        self.Glayout_edita_tuplas.setContentsMargins(0, 0, 0, 0)
        self.spin_cant_agregar = QSpinBox(self.gridLayoutWidget)
        self.spin_cant_agregar.setObjectName(u"spin_cant_agregar")

        self.Glayout_edita_tuplas.addWidget(self.spin_cant_agregar, 1, 0, 1, 1)

        self.label_cant_agregar = QLabel(self.gridLayoutWidget)
        self.label_cant_agregar.setObjectName(u"label_cant_agregar")

        self.Glayout_edita_tuplas.addWidget(self.label_cant_agregar, 0, 0, 1, 1)

        self.spin_cant_eliminar = QSpinBox(self.gridLayoutWidget)
        self.spin_cant_eliminar.setObjectName(u"spin_cant_eliminar")

        self.Glayout_edita_tuplas.addWidget(self.spin_cant_eliminar, 1, 1, 1, 1)

        self.btn_acpt_eliminar = QPushButton(self.gridLayoutWidget)
        self.btn_acpt_eliminar.setObjectName(u"btn_acpt_eliminar")

        self.Glayout_edita_tuplas.addWidget(self.btn_acpt_eliminar, 2, 1, 1, 1)

        self.label_cant_eliminar = QLabel(self.gridLayoutWidget)
        self.label_cant_eliminar.setObjectName(u"label_cant_eliminar")

        self.Glayout_edita_tuplas.addWidget(self.label_cant_eliminar, 0, 1, 1, 1)

        self.btn_acpt_agregar = QPushButton(self.gridLayoutWidget)
        self.btn_acpt_agregar.setObjectName(u"btn_acpt_agregar")

        self.Glayout_edita_tuplas.addWidget(self.btn_acpt_agregar, 2, 0, 1, 1)

        self.btn_calcular_nuevos_valores = QPushButton(self.tab)
        self.btn_calcular_nuevos_valores.setObjectName(u"btn_calcular_nuevos_valores")
        self.btn_calcular_nuevos_valores.setGeometry(QRect(290, 180, 171, 32))
        self.btn_calcular_nuevos_valores.setAutoDefault(False)
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 211, 400))
        self.Vlayout_catalogo = QVBoxLayout(self.verticalLayoutWidget)
        self.Vlayout_catalogo.setObjectName(u"Vlayout_catalogo")
        self.Vlayout_catalogo.setContentsMargins(0, 0, 0, 0)
        self.btn_usar_pieza_catalogo = QPushButton(self.verticalLayoutWidget)
        self.btn_usar_pieza_catalogo.setObjectName(u"btn_usar_pieza_catalogo")
        self.btn_usar_pieza_catalogo.setAutoDefault(False)

        self.Vlayout_catalogo.addWidget(self.btn_usar_pieza_catalogo)

        self.btn_usar_pieza_usuario = QPushButton(self.verticalLayoutWidget)
        self.btn_usar_pieza_usuario.setObjectName(u"btn_usar_pieza_usuario")
        self.btn_usar_pieza_usuario.setAutoDefault(False)

        self.Vlayout_catalogo.addWidget(self.btn_usar_pieza_usuario)

        self.btn_crear_pieza_temp = QPushButton(self.verticalLayoutWidget)
        self.btn_crear_pieza_temp.setObjectName(u"btn_crear_pieza_temp")
        self.btn_crear_pieza_temp.setAutoDefault(False)

        self.Vlayout_catalogo.addWidget(self.btn_crear_pieza_temp)

        self.label_familia = QLabel(self.verticalLayoutWidget)
        self.label_familia.setObjectName(u"label_familia")

        self.Vlayout_catalogo.addWidget(self.label_familia)

        self.combo_familia = QComboBox(self.verticalLayoutWidget)
        self.combo_familia.setObjectName(u"combo_familia")

        self.Vlayout_catalogo.addWidget(self.combo_familia)

        self.label_modelo = QLabel(self.verticalLayoutWidget)
        self.label_modelo.setObjectName(u"label_modelo")

        self.Vlayout_catalogo.addWidget(self.label_modelo)

        self.combo_modelo = QComboBox(self.verticalLayoutWidget)
        self.combo_modelo.setObjectName(u"combo_modelo")

        self.Vlayout_catalogo.addWidget(self.combo_modelo)

        self.label_tipo_seccion = QLabel(self.verticalLayoutWidget)
        self.label_tipo_seccion.setObjectName(u"label_tipo_seccion")

        self.Vlayout_catalogo.addWidget(self.label_tipo_seccion)

        self.list_tipo_seccion = QListWidget(self.verticalLayoutWidget)
        self.list_tipo_seccion.setObjectName(u"list_tipo_seccion")

        self.Vlayout_catalogo.addWidget(self.list_tipo_seccion)

        self.btn_acpt_tipo_seccion = QPushButton(self.verticalLayoutWidget)
        self.btn_acpt_tipo_seccion.setObjectName(u"btn_acpt_tipo_seccion")
        self.btn_acpt_tipo_seccion.setAutoDefault(False)

        self.Vlayout_catalogo.addWidget(self.btn_acpt_tipo_seccion)

        self.btn_save_seccion = QPushButton(self.verticalLayoutWidget)
        self.btn_save_seccion.setObjectName(u"btn_save_seccion")
        self.btn_save_seccion.setAutoDefault(False)

        self.Vlayout_catalogo.addWidget(self.btn_save_seccion)

        self.verticalLayoutWidget_3 = QWidget(self.tab)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(880, 10, 71, 121))
        self.Vlayout_label_resultados = QVBoxLayout(self.verticalLayoutWidget_3)
        self.Vlayout_label_resultados.setObjectName(u"Vlayout_label_resultados")
        self.Vlayout_label_resultados.setContentsMargins(0, 0, 0, 0)
        self.label_sum_altura = QLabel(self.verticalLayoutWidget_3)
        self.label_sum_altura.setObjectName(u"label_sum_altura")
        self.label_sum_altura.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.Vlayout_label_resultados.addWidget(self.label_sum_altura)

        self.label_sum_area = QLabel(self.verticalLayoutWidget_3)
        self.label_sum_area.setObjectName(u"label_sum_area")
        self.label_sum_area.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.Vlayout_label_resultados.addWidget(self.label_sum_area)

        self.label_sum_ponderado = QLabel(self.verticalLayoutWidget_3)
        self.label_sum_ponderado.setObjectName(u"label_sum_ponderado")
        self.label_sum_ponderado.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.Vlayout_label_resultados.addWidget(self.label_sum_ponderado)

        self.label_sum_op = QLabel(self.verticalLayoutWidget_3)
        self.label_sum_op.setObjectName(u"label_sum_op")
        self.label_sum_op.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.Vlayout_label_resultados.addWidget(self.label_sum_op)

        self.btn_salto_linea = QPushButton(self.tab)
        self.btn_salto_linea.setObjectName(u"btn_salto_linea")
        self.btn_salto_linea.setGeometry(QRect(10, 540, 100, 32))
        self.tab1_list_trapecios_existentes = QListWidget(self.tab)
        self.tab1_list_trapecios_existentes.setObjectName(u"tab1_list_trapecios_existentes")
        self.tab1_list_trapecios_existentes.setGeometry(QRect(650, 10, 201, 121))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 190, 1061, 351))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(-1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab2_label_cota = QLabel(self.gridLayoutWidget_2)
        self.tab2_label_cota.setObjectName(u"tab2_label_cota")
        self.tab2_label_cota.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout.addWidget(self.tab2_label_cota)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.tab2_relleno_layout_armaduras = QPushButton(self.gridLayoutWidget_2)
        self.tab2_relleno_layout_armaduras.setObjectName(u"tab2_relleno_layout_armaduras")
        self.tab2_relleno_layout_armaduras.setEnabled(True)
        self.tab2_relleno_layout_armaduras.setMaximumSize(QSize(75, 16777215))

        self.gridLayout.addWidget(self.tab2_relleno_layout_armaduras, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.tab2_btn_add_cota_custom = QPushButton(self.tab_2)
        self.tab2_btn_add_cota_custom.setObjectName(u"tab2_btn_add_cota_custom")
        self.tab2_btn_add_cota_custom.setGeometry(QRect(10, 40, 101, 32))
        self.tab2_btn_add_cord = QPushButton(self.tab_2)
        self.tab2_btn_add_cord.setObjectName(u"tab2_btn_add_cord")
        self.tab2_btn_add_cord.setGeometry(QRect(230, 40, 111, 32))
        self.tab2_btn_del_cota = QPushButton(self.tab_2)
        self.tab2_btn_del_cota.setObjectName(u"tab2_btn_del_cota")
        self.tab2_btn_del_cota.setGeometry(QRect(120, 40, 100, 32))
        self.tab2_btn_del_cord = QPushButton(self.tab_2)
        self.tab2_btn_del_cord.setObjectName(u"tab2_btn_del_cord")
        self.tab2_btn_del_cord.setGeometry(QRect(230, 70, 111, 32))
        self.gridLayoutWidget_3 = QWidget(self.tab_2)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(899, 10, 171, 116))
        self.tab2_gridLayout_totales = QGridLayout(self.gridLayoutWidget_3)
        self.tab2_gridLayout_totales.setObjectName(u"tab2_gridLayout_totales")
        self.tab2_gridLayout_totales.setContentsMargins(0, 0, 0, 0)
        self.tab2_label_cant_cord = QLabel(self.gridLayoutWidget_3)
        self.tab2_label_cant_cord.setObjectName(u"tab2_label_cant_cord")
        self.tab2_label_cant_cord.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab2_gridLayout_totales.addWidget(self.tab2_label_cant_cord, 0, 0, 1, 1)

        self.tab2_label_cdg_area = QLabel(self.gridLayoutWidget_3)
        self.tab2_label_cdg_area.setObjectName(u"tab2_label_cdg_area")
        self.tab2_label_cdg_area.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab2_gridLayout_totales.addWidget(self.tab2_label_cdg_area, 2, 0, 1, 1)

        self.tab2_label_area_total = QLabel(self.gridLayoutWidget_3)
        self.tab2_label_area_total.setObjectName(u"tab2_label_area_total")
        self.tab2_label_area_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab2_gridLayout_totales.addWidget(self.tab2_label_area_total, 1, 0, 1, 1)

        self.tab2_line_total_cdg_area = QLineEdit(self.gridLayoutWidget_3)
        self.tab2_line_total_cdg_area.setObjectName(u"tab2_line_total_cdg_area")

        self.tab2_gridLayout_totales.addWidget(self.tab2_line_total_cdg_area, 2, 1, 1, 1)

        self.tab2_line_total_area = QLineEdit(self.gridLayoutWidget_3)
        self.tab2_line_total_area.setObjectName(u"tab2_line_total_area")

        self.tab2_gridLayout_totales.addWidget(self.tab2_line_total_area, 1, 1, 1, 1)

        self.tab2_line_total_cordones = QLineEdit(self.gridLayoutWidget_3)
        self.tab2_line_total_cordones.setObjectName(u"tab2_line_total_cordones")

        self.tab2_gridLayout_totales.addWidget(self.tab2_line_total_cordones, 0, 1, 1, 1)

        self.tab2_label_cdg_fuerza = QLabel(self.gridLayoutWidget_3)
        self.tab2_label_cdg_fuerza.setObjectName(u"tab2_label_cdg_fuerza")
        self.tab2_label_cdg_fuerza.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab2_gridLayout_totales.addWidget(self.tab2_label_cdg_fuerza, 3, 0, 1, 1)

        self.tab2_line_total_cdg_fuerza = QLineEdit(self.gridLayoutWidget_3)
        self.tab2_line_total_cdg_fuerza.setObjectName(u"tab2_line_total_cdg_fuerza")

        self.tab2_gridLayout_totales.addWidget(self.tab2_line_total_cdg_fuerza, 3, 1, 1, 1)

        self.tab2_btn_valores = QPushButton(self.tab_2)
        self.tab2_btn_valores.setObjectName(u"tab2_btn_valores")
        self.tab2_btn_valores.setGeometry(QRect(10, 150, 171, 32))
        self.tab2_label_cota_dinamica = QLabel(self.tab_2)
        self.tab2_label_cota_dinamica.setObjectName(u"tab2_label_cota_dinamica")
        self.tab2_label_cota_dinamica.setGeometry(QRect(10, 20, 101, 16))
        self.tab2_btn_add_cota_testero = QPushButton(self.tab_2)
        self.tab2_btn_add_cota_testero.setObjectName(u"tab2_btn_add_cota_testero")
        self.tab2_btn_add_cota_testero.setGeometry(QRect(10, 70, 101, 32))
        self.tab2_label_cota_dinamica_2 = QLabel(self.tab_2)
        self.tab2_label_cota_dinamica_2.setObjectName(u"tab2_label_cota_dinamica_2")
        self.tab2_label_cota_dinamica_2.setGeometry(QRect(230, 20, 101, 16))
        self.tab2_label_testero = QLabel(self.tab_2)
        self.tab2_label_testero.setObjectName(u"tab2_label_testero")
        self.tab2_label_testero.setGeometry(QRect(610, 20, 113, 18))
        self.tab2_combo_testero = QComboBox(self.tab_2)
        self.tab2_combo_testero.setObjectName(u"tab2_combo_testero")
        self.tab2_combo_testero.setGeometry(QRect(610, 44, 141, 32))
        self.tab2_combo_preset = QComboBox(self.tab_2)
        self.tab2_combo_preset.setObjectName(u"tab2_combo_preset")
        self.tab2_combo_preset.setGeometry(QRect(747, 44, 121, 32))
        self.tab2_label_preset = QLabel(self.tab_2)
        self.tab2_label_preset.setObjectName(u"tab2_label_preset")
        self.tab2_label_preset.setGeometry(QRect(750, 20, 112, 18))
        self.tab2_btn_aplicar_preset = QPushButton(self.tab_2)
        self.tab2_btn_aplicar_preset.setObjectName(u"tab2_btn_aplicar_preset")
        self.tab2_btn_aplicar_preset.setGeometry(QRect(750, 70, 111, 32))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab3_label_ubicacion = QLabel(self.tab_3)
        self.tab3_label_ubicacion.setObjectName(u"tab3_label_ubicacion")
        self.tab3_label_ubicacion.setGeometry(QRect(10, 10, 71, 16))
        self.tab3_combo_ubicacion = QComboBox(self.tab_3)
        self.tab3_combo_ubicacion.setObjectName(u"tab3_combo_ubicacion")
        self.tab3_combo_ubicacion.setGeometry(QRect(5, 30, 141, 32))
        self.tab3_btn_apply_ubicacion = QPushButton(self.tab_3)
        self.tab3_btn_apply_ubicacion.setObjectName(u"tab3_btn_apply_ubicacion")
        self.tab3_btn_apply_ubicacion.setGeometry(QRect(145, 30, 100, 32))
        self.tab3_btn_apply_tipo_barras = QPushButton(self.tab_3)
        self.tab3_btn_apply_tipo_barras.setObjectName(u"tab3_btn_apply_tipo_barras")
        self.tab3_btn_apply_tipo_barras.setGeometry(QRect(125, 90, 100, 32))
        self.tab3_combo_tipo_barras = QComboBox(self.tab_3)
        self.tab3_combo_tipo_barras.setObjectName(u"tab3_combo_tipo_barras")
        self.tab3_combo_tipo_barras.setGeometry(QRect(5, 90, 121, 32))
        self.tab3_label_tipo_barras = QLabel(self.tab_3)
        self.tab3_label_tipo_barras.setObjectName(u"tab3_label_tipo_barras")
        self.tab3_label_tipo_barras.setGeometry(QRect(50, 70, 161, 16))
        self.tab3_label_refuerzo = QLabel(self.tab_3)
        self.tab3_label_refuerzo.setObjectName(u"tab3_label_refuerzo")
        self.tab3_label_refuerzo.setGeometry(QRect(260, 10, 211, 16))
        self.tab3_line_refuerzo = QLineEdit(self.tab_3)
        self.tab3_line_refuerzo.setObjectName(u"tab3_line_refuerzo")
        self.tab3_line_refuerzo.setGeometry(QRect(310, 33, 101, 25))
        self.tab3_btn_apply_tipo_cercos = QPushButton(self.tab_3)
        self.tab3_btn_apply_tipo_cercos.setObjectName(u"tab3_btn_apply_tipo_cercos")
        self.tab3_btn_apply_tipo_cercos.setGeometry(QRect(355, 90, 100, 32))
        self.tab3_combo_tipo_cercos = QComboBox(self.tab_3)
        self.tab3_combo_tipo_cercos.setObjectName(u"tab3_combo_tipo_cercos")
        self.tab3_combo_tipo_cercos.setGeometry(QRect(235, 90, 121, 32))
        self.tab3_label_tipo_cercos = QLabel(self.tab_3)
        self.tab3_label_tipo_cercos.setObjectName(u"tab3_label_tipo_cercos")
        self.tab3_label_tipo_cercos.setGeometry(QRect(330, 70, 61, 16))
        self.tab3_btn_apply_tipo_mallas = QPushButton(self.tab_3)
        self.tab3_btn_apply_tipo_mallas.setObjectName(u"tab3_btn_apply_tipo_mallas")
        self.tab3_btn_apply_tipo_mallas.setGeometry(QRect(585, 90, 100, 32))
        self.tab3_combo_tipo_mallas = QComboBox(self.tab_3)
        self.tab3_combo_tipo_mallas.setObjectName(u"tab3_combo_tipo_mallas")
        self.tab3_combo_tipo_mallas.setGeometry(QRect(465, 90, 121, 32))
        self.tab3_label_tipo_mallas = QLabel(self.tab_3)
        self.tab3_label_tipo_mallas.setObjectName(u"tab3_label_tipo_mallas")
        self.tab3_label_tipo_mallas.setGeometry(QRect(560, 70, 61, 16))
        self.tab3_btn_add_barras = QPushButton(self.tab_3)
        self.tab3_btn_add_barras.setObjectName(u"tab3_btn_add_barras")
        self.tab3_btn_add_barras.setGeometry(QRect(10, 120, 111, 32))
        self.tab3_btn_del_barras = QPushButton(self.tab_3)
        self.tab3_btn_del_barras.setObjectName(u"tab3_btn_del_barras")
        self.tab3_btn_del_barras.setGeometry(QRect(125, 120, 100, 32))
        self.tab3_btn_add_cercos = QPushButton(self.tab_3)
        self.tab3_btn_add_cercos.setObjectName(u"tab3_btn_add_cercos")
        self.tab3_btn_add_cercos.setGeometry(QRect(240, 120, 111, 32))
        self.tab3_btn_del_cercos = QPushButton(self.tab_3)
        self.tab3_btn_del_cercos.setObjectName(u"tab3_btn_del_cercos")
        self.tab3_btn_del_cercos.setGeometry(QRect(355, 120, 100, 32))
        self.tab3_btn_add_mallas = QPushButton(self.tab_3)
        self.tab3_btn_add_mallas.setObjectName(u"tab3_btn_add_mallas")
        self.tab3_btn_add_mallas.setGeometry(QRect(470, 120, 111, 32))
        self.tab3_btn_del_mallas = QPushButton(self.tab_3)
        self.tab3_btn_del_mallas.setObjectName(u"tab3_btn_del_mallas")
        self.tab3_btn_del_mallas.setGeometry(QRect(585, 120, 100, 32))
        self.verticalLayoutWidget_2 = QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 230, 851, 241))
        self.tab3_Vlayout_barras = QVBoxLayout(self.verticalLayoutWidget_2)
        self.tab3_Vlayout_barras.setObjectName(u"tab3_Vlayout_barras")
        self.tab3_Vlayout_barras.setContentsMargins(0, 0, 0, 0)
        self.tab3_Vspacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.tab3_Vlayout_barras.addItem(self.tab3_Vspacer)

        self.tab3_label_barras = QLabel(self.tab_3)
        self.tab3_label_barras.setObjectName(u"tab3_label_barras")
        self.tab3_label_barras.setGeometry(QRect(10, 180, 161, 16))
        self.tab3_label_posicion = QLabel(self.tab_3)
        self.tab3_label_posicion.setObjectName(u"tab3_label_posicion")
        self.tab3_label_posicion.setGeometry(QRect(30, 210, 58, 16))
        self.tab3_label_uso = QLabel(self.tab_3)
        self.tab3_label_uso.setObjectName(u"tab3_label_uso")
        self.tab3_label_uso.setGeometry(QRect(150, 210, 31, 16))
        self.tab3_label_n_min = QLabel(self.tab_3)
        self.tab3_label_n_min.setObjectName(u"tab3_label_n_min")
        self.tab3_label_n_min.setGeometry(QRect(260, 210, 58, 16))
        self.tab3_label_n_max = QLabel(self.tab_3)
        self.tab3_label_n_max.setObjectName(u"tab3_label_n_max")
        self.tab3_label_n_max.setGeometry(QRect(370, 210, 58, 16))
        self.tab3_label_d_min = QLabel(self.tab_3)
        self.tab3_label_d_min.setObjectName(u"tab3_label_d_min")
        self.tab3_label_d_min.setGeometry(QRect(450, 210, 81, 16))
        self.tab3_label_d_max = QLabel(self.tab_3)
        self.tab3_label_d_max.setObjectName(u"tab3_label_d_max")
        self.tab3_label_d_max.setGeometry(QRect(560, 210, 91, 16))
        self.tab3_label_cota = QLabel(self.tab_3)
        self.tab3_label_cota.setObjectName(u"tab3_label_cota")
        self.tab3_label_cota.setGeometry(QRect(680, 210, 61, 16))
        self.tab3_label_longitud = QLabel(self.tab_3)
        self.tab3_label_longitud.setObjectName(u"tab3_label_longitud")
        self.tab3_label_longitud.setGeometry(QRect(770, 210, 91, 16))
        self.tab3_label_cercos = QLabel(self.tab_3)
        self.tab3_label_cercos.setObjectName(u"tab3_label_cercos")
        self.tab3_label_cercos.setGeometry(QRect(20, 510, 61, 16))
        self.tab3_label_mallas = QLabel(self.tab_3)
        self.tab3_label_mallas.setObjectName(u"tab3_label_mallas")
        self.tab3_label_mallas.setGeometry(QRect(20, 550, 61, 16))
        self.tab3_horizontal_line = QFrame(self.tab_3)
        self.tab3_horizontal_line.setObjectName(u"tab3_horizontal_line")
        self.tab3_horizontal_line.setGeometry(QRect(20, 490, 841, 16))
        self.tab3_horizontal_line.setFrameShape(QFrame.Shape.HLine)
        self.tab3_horizontal_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)
        self.btn_calcular_nuevos_valores.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_save_pieza.setText(QCoreApplication.translate("Dialog", u"Guardar como Pieza de Usuario", None))
        self.label_guardar_pieza.setText(QCoreApplication.translate("Dialog", u"Guardar en base de datos", None))
        self.label_name.setText(QCoreApplication.translate("Dialog", u"Num", None))
        self.label_bi.setText(QCoreApplication.translate("Dialog", u"Base_inf", None))
        self.label_bs.setText(QCoreApplication.translate("Dialog", u"Base_sup", None))
        self.label_altura.setText(QCoreApplication.translate("Dialog", u"Altura", None))
        self.label_area.setText(QCoreApplication.translate("Dialog", u"Area", None))
        self.label_cg.setText(QCoreApplication.translate("Dialog", u"Cg_Inf", None))
        self.label_inercia.setText(QCoreApplication.translate("Dialog", u"Inercia", None))
        self.label_op.setText(QCoreApplication.translate("Dialog", u"I+A*r^2", None))
        self.label_cant_agregar.setText(QCoreApplication.translate("Dialog", u"Agregar trapecios", None))
        self.btn_acpt_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar", None))
        self.label_cant_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar trapecios", None))
        self.btn_acpt_agregar.setText(QCoreApplication.translate("Dialog", u"Agregar", None))
        self.btn_calcular_nuevos_valores.setText(QCoreApplication.translate("Dialog", u"Calcular nuevos valores", None))
        self.btn_usar_pieza_catalogo.setText(QCoreApplication.translate("Dialog", u"Usar pieza catalogo", None))
        self.btn_usar_pieza_usuario.setText(QCoreApplication.translate("Dialog", u"Usar pieza usuario", None))
        self.btn_crear_pieza_temp.setText(QCoreApplication.translate("Dialog", u"Crear pieza temporal", None))
        self.label_familia.setText(QCoreApplication.translate("Dialog", u"Familia", None))
        self.label_modelo.setText(QCoreApplication.translate("Dialog", u"Modelo", None))
        self.label_tipo_seccion.setText(QCoreApplication.translate("Dialog", u"Tipo secci\u00f3n", None))
        self.btn_acpt_tipo_seccion.setText(QCoreApplication.translate("Dialog", u"Aplicar secci\u00f3n", None))
        self.btn_save_seccion.setText(QCoreApplication.translate("Dialog", u"Guardar datos secci\u00f3n", None))
        self.label_sum_altura.setText(QCoreApplication.translate("Dialog", u"Altura: ", None))
        self.label_sum_area.setText(QCoreApplication.translate("Dialog", u"Area: ", None))
        self.label_sum_ponderado.setText(QCoreApplication.translate("Dialog", u"Y Inf: ", None))
        self.label_sum_op.setText(QCoreApplication.translate("Dialog", u"Inercia: ", None))
        self.btn_salto_linea.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Tab 1", None))
        self.tab2_label_cota.setText(QCoreApplication.translate("Dialog", u"Cota (m)", None))
        self.tab2_relleno_layout_armaduras.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.tab2_btn_add_cota_custom.setText(QCoreApplication.translate("Dialog", u"Cota Custom", None))
        self.tab2_btn_add_cord.setText(QCoreApplication.translate("Dialog", u"agrega cordon", None))
        self.tab2_btn_del_cota.setText(QCoreApplication.translate("Dialog", u"Borrar Cota", None))
        self.tab2_btn_del_cord.setText(QCoreApplication.translate("Dialog", u"eliminar cordon", None))
        self.tab2_label_cant_cord.setText(QCoreApplication.translate("Dialog", u"N cordones:", None))
        self.tab2_label_cdg_area.setText(QCoreApplication.translate("Dialog", u"c.d.g area:", None))
        self.tab2_label_area_total.setText(QCoreApplication.translate("Dialog", u"Area total:", None))
        self.tab2_label_cdg_fuerza.setText(QCoreApplication.translate("Dialog", u"c.d.g fuerza:", None))
        self.tab2_btn_valores.setText(QCoreApplication.translate("Dialog", u"obtener valores", None))
        self.tab2_label_cota_dinamica.setText(QCoreApplication.translate("Dialog", u"Agregar Cotas", None))
        self.tab2_btn_add_cota_testero.setText(QCoreApplication.translate("Dialog", u"Cota Testero", None))
        self.tab2_label_cota_dinamica_2.setText(QCoreApplication.translate("Dialog", u"Tipo de Cordon", None))
        self.tab2_label_testero.setText(QCoreApplication.translate("Dialog", u"Testero", None))
        self.tab2_label_preset.setText(QCoreApplication.translate("Dialog", u"Tipo Cableado", None))
        self.tab2_btn_aplicar_preset.setText(QCoreApplication.translate("Dialog", u"Usar Cableado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Tab 2", None))
        self.tab3_label_ubicacion.setText(QCoreApplication.translate("Dialog", u"Ubicaci\u00f3n", None))
        self.tab3_btn_apply_ubicacion.setText(QCoreApplication.translate("Dialog", u"Aplicar", None))
        self.tab3_btn_apply_tipo_barras.setText(QCoreApplication.translate("Dialog", u"Aplicar", None))
        self.tab3_label_tipo_barras.setText(QCoreApplication.translate("Dialog", u"BARRAS CORRUGADAS", None))
        self.tab3_label_refuerzo.setText(QCoreApplication.translate("Dialog", u"Cota refuerzo a.pasiva inf. (m)", None))
        self.tab3_line_refuerzo.setText("")
        self.tab3_btn_apply_tipo_cercos.setText(QCoreApplication.translate("Dialog", u"Aplicar", None))
        self.tab3_label_tipo_cercos.setText(QCoreApplication.translate("Dialog", u"CERCOS", None))
        self.tab3_btn_apply_tipo_mallas.setText(QCoreApplication.translate("Dialog", u"Aplicar", None))
        self.tab3_label_tipo_mallas.setText(QCoreApplication.translate("Dialog", u"MALLAS", None))
        self.tab3_btn_add_barras.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.tab3_btn_del_barras.setText(QCoreApplication.translate("Dialog", u"Del", None))
        self.tab3_btn_add_cercos.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.tab3_btn_del_cercos.setText(QCoreApplication.translate("Dialog", u"Del", None))
        self.tab3_btn_add_mallas.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.tab3_btn_del_mallas.setText(QCoreApplication.translate("Dialog", u"Del", None))
        self.tab3_label_barras.setText(QCoreApplication.translate("Dialog", u"BARRAS CORRUGADAS", None))
        self.tab3_label_posicion.setText(QCoreApplication.translate("Dialog", u"Posici\u00f3n", None))
        self.tab3_label_uso.setText(QCoreApplication.translate("Dialog", u"Uso", None))
        self.tab3_label_n_min.setText(QCoreApplication.translate("Dialog", u"N\u00b0 Min", None))
        self.tab3_label_n_max.setText(QCoreApplication.translate("Dialog", u"N\u00b0 Max", None))
        self.tab3_label_d_min.setText(QCoreApplication.translate("Dialog", u"\u00d8 min (mm)", None))
        self.tab3_label_d_max.setText(QCoreApplication.translate("Dialog", u"\u00d8 max (mm)", None))
        self.tab3_label_cota.setText(QCoreApplication.translate("Dialog", u"Cota (m)", None))
        self.tab3_label_longitud.setText(QCoreApplication.translate("Dialog", u"Longitud (m)", None))
        self.tab3_label_cercos.setText(QCoreApplication.translate("Dialog", u"CERCOS", None))
        self.tab3_label_mallas.setText(QCoreApplication.translate("Dialog", u"MALLAS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"Arm. Pasiva", None))
    # retranslateUi

