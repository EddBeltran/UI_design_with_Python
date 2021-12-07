import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLineEdit, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("GUI con función")

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.etiqueta = QLabel("Metros a pies", self)
        self.layout.addWidget(self.etiqueta, 0, 1, 1, 1)
        self.caja_texto = QLineEdit(self)
        self.layout.addWidget(self.caja_texto, 1, 0, 1, 2)
        self.boton = QPushButton("Convertir", self) 
        self.layout.addWidget(self.boton, 1, 2, 1, 2)
        self.boton.clicked.connect(self.metros_a_pies) #En caso de click llamamos a la funcion
        self.etiqueta_2 = QLabel(self)
        self.layout.addWidget(self.etiqueta_2, 2, 1, 1, 1)
    
    # se define la funcion de metros a pies
    def metros_a_pies(self):
        metros  = self.caja_texto.text() # obtenemos el valor de la caja de texto
        if (metros):
            pies = float(metros)*3.28084 # aplicamos la formula para convertir m -> ft
            self.etiqueta_2.setText(str(pies) + " pies") # mandamos el valor a etiqueta_2

        
if __name__ == '__main__':    
    app = QApplication(sys.argv)        
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())