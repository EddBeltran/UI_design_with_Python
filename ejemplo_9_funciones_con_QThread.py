import sys
from PyQt6.QtWidgets import QProgressBar, QPushButton, QWidget, QApplication, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import ejemplo_9_QThread_class as thread

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 450, 300)
        self.setWindowTitle("QThread")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.boton = QPushButton("Ejecutar función", self)
        self.boton.clicked.connect(self.graficar)
        self.layout.addWidget(self.boton, 0, 0, 1, 1)
        self.barra = QProgressBar(self)
        self.layout.addWidget(self.barra, 1, 0, 1, 1)

        self.fig = plt.figure(facecolor="#F4F4F4", tight_layout=True)
        self.canvas = FigureCanvas(self.fig)
        self.layout.addWidget(self.canvas, 2, 0, 1, 3)
        

    def graficar(self):
        # definimos al grafico y sus limites 
        ax = self.fig.add_subplot(111)
        ax.axis('equal')
        self.ln, = plt.plot([], [], 'r-')
        ax.set_xlim(-500, 500)
        ax.set_ylim(-500, 500)
        # importamos la clase externa
        self.funcion_externa = thread.External()
        self.funcion_externa.valor_barra.connect(self.actualizacion_barra)
        self.funcion_externa.valor_grafico.connect(self.actualizacion_grafico)
        self.funcion_externa.start()
        
    def actualizacion_barra(self, val):
        self.barra.setValue(val)
    
    def actualizacion_grafico(self, x, y):
        self.ln.set_data(x, y)
        self.canvas.draw()

        
if __name__ == '__main__':    
    app = QApplication(sys.argv)        
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())