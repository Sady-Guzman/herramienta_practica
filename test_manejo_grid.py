from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtCore import QRect


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 999, 434)

        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(30, 110, 941, 291))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.label_cotas = QLabel("COTAS", self.gridLayoutWidget)
        self.label_relleno = QLabel("RELLENO", self.gridLayoutWidget)

        self.gridLayout.addWidget(self.label_cotas, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.label_relleno, 0, 0, 1, 1)

        self.btn_add = QPushButton("add", self)
        self.btn_add.setGeometry(QRect(80, 40, 100, 32))
        self.btn_del = QPushButton("del", self)
        self.btn_del.setGeometry(QRect(210, 40, 100, 32))

        self.btn_add.clicked.connect(self.add_label)
        self.btn_del.clicked.connect(self.remove_last_column)

        self.label_count = 0  # Counter for dynamic labels


    def add_label(self):
        """Adds a label to the right end of row 1, then a spacer."""
        self.label_count += 1
        new_label = QLabel(f"Label {self.label_count}", self.gridLayoutWidget)

        col_position = self.gridLayout.columnCount()
        self.gridLayout.addWidget(new_label, 1, col_position)

        # Always add a new spacer to the right
        # spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # self.gridLayout.addItem(spacer, 1, col_position + 1)



    def remove_last_column(self):
        col_count = self.gridLayout.columnCount()
        print("col count = ", col_count)

        if col_count > 1:  # Ensure there's something to remove
            last_col = self.gridLayout.columnCount() - 1
            print("Last col = ", last_col)

            # Remove widget from the last column of row 1
            item = self.gridLayout.itemAtPosition(1, last_col)

            if item:
                widget = item.widget()
                if widget:
                    widget.setParent(None)  # Remove widget from layout
                    widget.deleteLater()
                self.gridLayout.removeItem(item)
            
            # Ensure the layout is refreshed
            self.gridLayout.invalidate()  # Recalculate layout after removal
        


if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()