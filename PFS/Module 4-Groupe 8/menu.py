from action import *
def menu ():
    print("1. Afficher les données dans l’ordre du fichier .csv")
    print("2. Afficher les données en ordre croissant/décroissant (selon le temps, selon le pouls) ")
    print("3. Rechercher et afficher les données pour un temps particulier")
    print("4. Afficher la moyenne de pouls dans une plage de temps donnée")
    print("5. Afficher le nombre de lignes de données actuellement en mémoire")
    print("6. Rechercher et afficher les max/min de pouls (avec le temps associé)")
    print("7.  Quitter l’application")

    option = int(input("Entrez un chiffres : "))
    if (option == 1) :
       afficher_donnees()
    elif (option == 2):
       action = str(input("Choisissez dans ordre croissant vous voulez afficher (temps(1) ou pouls(2)) ou decroissant (temps(3) ou pouls(4)): "))
       if (action == "1"):
         trier_donnees_par_temps()
       if (action == "2"):
         trier_donnees_par_pouls()
       if (action == "3"):
         trier_donnees_par_temps_decroissant()
       if (action == "4"):
         trier_donnees_par_pouls_decroissant()
    elif (option == 3):
        rechercher_donnees_par_temps()
    elif (option == 4):
        calculer_moyenne_pouls()
    elif (option == 5):
        afficher_nombre_donnees()
    elif (option == 6):
        rechercher_pouls_max_min()
    elif (option == 7):
        exit()
    else:
        print("valeur invalide. Choissisez un valeur de 1-7")
        menu()
 
menu()