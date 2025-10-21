# ============================================================================
# services/classe_service.py
# ============================================================================
CLASSE_SERVICE = """
Service de gestion de la classe (logique métier)
"""
from typing import List, Optional
from models.etudiant import Etudiant
from services.data_service import DataService


class ClasseService:
    """Gère une collection d'étudiants et leurs statistiques"""

    def __init__(self, nom_classe: str = "Classe par défaut"):
        """
        Initialise le service de classe.

        Args:
            nom_classe: Nom de la classe
        """
        self._etudiants: List[Etudiant] = []
        self.nom_classe = nom_classe
        self._data_service = DataService()

    @property
    def etudiants(self) -> List[Etudiant]:
        """Retourne une copie de la liste des étudiants"""
        return self._etudiants.copy()

    @property
    def nombre_etudiants(self) -> int:
        """Retourne le nombre d'étudiants"""
        return len(self._etudiants)

    def charger_etudiants(self) -> int:
        """
        Charge les étudiants depuis le fichier.

        Returns:
            int: Nombre d'étudiants chargés
        """
        self._etudiants = self._data_service.charger_etudiants()
        return len(self._etudiants)

    def sauvegarder_etudiants(self) -> bool:
        """
        Sauvegarde les étudiants.

        Returns:
            bool: True si succès
        """
        return self._data_service.sauvegarder_etudiants(self._etudiants)

    def matricule_existe(self, matricule: str) -> bool:
        """Vérifie si un matricule existe"""
        matricule_normalise = matricule.strip().upper()
        return any(e.matricule == matricule_normalise for e in self._etudiants)

    def chercher_etudiant(self, matricule: str) -> Optional[Etudiant]:
        """Recherche un étudiant par matricule"""
        matricule_normalise = matricule.strip().upper()
        return next(
            (e for e in self._etudiants if e.matricule == matricule_normalise),
            None
        )

    def ajouter_etudiant(self, etudiant: Etudiant) -> bool:
        """
        Ajoute un étudiant.

        Args:
            etudiant: L'étudiant à ajouter

        Returns:
            bool: True si ajouté
        """
        if not isinstance(etudiant, Etudiant):
            raise TypeError("L'objet doit être de type Etudiant")

        if self.matricule_existe(etudiant.matricule):
            return False

        self._etudiants.append(etudiant)
        self.sauvegarder_etudiants()
        return True

    def supprimer_etudiant(self, matricule: str) -> bool:
        """Supprime un étudiant"""
        etudiant = self.chercher_etudiant(matricule)
        if etudiant:
            self._etudiants.remove(etudiant)
            self.sauvegarder_etudiants()
            return True
        return False

    def calculer_moyenne_classe(self) -> float:
        """Calcule la moyenne de la classe"""
        if not self._etudiants:
            return 0.0
        total = sum(e.calculer_moyenne() for e in self._etudiants)
        return total / len(self._etudiants)

    def obtenir_meilleur_etudiant(self) -> Optional[Etudiant]:
        """Trouve le meilleur étudiant"""
        if not self._etudiants:
            return None
        return max(self._etudiants, key=lambda e: e.calculer_moyenne())

    def calculer_taux_reussite(self) -> float:
        """Calcule le taux de réussite"""
        if not self._etudiants:
            return 0.0
        admis = sum(1 for e in self._etudiants if e.est_admis())
        return (admis / len(self._etudiants)) * 100

    def obtenir_statistiques(self) -> dict:
        """Calcule toutes les statistiques"""
        if not self._etudiants:
            return {
                'nombre_etudiants': 0,
                'moyenne_classe': 0.0,
                'taux_reussite': 0.0,
                'meilleur_etudiant': None,
                'nombre_admis': 0,
                'nombre_refuses': 0
            }

        meilleur = self.obtenir_meilleur_etudiant()
        admis = sum(1 for e in self._etudiants if e.est_admis())

        return {
            'nombre_etudiants': len(self._etudiants),
            'moyenne_classe': self.calculer_moyenne_classe(),
            'taux_reussite': self.calculer_taux_reussite(),
            'meilleur_etudiant': str(meilleur) if meilleur else None,
            'meilleur_moyenne': meilleur.calculer_moyenne() if meilleur else 0,
            'nombre_admis': admis,
            'nombre_refuses': len(self._etudiants) - admis
        }

    def obtenir_etudiants_tries(self) -> List[Etudiant]:
        """Retourne les étudiants triés par nom/prénom"""
        return sorted(self._etudiants, key=lambda e: (e.nom, e.prenom))