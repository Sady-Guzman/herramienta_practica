# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora_trapecios2.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

from PySide6.QtWidgets import QVBoxLayout

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog  # Make sure Dialog is passed into the setupUi method
        self.mainLayout = QVBoxLayout(self.Dialog)  # Or any other layout type you need

        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(932, 616)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(760, 560, 161, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.combo_familia = QComboBox(Dialog)
        self.combo_familia.addItem("")
        self.combo_familia.addItem("")
        self.combo_familia.setObjectName(u"combo_familia")
        self.combo_familia.setGeometry(QRect(20, 40, 103, 32))
        self.combo_modelo = QComboBox(Dialog)
        self.combo_modelo.addItem("")
        self.combo_modelo.addItem("")
        self.combo_modelo.addItem("")
        self.combo_modelo.setObjectName(u"combo_modelo")
        self.combo_modelo.setGeometry(QRect(120, 40, 103, 32))
        self.label_familia = QLabel(Dialog)
        self.label_familia.setObjectName(u"label_familia")
        self.label_familia.setGeometry(QRect(30, 20, 58, 16))
        self.label_modelo = QLabel(Dialog)
        self.label_modelo.setObjectName(u"label_modelo")
        self.label_modelo.setGeometry(QRect(130, 20, 58, 16))
        self.label_trapecios = QLabel(Dialog)
        self.label_trapecios.setObjectName(u"label_trapecios")
        self.label_trapecios.setGeometry(QRect(20, 100, 58, 16))
        self.label_secciones = QLabel(Dialog)
        self.label_secciones.setObjectName(u"label_secciones")
        self.label_secciones.setGeometry(QRect(20, 130, 21, 16))
        self.label_bi = QLabel(Dialog)
        self.label_bi.setObjectName(u"label_bi")
        self.label_bi.setGeometry(QRect(60, 130, 58, 16))
        self.label_bs = QLabel(Dialog)
        self.label_bs.setObjectName(u"label_bs")
        self.label_bs.setGeometry(QRect(130, 130, 58, 16))
        self.label_h = QLabel(Dialog)
        self.label_h.setObjectName(u"label_h")
        self.label_h.setGeometry(QRect(200, 130, 58, 16))
        self.label_d = QLabel(Dialog)
        self.label_d.setObjectName(u"label_d")
        self.label_d.setGeometry(QRect(270, 130, 58, 16))
        self.label_a = QLabel(Dialog)
        self.label_a.setObjectName(u"label_a")
        self.label_a.setGeometry(QRect(340, 130, 31, 16))
        self.label_cg = QLabel(Dialog)
        self.label_cg.setObjectName(u"label_cg")
        self.label_cg.setGeometry(QRect(410, 130, 58, 16))
        self.label_i = QLabel(Dialog)
        self.label_i.setObjectName(u"label_i")
        self.label_i.setGeometry(QRect(480, 130, 21, 16))
        self.label_op = QLabel(Dialog)
        self.label_op.setObjectName(u"label_op")
        self.label_op.setGeometry(QRect(550, 130, 71, 16))
        self.label_cant = QLabel(Dialog)
        self.label_cant.setObjectName(u"label_cant")
        self.label_cant.setGeometry(QRect(270, 20, 101, 16))
        self.spin_cant = QSpinBox(Dialog)
        self.spin_cant.setObjectName(u"spin_cant")
        self.spin_cant.setGeometry(QRect(270, 40, 91, 31))
        self.btn_acpt_cant = QPushButton(Dialog)
        self.btn_acpt_cant.setObjectName(u"btn_acpt_cant")
        self.btn_acpt_cant.setGeometry(QRect(380, 40, 100, 32))
        self.sum_frame = QFrame(Dialog)
        self.sum_frame.setObjectName(u"sum_frame")
        self.sum_frame.setGeometry(QRect(20, 550, 581, 51))
        self.sum_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sum_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.sum_op = QLineEdit(self.sum_frame)
        self.sum_op.setObjectName(u"sum_op")
        self.sum_op.setGeometry(QRect(530, 0, 51, 21))
        self.sumprod_a_cg = QLineEdit(self.sum_frame)
        self.sumprod_a_cg.setObjectName(u"sumprod_a_cg")
        self.sumprod_a_cg.setGeometry(QRect(390, 0, 51, 21))
        self.label_sumprod = QLabel(self.sum_frame)
        self.label_sumprod.setObjectName(u"label_sumprod")
        self.label_sumprod.setGeometry(QRect(380, 30, 81, 16))
        self.label_sum = QLabel(self.sum_frame)
        self.label_sum.setObjectName(u"label_sum")
        self.label_sum.setGeometry(QRect(0, 0, 31, 16))
        self.sum_a = QLineEdit(self.sum_frame)
        self.sum_a.setObjectName(u"sum_a")
        self.sum_a.setGeometry(QRect(320, 0, 51, 21))
        self.sum_h = QLineEdit(self.sum_frame)
        self.sum_h.setObjectName(u"sum_h")
        self.sum_h.setGeometry(QRect(180, 0, 51, 21))
        self.t_frame1 = QFrame(Dialog)
        self.t_frame1.setObjectName(u"t_frame1")
        self.t_frame1.setGeometry(QRect(20, 160, 591, 41))
        self.t_frame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.t_frame1.setFrameShadow(QFrame.Shadow.Raised)
        self.t1_op = QLineEdit(self.t_frame1)
        self.t1_op.setObjectName(u"t1_op")
        self.t1_op.setGeometry(QRect(530, 10, 51, 21))
        self.t1_bs = QLineEdit(self.t_frame1)
        self.t1_bs.setObjectName(u"t1_bs")
        self.t1_bs.setGeometry(QRect(110, 10, 51, 21))
        self.t1_a = QLineEdit(self.t_frame1)
        self.t1_a.setObjectName(u"t1_a")
        self.t1_a.setGeometry(QRect(320, 10, 51, 21))
        self.t_name1 = QLabel(self.t_frame1)
        self.t_name1.setObjectName(u"t_name1")
        self.t_name1.setGeometry(QRect(0, 10, 31, 16))
        self.t1_cg = QLineEdit(self.t_frame1)
        self.t1_cg.setObjectName(u"t1_cg")
        self.t1_cg.setGeometry(QRect(390, 10, 51, 21))
        self.t1_h = QLineEdit(self.t_frame1)
        self.t1_h.setObjectName(u"t1_h")
        self.t1_h.setGeometry(QRect(180, 10, 51, 21))
        self.t1_bi = QLineEdit(self.t_frame1)
        self.t1_bi.setObjectName(u"t1_bi")
        self.t1_bi.setGeometry(QRect(40, 10, 51, 21))
        self.t1_i = QLineEdit(self.t_frame1)
        self.t1_i.setObjectName(u"t1_i")
        self.t1_i.setGeometry(QRect(460, 10, 51, 21))
        self.t1_d = QLineEdit(self.t_frame1)
        self.t1_d.setObjectName(u"t1_d")
        self.t1_d.setGeometry(QRect(250, 10, 51, 21))
        self.t_frame2 = QFrame(Dialog)
        self.t_frame2.setObjectName(u"t_frame2")
        self.t_frame2.setGeometry(QRect(20, 210, 591, 41))
        self.t_frame2.setFrameShape(QFrame.Shape.StyledPanel)
        self.t_frame2.setFrameShadow(QFrame.Shadow.Raised)
        self.t2_op = QLineEdit(self.t_frame2)
        self.t2_op.setObjectName(u"t2_op")
        self.t2_op.setGeometry(QRect(530, 10, 51, 21))
        self.t2_bs = QLineEdit(self.t_frame2)
        self.t2_bs.setObjectName(u"t2_bs")
        self.t2_bs.setGeometry(QRect(110, 10, 51, 21))
        self.t2_a = QLineEdit(self.t_frame2)
        self.t2_a.setObjectName(u"t2_a")
        self.t2_a.setGeometry(QRect(320, 10, 51, 21))
        self.t_name2 = QLabel(self.t_frame2)
        self.t_name2.setObjectName(u"t_name2")
        self.t_name2.setGeometry(QRect(0, 10, 31, 16))
        self.t2_cg = QLineEdit(self.t_frame2)
        self.t2_cg.setObjectName(u"t2_cg")
        self.t2_cg.setGeometry(QRect(390, 10, 51, 21))
        self.t2_h = QLineEdit(self.t_frame2)
        self.t2_h.setObjectName(u"t2_h")
        self.t2_h.setGeometry(QRect(180, 10, 51, 21))
        self.t2_bi = QLineEdit(self.t_frame2)
        self.t2_bi.setObjectName(u"t2_bi")
        self.t2_bi.setGeometry(QRect(40, 10, 51, 21))
        self.t2_i = QLineEdit(self.t_frame2)
        self.t2_i.setObjectName(u"t2_i")
        self.t2_i.setGeometry(QRect(460, 10, 51, 21))
        self.t2_d = QLineEdit(self.t_frame2)
        self.t2_d.setObjectName(u"t2_d")
        self.t2_d.setGeometry(QRect(250, 10, 51, 21))
        self.t_frame3 = QFrame(Dialog)
        self.t_frame3.setObjectName(u"t_frame3")
        self.t_frame3.setGeometry(QRect(20, 270, 591, 41))
        self.t_frame3.setFrameShape(QFrame.Shape.StyledPanel)
        self.t_frame3.setFrameShadow(QFrame.Shadow.Raised)
        self.t3_op = QLineEdit(self.t_frame3)
        self.t3_op.setObjectName(u"t3_op")
        self.t3_op.setGeometry(QRect(530, 10, 51, 21))
        self.t3_bs = QLineEdit(self.t_frame3)
        self.t3_bs.setObjectName(u"t3_bs")
        self.t3_bs.setGeometry(QRect(110, 10, 51, 21))
        self.t3_a = QLineEdit(self.t_frame3)
        self.t3_a.setObjectName(u"t3_a")
        self.t3_a.setGeometry(QRect(320, 10, 51, 21))
        self.t_name3 = QLabel(self.t_frame3)
        self.t_name3.setObjectName(u"t_name3")
        self.t_name3.setGeometry(QRect(0, 10, 31, 16))
        self.t3_cg = QLineEdit(self.t_frame3)
        self.t3_cg.setObjectName(u"t3_cg")
        self.t3_cg.setGeometry(QRect(390, 10, 51, 21))
        self.t3_h = QLineEdit(self.t_frame3)
        self.t3_h.setObjectName(u"t3_h")
        self.t3_h.setGeometry(QRect(180, 10, 51, 21))
        self.t3_bi = QLineEdit(self.t_frame3)
        self.t3_bi.setObjectName(u"t3_bi")
        self.t3_bi.setGeometry(QRect(40, 10, 51, 21))
        self.t3_i = QLineEdit(self.t_frame3)
        self.t3_i.setObjectName(u"t3_i")
        self.t3_i.setGeometry(QRect(460, 10, 51, 21))
        self.t3_d = QLineEdit(self.t_frame3)
        self.t3_d.setObjectName(u"t3_d")
        self.t3_d.setGeometry(QRect(250, 10, 51, 21))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

        # Connect the button to the method
        self.btn_acpt_cant.clicked.connect(self.generate_frames)
        
        # HARD CODED recordatorio
        # Keep track of the last Y position for the frames
        self.last_frame_y = 270  # This is where t_frame3 ends

    # setupUi



    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.combo_familia.setItemText(0, QCoreApplication.translate("Dialog", u"elegir", None))
        self.combo_familia.setItemText(1, QCoreApplication.translate("Dialog", u"VI", None))

        self.combo_familia.setPlaceholderText(QCoreApplication.translate("Dialog", u"Elegir", None))
        self.combo_modelo.setItemText(0, QCoreApplication.translate("Dialog", u"Elegir", None))
        self.combo_modelo.setItemText(1, QCoreApplication.translate("Dialog", u"asd", None))
        self.combo_modelo.setItemText(2, QCoreApplication.translate("Dialog", u"4120", None))

        self.combo_modelo.setPlaceholderText(QCoreApplication.translate("Dialog", u"Elegir", None))
        self.label_familia.setText(QCoreApplication.translate("Dialog", u"Familia", None))
        self.label_modelo.setText(QCoreApplication.translate("Dialog", u"Modelo", None))
        self.label_trapecios.setText(QCoreApplication.translate("Dialog", u"Trapecios", None))
        self.label_secciones.setText(QCoreApplication.translate("Dialog", u"S", None))
        self.label_bi.setText(QCoreApplication.translate("Dialog", u"b_i", None))
        self.label_bs.setText(QCoreApplication.translate("Dialog", u"b_s", None))
        self.label_h.setText(QCoreApplication.translate("Dialog", u"altura", None))
        self.label_d.setText(QCoreApplication.translate("Dialog", u"diagonal", None))
        self.label_a.setText(QCoreApplication.translate("Dialog", u"A", None))
        self.label_cg.setText(QCoreApplication.translate("Dialog", u"Cg Sup", None))
        self.label_i.setText(QCoreApplication.translate("Dialog", u"I", None))
        self.label_op.setText(QCoreApplication.translate("Dialog", u"I + A*r^2", None))
        self.label_cant.setText(QCoreApplication.translate("Dialog", u"n* Trapecios", None))
        self.btn_acpt_cant.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
        self.label_sumprod.setText(QCoreApplication.translate("Dialog", u"SumProduc", None))
        self.label_sum.setText(QCoreApplication.translate("Dialog", u"SUM", None))
        self.t_name1.setText(QCoreApplication.translate("Dialog", u"T1", None))
        self.t_name2.setText(QCoreApplication.translate("Dialog", u"T2", None))
        self.t_name3.setText(QCoreApplication.translate("Dialog", u"T3", None))
    # retranslateUi

    def generate_frames(self):
        # Get the number of frames to generate from the spinbox
        num_frames = self.spin_cant.value()
        print("spin_acpt_cant val: ", num_frames) #debug
        
        # Loop to create the frames
        for i in range(num_frames):
            self.create_frame(i + 4)  # Start from t_frame4, t_frame5, etc.

    # def create_frame(self, frame_num):
    #     # Create a new frame below the last one
    #     new_frame = QFrame(self.Dialog)
    #     new_frame.setObjectName(f"t_frame{frame_num}")
    #     new_frame.setGeometry(QRect(20, self.last_frame_y + 50, 591, 41))
    #     new_frame.setFrameShape(QFrame.Shape.StyledPanel)
    #     new_frame.setFrameShadow(QFrame.Shadow.Raised)

    #     # Add the components inside the frame (just like in t_frame1)
    #     label_name = QLabel(f"T{frame_num}", new_frame)
    #     label_name.setGeometry(QRect(0, 10, 31, 16))
        
    #     input_op = QLineEdit(new_frame)
    #     input_op.setObjectName(f"t{frame_num}_op")
    #     input_op.setGeometry(QRect(530, 10, 51, 21))

    #     input_bs = QLineEdit(new_frame)
    #     input_bs.setObjectName(f"t{frame_num}_bs")
    #     input_bs.setGeometry(QRect(110, 10, 51, 21))

    #     input_a = QLineEdit(new_frame)
    #     input_a.setObjectName(f"t{frame_num}_a")
    #     input_a.setGeometry(QRect(320, 10, 51, 21))

    #     input_cg = QLineEdit(new_frame)
    #     input_cg.setObjectName(f"t{frame_num}_cg")
    #     input_cg.setGeometry(QRect(390, 10, 51, 21))

    #     input_h = QLineEdit(new_frame)
    #     input_h.setObjectName(f"t{frame_num}_h")
    #     input_h.setGeometry(QRect(180, 10, 51, 21))

    #     input_bi = QLineEdit(new_frame)
    #     input_bi.setObjectName(f"t{frame_num}_bi")
    #     input_bi.setGeometry(QRect(40, 10, 51, 21))

    #     input_i = QLineEdit(new_frame)
    #     input_i.setObjectName(f"t{frame_num}_i")
    #     input_i.setGeometry(QRect(460, 10, 51, 21))

    #     input_d = QLineEdit(new_frame)
    #     input_d.setObjectName(f"t{frame_num}_d")
    #     input_d.setGeometry(QRect(250, 10, 51, 21))

    #     # Update the last frame's Y-position
    #     self.last_frame_y += 50  # Increase by the height of the frame (41px) + some spacing

    def create_frame(self, frame_num):

        print(f"Creating frame {frame_num}")

        # Create a new frame below the last one
        new_frame = QFrame(self.Dialog)
        new_frame.setObjectName(f"t_frame{frame_num}")
        new_frame.setGeometry(QRect(20, self.last_frame_y + 50, 591, 41))
        new_frame.setFrameShape(QFrame.Shape.StyledPanel)
        new_frame.setFrameShadow(QFrame.Shadow.Raised)

        # Add components to the frame
        label_name = QLabel(f"T{frame_num}", new_frame)
        label_name.setGeometry(QRect(0, 10, 31, 16))
        self.mainLayout.addWidget(label_name) # bloquea interaccion
        # self.Dialog.repaint()
        # self.Dialog.update()

        input_op = QLineEdit(new_frame)
        input_op.setObjectName(f"t{frame_num}_op")
        input_op.setGeometry(QRect(530, 10, 51, 21))

        input_bs = QLineEdit(new_frame)
        input_bs.setObjectName(f"t{frame_num}_bs")
        input_bs.setGeometry(QRect(110, 10, 51, 21))

        input_a = QLineEdit(new_frame)
        input_a.setObjectName(f"t{frame_num}_a")
        input_a.setGeometry(QRect(320, 10, 51, 21))

        input_cg = QLineEdit(new_frame)
        input_cg.setObjectName(f"t{frame_num}_cg")
        input_cg.setGeometry(QRect(390, 10, 51, 21))

        input_h = QLineEdit(new_frame)
        input_h.setObjectName(f"t{frame_num}_h")
        input_h.setGeometry(QRect(180, 10, 51, 21))

        # Update the last frame's Y position
        self.last_frame_y = new_frame.geometry().bottom()
