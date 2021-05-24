# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class home_ascoltatore(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(651, 508)
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 381, 41))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
"font: 30pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")

        """Btn mostra tutte"""
        self.btn_mostraTutte = QtWidgets.QPushButton(Form)
        self.btn_mostraTutte.setGeometry(QtCore.QRect(460, 130, 111, 61))
        self.btn_mostraTutte.setStyleSheet("*{background-color: rgb(207, 207, 207);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"color: rgb(0, 0, 0);\n}"
"*:hover{border: 5px solid rgb(221, 215, 25);\n}")

        self.btn_mostraTutte.setObjectName("pushButton")

        """Btn search"""
        self.btn_search = QtWidgets.QPushButton(Form)
        self.btn_search.setGeometry(QtCore.QRect(25, 130, 70, 61))
        self.btn_search.setStyleSheet("*{border: 1px solid rgb(207, 207, 207);"   #border per i bordi
                                       "border-radius: 20px;\n"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(207, 207, 207);\n}")
        self.btn_search.setObjectName("pushButton_4")

        """Linea Search"""
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 130, 331, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"border-radius: 20px;\n"
"border-color: rgb(133, 133, 133);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")


        self.listView_2 = QtWidgets.QListView(Form)
        self.listView_2.setGeometry(QtCore.QRect(250, 280, 231, 211))
        self.listView_2.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"border-radius: 10px;")
        self.listView_2.setObjectName("listView_2")
        self.line_9 = QtWidgets.QFrame(Form)
        self.line_9.setGeometry(QtCore.QRect(0, 260, 651, 16))
        self.line_9.setMinimumSize(QtCore.QSize(2, 2))
        self.line_9.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(Form)
        self.line_10.setGeometry(QtCore.QRect(220, 270, 20, 231))
        self.line_10.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(20, 280, 191, 211))
        self.listView.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"border-radius: 10px;")
        self.listView.setObjectName("listView")
        self.btn_Impostazioni = QtWidgets.QPushButton(Form)
        self.btn_Impostazioni.setGeometry(QtCore.QRect(520, 330, 91, 21))
        self.btn_Impostazioni.setMouseTracking(True)
        self.btn_Impostazioni.setTabletTracking(True)
        self.btn_Impostazioni.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"   #border per i bordi
                                       "border-radius: 10px;\n"
                                       "font: 10pt \"Arial\";"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_Impostazioni.setObjectName("pushButton_3")
        self.btn_Logout = QtWidgets.QPushButton(Form)
        self.btn_Logout.setGeometry(QtCore.QRect(520, 380, 91, 21))
        self.btn_Logout.setMouseTracking(True)
        self.btn_Logout.setTabletTracking(True)
        self.btn_Logout.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"   #border per i bordi
                                       "border-radius: 10px;\n"
                                       "font: 10pt \"Arial\";"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_Logout.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">PySound Label</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  Search..."))
        self.label.setText(_translate("Form", "PySound listener"))
        self.btn_mostraTutte.setText(_translate("Form", "Mostra tutte"))
        self.btn_Impostazioni.setText(_translate("Form", "Impostazioni"))
        self.btn_Logout.setText(_translate("Form", "Log out"))
        self.btn_search.setText(_translate("Form", "Cerca"))

"""app = QApplication([])
window = QWidget()
form = home_ascoltatore()
form.setupUi(window)
window.show()
app.exec()"""