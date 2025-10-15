"""
    Gestion d'étudiants

        Objectif : Manipuler des listes d'objets
        Concepts : Classes, listes, méthodes de classe
"""
class Etudiant :
    """ classe Etudiant"""

    def __init__(self, nom, prenom, matricule):
        """ initialisation de la classe Etudiant """
        self.nom = nom
        self.prenom = prenom
        self.matricule = matricule
        self.note = []

    def __str__(self):
        """ return le string """
        return f"{self.nom}"

    def calculer_moyenne(self):
        """ calculer la moyenne """
        if not self.note :
            return 0
        somme = sum(self.note)
        moyenne = somme / len(self.note)
        print(f"Le moyenne est {moyenne:.2f}")
        return moyenne

    def est_admis(self):
        """ Renvoie la decision """
        moyenne = self.calculer_moyenne()
        if moyenne >= 10:
            return True
        else:
            return False

class Classe :
    """ classe  Etudiant"""

    def __init__(self):
        """ initialisation de la classe Etudiant"""
        self.liste_etudiant = []

    def enregistrer_etudiant(self, etudiant : Etudiant):
        """ enregistrer un etudiant """

        self.liste_etudiant.append(etudiant)
        print(f"L'etudiant {etudiant.nom} a bien été crée ")

    def ajouter_etudiant(self):
        """ Ajouter un etudiant en la liste """

        while True :
            try :

               # Recuperer le nom
               nom = input("Entrez la nom ou tapez (q) pour quitter :").strip().lower()
               if nom == 'q':
                   break

               # Récuperer le prenom
               prenom = input("entrez le prenom : ").strip().lower()

               # Recuprer le matricule
               matricule = input("Entrez le matricule : ").strip().lower()
               if not matricule:
                   print("Le matricule est oligatoire.")
                   continue

               # Recuperer la note
               try :
                   note = float(input("Entrez la note"))
               except ValueError :
                   print("Errerur de saisie : le note doit etre un nombre.")
                   continue

              # Enregistrer le nouvel etudiant
               nouvel_etudiant = Etudiant(nom, prenom, matricule)

               # Ajouter la note a l'etudiant
               nouvel_etudiant.note.append(note)

               self.enregistrer_etudiant(nouvel_etudiant)
               print(f"L'etudiant {nom}, prenom : {prenom}, matricule : {matricule}, note : {note} a bien ete cree. ")

               continuer = input("Voulez vous ajoutrer un autre etudiant o/n ")
               if continuer not in ['o', 'oui'] :
                   break
            except  Exception as e:
                print(f"Erreur : {e}")

    def moyenne_classe(self):
        """ Calculer la moyenne de la classe """

        # verifie s'il ya les eutdiant dans la liste
        if not self.liste_etudiant :
            print("Il y a aucun etudiant dans la liste. la moyenne de la classe est = 0")
            return 0

        somme_moyenne_classe = 0

        # PArcourir le liste de etudiants
        for etudiant in self.liste_etudiant:
            # Calculer la moyenne de l'etudiant
            moyenne_etudiant  = etudiant.calculer_moyenne()

            # cumuler les moyennes
            somme_moyenne_classe += moyenne_etudiant


        # Calculer la moyenne generale
        nombre_etudiant = len(self.liste_etudiant)
        moyenne_generale = somme_moyenne_classe / nombre_etudiant

        print("-" * 30)
        print(f"La MOYENNE GÉNÉRALE de la classe est : {moyenne_generale:.2f}")
        print("-" * 30)

        return moyenne_generale




# Main
nouvel_etuduant = Classe()
nouvel_etuduant.ajouter_etudiant()
print()
nouvel_etuduant.moyenne_classe()