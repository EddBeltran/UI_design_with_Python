import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QSplitter, QVBoxLayout, QWidget, QApplication, QGridLayout, QPushButton
import assets.styles.stylesheet as styles

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Reservoir Simulator")

        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.main_layout)

        #-----------------------------------------------------# Vertical menu (left section)
        menu_frame = QFrame()
        menu_frame.setObjectName("left_frame")
        menu_layout = QVBoxLayout()
        menu_layout.setContentsMargins(0,0,0,0)
        menu_frame.setLayout(menu_layout)
        #    Add widgets into menu_layout
        button =QPushButton("bt1", self)
        menu_layout.addWidget(button)
        button =QPushButton("btn2", self)
        menu_layout.addWidget(button)
        button =QPushButton("btn3", self)
        menu_layout.addWidget(button)
        button =QPushButton("btn4", self)
        menu_layout.addWidget(button)
        button =QPushButton("btn5", self)
        menu_layout.addWidget(button)
        
        self.main_layout.addWidget(menu_frame, 0,0,2,1)


        #-------------------------------------------------------# Splitter (right section)
        #   Left side
        splitter_frame_left = QFrame()
        splitter_frame_left.setObjectName("sam_1")
        splitter_layout_left = QVBoxLayout()
        splitter_frame_left.setLayout(splitter_layout_left)
        #   Add widgets into splitter_layout_left
        button = QPushButton("btn 1 | spliter left", self)
        splitter_layout_left.addWidget(button)
        button = QPushButton("btn 2 | spliter left", self)
        splitter_layout_left.addWidget(button)

        #   Right side
        splitter_frame_right = QFrame()
        splitter_frame_right.setObjectName("sam_2")
        splitter_layout_right = QVBoxLayout()
        splitter_frame_right.setLayout(splitter_layout_right)
        #   Add widgets into splitter_layout_right
        button = QPushButton("btn 1 | spliter right", self)
        splitter_layout_right.addWidget(button)
        button = QPushButton("btn 2 | spliter right", self)
        splitter_layout_right.addWidget(button)

        #    Join Left and Right frames into Splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(splitter_frame_left)
        splitter.addWidget(splitter_frame_right)
        splitter.setSizes([100, 300])

        self.main_layout.addWidget(splitter, 0,1,2,1)

        #--------------------------------------------------------# Bottom section
        bottom_frame = QFrame()
        bottom_frame.setObjectName("bottom_frame")
        bottom_layout = QHBoxLayout()
        bottom_frame.setLayout(bottom_layout)
        button =QPushButton()
        bottom_layout.addWidget(button)

        self.main_layout.addWidget(bottom_frame, 1,0,1,2, Qt.AlignmentFlag.AlignBottom)
        

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.setStyleSheet(styles.main)
    myApp = MainApp()    
    myApp.show()
    sys.exit(app.exec())