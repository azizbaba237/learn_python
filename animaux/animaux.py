"""
    Objectif : Comprendre l'héritage et le polymorphisme
    Concepts : Héritage, super(), méthodes redéfinies
"""


class Animal:
    """ Classe d'animal """

    def __init__(self, nom: str, age: int):
        """ Constructeur """
        self.nom = nom
        self.age = age

    def __str__(self):
        """ Retourne une représentation lisible de l'animal """
        return f"{self.nom} (Âge: {self.age} ans)"

    def se_presenter(self):
        """ Retourne le nom et l'age de l'animal """
        print(f"Je suis {self.nom} et j'ai {self.age} ans.")

    def faire_du_bruit(self):
        """ Indique que la méthode doit être implémentée par les sous-classes """
        raise NotImplementedError("La sous-classe doit implémenter la méthode faire_du_bruit().")


class Chien(Animal):
    """ Classe Chien """

    def __init__(self, nom: str, age: int):
        super().__init__(nom, age)

    def faire_du_bruit(self):
        """ Le chien fait woof """
        print(f"{self.nom} fait : Woof!")


class Chat(Animal):
    """ Classe Chat """

    def __init__(self, nom: str, age: int):
        super().__init__(nom, age)

    def faire_du_bruit(self):
        print(f"{self.nom} fait : Miaou.")


class Oiseau(Animal):
    """ Classe Oiseau avec attribut 'peut_voler' """

    def __init__(self, nom: str, age: int, peut_voler: bool):
        super().__init__(nom, age)
        self.peut_voler = peut_voler

    def voler(self):
        if self.peut_voler:
            print(f"{self.nom} s'envole.")
        else:
            print(f"{self.nom} est un oiseau qui ne vole pas.")

    def faire_du_bruit(self):
        print(f"{self.nom} fait : Cui-cui.")


# main
animaux = [Chien("Rex", 5), Chat("Croquette", 12), Oiseau("Titi", 9, True), Oiseau("Manchot", 3, False)]
print("=" * 50)
print("DÉMONSTRATION DU POLYMORPHISME ET DE L'HÉRITAGE")
print("=" * 50)

for animal in animaux:
    # 1. Utilisation de la méthode __str__
    print(animal)

    # 2. Utilisation d'une méthode héritée
    animal.se_presenter()

    # 3. Utilisation d'une méthode polymorphique
    animal.faire_du_bruit()

    # 4. Utilisation de la méthode spécifique (avec vérification pour éviter les erreurs)
    if isinstance(animal, Oiseau):
        animal.voler()

    print("-" * 50)