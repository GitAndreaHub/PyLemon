# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class Caricamento_brano(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(469, 367)
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 50, 121, 41))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
"font: 30pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(168, 90, 131, 16))
        self.label_2.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 220, 181, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lineEdit.setObjectName("lineEdit")


        self.txt_nome_brano = QtWidgets.QLineEdit(Form)
        self.txt_nome_brano.setGeometry(QtCore.QRect(140, 220, 181, 31))
        self.txt_nome_brano.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.txt_nome_brano.setObjectName("txt_nome_brano")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 200, 101, 16))
        self.label_3.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 140, 101, 31))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setTabletTracking(True)
        self.pushButton.setStyleSheet("*{border: 1px solid rgb(221, 215, 25);"
                                       "border-radius: 10px;\n"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);\n}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 310, 81, 21))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setTabletTracking(True)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.pushButton_2.setObjectName("pushButton_2")


        self.btn_scegli_file = QtWidgets.QPushButton(Form)
        self.btn_scegli_file.setGeometry(QtCore.QRect(180, 140, 101, 31))
        self.btn_scegli_file.setMouseTracking(True)
        self.btn_scegli_file.setTabletTracking(True)
        self.btn_scegli_file.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.btn_scegli_file.setObjectName("btn_scegli_file")


        self.btn_pubblica = QtWidgets.QPushButton(Form)
        self.btn_pubblica.setGeometry(QtCore.QRect(190, 310, 81, 21))
        self.btn_pubblica.setMouseTracking(True)
        self.btn_pubblica.setTabletTracking(True)
        self.btn_pubblica.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.btn_pubblica.setObjectName("btn_pubblica")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "PySound"))
        self.label_2.setText(_translate("Form", "Pubblicazione brano"))
        self.label_3.setText(_translate("Form", "Nome brano:"))

        self.pushButton.setText(_translate("Form", "Scegli file"))
        self.pushButton_2.setText(_translate("Form", "Pubblica"))
        self.btn_scegli_file.setText(_translate("Form", "Scegli file"))
        self.btn_pubblica.setText(_translate("Form", "Pubblica"))

'''app = QApplication([])
window = QWidget()
form = Caricamento_brano()
form.setupUi(window)
window.show()
app.exec()'''
