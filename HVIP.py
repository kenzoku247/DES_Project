# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HVIP.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(800, 501)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout.addWidget(self.label_20)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.But_HV_IP = QtWidgets.QPushButton(self.centralwidget)
        self.But_HV_IP.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.But_HV_IP.setFont(font)
        self.But_HV_IP.setObjectName("But_HV_IP")
        self.gridLayout_12.addWidget(self.But_HV_IP, 1, 0, 1, 1)
        self.But_Loop = QtWidgets.QPushButton(self.centralwidget)
        self.But_Loop.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.But_Loop.setFont(font)
        self.But_Loop.setObjectName("But_Loop")
        self.gridLayout_12.addWidget(self.But_Loop, 1, 1, 1, 1)
        self.r_0 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.r_0.setFont(font)
        self.r_0.setAlignment(QtCore.Qt.AlignCenter)
        self.r_0.setReadOnly(True)
        self.r_0.setObjectName("r_0")
        self.gridLayout_12.addWidget(self.r_0, 0, 1, 1, 1)
        self.l_0 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.l_0.setFont(font)
        self.l_0.setText("")
        self.l_0.setAlignment(QtCore.Qt.AlignCenter)
        self.l_0.setReadOnly(True)
        self.l_0.setObjectName("l_0")
        self.gridLayout_12.addWidget(self.l_0, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_12, 5, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.Dl_9 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_9.setFont(font)
        self.Dl_9.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_9.setReadOnly(True)
        self.Dl_9.setObjectName("Dl_9")
        self.gridLayout_11.addWidget(self.Dl_9, 0, 2, 1, 1)
        self.Dl_12 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_12.setFont(font)
        self.Dl_12.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_12.setReadOnly(True)
        self.Dl_12.setObjectName("Dl_12")
        self.gridLayout_11.addWidget(self.Dl_12, 3, 2, 1, 1)
        self.Dl_16 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_16.setFont(font)
        self.Dl_16.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_16.setReadOnly(True)
        self.Dl_16.setObjectName("Dl_16")
        self.gridLayout_11.addWidget(self.Dl_16, 7, 2, 1, 1)
        self.Dl_8 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_8.setFont(font)
        self.Dl_8.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_8.setReadOnly(True)
        self.Dl_8.setObjectName("Dl_8")
        self.gridLayout_11.addWidget(self.Dl_8, 7, 0, 1, 1)
        self.Dl_7 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_7.setFont(font)
        self.Dl_7.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_7.setReadOnly(True)
        self.Dl_7.setObjectName("Dl_7")
        self.gridLayout_11.addWidget(self.Dl_7, 6, 0, 1, 1)
        self.Dl_5 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_5.setFont(font)
        self.Dl_5.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_5.setReadOnly(True)
        self.Dl_5.setObjectName("Dl_5")
        self.gridLayout_11.addWidget(self.Dl_5, 4, 0, 1, 1)
        self.Dl_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_2.setFont(font)
        self.Dl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_2.setReadOnly(True)
        self.Dl_2.setObjectName("Dl_2")
        self.gridLayout_11.addWidget(self.Dl_2, 1, 0, 1, 1)
        self.Dl_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_3.setFont(font)
        self.Dl_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_3.setReadOnly(True)
        self.Dl_3.setObjectName("Dl_3")
        self.gridLayout_11.addWidget(self.Dl_3, 2, 0, 1, 1)
        self.Dl_1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_1.setFont(font)
        self.Dl_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Dl_1.setText("")
        self.Dl_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_1.setReadOnly(True)
        self.Dl_1.setObjectName("Dl_1")
        self.gridLayout_11.addWidget(self.Dl_1, 0, 0, 1, 1)
        self.Dl_10 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_10.setFont(font)
        self.Dl_10.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_10.setReadOnly(True)
        self.Dl_10.setObjectName("Dl_10")
        self.gridLayout_11.addWidget(self.Dl_10, 1, 2, 1, 1)
        self.Dl_4 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_4.setFont(font)
        self.Dl_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_4.setReadOnly(True)
        self.Dl_4.setObjectName("Dl_4")
        self.gridLayout_11.addWidget(self.Dl_4, 3, 0, 1, 1)
        self.Dl_11 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_11.setFont(font)
        self.Dl_11.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_11.setReadOnly(True)
        self.Dl_11.setObjectName("Dl_11")
        self.gridLayout_11.addWidget(self.Dl_11, 2, 2, 1, 1)
        self.Dl_13 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_13.setFont(font)
        self.Dl_13.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_13.setReadOnly(True)
        self.Dl_13.setObjectName("Dl_13")
        self.gridLayout_11.addWidget(self.Dl_13, 4, 2, 1, 1)
        self.Dl_6 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_6.setFont(font)
        self.Dl_6.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_6.setReadOnly(True)
        self.Dl_6.setObjectName("Dl_6")
        self.gridLayout_11.addWidget(self.Dl_6, 5, 0, 1, 1)
        self.Dl_15 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_15.setFont(font)
        self.Dl_15.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_15.setReadOnly(True)
        self.Dl_15.setObjectName("Dl_15")
        self.gridLayout_11.addWidget(self.Dl_15, 6, 2, 1, 1)
        self.Dl_14 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dl_14.setFont(font)
        self.Dl_14.setAlignment(QtCore.Qt.AlignCenter)
        self.Dl_14.setReadOnly(True)
        self.Dl_14.setObjectName("Dl_14")
        self.gridLayout_11.addWidget(self.Dl_14, 5, 2, 1, 1)
        self.Dla_1 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dla_1.setFont(font)
        self.Dla_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Dla_1.setText("")
        self.Dla_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Dla_1.setReadOnly(True)
        self.Dla_1.setObjectName("Dla_1")
        self.gridLayout_11.addWidget(self.Dla_1, 0, 1, 1, 1)
        self.Dla_2 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dla_2.setFont(font)
        self.Dla_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Dla_2.setReadOnly(True)
        self.Dla_2.setObjectName("Dla_2")
        self.gridLayout_11.addWidget(self.Dla_2, 1, 1, 1, 1)
        self.Dla_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dla_3.setFont(font)
        self.Dla_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Dla_3.setReadOnly(True)
        self.Dla_3.setObjectName("Dla_3")
        self.gridLayout_11.addWidget(self.Dla_3, 2, 1, 1, 1)
        self.Dla_4 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dla_4.setFont(font)
        self.Dla_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Dla_4.setReadOnly(True)
        self.Dla_4.setObjectName("Dla_4")
        self.gridLayout_11.addWidget(self.Dla_4, 3, 1, 1, 1)
        self.Dla_5 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dla_5.setFont(font)
        self.Dla_5.setAlignment(QtCore.Qt.AlignCenter)
        self.Dla_5.setReadOnly(True)
        self.Dla_5.setObjectName("Dla_5")
        self.gridLayout_11.addWidget(self.Dla_5, 4, 1, 1, 1)
        self.Dla_6 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dla_6.setFont(font)
        self.Dla_6.setAlignment(QtCore.Qt.AlignCenter)
        self.Dla_6.setReadOnly(True)
        self.Dla_6.setObjectName("Dla_6")
        self.gridLayout_11.addWidget(self.Dla_6, 5, 1, 1, 1)
        self.Dla_7 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dla_7.setFont(font)
        self.Dla_7.setAlignment(QtCore.Qt.AlignCenter)
        self.Dla_7.setReadOnly(True)
        self.Dla_7.setObjectName("Dla_7")
        self.gridLayout_11.addWidget(self.Dla_7, 6, 1, 1, 1)
        self.Dla_8 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dla_8.setFont(font)
        self.Dla_8.setAlignment(QtCore.Qt.AlignCenter)
        self.Dla_8.setReadOnly(True)
        self.Dla_8.setObjectName("Dla_8")
        self.gridLayout_11.addWidget(self.Dla_8, 7, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_11, 1, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_8.addWidget(self.label_21, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_8.addWidget(self.label_17, 0, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_8.addWidget(self.label_22, 1, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_8.addWidget(self.label_18, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "DES ENCRYPT"))
        self.label_19.setText(_translate("MainWindow1", "L0"))
        self.label_20.setText(_translate("MainWindow1", "R0"))
        self.But_HV_IP.setText(_translate("MainWindow1", "Thực hiện hoán vị IP"))
        self.But_Loop.setText(_translate("MainWindow1", "Bắt đầu thực hiện vòng lặp"))
        self.label_21.setText(_translate("MainWindow1", "Before"))
        self.label_17.setText(_translate("MainWindow1", "Hoán vị IP"))
        self.label_22.setText(_translate("MainWindow1", "After"))
        self.label_18.setText(_translate("MainWindow1", "Khối dữ liệu đầu vào (64 bit)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
