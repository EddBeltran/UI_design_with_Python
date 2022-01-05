from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class LeftWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.frame = QFrame()
        self.layout = QGridLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.frame.setLayout(self.layout)
        self.frame.setObjectName("left_menu_frame")

        self.button = ["carpeta","modelo-3d","curvas-k","ajustes","mapa","codigo"]
        last_button = len(self.button) - 1 # the last button has a different alignment
        self.buttongroup = QButtonGroup()
        
        for index, value in enumerate(self.button):
            self.button[index] = QPushButton(self)
            self.button[index].setCursor(QCursor(Qt.PointingHandCursor))
            self.button[index].setObjectName("left_menu_button")
            self.button[index].setIcon(QIcon(":/icons/"+value+".svg"))
            self.button[index].setIconSize(QSize(35,35))
            self.button[index].setCheckable(True)

            self.buttongroup.addButton(self.button[index], index)
            
            if index != last_button :
                self.layout.addWidget(self.button[index], index,0,1,1)
            else:
                self.layout.addWidget(self.button[last_button], last_button,0,1,1, Qt.AlignmentFlag.AlignBottom)