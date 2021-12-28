from PySide6.QtCore import *
from PySide6.QtWidgets import *


class RightWidgets(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()
        self.frame = QFrame()
        self.frame.setObjectName("sam_2")
        self.layout = QVBoxLayout()
        self.frame.setLayout(self.layout)
        
        self.lbl_1 = QLabel("Default Right Frame")
        self.layout.addWidget(self.lbl_1)
        self.stacked_widget.addWidget(self.frame)