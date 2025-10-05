"""Jeu du chat et la sourie

    Returns:
        jeu: le chat doit attraper la sourie
"""

class Personnage:
    # Constructeur pour initialiser les attributs
    def __init__(self, nom: str, position_x: int, position_y: int):
        self.nom = nom
        self.position_x = position_x
        self.position_y = position_y

    # Méthode pour un affichage lisible de l'objet
    def __str__(self):
        return f"Personnage : {self.nom} (Position: X={self.position_x}, Y={self.position_y})"

    # Méthodes de déplacement
    def avancer_droite(self):
        self.position_x += 1
        print(f"-> {self.nom} avance à droite.")

    def avancer_gauche(self):
        self.position_x -= 1
        print(f"<- {self.nom} recule à gauche.")

    def avancer_haut(self):
        self.position_y += 1
        print(f"^ {self.nom} monte.")

    def avancer_bas(self):
        self.position_y -= 1
        print(f"v {self.nom} descend.")


def verification_capture(chat, souris):
    """Vérifie si le chat et la souris sont sur la même position."""
    if chat.position_x == souris.position_x and chat.position_y == souris.position_y:
        print("\n*** CAPTURE ! ***")
        print(f"Le chat {chat.nom} a attrapé la souris {souris.nom} à la position ({chat.position_x}, {chat.position_y})!")
        return True
    else:
        print("\nLe chat n'a pas encore attrapé la souris. Continuez le jeu !")
        return False

# --- Création des instances (Objets) ---
chat = Personnage("Lou", 2, 3)
souris = Personnage("Doe", 2, 3) # La souris est à droite du chat initialement

print("--- Début du Jeu ---")
print(chat)
print(souris)

# --- Déplacements ---
print("\n--- Tour 1 ---")
# Le chat avance à droite (2 -> 3)
chat.avancer_droite()
# La souris reste
print(souris) 

verification_capture(chat, souris)

print("\n--- Tour 2 ---")
# Le chat avance encore à droite (3 -> 4)
chat.avancer_droite()
# La souris recule à gauche (4 -> 3)
souris.avancer_gauche()

# --- Vérification finale ---
verification_capture(chat, souris)

# Affichage amélioré grâce à la méthode __str__
print("\n--- État Final ---")
print(chat)
print(souris)