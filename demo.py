from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QLineEdit
import sys
from PyQt6.QtGui import QPixmap,QFont

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
  
  def initUI(self):
    self.setWindowTitle("First PyQT Window")
    self.setGeometry(0, 0, 400, 150)

    # Label
    num1_label = QLabel("Enter first number",self)
    num1_label.resize(200,20)
    num1_label.move(20, 20)

    # Input
    self.num1_input = QLineEdit(self)
    self.num1_input.resize(200,20)
    self.num1_input.move(150, 20)

    # Label 2
    num2_label = QLabel("Enter second number",self)
    num2_label.resize(200,20)
    num2_label.move(20, 60)

    # Input 2
    self.num2_input = QLineEdit(self)
    self.num2_input.resize(200,20)
    self.num2_input.move(150, 60)

    # Button
    button = QPushButton("Calculate",self)
    button.move(270, 100)
    button.clicked.connect(self.calculate)

    # Label
    self.result_label = QLabel("Result: ", self)
    self.result_label.move(20, 100)

  def calculate(self):
    try:
      result = float(self.num1_input.text()) + float(self.num2_input.text())
      self.result_label.setText(f"Result: {result:.2f}")
      self.result_label.resize(300,20)
    except ValueError:
      self.result_label.setText("Invalid Input, Please enter numbers")
      self.result_label.resize(300,20)

    


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())