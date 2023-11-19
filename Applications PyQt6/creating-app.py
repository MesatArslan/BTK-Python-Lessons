import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt6.QtGui import QIcon

def window():
    # app = QtWidgets.QApplication
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('First Application')
    win.setGeometry(200,200,700,700)# ilk 2 kısım konumunu ayarlattırır sonraki kısımlar pencerenin boyutunu verir
    win.setWindowIcon(QIcon('roketsan.png'))
    win.setToolTip('My Tooltip')
    
    win.show()
    sys.exit(app.exec())

window()