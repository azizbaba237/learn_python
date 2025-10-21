# ============================================================================
# ui/interface.py
# ============================================================================
UI_INTERFACE = """
Interface utilisateur en ligne de commande
"""
from typing import List
from models.etudiant import Etudiant
from services.classe_service import ClasseService
from ui.menu import Menu
from config.settings import NOTE_MIN, NOTE_MAX
from utils.formatters import afficher_titre, afficher_message
from utils.validators import valider_note


class InterfaceGestion:
    """Gère l'interface CLI"""

    def __init__(self, classe_service: ClasseService):
        self.classe = classe_service
        self.menu = Menu()

    def saisir_notes(self) -> List[float]:
        """Gère la saisie des notes"""
        notes = []
        print("\\n--- Saisie des notes ---")
        print("Entrez les notes (entre 0 et 20), tapez 'f' pour finir")

        while True:
            try:
                saisie = input("Note : ").strip().lower()
                if saisie == 'f':
                    break

                est_valide, message = valider_note(saisie, NOTE_MIN, NOTE_MAX)
                if not est_valide:
                    afficher_message("❌", message)
                    continue

                note = float(saisie)
                notes.append(note)
                afficher_message("✅", f"Note {note} ajoutée")

            except ValueError:
                afficher_message("❌", "Veuillez entrer un nombre valide")

        return notes

    def ajouter_etudiant_interactif(self) -> None:
        """Gère l'ajout d'un étudiant"""
        afficher_titre("AJOUTER UN NOUVEL ÉTUDIANT", 50)

        try:
            nom = input("Nom : ").strip()
            if not nom:
                afficher_message("❌", "Le nom est obligatoire")
                return

            prenom = input("Prénom : ").strip()
            if not prenom:
                afficher_message("❌", "Le prénom est obligatoire")
                return

            matricule = input("Matricule : ").strip()
            if not matricule:
                afficher_message("❌", "Le matricule est obligatoire")
                return

            if self.classe.matricule_existe(matricule):
                afficher_message("❌", f"Le matricule {matricule.upper()} existe déjà")
                return

            etudiant = Etudiant(nom, prenom, matricule)
            notes = self.saisir_notes()

            for note in notes:
                etudiant.ajouter_note(note)

            if self.classe.ajouter_etudiant(etudiant):
                afficher_message("✅", f"Étudiant {etudiant} ajouté avec succès !")
                if not notes:
                    afficher_message("⚠️", "Aucune note n'a été saisie")
            else:
                afficher_message("❌", "Erreur lors de l'ajout")

        except Exception as e:
            afficher_message("❌", f"Erreur : {e}")

    def modifier_etudiant_interactif(self) -> None:
        """Gère la modification d'un étudiant"""
        afficher_titre("MODIFIER UN ÉTUDIANT", 50)

        matricule = input("Matricule de l'étudiant à modifier : ").strip()
        etudiant = self.classe.chercher_etudiant(matricule)

        if not etudiant:
            afficher_message("❌", f"Aucun étudiant trouvé avec le matricule {matricule}")
            return

        print("\\n--- Informations actuelles ---")
        self.menu.afficher_info_etudiant(etudiant)

        nouveau_nom = input(f"\\nNouveau nom [{etudiant.nom}] (Entrée pour conserver) : ").strip()
        if nouveau_nom:
            etudiant.nom = nouveau_nom.capitalize()

        nouveau_prenom = input(f"Nouveau prénom [{etudiant.prenom}] (Entrée pour conserver) : ").strip()
        if nouveau_prenom:
            etudiant.prenom = nouveau_prenom.capitalize()

        choix = input("\\nModifier les notes ? (o/n) : ").strip().lower()
        if choix in ['o', 'oui']:
            etudiant.vider_notes()
            notes = self.saisir_notes()
            for note in notes:
                etudiant.ajouter_note(note)

        self.classe.sauvegarder_etudiants()
        afficher_message("✅", f"Étudiant {etudiant} modifié avec succès !")
        self.menu.afficher_info_etudiant(etudiant)

    def supprimer_etudiant_interactif(self) -> None:
        """Gère la suppression d'un étudiant"""
        afficher_titre("SUPPRIMER UN ÉTUDIANT", 50)

        matricule = input("Matricule de l'étudiant à supprimer : ").strip()
        etudiant = self.classe.chercher_etudiant(matricule)

        if not etudiant:
            afficher_message("❌", f"Aucun étudiant trouvé avec le matricule {matricule}")
            return

        print(f"\\n⚠️  Vous allez supprimer : {etudiant}")
        confirmation = input("Confirmer la suppression ? (o/n) : ").strip().lower()

        if confirmation in ['o', 'oui']:
            if self.classe.supprimer_etudiant(matricule):
                afficher_message("✅", f"Étudiant {etudiant} supprimé avec succès")
            else:
                afficher_message("❌", "Erreur lors de la suppression")
        else:
            afficher_message("❌", "Suppression annulée")

    def executer(self) -> None:
        """Boucle principale de l'interface"""
        while True:
            self.menu.afficher_menu_principal()
            choix = input("\\nVotre choix : ").strip().lower()

            if choix == '1':
                self.ajouter_etudiant_interactif()
            elif choix == '2':
                self.modifier_etudiant_interactif()
            elif choix == '3':
                self.supprimer_etudiant_interactif()
            elif choix == '4':
                matricule = input("Matricule : ").strip()
                etudiant = self.classe.chercher_etudiant(matricule)
                if etudiant:
                    self.menu.afficher_info_etudiant(etudiant)
                else:
                    afficher_message("❌", f"Aucun étudiant trouvé avec le matricule {matricule}")
            elif choix == '5':
                etudiants = self.classe.obtenir_etudiants_tries()
                self.menu.afficher_liste_etudiants(etudiants, self.classe.nom_classe)
            elif choix == '6':
                stats = self.classe.obtenir_statistiques()
                self.menu.afficher_statistiques(stats, self.classe.nom_classe)
            elif choix == '7':
                if self.classe.sauvegarder_etudiants():
                    afficher_message("✅", "Données sauvegardées")
            elif choix == 'q':
                self.classe.sauvegarder_etudiants()
                print("\\n👋 Au revoir !")
                break
            else:
                afficher_message("❌", "Choix invalide")
