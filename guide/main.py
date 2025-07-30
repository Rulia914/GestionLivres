import os    #Permet d'utiliser des fonctions et lancer des commandes du terminal comme "cls" par exemple qui permet d'effacer ce qui a été print. La fonction en question est appelé après chaque saisie de l'utilisateur (si jamais tu les cherches)

choix = 1

while choix != 0:
    print("***** MENU PRINCIPAL *****")
    print("1. Auteurs")
    print("2. Livres")
    print("0. Quitter")

    choix = int(input("Votre choix: "))
    os.system("cls")    #Permet d'effacer ce qui a été print juste avant. Tu peux faire le test et de l'enlever et voir par toi-même la différence :)

    if choix == 1:
        choixSousMenu = 1
        while choixSousMenu != 0:
            print("***** MENU AUTEURS *****")
            print("1. Afficher")
            print("2. Ajouter")
            print("3. Modifier")
            print("4. Supprimer")
            print("0. Retour")

            choixSousMenu = int(input("Votre choix: "))
            os.system("cls")

            if choixSousMenu == 1:
                print("Affichage des auteurs")
                #Ajouter la logique ici pour afficher les auteurs 
            elif choixSousMenu == 2:
                print("Ajout d'un auteur")
                #Ajouter la logique ici pour ajouter un auteur 
            elif choixSousMenu == 3:
                print("Modification d'un auteur")
                #Ajouter la logique ici pour modifier un auteur
            elif choixSousMenu == 4:
                print("Suppression d'un auteur")
                #Ajouter la logique ici pour supprimer un auteur
            else:
                print("Retour au menu principal")
                #Ne rien faire ici. Ce "else" n'est pas obligatoire, c'était juste pour montrer qu'on rentre bien dans cette alternative-ci et qu'on retour au menu principal ensuite :)

    elif choix == 2:
        choixSousMenu = 1
        while choixSousMenu != 0:
            print("***** MENU LIVRES *****")
            print("1. Afficher")
            print("2. Ajouter")
            print("3. Modifier")
            print("4. Supprimer")
            print("0. Retour")

            choixSousMenu = int(input("Votre choix: "))
            os.system("cls")

            if choixSousMenu == 1:
                print("Affichage des livres")
                #Ajouter la logique ici pour afficher les livres
            elif choixSousMenu == 2:
                print("Ajout d'un livre")
                #Ajouter la logique ici pour ajouter un livre
            elif choixSousMenu == 3:
                print("Modification d'un livre")
                #Ajouter la logique ici pour modifier un livre
            elif choixSousMenu == 4:
                print("Suppression d'un auteur")
                #Ajouter la logique ici pour supprimer un livre
            else:
                print("Retour au menu principal")
                #Ne rien faire ici. Ce "else" n'est pas obligatoire, c'était juste pour montrer qu'on rentre bien dans cette alternative-ci et qu'on retour au menu principal ensuite :)


    else:
        print("Fin de programme, au revoir.")
