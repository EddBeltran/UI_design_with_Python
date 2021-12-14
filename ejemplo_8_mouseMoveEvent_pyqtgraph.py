import sys
from PyQt6.QtWidgets import QLabel, QWidget, QApplication, QGridLayout
import pyqtgraph as pg
import numpy as np

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 450, 300)
        self.setWindowTitle("Graficos con pyqtgraph")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.etiqueta = QLabel("Position: ", self)
        self.layout.addWidget(self.etiqueta, 0, 0, 1, 1)
        self.graficar()
        
    def graficar(self):
        x = np.linspace(0,10,100)
        y = np.sin(x)    
        self.my_plot = pg.PlotWidget()
        self.puntos = self.my_plot.plot(x,y, pen=('#208ce4fd'), symbol='o')
        self.layout.addWidget(self.my_plot, 1, 0, 1, 3)
        self.my_plot.scene().sigMouseMoved.connect(self.mouseMoved)
    
    def mouseMoved(self, point):
        self.position = self.my_plot.plotItem.vb.mapSceneToView(point)
        x_punto, y_punto = self.position.x(), self.position.y()
        self.etiqueta.setText("position: " 
            + str(round(x_punto, 3)) + "  " + str(round(y_punto,3)))
       
if __name__ == '__main__':    
    app = QApplication(sys.argv)        
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())