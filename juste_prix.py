"""
un programme qui génère un nombre aléatoire entre 1 et 100. 
L'utilisateur doit deviner ce nombre. Après chaque tentative,
le programme lui indique si le nombre à deviner est plus grand ou plus petit.
Le jeu s'arrête quand l'utilisateur trouve la bonne réponse ou pas.

"""
# Import de randiint qui va permetre de gener les nombres aleatoires 
from random import randint

# Délaration des variables 
juste_prix = randint(1, 100)
nombre_de_tentative = 5 

# Titre et description du jeu 
print()
print("--------- BIENVENU SUR LE JEU DU JUSTE PRIX ---------------")
nombre_de_tentative_s = 's' if nombre_de_tentative > 1 else ''
print(f"Le principe du jeu est tel que : vous devez deniner le bon prix en {nombre_de_tentative} tentative{nombre_de_tentative_s}. ")
print()

# Main 
while nombre_de_tentative > 0 :
    print()
    nombre_de_tentative_s = 's' if nombre_de_tentative > 1 else ''
    print(f"------------ Vous avez {nombre_de_tentative} tentative{nombre_de_tentative_s}. ------------------")
    prix_a_deviner_str = input("Entrez un prix s'il vous plait :")
    print()
    
    # Tester si le prix entrer par l'utilisateur est un nombre 
    if not prix_a_deviner_str.isdigit() :
        print("Prix non valide, entrez un nombre s'il vous plait.")
        continue
    
    # Transformation du nombre entrer en int 
    prix_a_deviner = int(prix_a_deviner_str)
    
    # Logique du programme une fois que le nombre entrer est un nombre 
    if prix_a_deviner < juste_prix :
        print("C'est plus grand !")
    elif prix_a_deviner > juste_prix :
        print("C'est plus petit !")
    else :
        print(f"vous avez gagné 🎉🎉😉😉 en {nombre_de_tentative} tentative{nombre_de_tentative_s}")
        print(f"Le Juste prix etait : {juste_prix}")
        break
        
    # Décrementation du nombre de tentative 
    nombre_de_tentative -= 1 
        
    # Si le joueur ne trouve pas le juste prix dans le nombre de tentative imparti 
    if nombre_de_tentative == 0 :
        print()
        print(f"Oups !!! vous avez perdu, le juste prix a deviner etait : {juste_prix}")
        print("Relancez le programme pour retenter votre change... 😉😉")
    