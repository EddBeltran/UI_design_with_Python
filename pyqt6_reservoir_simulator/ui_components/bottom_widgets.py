from PyQt6.QtWidgets import QFrame, QHBoxLayout, QPushButton, QWidget

class BottomWidgets(QWidget):
    def __init__(self):
        super().__init__()

        self.lables_frame = QFrame()
        self.lables_frame.setObjectName("sam_4")
        self.menu_layout = QHBoxLayout()
        self.menu_layout.setContentsMargins(0,0,0,0)
        self.lables_frame.setLayout(self.menu_layout)

        self.btn_1 = QPushButton("btn_1")
        self.btn_2 = QPushButton("btn_2")
        self.btn_3 = QPushButton("btn_3")
        self.btn_4 = QPushButton("btn_4")

        self.menu_layout.addWidget(self.btn_1)
        self.menu_layout.addWidget(self.btn_2)
        self.menu_layout.addWidget(self.btn_3)
        self.menu_layout.addWidget(self.btn_4)