from PySide6.QtCore import QThread, pyqtSignal
import numpy as np


class External(QThread):
    valor_barra = pyqtSignal(int)
    valor_grafico = pyqtSignal(np.ndarray, np.ndarray)
    
    def run(self):
        for i in range(0, 360):
            theta = np.radians(np.linspace(0, i*3, 300))
            r = theta**2
            x = r*np.cos(theta)
            y = r*np.sin(theta)
            
            self.valor_grafico.emit( x, y )    
            self.valor_barra.emit( int(((i+1)/360)*100) )
        

