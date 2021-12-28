from PySide6.QtCore import *
from PySide6.QtWidgets import *

class MiddleWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.frame = QFrame()
        self.layout = QVBoxLayout()
        self.frame.setLayout(self.layout)
        
        self.lbl_1 = QLabel("default page")
        self.layout.addWidget(self.lbl_1)
        self.stacked_widget.addWidget(self.frame)
    
    def show_page_1(self):
        page_num = 1
        if self.stacked_widget.currentIndex() != page_num :
            frame = QFrame()
            layout = QVBoxLayout()
            layout.setContentsMargins(0,0,0,0)
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
            self.stacked_widget.insertWidget(page_num, frame)
            self.stacked_widget.setCurrentIndex(page_num)
    
    def show_page_2(self):
        page_num = 2
        if self.stacked_widget.currentIndex() != page_num :
            frame = QFrame()
            layout = QVBoxLayout()
            layout.setContentsMargins(0,0,0,0)
            frame.setLayout(layout)
    
            lbl_1 = QLabel("Dimension")
            layout.addWidget(lbl_1)
            self.stacked_widget.insertWidget(page_num, frame)
            self.stacked_widget.setCurrentIndex(page_num)

    

        