"""
Système de Gestion d'Étudiants Optimisé

"""
import json
from typing import List, Optional
import os

CLASSE_DATA = "gestude.json"


# =================================================================
# CLASSE ETUDIANT
# =================================================================
class Etudiant:
    """
    Représente un étudiant avec ses informations personnelles et académiques.
    """

    SEUIL_ADMISSION = 10.0
    NOTE_MIN = 0.0
    NOTE_MAX = 20.0

    def __init__(self, nom: str, prenom: str, matricule: str):
        """
        Initialise un nouvel étudiant.

        Args:
            nom: Nom de famille (sera normalisé)
            prenom: Prénom (sera normalisé)
            matricule: Identifiant unique (obligatoire)
        """
        if not matricule or not matricule.strip():
            raise ValueError("Le matricule ne peut pas être vide")

        self.nom = nom.strip().capitalize()
        self.prenom = prenom.strip().capitalize()
        self.matricule = matricule.strip().upper()
        self._notes: List[float] = []

    def __str__(self) -> str:
        return f"{self.nom} {self.prenom} ({self.matricule})"

    def __repr__(self) -> str:
        return f"Etudiant(nom='{self.nom}', prenom='{self.prenom}', matricule='{self.matricule}')"

    def to_dict(self) -> dict:
        """Convertir l'objet Etudiant en dictionnaire pour le JSON"""
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "notes": self._notes
        }

    @property
    def notes(self) -> List[float]:
        """Retourne une copie de la liste des notes"""
        return self._notes.copy()

    def ajouter_note(self, note: float) -> bool:
        """Ajoute une note avec validation stricte"""
        try:
            note_float = float(note)
            if not (self.NOTE_MIN <= note_float <= self.NOTE_MAX):
                raise ValueError(f"La note doit être entre {self.NOTE_MIN} et {self.NOTE_MAX}")
            self._notes.append(note_float)
            return True
        except (ValueError, TypeError) as e:
            raise ValueError(f"Note invalide : {e}")

    def calculer_moyenne(self) -> float:
        """Calcule la moyenne arithmétique des notes"""
        if not self._notes:
            return 0.0
        return sum(self._notes) / len(self._notes)

    def est_admis(self) -> bool:
        """Détermine si l'étudiant est admis"""
        return self.calculer_moyenne() >= self.SEUIL_ADMISSION

    def vider_notes(self) -> None:
        """Supprime toutes les notes de l'étudiant"""
        self._notes.clear()

    def get_info(self) -> dict:
        """Retourne un dictionnaire avec toutes les informations"""
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

    def afficher_info(self) -> None:
        """Affiche les informations formatées de l'étudiant"""
        info = self.get_info()
        print("\n" + "=" * 50)
        print("INFORMATIONS DE L'ÉTUDIANT")
        print("=" * 50)
        print(f"Matricule    : {info['matricule']}")
        print(f"Nom          : {info['nom']}")
        print(f"Prénom       : {info['prenom']}")
        print(f"Notes        : {info['notes']}")
        print(f"Moyenne      : {info['moyenne']:.2f}/20")
        print(f"Décision     : {info['decision']}")
        print("=" * 50)


# =================================================================
# CLASSE CLASSE (Gestionnaire)
# =================================================================
class Classe:
    """Gère une collection d'étudiants et leurs statistiques"""

    def __init__(self, nom_classe: str = "Classe par défaut"):
        self._etudiants: List[Etudiant] = []
        self.nom_classe = nom_classe

    @property
    def etudiants(self) -> List[Etudiant]:
        """Retourne une copie de la liste des étudiants"""
        return self._etudiants.copy()

    def charger_etudiants(self):
        """Charge les étudiants depuis le fichier JSON"""
        try:
            if os.path.exists(CLASSE_DATA):
                with open(CLASSE_DATA, 'r', encoding='utf-8') as fichier:
                    data = json.load(fichier)
                    for matricule, info in data.items():
                        etudiant = Etudiant(
                            info['nom'],
                            info['prenom'],
                            matricule
                        )
                        for note in info.get('notes', []):
                            etudiant.ajouter_note(note)

                        self._etudiants.append(etudiant)
                print(f"✅ {len(self._etudiants)} étudiant(s) chargé(s) depuis le fichier {CLASSE_DATA}")
            else:
                print("ℹ️  Aucun fichier de données trouvé. Démarrage avec une classe vide.")
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"❌ Erreur de chargement : {e}")
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")

    def sauvegarder_etudiants(self):
        """Sauvegarde les étudiants dans le fichier JSON"""
        try:
            data = {}
            for etudiant in self._etudiants:
                data[etudiant.matricule] = etudiant.to_dict()

            with open(CLASSE_DATA, 'w', encoding='utf-8') as fichier:
                json.dump(data, fichier, indent=4, ensure_ascii=False)

            print(f"💾 {len(self._etudiants)} étudiant(s) sauvegardé(s) dans {CLASSE_DATA}")
            return True
        except Exception as e:
            print(f"❌ Erreur de sauvegarde : {e}")
            return False

    @property
    def nombre_etudiants(self) -> int:
        return len(self._etudiants)

    def matricule_existe(self, matricule: str) -> bool:
        """Vérifie si un matricule existe déjà"""
        matricule_normalise = matricule.strip().upper()
        return any(
            etudiant.matricule == matricule_normalise
            for etudiant in self._etudiants
        )

    def chercher_etudiant(self, matricule: str) -> Optional[Etudiant]:
        """Recherche un étudiant par son matricule"""
        matricule_normalise = matricule.strip().upper()
        return next(
            (etudiant for etudiant in self._etudiants
             if etudiant.matricule == matricule_normalise),
            None
        )

    def ajouter_etudiant(self, etudiant: Etudiant) -> bool:
        """Ajoute un étudiant à la classe"""
        if not isinstance(etudiant, Etudiant):
            raise TypeError("L'objet doit être de type Etudiant")

        if self.matricule_existe(etudiant.matricule):
            return False

        self._etudiants.append(etudiant)
        self.sauvegarder_etudiants()  # ✅ CORRECTION : Sauvegarde automatique
        return True

    def supprimer_etudiant(self, matricule: str) -> bool:
        """Supprime un étudiant de la classe"""
        etudiant = self.chercher_etudiant(matricule)
        if etudiant:
            self._etudiants.remove(etudiant)
            self.sauvegarder_etudiants()
            return True
        return False

    def calculer_moyenne_classe(self) -> float:
        """Calcule la moyenne générale de tous les étudiants"""
        if not self._etudiants:
            return 0.0
        total = sum(etudiant.calculer_moyenne() for etudiant in self._etudiants)
        return total / len(self._etudiants)

    def obtenir_meilleur_etudiant(self) -> Optional[Etudiant]:
        """Trouve l'étudiant avec la meilleure moyenne"""
        if not self._etudiants:
            return None
        return max(self._etudiants, key=lambda e: e.calculer_moyenne())

    def calculer_taux_reussite(self) -> float:
        """Calcule le pourcentage d'étudiants admis"""
        if not self._etudiants:
            return 0.0
        admis = sum(1 for etudiant in self._etudiants if etudiant.est_admis())
        return (admis / len(self._etudiants)) * 100

    def obtenir_statistiques(self) -> dict:
        """Calcule toutes les statistiques de la classe"""
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

    def afficher_statistiques(self) -> None:
        """Affiche les statistiques de la classe"""
        stats = self.obtenir_statistiques()

        print("\n" + "=" * 60)
        print(f"STATISTIQUES DE LA CLASSE : {self.nom_classe}")
        print("=" * 60)
        print(f"Nombre d'étudiants    : {stats['nombre_etudiants']}")
        print(f"Moyenne de la classe  : {stats['moyenne_classe']:.2f}/20")
        print(f"Taux de réussite      : {stats['taux_reussite']:.2f}%")
        print(f"Nombre d'admis        : {stats['nombre_admis']}")
        print(f"Nombre de refusés     : {stats['nombre_refuses']}")

        if stats['meilleur_etudiant']:
            print(f"Meilleur étudiant     : {stats['meilleur_etudiant']}")
            print(f"Meilleure moyenne     : {stats['meilleur_moyenne']:.2f}/20")

        print("=" * 60)

    def afficher_tous_les_etudiants(self) -> None:
        """Affiche la liste complète des étudiants"""
        if not self._etudiants:
            print("\n⚠️  La liste des étudiants est vide.")
            return

        print("\n" + "=" * 80)
        print(f"LISTE DES ÉTUDIANTS - {self.nom_classe}")
        print("=" * 80)

        etudiants_tries = sorted(
            self._etudiants,
            key=lambda e: (e.nom, e.prenom)
        )

        for i, etudiant in enumerate(etudiants_tries, 1):
            info = etudiant.get_info()
            print(f"\n{i}. {etudiant}")
            print(f"   Matricule : {info['matricule']}")
            print(f"   Notes     : {info['notes']}")
            print(f"   Moyenne   : {info['moyenne']:.2f}/20")
            print(f"   Statut    : {info['decision']}")

        print("=" * 80)


# =================================================================
# INTERFACE UTILISATEUR (CLI)
# =================================================================
class InterfaceGestion:
    """Gère l'interface en ligne de commande"""

    def __init__(self, classe: Classe):
        self.classe = classe

    def saisir_notes(self) -> List[float]:
        """Gère la saisie interactive des notes"""
        notes = []
        print("\n--- Saisie des notes ---")
        print("Entrez les notes (entre 0 et 20), tapez 'f' pour finir")

        while True:
            try:
                saisie = input("Note : ").strip().lower()

                if saisie == 'f':
                    break

                note = float(saisie)

                if not (Etudiant.NOTE_MIN <= note <= Etudiant.NOTE_MAX):
                    print(f"❌ La note doit être entre {Etudiant.NOTE_MIN} et {Etudiant.NOTE_MAX}")
                    continue

                notes.append(note)
                print(f"✅ Note {note} ajoutée")

            except ValueError:
                print("❌ Veuillez entrer un nombre valide")

        return notes

    def ajouter_etudiant_interactif(self) -> None:
        """Gère l'ajout interactif d'un étudiant"""
        print("\n" + "=" * 50)
        print("AJOUTER UN NOUVEL ÉTUDIANT")
        print("=" * 50)

        try:
            nom = input("Nom : ").strip()
            if not nom:
                print("❌ Le nom est obligatoire")
                return

            prenom = input("Prénom : ").strip()
            if not prenom:
                print("❌ Le prénom est obligatoire")
                return

            matricule = input("Matricule : ").strip()
            if not matricule:
                print("❌ Le matricule est obligatoire")
                return

            if self.classe.matricule_existe(matricule):
                print(f"❌ Le matricule {matricule.upper()} existe déjà")
                return

            etudiant = Etudiant(nom, prenom, matricule)

            notes = self.saisir_notes()
            for note in notes:
                etudiant.ajouter_note(note)

            if self.classe.ajouter_etudiant(etudiant):
                print(f"\n✅ Étudiant {etudiant} ajouté avec succès !")
                if not notes:
                    print("⚠️  Attention : aucune note n'a été saisie")
            else:
                print("❌ Erreur lors de l'ajout de l'étudiant")

        except Exception as e:
            print(f"❌ Erreur : {e}")

    def modifier_etudiant_interactif(self) -> None:
        """Gère la modification interactive d'un étudiant"""
        print("\n" + "=" * 50)
        print("MODIFIER UN ÉTUDIANT")
        print("=" * 50)

        matricule = input("Matricule de l'étudiant à modifier : ").strip()
        etudiant = self.classe.chercher_etudiant(matricule)

        if not etudiant:
            print(f"❌ Aucun étudiant trouvé avec le matricule {matricule}")
            return

        print("\n--- Informations actuelles ---")
        etudiant.afficher_info()

        nouveau_nom = input(f"\nNouveau nom [{etudiant.nom}] (Entrée pour conserver) : ").strip()
        if nouveau_nom:
            etudiant.nom = nouveau_nom.capitalize()

        nouveau_prenom = input(f"Nouveau prénom [{etudiant.prenom}] (Entrée pour conserver) : ").strip()
        if nouveau_prenom:
            etudiant.prenom = nouveau_prenom.capitalize()

        choix = input("\nModifier les notes ? (o/n) : ").strip().lower()
        if choix in ['o', 'oui']:
            etudiant.vider_notes()
            notes = self.saisir_notes()
            for note in notes:
                etudiant.ajouter_note(note)

        self.classe.sauvegarder_etudiants()  # ✅ Sauvegarde après modification
        print(f"\n✅ Étudiant {etudiant} modifié avec succès !")
        etudiant.afficher_info()

    def supprimer_etudiant_interactif(self) -> None:
        """Gère la suppression interactive d'un étudiant"""
        print("\n" + "=" * 50)
        print("SUPPRIMER UN ÉTUDIANT")
        print("=" * 50)

        matricule = input("Matricule de l'étudiant à supprimer : ").strip()
        etudiant = self.classe.chercher_etudiant(matricule)

        if not etudiant:
            print(f"❌ Aucun étudiant trouvé avec le matricule {matricule}")
            return

        print(f"\n⚠️  Vous allez supprimer : {etudiant}")
        confirmation = input("Confirmer la suppression ? (o/n) : ").strip().lower()

        if confirmation in ['o', 'oui']:
            if self.classe.supprimer_etudiant(matricule):
                print(f"✅ Étudiant {etudiant} supprimé avec succès")
            else:
                print("❌ Erreur lors de la suppression")
        else:
            print("❌ Suppression annulée")

    def afficher_menu(self) -> None:
        """Affiche le menu principal"""
        print("\n" + "=" * 60)
        print("SYSTÈME DE GESTION DES ÉTUDIANTS")
        print("=" * 60)
        print("1. Ajouter un étudiant")
        print("2. Modifier un étudiant")
        print("3. Supprimer un étudiant")
        print("4. Afficher un étudiant")
        print("5. Afficher tous les étudiants")
        print("6. Afficher les statistiques")
        print("7. Sauvegarder manuellement")
        print("q. Quitter")
        print("=" * 60)

    def executer(self) -> None:
        """Boucle principale de l'interface utilisateur"""
        while True:
            self.afficher_menu()

            choix = input("\nVotre choix : ").strip().lower()

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
                    etudiant.afficher_info()
                else:
                    print(f"❌ Aucun étudiant trouvé avec le matricule {matricule}")

            elif choix == '5':
                self.classe.afficher_tous_les_etudiants()

            elif choix == '6':
                self.classe.afficher_statistiques()

            elif choix == '7':
                self.classe.sauvegarder_etudiants()

            elif choix == 'q':
                self.classe.sauvegarder_etudiants()  # ✅ Sauvegarde avant de quitter
                print("\n👋 Au revoir !")
                break

            else:
                print("❌ Choix invalide, veuillez réessayer")


# =================================================================
# POINT D'ENTRÉE DU PROGRAMME
# =================================================================
def main():
    """Fonction principale pour démarrer l'application"""
    ma_classe = Classe("Terminale S1")

    # ✅ CORRECTION : Chargement au démarrage
    ma_classe.charger_etudiants()

    # Si la classe est vide, ajouter des données de test
    if ma_classe.nombre_etudiants == 0:
        print("\n📝 Création d'étudiants de test...")
        etudiants_test = [
            ("Aziz", "Baba", "A01", [15, 18, 16]),
            ("Karim", "Ali", "A02", [8, 11, 9]),
            ("Sara", "Doe", "A03", [19, 17, 18]),
        ]

        for nom, prenom, matricule, notes in etudiants_test:
            etudiant = Etudiant(nom, prenom, matricule)
            for note in notes:
                etudiant.ajouter_note(note)
            ma_classe.ajouter_etudiant(etudiant)

    interface = InterfaceGestion(ma_classe)
    interface.executer()


if __name__ == "__main__":
    main()