from PyQt6.QtWidgets import QMainWindow,QWidget,QApplication,QLabel,QPushButton,QLineEdit,QCheckBox
import sys
from PyQt6.QtGui import QPixmap,QFont

class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.initUI()
  
  def initUI(self):
    self.setWindowTitle("First PyQT Window")
    self.setGeometry(0, 0, 400, 150)

    # Total cost of coffee 
    self.total_cost = 0

    self.label = QLabel("Select your options", self)
    self.label.resize(200,20)
    self.label.move(20, 20)

    # Checkboxs
    sugar_checkbox = QCheckBox("Sugar($ 0.5)", self)
    sugar_checkbox.move(20, 40)
    sugar_checkbox.toggled.connect(self.sugar_checked)

    milk_checkbox = QCheckBox("Milk($ 1)", self)
    milk_checkbox.move(20, 60)
    milk_checkbox.toggled.connect(self.milk_checked)

    self.result_label = QLabel("Total cost is $0", self)
    self.result_label.resize(200,20)
    self.result_label.move(20, 90)

    


  def sugar_checked(self,checked):
    if checked:
      self.total_cost += 0.5
    else:
      self.total_cost -= 0.5
    self.result_label.setText(f"Total cost is ${self.total_cost}")

  def milk_checked(self,checked):
    if checked:
      self.total_cost += 1
    else:
      self.total_cost -= 1
    self.result_label.setText(f"Total cost is ${self.total_cost}")
  

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())