
from PyQt5 import QtCore, QtWidgets


'''---------------Classe view caricamento brano etichetta------------'''

class Caricamento_brano_etichetta(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(461, 342)
        Form.setMinimumSize(QtCore.QSize(461, 342))
        Form.setMaximumSize(QtCore.QSize(461, 342))
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")


        '''--------------Titolo finestra------------'''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 30, 131, 41))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
                                 "font: 30pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")


        '''------------Sottotitolo------------'''

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 70, 131, 16))
        self.label_2.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_2.setObjectName("label_2")


        '''-------------Bottone scegli file------------'''

        self.btn_Scegli_file = QtWidgets.QPushButton(Form)
        self.btn_Scegli_file.setGeometry(QtCore.QRect(180, 110, 101, 31))
        self.btn_Scegli_file.setMouseTracking(True)
        self.btn_Scegli_file.setTabletTracking(True)
        self.btn_Scegli_file.setStyleSheet("*{background-color: rgb(207, 207, 207);\n"
                                           "color: rgb(0, 0, 0);\n"
                                           "border-radius: 10px;\n"
                                           "color: rgb(0, 0, 0);\n}"
                                           "*:hover{border: 5px solid rgb(221, 215, 25);\n}")
        self.btn_Scegli_file.setObjectName("pushButton")



        '''---------------Bottone pubblica---------------'''

        self.btn_Pubblica = QtWidgets.QPushButton(Form)
        self.btn_Pubblica.setGeometry(QtCore.QRect(250, 280, 81, 21))
        self.btn_Pubblica.setMouseTracking(True)
        self.btn_Pubblica.setTabletTracking(True)
        self.btn_Pubblica.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                        "border-radius: 10px;\n"
                                        "color: 'white';}" +
                                        "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_Pubblica.setObjectName("pushButton_2")


        '''-------------Bottone indietro-----------'''

        self.btn_Back = QtWidgets.QPushButton(Form)
        self.btn_Back.setGeometry(QtCore.QRect(130, 280, 81, 21))
        self.btn_Back.setMouseTracking(True)
        self.btn_Back.setTabletTracking(True)
        self.btn_Back.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                    "border-radius: 10px;\n"
                                    "color: 'white';}" +
                                    "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_Back.setObjectName("btn_back")


        '''-------------Nome brano-------------'''

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 101, 16))
        self.label_3.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 190, 181, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                    "color: rgb(55, 55, 55);\n"
                                    "border-radius: 5px;")
        self.lineEdit.setObjectName("lineEdit")


        '''-------------Nome artista---------------'''

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 170, 101, 16))
        self.label_4.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_4.setObjectName("label_4")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 190, 181, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                      "color: rgb(55, 55, 55);\n"
                                      "border-radius: 5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ""))
        self.label_2.setText(_translate("Form", "Pubblicazione brano"))
        self.label.setText(_translate("Form", "PyLemon"))
        self.btn_Scegli_file.setText(_translate("Form", "Scegli file"))
        self.btn_Pubblica.setText(_translate("Form", "Pubblica"))
        self.btn_Back.setText(_translate("Form", "Indietro"))
        self.label_3.setText(_translate("Form", "Nome brano:"))
        self.label_4.setText(_translate("Form", "Nome artista:"))
