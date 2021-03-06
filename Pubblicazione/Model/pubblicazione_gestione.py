import os
import shutil
import json
from PyQt5 import QtWidgets

'''Classe responsabile della gestione dei file .mp3 presenti sulla piattaforma'''
class Gestione_mp3():

    '''Nel costruttore vado a leggere il file ContatoreBrani.json'''
    def __init__(self):
        self.verifica_nome_mp3 = True

        with open('Data/Json/ContatoreBrani.json', 'r') as j:
            self.json_contatore = json.load(j)

    '''Pop Up Finestra'''
    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    '''Funzione che, dato il path del file, carica il file sulla piiattaforma'''
    def Carica_mp3(self, percorsofile):
        contatoreid = self.json_contatore["contatore_id"]
        if os.path.isfile(percorsofile):
            oldfile1 = str(percorsofile)
            oldfile2 = oldfile1.split("/")
            nomefile= str(oldfile2[len(oldfile2)-1])
            id=int(contatoreid)
            id = id+1
            newnomefile = str(id) + ".mp3"
            shutil.copy(percorsofile, 'Data/mp3')
            shutil.move('Data/mp3/' + nomefile, 'Data/mp3/' + newnomefile)
            self.json_contatore["contatore_id"] = id
            with open("Data/Json/ContatoreBrani.json", "w") as write_file:
                json.dump(self.json_contatore, write_file)
            return True
        else : return False


    '''Funzione che, dato in input, l'id del brano, lo elimina dalla piattaforma'''
    def Elimina_mp3(self, id):

        try:
            os.remove('Data/mp3/'+str(id)+'.mp3')
            self.pop_message(text="Eliminazione avvenuta con successo.")
            self.pop_message(text="Per vedere gli aggiornamenti rieffettuare l'accesso")
            return True

        except:
            self.pop_message(text="Errore nella rimozione.\n"
                                      "Prova ad effettuare il logout e a riaccedere.")
            return False

'''Classe responsabile della gestione del file info_brani.json'''
class Gestione_json():


    '''Nel costruttore si esegue la lettura del file memorizzandola nell'attributo json_data'''
    def __init__(self):

        with open('Data/Json/info_brani.json', 'r') as j:
            self.json_data = json.load(j)


    '''Metodo che aggiunge coppie chiave-valore all'interno dell'attributo json_data(usato nell'attivit?? di pubblicazione).
       A questo punto si esegue la sovrascttura del file con i dati aggiornati'''
    def carica_brano_su_JSON(self, nome,artista,album,id,contatore):
        oggettobrano = {"Titolo": nome.title(), "Artista": artista.title(), "Album": album.title(), "id": id, "contatore": contatore }
        if self.json_data != None:

            self.json_data.append(oggettobrano)
            with open("Data/Json/info_brani.json", "w") as write_file:
                json.dump(self.json_data, write_file)

        else:
            self.json_data = oggettobrano
            with open("Data/Json/info_brani.json", "w") as write_file:
                json.dump(self.json_data, write_file)


    '''Metodo che ritorna l'id corrispondente di un brano dati titolo e album'''
    def ricerca_id(self, titolo, album):
        U = self.json_data
        for i in U:
            if (i["Titolo"] == titolo) and (i["Album"] == album):
                ID = i["id"]
        return ID



    '''Metodo che incrementa il valore della chiave CONTATORE a seguito di riproduzioni musicali.
       Sovrascittura del file per il suo aggiornamento'''
    def incremento_conta(self, titolo, album):
        data = self.json_data
        posi = 0
        for i in data:
            posi =posi + 1
            if (i["Titolo"] == titolo) and (i["Album"] == album):
                i["contatore"] += 1.0
                data[posi-1] = i
                break

        with open("Data/Json/info_brani.json", "w") as write_file:
            json.dump(data, write_file)



    '''Metodo ritorna l'id corrispondente ad un titolo di un brano.
       Utilizzato per la statistica I MIEI BRANI'''
    def getTitolo_da_Id(self, id):
        titolo =""
        for i in self.json_data:
            if i["id"] == float(id):
                titolo = i["Titolo"]
        return titolo


    '''Metodo che va ad elminare un object dal json file, dati il nome dell'artista ed il titolo del brano '''
    def elimina_object(self, nome_artista, titolo_brano):
        for i in self.json_data:
            if nome_artista == i["Artista"] and titolo_brano == i["Titolo"]:
                mp3 = Gestione_mp3()
                id = self.ricerca_id(i["Titolo"], i["Album"])
                if mp3.Elimina_mp3(id):
                    if i is self.json_data[len(self.json_data)-1]:
                        self.decrementa_conta_id()
                    self.json_data.remove(i)
                    with open("Data/Json/info_brani.json", "w") as write_file:
                        json.dump(self.json_data, write_file)
                    break
    '''---Decrememta il contatore delle canzoni se il brano da eliminare ?? situato 
        in ultima posizione del "json_data"---'''

    def decrementa_conta_id(self):
        with open('Data/Json/ContatoreBrani.json', 'r') as j:
            self.json_conta_id = json.load(j)

        self.json_conta_id["contatore_id"] = self.json_conta_id["contatore_id"] - 1
        with open("Data/Json/ContatoreBrani.json", "w") as write_file:
            json.dump(self.json_conta_id, write_file)


    '''Metodo che ritorna l'attributo json_data'''

    def get_jsonobject(self):
        return self.json_data