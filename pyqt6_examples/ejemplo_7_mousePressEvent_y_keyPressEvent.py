import sys
from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel
from PyQt6.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("Eventos")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.etiqueta = QLabel(self)
        self.layout.addWidget(self.etiqueta, 0, 1, 1, 1)

    def mousePressEvent(self, e):        
        if e.button() == Qt.MouseButton.LeftButton:
            self.etiqueta.setText("Click...")        
        if e.button() == Qt.MouseButton.RightButton:
            self.etiqueta.setText("Click Derecho...")
            
    def keyPressEvent(self, e):            
        if e.key() == (Qt.Key.Key_Control and Qt.Key.Key_X) :
            self.etiqueta.setText("Ctrl + X Presionado...")
        if e.key() == (Qt.Key.Key_Shift and Qt.Key.Key_Q) :
            self.etiqueta.setText("Shift + Q Presionado...")
        if e.key() == (Qt.Key.Key_Escape) :
            self.etiqueta.setText("Esc Presionado...")
    
        
if __name__ == '__main__':    
    app = QApplication(sys.argv)        
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec())