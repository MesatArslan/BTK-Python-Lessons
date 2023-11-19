import sys
from PyQt6 import QtWidgets
from _comboboxForm import Ui_MainWindow


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.cbcities.addItem('Ankara')
        # self.ui.cbcities.addItem('İstanbul')
        # self.ui.cbcities.addItem('Kocaeli')

        # combo = self.ui.cbcities
        # combo.addItem('Ankara')
        # combo.addItem('İstanbul')
        # combo.addItem('Kocaeli')
        # combo.addItems(['Adana','İzmir','Antalya'])

        self.ui.btnloaditems.clicked.connect(self.LoadItems)
        self.ui.btngetitem.clicked.connect(self.Getitem)
        self.ui.btnclearitems.clicked.connect(self.ClearItems)

        self.ui.cbcities.currentIndexChanged.connect(self.SelectedChanged)
        # self.ui.cbcities.currentIndexChanged[str].connect(self.SelectedChangedText)

    def ClearItems(self):
        self.ui.cbcities.clear()

    def SelectedChanged(self, index):
        print(index)

    def SelectedChangedText(self, text):
        print(text)

    def LoadItems(self):
        cities = ['Adana','İzmir','Antalya']

        self.ui.cbcities.addItems(cities)

    def Getitem(self):
        print(self.ui.cbcities.currentText())
        print(self.ui.cbcities.currentIndex())
        count = self.ui.cbcities.count()

        for index in range(count):
            print(self.ui.cbcities.itemText(index))
        


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec())    

app()