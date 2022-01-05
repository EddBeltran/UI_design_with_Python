from PySide6 import QtCharts
from PySide6.QtCore import *
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backend_bases import MouseButton
#import PySide6.QtCharts


class RightWidgets(QWidget):
    signal_to_save_data = Signal(tuple)
    
    def __init__(self):
        super().__init__()
        self.fig = plt.figure()
        self.xx = [0]; self.yy = [0]
        self.xx_2 = [0]; self.yy_2 = [0]
        self.xx_3 = [0]; self.yy_3 = [0]
        self.xx_4 = [0]; self.yy_4 = [0]

        self.ax = self.fig.add_subplot(111)
        self.line1, = self.ax.plot(self.xx, self.yy, 'bo-', picker=True, pickradius=5)
        self.line2, = self.ax.plot(self.xx_2, self.yy_2, 'go-', picker=True, pickradius=5)
        self.line3, = self.ax.plot(self.xx_3, self.yy_3, 'mo-', picker=True, pickradius=5)
        self.line4, = self.ax.plot(self.xx_4, self.yy_4, 'ro-', picker=True, pickradius=5)

        binding_id = plt.connect('motion_notify_event', self.on_move)
        plt.connect('button_press_event', self.on_click)
        #fig.canvas.mpl_connect('pick_event', onpick)

        self.flag_plot = 1


        self.stacked_widget = QStackedWidget()
        self.page_0()
        self.page_1()
        self.page_2()
        self.page_3()
        
        self.set_page_by_id(3)
    
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
    
    def page_3(self):
        id = 3
        frame = QFrame()
        layout = QVBoxLayout()
        #layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        self.series = QtCharts.QLineSeries()
        self.series.append(0, 6)
        self.series.append(2, 4)
        self.series.append(3, 8)
        self.series.append(7, 4)
        self.series.append(10, 5)
        self.series.append(QPointF(11, 1))
        self.series.append(QPointF(13, 3))
        self.series.append(QPointF(17, 6))
        self.series.append(QPointF(18, 3))
        self.series.append(QPointF(20, 2))

        self.chart = QtCharts.QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Simple line chart example")

        self._chart_view = QtCharts.QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)
        self._chart_view.show()
        layout.addWidget(self._chart_view)
        
        self.stacked_widget.insertWidget(id, frame)
    
    
    #---------------------------------------------------- plots and signals
    def create_plot(self, gridx, gridy):
        #self.fig.clf()
        #ax = self.fig.add_subplot(111)
        #ax.plot(gridx, gridy, 'g-', gridx.transpose(), gridy.transpose(),'g-')
        #if axis_equal:
            #print("true")
            #ax.axis('equal')
        self.line1.set_xdata(gridx)
        self.line1.set_ydata(gridy)
        self.canvas.draw()
        self.canvas.flush_events()
    
    #------------------------------------------------------ matplotlib drawing functions
    def on_click(self, event):
        if event.button is MouseButton.LEFT:           
            if self.flag_plot == 1:
                boundary_name = "South"
                self.xx.append(event.xdata)
                self.yy.append(event.ydata)
                self.line1.set_xdata(self.xx)
                self.line1.set_ydata(self.yy)
            
            if self.flag_plot == 2:
                boundary_name = "East"
                self.xx_2.append(event.xdata)
                self.yy_2.append(event.ydata)
                self.line2.set_xdata(self.xx_2)
                self.line2.set_ydata(self.yy_2)
             
            if self.flag_plot == 3:
                boundary_name = "North"
                self.xx_3.append(event.xdata)
                self.yy_3.append(event.ydata)
                self.line3.set_xdata(self.xx_3)
                self.line3.set_ydata(self.yy_3)
            
            if self.flag_plot == 4:
                boundary_name = "West"
                self.xx_4.append(event.xdata)
                self.yy_4.append(event.ydata)
                self.line4.set_xdata(self.xx_4)
                self.line4.set_ydata(self.yy_4)

            tuple_1 = (event.xdata, event.ydata, boundary_name)
            self.signal_to_save_data.emit(tuple_1) 
            print("click: ", self.flag_plot)
            self.fig.canvas.draw()
    
    def on_move(self, event):
        #x, y = event.x, event.y
        if event.inaxes:
            ax = event.inaxes  # the axes instance
            print('data coords %f %f' % (event.xdata, event.ydata))