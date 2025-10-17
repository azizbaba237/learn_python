"""
    Gestion d'étudiants

        Objectif : Manipuler des listes d'objets
        Concepts : Classes, listes, méthodes de classe
"""
# =================================================================
# CLASSE ETUDIANT
# =================================================================
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
        return moyenne

    def est_admis(self):
        """ Renvoie la decision """
        moyenne = self.calculer_moyenne()
        if moyenne >= 10:
            return True
        else:
            return False

    def get_matricule(self):
        return self.matricule

    def get_info(self):
        """ Getter pour avoir les informations d'un etudiant """

        print("************* INFORMATION DE L'ETUDIANT **********")

        moyenne = self.calculer_moyenne()
        decision = "admis" if self.est_admis() else "refuser"
        matricule =self.get_matricule()

        print(f"Matricule : {matricule}")
        print(f"Nom: {self.nom}")
        print(f"Prénom: {self.prenom}")
        print(f"Note : {self.note}")
        print(f"Moyenne : {moyenne:.2f}")
        print(f"Décision : {decision}")


# =================================================================
# CLASSE CLASSE
# =================================================================
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

    def afficher_tous_les_etudiants(self):
        """ Affiche le nom, le prénom, les notes et le statut d'admission de tous les étudiants de la liste. """

        print("\n--- Liste et statut des étudiants ---")

        if self.liste_etudiant:
            for etudiant in self.liste_etudiant:
                etat_admission = "Admis" if etudiant.est_admis() else "échoué"
                moyenne_individuelle = etudiant.calculer_moyenne()

                print(
                    f"\n Matricule : {etudiant.matricule} \n Nom : {etudiant.nom} \n Prenom : {etudiant.prenom} \n Note : {etudiant.note} \n Moyenne : {moyenne_individuelle:.2f} \n Décision : {etat_admission}")
        else:
            print("La liste des etudiants est vide.")
            return

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

    def chercher_etudiant(self, matricule):
        """ Chercher un etudiant """
        matricule = matricule.strip().lower()

        for etudiant in self.liste_etudiant:
            if etudiant.matricule.lower() == matricule:
                return etudiant
        return None

    def afficher_info_etudiant(self, matricule):
        """ afficher les informations d'un etudiant """

        # chercher etudiant
        etudiant = self.chercher_etudiant(matricule)

        # si l'etudiant n'existe pas dans la liste
        if not etudiant :
            print("L'etudiant n'existe pas dans la liste.")
            return

        # Recuperer les informations l'etudiant
        etudiant.get_info()
    
    def supprimer_etudiant(self, matricule):
        """ Supprimer un etudiant de la liste """

        # Normaliser le matricule
        matricule_saisi_normaliser = matricule.strip().lower()

        # initialisation de l'etudiant a supprimer
        etudiant_a_supprimer = None

        # chercher le matricule a supprimer et l'afficher l'etudiant en question
        for etudiant in self.liste_etudiant:
            if etudiant.matricule.strip().lower() == matricule_saisi_normaliser:
                etudiant_a_supprimer = etudiant
                break

        # Supprimer l'etudiant s'il existe
        if etudiant_a_supprimer :
            self.liste_etudiant.remove(etudiant_a_supprimer)
            print(f"L'etudiant au matricule : {etudiant_a_supprimer.matricule} a ete retiré avec succes.")

        # Si le matricule n'existe pas
        else:
            print(f"Le matricul {matricule} n'existe pas.")




# =================================================================
# MAIN
# =================================================================
if __name__=="__main__" :

    # Creation de l'instance de la classe
    gestionnaire_classe = Classe()  # J'utilise un nom plus explicite ici

    # ----------------------------------------------------
    # Quelques etudiants pré-créés
    # ----------------------------------------------------

    # 1. Création de l'étudiant 'Aziz'
    aziz = Etudiant("aziz", "baba", "A01")
    aziz.ajouter_note(15)  # Utilise la méthode Etudiant.ajouter_note(note)
    aziz.ajouter_note(18)
    gestionnaire_classe.enregistrer_etudiant(aziz)  # Enregistrement dans la liste

    # 2. Création de l'étudiant 'Karim'
    karim = Etudiant("karim", "ali", "A02")
    karim.ajouter_note(8)
    karim.ajouter_note(11)
    gestionnaire_classe.enregistrer_etudiant(karim)

    # 3. Création de l'étudiant 'Sara'
    sara = Etudiant("sara", "doe", "A03")
    sara.ajouter_note(19)
    sara.ajouter_note(10)
    sara.ajouter_note(14)
    gestionnaire_classe.enregistrer_etudiant(sara)

    # ----------------------------------------------------

    while True :
        print()
        print("************** Porgramme de Gestion des Etudiants ******************")
        print()
        print("1. Ajouter un Etudiant")
        print("2. voir la moyenne de la calsse ")
        print("3. voir le meilleur Etudiant")
        print("4. voir le taux de reussite ")
        print("5. afficher tous les etudiants ")
        print("6. afficher les informations d'un etudiant ")
        print("7. supprimer un etudiant")
        print("q. Quitter le programme")
        print()


        try :
            print()
            choix = input("Que souhaitez-vous faire ? ")

            if choix == '1' :
                gestionnaire_classe.ajouter_etudiant()
            elif choix == '2' :
                gestionnaire_classe.moyenne_classe()
            elif choix == '3' :
                gestionnaire_classe.meilleur_etudiant()
            elif choix == '4' :
                gestionnaire_classe.taux_reussite()
            elif choix == '5' :
                gestionnaire_classe.afficher_tous_les_etudiants()
            elif choix == '6' :
                matricule = input("Entrez le matricule: ").strip().lower()
                gestionnaire_classe.afficher_info_etudiant(matricule)
            elif choix == '7':
                matricule = input("Entrez le matricule: ").strip().lower()
                gestionnaire_classe.supprimer_etudiant(matricule)
                gestionnaire_classe.afficher_tous_les_etudiants()
            elif choix == 'q':
                print("Vous avez quitter le programme.")
                break

        except Exception as e :
            print(f"Erreur : choix non valide. {e}")
            continue