import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *

import ui_components as component
import assets.stylesheet as styles


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Reservoir Simulator")

        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.main_layout)

        self.left_section = component.LeftWidgets()
        self.rigth_section = component.RightWidgets()
        self.bottom_section = component.BottomWidgets()

        self.left_section.btn_1.clicked.connect(self.fun_1)
        self.left_section.btn_2.clicked.connect(self.fun_2)

        self.main_layout.addWidget(self.left_section.menu_frame, 0,0,1,1)
        self.main_layout.addWidget(self.rigth_section.splitter, 0,1,1,1)
        self.main_layout.addWidget(self.bottom_section.lables_frame, 1,0,1,2)

    def fun_1(self):
        self.rigth_section.show_frame()
    
    def fun_2(self):
        self.rigth_section.show_frame_2()
        

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.setStyleSheet(styles.main)
    app.setWindowIcon(QIcon("icon.ico"))
    myApp = MainApp()    
    myApp.show()
    sys.exit(app.exec())