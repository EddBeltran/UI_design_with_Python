import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("Mi primer GUI")
        self.boton = QPushButton("Botón",self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())

