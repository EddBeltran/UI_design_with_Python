import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 250)
        self.setWindowTitle("GUI con eventos")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.etiqueta = QLabel(self)
        self.figura = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.figura)
        self.layout.addWidget(self.etiqueta)
        self.layout.addWidget(self.canvas)
        self.establecer_grafico()
        
    def establecer_grafico(self):
        self.figura.clf()
        self.ax = self.figura.add_subplot(111)
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)
        self.puntos_x, self.puntos_y  = [], []
        self.polilinea, = self.ax.plot(self.puntos_x, self.puntos_y, 'co-')
        plt.connect('motion_notify_event', self.on_move)
        plt.connect('button_press_event', self.on_click)
        self.canvas.draw()

    def on_move(self, event):
        if event.inaxes:
            x, y = event.xdata, event.ydata
            self.etiqueta.setText(
                "Coordenadas: " 
                + str(round(x)) + "," 
                + str(round(y))
            )
            
    def on_click(self, event):
        if event.button is MouseButton.LEFT:
            x, y = event.xdata, event.ydata
            self.puntos_x.append(x)
            self.puntos_y.append(y)
            self.polilinea.set_xdata(self.puntos_x)
            self.polilinea.set_ydata(self.puntos_y)
            self.canvas.draw()
        
    def keyPressEvent(self, event):            
        if event.key() == (Qt.Key.Key_Control and Qt.Key.Key_X) :
            self.etiqueta.setText("Se han borrado los puntos")
            self.establecer_grafico()
            
if __name__ == '__main__':    
    app = QApplication(sys.argv)        
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())