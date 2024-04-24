from PyQt6.QtWidgets import QGridLayout,QVBoxLayout,QHBoxLayout,QMainWindow,QWidget,QApplication,QLabel,QPushButton,QLineEdit,QCheckBox,QMessageBox
import sys
from PyQt6.QtGui import QPixmap,QFont

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
  
  def initUI(self):
    self.setWindowTitle("First PyQT Window")
    self.setGeometry(0, 0, 400, 150)

    label_1 = QLabel("Label 1")
    label_2 = QLabel("Label 2")
    label_3 = QLabel("Label 3")

    button_1 = QPushButton("Button 1")
    button_2 = QPushButton("Button 2")
    button_3 = QPushButton("Button 3")

    layout = QGridLayout()
    self.setLayout(layout)

    layout.addWidget(label_1,0,0)
    layout.addWidget(label_2,0,1)
    layout.addWidget(label_3,0,2)
    layout.addWidget(button_1,1,0)
    layout.addWidget(button_2,1,1)
    layout.addWidget(button_3,1,2)




    

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())