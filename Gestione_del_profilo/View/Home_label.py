# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class home_etichetta(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(910, 515)
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(35, 10, 380, 81))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
"font: 30pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")

        """Linea Search"""
        self.txt_nome = QtWidgets.QLineEdit(Form)
        self.txt_nome.setGeometry(QtCore.QRect(110, 130, 331, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txt_nome.setFont(font)
        self.txt_nome.setTabletTracking(False)
        self.txt_nome.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                    "border-radius: 20px;\n"
                                    "border-color: rgb(133, 133, 133);")
        # self.lineEdit.setText("")
        self.txt_nome.setObjectName("lineEdit")

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

        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 270, 911, 16))
        self.line_2.setMinimumSize(QtCore.QSize(2, 2))
        self.line_2.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(210, 280, 20, 231))
        self.line_3.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(470, 280, 20, 231))
        self.line_4.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(640, 0, 20, 271))
        self.line.setStyleSheet("color: rgb(207, 207, 207);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_Pubblica = QtWidgets.QPushButton(Form)
        self.btn_Pubblica.setGeometry(QtCore.QRect(800, 390, 91, 21))
        self.btn_Pubblica.setMouseTracking(True)
        self.btn_Pubblica.setTabletTracking(True)
        self.btn_Pubblica.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                       "border-radius: 10px;\n"
                                       "font: 10pt \"Arial\";"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_Pubblica.setObjectName("pushButton_2")
        self.btn_Impostazioni = QtWidgets.QPushButton(Form)
        self.btn_Impostazioni.setGeometry(QtCore.QRect(800, 340, 91, 21))
        self.btn_Impostazioni.setMouseTracking(True)
        self.btn_Impostazioni.setTabletTracking(True)
        self.btn_Impostazioni.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"   #border per i bordi
                                       "border-radius: 10px;\n"
                                       "font: 10pt \"Arial\";"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);\n}") #hover: quando passo con la freccetta sopra al bordo cambia colore
        self.btn_Impostazioni.setObjectName("pushButton_3")
        self.btn_Logout = QtWidgets.QPushButton(Form)
        self.btn_Logout.setGeometry(QtCore.QRect(800, 440, 91, 21))
        self.btn_Logout.setMouseTracking(True)
        self.btn_Logout.setTabletTracking(True)
        self.btn_Logout.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                       "border-radius: 10px;\n"
                                       "font: 10pt \"Arial\";"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_Logout.setObjectName("pushButton_4")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(660, 10, 231, 241))
        self.scrollArea.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"border-radius: 20px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 231, 241))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(10, 290, 191, 211))
        self.listView.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"border-radius: 10px;")
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(Form)
        self.listView_2.setGeometry(QtCore.QRect(230, 290, 231, 211))
        self.listView_2.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"border-radius: 10px;")
        self.listView_2.setObjectName("listView_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Etichetta"))
        self.label.setText(_translate("Form",  "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">PySound Label</span></p></body></html>"))
        self.txt_nome.setPlaceholderText(_translate("Form", "  Search..."))
        self.btn_mostraTutte.setText(_translate("Form", "Mostra tutte"))
        self.btn_Pubblica.setText(_translate("Form", "Pubblica"))
        self.btn_Impostazioni.setText(_translate("Form", "Impostazioni"))
        self.btn_Logout.setText(_translate("Form", "Log out"))
        self.btn_search.setText(_translate("Form", "Cerca"))

"""app = QApplication([])
window = QWidget()
form = home_etichetta()
form.setupUi(window)
window.show()
app.exec()"""