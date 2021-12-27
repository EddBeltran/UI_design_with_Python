import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import ui_components as components
import ui_assets as assets

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Reservoir Simulator")

        self.main_layout = QGridLayout()
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.main_layout)

        self.left_section = components.LeftWidgets()
        self.middle_section = components.MiddleWidgets()
        self.rigth_section = components.RightWidgets()
        self.bottom_section = components.BottomWidgets()

        # add splitter between middle and right sections
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.addWidget(self.middle_section.frame)
        self.splitter.addWidget(self.rigth_section.stacked_widget)
        
        # set widgets into layouts
        self.main_layout.addWidget(self.left_section.frame, 0,0,1,1)
        self.main_layout.addWidget(self.splitter, 0,1,1,1)
        self.main_layout.addWidget(self.bottom_section.frame, 1,0,1,2)

        self.left_section.btn_1.clicked.connect(self.fun_1)
        self.left_section.btn_2.clicked.connect(self.fun_2)

    def fun_1(self):
        self.rigth_section.show_frame()
    
    def fun_2(self):
        self.rigth_section.show_frame_2()
        

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.setStyleSheet(assets.style)
    app.setWindowIcon(QIcon("icon.ico"))
    myApp = MainApp()    
    myApp.show()
    sys.exit(app.exec())