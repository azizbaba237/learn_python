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

    def ajouter_note(self, note):
        """ Ajouter la note """
        try :
            # S'assurer qu'on ajoute bien une note
            self.note.append(float(note))

        except ValueError :
            print("Erreur : la valeur entrée doit etre un nombre.")

    def calculer_moyenne(self):
        """ calculer la moyenne """
        if not self.note :
            return 0
        somme = sum(self.note)
        moyenne = somme / len(self.note)
        print(f"{moyenne:.2f}")
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

    def afficher_tous_les_etudiants(self):
        """ Affiche le nom, le prénom, les notes et le statut d'admission de tous les étudiants de la liste. """

        print("\n--- Liste et statut des étudiants ---")

        if self.liste_etudiant:
            for etudiant in self.liste_etudiant:
                etat_admission = "Admis" if etudiant.est_admis() else "échoué"
                moyenne_individuelle = etudiant.calculer_moyenne()

                print(f"\n Nom : {etudiant.nom} \n Prenom : {etudiant.prenom} \n Note : {etudiant.note} \n Moyenne : {moyenne_individuelle} \n Décision : {etat_admission}")
        else :
            print("La liste des etudiants est vide.")
            return

    def ajouter_etudiant(self):
        """ Ajouter un etudiant en la liste """

        while True :
            try :

               # Recuperer le nom
               nom = input("Entrez le nom ou tapez (q) pour quitter :").strip().lower()
               if nom == 'q':
                   break

               # Récuperer le prenom
               prenom = input("entrez le prenom : ").strip().lower()

               # Recuprer le matricule
               matricule = input("Entrez le matricule : ").strip().lower()
               if not matricule:
                   print("Le matricule est obligatoire")
                   continue

               # Enregistrer le nouvel etudiant
               nouvel_etudiant = Etudiant(nom, prenom, matricule)

               # Boucle ajouter notes
               while True :
                   try :
                       saisi_note = input("Entrez la note ou tapez (f) pour finir : ").strip().lower()
                       if saisi_note == 'f':
                           break

                       # utiliser la methode d'Etuduant
                       nouvel_etudiant.ajouter_note(saisi_note)

                   except ValueError :
                       print("Errerur de saisie : la note doit etre un nombre.")
                       continue
               # verifie au moins une note a été saisie
               if not nouvel_etudiant.note :
                   print("Attention l'etudiant n'a pas de note ")


               self.enregistrer_etudiant(nouvel_etudiant)
               print(f"L'etudiant {nom}, prenom : {prenom}, matricule : {matricule} a été crée avec succès. ")

               continuer = input("Voulez-vous ajouter un autre tudiant o/n ")
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

        # Parcourir le liste de etudiants
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

        # retourne la moyenne generale
        return moyenne_generale

    def meilleur_etudiant(self):
        """ retourne l'étudiant avec la meilleure moyenne """

        # Verifie si l'etudiant existe dans la liste
        if not self.liste_etudiant :
            return "La liste des etudiant est vide."

        # Initialisation du meilleur etudiant et de la moyenne maximale
        meilleur = None
        moyenne_maximale = -1

        # boubler dans la liste des etudiants
        for etudiant in self.liste_etudiant :
            # calculer la moyenne individuelle
            moyenne_actuelle = etudiant.calculer_moyenne()

            # obtenir le meilleur etudiant
            if moyenne_actuelle > moyenne_maximale :
                moyenne_maximale = moyenne_actuelle
                meilleur = etudiant

        # Affichage
        print("-" * 30)
        print(f"Le meilleur Etudiant est : {meilleur.nom} {meilleur.prenom}")
        print(f"Sa moyenne est de : {moyenne_maximale:.2f}")
        print("-" * 30)


    def taux_reussite(self):
        """ retourne le pourcentage d'étudiants admis """

        # verifie si le liste des etuduant est vide
        if not self.liste_etudiant :
            return "Aucun etudiant n'est enregistrer."

        # Initialisation
        admis_compteur = 0

        # Recuperation du nombre d'etudiant
        nombre_total_etudiants = len(self.liste_etudiant)

        # Boucler
        for etudiant in self.liste_etudiant:
            if etudiant.est_admis():
                admis_compteur += 1

        # Calcul du taux de reussite
        taux_de_reussite = (admis_compteur / nombre_total_etudiants) * 100

        # Affichage
        print('-' * 30)
        print(f"Le Nombre d'etudiant inscrit est de : {nombre_total_etudiants}")
        print(f"Le nombre d'admis est de : {admis_compteur}")
        print(f"Le taux de reussite est de : {taux_de_reussite:.2f} % ")
        print('-' * 30)
        return taux_de_reussite

# Main
if __name__=="__main__" :

    # Creation de l'instance de la classe
    etudiant = Classe()

    while True :

        print("************** Porgramme de Gestion des Etudiants ******************")
        print("1. Ajouter un Etudiant")
        print("2. voir la moyenne de la calsse ")
        print("3. voir le meilleur Etudiant")
        print("4. voir le taux de reussite ")
        print("5. afficher tous les etudiants ")
        print("q. Quitter le programme")


        try :
            print()
            choix = input("Que souhaitez-vous faire ? ")

            if choix == '1' :
                etudiant.ajouter_etudiant()
            elif choix == '2' :
                etudiant.moyenne_classe()
            elif choix == '3' :
                etudiant.meilleur_etudiant()
            elif choix == '4' :
                etudiant.taux_reussite()
            elif choix == '5' :
                etudiant.afficher_tous_les_etudiants()
            elif choix == 'q':
                print("Vous avez quitter le programme.")
                break

        except Exception as e :
            print(f"Erreur : choix non valide. {e}")
            continue