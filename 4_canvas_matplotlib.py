import sys
from PySide6.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import numpy as np

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 450, 300)
        self.setWindowTitle("Canvas con matplotlib")
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.distancia_x = QLineEdit(self)
        self.distancia_y = QLineEdit(self)
        self.nodos_x = QLineEdit(self)
        self.nodos_y = QLineEdit(self)
        self.boton = QPushButton("Generar malla", self) 
        self.figura = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.figura)
        
        self.distancia_x.setPlaceholderText("distancia en x")
        self.distancia_y.setPlaceholderText("distancia en y")
        self.nodos_x.setPlaceholderText("nodos en x")
        self.nodos_y.setPlaceholderText("nodos en y")

        self.layout.addWidget(self.distancia_x, 0, 0, 1, 1)
        self.layout.addWidget(self.distancia_y, 0, 1, 1, 1)
        self.layout.addWidget(self.nodos_x, 1, 0, 1, 1)
        self.layout.addWidget(self.nodos_y, 1, 1, 1, 1) 
        self.layout.addWidget(self.boton, 2, 0, 1, 2)
        self.layout.addWidget(self.canvas, 3, 0, 1, 4)

        self.boton.clicked.connect(self.generar_malla_rectangular)

    def generar_malla_rectangular(self):
        nx, ny = self.nodos_x.text(), self.nodos_y.text()
        lx, ly = self.distancia_x.text(), self.distancia_y.text()

        if (nx != '' and ny != '' and lx != '' and ly != ''):
            malla_x, malla_y = np.meshgrid(
                np.linspace(0,float(lx), int(nx)), 
                np.linspace(0,float(ly), int(ny)))

            self.figura.clf()
            ax = self.figura.add_subplot(111)
            ax.plot(malla_x, malla_y, 'g-', 
                malla_x.transpose(), malla_y.transpose(), 'g-')
            ax.axis('equal')
            self.canvas.draw()
        
if __name__ == '__main__':    
    app = QApplication(sys.argv)        
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())