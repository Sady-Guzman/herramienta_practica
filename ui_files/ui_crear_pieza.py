# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crear_pieza.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(536, 336)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setBold(False)
        font.setItalic(False)
        Dialog.setFont(font)
        self.verticalLayoutWidget_5 = QWidget(Dialog)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(20, 130, 221, 191))
        self.layout_nuevas_row = QVBoxLayout(self.verticalLayoutWidget_5)
        self.layout_nuevas_row.setObjectName(u"layout_nuevas_row")
        self.layout_nuevas_row.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layout_nuevas_row.addItem(self.verticalSpacer)

        self.btn_aceptar = QPushButton(Dialog)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setGeometry(QRect(390, 290, 131, 32))
        self.btn_aceptar.setAutoDefault(False)
        self.label_titulo = QLabel(Dialog)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(20, 10, 181, 16))
        self.gridLayoutWidget_3 = QWidget(Dialog)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(20, 40, 501, 60))
        self.gridLayout_datos = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_datos.setObjectName(u"gridLayout_datos")
        self.gridLayout_datos.setContentsMargins(0, 0, 0, 0)
        self.label_familia = QLabel(self.gridLayoutWidget_3)
        self.label_familia.setObjectName(u"label_familia")

        self.gridLayout_datos.addWidget(self.label_familia, 1, 0, 1, 1)

        self.lineEdit_modelo = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_modelo.setObjectName(u"lineEdit_modelo")

        self.gridLayout_datos.addWidget(self.lineEdit_modelo, 1, 3, 1, 1)

        self.label_modelo = QLabel(self.gridLayoutWidget_3)
        self.label_modelo.setObjectName(u"label_modelo")

        self.gridLayout_datos.addWidget(self.label_modelo, 1, 2, 1, 1)

        self.label_cant_agregar = QLabel(self.gridLayoutWidget_3)
        self.label_cant_agregar.setObjectName(u"label_cant_agregar")

        self.gridLayout_datos.addWidget(self.label_cant_agregar, 0, 4, 1, 1)

        self.lineEdit_familia = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_familia.setObjectName(u"lineEdit_familia")

        self.gridLayout_datos.addWidget(self.lineEdit_familia, 1, 1, 1, 1)

        self.layout_btns_secciones = QHBoxLayout()
        self.layout_btns_secciones.setObjectName(u"layout_btns_secciones")
        self.btn_agregar_seccion = QPushButton(self.gridLayoutWidget_3)
        self.btn_agregar_seccion.setObjectName(u"btn_agregar_seccion")

        self.layout_btns_secciones.addWidget(self.btn_agregar_seccion)

        self.btn_eliminar_seccion = QPushButton(self.gridLayoutWidget_3)
        self.btn_eliminar_seccion.setObjectName(u"btn_eliminar_seccion")

        self.layout_btns_secciones.addWidget(self.btn_eliminar_seccion)


        self.gridLayout_datos.addLayout(self.layout_btns_secciones, 1, 4, 1, 1)

        self.label_nombre_secciones = QLabel(Dialog)
        self.label_nombre_secciones.setObjectName(u"label_nombre_secciones")
        self.label_nombre_secciones.setGeometry(QRect(20, 100, 219, 29))
        self.btn_cancelar = QPushButton(Dialog)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setGeometry(QRect(280, 290, 100, 32))

        self.retranslateUi(Dialog)

        self.btn_aceptar.setDefault(True)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_aceptar.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.label_titulo.setText(QCoreApplication.translate("Dialog", u"Ingresar datos nueva pieza", None))
        self.label_familia.setText(QCoreApplication.translate("Dialog", u"Familia:", None))
        self.lineEdit_modelo.setText("")
        self.label_modelo.setText(QCoreApplication.translate("Dialog", u"Modelo:", None))
        self.label_cant_agregar.setText(QCoreApplication.translate("Dialog", u"Cantidad de secciones", None))
        self.lineEdit_familia.setText("")
        self.btn_agregar_seccion.setText(QCoreApplication.translate("Dialog", u"Agregar", None))
        self.btn_eliminar_seccion.setText(QCoreApplication.translate("Dialog", u"Eliminar", None))
        self.label_nombre_secciones.setText(QCoreApplication.translate("Dialog", u"Nombre para secciones", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
    # retranslateUi

