from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QLineEdit
import sys
from PyQt6.QtGui import QPixmap,QFont

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
  
  def initUI(self):
    self.setWindowTitle("First PyQT Window")
    self.setGeometry(0, 0, 400, 400)

    # Label
    name_label = QLabel(self)
    name_label.setText("Enter your name")
    name_label.move(60, 10)

    # Input
    self.name = QLineEdit(self)
    self.name.resize(200,20)
    # name.setPlaceholderText("Enter your name")
    self.name.move(60, 30)

    # Button
    button = QPushButton(self)
    button.setText("Add")
    button.move(200, 80)
    button.clicked.connect(self.button_clicked)

    # Label
    self.result_label = QLabel(self)
    self.result_label.setFixedSize(150,20)
    self.result_label.move(60, 120)

  def button_clicked(self):
    print(f"Your name is {self.name.text()}")
    self.result_label.setText(f"Your name is {self.name.text()}")
    

    

    


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())