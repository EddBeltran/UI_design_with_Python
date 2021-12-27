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

        self.btn_1 = QPushButton(self)
        self.btn_2 = QPushButton(self)
        self.btn_3 = QPushButton(self)
        self.btn_4 = QPushButton(self)
        self.btn_5 = QPushButton(self)
        self.btn_6 = QPushButton(self)

        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_1.setIcon(QIcon(":/icons/carpeta.svg"))
        self.btn_2.setIcon(QIcon(":/icons/modelo-3d.svg"))
        self.btn_3.setIcon(QIcon(":/icons/curvas-k.svg"))
        self.btn_4.setIcon(QIcon(":/icons/ajustes.svg"))
        self.btn_5.setIcon(QIcon(":/icons/mapa.svg"))
        self.btn_6.setIcon(QIcon(":/icons/codigo.svg"))

        self.btn_1.setIconSize(QSize(35,35))
        self.btn_2.setIconSize(QSize(35,35))
        self.btn_3.setIconSize(QSize(35,35))
        self.btn_4.setIconSize(QSize(35,35))
        self.btn_5.setIconSize(QSize(35,35))
        self.btn_6.setIconSize(QSize(35,35))
   
        self.btn_1.setObjectName("left_menu_button")
        self.btn_2.setObjectName("left_menu_button")
        self.btn_3.setObjectName("left_menu_button")
        self.btn_4.setObjectName("left_menu_button")
        self.btn_5.setObjectName("left_menu_button")
        self.btn_6.setObjectName("left_menu_button")

        self.layout.addWidget(self.btn_1, 0,0,1,1)
        self.layout.addWidget(self.btn_2, 1,0,1,1)
        self.layout.addWidget(self.btn_3, 2,0,1,1)
        self.layout.addWidget(self.btn_4, 3,0,1,1)
        self.layout.addWidget(self.btn_5, 4,0,1,1)
        self.layout.addWidget(self.btn_6, 5,0,1,1, Qt.AlignmentFlag.AlignBottom)