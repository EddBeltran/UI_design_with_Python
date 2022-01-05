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
        self.xx_1 = []; self.yy_1 = []
        self.xx_2 = []; self.yy_2 = []
        self.xx_3 = []; self.yy_3 = []
        self.xx_4 = []; self.yy_4 = []
        self.gridx = []; self.gridy = [] 
        self.gridx_2 = []; self.gridy_2 = []

        self.malla_x, self.malla_y = np.zeros((10, 10)), np.zeros((10, 10))
         

        self.ax = self.fig.add_subplot(111)

        self.line1, = self.ax.plot(self.xx_1, self.yy_1, 'go-', picker=True, pickradius=5)
        self.line2, = self.ax.plot(self.xx_2, self.yy_2, 'bo-', picker=True, pickradius=5)
        self.line3, = self.ax.plot(self.xx_3, self.yy_3, 'mo-', picker=True, pickradius=5)
        self.line4, = self.ax.plot(self.xx_4, self.yy_4, 'ro-', picker=True, pickradius=5)
        self.line_grid, = self.ax.plot(self.gridy, self.gridy, 'yo', picker=True, pickradius=5)
        self.line_grid_2, = self.ax.plot(self.gridy_2, self.gridy_2, 'ko', picker=True, pickradius=5)
        

        binding_id = plt.connect('motion_notify_event', self.on_move)
        plt.connect('button_press_event', self.on_click)
        #fig.canvas.mpl_connect('pick_event', onpick)

        self.flag_plot = 1


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
                    self.xx_1.pop(len1-1)
                    self.yy_1.pop(len1-1)

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
                    self.xx_2.pop(len2-1)
                    self.yy_2.pop(len2-1)

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
                    self.xx_3.pop(len3-1)
                    self.yy_3.pop(len3-1)

                self.xx_4.append(event.xdata)
                self.yy_4.append(event.ydata)
                self.line4.set_xdata(self.xx_4)
                self.line4.set_ydata(self.yy_4)

            tuple_1 = (index, boundary_name, event.xdata, event.ydata)
            self.signal_to_save_data.emit(tuple_1)
            self.fig.canvas.draw()
    
    def join_boundaries(self):
        self.xx_4.append(self.xx_1[0])
        self.yy_4.append(self.yy_1[0])
        x = np.concatenate((self.xx_1, self.xx_2, self.xx_3, self.xx_4), axis=None)
        y = np.concatenate((self.yy_1, self.yy_2, self.yy_3, self.yy_4), axis=None)

        nodos_x = 10
        nodos_y = 10

        xi, eta = np.zeros(nodos_x), np.zeros(nodos_y)
        frontera_norte_x, frontera_sur_x, frontera_norte_y, frontera_sur_y  = np.zeros(nodos_x), np.zeros(nodos_x), np.zeros(nodos_x), np.zeros(nodos_x)
        frontera_este_x, frontera_oeste_x, frontera_este_y, frontera_oeste_y  = np.zeros(nodos_y), np.zeros(nodos_y), np.zeros(nodos_y), np.zeros(nodos_y)
        
        ##------- Asignación de las Fronteras para x e y --------#
        for i in range (0, nodos_x):
            frontera_sur_x[i] = x[i]
            frontera_sur_y[i] = y[i]
        #
            frontera_norte_x[i] = x[nodos_x + nodos_y + nodos_x-1-(i+2)]
            frontera_norte_y[i] = y[nodos_x + nodos_y + nodos_x-1-(i+2)]
        #
        for i in range (0, nodos_y):
            frontera_este_x[i] = x[nodos_x + i-1]
            frontera_este_y[i] = y[nodos_x + i-1]
        #    
            frontera_oeste_x[i] = x[(2*nodos_x + 2*nodos_y-2)-(i+2)]
            frontera_oeste_y[i] = y[2*nodos_x + 2*nodos_y-2-(i+2)]
    
        #  Calculo de xi e eta --> paramentros necesarios para hacer el cambio de coordenadas -----------#
        d_xi=1.0E+00/(nodos_x-1)
        for i in range (1, nodos_x):
            xi[i]=d_xi*(i)
    
        d_eta=1.0E+00/(nodos_y-1)
        for i in range (1, nodos_y):
            eta[i]=d_eta*(i)
        
        # Generacion de los puntos internos de la malla   
        for i in range (1, nodos_x-1):
            for j in range (1, nodos_y-1):
                self.malla_x[i][j]=((1.0E+00-eta[j])*frontera_sur_x[i]+eta[j]*frontera_norte_x[i]+
                             (1.0E+00-xi[i])*frontera_oeste_x[j]+xi[i]*frontera_este_x[j]-
                             (xi[i]*eta[j]*frontera_norte_x[nodos_x-1]+xi[i]*(1.0E+00-eta[j])*frontera_sur_x[nodos_x-1]+
                             eta[j]*(1.0E+00-xi[i])*frontera_norte_x[0]+
                             (1.0E+00-xi[i])*(1.0E+00-eta[j])*frontera_sur_x[0]))
                
                self.malla_y[i][j]=((1.0E+00-eta[j])*frontera_sur_y[i]+eta[j]*frontera_norte_y[i]+
                             (1.0E+00-xi[i])*frontera_oeste_y[j]+xi[i]*frontera_este_y[j]-
                             (xi[i]*eta[j]*frontera_norte_y[nodos_x-1]+xi[i]*(1.0E+00-eta[j])*frontera_sur_y[nodos_x-1]+
                             eta[j]*(1.0E+00-xi[i])*frontera_norte_y[0]+
                             (1.0E+00-xi[i])*(1.0E+00-eta[j])*frontera_sur_y[0]))
        
        #---  Asignación de los limites de la geometria en las fronteras ---#
        for i in range (0, nodos_x):
            self.malla_x[i][0] = frontera_sur_x[i]    #  Frontera Sur
            self.malla_y[i][0] = frontera_sur_y[i]    #  Frontera Sur
            
            self.malla_x[i][nodos_y-1] = frontera_norte_x[i]  #  Frontera Norte
            self.malla_y[i][nodos_y-1] = frontera_norte_y[i]  #  Frontera Norte
        
        for i in range(1, nodos_y-1):
            self.malla_x[0][i] = frontera_oeste_x[i]        #  Frontera Oeste
            self.malla_y[0][i] = frontera_oeste_y[i]        # Frontera Oeste
    
            self.malla_x[nodos_x-1][i] = frontera_este_x[i]   #  Frontera Este
            self.malla_y[nodos_x-1][i] = frontera_este_y[i]   # Frontera Este
        
        self.line_grid.set_xdata(self.malla_x)
        self.line_grid.set_ydata(self.malla_y)
        self.fig.canvas.draw()
        
    
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

        self.line_grid_2.set_xdata(X)
        self.line_grid_2.set_ydata(Y)
        self.fig.canvas.draw()

            
            
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