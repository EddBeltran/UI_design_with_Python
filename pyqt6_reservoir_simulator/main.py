import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QSplitter, QTextEdit, QWidget, QApplication, QGridLayout, QPushButton, QLineEdit, QSlider
import assets.styles.stylesheet as styles

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Reservoir Simulator")

        """
         ____________
        ||   |     | |
        || 1 | 2   |3|
        ||___|_____|_|
        ||___|_____|_|
        """
        
        hbox = QHBoxLayout(self)	
        #----------------------------Section Right
        topleft = QFrame()
        
        grid_ly = QGridLayout()
        button = QPushButton("nooo", self)
        grid_ly.addWidget(button, 0,0,1,1)
        #button.setLayout(grid_ly, 0,0,1,1)
        topleft.setLayout(grid_ly)
        #----------------------------Section Left
        #textedit = QTextEdit()
        #self.layout = QGridLayout()
        button = QPushButton("Bro", self)
        #self.setLayout(self.layout)

        #----------------------------Separator
        splitter1 = QSplitter(Qt.Orientation.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(button)
        splitter1.setSizes([100,200])
        #------------------------------------------------

        hbox.addWidget(splitter1)
        self.setLayout(hbox)

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.setStyleSheet(styles.main)
    myApp = MainApp()    
    myApp.show()
    sys.exit(app.exec())