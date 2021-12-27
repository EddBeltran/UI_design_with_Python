from PySide6.QtCore import *
from PySide6.QtWidgets import *

class MiddleWidgets(QWidget):
    def __init__(self):
        super().__init__()

        self.frame = QFrame()
        self.frame.setObjectName("sam_1")
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.frame.setLayout(self.layout)

        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())        
        treeview = QTreeView()
        treeview.setModel(model)
        treeview.setRootIndex(model.index(QDir.currentPath() + "\data"))
        treeview.hideColumn(1)
        treeview.hideColumn(2)
        treeview.hideColumn(3)
        treeview.setHeaderHidden(True)
        self.layout.addWidget(treeview)

        