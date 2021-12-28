from PySide6.QtCore import *
from PySide6.QtWidgets import *

class MiddleWidgets(QWidget):
    signal_middle = Signal(tuple)
    
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.page_0()
        self.page_1()
        self.set_page_by_id(0)  
    
    def set_page_by_id(self, id):
        self.stacked_widget.setCurrentIndex(id)     
    
    def page_0(self):
        id = 0
        frame = QFrame()
        layout = QVBoxLayout()
        #layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        lbl_1 = QLabel("page 2")
        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())        
        treeview = QTreeView()
        treeview.setModel(model)
        treeview.setRootIndex(model.index(QDir.currentPath() + "\data"))
        treeview.hideColumn(1)
        treeview.hideColumn(2)
        treeview.hideColumn(3)
        treeview.setHeaderHidden(True)
        layout.addWidget(lbl_1)
        layout.addWidget(treeview)
        self.stacked_widget.insertWidget(id, frame)
    
    def page_1(self):
        id = 1
        frame = QFrame()
        layout = QGridLayout()
        #layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        lbl_1 = QLabel("Dimension")
        rb_1 = QRadioButton('1D')
        rb_2 = QRadioButton('2D')
        rb_3 = QRadioButton('3D')
        lbl_2 = QLabel("Size")
        self.lx = QLineEdit()
        self.ly = QLineEdit()
        self.lz = QLineEdit()
        lbl_3 = QLabel("Nodes")
        self.nodes_x = QLineEdit()
        self.nodes_y = QLineEdit()
        self.nodes_z = QLineEdit()
        submit = QPushButton("create grid")
        
        layout.addWidget(lbl_1, 0,0,1,3)
        layout.addWidget(rb_1, 1,0,1,1)
        layout.addWidget(rb_2, 1,1,1,1)
        layout.addWidget(rb_3, 1,2,1,1)
        layout.addWidget(lbl_2, 2,0,1,3)
        layout.addWidget(self.lx, 3,0,1,1)
        layout.addWidget(self.ly, 3,1,1,1)
        layout.addWidget(self.lz, 3,2,1,1)
        layout.addWidget(lbl_3, 4,0,1,3)
        layout.addWidget(self.nodes_x, 5,0,1,1)
        layout.addWidget(self.nodes_y, 5,1,1,1)
        layout.addWidget(self.nodes_z, 5,2,1,1)
        layout.addWidget(submit, 6,0,1,3)        
        self.stacked_widget.insertWidget(id, frame)
        submit.clicked.connect(self.send_grid_parameters) #lambda: self.signal.emit(p1_tuple)
         
    def send_grid_parameters(self):
        tuple_1 = (self.lx.text(), self.ly.text(), self.nodes_x.text(), self.nodes_y.text())
        self.signal_middle.emit(tuple_1)