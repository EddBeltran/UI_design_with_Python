import sys
from PySide6.QtCore import QPoint, QSettings, QSize
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import ui_components as components
import ui_assets as assets
import ui_functions as functions
import numpy as np
import matplotlib.pyplot as plt

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
        self.right_section = components.RightWidgets()
        self.bottom_section = components.BottomWidgets()

        # add splitter between middle and right sections
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.addWidget(self.middle_section.stacked_widget)
        self.splitter.addWidget(self.right_section.stacked_widget)
        self.splitter.setSizes([0, 1])
        
        # set the widget components into main_layout
        self.main_layout.addWidget(self.left_section.frame, 0,0,1,1)
        self.main_layout.addWidget(self.splitter, 0,1,1,1)
        self.main_layout.addWidget(self.bottom_section.frame, 1,0,1,2)
        
        # call functions when a button is clicked or a signal is activated
        self.left_section.buttongroup.idClicked.connect(self.show_middle_pages)
        self.middle_section.signal.connect(self.show_right_content)
        self.right_section.signal_to_save_data.connect(self.set_points)
    
    def database_connexion(self):
        print("database connected")
        self.db_meshgrid = "local_project_directory/input-data/meshgrid.csv"

    #----------------------------------------------------------------------------- functions
    def set_points(self, value):
        if len(value) > 3:
            self.middle_section.addpoints(value[0], value[1], value[2], value[3])
        else:
            gridx, gridy  = functions.interpolacion_transfinita_2D(value[0], value[1], 20, 20)
            plt.plot(gridx, gridy, 'go')
            plt.show()#print()



    def show_middle_pages(self, id):
        self.middle_section.set_page_by_id(id)
        if self.middle_section.stacked_widget.frameGeometry().width() == 0:
            self.splitter.setSizes([236, 1075])

    def show_right_content(self, value):
        lx, ly, nx , ny = value[0], value[1], value[3], value[4] 
        gridx_2d, gridy_2d = np.meshgrid(np.linspace(0, lx, nx),
                                         np.linspace(0, ly, ny)) 
       
        #gridx_1d, gridy_1d  = functions.ARRtoLIST(gridx_2d, gridy_2d, nx, ny) 
        #functions.save_two_columns(self.db_meshgrid, gridx_1d, gridy_1d)

        self.right_section.set_page_by_id(1)
        #x = [1,2]; y = [1,2]
        #self.right_section.create_plot(x, y)
    
    def keyPressEvent(self, e):            
        if e.key() == (Qt.Key.Key_Control and Qt.Key.Key_X) :
            self.right_section.flag_plot += 1
        
        if e.key() == (Qt.Key.Key_Control and Qt.Key.Key_S) :
            print("Generar malla...")
            self.right_section.join_boundaries()
        
        if e.key() == (Qt.Key.Key_Control and Qt.Key.Key_C) :
            print("Generar malla...")
            self.right_section.new_mesh()
            



if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.setStyleSheet(assets.style)
    app.setWindowIcon(QIcon("icon.ico"))
    myApp = MainApp()    
    myApp.show()
    sys.exit(app.exec())