from PySide6.QtWidgets import QMessageBox

def popup_msg(message):
    popup = QMessageBox()
    popup.setIcon(QMessageBox.Warning)  # ICONO
    popup.setWindowTitle("Mensaje")  # title
    popup.setText(message)  # Main message text
    popup.setStandardButtons(QMessageBox.Ok)  # agrega btn OK
    popup.exec()  # muestra ventana PopUp