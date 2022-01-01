import sys
from PyQt6.QtWidgets import *#QWidget, QApplication, QGridLayout, QPushButton
import pyqtgraph as pg
import numpy as np

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 450, 300)
        self.setWindowTitle("Graficos con pyqtgraph")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.sen = QPushButton("Seno", self)
        self.layout.addWidget(self.sen, 0, 0, 1, 1)
        self.sen.clicked.connect(self.graficar)
        self.cos = QPushButton("Coseno", self)
        self.layout.addWidget(self.cos, 0, 1, 1, 1)
        self.cos.clicked.connect(self.graficar)

        self.my_plot = pg.PlotWidget()
        self.puntos = self.my_plot.plot(pen=('#208ce4fd'), symbol='o')
        self.layout.addWidget(self.my_plot)
    
    def graficar(self):
        x = np.linspace(0,10,100)
        funcion = ((self.sender()).text()) #texto del botón al clic
        if funcion == "Seno": #ajustamos los puntos del grafico 
            y = np.sin(x)
            self.puntos.setData(x, y, symbolBrush =('#FFC300'))
        if funcion == "Coseno":
            y = np.cos(x)
            self.puntos.setData(x, y, symbolBrush =('#FF5733'))
       
if __name__ == '__main__':    
    app = QApplication(sys.argv)        
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())