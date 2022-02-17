import sys
from PySide6.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI con función")
        self.setGeometry(100, 100, 300, 150)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.etiqueta_titulo = QLabel("Metros a pies", self)
        self.caja_texto = QLineEdit(self)
        self.boton = QPushButton("Convertir", self) 
        self.etiqueta_resultado = QLabel("Resultado", self)

        self.layout.addWidget(self.etiqueta_titulo, 0, 0, 1, 2)
        self.layout.addWidget(self.caja_texto, 1, 0, 1, 1)
        self.layout.addWidget(self.boton, 1, 1, 1, 1)
        self.layout.addWidget(self.etiqueta_resultado, 2, 0, 1, 2)
        #    En caso de click llamamos a la funcion
        self.boton.clicked.connect(self.calcular_metros_a_pies)
    
    def calcular_metros_a_pies(self):
        metros  = self.caja_texto.text()
        if (metros):
            pies = float(metros)*3.28084
            self.etiqueta_resultado.setText(str(pies) + " pies")
        
if __name__ == '__main__':    
    app = QApplication(sys.argv)        
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())