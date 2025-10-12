import json 
import os 
import datetime

from lief import exception

"""
    Gestion de banque simple avec des comptes utilisateurs et des transactions basiques.
"""
# Recuperation du fichier JSON
BANQUE = "banque.json"


# =================================================================
# CLASSE COMPTE BANCAIRE
# =================================================================

class CompteBancaire :
    """ Classe représentant le compte bancaire """

    def __init__(self, titulaire, numero_compte):
        """
            Constructeur de compte bancaire

            Args :
                titulaire : nom du proprietaire du compte
                numero_compte : numéro unique du compte
        """
        self.__titulaire = titulaire
        self.__numero_compte = numero_compte
        self.__solde = 5000.0  # Solde initial du compte
        self.historique = [] # Historique des transactions

    # Convertit l'objet compte bancaire en fichier JSON
    def to_dict(self):
        return {
            "titulaire" : self.__titulaire,
            "numero_compte" : self.__numero_compte,
            "solde" : self.__solde,
        }

    # Affichage standard
    def __str__(self):
        return f"\n Compte de : {self.__titulaire}, \n Numéro de compte : {self.__numero_compte}, \n Solde : {self.__solde} Fcfa."


    # Déposer de l'argent sur le compte 
    def deposer(self, montant, ) :
        """
            Déposer un montant sur le compte

            Args :
                montant : Montant à déposer
        """
        if montant > 0 :
            self.__solde += montant
            self.__enregistrer_transaction("Dépot", montant)
            print(f" ✔ Dépot de {montant} Fcfa effectuée avec succès.")
        else :
            print(" ❗ Le montant du dépot ne doit pas etre négatif.")

    # Rétirer de l'argent du compte 
    def retirer(self, montant) :
        """
            Rétirer un montant sur le compte

            Args :
                Montant  : montant à retirer du compte
        """
        if montant > 0 :
            if montant <= self.__solde :
                self.__solde -= montant
                self.__enregistrer_transaction("Retrait", montant)
                print(f" ✔ Retrait de {montant} Fcfa effectuée avec succès.")
            else :
                print(" ❗ Fonds insuffisants pour effetuer un retrait")
        else :
            print(" ❗ Le montant doit etre positif.")

    # Afficher le solde du compte 
    def afficher_soldes(self) :
        print(f"Le solde du compte No : {self.__numero_compte}, de Mme/M. {self.__titulaire}  est =  {self.__solde} Fcfa.")

    # Avoir juste le solde
    def get_solde(self):

        return self.__solde

    # Recuperer le numero de compte 
    def get_numero_compte(self) :
        return self.__numero_compte

    # Avoir les informations du compte 
    def get_infos(self) :
        """
            Avoir les informations sur un compte
        """
        print(" ======= INFORMATIONS DU COMPTE =========")
        print(f"Titulaire : {self.__titulaire}")
        print(f"Numero du compte : {self.__numero_compte}")
        print(f"Solde du compte : {self.__solde}")

    # Enregistrer une transaction dans l'historique
    def __enregistrer_transaction(self, type_transaction, montant) :
        """
            Enregistrer une transaction du compte

            Args :
                Type_transaction : Renseigne sur le type de transaction ( Dépot / Rétrait )
                Montant          : Montant de la transaction
        """
        transaction =  {
            "type" : type_transaction,
            "montant" : montant,
            "date" : datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "solde_apres_transaction" : self.__solde
        }

        # Ajouter la transaction à l'historique
        self.historique.append(transaction)

    # Afficher l'historique des transactions
    def afficher_historique(self) :
        """ Avoir tout l'histotique des differentes transactions """

        print(" ======= HISTORIQUE DES TRANSACTIONS =========")

        # Vérifier si l'historique est vide
        if not self.historique :
            print(" ❌ Aucune transaction n'a été effectée.")

        # Afficher les transactions
        else :
            print("\n" + "=" * 40)
            print(f"\n Historique des transactions pour le compte No : {self.__numero_compte} ")
            print("=" * 40)
            for transaction in self.historique :
                print(f"\n Date : {transaction['date']}, \n Type : {transaction['type']}, \n Montant: {transaction['montant']} Fcfa, \n Solde apres transaction : {transaction['solde_apres_transaction']} Fcafa.")
                

# =================================================================
# CLASSE BANQUE 
# =================================================================

class Banque :
    """ Classe qui représente la banque Banque """

    def __init__(self, nom_banque):
        """
            Constructeur de la Banque

            Args :
                nom_banque : représente le nom de la banque
        """
        self.nom_banque = nom_banque
        self.__comptes = []
        self.charger_compte()

    # Charger tous les compte depuis le fichier JSON
    def charger_compte(self):
        """ Charger les comptes du fichier JSON """
        try :
            if os.path.exists(BANQUE) :
                with open(BANQUE, 'r', encoding='utf-8' ) as compte:
                    data = json.load(compte)
                    for numero_compte, infos in data.items() :
                        compte = CompteBancaire(
                            numero_compte,
                            infos['titulaire'],
                            infos['numero_compte'],
                            int(infos['solde'])
                        )
                        self.__comptes.append(compte)
                print(f" le nombre de compte est : {len(self.__comptes)} chargé depuis {BANQUE}")
            else :
                print("Aucun compte trouvé")
        except (json.JSONDecodeError, FileNotFoundError) as e :
            print(f"Erreur de chargement {e}")

    # Sauvegarder les cpmtes dans le fichier JSON
    def sauvegarder_comptes(self):
        try :
            data = {}
            for compte in self.__comptes :
                data[compte.get_numero_compte] = compte.to_dict()

            with open(BANQUE, 'w', encoding='utf-8') as fichier :
                json.dump(data, fichier, indent=4, ensure_ascii=False)
            print(f"{len(self.__comptes)} a bien ete sauvegarder dans {BANQUE}")
            return True
        except Exception as e :
            print(f"Erreur de sauvegarde {e}")
            return False

    # Ouvrir un compte
    def ouvrir_compte(self, compte : CompteBancaire):
        """ ouvrir un compte
                Args:
                    compte (CompteBancaire): ouvrir un compte dans la banque
        """
        self.__comptes.append(compte)
        self.sauvegarder_comptes()
        print(f"Le commpte No : {compte.get_numero_compte()} de Mme/M. {compte.titulaire} a ete ouvert avec succes.")

    # Ouvrir un compte de façon interactif
    def ouvrir_compte_interactif(self, titulaire, numero_compte) :
        """
            Ouvrir un compte bancaire de façon interactif

            Args :
                titulaire : nom du proprietaire du compte
                numero_compte : numéro unique du compte
        """
        while True :
            try :
                # Recuperer le numero de compte
                numero_compte = input("Entrez le numero de compte que vous souhaitez creer ou ( 0 ) pour quitter : ").strip()
                if numero_compte.lower() == '0' :
                    break

                # Verifie si l'utilisateur n'entre rien
                if not numero_compte :
                    print("Erreur : le numero de compte ne peut pas etre vide.")
                    continue

                # Recuperer le nom du titulaire du compte
                titulaire = input("Entrez le nom du titulaire du compte : ").strip()

                # verifie si l'utilisateur n'a rien entrer
                if not titulaire :
                    print("Il faut absolument le nom du titulaire du compte.")
                    continue

                # Recuperer le solde
                solde = int(input("Entrez le solde du compte : ").strip())

                # Verifie si l'utilisateur n'a rien entrer
                if not solde :
                    print("Il faut au moins 100f pour ouvrir votre compte ")
                    continue

                # Creer une instance de compte bancaire
                compte = CompteBancaire(numero_compte, titulaire, solde)

                # ajouter le compte a la banque
                self.ouvrir_compte(compte)

                # Conitinuer ou sortir
                continuer = input("Entrez le continuer ? (y/n) : ").strip()
                if continuer.lower() != 'y' :
                    break


                # Vérification si le comte existe deja ou pas avant de creer
                #for compte in self.__comptes :
                #    if compte.get_numero_compte() == numero_compte :
                #        print(f" ❌ Erreur : le compte No {numero_compte} existe deja.")
                #        return

                # Creation de compte
                #nouveau_compte = CompteBancaire(titulaire, numero_compte)
                #self.__comptes.append(nouveau_compte)
                #print(f" ✔ Le compte No : {numero_compte} a été crée avec succès.")
                #return
            except exception as e :
                print(f"Erreur : {e}")


    # Afficher tous les comptes
    def lister_tous_les_comptes(self):
        """ Afficher tous les comptes """

        # Verifie si le compte existe ou pas
        if not self.__comptes :
            print(f" ❌ Aucun compte disponible dans la banque : {self.nom_banque}")
            return

        # Affiche le lite des compte
        print(f"Liste des comptes - {self.nom_banque}")
        print("=" * 50)

        # Recupere les informations des comptes
        for compte in self.__comptes :
            compte.get_infos()
            print("-" * 50)


    # Chercher uun compte 
    def chercher_compte(self, numero_compte) :
        """
            Cherher un compte particulier

            Args :
                numero_compte : numéro unique du compte à cherhcer
        """

        for compte in self.__comptes :
            if compte.get_numero_compte() == numero_compte :
                return compte 
        return None


    #Effectuer un depot
    def effectuer_depot(self, numero_compte, montant) :
        """
            Effectuer un depot sur un compte

            Args :
                Montant : Montant à déposer sur le compte
                numero_compte : numéro unique du compte
        """

        # Recuperer le compte a travers son numero
        compte = self.chercher_compte(numero_compte)

        # Si le compte n'existe pas
        if not compte :
            print(f" ❌ Erreur : le compte No {numero_compte} n'existe pas ")
            return 

        # Si le compte existe, faire le depot
        compte.deposer(montant)


    #Effectuer un retrait
    def effectuer_retrait(self, numero_compte, montant) :
        """
            Effectuer un retrait sur un compte

            Args :
                montant : Montant à retirer sur le compte
                numero_compte : numéro unique du compte
                """
        # recuperer le compte par son numero
        compte = self.chercher_compte(numero_compte)

        # si le compte n'existe pas
        if compte == None :
            print(f"Le compte No {numero_compte} n'existe pas.")
            return 

        # Si le compte existe, faire le retrait
        compte.retirer(montant)
        
    # Afficher les information d'un compte
    def afficher_infos_compte(self, numero_compte) :
        """
            Afficher les information d'un compte

            Args :
                numero_compte : numéro unique du compte
        """

        # Recuper le compte par son numero
        compte = self.chercher_compte(numero_compte)

        # Si le compte n'existe pas
        if compte == None :
            print(f" ❌ Le compte au numero {numero_compte} n'existe pas.")
            return

        # si le compte existe recuper les informations
        compte.get_infos()


    # Calcul total actif de la banque
    def calcul_total_actif(self):

        total = 0
        for compte in self.__comptes :
            total += compte.get_solde()
        return total


    # Obtenir les statistique de la banque
    def obtenir_statistique(self):
        print(f"Statistique de la banque : {self.nom_banque}")
        print("=" * 50)
        print(f"Le Nombre de compte dans la banque : {len(self.__comptes)}")
        print(f"Total des actifs : {self.calcul_total_actif()}")
        print("=" * 50)

    # Trasnferer d'un compte a un autre
    def transferer(self, numero_compte_source, numero_compte_destinataire, montant):
        """
           Faire le transfert d'un compte vers un autre

            Args :
                Montant : Montant à déposer sur le compte
                numero_compte_source : numéro unique du compte qui doit faire le transfert
                numero_compte_destinataire : numero unique du compte qui doit recevoir
        """

        compte_source = self.chercher_compte(numero_compte_source)
        compte_destinataire = self.chercher_compte(numero_compte_destinataire)

        # si le compte source n'existe pas
        if compte_source is None :
            print(f" ❌ Le compte No {numero_compte_source} n'existe pas.")
            return

        # Si le code source du destinataire n'existe pas
        if compte_destinataire is None :
            print(f" ❌ Le compte No {numero_compte_destinataire} n'existe pas.")
            return

        # Si le compte source est pareil que le compte du destinataire
        if numero_compte_source == numero_compte_destinataire :
            print(" ❌ Erreur : Impossible de faire le transfert au meme numero")
            return

        # Sauverader solde avant retrait
        solde_avant = compte_source.get_solde()

        # tenter le retrait sur le compte source
        compte_source.retirer(montant)

        # Verifie si le retrait a resussi ( si le solde a changer )
        if compte_source.get_solde() < solde_avant :
            # Le retrait a reussi, effectuer le depot
            compte_destinataire.deposer(montant)
            print(f" Transfert de {montant }Fcfa effectué de {numero_compte_source} vers {numero_compte_destinataire}")


    # Afficher l'historique des transactions
    def afficher_historique(self, numero_compte) :
        """
            Afficher l'historique de toutes les transactions

            Args :
                numero_compte : Numero unique du compte dont on veut avoir l'historique
        """

        # recuperer le compte par son numero unique
        compte = self.chercher_compte(numero_compte)

        # si le compte n'existe pas
        if compte == None :
            print(f"Le compte No {numero_compte} n'existe pas.")
            return

        # si le compte existe alors afficher l'historique
        compte.afficher_historique()

# =================================================================
# MAIN
# =================================================================

if __name__ == "__main__":
    """
        la partie execution
    """

    # Creer une banque 
    ma_banque = Banque("Banque Nationale")
    print(ma_banque)
    
    # Creation de que quelques comptes 
    print("Ouverture de compte")
    ma_banque.ouvrir_compte("Aziz", "A01")
    ma_banque.ouvrir_compte("Baba", "A02")
    print()
        
        
    while True :
        
        print()
        print(" =======   GESTION DE COMPTE BANCAIRE =========")
        print()
        
        print(" 1. 👉 Afficher tous les comptes ")
        print(" 2. ✔ Ouvrir un compte")
        print(" 3. 👍 Faire un dépot ")
        print(" 4. Faire un retrait ")
        print(" 5. Voir les informations d'un compte ")
        print(" 6. voir l'historique des transactions")
        print(" 7. Afficher statistique de la banque ")
        print(" 8. Faire les transfers ")
        print(" 0  Quitter le programmme ")
        
        print()
        # choix des differentes options du menu
        choice = input("Quel est votre besoin ? ")
        print()


        # Affiche tous les compte
        if choice == '1' :
            #ma_banque.lister_tous_les_comptes()
            ma_banque.charger_compte()

        # Ouvrir un compte bancaire
        elif choice == '2' :
            titulaire = input("Entrez le nom du titulaire :").strip()
            numero_compte = input("Entrez le numero du compte :").strip()
            ma_banque.ouvrir_compte(titulaire, numero_compte)

        # Faire un depot
        elif choice == '3' :
            numero_compte = input("Entrez le numero du compte que vous voulez utiliser : ").strip()
            montant = int(input("Quel est le montant que vous souhaitez déposer : ").strip())
            ma_banque.effectuer_depot(numero_compte, montant)

        # Faire un retrait
        elif choice == '4' :
            numero_compte = input("Entrez le numero du compte que vous voulez utiliser : ").strip()
            montant = int(input("Entrez le montant a retirer : ").strip())
            ma_banque.effectuer_retrait(numero_compte, montant)

        # Afficher les information d'un compte
        elif choice == '5' :
            numero_compte = input("Quel compte voulez vous voir ? ").strip()
            ma_banque.afficher_infos_compte(numero_compte)

        # Affiher l'historique des transactions d'un compte
        elif choice == '6' :
            numero_compte = input("Entrez le numeor de compte : ")
            ma_banque.afficher_historique(numero_compte)

        # Voir les statistiques de la banque
        elif choice == '7' :
            ma_banque.obtenir_statistique()

        # Faire un transfert
        elif choice == '8' :
            numero_compte_source = input("Entrez le numero du compte source :").strip()
            numero_compte_destinataire = input("Entrez le numero du compte du destintaire :").strip()
            montant = int(input("Entrez le montant a transferer : ").strip())
            ma_banque.transferer(numero_compte_source, numero_compte_destinataire, montant)

        # Quitter le programme
        elif choice == '0' :
            print("Vous avez quiteer le programme.")
            break

    