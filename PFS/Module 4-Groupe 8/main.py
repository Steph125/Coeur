from donnees import *
from action import *
from menu import *
# chemin vers le fichier CSV
fichier = "Battements.csv"

# chargement des données
mesures = charger_donnees(fichier)

# affichage du menu et traitement des actions de l'utilisateur
while True:
    menu()

