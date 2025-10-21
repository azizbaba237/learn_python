# ============================================================================
# utils/validators.py
# ============================================================================
VALIDATORS = """
Fonctions de validation des données
"""
from typing import Tuple


def valider_note(note: float, min_val: float = 0.0, max_val: float = 20.0) -> Tuple[bool, str]:
    """
    Valide qu'une note est dans la plage autorisée.

    Args:
        note: La note à valider
        min_val: Valeur minimale acceptée
        max_val: Valeur maximale acceptée

    Returns:
        Tuple[bool, str]: (est_valide, message_erreur)
    """
    try:
        note_float = float(note)
        if not (min_val <= note_float <= max_val):
            return False, f"La note doit être entre {min_val} et {max_val}"
        return True, ""
    except (ValueError, TypeError):
        return False, "La note doit être un nombre valide"


def valider_matricule(matricule: str) -> Tuple[bool, str]:
    """
    Valide qu'un matricule n'est pas vide.

    Args:
        matricule: Le matricule à valider

    Returns:
        Tuple[bool, str]: (est_valide, message_erreur)
    """
    if not matricule or not matricule.strip():
        return False, "Le matricule ne peut pas être vide"
    return True, ""


def normaliser_texte(texte: str) -> str:
    """
    Normalise un texte (strip + capitalize).

    Args:
        texte: Le texte à normaliser

    Returns:
        str: Texte normalisé
    """
    return texte.strip().capitalize()


def normaliser_matricule(matricule: str) -> str:
    """
    Normalise un matricule (strip + uppercase).

    Args:
        matricule: Le matricule à normaliser

    Returns:
        str: Matricule normalisé
    """
    return matricule.strip().upper()
