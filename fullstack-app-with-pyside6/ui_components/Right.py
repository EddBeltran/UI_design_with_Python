from PySide6 import QtCharts
from PySide6.QtCore import *
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas  
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backend_bases import MouseButton
import ui_functions as functions
#import PySide6.QtCharts


class RightWidgets(QWidget):
    grid_control_points = Signal(tuple)
    
    def __init__(self):
        super().__init__()
        # variables
        self.flag_plot = 1
        self.control_point_index = 0
        self.brush_tool = 1 #1-polygon, 2-bezierCurve
        # render pages
        self.stacked_widget = QStackedWidget()
        self.page_0()
        self.page_1()
        self.set_page_by_id(0)
    
    def set_page_by_id(self, id):
        self.stacked_widget.setCurrentIndex(id)     
    
    #------------------------------------------------------- pages
    def page_0(self):
        id = 0
        frame = QFrame()
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)
        self.fig_1 = plt.figure()
        self.canvas_1 = FigureCanvas(self.fig_1)
        ax = self.fig_1.add_subplot(111)     
        ax.set_title('Malla sencilla 2D')
        ax.axis('equal')
        self.canvas_1.draw()
        layout.addWidget(self.canvas_1)
        self.stacked_widget.insertWidget(id, frame)
    
    def page_1(self):
        id = 1
        frame = QFrame()
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)
        self.fig_2 = plt.figure()
        self.canvas_2 = FigureCanvas(self.fig_2)
        self.set_drawing_workspace()

        binding_id = plt.connect('motion_notify_event', self.on_move)
        plt.connect('button_press_event', self.on_click)
        #self.fig.canvas.mpl_connect('pick_event', onpick)
        layout.addWidget(self.canvas_2)
        self.stacked_widget.insertWidget(id, frame)
    

    #---------------------------------------------------- plots from matplotlib
    def create_regular_meshgrid(self, gridx, gridy):
        self.fig_1.clf()
        ax = self.fig_1.add_subplot(111)
        ax.plot(gridx, gridy, 'g.-', gridx.transpose(), gridy.transpose(),'g.-')      
        ax.set_title('Malla sencilla 2D')
        ax.axis('equal')
        self.canvas_1.draw()
        self.canvas_1.flush_events()

    def set_drawing_workspace(self, lim_x=100, lim_y=100):
        self.fig_2.clf()
        self.ax = self.fig_2.add_subplot(111)
        self.ax.axis('equal')
        self.ax.set_title('Dibuja al hacer click')
        self.ax.set_xlim(0, lim_x)
        self.ax.set_ylim(0, lim_y)

        self.xx_1 = []; self.yy_1 = []
        self.xx_2 = []; self.yy_2 = []
        self.xx_3 = []; self.yy_3 = []
        self.xx_4 = []; self.yy_4 = []
        self.gridx = []; self.gridy = [] 
        self.gridx_2 = []; self.gridy_2 = []
        self.line1, = self.ax.plot(self.xx_1, self.yy_1, 'go-', picker=True, pickradius=5)
        self.line2, = self.ax.plot(self.xx_2, self.yy_2, 'bo-', picker=True, pickradius=5)
        self.line3, = self.ax.plot(self.xx_3, self.yy_3, 'mo-', picker=True, pickradius=5)
        self.line4, = self.ax.plot(self.xx_4, self.yy_4, 'ro-', picker=True, pickradius=5)
        self.line_grid, = self.ax.plot(self.gridy, self.gridy, 'yo', picker=True, pickradius=5)
        self.line_grid_2, = self.ax.plot(self.gridy_2, self.gridy_2, 'ko', picker=True, pickradius=5)
        self.canvas_2.draw()
        self.canvas_2.flush_events()
    
    def create_irregular_meshgrid(self, gridx, gridy):
        self.fig_2.clf()
        self.ax = self.fig_2.add_subplot(111)
        self.ax.plot(gridx, gridy, 'c.-', gridx.transpose(), gridy.transpose(),'c.-')      
        self.ax.set_title('Malla irregular 2D')
        self.ax.axis('equal')
        self.canvas_2.draw()
        self.canvas_2.flush_events()

    
    #------------------------------------------------------ mouse interactions with matplotlib
    def on_move(self, event):
        if event.inaxes:
            ax = event.inaxes
            #if len( self.xx_1) > 2:
            #    #x, y = functions.interp_curva_bezier([self.xx_1[0], self.xx_1[1], event.xdata], [self.yy_1[0], self.yy_1[1], event.ydata], 20, ultimo_punto=True)
            #    x, y = functions.interp_cuadratic_bezier([self.xx_1[0], self.xx_1[1], event.xdata], [self.yy_1[0], self.yy_1[1], event.ydata], 20, ultimo_punto=True)
            #    self.line_grid.set_xdata(x)
            #    self.line_grid.set_ydata(y)
            #    self.canvas_2.draw()


    
    #def on_release(self, event):
    #    if event.button is MouseButton.LEFT and self.brush_tool == 2:
    #        print("released")

    def on_click(self, event):
        if event.button is MouseButton.LEFT:
            if self.flag_plot == 1:         
                boundary_name = "South"
                self.xx_1.append(event.xdata)
                self.yy_1.append(event.ydata)
                self.line1.set_xdata(self.xx_1)
                self.line1.set_ydata(self.yy_1)
            
            if self.flag_plot == 2:
                boundary_name = "East"
                if len(self.xx_2) < 1:    
                    self.xx_2.append(self.xx_1[len(self.xx_1) - 1])
                    self.yy_2.append(self.yy_1[len(self.yy_1) - 1])

                self.xx_2.append(event.xdata)
                self.yy_2.append(event.ydata)
                self.line2.set_xdata(self.xx_2)
                self.line2.set_ydata(self.yy_2)
             
            if self.flag_plot == 3:
                boundary_name = "North"
                if len(self.xx_3) < 1:    
                    self.xx_3.append(self.xx_2[len(self.xx_2) - 1])
                    self.yy_3.append(self.yy_2[len(self.yy_2) - 1])

                self.xx_3.append(event.xdata)
                self.yy_3.append(event.ydata)
                self.line3.set_xdata(self.xx_3)
                self.line3.set_ydata(self.yy_3)
            
            if self.flag_plot == 4:
                boundary_name = "West"
                if len(self.xx_4) < 1:    
                    self.xx_4.append(self.xx_3[len(self.xx_3) - 1])
                    self.yy_4.append(self.yy_3[len(self.yy_3) - 1])

                self.xx_4.append(event.xdata)
                self.yy_4.append(event.ydata)
                self.line4.set_xdata(self.xx_4)
                self.line4.set_ydata(self.yy_4)
            
            send_data = (event.xdata, event.ydata, boundary_name, self.control_point_index)
            self.grid_control_points.emit( send_data )
            self.control_point_index += 1
            self.canvas_2.draw()







            
    def new_mesh(self):
        nodos_x, nodos_y = 10, 10 
        itermax = 800
        error = 0.0001

        alpha, beta, gamma = np.zeros((nodos_x,nodos_y)), np.zeros((nodos_x,nodos_y)), np.zeros((nodos_x,nodos_y))
        X, Y= np.zeros((nodos_x,nodos_y)), np.zeros((nodos_x,nodos_y))
        errX, errY = np.ones(itermax), np.ones(itermax)
        
        X, Y = self.malla_x, self.malla_y        
        newX = X; newY = Y
        #-------------------------------------Inicia el método iterativo-------------|
        for t in range (1, itermax):
            for i in range(1, nodos_x-1):
                for j in range(1, nodos_y-1):
                    alpha[i,j] = (1/4)*((X[i,j+1]-X[i,j-1])**2 + (Y[i,j+1] - Y[i,j-1])**2)
                    beta[i,j]  = (1/16)*((X[i+1,j]-X[i-1,j])*(X[i,j+1]-X[i,j-1]) + (Y[i+1,j] - Y[i-1,j])*(Y[i,j+1] - Y[i,j-1]))
                    gamma[i,j] = (1/4)*((X[i+1,j]-X[i-1,j])**2 + (Y[i+1,j] - Y[i-1,j])**2)
                    
                    newX[i,j] = ((-0.5)/(alpha[i,j] + gamma[i,j]+10e-9))*(2*beta[i,j]*(X[i+1,j+1] - X[i-1,j+1] - X[i+1,j-1] + X[i-1,j-1]) - alpha[i,j]*(X[i+1,j]+X[i-1,j]) - gamma[i,j]*(X[i,j+1]+X[i,j-1]))
                    newY[i,j] = ((-0.5)/(alpha[i,j] + gamma[i,j]+10e-9))*(2*beta[i,j]*(Y[i+1,j+1] - Y[i-1,j+1] - Y[i+1,j-1] + Y[i-1,j-1]) - alpha[i,j]*(Y[i+1,j]+Y[i-1,j]) - gamma[i,j]*(Y[i,j+1]+Y[i,j-1]))
           
            #calculamos el error
            errX[t] = np.linalg.norm(newX)
            errY[t] = np.linalg.norm(newY)
            
            #Neuman BC
            newX[0,:] = X[1,:]   #rigth
            newX[nodos_x-1, :] = X[nodos_x-1, :] #left
            newX[:, nodos_y-1] = X[:, nodos_y-1]   #top
            newX[:, 0] = X[:, 0] #bottom

            newY[0,:] = Y[1,:]   #rigth
            newY[nodos_x-1, :] = Y[nodos_x-1, :] #left
            newY[:, nodos_y-1] = Y[:, nodos_y-1]   #top
            newY[:, 0] = Y[:, 0] #bottom
            
            if t>2:
                err_x = errX[t] - errX[t-1]; err_y = errY[t] - errY[t-1]   
                if err_x<error and err_y<error: break
            X,Y = newX, newY