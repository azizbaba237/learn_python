import sys
"""
Liste de courses 🛒 : 
Crée un programme qui permet de gérer une liste de courses. 
Il devrait proposer un menu avec des options comme :

    - ajouter un article à la liste.

    - afficher la liste complète.

    - retirer un article de la liste.

    - quitter le programme.

Compétences travaillées : listes, boucles (while et for), fonctions, et gestion de l'entrée utilisateur.
"""
# Déclaration des variables 
LISTE_ARTICLE = []
MENU  = """
     1. ajouter un article à la liste.
     2. afficher la liste complète.
     3. retirer un article de la liste.
     4. quitter le programme.
"""
MENU_OPTION = ["1", "2", "3", "4"]


# Titre et Description 
print()
print("------------  BIENVENU SUR CE PROGRAMME DE GESTION D'ARTICLE -----------")
print

# Main 
while True :
    # Initialisation du choix de l'utiliateur 
    choix_utilisateur = ""
    
    # Verification et recuperation du choix de l'utilisateur 
    if choix_utilisateur not in MENU_OPTION :
        choix_utilisateur = print(MENU)
        choix_utilisateur = input("Que souhaitez vous faire ?")
    
    # Si choix de l'utilisateur non valide 
    if choix_utilisateur not in MENU_OPTION :
        print()
        print("Choix non disponible, faites un choix valide.")
        continue
    
    # Ajouter un article a la liste 
    if choix_utilisateur == "1" :
        print()
        print("------------  AJOUTER UN ARTICLE -----------")
        print()
        article_a_ajouter = input("Entrez le nom de l'article que vous souhaitez ajouter : ")
        LISTE_ARTICLE.append(article_a_ajouter)
        print()
        print(f"L'article : ' {article_a_ajouter} ', a bien été ajouter à la liste.")
        
    # Pour afficher la liste des articles 
    elif choix_utilisateur == "2" :
        print()
        print("------------ LISTE DES ARTICLES DISPONIBLES -----------")
        print()
        if LISTE_ARTICLE :
            for i, article in enumerate(LISTE_ARTICLE, 1) :
                print(f" {i}. {article}")
        else :
            print("La liste des articles est vide.")
                
    # Pour supprimer une tâche 
    elif choix_utilisateur == "3":
        print()
        print("------------ LISTE DES ARTICLES DISPONIBLES -----------")
        print()
        if LISTE_ARTICLE:
            # Afficher la liste des articles disponibles 
            for i, article in enumerate(LISTE_ARTICLE, 1):
                print(f"{i} - {article}")
                
            try:
                # Récupération de l'indice de l'article à supprimer 
                indice_article_a_supprimer = int(input("Entrez le numéro de l'article que vous souhaitez supprimer : "))
                
                # Vérifier si l'indice est valide (entre 1 et la longueur de la liste)
                if 1 <= indice_article_a_supprimer <= len(LISTE_ARTICLE):
                    # Suppression de l'article (on soustrait 1 car l'affichage commence à 1 mais les indices de liste à 0)
                    article_a_supprimer = LISTE_ARTICLE.pop(indice_article_a_supprimer - 1)
                    print()
                    print(f"L'article '{article_a_supprimer}' a bien été supprimé.")
                else:
                    print("Oups ! Le numéro saisi n'est pas valide. Veuillez choisir un numéro dans la liste.")
                    
            except ValueError:
                print("Erreur : Veuillez saisir un numéro valide.")
        else:
            print("La liste des articles est vide.")
    
    # Pour quitter le programme 
    elif choix_utilisateur == "4" :
        print("Vous avez quitter le programme. ")
        sys.exit()