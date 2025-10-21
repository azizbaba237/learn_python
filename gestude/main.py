# ============================================================================
# main.py
# ============================================================================
MAIN = """
Point d'entrée principal de l'application
"""
from models.etudiant import Etudiant
from services.classe_service import ClasseService
from ui.interface import InterfaceGestion


def creer_donnees_test(classe_service: ClasseService) -> None:
    """Crée des données de test si la classe est vide"""
    if classe_service.nombre_etudiants > 0:
        return

    print("\\n📝 Création d'étudiants de test...")

    etudiants_test = [
        ("Aziz", "Baba", "A01", [15, 18, 16]),
        ("Karim", "Ali", "A02", [8, 11, 9]),
        ("Sara", "Doe", "A03", [19, 17, 18]),
    ]

    for nom, prenom, matricule, notes in etudiants_test:
        etudiant = Etudiant(nom, prenom, matricule)
        for note in notes:
            etudiant.ajouter_note(note)
        classe_service.ajouter_etudiant(etudiant)

    print(f"✅ {classe_service.nombre_etudiants} étudiants de test créés")


def main():
    """Fonction principale"""
    print("=" * 60)
    print("SYSTÈME DE GESTION D'ÉTUDIANTS".center(60))
    print("=" * 60)

    # Initialisation du service
    classe = ClasseService("Terminale S1")

    # Chargement des données
    nb_charges = classe.charger_etudiants()
    if nb_charges > 0:
        print(f"✅ {nb_charges} étudiant(s) chargé(s) depuis le fichier")
    else:
        print("ℹ️  Démarrage avec une classe vide")

    # Création de données de test si nécessaire
    creer_donnees_test(classe)

    # Lancement de l'interface
    interface = InterfaceGestion(classe)
    interface.executer()


if __name__ == "__main__":
    main()
