from PySide6.QtWidgets import QLineEdit, QWidget, QPushButton, QGridLayout
from PySide6.QtCore import Signal

class GUI_DOS(QWidget):
    signal_gui = Signal(tuple)
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 100, 250, 100)
        self.setWindowTitle("GUI Secundaria")        
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.caja_1 = QLineEdit(self)
        self.layout.addWidget(self.caja_1, 0, 0, 1, 1)
        self.caja_2 = QLineEdit(self)
        self.layout.addWidget(self.caja_2, 0, 1, 1, 1)
        self.boton = QPushButton("Enviar", self)
        self.layout.addWidget(self.boton, 1, 0, 2, 1)
        self.boton.clicked.connect(self.enviar_parametros)

    def enviar_parametros(self):
        valor_1, valor_2 = self.caja_1.text(), self.caja_2.text()
        if (valor_1 and valor_2):
            valores = valor_1, valor_2
            self.signal_gui.emit(valores)

