# ============================================================================
# utils/formatters.py
# ============================================================================
FORMATTERS = """
Fonctions de formatage pour l'affichage
"""


def afficher_separateur(largeur: int = 60, caractere: str = "=") -> None:
    """Affiche une ligne de séparation"""
    print(caractere * largeur)


def afficher_titre(titre: str, largeur: int = 60) -> None:
    """Affiche un titre centré avec séparateurs"""
    print("\\n" + "=" * largeur)
    print(titre.center(largeur))
    print("=" * largeur)


def formater_moyenne(moyenne: float) -> str:
    """Formate une moyenne avec 2 décimales"""
    return f"{moyenne:.2f}/20"


def formater_pourcentage(valeur: float) -> str:
    """Formate un pourcentage avec 2 décimales"""
    return f"{valeur:.2f}%"


def afficher_message(icone: str, message: str) -> None:
    """Affiche un message avec une icône"""
    print(f"{icone} {message}")
