import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPlainTextEdit, QPushButton
from ui_files.ui_main_window3 import Ui_Dialog  # Import from the ui_files directory

# New window class to display the text from the text box
class TextWindow(QDialog):
    def __init__(self, text):
        super().__init__()
        self.setWindowTitle("Text Window")
        layout = QVBoxLayout()
        label = QLabel(text)  # Display the passed text
        layout.addWidget(label)
        self.setLayout(layout)

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI on the dialog window
        
        # Connect the button's clicked signal in the 2nd tab to show the text window
        self.ui.pushButton.clicked.connect(self.show_text_window)
        
        # Connect the button's clicked signal in the 3rd tab to display the text
        self.ui.pushButton_2.clicked.connect(self.show_text_from_tab2)

    def show_text_window(self):
        # Retrieve the text from the text box (QPlainTextEdit) in the 2nd tab
        text = self.ui.plainTextEdit.toPlainText()

        # Create and show the TextWindow with the retrieved text
        self.text_window = TextWindow(text)
        self.text_window.exec()  # Show the window as a modal dialog

    def show_text_from_tab2(self):
        # Retrieve the text from the text box (QPlainTextEdit) in the 2nd tab
        text = self.ui.plainTextEdit.toPlainText()

        # Create and show the TextWindow with the retrieved text from the 2nd tab
        self.text_window = TextWindow(text)
        self.text_window.exec()  # Show the window as a modal dialog

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application
    dialog = MyDialog()            # Create the dialog window
    dialog.show()                  # Show the dialog window
    sys.exit(app.exec())           # Start the application's event loop