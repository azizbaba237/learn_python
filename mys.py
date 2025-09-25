from random import randint

# Initialisation du jeu
nombre_mystere = randint(1, 10)
nombre_essai = 5

print("------ BIENVENU AU JEU DU NOMBRE MYSTERE ---------")
print("Le principe est très simple : vous devez deviner le nombre mystère en 5 tentatives")

while nombre_essai > 0:
    print(f"Il vous reste {nombre_essai} essais.")
    nombre_a_deviner_str = input("Entrez un nombre : ")

    # Vérification si l'entrée est un nombre
    if not nombre_a_deviner_str.isdigit():
        print("Entrée non valide : veuillez entrer un nombre.")
        continue  # Passer directement à la prochaine itération de la boucle

    # Conversion en entier et vérification
    nombre_a_deviner = int(nombre_a_deviner_str)

    if nombre_a_deviner < nombre_mystere:
        print("C'est plus !")
    elif nombre_a_deviner > nombre_mystere:
        print("C'est moins !")
    else:  # Si nombre_a_deviner est égal à nombre_mystere
        print(f"Bravo ! Vous avez gagné ! Le nombre mystère était bien {nombre_mystere}.")
        print(f"Vous l'avez fait en {nombre_essai} essai.")
        break  # Sortir de la boucle si la réponse est correcte

    # Décrémentation du nombre d'essais
    nombre_essai -= 1

# Message de fin de jeu si la boucle se termine (nombre d'essais = 0)
if nombre_essai == 0:
    print(f"Vous avez perdu. Le nombre mystère était {nombre_mystere}.")