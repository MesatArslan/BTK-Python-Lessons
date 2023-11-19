import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget , QMainWindow, QGridLayout
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self,color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(400,200,500,500) 

        # layout = QtWidgets.QBoxLayout()

        # layout = QtWidgets.QHBoxLayout()
        # layout.addWidget(Color('red'))
        # layout.addWidget(Color('blue'))
        # layout.addWidget(Color('green'))
        

        hlayout1 = QtWidgets.QHBoxLayout()
        hlayout1.addWidget(Color('red'))
        hlayout1.addWidget(Color('blue'))
        hlayout1.addWidget(Color('green'))
        hlayout1.setContentsMargins(50,0,0,0)

        hlayout2 = QtWidgets.QHBoxLayout()
        hlayout2.addWidget(Color('red'))
        hlayout2.addWidget(Color('green'))


        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout2)
        vlayout.addLayout(hlayout1)

    

        # layout = QtWidgets.QGridLayout()

        # layout.addWidget(Color('red'),0,0)
        # layout.addWidget(Color('blue'),1,0)
        # layout.addWidget(Color('green'),0,1)
        # layout.addWidget(Color('yellow'),3,2)


        widget = QWidget()
        widget.setLayout(vlayout)


        self.setCentralWidget(widget)

def App():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
App()

        

