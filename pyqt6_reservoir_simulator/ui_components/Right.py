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



        
        
"""
    def show_frame(self):
        self.val = self.val + 1
        print("index: ", self.val)

        frame = QFrame()
        frame.setObjectName("sam_2")
        layout = QVBoxLayout()
        frame.setLayout(layout)

        self.lbl_2 = QLabel("Page with index: " + str(self.val))
        layout.addWidget(self.lbl_2)
        self.stacked_widget.insertWidget(self.val, frame)
        self.stacked_widget.setCurrentIndex(self.val)

    def show_frame_2(self):
        self.val = self.val - 1
        print("index: ", self.val)
        self.stacked_widget.setCurrentIndex(self.val)
"""