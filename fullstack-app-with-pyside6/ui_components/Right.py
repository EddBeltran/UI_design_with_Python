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
    grid_control_points = Signal(tuple)
    
    def __init__(self):
        super().__init__()

        self.flag_plot = 1

        self.stacked_widget = QStackedWidget()
        self.page_0()
        self.page_1()
        self.page_2()
        
        self.set_page_by_id(0)
    
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

        self.fig_1 = plt.figure()
        self.canvas_1 = FigureCanvas(self.fig_1)
        #self.create_plot(0,0)

        layout.addWidget(self.canvas_1)
        self.stacked_widget.insertWidget(id, frame)
    
    def page_2(self):
        id = 2
        frame = QFrame()
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        self.fig_2 = plt.figure()
        self.canvas_2 = FigureCanvas(self.fig_2)
        self.ax = self.fig_2.add_subplot(111)
        self.ax.axis('equal')
        self.ax.set_title('Dibuja al hacer click')

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

        binding_id = plt.connect('motion_notify_event', self.on_move)
        plt.connect('button_press_event', self.on_click)
        #self.fig.canvas.mpl_connect('pick_event', onpick)

        
        layout.addWidget(self.canvas_2)
        self.stacked_widget.insertWidget(id, frame)
          
    
    #---------------------------------------------------- plots and signals
    def create_plot(self, gridx, gridy): # plot meshgrid
        self.fig_1.clf()
        ax = self.fig_1.add_subplot(111)
        ax.plot(gridx, gridy, 'y-', gridx.transpose(), gridy.transpose(),'y-')
        ax.set_title('Malla estructurada 2D')
        ax.axis('equal')
        self.canvas_1.draw()
        self.canvas_1.flush_events()
    
    #------------------------------------------------------ matplotlib drawing functions
    def on_click(self, event):
        if event.button is MouseButton.LEFT:
            if self.flag_plot == 1:
                index = len(self.xx_1)          
                boundary_name = "South"
                self.xx_1.append(event.xdata)
                self.yy_1.append(event.ydata)
                self.line1.set_xdata(self.xx_1)
                self.line1.set_ydata(self.yy_1)
            
            if self.flag_plot == 2:
                len1 = len(self.xx_1)
                index = len1
                boundary_name = "East"
                if len(self.xx_2) < 1:    
                    self.xx_2.append(self.xx_1[len1-1])
                    self.yy_2.append(self.yy_1[len1-1])

                self.xx_2.append(event.xdata)
                self.yy_2.append(event.ydata)
                self.line2.set_xdata(self.xx_2)
                self.line2.set_ydata(self.yy_2)
             
            if self.flag_plot == 3:
                len2 = len(self.xx_2)
                index = len2
                boundary_name = "North"
                if len(self.xx_3) < 1:    
                    self.xx_3.append(self.xx_2[len2-1])
                    self.yy_3.append(self.yy_2[len2-1])

                self.xx_3.append(event.xdata)
                self.yy_3.append(event.ydata)
                self.line3.set_xdata(self.xx_3)
                self.line3.set_ydata(self.yy_3)
            
            if self.flag_plot == 4:
                len3 = len(self.xx_3)
                index = len3
                boundary_name = "West"
                if len(self.xx_4) < 1:    
                    self.xx_4.append(self.xx_3[len3-1])
                    self.yy_4.append(self.yy_3[len3-1])

                self.xx_4.append(event.xdata)
                self.yy_4.append(event.ydata)
                self.line4.set_xdata(self.xx_4)
                self.line4.set_ydata(self.yy_4)

            tuple_1 = (index, boundary_name, event.xdata, event.ydata)
            self.grid_control_points.emit(tuple_1)
            self.canvas_2.draw()
    
       
    
    def new_mesh(self):
        #Malla con ecuaciones elipticas
        nodos_x, nodos_y = 10, 10 
        itermax = 300
        error = 0.001

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
            newY[0,:] = newY[1,:]   #rigth
            #newY[nodos_x-1,:] = newY[nodos_x-2,:] #left
            
            if t>2:
                err_x = errX[t] - errX[t-1]; err_y = errY[t] - errY[t-1]   
                if err_x<error and err_y<error: break
            X,Y = newX, newY

        #self.line_grid_2.set_xdata(X)
        #self.line_grid_2.set_ydata(Y)
        #self.fig.canvas.draw()

            
            
        #mandamos a pantalla la malla generada
        #plt.title("Malla estructurada generada con EDP elípticas")
        #plt.plot(X,Y,'b-', X.transpose(),Y.transpose(),'b-')
        #plt.axis('equal')
        #plt.show()

        #x_new = np.concatenate((self.xx_1, self.xx_2, self.xx_3, self.xx_4 ), axis=None)
        #y_new = np.concatenate((self.yy_1, self.yy_2, self.yy_3, self.yy_4 ), axis=None)
        #tuple_1 = (x_new, y_new)
        #self.signal_to_save_data.emit(tuple_1)
        

    
    def on_move(self, event):
        #x, y = event.x, event.y
        if event.inaxes:
            ax = event.inaxes  # the axes instance
            #print('data coords %f %f' % (event.xdata, event.ydata))