from PyQt6 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_Sumup.clicked.connect(self.calculate)
        self.ui.btn_substraction.clicked.connect(self.calculate)
        self.ui.btn_division.clicked.connect(self.calculate)
        self.ui.btn_multiplication.clicked.connect(self.calculate)

    def calculate(self):
        sender = self.sender().text()
        result = 0

        # print(sender.text)
        if sender == 'Sum up':
            result = int(self.ui.txt_number1.text())  +  int(self.ui.txt_number2.text())
        elif sender == 'Substraction':
            result = int(self.ui.txt_number1.text())  -  int(self.ui.txt_number2.text())
        elif sender == 'Division':
            result = int(self.ui.txt_number1.text())  /  int(self.ui.txt_number2.text())
        elif sender == 'Multiplication':
            result = int(self.ui.txt_number1.text())  *  int(self.ui.txt_number2.text())
        self.ui.lbl_result.setText('Result: '+ str(result))


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()

    win.show()
    sys.exit(app.exec())

app()
