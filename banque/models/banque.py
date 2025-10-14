from models.compte_bancaire import CompteBancaire
from utils.file_manager import FileManager
from utils.validators import Validators
from config.constants import FICHIER_BANQUE, SOLDE_MINIMUM


class Banque:
    """ Classe représentant la banque """

    def __init__(self, nom_banque):
        self.nom_banque = nom_banque
        self.__comptes = []
        self.__charger_comptes()

    def __charger_comptes(self):
        """ Charge les comptes depuis le fichier """
        self.__comptes = FileManager.charger_comptes(FICHIER_BANQUE)

    def __sauvegarder(self):
        """ Sauvegarde les comptes dans le fichier """
        return FileManager.sauvegarder_comptes(FICHIER_BANQUE, self.__comptes)

    def ouvrir_compte(self, titulaire, numero_compte, solde):
        """ Ouvre un nouveau compte """
        # Vérifications
        if not Validators.valider_numero_compte(numero_compte):
            return False, "Numéro de compte invalide"

        if not Validators.valider_titulaire(titulaire):
            return False, "Nom du titulaire invalide"

        if not Validators.valider_solde(solde):
            return False, f"Solde minimum : {SOLDE_MINIMUM} Fcfa"

        # Vérifier si le compte existe déjà
        if self.chercher_compte(numero_compte):
            return False, f"Le compte No {numero_compte} existe déjà"

        # Créer le compte
        nouveau_compte = CompteBancaire(titulaire, numero_compte, solde)
        self.__comptes.append(nouveau_compte)
        self.__sauvegarder()
        return True, f"Compte No {numero_compte} créé avec succès"

    def chercher_compte(self, numero_compte):
        """ Recherche un compte par son numéro """
        for compte in self.__comptes:
            if compte.get_numero_compte() == numero_compte:
                return compte
        return None

    def modifier_compte(self, numero_compte, nouveau_titulaire):
        """ Modifier les comptes dans le fichier """

        if not Validators.valider_titulaire(nouveau_titulaire):
            return False, "Nom du titulaire invalide"

        # Recherche du compte
        compte = self.chercher_compte(numero_compte)

        # si le compte existe
        if compte:
            compte.set_titulaire(nouveau_titulaire)
            self.__sauvegarder()
            return True, f"Le compte No {numero_compte} a été modifié avec succès."

        # Si le compte n'existe pas
        else :
            return False, f"Le compte No {numero_compte} n'existe pas."


    def supprimer_compte(self, numero_compte):
        """ Supprimer un compte dans le fichier """

        # Chercher le compte
        compte = self.chercher_compte(numero_compte)

        if compte:
            self.__comptes.remove(compte)
            self.__sauvegarder()
            return True, f"Le compte No {numero_compte} a été supprimé avec succès."
        else:
            return False, f"Le compte No {numero_compte} n'existe pas."


    def effectuer_depot(self, numero_compte, montant):
        """ Effectue un dépôt sur un compte """

        compte = self.chercher_compte(numero_compte)
        if not compte:
            return False, f"Compte No {numero_compte} introuvable"

        if not Validators.valider_montant(montant):
            return False, "Montant invalide"

        if compte.deposer(montant):
            self.__sauvegarder()
            return True, f"Dépôt de {montant} Fcfa effectué"
        return False, "Échec du dépôt"


    def effectuer_retrait(self, numero_compte, montant):
        """ Effectue un retrait sur un compte """

        compte = self.chercher_compte(numero_compte)
        if not compte:
            return False, f"Compte No {numero_compte} introuvable"

        if not Validators.valider_montant(montant):
            return False, "Montant invalide"

        if compte.retirer(montant):
            self.__sauvegarder()
            return True, f"Retrait de {montant} Fcfa effectué"
        return False, "Fonds insuffisants"

    def transferer(self, numero_source, numero_dest, montant):
        """ Transfère de l'argent entre deux comptes """

        compte_source = self.chercher_compte(numero_source)
        compte_dest = self.chercher_compte(numero_dest)

        if not compte_source:
            return False, f"Compte source {numero_source} introuvable"

        if not compte_dest:
            return False, f"Compte destinataire {numero_dest} introuvable"

        if numero_source == numero_dest:
            return False, "Impossible de transférer vers le même compte"

        solde_avant = compte_source.get_solde()
        if compte_source.retirer(montant):
            if compte_source.get_solde() < solde_avant:
                compte_dest.deposer(montant)
                self.__sauvegarder()
                return True, f"Transfert de {montant} Fcfa effectué"

        return False, "Échec du transfert"

    def lister_comptes(self):
        """ Liste tous les comptes """

        if not self.__comptes:
            print(f"❌ Aucun compte dans {self.nom_banque}")
            return

        print(f"\\n{'='*50}")
        print(f"COMPTES - {self.nom_banque}")
        print('='*50)
        for compte in self.__comptes:
            compte.get_infos()

    def obtenir_statistiques(self):
        """ Affiche les statistiques de la banque """

        total_actifs = sum(c.get_solde() for c in self.__comptes)
        print(f"\\n{'='*50}")
        print(f"STATISTIQUES - {self.nom_banque}")
        print('='*50)
        print(f"Nombre de comptes : {len(self.__comptes)}")
        print(f"Total des actifs : {total_actifs} Fcfa")
        print('='*50)

    def afficher_historique(self, numero_compte):
        """ Affiche l'historique d'un compte """

        compte = self.chercher_compte(numero_compte)
        if not compte:
            print(f"❌ Compte No {numero_compte} introuvable")
            return
        compte.afficher_historique()