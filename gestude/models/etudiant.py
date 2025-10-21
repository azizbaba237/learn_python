# ============================================================================
# models/étudiant.py
# ============================================================================
MODEL_ETUDIANT = """
Modèle de données : Étudiant
"""
from typing import List
from config.settings import SEUIL_ADMISSION, NOTE_MIN, NOTE_MAX
from utils.validators import valider_note, valider_matricule, normaliser_texte, normaliser_matricule


class Etudiant:
    """
    Représente un étudiant avec ses informations personnelles et académiques.

    Attributs:
        nom (str): Nom de famille de l'étudiant
        prenom (str): Prénom de l'étudiant
        matricule (str): Identifiant unique de l'étudiant
        _notes (List[float]): Liste des notes obtenues (privé)
    """

    def __init__(self, nom: str, prenom: str, matricule: str):
        """
        Initialise un nouvel étudiant.

        Args:
            nom: Nom de famille
            prenom: Prénom
            matricule: Identifiant unique

        Raises:
            ValueError: Si le matricule est invalide
        """
        est_valide, message = valider_matricule(matricule)
        if not est_valide:
            raise ValueError(message)

        self.nom = normaliser_texte(nom)
        self.prenom = normaliser_texte(prenom)
        self.matricule = normaliser_matricule(matricule)
        self._notes: List[float] = []

    def __str__(self) -> str:
        """Représentation textuelle lisible"""
        return f"{self.nom} {self.prenom} ({self.matricule})"

    def __repr__(self) -> str:
        """Représentation technique pour le débogage"""
        return f"Etudiant(nom='{self.nom}', prenom='{self.prenom}', matricule='{self.matricule}')"

    @property
    def notes(self) -> List[float]:
        """Retourne une copie de la liste des notes"""
        return self._notes.copy()

    def ajouter_note(self, note: float) -> bool:
        """
        Ajoute une note avec validation.

        Args:
            note: La note à ajouter

        Returns:
            bool: True si ajout réussi

        Raises:
            ValueError: Si la note est invalide
        """
        est_valide, message = valider_note(note, NOTE_MIN, NOTE_MAX)
        if not est_valide:
            raise ValueError(message)

        self._notes.append(float(note))
        return True

    def calculer_moyenne(self) -> float:
        """Calcule la moyenne arithmétique des notes"""
        if not self._notes:
            return 0.0
        return sum(self._notes) / len(self._notes)

    def est_admis(self) -> bool:
        """Détermine si l'étudiant est admis"""
        return self.calculer_moyenne() >= SEUIL_ADMISSION

    def vider_notes(self) -> None:
        """Supprime toutes les notes"""
        self._notes.clear()

    def to_dict(self) -> dict:
        """Convertit l'objet en dictionnaire pour JSON"""
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "notes": self._notes
        }

    @classmethod
    def from_dict(cls, matricule: str, data: dict) -> 'Etudiant':
        """
        Crée un étudiant depuis un dictionnaire.

        Args:
            matricule: Le matricule de l'étudiant
            data: Dictionnaire contenant les données

        Returns:
            Etudiant: Nouvelle instance
        """
        etudiant = cls(data['nom'], data['prenom'], matricule)
        for note in data.get('notes', []):
            etudiant.ajouter_note(note)
        return etudiant

    def get_info(self) -> dict:
        """Retourne toutes les informations de l'étudiant"""
        moyenne = self.calculer_moyenne()
        return {
            'matricule': self.matricule,
            'nom': self.nom,
            'prenom': self.prenom,
            'notes': self.notes,
            'moyenne': moyenne,
            'admis': self.est_admis(),
            'decision': 'Admis' if self.est_admis() else 'Refusé'
        }