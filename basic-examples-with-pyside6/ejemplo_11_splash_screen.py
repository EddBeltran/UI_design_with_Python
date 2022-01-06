from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys, time


class Form(QDialog):
    """ Just a simple dialog with a couple of widgets
    """
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        self.browser = QTextBrowser()
        self.setWindowTitle('Just a dialog')
        self.lineedit = QLineEdit("Write something and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)


    def update_ui(self):
        self.browser.append(self.lineedit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    splash_pix = QPixmap('img/bee2.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    splash.setEnabled(False)
    splash.show()
    splash.showMessage("<h1><font color='green'>Welcome BeeMan!</font></h1>", Qt.AlignTop | Qt.AlignCenter, Qt.black)
    time.sleep(1) # Simulate something that takes time
    form = Form()
    form.show()
    splash.finish(form)
    
    sys.exit(app.exec())