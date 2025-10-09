import json 
import os 
import datetime
"""Gestion de banque simple avec des comptes utilisateurs et des transactions basiques.
"""

# Classe representant un compte bancaire 
class CompteBancaire :
    def __init__(self, titulaire, numero_compte):
        self.__titulaire = titulaire
        self.__numero_compte = numero_compte
        self.__solde = 0.0  # Solde initial du compte
        self.historique = [] # Historique des transactions
        
        
    def __str__(self):
        return f"\n Compte de : {self.__titulaire}, \n Numéro de compte : {self.__numero_compte}, \n Solde : {self.__solde} Fcfa."
    
    
    # Déposer de l'argent sur le compte 
    def deposer(self, montant, ) :
        if montant > 0 :
            self.__solde += montant 
            self.__enregistrer_transaction("Depot", montant)
            print(f"Dépot de {montant} Fcfa effectuée avec succès.")
        else :
            print("Le montant du dépot ne doit pas etre négatif.")
            
    # Rétirer de l'argent du compte 
    def retirer(self, montant) :
        if montant > 0 :
            if montant <= self.__solde :
                self.__solde -= montant
                self.__enregistrer_transaction("Retrait", montant) 
                print(f"Retrait de {montant} Fcfa effectuée avec succès.")
            else : 
                print("Fonds insuffisants pour effetuer un retrait")
        else :
            print("Le montant doit etre positif.")
            
    # Afficher le solde du compte 
    def afficher_soldes(self) :
        print(f"\n Le solde du compte No : {self.__numero_compte},  est de {self.__solde} Fcfa.")
        
    # Avoir les informations du compte 
    def get_infos(self) :
        return ({
            "\n titulaire" : self.__titulaire,
            "\n numero_compte": self.__numero_compte,
            "\n solde" : self.__solde
        })
    
    # Enregistrer une transaction dans l'historique
    def __enregistrer_transaction(self, type_transaction, montant) :
        transaction =  {
            "type" : type_transaction,
            "montant" : montant,
            "date" : datetime.datetime.now().isoformat(),
            "solde_apres_transaction" : self.__solde
        }
        
        # Ajouter la transaction à l'historique
        self.historique.append(transaction)
        
    # Afficher l'historique des transactions
    def afficher_historique(self) :
        
        # Vérifier si l'historique est vide
        if not self.historique :
            print("Aucune transaction n'a été effectée.")
            
        # Afficher les transactions
        else :
            print("\n" + "=" * 40)
            print(f"\n Historique des transactions pour le compte No : {self.__numero_compte} ")
            print("=" * 40)
            for transaction in self.historique :
                print(f"\n Date : {transaction['date']}, \n Type : {transaction['type']}, \n Montant: {transaction['montant']} Fcfa, \n Solde apres transaction : {transaction['solde_apres_transaction']} Fcafa.")
                
        

# Test de la classe CompteBancaire    
test = CompteBancaire("Aziz", "F2345678")
print(test)
print("-" * 50)

# Effectuer des opérations de dépôt et de retrait
test_deposer = test.deposer(5000)
print(test)
print("-" * 50)

# Effectuer un retrait
test_retirer = test.retirer(2999.5677)
print(test)

# infos du compte 
test_infos = test.get_infos()
print(test_infos)

test_hostorique = test.afficher_historique()

# Classe banque 
# class Banque :
#     def __init__(self, nom_banque) :
#         self.nom_banque = nom_banque
#         self.comptes = {}
#         self.fichier_donnees = "banque.json"
#         self.charger_donnees()
        
#     def __str__(self):
#         return f"Bansue : {self.nom_banque}, nombre de comptes : {len(self.comptes)}"
    

    