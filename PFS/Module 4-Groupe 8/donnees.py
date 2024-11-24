import csv
## Crée une structure de donnés Pouls
class Pouls():
    def __init__(self, pouls, temps):
        self.pouls = pouls
        self.temps = temps
    def __str__(self):
        return f"Pouls(pouls={self.pouls}, temps={self.temps})"

## Charge les donnés du fichier .csv dans une liste de pouls
poulss = []
x = []
y = []
def charger_donnees(fichier):
     with open (fichier, "r") as mon_fichier:
        lecteur_csv = csv.reader(mon_fichier,delimiter=';')
        for row in lecteur_csv:
          ## transformation de chaine en caractere
          a = row[1]
          x.append(a)
          b = row[0]
          y.append(b)
          poulss.append(Pouls(float(a), int(b)))

## Affichage des donnees selon le fichier csv
def afficher_donnees():
    for donnee in poulss :
        print(donnee)

## Fonction pour ajouter des donnees dans un fichier csv
def ajouter_donnees(temps,pouls):
    poulss.append(Pouls(float(temps), int(pouls)))
def supprimer_donnee(temps):
    for donnee in poulss:
        if donnee.temps == temps:
            poulss.remove(donnee)
            return True
    return False
def trier_donnees():
    poulss.sort(key=lambda x: x.temps)

def rechercher_donnee(temps):
    for donnee in poulss:
        if donnee.temps == temps:
            return donnee
    return None