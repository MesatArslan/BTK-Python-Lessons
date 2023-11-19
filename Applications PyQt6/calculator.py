import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication,QMainWindow


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()
        
        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,500)
        self.initUI()


    def initUI(self):
        self.lbl_number1 = QtWidgets.QLabel(self)
        self.lbl_number1.setText('Number 1:')
        self.lbl_number1.move(50,30)

        self.txt_number1 = QtWidgets.QLineEdit(self)
        self.txt_number1.move(150,30)
        self.txt_number1.resize(200,32)

        self.lbl_number2 = QtWidgets.QLabel(self)
        self.lbl_number2.setText('Number 2:')
        self.lbl_number2.move(50,80)

        self.txt_number2 = QtWidgets.QLineEdit(self)
        self.txt_number2.move(150,80)
        self.txt_number2.resize(200,32)

        self.btn_sum = QtWidgets.QPushButton(self)
        self.btn_sum.setText('Sum up') 
        self.btn_sum.move(150,130)
        self.btn_sum.clicked.connect(self.calculate)

        self.btn_substract = QtWidgets.QPushButton(self)
        self.btn_substract.setText('Substract') 
        self.btn_substract.move(150,170)
        self.btn_substract.clicked.connect(self.calculate)


        self.btn_division = QtWidgets.QPushButton(self)
        self.btn_division.setText('Division') 
        self.btn_division.move(150,210)
        self.btn_division.clicked.connect(self.calculate)


        self.btn_multiplication = QtWidgets.QPushButton(self)
        self.btn_multiplication.setText('Multiplication') 
        self.btn_multiplication.move(150,250)
        self.btn_multiplication.clicked.connect(self.calculate)


        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.move(150,290)

    def calculate(self):
        sender = self.sender().text()
        result = 0

        # print(sender.text)
        if sender == 'Sum up':
            result = int(self.txt_number1.text())  +  int(self.txt_number2.text())
        elif sender == 'Substract':
            result = int(self.txt_number1.text())  -  int(self.txt_number2.text())
        elif sender == 'Division':
            result = int(self.txt_number1.text())  /  int(self.txt_number2.text())
        elif sender == 'Multiplication':
            result = int(self.txt_number1.text())  *  int(self.txt_number2.text())
            
        self.lbl_result.setText('Result: '+ str(result))


        

    # def sum_up(self):
    #     result = int(self.txt_number1.text())  +  int(self.txt_number2.text())
    #     self.lbl_result.setText('Result: '+ str(result))

    # def substract(self):
    #     result = int(self.txt_number1.text())  -  int(self.txt_number2.text())
    #     self.lbl_result.setText('Result: '+ str(result))

    # def division(self):
    #     result = int(self.txt_number1.text())  / int(self.txt_number2.text())
    #     self.lbl_result.setText('Result: '+ str(result))

    # def multiplication(self):
    #     result = int(self.txt_number1.text())  *  int(self.txt_number2.text())
    #     self.lbl_result.setText('Result: '+ str(result))

def app():
    app = QApplication(sys.argv)
    win = MainForm()

    win.show()
    sys.exit(app.exec())

app()


     
        
      

        



