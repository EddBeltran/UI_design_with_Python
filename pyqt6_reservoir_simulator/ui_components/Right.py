from PySide6 import QtCharts
from PySide6.QtCore import *
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  
import matplotlib.pyplot as plt
import numpy as np
#import PySide6.QtCharts


class RightWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.fig = plt.figure()
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
    
    def mousePressEvent(self, e):        
        if e.button() == Qt.MouseButton.LeftButton:
            self.etiqueta.setText("Click...")
    
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