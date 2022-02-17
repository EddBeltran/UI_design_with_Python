import sys
from PySide6.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QGridLayout
from  ejemplo_6_pyqtsignal_GUI_secundaria import GUI_DOS # Importamos la gui secundaria

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 250, 200)
        self.setWindowTitle("GUI Principal")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.boton = QPushButton("Abrir GUI Secundaria",self)
        self.layout.addWidget(self.boton, 0, 0, 1, 1)
        self.boton.clicked.connect(self.abrir_gui)
        self.etiqueta = QLabel(self)
        self.layout.addWidget(self.etiqueta, 1, 0, 1, 1)
        # importamos la segunda GUI y en caso de recibir la señal, corre
        # la función -> recibir valores
        self.nueva_ventana = GUI_DOS()
        self.nueva_ventana.signal_gui.connect(self.recibir_valores)
        
    def abrir_gui(self): #Funcion para abrir la segunda ventana
        self.nueva_ventana.show()
    
    def recibir_valores(self,valor):
        texto = ( "Has recibido los valores: " + valor[0] + ", " + valor[1] )
        self.etiqueta.setText(texto)

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())
