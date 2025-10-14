from config.constants import SOLDE_MINIMUM


class Validators:
    '''Classe pour valider les entrées utilisateur'''

    @staticmethod
    def valider_numero_compte(numero_compte):
        '''Valide qu'un numéro de compte n'est pas vide'''
        return numero_compte and numero_compte.strip() != ""

    @staticmethod
    def valider_titulaire(titulaire):
        '''Valide qu'un nom de titulaire n'est pas vide'''
        return titulaire and titulaire.strip() != ""

    @staticmethod
    def valider_solde(solde):
        '''Valide qu'un solde est suffisant'''
        try:
            solde_float = float(solde)
            return solde_float >= SOLDE_MINIMUM
        except ValueError:
            return False

    @staticmethod
    def valider_montant(montant):
        '''Valide qu'un montant est positif'''
        try:
            montant_float = float(montant)
            return montant_float > 0
        except ValueError:
            return False