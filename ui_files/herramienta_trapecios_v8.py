# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'herramienta_trapecios_v8.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1088, 679)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setBold(False)
        font.setItalic(False)
        Dialog.setFont(font)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 1061, 661))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.btn_save_pieza = QPushButton(self.tab)
        self.btn_save_pieza.setObjectName(u"btn_save_pieza")
        self.btn_save_pieza.setGeometry(QRect(0, 591, 221, 31))
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
        self.label_guardar_pieza.setGeometry(QRect(0, 570, 221, 21))
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
        self.verticalLayoutWidget_4.setGeometry(QRect(910, 10, 131, 116))
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
        self.gridLayoutWidget.setGeometry(QRect(290, 10, 259, 91))
        self.Glayout_edita_tuplas = QGridLayout(self.gridLayoutWidget)
        self.Glayout_edita_tuplas.setObjectName(u"Glayout_edita_tuplas")
        self.Glayout_edita_tuplas.setContentsMargins(0, 0, 0, 0)
        self.label_cant_eliminar = QLabel(self.gridLayoutWidget)
        self.label_cant_eliminar.setObjectName(u"label_cant_eliminar")

        self.Glayout_edita_tuplas.addWidget(self.label_cant_eliminar, 0, 1, 1, 1)

        self.spin_cant_agregar = QSpinBox(self.gridLayoutWidget)
        self.spin_cant_agregar.setObjectName(u"spin_cant_agregar")

        self.Glayout_edita_tuplas.addWidget(self.spin_cant_agregar, 1, 0, 1, 1)

        self.btn_acpt_eliminar = QPushButton(self.gridLayoutWidget)
        self.btn_acpt_eliminar.setObjectName(u"btn_acpt_eliminar")

        self.Glayout_edita_tuplas.addWidget(self.btn_acpt_eliminar, 2, 1, 1, 1)

        self.btn_acpt_agregar = QPushButton(self.gridLayoutWidget)
        self.btn_acpt_agregar.setObjectName(u"btn_acpt_agregar")

        self.Glayout_edita_tuplas.addWidget(self.btn_acpt_agregar, 2, 0, 1, 1)

        self.spin_cant_eliminar = QSpinBox(self.gridLayoutWidget)
        self.spin_cant_eliminar.setObjectName(u"spin_cant_eliminar")

        self.Glayout_edita_tuplas.addWidget(self.spin_cant_eliminar, 1, 1, 1, 1)

        self.label_cant_agregar = QLabel(self.gridLayoutWidget)
        self.label_cant_agregar.setObjectName(u"label_cant_agregar")

        self.Glayout_edita_tuplas.addWidget(self.label_cant_agregar, 0, 0, 1, 1)

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
        self.verticalLayoutWidget_3.setGeometry(QRect(790, 10, 121, 121))
        self.Vlayout_label_resultados = QVBoxLayout(self.verticalLayoutWidget_3)
        self.Vlayout_label_resultados.setObjectName(u"Vlayout_label_resultados")
        self.Vlayout_label_resultados.setContentsMargins(0, 0, 0, 0)
        self.label_sum_altura = QLabel(self.verticalLayoutWidget_3)
        self.label_sum_altura.setObjectName(u"label_sum_altura")

        self.Vlayout_label_resultados.addWidget(self.label_sum_altura)

        self.label_sum_area = QLabel(self.verticalLayoutWidget_3)
        self.label_sum_area.setObjectName(u"label_sum_area")

        self.Vlayout_label_resultados.addWidget(self.label_sum_area)

        self.label_sum_ponderado = QLabel(self.verticalLayoutWidget_3)
        self.label_sum_ponderado.setObjectName(u"label_sum_ponderado")

        self.Vlayout_label_resultados.addWidget(self.label_sum_ponderado)

        self.label_sum_op = QLabel(self.verticalLayoutWidget_3)
        self.label_sum_op.setObjectName(u"label_sum_op")

        self.Vlayout_label_resultados.addWidget(self.label_sum_op)

        self.btn_salto_linea = QPushButton(self.tab)
        self.btn_salto_linea.setObjectName(u"btn_salto_linea")
        self.btn_salto_linea.setGeometry(QRect(610, 20, 100, 32))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 40, 701, 351))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_3.addWidget(self.comboBox_2, 1, 0, 1, 1)

        self.lineEdit_17 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_3.addWidget(self.lineEdit_17, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 0, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_10 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_2.addWidget(self.lineEdit_10, 1, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(0)
        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_7)

        self.lineEdit_11 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.lineEdit_11)

        self.lineEdit_12 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_12)

        self.lineEdit_13 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lineEdit_13)

        self.lineEdit_14 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_14)

        self.lineEdit_15 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lineEdit_15)

        self.lineEdit_16 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_16)


        self.gridLayout.addLayout(self.formLayout_2, 1, 2, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(0)
        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_6)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lineEdit_4)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_9)


        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)
        self.btn_calcular_nuevos_valores.setDefault(True)


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
        self.label_cant_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar trapecios", None))
        self.btn_acpt_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar", None))
        self.btn_acpt_agregar.setText(QCoreApplication.translate("Dialog", u"Agregar", None))
        self.label_cant_agregar.setText(QCoreApplication.translate("Dialog", u"Agregar trapecios", None))
        self.btn_calcular_nuevos_valores.setText(QCoreApplication.translate("Dialog", u"Calcular nuevos valores", None))
        self.btn_usar_pieza_catalogo.setText(QCoreApplication.translate("Dialog", u"Usar pieza catalogo", None))
        self.btn_usar_pieza_usuario.setText(QCoreApplication.translate("Dialog", u"Usar pieza usuario", None))
        self.btn_crear_pieza_temp.setText(QCoreApplication.translate("Dialog", u"Crear pieza temporal", None))
        self.label_familia.setText(QCoreApplication.translate("Dialog", u"Familia", None))
        self.label_modelo.setText(QCoreApplication.translate("Dialog", u"Modelo", None))
        self.label_tipo_seccion.setText(QCoreApplication.translate("Dialog", u"Tipo secci\u00f3n", None))
        self.btn_acpt_tipo_seccion.setText(QCoreApplication.translate("Dialog", u"Aplicar secci\u00f3n", None))
        self.btn_save_seccion.setText(QCoreApplication.translate("Dialog", u"Guardar datos secci\u00f3n", None))
        self.label_sum_altura.setText(QCoreApplication.translate("Dialog", u"Altura", None))
        self.label_sum_area.setText(QCoreApplication.translate("Dialog", u"Area", None))
        self.label_sum_ponderado.setText(QCoreApplication.translate("Dialog", u"Y Inf", None))
        self.label_sum_op.setText(QCoreApplication.translate("Dialog", u"Inercia", None))
        self.btn_salto_linea.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Tab 1", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Area Cordon", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Tipo Cordon", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Area Cordon", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Tipo Cordon", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"N Cordones", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Tpi (N/mm2)", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"N Cordones", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Tpi (N/mm2)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Cota (m)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Tab 2", None))
    # retranslateUi

