# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QPushButton, QWidget

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(820, 638)

        # Grid layout widget
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(90, 230, 160, 80))

        # Create grid layout
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        # Label and LineEdit at the beginning (optional example)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        # PushButton to add new column
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 40, 100, 32))
        self.pushButton.setText("Add Column")
        self.pushButton.clicked.connect(self.add_column)

        # Second PushButton (if needed, otherwise remove it)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 40, 100, 32))

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Add Column", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton 2", None))




    def add_column(self):
        # Determine the next available column index
        current_column_count = self.gridLayout.columnCount() # IMPORTANT

        # Add a new label in the first row
        new_label = QLabel(f"Label {current_column_count + 1}")
        self.gridLayout.addWidget(new_label, 0, current_column_count)

        # Add a new QLineEdit in the second row
        new_lineedit = QLineEdit()
        self.gridLayout.addWidget(new_lineedit, 1, current_column_count)

        # set column stretch to allow resizing
        self.gridLayout.setColumnStretch(current_column_count, 1) # IMPORTANT

        # Ensure the layout adjusts with the window size after adding the column
        self.gridLayoutWidget.adjustSize()
        self.gridLayoutWidget.resize(self.gridLayoutWidget.sizeHint())

        # Update the grid layout size after each new column
        self.gridLayoutWidget.setMinimumSize(self.gridLayoutWidget.sizeHint())



# Application setup
if __name__ == "__main__":
    app = QApplication([])

    # Create the main form
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    # Show the form
    Form.show()

    app.exec()