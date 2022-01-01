import sys
from PySide6.QtCore import QPoint, QSettings, QSize
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import ui_components as components
import ui_assets as assets
import ui_functions as functions
import numpy as np

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        #self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Reservoir Simulator")

        self.database_connexion()

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
        |   |   spplitter         |
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
        #self.splitter.HLine.setStyleSheet()
        self.splitter.addWidget(self.middle_section.stacked_widget)
        self.splitter.addWidget(self.rigth_section.stacked_widget)
        #self.splitter.HLine.clicked.connect(self.spplitter_val)
        #self.val = self.splitter.saveGeometry()
        #self.splitter.setSizes([statusWin.sizeHint().height()*2, statusWin.sizeHint().height()*0.05])
        #self.splitter.setStretchFactor(0, 2)
        #self.splitter.setStretchFactor(1, 5)
        self.splitter.setSizes([0, 1])
        #self.splitter.setStretchFactor(1, 10)
        #self.settings = QSettings()
        #self.splitter.saveGeometry()
        #self.settings = QSettings( 'My company', 'myApp')
        #self.resize(self.settings.value("size",QSize(800, 600)))
        #self.move(self.settings.value("pos", QPoint(50, 50)))
        
        #self.settings.setValue("floatingWindow/size", self.size())
        #self.settings.setValue("floatingWindow/pos", self.pos())
        
        # set the widget components into main_layout
        self.main_layout.addWidget(self.left_section.frame, 0,0,1,1)
        self.main_layout.addWidget(self.splitter, 0,1,1,1)
        self.main_layout.addWidget(self.bottom_section.frame, 1,0,1,2)
        
        # call functions when a button is clicked or a signal is activated
        self.left_section.buttongroup.idClicked.connect(self.show_middle_pages)
        self.middle_section.signal.connect(self.show_right_content)
    
    def database_connexion(self):
        print("database connected")
        self.db_meshgrid = "local_project_directory/input-data/meshgrid.csv"
        #db_meshgrid = "local_project_directory/input-data/meshgrid.xlsx"


    

    def show_middle_pages(self, id):
        self.middle_section.set_page_by_id(id)
    
    def show_right_content(self, value):
        lx, ly, nx , ny = value[0], value[1], value[3], value[4] 
        gridx_2d, gridy_2d = np.meshgrid(np.linspace(0, lx, nx),
                                         np.linspace(0, ly, ny)) 
       
        gridx_1d, gridy_1d  = functions.ARRtoLIST(gridx_2d, gridy_2d, nx, ny) 
        functions.save_two_columns(self.db_meshgrid, gridx_1d, gridy_1d)

        self.rigth_section.create_plot(gridx_2d, gridy_2d)
    
    def keyPressEvent(self, e): #keyPressEvent            
        if e.key() == (Qt.Key.Key_Control and Qt.Key.Key_X) :
            #self.splitter.setSizes([500, 1200])
            self.splitter.setSizes([236, 1075])
        
        if e.key() == (Qt.Key.Key_Control and Qt.Key.Key_Z) :
            self.splitter.get([0, 1])
            #self.splitter.getSizes()
        
        if e.key() == (Qt.Key.Key_Control and Qt.Key.Key_S) :
            wid_1 = self.middle_section.stacked_widget.frameGeometry().width()
            wid_2 = self.rigth_section.stacked_widget.frameGeometry().width()

            print("dimension", wid_1, wid_2)

        
                    
        #self.settings.setValue("size", self.size())
        #self.settings.setValue("pos", self.pos())
        #e.accept()
            #s = [200, 500]
            #self.splitter.restoreState()
    
    def spplitter_val(self):
        print("xss")


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.setStyleSheet(assets.style)
    app.setWindowIcon(QIcon("icon.ico"))
    myApp = MainApp()    
    myApp.show()
    sys.exit(app.exec())