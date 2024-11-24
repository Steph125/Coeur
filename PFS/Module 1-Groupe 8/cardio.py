import serial
import csv

##Definition des blocs d'instructions a essayer et executer en cas d'erreur

try:
        #fonction setup
        port=serial.Serial("COM7",9600,timeout=1)
except:
        print("Votre appareil n'est pas connecté")

    #Enregistrement et stockage des donnees
def stockage():
        compt=0
        while compt<=10:
            recup= str(port.readline())
            valeur=recup[2:][:-5]
            with open("data.csv","a") as file:
                file.write(valeur + "\n")
            compt= compt + 1

    ##Definition de la fonction de conversion du fichier csv en un fichier txt
def convertir(file):
        name= 'file'
        with open (name,"r") as conv:
            num=csv.reader(conv, delimiter=';')
            for l in num:
                with open ("data.txt", "w+") as file_1:
                    file_1.write(num)


    #Nettoyage des donnees brutes de l'arduino
def nettoie(fichier,liste,liste1):
        name= 'data.csv'
        with open(name, "r") as number:
            fichierCSV = csv.reader(number)
            liste=[]
            liste1=[]
            for l in fichierCSV:
                x=int(line[0])
                y=int(line[1])
                liste.append(x)
                liste1.append(y)
                period=liste1[4] ##takes the last value of time in the list time


    #Calcul du bps:nombre de battements par seconde
def calcul_bps(bps):
        bps=0
        rawdata=[]
        perioddata=[]
        stockage()
        data="data.csv"
        nettoie(data,rawdata,perioddata)
        for i in rawdata:
            if (rawdata[i] == 0) and (rawdata[i] < 300):
                bps = 0
                return bps
            elif (rawdata[i] >= 300) and (rawdata[i] <= 392):
                bps = bps + 1
                return bps
            else:
                print("Impossible de calculer de le bps")

    #Calcul du pouls/frequence cardiaque à partir du bps
def calcul_pouls(bps):
        pouls=60*bps
        return pouls

    #Enregister le pouls et la duree d'execution
def enregistrement(pouls,period):
        with open("results.csv","a") as fichier:
            fichier.write(pouls +";" + "\n")
            fichier.write(period +";" + "\n")
