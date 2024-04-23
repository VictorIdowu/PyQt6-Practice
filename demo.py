from PyQt6.QtWidgets import QVBoxLayout,QHBoxLayout,QMainWindow,QWidget,QApplication,QLabel,QPushButton,QLineEdit,QCheckBox,QMessageBox
import sys
from PyQt6.QtGui import QPixmap,QFont

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
  
  def initUI(self):
    self.setWindowTitle("First PyQT Window")
    self.setGeometry(0, 0, 400, 150)

    button_1 = QPushButton("Button 1")
    button_2 = QPushButton("Button 2")
    button_3 = QPushButton("Button 3")
    button_4 = QPushButton("Button 4")

    h_box_1 = QHBoxLayout()
    h_box_1.addWidget(button_1)
    h_box_1.addWidget(button_2)

    h_box_2 = QHBoxLayout()
    h_box_2.addWidget(button_3)
    h_box_2.addWidget(button_4)

    v_box = QVBoxLayout()
    v_box.addLayout(h_box_1)
    v_box.addLayout(h_box_2)

    self.setLayout(v_box)




    

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())