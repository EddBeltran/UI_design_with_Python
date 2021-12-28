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

        """
        GUI Sections (ui_components)
        __________________________
        |______________________-_x|
        |   |       |             |
        |   |       |             |
        Left| Middle|    Right    |
        |   |       |             |
        |   |       |             |
        |___|_______|_____________|
        |________Bottom___________|
        
        """

        self.left_section = components.LeftWidgets()
        self.middle_section = components.MiddleWidgets()
        self.rigth_section = components.RightWidgets()
        self.bottom_section = components.BottomWidgets()

        # add splitter between middle and right sections
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.addWidget(self.middle_section.stacked_widget)
        self.splitter.addWidget(self.rigth_section.stacked_widget)
        
        # set widgets into layouts
        self.main_layout.addWidget(self.left_section.frame, 0,0,1,1)
        self.main_layout.addWidget(self.splitter, 0,1,1,1)
        self.main_layout.addWidget(self.bottom_section.frame, 1,0,1,2)
        
        # call functions when a button is clicked
        for i in range(5):
            self.left_section.button[i].clicked.connect(self.fun_1)

    def fun_1(self):
        if self.left_section.button[0].isChecked():
            print("boton 1 checked")
        else:
            print("no bro")
        #self.middle_section.show_page_1()
        #self.middle_section.show_page_2()
        

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.setStyleSheet(assets.style)
    app.setWindowIcon(QIcon("icon.ico"))
    myApp = MainApp()    
    myApp.show()
    sys.exit(app.exec())