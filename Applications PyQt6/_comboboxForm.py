# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 404)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbcities = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cbcities.setGeometry(QtCore.QRect(30, 20, 171, 81))
        self.cbcities.setObjectName("cbcities")
        self.lblresult = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblresult.setGeometry(QtCore.QRect(280, 40, 58, 16))
        self.lblresult.setObjectName("lblresult")
        self.btngetitem = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btngetitem.setGeometry(QtCore.QRect(40, 140, 121, 61))
        self.btngetitem.setObjectName("btngetitem")
        self.btnloaditems = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnloaditems.setGeometry(QtCore.QRect(250, 140, 121, 61))
        self.btnloaditems.setObjectName("btnloaditems")
        self.btnclearitems = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnclearitems.setGeometry(QtCore.QRect(40, 240, 121, 61))
        self.btnclearitems.setObjectName("btnclearitems")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblresult.setText(_translate("MainWindow", "TextLabel"))
        self.btngetitem.setText(_translate("MainWindow", "Get Item"))
        self.btnloaditems.setText(_translate("MainWindow", "Load Items"))
        self.btnclearitems.setText(_translate("MainWindow", "Clear Items"))
