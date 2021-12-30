from PySide6.QtCore import *
from PySide6.QtWidgets import *

class MiddleWidgets(QWidget):
    signal = Signal(tuple)
    
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setObjectName("middle_stacked_widget")
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
    
    def page_1(self):
        id = 1
        frame = QFrame()
        layout = QGridLayout()
        #layout.setContentsMargins(0,0,0,0)
        frame.setLayout(layout)

        lbl_1 = QLabel("Grid")
        lbl_2 = QLabel("Dimension")
        self.rb_1 = QRadioButton('1D')
        self.rb_2 = QRadioButton('2D')
        self.rb_3 = QRadioButton('3D')
        self.rb_1.setChecked(True)
        self.rb_1.toggled.connect(self.set_text_edit)
        self.rb_2.toggled.connect(self.set_text_edit)
        self.rb_3.toggled.connect(self.set_text_edit)

        lbl_3 = QLabel("Size")
        self.lx = QLineEdit()
        self.ly = QLineEdit()
        self.lz = QLineEdit()

        self.ly.setEnabled(False)
        self.lz.setEnabled(False)
        
        lbl_4 = QLabel("Nodes")
        self.nodes_x = QLineEdit()
        self.nodes_y = QLineEdit()
        self.nodes_z = QLineEdit()

        self.nodes_y.setEnabled(False)
        self.nodes_z.setEnabled(False)

        #check_btn = QCheckBox("Draw custom grid")
        customize_btn = QPushButton("Customize")
        generate_grid = QPushButton("Generate meshgrid")
        
        layout.addWidget(lbl_1, 0,0,1,3)
        layout.addWidget(lbl_2, 1,0,1,3)
        layout.addWidget(self.rb_1, 2,0,1,1)
        layout.addWidget(self.rb_2, 2,1,1,1)
        layout.addWidget(self.rb_3, 2,2,1,1)
        layout.addWidget(lbl_3, 3,0,1,3)
        layout.addWidget(self.lx, 4,0,1,1)
        layout.addWidget(self.ly, 4,1,1,1)
        layout.addWidget(self.lz, 4,2,1,1)
        layout.addWidget(lbl_4, 5,0,1,3)
        layout.addWidget(self.nodes_x, 6,0,1,1)
        layout.addWidget(self.nodes_y, 6,1,1,1)
        layout.addWidget(self.nodes_z, 6,2,1,1)
        
        layout.addWidget(customize_btn, 8,0,1,1, Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(generate_grid, 8,1,1,2, Qt.AlignmentFlag.AlignBottom)
        layout.setRowStretch(8,3)
        self.stacked_widget.insertWidget(id, frame)
        generate_grid.clicked.connect(self.send_parameters_by_signal) #lambda: self.signal.emit(p1_tuple)
    
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

         
    def send_parameters_by_signal(self):
        
        tuple_1 = (self.lx.text(), self.ly.text(), self.lz.text(),  self.nodes_x.text(), self.nodes_y.text(), self.nodes_z.text() )
        self.signal.emit(tuple_1)