import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget
from _radiobuttonform import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.radioTurkey.setChecked(True)
        self.ui.radioHighschool.setChecked(True)

        self.ui.radioTurkey.toggled.connect(self.onClickedCountry)
        self.ui.radioGreece.toggled.connect(self.onClickedCountry)
        self.ui.radioGermany.toggled.connect(self.onClickedCountry)
        self.ui.radioAzerbaijan.toggled.connect(self.onClickedCountry)

        self.ui.radioPrimaryschool.toggled.connect(self.onClickedEducation)
        self.ui.radioHighschool.toggled.connect(self.onClickedEducation)
        self.ui.radioUniversity.toggled.connect(self.onClickedEducation)
        self.ui.radioDegree.toggled.connect(self.onClickedEducation)


    def onClickedCountry(self):
        rb = self.sender()
        if rb.isChecked():
            print('Selected Country: ' + rb.text())
    
    def onClickedEducation(self):
        rb = self.sender()
        if rb.isChecked():
            print('Selected Education: ' + rb.text())
        
    def getselectedCountry(self):
        items = self.ui


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())
