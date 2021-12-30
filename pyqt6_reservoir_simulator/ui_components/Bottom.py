from PySide6.QtWidgets import *

class BottomWidgets(QWidget):
    def __init__(self):
        super().__init__()

        self.frame = QFrame()
        self.frame.setObjectName("bottom_frame")
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.frame.setLayout(self.layout)

        #self.btn_1 = QPushButton("btn_1")
        #self.btn_2 = QPushButton("btn_2")
        #self.btn_3 = QPushButton("btn_3")
        #self.btn_4 = QPushButton("btn_4")
#
        #self.layout.addWidget(self.btn_1)
        #self.layout.addWidget(self.btn_2)
        #self.layout.addWidget(self.btn_3)
        #self.layout.addWidget(self.btn_4)