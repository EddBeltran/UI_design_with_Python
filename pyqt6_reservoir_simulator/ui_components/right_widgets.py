from PySide6.QtCore import *
from PySide6.QtWidgets import *

class RightWidgets(QWidget):
    def __init__(self):
        super().__init__()

        #   Left side
        self.frame_left = QFrame()
        self.frame_left.setObjectName("sam_1")
        self.layout_left = QVBoxLayout()
        self.frame_left.setLayout(self.layout_left)
        self.lbl_1 = QLabel("Default Left Frame")
        self.layout_left.addWidget(self.lbl_1)
        #   Right side
        self.stacked_widget = QStackedWidget()
        self.frame_right = QFrame()
        self.frame_right.setObjectName("sam_2")
        self.layout_right = QVBoxLayout()
        self.frame_right.setLayout(self.layout_right)
        #   Add widgets into layout_right
        self.lbl_2 = QLabel("Default Right Frame")
        self.layout_right.addWidget(self.lbl_2)
        self.stacked_widget.addWidget(self.frame_right)

        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.addWidget(self.frame_left)
        self.splitter.addWidget(self.stacked_widget)        

        self.val = 0

        
        

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