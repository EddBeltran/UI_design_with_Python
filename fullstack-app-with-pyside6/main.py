import sys
from PySide6.QtCore import * #QPoint, QSettings, QSize
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from numpy.core.function_base import linspace
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
        
        # open pages when a button is clicked or a signal is activated
        self.left_section.buttongroup.idClicked.connect(self.show_middle_pages)
        self.middle_section.open_right_page.connect(self.show_right_pages)
        self.middle_section.customize_cbx.stateChanged.connect(self.show_right_pages_matplotlib)

        # meshgrid functions
        self.right_section.grid_control_points.connect(self.save_clicked_points)
        self.middle_section.grid_parameters.connect(self.generate_meshgrid_points)
        
    
    #----------------------------------------------------------------------------- functions
    def database_connexion(self):
        self.db_meshgrid = "local_project_directory/input-data/meshgrid.csv"

    def show_middle_pages(self, id):
        self.middle_section.set_page_by_id(id)
        if self.middle_section.stacked_widget.frameGeometry().width() == 0:
            self.splitter.setSizes([236, 1075])

    def show_right_pages(self, id):
        self.right_section.set_page_by_id(id)
    
    def show_right_pages_matplotlib(self, state):
        if state < 1: self.right_section.set_page_by_id(0)
        if state > 1: self.right_section.set_page_by_id(1)

    def save_clicked_points(self, value):
        self.middle_section.add_points_in_table(value[0], value[1], value[2], value[3])
        
    
    #--------------------------------------------------------------------- key press events
    def keyPressEvent(self, e):            
        if e.key() == (Qt.Key.Key_Control and Qt.Key.Key_X) :
            self.right_section.flag_plot += 1
        
        if e.key() == (Qt.Key.Key_Control and Qt.Key.Key_S) :
            self.right_section.xx_4.append(self.right_section.xx_1[0])
            self.right_section.yy_4.append(self.right_section.yy_1[0])
            self.right_section.line4.set_xdata(self.right_section.xx_4)
            self.right_section.line4.set_ydata(self.right_section.yy_4)
            self.right_section.canvas_2.draw()

        if e.key() == (Qt.Key.Key_Control and Qt.Key.Key_Z):
            self.right_section.flag_plot = 1
            self.right_section.set_drawing_workspace(self.length_x, self.length_y)


    def generate_meshgrid_points(self, value):
        self.length_x = value[0]
        self.length_y = value[1]
        self.nodes_x = value[3]
        self.nodes_y = value[4]
        self.right_section.ax.set_xlim(0, self.length_x)
        self.right_section.ax.set_ylim(0, self.length_y)

        if self.middle_section.customize_cbx.isChecked():
            puntos_control_f_sur_x = self.right_section.xx_1
            puntos_control_f_sur_y = self.right_section.yy_1
            puntos_control_f_este_x = self.right_section.xx_2
            puntos_control_f_este_y = self.right_section.yy_2
            puntos_control_f_norte_x = self.right_section.xx_3
            puntos_control_f_norte_y = self.right_section.yy_3
            puntos_control_f_oeste_x = self.right_section.xx_4
            puntos_control_f_oeste_y = self.right_section.yy_4
            front_sur_x, front_sur_y = functions.interpolador_lineal(puntos_control_f_sur_x, puntos_control_f_sur_y, self.nodes_x)
            front_este_x, front_este_y = functions.interpolador_lineal(puntos_control_f_este_x, puntos_control_f_este_y, self.nodes_y)
            front_norte_x, front_norte_y = functions.interpolador_lineal(puntos_control_f_norte_x, puntos_control_f_norte_y, self.nodes_x)
            front_oeste_x, front_oeste_y = functions.interpolador_lineal(puntos_control_f_oeste_x, puntos_control_f_oeste_y, self.nodes_y, ultimo_punto=True)
            self.contorno_malla_x = np.concatenate((front_sur_x, front_este_x, front_norte_x, front_oeste_x), axis=None)
            self.contorno_malla_y = np.concatenate((front_sur_y, front_este_y, front_norte_y, front_oeste_y), axis=None)            
            self.gridx, self.gridy  = functions.interpolacion_transfinita_2D(self.contorno_malla_x, self.contorno_malla_y, self.nodes_x, self.nodes_y)
            self.right_section.create_irregular_meshgrid(self.gridx, self.gridy)
 
        else:
            self.gridx, self.gridy = np.meshgrid( linspace(0, self.length_x, self.nodes_x), linspace(0, self.length_y, self.nodes_y))
            self.right_section.create_regular_meshgrid(self.gridx, self.gridy)        


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.setStyleSheet(assets.style)
    app.setWindowIcon(QIcon("icon.ico"))
    myApp = MainApp()    
    myApp.show()
    sys.exit(app.exec())