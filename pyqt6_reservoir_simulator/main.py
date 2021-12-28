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
        # call the ui components
        self.left_section = components.LeftWidgets()
        self.middle_section = components.MiddleWidgets()
        self.rigth_section = components.RightWidgets()
        self.bottom_section = components.BottomWidgets()

        # add splitter between middle and right sections
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.addWidget(self.middle_section.stacked_widget)
        self.splitter.addWidget(self.rigth_section.stacked_widget)
        
        # set the widget components into main_layout
        self.main_layout.addWidget(self.left_section.frame, 0,0,1,1)
        self.main_layout.addWidget(self.splitter, 0,1,1,1)
        self.main_layout.addWidget(self.bottom_section.frame, 1,0,1,2)
        
        # call functions when a button is clicked or a signal is activated
        self.left_section.buttongroup.idClicked.connect(self.show_middle_sections)
        self.middle_section.signal_middle.connect(self.plot_grid)

    def show_middle_sections(self, id):
        self.middle_section.set_page_by_id(id)
    
    def plot_grid(self, value):
        print("singnal: ", value)


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.setStyleSheet(assets.style)
    app.setWindowIcon(QIcon("icon.ico"))
    myApp = MainApp()    
    myApp.show()
    sys.exit(app.exec())