import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLineEdit, QLabel
# Importamos los siguientes archivos para deplegar matplotlib en pyqt5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 450, 300)
        self.setWindowTitle("GUI con matplotlib")

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.lx = QLineEdit(self)
        self.lx.setPlaceholderText("distancia en x")
        self.layout.addWidget(self.lx, 0, 0, 1, 1)
        self.ly = QLineEdit(self)
        self.layout.addWidget(self.ly, 0, 1, 1, 1)
        self.ly.setPlaceholderText("distancia en y")

        #setPlaceholdertext despliega una etiqueta de texto dentro del QLineEdit
        
        self.nodos_x = QLineEdit(self)
        self.layout.addWidget(self.nodos_x, 1, 0, 1, 1)
        self.nodos_x.setPlaceholderText("nodos en x")
        self.nodos_y = QLineEdit(self)
        self.layout.addWidget(self.nodos_y, 1, 1, 1, 1)
        self.nodos_y.setPlaceholderText("nodos en y")
        

        self.boton = QPushButton("Generar malla", self) 
        self.layout.addWidget(self.boton, 2, 0, 1, 2)
        self.boton.clicked.connect(self.generar_malla)

        self.fig = plt.figure(figsize=(5, 4), facecolor="#F4F4F4", tight_layout=True)
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas, 3, 0, 1, 4)
        
    # se define la funcion para crear la malla
    def generar_malla(self):
        # obtenemos los valores de las cajas de texto
        nx, ny = self.nodos_x.text(), self.nodos_y.text()
        lx, ly = self.lx.text(), self.ly.text()

        if (nx and ny and lx and ly):
            # Creamos la malla con  numpy
            malla_x, malla_y = np.meshgrid(
                np.linspace(0,float(lx), int(nx)), 
                np.linspace(0,float(ly), int(ny)))

            self.fig.clf()
            ax = self.fig.add_subplot(111)
            ax.plot(malla_x, malla_y, 'g-', 
                malla_x.transpose(), malla_y.transpose(), 'g-')
            ax.axis('equal')
            self.canvas.draw()
        
        
if __name__ == '__main__':    
    app = QApplication(sys.argv)        
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
