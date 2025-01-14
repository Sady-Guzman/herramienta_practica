# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'herramienta_trapecios_v6.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1070, 631)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setBold(False)
        font.setItalic(False)
        Dialog.setFont(font)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 211, 318))
        self.Vlayout_catalogo = QVBoxLayout(self.verticalLayoutWidget)
        self.Vlayout_catalogo.setObjectName(u"Vlayout_catalogo")
        self.Vlayout_catalogo.setContentsMargins(0, 0, 0, 0)
        self.btn_acpt_pieza = QPushButton(self.verticalLayoutWidget)
        self.btn_acpt_pieza.setObjectName(u"btn_acpt_pieza")

        self.Vlayout_catalogo.addWidget(self.btn_acpt_pieza)

        self.btn_acpt_pieza_2 = QPushButton(self.verticalLayoutWidget)
        self.btn_acpt_pieza_2.setObjectName(u"btn_acpt_pieza_2")

        self.Vlayout_catalogo.addWidget(self.btn_acpt_pieza_2)

        self.btn_crear_pieza_temp = QPushButton(self.verticalLayoutWidget)
        self.btn_crear_pieza_temp.setObjectName(u"btn_crear_pieza_temp")

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

        self.combo_tipo_seccion = QComboBox(self.verticalLayoutWidget)
        self.combo_tipo_seccion.setObjectName(u"combo_tipo_seccion")

        self.Vlayout_catalogo.addWidget(self.combo_tipo_seccion)

        self.btn_acpt_tipo_seccion = QPushButton(self.verticalLayoutWidget)
        self.btn_acpt_tipo_seccion.setObjectName(u"btn_acpt_tipo_seccion")

        self.Vlayout_catalogo.addWidget(self.btn_acpt_tipo_seccion)

        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(300, 210, 751, 31))
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

        self.verticalLayoutWidget_3 = QWidget(Dialog)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(800, 10, 121, 121))
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

        self.verticalLayoutWidget_4 = QWidget(Dialog)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(920, 10, 131, 116))
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

        self.verticalLayoutWidget_5 = QWidget(Dialog)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(300, 240, 751, 351))
        self.layout_nuevas_row = QVBoxLayout(self.verticalLayoutWidget_5)
        self.layout_nuevas_row.setObjectName(u"layout_nuevas_row")
        self.layout_nuevas_row.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_nuevas_row.addItem(self.verticalSpacer)

        self.gridLayoutWidget = QWidget(Dialog)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(300, 10, 259, 91))
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

        self.btn_calcular_nuevos_valores = QPushButton(Dialog)
        self.btn_calcular_nuevos_valores.setObjectName(u"btn_calcular_nuevos_valores")
        self.btn_calcular_nuevos_valores.setGeometry(QRect(300, 180, 171, 32))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_acpt_pieza.setText(QCoreApplication.translate("Dialog", u"Usar pieza catalogo", None))
        self.btn_acpt_pieza_2.setText(QCoreApplication.translate("Dialog", u"Usar pieza usuario", None))
        self.btn_crear_pieza_temp.setText(QCoreApplication.translate("Dialog", u"Crear pieza temporal", None))
        self.label_familia.setText(QCoreApplication.translate("Dialog", u"Familia", None))
        self.label_modelo.setText(QCoreApplication.translate("Dialog", u"Modelo", None))
        self.label_tipo_seccion.setText(QCoreApplication.translate("Dialog", u"Tipo secci\u00f3n", None))
        self.btn_acpt_tipo_seccion.setText(QCoreApplication.translate("Dialog", u"Cambiar secci\u00f3n", None))
        self.label_name.setText(QCoreApplication.translate("Dialog", u"Num", None))
        self.label_bi.setText(QCoreApplication.translate("Dialog", u"Base_inf", None))
        self.label_bs.setText(QCoreApplication.translate("Dialog", u"Base_sup", None))
        self.label_altura.setText(QCoreApplication.translate("Dialog", u"Altura", None))
        self.label_area.setText(QCoreApplication.translate("Dialog", u"Area", None))
        self.label_cg.setText(QCoreApplication.translate("Dialog", u"Cg_Sup", None))
        self.label_inercia.setText(QCoreApplication.translate("Dialog", u"Inercia", None))
        self.label_op.setText(QCoreApplication.translate("Dialog", u"I+A*r^2", None))
        self.label_sum_altura.setText(QCoreApplication.translate("Dialog", u"Sum Altura", None))
        self.label_sum_area.setText(QCoreApplication.translate("Dialog", u"Sum Area", None))
        self.label_sum_ponderado.setText(QCoreApplication.translate("Dialog", u"Sum Ponderado", None))
        self.label_sum_op.setText(QCoreApplication.translate("Dialog", u"Sum I+A*r^2", None))
        self.label_cant_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar secciones", None))
        self.btn_acpt_eliminar.setText(QCoreApplication.translate("Dialog", u"Eliminar", None))
        self.btn_acpt_agregar.setText(QCoreApplication.translate("Dialog", u"Agregar", None))
        self.label_cant_agregar.setText(QCoreApplication.translate("Dialog", u"Agregar secciones", None))
        self.btn_calcular_nuevos_valores.setText(QCoreApplication.translate("Dialog", u"Calcular nuevos valores", None))
    # retranslateUi

