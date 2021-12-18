import sys
from PyQt6.QtWidgets import QLabel, QWidget, QApplication, QGridLayout, QPushButton, QLineEdit, QSlider

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("GUI con layout")

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        self.etiqueta = QLabel("GUI con hoja de estilos", self) 
        self.layout.addWidget(self.etiqueta, 0, 0, 1, 1)
        self.caja_texto = QLineEdit(self) 
        self.layout.addWidget(self.caja_texto, 1, 0, 1, 1)
        
        self.boton = QPushButton("Enviar", self) 
        self.layout.addWidget(self.boton, 2, 0, 1, 1)

if __name__ == '__main__':    
    app = QApplication(sys.argv)

    with open('ejemplo_10_hoja_de_estilos.qss', 'r') as f:
       style = f.read()
    app.setStyleSheet(style)

    myApp = MyApp()    
    myApp.show()
    sys.exit(app.exec())