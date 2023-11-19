import sys
from PyQt6 import QtWidgets
from _checkboxfrom import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbCinema.stateChanged.connect(self.show_state)
        self.ui.cbReadabook.stateChanged.connect(self.show_state)
        self.ui.cbSport.stateChanged.connect(self.show_state)

        self.ui.pushButton.clicked.connect(self.getAllChecked)

    
    def getAllChecked(self):
        result = ''
        items = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'
        self.ui.label.setText(result)      

            # print(cb.isChecked())
            # print(cb.text())


    def show_state(self,value):
        # print(value)
        # print(self.ui.cbCinema.isChecked())
        # print(self.ui.cbCinema.text())

        cb = self.sender()
        print(cb)


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())    

app()