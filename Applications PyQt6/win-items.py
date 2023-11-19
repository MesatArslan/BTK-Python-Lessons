import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt6.QtGui import QIcon


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()

        self.setWindowTitle('First Application')
        self.setGeometry(200,200,700,700) 
        self.setWindowIcon(QIcon('roketsan.png'))
        self.setToolTip('My Tooltip')
        self.initUI()

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self) 
        self.lbl_name.setText('Your name: ')
        self.lbl_name.move(50,30)
        
        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText('Your surname: ')
        self.lbl_surname.move(50,70)

        self.lbl_result = QtWidgets.QLabel(self)
        # self.lbl_result.setText('Result...')
        self.lbl_result.resize(300,32)
        self.lbl_result.move(140,140)


        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(140,30)
        self.txt_name.resize(200,32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(140,70)
        self.txt_surname.resize(200,32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.move(140,110)
        self.btn_save.setText('Save it')
        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
        self.lbl_result.setText('Name: '+ self.txt_name.text() +'\nSurname: '+ self.txt_surname.text())
        
        
       

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())


window()


# def window():
#     # app = QtWidgets.QApplication
#     app = QApplication(sys.argv)
#     win = QMainWindow()

    

#     win.setWindowTitle('First Application')
#     win.setGeometry(200,200,700,700)# ilk 2 kısım konumunu ayarlattırır sonraki kısımlar pencerenin botunu verir
#     win.setWindowIcon(QIcon('roketsan.png'))
#     win.setToolTip('My Tooltip')

#     lbl_name = QtWidgets.QLabel(win) # kutucuğun içine neyin elemanını olduğunu yazıyoruz.
#     lbl_name.setText('Your name: ')
#     lbl_name.move(50,30)

#     lbl_surname = QtWidgets.QLabel(win)
#     lbl_surname.setText('Your surname: ')
#     lbl_surname.move(50,70)

#     txt_name = QtWidgets.QLineEdit(win)
#     txt_name.move(140,30)

#     txt_surname = QtWidgets.QLineEdit(win)
#     txt_surname.move(140,70)

#     def clicked(self):
#         print('Cliked the button.\nName: '+ txt_name.text()+'\nSurname: '+ txt_surname.text())

#     btn_save = QtWidgets.QPushButton(win)
#     btn_save.move(140,110)
#     btn_save.setText('Save it')
#     btn_save.clicked.connect(clicked)

#     win.show()
#     sys.exit(app.exec())


# window()




# QLabel
# QComboBox
# QCheckBox
# QRadioButton
# QPushButton
# QTablewidget
# OLineEdit
# OSlider
# 0ProgressBar