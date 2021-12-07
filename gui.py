#--- Librerias de la interfaz
import sys
from PyQt5.QtWidgets import QWidget,QHBoxLayout, QTableWidget,QTableWidgetItem, QProgressBar, QApplication,QGridLayout, QPushButton, QLabel, QFileDialog, QLineEdit,QCheckBox, QSlider,QRadioButton,QComboBox #,, QStatusBar,QProgressBar,QGraphicsView, QGraphicsScene
import pyqtgraph as pg
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(10, 10, 900, 600)
        self.setWindowTitle("HYBRID SIMULATOR")
        self.setWindowIcon(QIcon('gui/iconos/icono_2.ico'))
        
        self.layout=QGridLayout()
        self.setLayout(self.layout)
        self.layout.setVerticalSpacing(0)
        self.layout.setHorizontalSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        
        #--------------------------------------------------------------------//
        #-------------------------------------------------------LEFT PANEL---//
        self.btn_1 = QPushButton("File Options  +",self)
        self.layout.addWidget(self.btn_1,0, 0, 1, 1)
        self.btn_1.setStyleSheet(bt_style)
        
        self.btn_2 = QPushButton("  Grid",self)
        self.layout.addWidget(self.btn_2,1, 0, 1, 1)
        self.btn_2.setStyleSheet(bt_style)
        self.btn_2.setIcon(QIcon('gui/iconos/grid.png'))
        self.btn_2.clicked.connect(self.show_new_window)
          
        self.btn_3 = QPushButton("  Reservoir Properties",self)
        self.layout.addWidget(self.btn_3,2, 0, 1, 1)
        self.btn_3.setStyleSheet(bt_style)
        self.btn_3.setIcon(QIcon('gui/iconos/roca.png'))
        self.btn_3.clicked.connect(self.show_new_window)
           
        self.btn_4 = QPushButton("  PVT Data",self)
        self.layout.addWidget(self.btn_4,3, 0, 1, 1)
        self.btn_4.setStyleSheet(bt_style)
        self.btn_4.setIcon(QIcon('gui/iconos/pvt.png'))
        self.btn_4.clicked.connect(self.show_new_window)
        
        self.btn_5 = QPushButton("  Permeability Curves",self)
        self.layout.addWidget(self.btn_5,4, 0, 1, 1)
        self.btn_5.setStyleSheet(bt_style)
        self.btn_5.setIcon(QIcon('gui/iconos/kr_2.png'))
        self.btn_5.clicked.connect(self.show_new_window)
               
        self.btn_7 = QPushButton("  Solver",self)
        self.layout.addWidget(self.btn_7,5, 0, 1, 1)
        self.btn_7.setStyleSheet(bt_style)
        self.btn_7.setIcon(QIcon('gui/iconos/math.png'))
        self.btn_7.clicked.connect(self.show_new_window)
        
        self.btn_8 = QPushButton("  Wells",self)
        self.layout.addWidget(self.btn_8,6, 0, 1, 1)
        self.btn_8.setStyleSheet(bt_style)
        self.btn_8.setIcon(QIcon('gui/iconos/well.png'))
        self.btn_8.clicked.connect(self.show_new_window)
        
        self.lbl_1 = QLabel(".",self)
        self.layout.addWidget(self.lbl_1,7, 0, 1, 1)
        self.lbl_1.setStyleSheet(bt_style3)
        
        self.lbl_2 = QLabel("..",self)
        self.layout.addWidget(self.lbl_2,8, 0, 1, 1)
        self.lbl_2.setStyleSheet(bt_style3)
        
        #--------------------------------------------------------------------//
        #-------------------------------------------------------TOP LAYOUT---//
        self.layout_top=QGridLayout()
        self.layout.addLayout(self.layout_top,0, 1, 1, 3)
        
        #---------
        self.btn_a = QPushButton(self)
        self.layout_top.addWidget(self.btn_a,0, 0, 1, 1)
        self.btn_a.setIcon(QIcon('gui/iconos/vista1.png'))
        
        self.btn_a = QPushButton(self)
        self.layout_top.addWidget(self.btn_a,0, 1, 1, 1)
        self.btn_a.setIcon(QIcon('gui/iconos/vista2.png'))
        
        self.btn_a = QPushButton(self)
        self.layout_top.addWidget(self.btn_a,0, 2, 1, 1)
        self.btn_a.setIcon(QIcon('gui/iconos/vista3.png'))
        
        self.combo_plot = QComboBox(self)
        self.layout_top.addWidget(self.combo_plot,0, 3, 1, 1)
        
        self.combo_plot.addItem("HYBRID-IMPES")
        self.combo_plot.addItem("IMPES")
        
        
        self.btn_run = QPushButton("RUN",self)
        self.layout_top.addWidget(self.btn_run,0, 4, 1, 1)
        self.btn_run.clicked.connect(self.onButtonClick)
        
        #------------
        self.progress = QProgressBar(self)
        self.layout_top.addWidget(self.progress,1, 0, 1, 5)
        self.progress.setMaximum(100)
        self.progress.setTextVisible(False)
        self.progress.setStyleSheet(styles.progress_bar)

        
        
        #----------------------------------------------------------------------
        #------------------------------------------------------PLOT-LAYOUT---//  
        self.layout_plot=QGridLayout()
        self.layout.addLayout(self.layout_plot,1, 1, 8, 3)
        
        self.tableWidget = QTableWidget()
        self.layout_plot.addWidget(self.tableWidget,0, 0, 2, 2, alignment=QtCore.Qt.AlignCenter)
        
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        
        self.btn_x = QPushButton("Create New Project",self)
        self.btn_y = QPushButton("Open Project",self)
        self.btn_z = QPushButton("Edit an Example",self)
        self.btn_z.clicked.connect(self.load_data)
        
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setCellWidget(0, 0, self.btn_x)
        self.tableWidget.setCellWidget(1, 0, self.btn_y)
        self.tableWidget.setCellWidget(2, 0, self.btn_z)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(True)
        


        #--------------------------------------------------------------------//
        #-------------------------------------------------------MATPLOTLIB---//
        self.fig1 = plt.figure(figsize=(5, 4), facecolor="#F4F4F4", tight_layout=True)
        self.canvas1 = FigureCanvas(self.fig1)
        self.layout_plot.addWidget(self.canvas1, 0, 0, 1, 1)             
        self.canvas1.hide()

                
        self.canvas2 = FigureCanvas(plt.Figure(figsize=(5, 4), facecolor="#F4F4F4", tight_layout=True))
        self.layout_plot.addWidget(self.canvas2, 0, 1, 1, 1)
        self.ax2 = self.canvas2.figure.subplots()
        self.canvas2.hide()
        
        self.fig3 = plt.figure(figsize=(5, 4), facecolor="#F4F4F4", tight_layout=True)
        self.canvas3 = FigureCanvas(self.fig3)
        self.layout_plot.addWidget(self.canvas3, 1, 0, 1, 1)     
        self.canvas3.hide()
        
        self.fig4 = plt.figure(figsize=(5, 4), facecolor="#F4F4F4", tight_layout=True)
        self.canvas4 = FigureCanvas(self.fig4)
        self.layout_plot.addWidget(self.canvas4, 1, 1, 1, 1)     
        self.canvas4.hide()
        
        self.vel = None
        
       
        #----------------------------------------------------------------------
        #-------------------------------------------------------SIGNALS------//
        self.grid_window = GRID_WINDOW(self)  
        self.grid_window.signal_grid.connect(self.plot_grid)
        self.grid_window.signal_btn_tool.connect(self.choose_tool)
        #self.grid_window.signal_NX_NY.connect(self.POLI_POINTS)
        
        self.properties_window = PROPERTIES_WINDOW(self)  
        self.properties_window.signal_properties.connect(self.plot_properties)
        
        self.krcurves_window = KRCURVES_WINDOW(self)  
        self.krcurves_window.signal_krcurves.connect(self.plot_krcurves)
        
        self.pvt_window = PVT_WINDOW(self)

        self.solver_window = SOLVER_WINDOW(self)
        
        self.wells_window = WELLS_WINDOW(self)
        self.wells_window.signal_well.connect(self.plot_wells)
        
        
        #--------------------------------------------------------------------//
        #-------------------------------------------------------VARIABLES----//
        self.flag = 0
        self.flag_well = 0
        
        self.data_points = None
        self.data_points_border = None
        self.data_points_curva = None
        
        self.create_plot()
        
        global j,x,y,a,b,x_poli,y_poli
        j=0
        self.flag = 2
        self.value = 0
        self.val = 0
        self.flag2=0
        self.flag_3=0
        self.mesh_run_CC = 0
        x=[]; y=[]
        x_poli = []; y_poli = []
        self.curva_val  = 35
        self.count = []
        
        
        self.show()



#-------------------------------------------------------------------------------------------
    def load_data(self):
        self.tableWidget.hide()
        #-------------------- set GRID
        df = pd.read_excel('input/database.xlsx', sheet_name='GRID')
        gridx = df["GRIDX"]
        gridy = df["GRIDY"]
        
        #---------------------------------------------- GRID values
        df = pd.read_excel('input/database.xlsx', sheet_name='GENERAL')       
        nx = int(df.at[0, "VALUE"])
        ny = int(df.at[1, "VALUE"])
        lx = float(df.at[2, "VALUE"])
        ly = float(df.at[3, "VALUE"])

        self.grid_window.txt_lx.setText(str(lx))
        self.grid_window.txt_ly.setText(str(ly))
        self.grid_window.txt_nx.setText(str(nx))
        self.grid_window.txt_ny.setText(str(ny))
        
        #----------------------------------------------- RESERVOIR values
        absPermX = float(df.at[7, "VALUE"])
        absPermY = float(df.at[8, "VALUE"])
        porosity = float(df.at[9, "VALUE"])
        
        self.properties_window.txt_abKx.setText(str(absPermX))
        self.properties_window.txt_abKy.setText(str(absPermY))
        self.properties_window.txt_porosity.setText(str(porosity))
        
        #----------------------------------------------- KR CURVES values
        for i in range(0,6):
            val = float(df.at[18+i, "VALUE"])
            self.krcurves_window.tableWidget.setItem(i,1, QTableWidgetItem(str(val)))
            
        #------------------------------------------------------- PVT values
        for i in range(0,8):
            if (i !=5 or i != 6 ):
                val = float(df.at[27+i, "VALUE"])
                self.pvt_window.tableWidget.setItem(i+1,1, QTableWidgetItem(str(val)))
            else:
                val = 0

        #------------------------------------------------------- SOLVER values
        self.tot_time = int(df.at[36, "VALUE"]) 
        
        for i in range(0,9):
            val = float(df.at[36+i, "VALUE"])
            self.solver_window.tableWidget.setItem(i,1, QTableWidgetItem(str(val)))
                
        
        #----------------------------------------------------------------------
        #-------------------------------------------------------------plot Grid & wells
        self.gridx, self.gridy  = grid2.LISTtoARR(gridx, gridy, nx, ny)
        self.plot_grid(self.gridx, self.gridy, nx, ny)

        #----------------------------------------------------------GENERATE GRID CENTERS
        self.cent_x, self.cent_y = grid2.gridCenters2(self.gridx, self.gridy, nx, ny)
        
        
     
        
        
    def plot_wells(self):
        df = pd.read_excel('input/database.xlsx', sheet_name='GENERAL')       
        nx = int(df.at[0, "VALUE"])
        ny = int(df.at[1, "VALUE"])
        self.plot_grid(self.gridx, self.gridy, nx, ny)
        
        


#-------------------------------------------------------------------------------------------            
    def onButtonClick(self):
        algorithm = self.combo_plot.currentText()
        if algorithm=="HYBRID-IMPES":
            print("HYBRID-IMPES")
            import a_hybrid.main_class as SIMU
        else:
            import a_impes.main_class as SIMU
            print("IMPES")

        self.calc = SIMU.External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.plotChanged.connect(self.onplotChanged)
        self.calc.start()
        
    def onCountChanged(self, val):
        self.progress.setValue(val)
    
    def onplotChanged(self, count, Sw_k, Po_k, uw_x, uw_y, days, Qo, Qw): # IN HYBRID ADD--> days, Qo, Qw
        #---------------------------------- PLOT 1
        #--------------------------------------PLOT 3
        self.layout_plot.addWidget(self.canvas1, 0, 0, 1, 1)  
        self.canvas1.show()
        self.fig1.clf()
        ax1 = self.fig1.add_subplot(111)
        sat = ax1.contourf(self.cent_x, self.cent_y, Sw_k, 10, alpha=.9, cmap=plt.cm.viridis)#Spectral , viridis, cividis, inferno, 
        ax1.axis('equal')
        t_simu = (count*self.tot_time)/100
        stringSat = 'Saturacion %s dias' %str(t_simu)
        ax1.set_title(stringSat)
        ax1.set_xlabel('x [m]')
        ax1.set_ylabel('y [m]')
        self.fig1.colorbar(sat, ax=ax1)
        self.canvas1.draw()
        
        #self.fig1.colorbar(sat, ax=ax1)
        # sat = ax1.plot(self.x_prod,self.y_prod,'ko')
        # sat = ax1.plot(self.x_inj,self.y_inj,'kv')
        

        # for i in range(0,len(self.x_prod)):
        #     text = "  Producer" + str(i+1)
        #     sat = ax1.annotate(text, (self.x_prod[i], self.y_prod[i]), color='k')
        
        # for i in range(0,len(self.x_inj)):
        #     text = "  Injector" + str(i+1)
        #     sat = ax1.annotate(text, (self.x_inj[i], self.y_inj[i]), color='k')    
        
        #self.canvas1.draw()
        
        #--------------------------------------PLOT 2
        self.canvas3.show()
        self.fig3.clf()
        ax3 = self.fig3.add_subplot(111)
        press = ax3.contourf(self.cent_x, self.cent_y, Po_k, 10, alpha=.9, cmap=plt.cm.viridis)
        ax3.axis('equal')
        ax3.set_title('Presión')
        ax3.set_xlabel('x [m]')
        ax3.set_ylabel('y [m]')
        self.fig3.colorbar(press, ax=ax3)
        self.canvas3.draw()

        #--------------------------------------PLOT 3
        self.canvas2.show()
        self.ax2.clear()
        self.vel = self.ax2.quiver(self.cent_x, self.cent_y, uw_x, uw_y, linewidth=0.5, color='b')
        self.ax2.axis('equal')
        self.ax2.set_title('Campo vectorial de velocidad')
        self.ax2.set_xlabel('x [m]')
        self.ax2.set_ylabel('y [m]')
        self.canvas2.draw()
        
        #--------------------------------------PLOT 4
        self.canvas4.show()
        self.fig4.clf()
        ax4 = self.fig4.add_subplot(111)
        fluids = ax4.plot(days, Qo, 'g-')
        fluids = ax4.plot(days, Qw, 'b-')
        ax4.set_title('Producing well 1')
        ax4.set_xlabel('days')
        ax4.set_ylabel('Qo')
        self.canvas4.draw()
        

    def show_new_window(self):
        btn_ID = ((self.sender()).text())
        if (btn_ID == '  Grid'):     self.grid_window.show()
        if (btn_ID == '  Reservoir Properties'):  self.properties_window.show()
        if (btn_ID == '  Permeability Curves'):   self.krcurves_window.show()
        if (btn_ID == '  PVT Data'):  self.pvt_window.show()
        if (btn_ID == '  Solver'):    self.solver_window.show()
        if (btn_ID == '  Wells'):     self.wells_window.show()
            
            
            
            
         
            
            



    def create_plot(self):
        global x,y,x_poli,y_poli,j
        
        self.my_plot = pg.PlotWidget()
        self.layout_plot.addWidget(self.my_plot,0, 0, 2, 2)
        
        lsx=float(1000); lsy=float(1000); ss1=[lsy,0,0];  ss2=[0,0,lsx]
        self.data_points_border = self.my_plot.plot(ss1, ss2, pen='w', symbol=None)
        self.data_points = self.my_plot.plot(pen=('#208ce4fd'), symbol='o', symbolBrush =('#ff8000ff'),symbolPen=None, symbolSize=7)                                          
        
        self.my_plot.setBackground('#303030')
        self.my_plot.setAspectLocked()
        self.my_plot.showGrid(x=True, y=True)
        self.my_plot.scene().sigMouseMoved.connect(self.mouseMoved)
        
        self.my_plot.hide()
        
    
    def choose_tool(self, signal, a, b, c):
        global x_poli, y_poli
        if signal == 1:
            self.NX = a
            self.NY = b
            self.flag = signal
            self.canvas1.hide()
            self.my_plot.show()
        
        if signal == 4: #CLEAR DATA
            self.canvas1.hide(); self.my_plot.show()
            x_poli.clear(); y_poli.clear()
            self.data_points.setData(x_poli, y_poli)
        
        if signal == 5: #UPDATE
            self.NX = a
            self.NY = b
            self.POLI_POINTS()
            
        if signal == 6: #IMAGE
            self.canvas1.hide(); self.my_plot.show()
            self.imagePath = a
            len_x = b
            len_y = c
            
            
            self.pixmap = QPixmap(self.imagePath)
            self.img = pg.QtGui.QGraphicsPixmapItem(self.pixmap)       
            self.my_plot.addItem(self.img)       
            self.img.scale(1, -1)
            
            self.w_pix=(self.pixmap.width())
            self.h_pix=(self.pixmap.height())
            self.img.setOffset(0, -(self.h_pix))        
            self.img.setTransformationMode(Qt.SmoothTransformation)
            self.img.setOpacity(0.15)
            
            x1=(len_x/self.w_pix);   y1=(len_y/self.h_pix)
            self.img.scale(x1, y1)
            #self.w_pix=lsx;   self.h_pix=lsy
            self.img.setTransformationMode(Qt.SmoothTransformation)

        
        




    #------------------------------------------------------------------------//
    #------------------------------------------------------------------------//
    #-------------------------------------------------MOUSE FUNCTIONS -------//
    def mouseMoved(self, point):
        global x_poli,y_poli,j,x1,y1,x,y
        
        if self.flag==1: # POLIGONO            
            self.position = self.my_plot.plotItem.vb.mapSceneToView(point)
            
        if self.flag==2: #CURVA BEZIER
            self.position = self.my_plot.plotItem.vb.mapSceneToView(point)
            x_poli[j] = self.position.x()
            y_poli[j] = self.position.y()
            a=[0,0]; b=[0,0]
            
            if j > 0:
                self.CURVA_PLOT()    
            if j % 2 != 0:
                a[0]=x_poli[j-1]
                b[0]=y_poli[j-1]
                a[1]=x_poli[j]
                b[1]=y_poli[j]
                self.data_points.setData(a, b, pen=('#208ce4fd'), symbol='o', symbolBrush =('#ff8000ff'))
                  
    
    #-------------------------------------------------------------- funcion CLICK
    def mousePressEvent(self, ev):
        global x,y,j,x_poli,y_poli
            
        if ev.button() == QtCore.Qt.LeftButton and self.flag==1: #POLIGONO
            x_poli.append(self.position.x())
            y_poli.append(self.position.y())
            self.data_points.setData(x_poli, y_poli)
            j = j + 1
            
        #if ev.button() == QtCore.Qt.LeftButton and self.flag==2: #CURVA
            #x_poli.append(self.position.x())
            #y_poli.append(self.position.y())
            #self.data_points.setData(x_poli, y_poli, pen=None,symbol='o',symbolBrush=None)
            #j=j+1


    ####################################################################### GENERAR PUNTOS INTERMEDIOS

    def CURVA_PLOT(self):
        global x,y,x_poli,y_poli,j
        x=[]
        y=[]
        u=0.5
        if self.flag2==2:
            delta=0.095-(float(self.curva_val)/1000)

        if self.flag2 != 2:
            delta = 0.045 - (float(self.curva_val) / 1000)

        for k in range(2,j+1,2):
            t=0
            x2= (1/(2*(1-u)*u))*x_poli[k-1] -((1-u)/(2*u))*x_poli[k-2] -(u/(2*(1-u)))*x_poli[k]
            y2= (1/(2*(1-u)*u))*y_poli[k-1] -((1-u)/(2*u))*y_poli[k-2] -(u/(2*(1-u)))*y_poli[k]
            while t<1:
                xs = (1-t)**2 * x_poli[k-2] + 2*(1-t)*t*x2 + t**2*x_poli[k]
                ys = (1-t)**2 * y_poli[k-2] + 2*(1-t)*t*y2 + t**2*y_poli[k]
                x.append(xs); y.append(ys);
                t=t+delta
            self.data_points_curva.setData(x, y,symbolPen=None, symbolSize = 3)
                       
    def POLI_POINTS(self):
        global x_poli,y_poli,j
        
        if self.mesh_run_CC == 1:
            self.xf,self.yf = grid2.POLI_POINTS(x_poli,y_poli, self.NX)
            self.data_points.setData(self.xf,self.yf, pen=('#208ce4fd'), symbol='o', symbolBrush=('#ff8000ff'),symbolSize=4)
            save.SAVE_2COLUMS_XLSX('input/database.xlsx', 'GRID_PERIMETER', 'POINTSX', self.xf, 'POINTSY', self.yf)
        
        else:
            df = pd.read_excel('input/database.xlsx', sheet_name='GRID_CONTROL_POINTS')
            x_control = df["X_CONT"]
            y_control = df["Y_CONT"]
            xf, yf = grid2.POLI_POINTS(x_control, y_control, self.NX)
            save.SAVE_2COLUMS_XLSX('input/database.xlsx', 'GRID_PERIMETER', 'POINTSX', xf, 'POINTSY', yf)
        
        self.mesh_run_CC = 0
                        
        
        
    #-------------------------------------------------------------------------//    
    #-----------------------------------------------------KEY PRESS FUNCTION--//
    def keyPressEvent(self, e):
        global x, y, j,x_poli,y_poli
        
        if e.key() == (Qt.Key_Control and Qt.Key_X) and self.flag==1: # POLIGONO
            self.flag = 0            
            x_poli.append(x_poli[0])
            y_poli.append(y_poli[0])
            self.data_points.setData(x_poli, y_poli)
            self.mesh_run_CC = 1
            self.POLI_POINTS()  
            save.SAVE_2COLUMS_XLSX('input/database.xlsx', 'GRID_CONTROL_POINTS', 'X_CONT', x_poli, 'Y_CONT', y_poli)
            
        if e.key() == Qt.Key_Escape: # PAUSE
            self.flag=0
            self.value=0
        
    

           
        
        
        






        
        
            
            
        
#------------------------------------------------------------------------------//
#---------------------------------------------------------------------PLOTS----//   
    def plot_grid(self, gridx, gridy,nx,ny):
        df = pd.read_excel('input/database.xlsx', sheet_name='WELLS')
        wells = int(df.at[0, "WELLS"])
        self.x_prod, self.y_prod, self.x_inj, self.y_inj = grid2.SEPARATE_COORD(df, wells)
        
        self.gridx = gridx
        self.gridy = gridy
        
        self.my_plot.hide()
        self.layout_plot.addWidget(self.canvas1, 0, 0, 2, 2)          
        self.canvas1.show()
        
        self.fig1.clf()
        ax = self.fig1.add_subplot(111)
        ax.axis('equal')
        ax.plot(self.gridx, self.gridy, 'g-', self.gridx.transpose(), self.gridy.transpose(),'g-')
        ax.plot(self.x_prod,self.y_prod,'bo')
        ax.plot(self.x_inj,self.y_inj,'rv')
        
        for i in range(0,len(self.x_prod)):
            text = "  Producer" + str(i+1)
            ax.annotate(text, (self.x_prod[i], self.y_prod[i]))
        
        for i in range(0,len(self.x_inj)):
            text = "  Injector" + str(i+1)
            ax.annotate(text, (self.x_inj[i], self.y_inj[i]))
        
        self.canvas1.draw()
        self.cent_x, self.cent_y = grid2.gridCenters2(self.gridx, self.gridy, nx, ny)


    def plot_properties(self):
        nx=self.NX+1
        ny=self.NY+1
        
        """
        self.cent_x, self.cent_y = grid.gridCenters(self.gridx, self.gridy, self.NX, self.NY)
        
        df = pd.read_excel('data.xlsx', sheet_name='PROPERTIES')
        absPerX = np.ones((nx,ny))*(float(df.at[0, "Value"])*1.062350161E-14)
        absPerY = np.ones((nx,ny))*(float(df.at[1, "Value"])*1.062350161E-14)
        porosity = np.ones((nx,ny))*(float(df.at[2, "Value"]))
        
        num = nx*ny 
        por = np.random.uniform(0.15,0.35,num)
        por_new = por.reshape((nx,ny))
        
        self.canvas.show()
        self.ax.clear()         
        self.ax.set_xlim([0, self.LY])
        self.ax.set_ylim([0, self.LY])
        self.ax.axis('equal')
        self.bar = self.ax.contourf(self.cent_x, self.cent_y, por_new, cmap=plt.cm.inferno)
        self.canvas.draw()
        """




    def plot_krcurves(self):
        df  = pd.read_excel('data.xlsx', sheet_name='KR_CURVES')        
        Swr  = float(df.at[0, "Value"])
        Sor  = float(df.at[1, "Value"])
        krw_ro  = float(df.at[2, "Value"])
        kro_rw  = float(df.at[3, "Value"])
        theta  = float(df.at[4, "Value"])
        
        Sw  = np.linspace(0.2,0.8,30)#ones((self.nx,self.ny))*(float(df.at[0, "sw"]))
        size=len(Sw)
        krw = np.zeros(size)
        kro = np.zeros(size)
                
        for i in range(0,size):
            if (Sw[i]<Swr):
                krw[i]=0
            else:
                krw[i]=krw_ro*pow(((Sw[i]-Swr)/(1.0-Sor-Swr)),theta)
        
        for i in range(0,size):
            if (1.0-Sw[0]<Sor):
                kro[i]=0.0
            else:
                kro[i] = kro_rw*pow(((1.0-Sor-Sw[i])/(1.0-Sor-Swr)),theta)
        
        """
        self.canvas1.show()
        self.ax.clear()         
        #self.ax.set_xlim([0, 1])
        #self.ax.set_ylim([0, 1])
        self.ax.axis('equal')
        self.bar = self.ax.plot(Sw, krw, 'b-',Sw, kro, 'r-')
        self.canvas.draw()
        """




    def plot_wells_2(self):
        self.my_plot.show()
        #self.mesh.hide()
        self.flag = 1
        
        self.data_grid_points = None
        self.data_contour_points = None
        
        lx=1000
        ly=1000
                                     
        grid_lim_x = [0,0,lx,lx,0] 
        grid_lim_y = [0,ly,ly,0,0]                                                                        
        xp=[0]
        yp=[0]
        #fillLevel=-0.3, brush='#1ad41154',
        #self.data_grid_points.setData(self.datax,self.datay, pen=None, symbol='o', symbolBrush =('#ff8000ff'),symbolPen=None, symbolSize=5)
        self.data_contour_points = self.my_plot.plot(grid_lim_x,grid_lim_y,  pen=pg.mkPen('b', width=5), symbol='o', symbolBrush =('#ff8000ff'),symbolPen=None, symbolSize=5)
        #self.my_plot.plot(xp,yp, pen=None, symbol='o', symbolBrush =('#ff8000ff'),symbolPen=None, symbolSize=5)        
        #self.data_contour_points.setData(grid_lim_x,grid_lim_y, fillLevel=-0.3, brush='#1ad41154', pen=None, symbol=None, symbolBrush =('#ff8000ff'),symbolPen=None, symbolSize=5)

          
bt_style = '''
QPushButton {color: white; 
             background-color: #0a2849;
             border: 0px solid;
             font: 12pt Arial;
             
             text-align: left;
             padding: 12px;
             max-width: 180 px;}

QPushButton:hover {background-color: #085698}

QPushButton:pressed {background-color: rgb(19,72,92)}
'''      

bt_style2 = '''
QPushButton {color: rgb(255, 255, 255); 
             background-color: white;
             border: 0px solid;
             font: 12pt Arial;
             text-align: left;
             padding: 12px;}

QPushButton:hover {background-color: rgb(0,112,129)}

QPushButton:pressed {background-color: rgb(19,72,92)}
'''  
bt_style3 = '''
QLabel {color: rgb(255, 255, 255); 
             background-color: #0a2849;
             border: 0px solid;
             font: 12pt Arial;}
    
''' 


    
#303030
#rgb(157,194,18) verde
#rgb(227,8,8) -rojo 

style = '''
QWidget {background-color: white; }  
 
'''


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    app.setStyleSheet(style)
    app.setStyle("fusion")
        
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
