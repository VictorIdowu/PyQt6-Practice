from PyQt6.QtWidgets import QWidget,QApplication,QLabel
import sys
from PyQt6.QtGui import QPixmap,QFont

class Window(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("First PyQT Window")
    self.setGeometry(0, 0, 400, 400)

    with open('car.png'):
      image_label = QLabel(self)
      pixmap = QPixmap('car.png')
      image_label.setPixmap(pixmap)
      image_label.move(60,0)

    # Car name
    name_label = QLabel(self)
    name_label.setText("My Car")
    name_label.setFont(QFont("Araial", 14))
    name_label.move(170,170)

    # Engine Specs
    engine_label = QLabel(self)
    engine_label.setText("Engine Capacity: 4L TFSI")
    engine_label.setFont(QFont("Araial", 10))
    engine_label.move(10,210)

    # Features
    features_label = QLabel(self)
    features_label.setText("Features: ABS, EBD, ADAS")
    features_label.setFont(QFont("Araial", 10))
    features_label.move(10,240)

    # Models
    models_label = QLabel(self)
    models_label.setText("Models: 2.2 Petrol, 1.8 Diesel")
    models_label.setFont(QFont("Araial", 10))
    models_label.move(10,270)

    # Pricing
    pricing_label = QLabel(self)
    pricing_label.setText("$80,000")
    pricing_label.setFont(QFont("Araial", 10))
    pricing_label.move(10,300)

    


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())