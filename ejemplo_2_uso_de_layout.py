import sys
from PyQt6.QtWidgets import QProgressBar, QWidget, QApplication, QGridLayout, QPushButton, QLineEdit

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle("GUI con layout")

        self.layout = QGridLayout()       # Definimos un layout
        self.setLayout(self.layout)
        
        # Definimos el botón
        self.boton = QPushButton("Botón", self) 
        self.layout.addWidget(self.boton, 0, 0, 1, 1)
        # Primeros 2 digitos -> Posicion (vertical, horizontal, ...)
        # Ultimos 2 -> Espacios que ocupa (... vertical, horizontal) 
        
        self.caja_texto = QLineEdit(self) # Definimos la caja de texto
        # Le asignamos una posicion dentro del layout
        self.layout.addWidget(self.caja_texto, 0, 1, 1, 1)

        self.progress_bar = QProgressBar(self) # Definimos una progress bar
        # Le asignamos una posicion dentro del layout
        self.layout.addWidget(self.progress_bar, 1, 0, 1, 2)

        
if __name__ == '__main__':    
    app = QApplication(sys.argv)        
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())