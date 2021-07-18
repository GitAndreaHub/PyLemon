import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

from Pubblicazione.Model.pubblicazione_Dati_utente import DataPick
from Pubblicazione.View.Caricamento_brano_etichetta import Caricamento_brano_etichetta
from Pubblicazione.Model.pubblicazione_gestione import Gestione_mp3, Gestione_json

''' Classe di controllo per le funzionalità dell caricamento di un brano per un'etichetta discografica'''
class Controller_Caricamento_Brano_Etichetta(QtWidgets.QWidget, Caricamento_brano_etichetta):
    switch_window_1 = QtCore.pyqtSignal()
    switch_window_2 = QtCore.pyqtSignal()
    switch_window_3 = QtCore.pyqtSignal()

    ''' Nel costruttore andiamo a definire delle variabili utili a seguire e collegare i pulsanti della view con delle fuzioni definite sotto'''
    def __init__(self,verifica_album,nome_album):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        pick = DataPick()
        myData = pick.return_credenziali()
        self.nome_etichetta = myData[1]
        self.cognome_etichetta = myData[2]

        self.Gestione_mp3 = Gestione_mp3()
        self.Gestione_Json = Gestione_json()

        self.verifica_album = verifica_album
        self.nome_album = nome_album
        self.path = ""

        self.controllo_fine_album = False

        self.btn_Scegli_file.clicked.connect(self.btn_scegli_file_handler)
        self.btn_Pubblica.clicked.connect(self.btn_pubblica_handler)
        self.btn_Back.clicked.connect(self.btn_back_handler)

    '''Pop Up Pinestra'''
    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    '''Funzione per pubblicare un brano collegato al pulsante btn_pubblica'''
    def btn_pubblica_handler(self):
        if self.Controllo_pubblicazione() is True:
            self.Gestione_Json.carica_brano_su_JSON(self.nome, self.etichetta, self.album, self.id, self.contatore)
            self.Gestione_mp3.Carica_mp3(self.nomefile2)
            self.Controllo_emit()


    def Controllo_pubblicazione(self):
        try:
            path= str(self.path)
            print(path)
            stringa_split = path.split(", ")
            nomefile = stringa_split[0].replace("(", "")
            print(nomefile)
            self.nomefile2 = nomefile.replace("'","")

            self.nome = self.lineEdit.text()
            self.etichetta = self.lineEdit_2.text()
            if self.nome and self.etichetta:
                if self.verifica_album == False:
                    self.album = self.nome
                else:
                    self.album = self.nome_album

                self.contatore = 0
                self.id = self.Gestione_mp3.json_contatore["contatore_id"]+1
                if path == '':
                    raise Exception

                else:
                    if self.verifica_album:
                        self.pop_message(text="Brano caricato con successo")
                    else: self.pop_message(text="Brano caricato con successo")
                    return True

            else:
                self.pop_message(text="Immetti nome canzone e/o artista")
                return False
        except Exception:
            self.pop_message(text="Errore nel file da caricare.\n"
                                  "Il nome del file non deve contenere parentesi tonde,quadre,graffe e le virgolette")
            return False

    def Controllo_emit(self):
        if self.verifica_album is False:
            self.switch_window_1.emit()

        if self.verifica_album is True:
            if self.controllo_fine_album is True:
                self.switch_window_1.emit()
            else: self.switch_window_3.emit()

    '''Funzione che permette di visualizzare un File Dialog e prende il path del file, collegata al pulsante btn_scegli_file'''
    def btn_scegli_file_handler(self):
        self.path = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a data file',
            directory=os.getcwd(),
            filter='Data File (*.mp3)',
        )

    '''Funzione collegata al pulsante btn_back e permette di far visualizzare un'altra finestra'''
    def btn_back_handler(self):
        self.switch_window_2.emit()