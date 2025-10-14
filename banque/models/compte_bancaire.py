import datetime
from config.constants import FORMAT_DATE


class CompteBancaire:
    """ Classe représentant un compte bancaire"""

    def __init__(self, titulaire, numero_compte, solde):
        self.__titulaire = titulaire
        self.__numero_compte = numero_compte
        self.__solde = solde
        self.historique = []

    def to_dict(self):
        """ Convertit le compte en dictionnaire pour JSON"""
        return {
            "titulaire": self.__titulaire,
            "numero_compte": self.__numero_compte,
            "solde": self.__solde,
        }

    def __str__(self):
        return f"Compte de : {self.__titulaire}, Numéro : {self.__numero_compte}, Solde : {self.__solde} Fcfa"

    def deposer(self, montant):
        """ Dépose un montant sur le compte"""
        if montant > 0:
            self.__solde += montant
            self.__enregistrer_transaction("Dépôt", montant)
            return True
        return False

    def retirer(self, montant):
        """ Retire un montant du compte"""
        if montant > 0 and montant <= self.__solde:
            self.__solde -= montant
            self.__enregistrer_transaction("Retrait", montant)
            return True
        return False

    def __enregistrer_transaction(self, type_transaction, montant):
        """ Enregistre une transaction dans l'historique"""
        transaction = {
            "type": type_transaction,
            "montant": montant,
            "date": datetime.datetime.now().strftime(FORMAT_DATE),
            "solde_apres_transaction": self.__solde
        }
        self.historique.append(transaction)

    def afficher_historique(self):
        """ Affiche l'historique des transactions"""
        if not self.historique:
            print(" ❌ Aucune transaction effectuée.")
            return

        print("\\n" + "=" * 50)
        print(f"Historique - Compte No : {self.__numero_compte}")
        print("=" * 50)
        for transaction in self.historique:
            print(f"Date : {transaction['date']}")
            print(f"Type : {transaction['type']}")
            print(f"Montant : {transaction['montant']} Fcfa")
            print(f"Solde après : {transaction['solde_apres_transaction']} Fcfa")
            print("-" * 50)

    # Getters
    def get_solde(self):
        return self.__solde

    def get_numero_compte(self):
        return self.__numero_compte

    def get_titulaire(self):
        return self.__titulaire

    def get_infos(self):
        """ Affiche les informations du compte """
        print("=" * 50)
        print(f"Titulaire : {self.__titulaire}")
        print(f"Numéro : {self.__numero_compte}")
        print(f"Solde : {self.__solde} Fcfa")
        print("=" * 50)

    # Setters
    def set_titulaire(self, nouveau_titulaire):
        """ Modifie le nom du titulaire"""
        self.__titulaire = nouveau_titulaire