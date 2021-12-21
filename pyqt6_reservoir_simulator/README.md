# This is a GUI


# assets directory
## icons and images
In these directories are saved all the icons and images used in the UI. However, this files are not calling directly from UI widgets. If you need more icons or images, add them in the rc_file.py see all the details bellow.  
## stylesheet.py
This file is needed to add all the style (colors, sizes, effects) in the UI. If you are familiar with CSS, this file will be quite simmilar. For example: if you need to style a QPushButton you can set an Object Name or syle it directly. 

See more in the documentation:
https://doc.qt.io/qtforpython/overviews/stylesheet-examples.html


## rc_file.py
This python file is necesary to storage different files, for example images and icons. If you need to add more icons or modify the current ones. Follow the next steps.

1. Access to the assets directory from your terminal
2. Open file.qrc
3. Add the path to file.qrc
4. Save the file.qrc
5. Excecute the follow command in your terminal:

pyside6-rcc files.qrc -o rc_file.py

Notes: 
- the file.qrc and rc_file.py module can have different names
- pyside6-rcc command change according to the PyQt or PySide version

See the official documentation:
https://doc.qt.io/qtforpython/tutorials/basictutorial/qrcfiles.html