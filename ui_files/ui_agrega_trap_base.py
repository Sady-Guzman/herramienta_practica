# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agrega_trapecios.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")


        Dialog.resize(1065, 776)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setBold(False)
        font.setItalic(False)
        Dialog.setFont(font)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 201, 125))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_familia = QLabel(self.verticalLayoutWidget)
        self.label_familia.setObjectName(u"label_familia")

        self.verticalLayout_2.addWidget(self.label_familia)

        self.combo_familia = QComboBox(self.verticalLayoutWidget)
        self.combo_familia.addItem("")
        self.combo_familia.addItem("")
        self.combo_familia.addItem("")
        self.combo_familia.setObjectName(u"combo_familia")

        self.verticalLayout_2.addWidget(self.combo_familia)

        self.label_modelo = QLabel(self.verticalLayoutWidget)
        self.label_modelo.setObjectName(u"label_modelo")

        self.verticalLayout_2.addWidget(self.label_modelo)

        self.combo_modelo = QComboBox(self.verticalLayoutWidget)
        self.combo_modelo.addItem("")
        self.combo_modelo.addItem("")
        self.combo_modelo.addItem("")
        self.combo_modelo.setObjectName(u"combo_modelo")

        self.verticalLayout_2.addWidget(self.combo_modelo)

        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(250, 10, 161, 121))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_cant = QLabel(self.verticalLayoutWidget_2)
        self.label_cant.setObjectName(u"label_cant")

        self.verticalLayout_3.addWidget(self.label_cant)

        self.spin_cant = QSpinBox(self.verticalLayoutWidget_2)
        self.spin_cant.setObjectName(u"spin_cant")

        self.verticalLayout_3.addWidget(self.spin_cant)

        self.btn_acpt_cant = QPushButton(self.verticalLayoutWidget_2)
        self.btn_acpt_cant.setObjectName(u"btn_acpt_cant")

        self.verticalLayout_3.addWidget(self.btn_acpt_cant)

        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 180, 751, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_name = QLabel(self.horizontalLayoutWidget)
        self.label_name.setObjectName(u"label_name")

        self.horizontalLayout.addWidget(self.label_name)

        self.label_bi = QLabel(self.horizontalLayoutWidget)
        self.label_bi.setObjectName(u"label_bi")

        self.horizontalLayout.addWidget(self.label_bi)

        self.label_bs = QLabel(self.horizontalLayoutWidget)
        self.label_bs.setObjectName(u"label_bs")

        self.horizontalLayout.addWidget(self.label_bs)

        self.label_altura = QLabel(self.horizontalLayoutWidget)
        self.label_altura.setObjectName(u"label_altura")

        self.horizontalLayout.addWidget(self.label_altura)

        self.label_area = QLabel(self.horizontalLayoutWidget)
        self.label_area.setObjectName(u"label_area")

        self.horizontalLayout.addWidget(self.label_area)

        self.label_cg = QLabel(self.horizontalLayoutWidget)
        self.label_cg.setObjectName(u"label_cg")

        self.horizontalLayout.addWidget(self.label_cg)

        self.label_inercia = QLabel(self.horizontalLayoutWidget)
        self.label_inercia.setObjectName(u"label_inercia")

        self.horizontalLayout.addWidget(self.label_inercia)

        self.label_op = QLabel(self.horizontalLayoutWidget)
        self.label_op.setObjectName(u"label_op")

        self.horizontalLayout.addWidget(self.label_op)

        self.horizontalLayoutWidget_2 = QWidget(Dialog)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 210, 751, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.t1_name = QLabel(self.horizontalLayoutWidget_2)
        self.t1_name.setObjectName(u"t1_name")

        self.horizontalLayout_2.addWidget(self.t1_name)

        self.t1_bi = QLineEdit(self.horizontalLayoutWidget_2)
        self.t1_bi.setObjectName(u"t1_bi")

        self.horizontalLayout_2.addWidget(self.t1_bi)

        self.t1_bs = QLineEdit(self.horizontalLayoutWidget_2)
        self.t1_bs.setObjectName(u"t1_bs")

        self.horizontalLayout_2.addWidget(self.t1_bs)

        self.t1_altura = QLineEdit(self.horizontalLayoutWidget_2)
        self.t1_altura.setObjectName(u"t1_altura")

        self.horizontalLayout_2.addWidget(self.t1_altura)

        self.t1_area = QLineEdit(self.horizontalLayoutWidget_2)
        self.t1_area.setObjectName(u"t1_area")

        self.horizontalLayout_2.addWidget(self.t1_area)

        self.t1_cg = QLineEdit(self.horizontalLayoutWidget_2)
        self.t1_cg.setObjectName(u"t1_cg")

        self.horizontalLayout_2.addWidget(self.t1_cg)

        self.t1_inercia = QLineEdit(self.horizontalLayoutWidget_2)
        self.t1_inercia.setObjectName(u"t1_inercia")

        self.horizontalLayout_2.addWidget(self.t1_inercia)

        self.t1_op = QLineEdit(self.horizontalLayoutWidget_2)
        self.t1_op.setObjectName(u"t1_op")

        self.horizontalLayout_2.addWidget(self.t1_op)

        self.verticalLayoutWidget_3 = QWidget(Dialog)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(800, 180, 121, 121))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_sum_altura = QLabel(self.verticalLayoutWidget_3)
        self.label_sum_altura.setObjectName(u"label_sum_altura")

        self.verticalLayout_4.addWidget(self.label_sum_altura)

        self.label_sum_area = QLabel(self.verticalLayoutWidget_3)
        self.label_sum_area.setObjectName(u"label_sum_area")

        self.verticalLayout_4.addWidget(self.label_sum_area)

        self.label_sum_ponderado = QLabel(self.verticalLayoutWidget_3)
        self.label_sum_ponderado.setObjectName(u"label_sum_ponderado")

        self.verticalLayout_4.addWidget(self.label_sum_ponderado)

        self.label_sum_op = QLabel(self.verticalLayoutWidget_3)
        self.label_sum_op.setObjectName(u"label_sum_op")

        self.verticalLayout_4.addWidget(self.label_sum_op)

        self.verticalLayoutWidget_4 = QWidget(Dialog)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(920, 180, 131, 116))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.result_sum_altura = QLineEdit(self.verticalLayoutWidget_4)
        self.result_sum_altura.setObjectName(u"result_sum_altura")
        self.result_sum_altura.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.result_sum_altura)

        self.result_sum_area = QLineEdit(self.verticalLayoutWidget_4)
        self.result_sum_area.setObjectName(u"result_sum_area")
        self.result_sum_area.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.result_sum_area)

        self.result_sum_ponderado = QLineEdit(self.verticalLayoutWidget_4)
        self.result_sum_ponderado.setObjectName(u"result_sum_ponderado")
        self.result_sum_ponderado.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.result_sum_ponderado)

        self.result_sum_op = QLineEdit(self.verticalLayoutWidget_4)
        self.result_sum_op.setObjectName(u"result_sum_op")
        self.result_sum_op.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.result_sum_op)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_familia.setText(QCoreApplication.translate("Dialog", u"Familia", None))
        self.combo_familia.setItemText(0, QCoreApplication.translate("Dialog", u"Elegir", None))
        self.combo_familia.setItemText(1, QCoreApplication.translate("Dialog", u"VI", None))
        self.combo_familia.setItemText(2, QCoreApplication.translate("Dialog", u"VF", None))

        self.label_modelo.setText(QCoreApplication.translate("Dialog", u"Modelo", None))
        self.combo_modelo.setItemText(0, QCoreApplication.translate("Dialog", u"Elegir", None))
        self.combo_modelo.setItemText(1, QCoreApplication.translate("Dialog", u"4120", None))
        self.combo_modelo.setItemText(2, QCoreApplication.translate("Dialog", u"9kjahsd", None))

        self.label_cant.setText(QCoreApplication.translate("Dialog", u"n* Secciones", None))
        self.btn_acpt_cant.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.label_name.setText(QCoreApplication.translate("Dialog", u"Num", None))
        self.label_bi.setText(QCoreApplication.translate("Dialog", u"Base_inf", None))
        self.label_bs.setText(QCoreApplication.translate("Dialog", u"Base_sup", None))
        self.label_altura.setText(QCoreApplication.translate("Dialog", u"Altura", None))
        self.label_area.setText(QCoreApplication.translate("Dialog", u"Area", None))
        self.label_cg.setText(QCoreApplication.translate("Dialog", u"Cg_Sup", None))
        self.label_inercia.setText(QCoreApplication.translate("Dialog", u"I(nercia?)", None))
        self.label_op.setText(QCoreApplication.translate("Dialog", u"I+A*r^2", None))
        self.t1_name.setText(QCoreApplication.translate("Dialog", u"T1              ", None))
        self.label_sum_altura.setText(QCoreApplication.translate("Dialog", u"Sum Altura", None))
        self.label_sum_area.setText(QCoreApplication.translate("Dialog", u"Sum Area", None))
        self.label_sum_ponderado.setText(QCoreApplication.translate("Dialog", u"Sum Ponderado", None))
        self.label_sum_op.setText(QCoreApplication.translate("Dialog", u"Sum I+A*r^2", None))
    # retranslateUi

