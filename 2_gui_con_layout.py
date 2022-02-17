import sys
from PySide6.QtWidgets import (QProgressBar, QWidget, QApplication, QVBoxLayout, QPushButton, QLineEdit)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("GUI con layout")
        #    Definir el layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        #    Definir widgets
        self.boton = QPushButton("Botón", self) 
        self.caja_texto = QLineEdit(self)
        self.barra_progreso = QProgressBar(self)
        #    Agregar widgets al layout
        self.layout.addWidget(self.boton)
        self.layout.addWidget(self.caja_texto)
        self.layout.addWidget(self.barra_progreso)
        
if __name__ == '__main__':    
    app = QApplication(sys.argv)        
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())