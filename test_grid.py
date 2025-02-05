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


'''

        # Create a new grid layout for this column
        sub_grid_layout = QGridLayout()

        # Add the "Tipo" label at (0, 0)
        label_tipo = QLabel("Tipo")
        label_tipo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub_grid_layout.addWidget(label_tipo, 0, 0)

        # Add the ComboBox at (1, 0)
        combo = QComboBox()
        combo.addItem("Ø 15.42 mm")  # Add item "a"
        combo.addItem("Ø 13 mm")  # Add item "b"
        combo.addItem("Ø 9 mm")  # Add item "c"

        combo.setMinimumSize(99, 0)  # Min width: 99, height: default (0)
        combo.setMaximumSize(130, 16777215)  # Max width: 100, height: unlimited
        sub_grid_layout.addWidget(combo, 1, 0)

        # Add the "Area" label at (0, 1)
        label_area = QLabel("Area")
        label_area.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub_grid_layout.addWidget(label_area, 0, 1)

        # Add a QLineEdit at (1, 1)
        line_edit_area = QLineEdit()
        line_edit_area.setMinimumSize(70, 0)
        line_edit_area.setMaximumSize(100, 16777215)
        sub_grid_layout.addWidget(line_edit_area, 1, 1)

        # Add the new sub-grid layout to the main grid layout in the new column
        self.ui.gridLayout.addLayout(sub_grid_layout, 0, index)

        # Set stretch for the new column to allow resizing
        self.ui.gridLayout.setColumnStretch(index, 1)

'''