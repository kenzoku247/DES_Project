# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mrE.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(800, 424)
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.E_5 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.E_5.setFont(font)
        self.E_5.setAlignment(QtCore.Qt.AlignCenter)
        self.E_5.setReadOnly(True)
        self.E_5.setObjectName("E_5")
        self.gridLayout_2.addWidget(self.E_5, 7, 1, 1, 1)
        self.E_1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.E_1.setFont(font)
        self.E_1.setAlignment(QtCore.Qt.AlignCenter)
        self.E_1.setReadOnly(True)
        self.E_1.setObjectName("E_1")
        self.gridLayout_2.addWidget(self.E_1, 3, 1, 1, 1)
        self.E_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.E_3.setFont(font)
        self.E_3.setAlignment(QtCore.Qt.AlignCenter)
        self.E_3.setReadOnly(True)
        self.E_3.setObjectName("E_3")
        self.gridLayout_2.addWidget(self.E_3, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.E_4 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.E_4.setFont(font)
        self.E_4.setAlignment(QtCore.Qt.AlignCenter)
        self.E_4.setReadOnly(True)
        self.E_4.setObjectName("E_4")
        self.gridLayout_2.addWidget(self.E_4, 6, 1, 1, 1)
        self.E_6 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.E_6.setFont(font)
        self.E_6.setAlignment(QtCore.Qt.AlignCenter)
        self.E_6.setReadOnly(True)
        self.E_6.setObjectName("E_6")
        self.gridLayout_2.addWidget(self.E_6, 8, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 9, 1, 1, 1)
        self.E_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.E_2.setFont(font)
        self.E_2.setAlignment(QtCore.Qt.AlignCenter)
        self.E_2.setReadOnly(True)
        self.E_2.setObjectName("E_2")
        self.gridLayout_2.addWidget(self.E_2, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)
        self.kdv = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kdv.setFont(font)
        self.kdv.setAlignment(QtCore.Qt.AlignCenter)
        self.kdv.setReadOnly(True)
        self.kdv.setObjectName("kdv")
        self.gridLayout_2.addWidget(self.kdv, 1, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 2, 1, 1)
        self.kdmr = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kdmr.setFont(font)
        self.kdmr.setAlignment(QtCore.Qt.AlignCenter)
        self.kdmr.setReadOnly(True)
        self.kdmr.setObjectName("kdmr")
        self.gridLayout_2.addWidget(self.kdmr, 10, 1, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        MainWindow3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow3)
        self.statusbar.setObjectName("statusbar")
        MainWindow3.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "DES ENCRYPT"))
        self.label.setText(_translate("MainWindow3", "Khối đầu vào"))
        self.label_3.setText(_translate("MainWindow3", "Khối đã mở rộng"))
        self.label_2.setText(_translate("MainWindow3", "Hoán vị E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow3 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow3)
    MainWindow3.show()
    sys.exit(app.exec_())