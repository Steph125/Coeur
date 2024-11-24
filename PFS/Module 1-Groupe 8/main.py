##Importation des modules
from cardio import *

##Declaration des variables
bps = 0
pouls = 0

##Fonction loop
while True:
    ##calcul du pouls et enregistrement du pouls calcule ainsi que de la duree
    bps = calcul_bps(bps)
    pouls = calcul_pouls(bps)
    enregistrement(pouls)
    port.write(pouls)  ## envoi le pouls vers Arduino

##Appel de la fonction de conversion et construction du graphe de l'evolution du pouls en fonction du temps
convertir(results.csv)
values, time = np.loadtxt('data.txt', delimiter=';', unpack=True)

