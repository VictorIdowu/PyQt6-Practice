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

    num_label = QLabel("Enter a number", self)
    num_label.move(20, 20)

    self.num_input = QLineEdit(self)
    self.num_input.move(200, 20)

    cal_button = QPushButton("Find Root", self)
    cal_button.move(200, 60)
    cal_button.clicked.connect(self.find_root)

    self.result_label = QLabel("Result: ", self)
    self.result_label.move(20,100)
  
  def find_root(self):
    try:
      num = int(self.num_input.text())
      if num < 0:
        msg = QMessageBox.warning(self, "Invalid input","Please enter a positive number")
        return 
      root = num ** 0.5
      if root.is_integer():
        self.result_label.setText("The root of {} is {}".format(num, root))
        self.result_label.resize(300,20)
      else:
        msg = QMessageBox.warning(self, "Not a perfect square","The number you entered is not a perfect square")
    except ValueError:
      msg = QMessageBox.warning(self, "Invalid input","Please enter a valid number")
      



   

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())