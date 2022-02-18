import sys
from PySide6.QtWidgets import *
from  gui_secundaria import GuiSecundaria

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 250, 200)
        self.setWindowTitle("GUI Principal")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.boton = QPushButton("Abrir GUI Secundaria",self)
        self.etiqueta = QLabel(self)
        self.layout.addWidget(self.boton, 0, 0, 1, 1)
        self.layout.addWidget(self.etiqueta, 1, 0, 1, 1)
        self.boton.clicked.connect(self.abrir_gui_secundaria)
        
        #    Definimos a la GUI secundaria
        self.nueva_ventana = GuiSecundaria()
        self.nueva_ventana.signal.connect(self.recibir_valores)
        
    def abrir_gui_secundaria(self):
        self.nueva_ventana.show()
    
    def recibir_valores(self,valor):
        texto = ( "Has recibido los valores: " + valor[0] + ", " + valor[1] )
        self.etiqueta.setText(texto)

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())
