from PySide6.QtCore import *
from PySide6.QtGui import * #QStandardItem, QStandardItemModel
from PySide6.QtWidgets import *
import numpy as np

class MiddleWidgets(QWidget):
    signal = Signal(tuple)
    
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setObjectName("middle_stacked_widget")
        self.page_0()
        self.page_1()
        self.page_2()
        self.page_3()
        self.page_4()        
        
        self.set_page_by_id(0)
        self.cont = 0  
    
    def set_page_by_id(self, id):
        self.stacked_widget.setCurrentIndex(id)     
    
    #----------------------------------------------- render pages
    def page_0(self): # Files exploter
        id = 0
        frame = QFrame()
        layout = QVBoxLayout()
        #layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        path  = QDir.currentPath()
        #path_array = path.split("\\")
        lbl_1 = QLabel("Exporer")
        lbl_2 = QLineEdit(path)
        
        
        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())        
        treeview = QTreeView()
        treeview.setModel(model)
        treeview.setRootIndex(model.index(QDir.currentPath()))
        treeview.hideColumn(1)
        treeview.hideColumn(2)
        treeview.hideColumn(3)
        treeview.setHeaderHidden(True)
        layout.addWidget(lbl_1)
        layout.addWidget(lbl_2)
        layout.addWidget(treeview)
        self.stacked_widget.insertWidget(id, frame)
    
    def page_1(self): # Grid settings
        id = 1
        frame = QFrame()
        layout = QGridLayout()
        #layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        lbl_1 = QLabel("Grid")
        self.rb_1 = QRadioButton('1D')
        self.rb_2 = QRadioButton('2D')
        self.rb_3 = QRadioButton('3D')
        self.rb_2.setChecked(True)
        self.rb_1.toggled.connect(self.set_text_edit)
        self.rb_2.toggled.connect(self.set_text_edit)
        self.rb_3.toggled.connect(self.set_text_edit)

        lbl_3 = QLabel("Size")
        self.lx = QLineEdit()
        self.ly = QLineEdit()
        self.lz = QLineEdit()
        self.lz.setEnabled(False)
        
        lbl_4 = QLabel("Nodes")
        self.nodes_x = QLineEdit()
        self.nodes_y = QLineEdit()
        self.nodes_z = QLineEdit()
        self.nodes_z.setEnabled(False)
        
        #QValidator(float)Qd
        self.onlyFloat = QDoubleValidator(10.0, 500000.0, 3)
        self.onlyInt = QIntValidator(10, 200)
        self.nodes_x.setValidator(self.onlyInt)
        self.nodes_y.setValidator(self.onlyInt)
        
        self.lx.setValidator(self.onlyFloat)
        self.ly.setValidator(self.onlyFloat)
        
        
        #self.onlyInt = Qva#QFloatValidator()
        #self.nodes_x.setValidator(self.onlyInt)
        

        self.customize_cbx = QCheckBox("Draw custom grid")
        self.customize_cbx.stateChanged.connect(self.set_pqtgraph_drawing_widgets)
        self.lbl_5 = QLabel("Control Points")
        self.tableWidget = QTableView()
        self.tableWidget.verticalHeader().setVisible(False)      
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['id','Boundary', 'X', 'Y'])
        self.tableWidget.setModel(self.model)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.rb_4 = QRadioButton('Transfinite Interpolation Method')
        self.rb_5 = QRadioButton('Iterative Method using Elliptical PDEs')
        self.rb_4.setChecked(True)
        self.lbl_6 = QLabel("Iterations: ")
        self.iterations = QLineEdit("200")
        self.btn_more = QPushButton("... More")
        self.set_pqtgraph_drawing_widgets()  

        generate_grid = QPushButton("Generate meshgrid")
        
        layout.addWidget(lbl_1, 0,0,1,3)
        layout.addWidget(self.rb_1, 1,0,1,1)
        layout.addWidget(self.rb_2, 1,1,1,1)
        layout.addWidget(self.rb_3, 1,2,1,1)
        layout.addWidget(lbl_3, 2,0,1,3)
        layout.addWidget(self.lx, 3,0,1,1)
        layout.addWidget(self.ly, 3,1,1,1)
        layout.addWidget(self.lz, 3,2,1,1)
        layout.addWidget(lbl_4, 4,0,1,3)
        layout.addWidget(self.nodes_x, 5,0,1,1)
        layout.addWidget(self.nodes_y, 5,1,1,1)
        layout.addWidget(self.nodes_z, 5,2,1,1)
        layout.addWidget(self.customize_cbx, 6,0,1,3)
        layout.addWidget(self.lbl_5, 7,0,1,3)
        layout.addWidget(self.tableWidget, 8,0,1,3)
        layout.addWidget(self.rb_4, 9,0,1,3)
        layout.addWidget(self.rb_5, 10,0,1,3)
        layout.addWidget(self.lbl_6, 11,0,1,1)
        layout.addWidget(self.iterations, 11,1,1,1)
        layout.addWidget(self.btn_more, 11,2,1,1)
        layout.addWidget(generate_grid, 12,0,1,3, Qt.AlignmentFlag.AlignBottom)
        layout.setRowStretch(12,3)
        
        self.stacked_widget.insertWidget(id, frame)
        generate_grid.clicked.connect(self.send_parameters_by_signal)
    
    def page_2(self):
        id = 2
        frame = QFrame()
        layout = QVBoxLayout()
        #layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        lbl_1 = QLabel("page 2")
        layout.addWidget(lbl_1)
        self.stacked_widget.insertWidget(id, frame)
    
    def page_3(self):
        id = 3
        frame = QFrame()
        layout = QVBoxLayout()
        #layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        lbl_1 = QLabel("page 3")
        layout.addWidget(lbl_1)
        self.stacked_widget.insertWidget(id, frame)
    
    def page_4(self):
        id = 4
        frame = QFrame()
        layout = QVBoxLayout()
        #layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        lbl_1 = QLabel("page 4")
        layout.addWidget(lbl_1)
        self.stacked_widget.insertWidget(id, frame)
    
    #------------------------------------------------------ add or modify widgets of rendered pages       
    def set_text_edit(self):
        if self.rb_1.isChecked():
            self.ly.setEnabled(False)
            self.lz.setEnabled(False)
            self.nodes_y.setEnabled(False)
            self.nodes_z.setEnabled(False)
        
        if self.rb_2.isChecked():
            self.ly.setEnabled(True)
            self.lz.setEnabled(False)
            self.nodes_y.setEnabled(True)
            self.nodes_z.setEnabled(False)
        
        if self.rb_3.isChecked():
            self.ly.setEnabled(True)
            self.lz.setEnabled(True)
            self.nodes_y.setEnabled(True)
            self.nodes_z.setEnabled(True)
        
    
    def set_pqtgraph_drawing_widgets(self):
        if self.customize_cbx.isChecked():
            self.response = True
        else:
            self.response = False
        self.lbl_5.setEnabled(self.response)
        self.tableWidget.setEnabled(self.response)
        self.rb_4.setEnabled(self.response)
        self.rb_5.setEnabled(self.response)
        self.lbl_6.setEnabled(self.response)
        self.iterations.setEnabled(self.response)
        self.btn_more.setEnabled(self.response)
        
        
    def addpoints(self, id_array, boundary, point_x, point_y):
        item_0 = QStandardItem(str(id_array)) 
        item_1 = QStandardItem(boundary)
        item_2 = QStandardItem( str(round(point_x, 2)) )
        item_3 = QStandardItem( str(round(point_y, 2)) )
        item_0.setTextAlignment(Qt.AlignHCenter)
        item_1.setTextAlignment(Qt.AlignHCenter)
        item_2.setTextAlignment(Qt.AlignHCenter)
        item_3.setTextAlignment(Qt.AlignHCenter)
        
        self.model.setItem(id_array, 0, item_0)
        self.model.setItem(id_array, 1, item_1)
        self.model.setItem(id_array, 2, item_2)
        self.model.setItem(id_array, 3, item_3)

        self.cont = self.cont + 1

    #---------------------------------------------------- send signals     
    def send_parameters_by_signal(self):
        #if (type(self.lx.text()))
        #print(self.lx.validator())
        if (self.lx.text() == '' or self.ly.text() == '' or self.nodes_x.text() == '' or self.nodes_y.text() ==''):
            print("Please fill the required fields")
        else:
            tuple_1 = (float(self.lx.text()), float(self.ly.text()), 0.0,
                       int(self.nodes_x.text()), int(self.nodes_y.text()), 0 )

            self.signal.emit(tuple_1)