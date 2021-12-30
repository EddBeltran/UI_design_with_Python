from PySide6.QtCore import *
from PySide6.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  
import matplotlib.pyplot as plt
import numpy as np


class RightWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.fig = plt.figure()
        self.stacked_widget = QStackedWidget()
        self.page_0()
        self.page_1()
        self.set_page_by_id(1)
    
    def set_page_by_id(self, id):
        self.stacked_widget.setCurrentIndex(id)     
    
    #------------------------------------------------------- pages
    def page_0(self):
        id = 0
        frame = QFrame()
        layout = QVBoxLayout()
        #layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        lbl_1 = QLabel("default page right")
        layout.addWidget(lbl_1)
        self.stacked_widget.insertWidget(id, frame)
    
    def page_1(self):
        id = 1
        frame = QFrame()
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        self.stacked_widget.insertWidget(id, frame)
    
    def page_2(self):
        id = 2
        frame = QFrame()
        layout = QVBoxLayout()
        #layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        self.stacked_widget.insertWidget(id, frame)
    
    #---------------------------------------------------- plots and signals
    def create_plot(self, gridx, gridy):
        self.fig.clf()
        ax = self.fig.add_subplot(111)
        ax.plot(gridx, gridy, 'g-', gridx.transpose(), gridy.transpose(),'g-')
        #if axis_equal:
            #print("true")
            #ax.axis('equal')
        self.canvas.draw()
        self.canvas.flush_events()
         
    def send_parameters_by_signal(self):
        tuple_1 = (self.lx.text(), self.ly.text(), self.nodes_x.text(), self.nodes_y.text())
        self.signal.emit(tuple_1)