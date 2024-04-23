from PyQt6.QtWidgets import QMainWindow,QWidget,QApplication,QLabel,QPushButton,QLineEdit,QCheckBox,QMessageBox
import sys
from PyQt6.QtGui import QPixmap,QFont

class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.initUI()
  
  def initUI(self):
    self.setWindowTitle("First PyQT Window")
    self.setGeometry(0, 0, 400, 150)

    button  = QPushButton("Show Messagebox", self)
    button.setGeometry(150, 80, 200, 40)
    button.clicked.connect(self.show_messagebox)

  
  def show_messagebox(self):
    msg = QMessageBox()
    msg.setWindowTitle("Message Box")
    msg.setText("This is a message box")
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
    msg.setDefaultButton(QMessageBox.StandardButton.Ok)
    result = msg.exec()
    if result == QMessageBox.StandardButton.Ok:
      print("OK")
    else:
      print("Cancel")

   

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())