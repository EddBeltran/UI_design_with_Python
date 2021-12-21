from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from assets.rc_files import *

class LeftWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.menu_frame = QFrame()
        self.menu_layout = QGridLayout()
        self.menu_layout.setContentsMargins(0,0,0,0)
        self.menu_layout.setSpacing(0)
        self.menu_frame.setLayout(self.menu_layout)

        self.btn_1 = QPushButton(self)
        self.btn_2 = QPushButton("btn_2")
        self.btn_3 = QPushButton("btn_3")
        self.btn_4 = QPushButton("btn_4")
        self.btn_5 = QPushButton("btn_5")

        self.btn_1.setIcon(QIcon(":/icons/roca.png"))
        self.btn_1.setIconSize(QSize(40,40))

        self.btn_1.setObjectName("don_bro")
        self.btn_2.setObjectName("left_menu")
        self.btn_3.setObjectName("left_menu")
        self.btn_4.setObjectName("left_menu")
        self.btn_5.setObjectName("left_menu")

        self.menu_layout.addWidget(self.btn_1, 0,0,1,1)
        self.menu_layout.addWidget(self.btn_2, 1,0,1,1)
        self.menu_layout.addWidget(self.btn_3, 2,0,1,1)
        self.menu_layout.addWidget(self.btn_4, 3,0,1,1)
        self.menu_layout.addWidget(self.btn_5, 4,0,1,1, Qt.AlignmentFlag.AlignBottom)
