# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow4(object):
    def setupUi(self, MainWindow4):
        MainWindow4.setObjectName("MainWindow4")
        MainWindow4.resize(800, 393)
        self.centralwidget = QtWidgets.QWidget(MainWindow4)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.S_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S_2.setFont(font)
        self.S_2.setAlignment(QtCore.Qt.AlignCenter)
        self.S_2.setReadOnly(True)
        self.S_2.setObjectName("S_2")
        self.gridLayout.addWidget(self.S_2, 4, 0, 1, 1)
        self.S_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S_label.setFont(font)
        self.S_label.setObjectName("S_label")
        self.gridLayout.addWidget(self.S_label, 2, 0, 1, 1)
        self.S_1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S_1.setFont(font)
        self.S_1.setAlignment(QtCore.Qt.AlignCenter)
        self.S_1.setReadOnly(True)
        self.S_1.setObjectName("S_1")
        self.gridLayout.addWidget(self.S_1, 3, 0, 1, 1)
        self.S_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S_3.setFont(font)
        self.S_3.setAlignment(QtCore.Qt.AlignCenter)
        self.S_3.setReadOnly(True)
        self.S_3.setObjectName("S_3")
        self.gridLayout.addWidget(self.S_3, 5, 0, 1, 1)
        self.S_4 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S_4.setFont(font)
        self.S_4.setAlignment(QtCore.Qt.AlignCenter)
        self.S_4.setReadOnly(True)
        self.S_4.setObjectName("S_4")
        self.gridLayout.addWidget(self.S_4, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.S_dv = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S_dv.setFont(font)
        self.S_dv.setAlignment(QtCore.Qt.AlignCenter)
        self.S_dv.setReadOnly(True)
        self.S_dv.setObjectName("S_dv")
        self.gridLayout.addWidget(self.S_dv, 1, 0, 1, 2)
        self.S_dr = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S_dr.setFont(font)
        self.S_dr.setAlignment(QtCore.Qt.AlignCenter)
        self.S_dr.setReadOnly(True)
        self.S_dr.setObjectName("S_dr")
        self.gridLayout.addWidget(self.S_dr, 8, 0, 1, 2)
        self.But_Next = QtWidgets.QPushButton(self.centralwidget)
        self.But_Next.setObjectName("But_Next")
        self.gridLayout.addWidget(self.But_Next, 9, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        MainWindow4.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow4.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow4)
        self.statusbar.setObjectName("statusbar")
        MainWindow4.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow4)

    def retranslateUi(self, MainWindow4):
        _translate = QtCore.QCoreApplication.translate
        MainWindow4.setWindowTitle(_translate("MainWindow4", "DES ENCRYPT"))
        self.label.setText(_translate("MainWindow4", "Khối đầu vào"))
        self.S_label.setText(_translate("MainWindow4", "Sbox số 1"))
        self.label_3.setText(_translate("MainWindow4", "Khối đầu ra"))
        self.But_Next.setText(_translate("MainWindow4", "------>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow4 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setupUi(MainWindow4)
    MainWindow4.show()
    sys.exit(app.exec_())