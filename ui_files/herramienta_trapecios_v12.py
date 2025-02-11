# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'herramienta_trapecios_v12.ui'
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
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

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
        self.tab1_list_trapecios_existentes.setGeometry(QRect(410, 20, 131, 81))
        self.btn_acpt_eliminar = QPushButton(self.tab)
        self.btn_acpt_eliminar.setObjectName(u"btn_acpt_eliminar")
        self.btn_acpt_eliminar.setGeometry(QRect(270, 70, 131, 32))
        self.label_cant_eliminar = QLabel(self.tab)
        self.label_cant_eliminar.setObjectName(u"label_cant_eliminar")
        self.label_cant_eliminar.setGeometry(QRect(405, 100, 141, 22))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_cant_eliminar.setFont(font1)
        self.btn_acpt_agregar = QPushButton(self.tab)
        self.btn_acpt_agregar.setObjectName(u"btn_acpt_agregar")
        self.btn_acpt_agregar.setGeometry(QRect(270, 40, 131, 32))
        self.label_cant_agregar = QLabel(self.tab)
        self.label_cant_agregar.setObjectName(u"label_cant_agregar")
        self.label_cant_agregar.setGeometry(QRect(290, 10, 119, 31))
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_cant_agregar.setFont(font2)
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
        self.gridLayoutWidget_3.setGeometry(QRect(809, 10, 261, 147))
        self.tab2_gridLayout_totales = QGridLayout(self.gridLayoutWidget_3)
        self.tab2_gridLayout_totales.setObjectName(u"tab2_gridLayout_totales")
        self.tab2_gridLayout_totales.setContentsMargins(0, 0, 0, 0)
        self.tab2_label_cant_cord = QLabel(self.gridLayoutWidget_3)
        self.tab2_label_cant_cord.setObjectName(u"tab2_label_cant_cord")
        self.tab2_label_cant_cord.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab2_gridLayout_totales.addWidget(self.tab2_label_cant_cord, 0, 0, 1, 1)

        self.tab2_label_cdg_fuerza = QLabel(self.gridLayoutWidget_3)
        self.tab2_label_cdg_fuerza.setObjectName(u"tab2_label_cdg_fuerza")
        self.tab2_label_cdg_fuerza.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab2_gridLayout_totales.addWidget(self.tab2_label_cdg_fuerza, 3, 0, 1, 1)

        self.tab2_label_area_total = QLabel(self.gridLayoutWidget_3)
        self.tab2_label_area_total.setObjectName(u"tab2_label_area_total")
        self.tab2_label_area_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab2_gridLayout_totales.addWidget(self.tab2_label_area_total, 1, 0, 1, 1)

        self.tab2_label_cdg_area = QLabel(self.gridLayoutWidget_3)
        self.tab2_label_cdg_area.setObjectName(u"tab2_label_cdg_area")
        self.tab2_label_cdg_area.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab2_gridLayout_totales.addWidget(self.tab2_label_cdg_area, 2, 0, 1, 1)

        self.tab2_line_total_cordones = QLineEdit(self.gridLayoutWidget_3)
        self.tab2_line_total_cordones.setObjectName(u"tab2_line_total_cordones")

        self.tab2_gridLayout_totales.addWidget(self.tab2_line_total_cordones, 0, 1, 1, 1)

        self.tab2_line_total_cdg_fuerza = QLineEdit(self.gridLayoutWidget_3)
        self.tab2_line_total_cdg_fuerza.setObjectName(u"tab2_line_total_cdg_fuerza")

        self.tab2_gridLayout_totales.addWidget(self.tab2_line_total_cdg_fuerza, 3, 1, 1, 1)

        self.tab2_line_total_area = QLineEdit(self.gridLayoutWidget_3)
        self.tab2_line_total_area.setObjectName(u"tab2_line_total_area")

        self.tab2_gridLayout_totales.addWidget(self.tab2_line_total_area, 1, 1, 1, 1)

        self.tab2_line_total_cdg_area = QLineEdit(self.gridLayoutWidget_3)
        self.tab2_line_total_cdg_area.setObjectName(u"tab2_line_total_cdg_area")

        self.tab2_gridLayout_totales.addWidget(self.tab2_line_total_cdg_area, 2, 1, 1, 1)

        self.tab2_label_inercia = QLabel(self.gridLayoutWidget_3)
        self.tab2_label_inercia.setObjectName(u"tab2_label_inercia")
        self.tab2_label_inercia.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab2_gridLayout_totales.addWidget(self.tab2_label_inercia, 4, 0, 1, 1)

        self.tab2_line_total_inercia = QLineEdit(self.gridLayoutWidget_3)
        self.tab2_line_total_inercia.setObjectName(u"tab2_line_total_inercia")

        self.tab2_gridLayout_totales.addWidget(self.tab2_line_total_inercia, 4, 1, 1, 1)

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
        self.tab2_label_testero.setGeometry(QRect(460, 20, 113, 18))
        self.tab2_combo_testero = QComboBox(self.tab_2)
        self.tab2_combo_testero.setObjectName(u"tab2_combo_testero")
        self.tab2_combo_testero.setGeometry(QRect(460, 44, 141, 32))
        self.tab2_combo_preset = QComboBox(self.tab_2)
        self.tab2_combo_preset.setObjectName(u"tab2_combo_preset")
        self.tab2_combo_preset.setGeometry(QRect(597, 44, 121, 32))
        self.tab2_label_preset = QLabel(self.tab_2)
        self.tab2_label_preset.setObjectName(u"tab2_label_preset")
        self.tab2_label_preset.setGeometry(QRect(600, 20, 112, 18))
        self.tab2_btn_aplicar_preset = QPushButton(self.tab_2)
        self.tab2_btn_aplicar_preset.setObjectName(u"tab2_btn_aplicar_preset")
        self.tab2_btn_aplicar_preset.setGeometry(QRect(600, 70, 111, 32))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab3_label_ubicacion = QLabel(self.tab_3)
        self.tab3_label_ubicacion.setObjectName(u"tab3_label_ubicacion")
        self.tab3_label_ubicacion.setGeometry(QRect(10, 10, 71, 16))
        self.tab3_combo_ubicacion = QComboBox(self.tab_3)
        self.tab3_combo_ubicacion.setObjectName(u"tab3_combo_ubicacion")
        self.tab3_combo_ubicacion.setGeometry(QRect(5, 30, 181, 32))
        self.tab3_btn_apply_ubicacion = QPushButton(self.tab_3)
        self.tab3_btn_apply_ubicacion.setObjectName(u"tab3_btn_apply_ubicacion")
        self.tab3_btn_apply_ubicacion.setGeometry(QRect(190, 30, 100, 32))
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
        self.tab3_label_refuerzo.setGeometry(QRect(360, 10, 211, 16))
        self.tab3_line_refuerzo = QLineEdit(self.tab_3)
        self.tab3_line_refuerzo.setObjectName(u"tab3_line_refuerzo")
        self.tab3_line_refuerzo.setGeometry(QRect(410, 33, 101, 25))
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
        self.tab3_Vlayout_barras.setSpacing(0)
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
        self.tab3_label_uso.setGeometry(QRect(170, 210, 31, 16))
        self.tab3_label_n_min = QLabel(self.tab_3)
        self.tab3_label_n_min.setObjectName(u"tab3_label_n_min")
        self.tab3_label_n_min.setGeometry(QRect(280, 210, 58, 16))
        self.tab3_label_n_max = QLabel(self.tab_3)
        self.tab3_label_n_max.setObjectName(u"tab3_label_n_max")
        self.tab3_label_n_max.setGeometry(QRect(380, 210, 58, 16))
        self.tab3_label_d_min = QLabel(self.tab_3)
        self.tab3_label_d_min.setObjectName(u"tab3_label_d_min")
        self.tab3_label_d_min.setGeometry(QRect(465, 210, 81, 16))
        self.tab3_label_d_max = QLabel(self.tab_3)
        self.tab3_label_d_max.setObjectName(u"tab3_label_d_max")
        self.tab3_label_d_max.setGeometry(QRect(565, 210, 91, 16))
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
        self.tab3_btn_calcular = QPushButton(self.tab_3)
        self.tab3_btn_calcular.setObjectName(u"tab3_btn_calcular")
        self.tab3_btn_calcular.setGeometry(QRect(939, 10, 141, 32))
        self.tab3_label_yinf_barras = QLabel(self.tab_3)
        self.tab3_label_yinf_barras.setObjectName(u"tab3_label_yinf_barras")
        self.tab3_label_yinf_barras.setGeometry(QRect(860, 100, 101, 20))
        self.tab3_line_yinf_barras = QLineEdit(self.tab_3)
        self.tab3_line_yinf_barras.setObjectName(u"tab3_line_yinf_barras")
        self.tab3_line_yinf_barras.setGeometry(QRect(970, 100, 81, 21))
        self.tab3_label_area_barras = QLabel(self.tab_3)
        self.tab3_label_area_barras.setObjectName(u"tab3_label_area_barras")
        self.tab3_label_area_barras.setGeometry(QRect(830, 70, 131, 20))
        self.tab3_line_area_barras = QLineEdit(self.tab_3)
        self.tab3_line_area_barras.setObjectName(u"tab3_line_area_barras")
        self.tab3_line_area_barras.setGeometry(QRect(970, 70, 81, 21))
        self.tab3_line_inercia_barras = QLineEdit(self.tab_3)
        self.tab3_line_inercia_barras.setObjectName(u"tab3_line_inercia_barras")
        self.tab3_line_inercia_barras.setGeometry(QRect(970, 130, 81, 21))
        self.tab3_label_inercia_barras = QLabel(self.tab_3)
        self.tab3_label_inercia_barras.setObjectName(u"tab3_label_inercia_barras")
        self.tab3_label_inercia_barras.setGeometry(QRect(830, 130, 141, 20))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab4_label_caracteristicas_horm = QLabel(self.tab_4)
        self.tab4_label_caracteristicas_horm.setObjectName(u"tab4_label_caracteristicas_horm")
        self.tab4_label_caracteristicas_horm.setGeometry(QRect(10, 10, 221, 31))
        self.tab4_label_caracteristicas_horm.setFont(font2)
        self.gridLayoutWidget = QWidget(self.tab_4)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 70, 303, 151))
        self.tab4_gridLayout_fc = QGridLayout(self.gridLayoutWidget)
        self.tab4_gridLayout_fc.setObjectName(u"tab4_gridLayout_fc")
        self.tab4_gridLayout_fc.setContentsMargins(0, 0, 0, 0)
        self.tab4_grid_horm_relleno = QLabel(self.gridLayoutWidget)
        self.tab4_grid_horm_relleno.setObjectName(u"tab4_grid_horm_relleno")

        self.tab4_gridLayout_fc.addWidget(self.tab4_grid_horm_relleno, 0, 0, 1, 1)

        self.tab4_label_horm_final = QLabel(self.gridLayoutWidget)
        self.tab4_label_horm_final.setObjectName(u"tab4_label_horm_final")
        self.tab4_label_horm_final.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab4_gridLayout_fc.addWidget(self.tab4_label_horm_final, 3, 0, 1, 1)

        self.tab4_label_grid_e = QLabel(self.gridLayoutWidget)
        self.tab4_label_grid_e.setObjectName(u"tab4_label_grid_e")
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setItalic(False)
        self.tab4_label_grid_e.setFont(font3)

        self.tab4_gridLayout_fc.addWidget(self.tab4_label_grid_e, 0, 2, 1, 1)

        self.tab4_label_horm_min = QLabel(self.gridLayoutWidget)
        self.tab4_label_horm_min.setObjectName(u"tab4_label_horm_min")
        self.tab4_label_horm_min.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab4_gridLayout_fc.addWidget(self.tab4_label_horm_min, 1, 0, 1, 1)

        self.tab4_label_horm_max = QLabel(self.gridLayoutWidget)
        self.tab4_label_horm_max.setObjectName(u"tab4_label_horm_max")
        self.tab4_label_horm_max.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab4_gridLayout_fc.addWidget(self.tab4_label_horm_max, 2, 0, 1, 1)

        self.tab4_label_grid_fc = QLabel(self.gridLayoutWidget)
        self.tab4_label_grid_fc.setObjectName(u"tab4_label_grid_fc")
        self.tab4_label_grid_fc.setFont(font3)

        self.tab4_gridLayout_fc.addWidget(self.tab4_label_grid_fc, 0, 1, 1, 1)

        self.tab4_label_horm_insitu = QLabel(self.gridLayoutWidget)
        self.tab4_label_horm_insitu.setObjectName(u"tab4_label_horm_insitu")
        self.tab4_label_horm_insitu.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab4_gridLayout_fc.addWidget(self.tab4_label_horm_insitu, 4, 0, 1, 1)

        self.tab4_line_horm_min_fc = QLineEdit(self.gridLayoutWidget)
        self.tab4_line_horm_min_fc.setObjectName(u"tab4_line_horm_min_fc")
        self.tab4_line_horm_min_fc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_fc.addWidget(self.tab4_line_horm_min_fc, 1, 1, 1, 1)

        self.tab4_line_horm_min_e = QLineEdit(self.gridLayoutWidget)
        self.tab4_line_horm_min_e.setObjectName(u"tab4_line_horm_min_e")
        self.tab4_line_horm_min_e.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tab4_line_horm_min_e.setReadOnly(True)

        self.tab4_gridLayout_fc.addWidget(self.tab4_line_horm_min_e, 1, 2, 1, 1)

        self.tab4_line_horm_max_fc = QLineEdit(self.gridLayoutWidget)
        self.tab4_line_horm_max_fc.setObjectName(u"tab4_line_horm_max_fc")
        self.tab4_line_horm_max_fc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_fc.addWidget(self.tab4_line_horm_max_fc, 2, 1, 1, 1)

        self.tab4_line_horm_max_e = QLineEdit(self.gridLayoutWidget)
        self.tab4_line_horm_max_e.setObjectName(u"tab4_line_horm_max_e")
        self.tab4_line_horm_max_e.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tab4_line_horm_max_e.setReadOnly(True)

        self.tab4_gridLayout_fc.addWidget(self.tab4_line_horm_max_e, 2, 2, 1, 1)

        self.tab4_line_horm_final_fc = QLineEdit(self.gridLayoutWidget)
        self.tab4_line_horm_final_fc.setObjectName(u"tab4_line_horm_final_fc")
        self.tab4_line_horm_final_fc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_fc.addWidget(self.tab4_line_horm_final_fc, 3, 1, 1, 1)

        self.tab4_line_horm_final_e = QLineEdit(self.gridLayoutWidget)
        self.tab4_line_horm_final_e.setObjectName(u"tab4_line_horm_final_e")
        self.tab4_line_horm_final_e.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tab4_line_horm_final_e.setReadOnly(True)

        self.tab4_gridLayout_fc.addWidget(self.tab4_line_horm_final_e, 3, 2, 1, 1)

        self.tab4_line_horm_insitu_fc = QLineEdit(self.gridLayoutWidget)
        self.tab4_line_horm_insitu_fc.setObjectName(u"tab4_line_horm_insitu_fc")
        self.tab4_line_horm_insitu_fc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_fc.addWidget(self.tab4_line_horm_insitu_fc, 4, 1, 1, 1)

        self.tab4_line_horm_insitu_e = QLineEdit(self.gridLayoutWidget)
        self.tab4_line_horm_insitu_e.setObjectName(u"tab4_line_horm_insitu_e")
        self.tab4_line_horm_insitu_e.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tab4_line_horm_insitu_e.setReadOnly(True)

        self.tab4_gridLayout_fc.addWidget(self.tab4_line_horm_insitu_e, 4, 2, 1, 1)

        self.horizontalLayoutWidget_2 = QWidget(self.tab_4)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 40, 311, 32))
        self.tab4_horizontalLayout_tipo_hormigon = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.tab4_horizontalLayout_tipo_hormigon.setObjectName(u"tab4_horizontalLayout_tipo_hormigon")
        self.tab4_horizontalLayout_tipo_hormigon.setContentsMargins(0, 0, 0, 0)
        self.tab4_label_tipo_horm = QLabel(self.horizontalLayoutWidget_2)
        self.tab4_label_tipo_horm.setObjectName(u"tab4_label_tipo_horm")
        self.tab4_label_tipo_horm.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab4_horizontalLayout_tipo_hormigon.addWidget(self.tab4_label_tipo_horm)

        self.tab4_combo_tipo_horm = QComboBox(self.horizontalLayoutWidget_2)
        self.tab4_combo_tipo_horm.setObjectName(u"tab4_combo_tipo_horm")
        self.tab4_combo_tipo_horm.setMinimumSize(QSize(0, 0))

        self.tab4_horizontalLayout_tipo_hormigon.addWidget(self.tab4_combo_tipo_horm)

        self.tab4_horizontalLayout_tipo_hormigon.setStretch(0, 1)
        self.tab4_horizontalLayout_tipo_hormigon.setStretch(1, 2)
        self.gridLayoutWidget_4 = QWidget(self.tab_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(350, 40, 271, 113))
        self.tab4_gridLayout_densidades = QGridLayout(self.gridLayoutWidget_4)
        self.tab4_gridLayout_densidades.setObjectName(u"tab4_gridLayout_densidades")
        self.tab4_gridLayout_densidades.setContentsMargins(0, 0, 0, 0)
        self.tab4_label_temporal2 = QLabel(self.gridLayoutWidget_4)
        self.tab4_label_temporal2.setObjectName(u"tab4_label_temporal2")

        self.tab4_gridLayout_densidades.addWidget(self.tab4_label_temporal2, 0, 1, 1, 1)

        self.tab4_label_dens_horm = QLabel(self.gridLayoutWidget_4)
        self.tab4_label_dens_horm.setObjectName(u"tab4_label_dens_horm")

        self.tab4_gridLayout_densidades.addWidget(self.tab4_label_dens_horm, 1, 0, 1, 1)

        self.tab4_line_dens_horm = QLineEdit(self.gridLayoutWidget_4)
        self.tab4_line_dens_horm.setObjectName(u"tab4_line_dens_horm")

        self.tab4_gridLayout_densidades.addWidget(self.tab4_line_dens_horm, 1, 1, 1, 1)

        self.tab4_label_wc = QLabel(self.gridLayoutWidget_4)
        self.tab4_label_wc.setObjectName(u"tab4_label_wc")
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(16)
        font4.setBold(False)
        font4.setItalic(False)
        self.tab4_label_wc.setFont(font4)

        self.tab4_gridLayout_densidades.addWidget(self.tab4_label_wc, 0, 0, 1, 1)

        self.tab4_label_dens_acero = QLabel(self.gridLayoutWidget_4)
        self.tab4_label_dens_acero.setObjectName(u"tab4_label_dens_acero")

        self.tab4_gridLayout_densidades.addWidget(self.tab4_label_dens_acero, 2, 0, 1, 1)

        self.tab4_line_dens_acero = QLineEdit(self.gridLayoutWidget_4)
        self.tab4_line_dens_acero.setObjectName(u"tab4_line_dens_acero")

        self.tab4_gridLayout_densidades.addWidget(self.tab4_line_dens_acero, 2, 1, 1, 1)

        self.tab4_label_dens_concreto = QLabel(self.gridLayoutWidget_4)
        self.tab4_label_dens_concreto.setObjectName(u"tab4_label_dens_concreto")

        self.tab4_gridLayout_densidades.addWidget(self.tab4_label_dens_concreto, 3, 0, 1, 1)

        self.tab4_line_dens_concreto = QLineEdit(self.gridLayoutWidget_4)
        self.tab4_line_dens_concreto.setObjectName(u"tab4_line_dens_concreto")

        self.tab4_gridLayout_densidades.addWidget(self.tab4_line_dens_concreto, 3, 1, 1, 1)

        self.tab4_btn_guardar_valores = QPushButton(self.tab_4)
        self.tab4_btn_guardar_valores.setObjectName(u"tab4_btn_guardar_valores")
        self.tab4_btn_guardar_valores.setGeometry(QRect(360, 190, 211, 32))
        self.tab4_instrucciones1 = QLabel(self.tab_4)
        self.tab4_instrucciones1.setObjectName(u"tab4_instrucciones1")
        self.tab4_instrucciones1.setGeometry(QRect(770, 20, 311, 20))
        font5 = QFont()
        font5.setFamilies([u"Verdana"])
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        self.tab4_instrucciones1.setFont(font5)
        self.tab4_instrucciones2 = QLabel(self.tab_4)
        self.tab4_instrucciones2.setObjectName(u"tab4_instrucciones2")
        self.tab4_instrucciones2.setGeometry(QRect(770, 70, 311, 51))
        self.tab4_instrucciones2.setFont(font5)
        self.tab4_instrucciones2.setWordWrap(True)
        self.tab4_instrucciones3 = QLabel(self.tab_4)
        self.tab4_instrucciones3.setObjectName(u"tab4_instrucciones3")
        self.tab4_instrucciones3.setGeometry(QRect(770, 120, 231, 51))
        self.tab4_instrucciones3.setFont(font5)
        self.tab4_instrucciones3.setWordWrap(True)
        self.tab4_instrucciones4 = QLabel(self.tab_4)
        self.tab4_instrucciones4.setObjectName(u"tab4_instrucciones4")
        self.tab4_instrucciones4.setGeometry(QRect(770, 170, 221, 71))
        self.tab4_instrucciones4.setWordWrap(True)
        self.gridLayoutWidget_6 = QWidget(self.tab_4)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(20, 530, 551, 94))
        self.tab4_gridLayout_info = QGridLayout(self.gridLayoutWidget_6)
        self.tab4_gridLayout_info.setObjectName(u"tab4_gridLayout_info")
        self.tab4_gridLayout_info.setContentsMargins(0, 0, 0, 0)
        self.tab4_label_tipo_3 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_tipo_3.setObjectName(u"tab4_label_tipo_3")
        self.tab4_label_tipo_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_tipo_3, 2, 0, 1, 1)

        self.tab4_label_tpi_1 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_tpi_1.setObjectName(u"tab4_label_tpi_1")
        self.tab4_label_tpi_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_tpi_1, 0, 4, 1, 1)

        self.tab4_label_tipo_1 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_tipo_1.setObjectName(u"tab4_label_tipo_1")
        self.tab4_label_tipo_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_tipo_1, 0, 0, 1, 1)

        self.tab4_label_acero_1 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_acero_1.setObjectName(u"tab4_label_acero_1")
        self.tab4_label_acero_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_acero_1, 0, 2, 1, 1)

        self.tab4_label_tipo_2 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_tipo_2.setObjectName(u"tab4_label_tipo_2")
        self.tab4_label_tipo_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_tipo_2, 1, 0, 1, 1)

        self.tab4_label_pulgada_1 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_pulgada_1.setObjectName(u"tab4_label_pulgada_1")
        self.tab4_label_pulgada_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_pulgada_1, 0, 1, 1, 1)

        self.tab4_label_area_1 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_area_1.setObjectName(u"tab4_label_area_1")
        self.tab4_label_area_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_area_1, 0, 3, 1, 1)

        self.tab4_label_tipo_4 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_tipo_4.setObjectName(u"tab4_label_tipo_4")
        self.tab4_label_tipo_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_tipo_4, 3, 0, 1, 1)

        self.tab4_label_pulgada_2 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_pulgada_2.setObjectName(u"tab4_label_pulgada_2")
        self.tab4_label_pulgada_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_pulgada_2, 1, 1, 1, 1)

        self.tab4_label_pulgada_3 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_pulgada_3.setObjectName(u"tab4_label_pulgada_3")
        self.tab4_label_pulgada_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_pulgada_3, 2, 1, 1, 1)

        self.tab4_label_pulgada_4 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_pulgada_4.setObjectName(u"tab4_label_pulgada_4")
        self.tab4_label_pulgada_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_pulgada_4, 3, 1, 1, 1)

        self.tab4_label_acero_2 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_acero_2.setObjectName(u"tab4_label_acero_2")
        self.tab4_label_acero_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_acero_2, 1, 2, 1, 1)

        self.tab4_label_acero_3 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_acero_3.setObjectName(u"tab4_label_acero_3")
        self.tab4_label_acero_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_acero_3, 2, 2, 1, 1)

        self.tab4_label_acero_4 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_acero_4.setObjectName(u"tab4_label_acero_4")
        self.tab4_label_acero_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_acero_4, 3, 2, 1, 1)

        self.tab4_label_tpi_2 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_tpi_2.setObjectName(u"tab4_label_tpi_2")
        self.tab4_label_tpi_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_tpi_2, 1, 4, 1, 1)

        self.tab4_label_tpi_3 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_tpi_3.setObjectName(u"tab4_label_tpi_3")
        self.tab4_label_tpi_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_tpi_3, 2, 4, 1, 1)

        self.tab4_label_tpi_4 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_tpi_4.setObjectName(u"tab4_label_tpi_4")
        self.tab4_label_tpi_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_tpi_4, 3, 4, 1, 1)

        self.tab4_label_area_2 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_area_2.setObjectName(u"tab4_label_area_2")
        self.tab4_label_area_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_area_2, 1, 3, 1, 1)

        self.tab4_label_area_3 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_area_3.setObjectName(u"tab4_label_area_3")
        self.tab4_label_area_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_area_3, 2, 3, 1, 1)

        self.tab4_label_area_4 = QLabel(self.gridLayoutWidget_6)
        self.tab4_label_area_4.setObjectName(u"tab4_label_area_4")
        self.tab4_label_area_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab4_gridLayout_info.addWidget(self.tab4_label_area_4, 3, 3, 1, 1)

        self.tab4_label_title_tipo = QLabel(self.tab_4)
        self.tab4_label_title_tipo.setObjectName(u"tab4_label_title_tipo")
        self.tab4_label_title_tipo.setGeometry(QRect(40, 510, 41, 16))
        self.tab4_label_title_tipo.setFont(font2)
        self.tab4_label_title_pulgada = QLabel(self.tab_4)
        self.tab4_label_title_pulgada.setObjectName(u"tab4_label_title_pulgada")
        self.tab4_label_title_pulgada.setGeometry(QRect(120, 510, 91, 16))
        self.tab4_label_title_pulgada.setFont(font2)
        self.tab4_label_title_acero = QLabel(self.tab_4)
        self.tab4_label_title_acero.setObjectName(u"tab4_label_title_acero")
        self.tab4_label_title_acero.setGeometry(QRect(240, 510, 91, 16))
        self.tab4_label_title_acero.setFont(font2)
        self.tab4_label_title_area = QLabel(self.tab_4)
        self.tab4_label_title_area.setObjectName(u"tab4_label_title_area")
        self.tab4_label_title_area.setGeometry(QRect(350, 510, 91, 16))
        self.tab4_label_title_area.setFont(font2)
        self.tab4_label_title_tpi = QLabel(self.tab_4)
        self.tab4_label_title_tpi.setObjectName(u"tab4_label_title_tpi")
        self.tab4_label_title_tpi.setGeometry(QRect(470, 510, 101, 16))
        self.tab4_label_title_tpi.setFont(font2)
        self.tab4_separador_tabla = QFrame(self.tab_4)
        self.tab4_separador_tabla.setObjectName(u"tab4_separador_tabla")
        self.tab4_separador_tabla.setGeometry(QRect(20, 520, 561, 16))
        self.tab4_separador_tabla.setFrameShape(QFrame.Shape.HLine)
        self.tab4_separador_tabla.setFrameShadow(QFrame.Shadow.Sunken)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tab5_line_temp1 = QLineEdit(self.tab_5)
        self.tab5_line_temp1.setObjectName(u"tab5_line_temp1")
        self.tab5_line_temp1.setGeometry(QRect(940, 540, 113, 21))
        self.tab5_label_temp1 = QLabel(self.tab_5)
        self.tab5_label_temp1.setObjectName(u"tab5_label_temp1")
        self.tab5_label_temp1.setGeometry(QRect(880, 510, 181, 16))
        self.tab5_label_temp2 = QLabel(self.tab_5)
        self.tab5_label_temp2.setObjectName(u"tab5_label_temp2")
        self.tab5_label_temp2.setGeometry(QRect(870, 540, 71, 16))
        self.tab5_label_temp3 = QLabel(self.tab_5)
        self.tab5_label_temp3.setObjectName(u"tab5_label_temp3")
        self.tab5_label_temp3.setGeometry(QRect(880, 580, 61, 16))
        self.tab5_line_temp2 = QLineEdit(self.tab_5)
        self.tab5_line_temp2.setObjectName(u"tab5_line_temp2")
        self.tab5_line_temp2.setGeometry(QRect(940, 580, 113, 21))
        self.tab5_horizontal_line_temp = QFrame(self.tab_5)
        self.tab5_horizontal_line_temp.setObjectName(u"tab5_horizontal_line_temp")
        self.tab5_horizontal_line_temp.setGeometry(QRect(940, 560, 111, 20))
        self.tab5_horizontal_line_temp.setFrameShape(QFrame.Shape.HLine)
        self.tab5_horizontal_line_temp.setFrameShadow(QFrame.Shadow.Sunken)
        self.tab5_titulo_caracteristicas = QLabel(self.tab_5)
        self.tab5_titulo_caracteristicas.setObjectName(u"tab5_titulo_caracteristicas")
        self.tab5_titulo_caracteristicas.setGeometry(QRect(70, 20, 321, 41))
        font6 = QFont()
        font6.setFamilies([u"Verdana"])
        font6.setPointSize(17)
        font6.setBold(False)
        font6.setItalic(False)
        self.tab5_titulo_caracteristicas.setFont(font6)
        self.gridLayoutWidget_5 = QWidget(self.tab_5)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(30, 70, 361, 109))
        self.tab5_gridLayout_caracteristicas = QGridLayout(self.gridLayoutWidget_5)
#ifndef Q_OS_MAC
        self.tab5_gridLayout_caracteristicas.setSpacing(-1)
#endif
        self.tab5_gridLayout_caracteristicas.setObjectName(u"tab5_gridLayout_caracteristicas")
        self.tab5_gridLayout_caracteristicas.setContentsMargins(0, 0, 0, 0)
        self.tab5_label_relleno_grid = QLabel(self.gridLayoutWidget_5)
        self.tab5_label_relleno_grid.setObjectName(u"tab5_label_relleno_grid")
        self.tab5_label_relleno_grid.setEnabled(False)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_label_relleno_grid, 0, 0, 1, 1)

        self.tab5_label_simple_t0 = QLabel(self.gridLayoutWidget_5)
        self.tab5_label_simple_t0.setObjectName(u"tab5_label_simple_t0")
        self.tab5_label_simple_t0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_label_simple_t0, 0, 2, 1, 1)

        self.tab5_label_cdg = QLabel(self.gridLayoutWidget_5)
        self.tab5_label_cdg.setObjectName(u"tab5_label_cdg")
        self.tab5_label_cdg.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_label_cdg, 2, 0, 1, 1)

        self.tab5_label_area = QLabel(self.gridLayoutWidget_5)
        self.tab5_label_area.setObjectName(u"tab5_label_area")
        self.tab5_label_area.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_label_area, 1, 0, 1, 1)

        self.tab5_label_inercia = QLabel(self.gridLayoutWidget_5)
        self.tab5_label_inercia.setObjectName(u"tab5_label_inercia")
        self.tab5_label_inercia.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_label_inercia, 3, 0, 1, 1)

        self.tab5_label_bruta = QLabel(self.gridLayoutWidget_5)
        self.tab5_label_bruta.setObjectName(u"tab5_label_bruta")
        self.tab5_label_bruta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_label_bruta, 0, 1, 1, 1)

        self.tab5_label_simple_t00 = QLabel(self.gridLayoutWidget_5)
        self.tab5_label_simple_t00.setObjectName(u"tab5_label_simple_t00")
        self.tab5_label_simple_t00.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_label_simple_t00, 0, 3, 1, 1)

        self.tab5_line_area_bruta = QLineEdit(self.gridLayoutWidget_5)
        self.tab5_line_area_bruta.setObjectName(u"tab5_line_area_bruta")
        self.tab5_line_area_bruta.setMaximumSize(QSize(100, 16777215))
        self.tab5_line_area_bruta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_line_area_bruta, 1, 1, 1, 1)

        self.tab5_line_area_t0 = QLineEdit(self.gridLayoutWidget_5)
        self.tab5_line_area_t0.setObjectName(u"tab5_line_area_t0")
        self.tab5_line_area_t0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_line_area_t0, 1, 2, 1, 1)

        self.tab5_line_area_t00 = QLineEdit(self.gridLayoutWidget_5)
        self.tab5_line_area_t00.setObjectName(u"tab5_line_area_t00")
        self.tab5_line_area_t00.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_line_area_t00, 1, 3, 1, 1)

        self.tab5_line_cdg_bruta = QLineEdit(self.gridLayoutWidget_5)
        self.tab5_line_cdg_bruta.setObjectName(u"tab5_line_cdg_bruta")
        self.tab5_line_cdg_bruta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_line_cdg_bruta, 2, 1, 1, 1)

        self.tab5_line_cdg_t0 = QLineEdit(self.gridLayoutWidget_5)
        self.tab5_line_cdg_t0.setObjectName(u"tab5_line_cdg_t0")
        self.tab5_line_cdg_t0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_line_cdg_t0, 2, 2, 1, 1)

        self.tab5_line_cdg_t00 = QLineEdit(self.gridLayoutWidget_5)
        self.tab5_line_cdg_t00.setObjectName(u"tab5_line_cdg_t00")
        self.tab5_line_cdg_t00.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_line_cdg_t00, 2, 3, 1, 1)

        self.tab5_line_inercia_bruta = QLineEdit(self.gridLayoutWidget_5)
        self.tab5_line_inercia_bruta.setObjectName(u"tab5_line_inercia_bruta")
        self.tab5_line_inercia_bruta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_line_inercia_bruta, 3, 1, 1, 1)

        self.tab5_line_inercia_t0 = QLineEdit(self.gridLayoutWidget_5)
        self.tab5_line_inercia_t0.setObjectName(u"tab5_line_inercia_t0")
        self.tab5_line_inercia_t0.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_line_inercia_t0, 3, 2, 1, 1)

        self.tab5_line_inercia_t00 = QLineEdit(self.gridLayoutWidget_5)
        self.tab5_line_inercia_t00.setObjectName(u"tab5_line_inercia_t00")
        self.tab5_line_inercia_t00.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tab5_gridLayout_caracteristicas.addWidget(self.tab5_line_inercia_t00, 3, 3, 1, 1)

        self.tab5_btn_calcular = QPushButton(self.tab_5)
        self.tab5_btn_calcular.setObjectName(u"tab5_btn_calcular")
        self.tab5_btn_calcular.setGeometry(QRect(889, 20, 171, 32))
        self.tabWidget.addTab(self.tab_5, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(1)
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
        self.btn_acpt_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar Selecci\u00f3n", None))
        self.label_cant_eliminar.setText(QCoreApplication.translate("Dialog", u"*Elegir trapecio a eliminar", None))
        self.btn_acpt_agregar.setText(QCoreApplication.translate("Dialog", u"Agregar Trapecio", None))
        self.label_cant_agregar.setText(QCoreApplication.translate("Dialog", u"TRAPECIOS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Geometr\u00eda", None))
        self.tab2_label_cota.setText(QCoreApplication.translate("Dialog", u"Cota (m)", None))
        self.tab2_relleno_layout_armaduras.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.tab2_btn_add_cota_custom.setText(QCoreApplication.translate("Dialog", u"Cota Custom", None))
        self.tab2_btn_add_cord.setText(QCoreApplication.translate("Dialog", u"agrega cordon", None))
        self.tab2_btn_del_cota.setText(QCoreApplication.translate("Dialog", u"Borrar Cota", None))
        self.tab2_btn_del_cord.setText(QCoreApplication.translate("Dialog", u"eliminar cordon", None))
        self.tab2_label_cant_cord.setText(QCoreApplication.translate("Dialog", u"N cordones:", None))
        self.tab2_label_cdg_fuerza.setText(QCoreApplication.translate("Dialog", u"c.d.g fuerza[m]:", None))
        self.tab2_label_area_total.setText(QCoreApplication.translate("Dialog", u"Area total [cm2]:", None))
        self.tab2_label_cdg_area.setText(QCoreApplication.translate("Dialog", u"c.d.g area[m]:", None))
        self.tab2_label_inercia.setText(QCoreApplication.translate("Dialog", u"Inercia (cdg Area) [m4]", None))
        self.tab2_btn_valores.setText(QCoreApplication.translate("Dialog", u"obtener valores", None))
        self.tab2_label_cota_dinamica.setText(QCoreApplication.translate("Dialog", u"Agregar Cotas", None))
        self.tab2_btn_add_cota_testero.setText(QCoreApplication.translate("Dialog", u"Cota Testero", None))
        self.tab2_label_cota_dinamica_2.setText(QCoreApplication.translate("Dialog", u"Tipo de Cordon", None))
        self.tab2_label_testero.setText(QCoreApplication.translate("Dialog", u"Testero", None))
        self.tab2_label_preset.setText(QCoreApplication.translate("Dialog", u"Tipo Cableado", None))
        self.tab2_btn_aplicar_preset.setText(QCoreApplication.translate("Dialog", u"Usar Cableado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Arm. Activa", None))
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
        self.tab3_btn_calcular.setText(QCoreApplication.translate("Dialog", u"Agregar a calculo", None))
        self.tab3_label_yinf_barras.setText(QCoreApplication.translate("Dialog", u"Yinf Barras[m]:", None))
        self.tab3_label_area_barras.setText(QCoreApplication.translate("Dialog", u"Area Barras [mm2]:", None))
        self.tab3_label_inercia_barras.setText(QCoreApplication.translate("Dialog", u"Inercia Barras [m4]:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"Arm. Pasiva", None))
        self.tab4_label_caracteristicas_horm.setText(QCoreApplication.translate("Dialog", u"Caracter\u00edsticas del Hormig\u00f3n", None))
        self.tab4_grid_horm_relleno.setText("")
        self.tab4_label_horm_final.setText(QCoreApplication.translate("Dialog", u"Hor.Pref. Final", None))
        self.tab4_label_grid_e.setText(QCoreApplication.translate("Dialog", u"E(N/mm2)", None))
        self.tab4_label_horm_min.setText(QCoreApplication.translate("Dialog", u"Hor.Pref.Inic.(min)", None))
        self.tab4_label_horm_max.setText(QCoreApplication.translate("Dialog", u"Hor.Pref.inic.(max)", None))
        self.tab4_label_grid_fc.setText(QCoreApplication.translate("Dialog", u"f'c(N/mm2)", None))
        self.tab4_label_horm_insitu.setText(QCoreApplication.translate("Dialog", u"Hor.In-Situ", None))
        self.tab4_line_horm_min_e.setText("")
        self.tab4_label_tipo_horm.setText(QCoreApplication.translate("Dialog", u"Tipo Hormig\u00f3n", None))
        self.tab4_label_temporal2.setText("")
        self.tab4_label_dens_horm.setText(QCoreApplication.translate("Dialog", u"Dens. Horm.(kN/m3)", None))
        self.tab4_line_dens_horm.setText("")
        self.tab4_label_wc.setText("")
        self.tab4_label_dens_acero.setText(QCoreApplication.translate("Dialog", u"Dens. Acero(kN/m3)", None))
        self.tab4_label_dens_concreto.setText(QCoreApplication.translate("Dialog", u"Dens. Concreto(kg/m3) [wc]", None))
        self.tab4_btn_guardar_valores.setText(QCoreApplication.translate("Dialog", u"Calcular con Wc", None))
        self.tab4_instrucciones1.setText(QCoreApplication.translate("Dialog", u"*Dens. Concreto [wc] por defecto = 2400 (kg/m3)", None))
        self.tab4_instrucciones2.setText(QCoreApplication.translate("Dialog", u"Al seleccionar tipo de hormi\u00f3n en lista superior se asignan automaticamete valores para f'c ; Ec ; densidades en los campos.", None))
        self.tab4_instrucciones3.setText(QCoreApplication.translate("Dialog", u"Estos valores usan formula JACENA de Ec = 4700 * raiz(f'c).", None))
        self.tab4_instrucciones4.setText(QCoreApplication.translate("Dialog", u"Para usar resultados de formula Ec = Wc^1.5 * 0.043 * raiz(f'c). >>Usar boton \"Calcular con Wc\"", None))
        self.tab4_label_tipo_3.setText(QCoreApplication.translate("Dialog", u"\u00d8 12.70 mm", None))
        self.tab4_label_tpi_1.setText(QCoreApplication.translate("Dialog", u"1230", None))
        self.tab4_label_tipo_1.setText(QCoreApplication.translate("Dialog", u"\u00d8 4.98 mm", None))
        self.tab4_label_acero_1.setText(QCoreApplication.translate("Dialog", u"ASTM-421", None))
        self.tab4_label_tipo_2.setText(QCoreApplication.translate("Dialog", u"\u00d8 9.3mm", None))
        self.tab4_label_pulgada_1.setText(QCoreApplication.translate("Dialog", u"------", None))
        self.tab4_label_area_1.setText(QCoreApplication.translate("Dialog", u"0.195", None))
        self.tab4_label_tipo_4.setText(QCoreApplication.translate("Dialog", u"\u00d8 15.24mm", None))
        self.tab4_label_pulgada_2.setText(QCoreApplication.translate("Dialog", u"3/8''", None))
        self.tab4_label_pulgada_3.setText(QCoreApplication.translate("Dialog", u"1/2''", None))
        self.tab4_label_pulgada_4.setText(QCoreApplication.translate("Dialog", u"0.6''", None))
        self.tab4_label_acero_2.setText(QCoreApplication.translate("Dialog", u"ASTM-416", None))
        self.tab4_label_acero_3.setText(QCoreApplication.translate("Dialog", u"ASTM-416", None))
        self.tab4_label_acero_4.setText(QCoreApplication.translate("Dialog", u"ASTM-416", None))
        self.tab4_label_tpi_2.setText(QCoreApplication.translate("Dialog", u"1400", None))
        self.tab4_label_tpi_3.setText(QCoreApplication.translate("Dialog", u"1400", None))
        self.tab4_label_tpi_4.setText(QCoreApplication.translate("Dialog", u"1400", None))
        self.tab4_label_area_2.setText(QCoreApplication.translate("Dialog", u"0.432", None))
        self.tab4_label_area_3.setText(QCoreApplication.translate("Dialog", u"0.775", None))
        self.tab4_label_area_4.setText(QCoreApplication.translate("Dialog", u"1.102", None))
        self.tab4_label_title_tipo.setText(QCoreApplication.translate("Dialog", u"Tipo", None))
        self.tab4_label_title_pulgada.setText(QCoreApplication.translate("Dialog", u"Eq. Pulgada", None))
        self.tab4_label_title_acero.setText(QCoreApplication.translate("Dialog", u"Tipo Acero", None))
        self.tab4_label_title_area.setText(QCoreApplication.translate("Dialog", u"\u00c1rea (cm2)", None))
        self.tab4_label_title_tpi.setText(QCoreApplication.translate("Dialog", u"Tpi (N/mm2)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"Materiales", None))
        self.tab5_label_temp1.setText(QCoreApplication.translate("Dialog", u"Ingresar datos esfuerzo", None))
        self.tab5_label_temp2.setText(QCoreApplication.translate("Dialog", u"Momento:", None))
        self.tab5_label_temp3.setText(QCoreApplication.translate("Dialog", u"Modulo:", None))
        self.tab5_titulo_caracteristicas.setText(QCoreApplication.translate("Dialog", u"Caracter\u00edsticas mec\u00e1nicas secci\u00f3n", None))
        self.tab5_label_relleno_grid.setText("")
        self.tab5_label_simple_t0.setText(QCoreApplication.translate("Dialog", u"Simple t=0", None))
        self.tab5_label_cdg.setText(QCoreApplication.translate("Dialog", u"Yinf", None))
        self.tab5_label_area.setText(QCoreApplication.translate("Dialog", u"Area", None))
        self.tab5_label_inercia.setText(QCoreApplication.translate("Dialog", u"Inercia", None))
        self.tab5_label_bruta.setText(QCoreApplication.translate("Dialog", u"Bruta t=0", None))
        self.tab5_label_simple_t00.setText(QCoreApplication.translate("Dialog", u"Simple t=00", None))
        self.tab5_line_area_bruta.setText("")
        self.tab5_btn_calcular.setText(QCoreApplication.translate("Dialog", u"Calcular caracter\u00edsticas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Dialog", u"Calc. Parcial", None))
    # retranslateUi

