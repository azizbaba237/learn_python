# ============================================================================
# ui/menu.py
# ============================================================================
UI_MENU = """
Gestion des menus et affichages
"""
from utils.formatters import afficher_titre, afficher_separateur, formater_moyenne, formater_pourcentage


class Menu:
    """Gère l'affichage des menus"""

    @staticmethod
    def afficher_menu_principal() -> None:
        """Affiche le menu principal"""
        afficher_titre("SYSTÈME DE GESTION DES ÉTUDIANTS")
        print("1. Ajouter un étudiant")
        print("2. Modifier un étudiant")
        print("3. Supprimer un étudiant")
        print("4. Afficher un étudiant")
        print("5. Afficher tous les étudiants")
        print("6. Afficher les statistiques")
        print("7. Sauvegarder manuellement")
        print("q. Quitter")
        afficher_separateur()

    @staticmethod
    def afficher_info_etudiant(etudiant) -> None:
        """Affiche les informations d'un étudiant"""
        info = etudiant.get_info()
        afficher_titre("INFORMATIONS DE L'ÉTUDIANT", 50)
        print(f"Matricule    : {info['matricule']}")
        print(f"Nom          : {info['nom']}")
        print(f"Prénom       : {info['prenom']}")
        print(f"Notes        : {info['notes']}")
        print(f"Moyenne      : {formater_moyenne(info['moyenne'])}")
        print(f"Décision     : {info['decision']}")
        afficher_separateur(50)

    @staticmethod
    def afficher_liste_etudiants(etudiants, nom_classe: str) -> None:
        """Affiche la liste des étudiants"""
        if not etudiants:
            print("\\n⚠️  La liste des étudiants est vide.")
            return

        afficher_titre(f"LISTE DES ÉTUDIANTS - {nom_classe}", 80)

        for i, etudiant in enumerate(etudiants, 1):
            info = etudiant.get_info()
            print(f"\\n{i}. {etudiant}")
            print(f"   Matricule : {info['matricule']}")
            print(f"   Notes     : {info['notes']}")
            print(f"   Moyenne   : {formater_moyenne(info['moyenne'])}")
            print(f"   Statut    : {info['decision']}")

        afficher_separateur(80)

    @staticmethod
    def afficher_statistiques(stats: dict, nom_classe: str) -> None:
        """Affiche les statistiques de la classe"""
        afficher_titre(f"STATISTIQUES - {nom_classe}")
        print(f"Nombre d'étudiants    : {stats['nombre_etudiants']}")
        print(f"Moyenne de la classe  : {formater_moyenne(stats['moyenne_classe'])}")
        print(f"Taux de réussite      : {formater_pourcentage(stats['taux_reussite'])}")
        print(f"Nombre d'admis        : {stats['nombre_admis']}")
        print(f"Nombre de refusés     : {stats['nombre_refuses']}")

        if stats['meilleur_etudiant']:
            print(f"Meilleur étudiant     : {stats['meilleur_etudiant']}")
            print(f"Meilleure moyenne     : {formater_moyenne(stats['meilleur_moyenne'])}")

        afficher_separateur()
