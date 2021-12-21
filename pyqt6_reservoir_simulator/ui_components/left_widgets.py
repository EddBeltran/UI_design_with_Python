from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QGridLayout, QPushButton, QVBoxLayout, QWidget

class LeftWidgets(QWidget):
    def __init__(self):
        super().__init__()

        self.menu_frame = QFrame()
        self.menu_layout = QGridLayout()
        self.menu_layout.setContentsMargins(0,0,0,0)
        self.menu_layout.setSpacing(0)
        self.menu_frame.setLayout(self.menu_layout)

        self.btn_1 = QPushButton("btn_1")
        self.btn_2 = QPushButton("btn_2")
        self.btn_3 = QPushButton("btn_3")
        self.btn_4 = QPushButton("btn_4")

        self.btn_5 = QPushButton("btn_5")

        self.menu_layout.addWidget(self.btn_1, 0,0,1,1)
        self.menu_layout.addWidget(self.btn_2, 1,0,1,1)
        self.menu_layout.addWidget(self.btn_3, 2,0,1,1)
        self.menu_layout.addWidget(self.btn_4, 3,0,1,1)

        self.menu_layout.addWidget(self.btn_5, 4,0,1,1, Qt.AlignmentFlag.AlignBottom)
