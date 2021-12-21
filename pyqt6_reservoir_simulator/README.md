# This is a GUI


# assets directory
## icons and images
In these directories are saved all the icons and images used in the UI. However, this files are not calling directly in the UI. If you need to add more icons or images to the UI, add the in the rc_file.py see the details bellow.  
## stylesheet.py
This file is needed to add all the style (colors, sizes, effects) in the UI. If you are familiar with CSS, this file will be quite simmilar. For example: if you need to style a QPushButton you can set an Object Name or syle it directly. 

See the example:
----------------------------------------------------------------
**Without object name:**
stylesheet.py
...
#QPushButton {
    background: red;
    width: 40px;
    height: 40px;
}

**With object name:**
widgets.py
...
self.btn_1.setObjectName("button_1")
...

stylesheet.py
...
#button_1 {
    background: red;
    width: 40px;
    height: 40px;
}
------------------------------------------------------------------------
See more in the documentation: https://doc.qt.io/qtforpython/overviews/stylesheet-examples.html


## rc_file.py
This python file is necesary to storage different files, for example images and icons. If you need to add more icons or modify the current ones. Follow the next steps.

1. Access to the assets directory from your terminal
2. Open file.qrc
3. Add the path to file.qrc
   - see the example: <file>icons/curve.png</file>
4. Save the file.qrc
5. Excecute the follow command in your terminal:

pyside6-rcc files.qrc -o rc_file.py

### Example:
----------------------------------------------------
**import the module:**
from assets.rc_files import *

class LeftWidgets(QWidget):
    def __init__(self):
        ...
        self.btn_1 = QPushButton(self)
        **use the path you set in file.qrc**
        self.btn_1.setIcon(QIcon(**":/icons/roca.png"**))
        **Change the size of the icon**
        self.btn_1.setIconSize(QSize(40,40))
----------------------------------------------------

Notes: 
- the file.qrc and rc_file.py module can have different names
- pyside6-rcc command change according to the PyQt or PySide version

official documentation:
https://doc.qt.io/qtforpython/tutorials/basictutorial/qrcfiles.html


