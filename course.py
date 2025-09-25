# GESTION DE LA LISTE DES COURSES 
import sys 

# Declaration de la liste 
LISTE_COUSES = []

# Menu 
MENU = """
    1. Ajouter une course 
    2. Afficher la liste des courses 
    3. Supprimer une course
    4. Vider la liste de course
    5. Quitter le programme
    6. Modifier une course
    👉 Votre choix : 
"""

# Choix d'une option 
CHOIX_MENU = ["1", "2", "3", "4", "5", "6"]

# Main 
while True :
    user_choice = ""
    if user_choice not in CHOIX_MENU :
        user_choice = input(MENU)
    if user_choice not in CHOIX_MENU :
        print("Oups !!! choix non valide... Faites un choix valide s'il vous plait.")
        continue
    
    #Ajouter une course 
    if user_choice == "1" :
        print()
        print("----- AJOUTER UNE COURSE SUR LA LISTE  ------")
        print()
        course = input("Entrez le nom de la course que vous souhaitez ajouter : ")
        LISTE_COUSES.append(course)
        print(f"{course}, a bien été ajouté à la liste des courses.")

    # Afficher la liste des courses 
    elif user_choice == "2" :
        if LISTE_COUSES :
            print()
            print("----- VOTRE LISTE DES COURSES ACTUELLE ------")
            print()
            for i, course in enumerate(LISTE_COUSES, 1) :
                print(f"{i} - {course}")
        else :
            print("La liste des courses est vide.")
    
    # Pour modifier une couse

    if user_choice == "6":
        if LISTE_COUSES:
            print()
            print("------ VOTRE LISTE DES COURSES ACTUELLE ------")
            print()
            for i, course in enumerate(LISTE_COUSES, 1):
                print(f"{i} - {course}")

            try:
                course_a_modifier_index = int(input("Entrez le numéro de la course que vous souhaitez modifier : ")) - 1
                
                # Vérification si l'index est valide
                if 0 <= course_a_modifier_index < len(LISTE_COUSES):
                    # Utilisation de input() pour le nouveau nom
                    nouvelle_course = input("Entrez le nom de la nouvelle course : ")
                    
                    # Récupère l'ancien nom pour l'affichage de confirmation
                    ancienne_course = LISTE_COUSES[course_a_modifier_index]
                    
                    # Modifie la course
                    LISTE_COUSES[course_a_modifier_index] = nouvelle_course
                    
                    #Affichage de confirmation
                    print(f"La course : '{ancienne_course}', a été modifiée par : '{nouvelle_course}'. ")
                    print(f"La nouvelle liste de courses est : {LISTE_COUSES}")
                else:
                    print("Numéro de course invalide.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")
        else:
            print("La liste des courses est vide.")
    
    # Supprimer une course 
    elif user_choice == "3" :
        if LISTE_COUSES :
            print()
            print("----- VOTRE LISTE DES COURSES ACTUELLE ------")
            print()
            for i, course in enumerate(LISTE_COUSES, 1) :
                print(f"{i} - {course}")
            courserPosition = int(input("Entrer le numero de la course que vous soujaitez supprimer :"))
            course_a_supprimer = LISTE_COUSES.pop(courserPosition - 1)
            print(f"La course: {course_a_supprimer}, a bien été retirée la liste.")
        else : 
            print("Rien à supprimer : la liste des courses est vide.")
    
    # Pour vider la list des course 
    elif user_choice == "4" :
        if LISTE_COUSES :
            LISTE_COUSES.clear()
            print("La liste des courses a bien été vidée. ")
        else :
            print("La liste est vide : rien a supprimer.")
    
    # Pour quitter le programme 
    elif user_choice == "5" :
        print("Vous avez quitté le programme : a bientot... ")
        sys.exit()