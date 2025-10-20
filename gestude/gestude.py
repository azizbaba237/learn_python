"""
Système de Gestion d'Étudiants Optimisé

Objectif : Gérer une classe d'étudiants avec leurs notes et résultats
Concepts : POO, encapsulation, validation des données, séparation des responsabilités
"""

from typing import List, Optional
from dataclasses import dataclass, field


# =================================================================
# CLASSE ETUDIANT
# =================================================================
class Etudiant:
    """
    Représente un étudiant avec ses informations personnelles et académiques.

    Attributs:
        nom (str): Nom de famille de l'étudiant
        prenom (str): Prénom de l'étudiant
        matricule (str): Identifiant unique de l'étudiant
        notes (List[float]): Liste des notes obtenues (privé via property)
    """

    # Constante de classe pour le seuil d'admission
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

        Raises:
            ValueError: Si le matricule est vide
        """
        # Validation du matricule (obligatoire et non vide)
        if not matricule or not matricule.strip():
            raise ValueError("Le matricule ne peut pas être vide")

        # Normalisation des données : strip() + capitalize() pour format uniforme
        self.nom = nom.strip().capitalize()
        self.prenom = prenom.strip().capitalize()
        self.matricule = matricule.strip().upper()  # Matricule en majuscules

        # Attribut privé pour les notes (encapsulation)
        self._notes: List[float] = []

    def __str__(self) -> str:
        """Représentation textuelle lisible de l'étudiant."""
        return f"{self.nom} {self.prenom} ({self.matricule})"

    def __repr__(self) -> str:
        """Représentation technique pour le débogage."""
        return f"Etudiant(nom='{self.nom}', prenom='{self.prenom}', matricule='{self.matricule}')"

    # Property pour l'encapsulation des notes (lecture seule de l'extérieur)
    @property
    def notes(self) -> List[float]:
        """Retourne une copie de la liste des notes (évite les modifications externes)."""
        return self._notes.copy()

    def ajouter_note(self, note: float) -> bool:
        """
        Ajoute une note avec validation stricte.

        Args:
            note: La note à ajouter (entre 0 et 20)

        Returns:
            bool: True si ajout réussi, False sinon

        Raises:
            ValueError: Si la note est hors limites
        """
        try:
            # Conversion en float pour accepter "15" ou "15.5"
            note_float = float(note)

            # Validation de la plage de notes
            if not (self.NOTE_MIN <= note_float <= self.NOTE_MAX):
                raise ValueError(
                    f"La note doit être entre {self.NOTE_MIN} et {self.NOTE_MAX}"
                )

            self._notes.append(note_float)
            return True

        except (ValueError, TypeError) as e:
            # On relance l'exception pour que l'appelant puisse la gérer
            raise ValueError(f"Note invalide : {e}")

    def calculer_moyenne(self) -> float:
        """
        Calcule la moyenne arithmétique des notes.

        Returns:
            float: La moyenne (0 si aucune note)
        """
        # Utilisation de la fonction built-in sum() et len()
        if not self._notes:
            return 0.0
        return sum(self._notes) / len(self._notes)

    def est_admis(self) -> bool:
        """
        Détermine si l'étudiant est admis (moyenne >= seuil).

        Returns:
            bool: True si admis, False sinon
        """
        return self.calculer_moyenne() >= self.SEUIL_ADMISSION

    def vider_notes(self) -> None:
        """Supprime toutes les notes de l'étudiant."""
        self._notes.clear()  # Plus efficace que self._notes = []

    def get_info(self) -> dict:
        """
        Retourne un dictionnaire avec toutes les informations de l'étudiant.

        Returns:
            dict: Informations complètes (nom, prénom, matricule, notes, moyenne, statut)
        """
        moyenne = self.calculer_moyenne()
        return {
            'matricule': self.matricule,
            'nom': self.nom,
            'prenom': self.prenom,
            'notes': self.notes,  # Utilise la property (copie)
            'moyenne': moyenne,
            'admis': self.est_admis(),
            'decision': 'Admis' if self.est_admis() else 'Refusé'
        }

    def afficher_info(self) -> None:
        """Affiche les informations formatées de l'étudiant dans la console."""
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
    """
    Gère une collection d'étudiants et leurs statistiques.

    Attributs:
        etudiants (List[Etudiant]): Liste des étudiants inscrits
        nom_classe (str): Nom optionnel de la classe
    """

    def __init__(self, nom_classe: str = "Classe par défaut"):
        """
        Initialise une nouvelle classe.

        Args:
            nom_classe: Nom descriptif de la classe
        """
        self._etudiants: List[Etudiant] = []
        self.nom_classe = nom_classe

    @property
    def etudiants(self) -> List[Etudiant]:
        """Retourne une copie de la liste des étudiants."""
        return self._etudiants.copy()

    @property
    def nombre_etudiants(self) -> int:
        """Retourne le nombre d'étudiants dans la classe."""
        return len(self._etudiants)

    def matricule_existe(self, matricule: str) -> bool:
        """
        Vérifie si un matricule existe déjà dans la classe.

        Args:
            matricule: Le matricule à vérifier

        Returns:
            bool: True si le matricule existe, False sinon
        """
        matricule_normalise = matricule.strip().upper()
        # Utilisation de any() pour une recherche efficace
        return any(
            etudiant.matricule == matricule_normalise
            for etudiant in self._etudiants
        )

    def chercher_etudiant(self, matricule: str) -> Optional[Etudiant]:
        """
        Recherche un étudiant par son matricule.

        Args:
            matricule: Le matricule à rechercher

        Returns:
            Etudiant ou None: L'étudiant trouvé ou None
        """
        matricule_normalise = matricule.strip().upper()
        # Utilisation de next() avec générateur (plus efficace qu'une boucle)
        return next(
            (etudiant for etudiant in self._etudiants
             if etudiant.matricule == matricule_normalise),
            None  # Valeur par défaut si non trouvé
        )

    def ajouter_etudiant(self, etudiant: Etudiant) -> bool:
        """
        Ajoute un étudiant à la classe après validation.

        Args:
            etudiant: L'étudiant à ajouter

        Returns:
            bool: True si ajouté, False si matricule existe déjà

        Raises:
            TypeError: Si l'objet n'est pas de type Etudiant
        """
        # Validation du type
        if not isinstance(etudiant, Etudiant):
            raise TypeError("L'objet doit être de type Etudiant")

        # Vérification de l'unicité du matricule
        if self.matricule_existe(etudiant.matricule):
            return False

        self._etudiants.append(etudiant)
        return True

    def supprimer_etudiant(self, matricule: str) -> bool:
        """
        Supprime un étudiant de la classe.

        Args:
            matricule: Le matricule de l'étudiant à supprimer

        Returns:
            bool: True si supprimé, False si non trouvé
        """
        etudiant = self.chercher_etudiant(matricule)
        if etudiant:
            self._etudiants.remove(etudiant)
            return True
        return False

    def calculer_moyenne_classe(self) -> float:
        """
        Calcule la moyenne générale de tous les étudiants.

        Returns:
            float: La moyenne de la classe (0 si aucun étudiant)
        """
        if not self._etudiants:
            return 0.0

        # Somme des moyennes individuelles / nombre d'étudiants
        total = sum(etudiant.calculer_moyenne() for etudiant in self._etudiants)
        return total / len(self._etudiants)

    def obtenir_meilleur_etudiant(self) -> Optional[Etudiant]:
        """
        Trouve l'étudiant avec la meilleure moyenne.

        Returns:
            Etudiant ou None: Le meilleur étudiant ou None si liste vide
        """
        if not self._etudiants:
            return None

        # Utilisation de max() avec une clé personnalisée
        return max(self._etudiants, key=lambda e: e.calculer_moyenne())

    def calculer_taux_reussite(self) -> float:
        """
        Calcule le pourcentage d'étudiants admis.

        Returns:
            float: Taux de réussite en pourcentage (0 si aucun étudiant)
        """
        if not self._etudiants:
            return 0.0

        # Compte le nombre d'étudiants admis
        admis = sum(1 for etudiant in self._etudiants if etudiant.est_admis())
        return (admis / len(self._etudiants)) * 100

    def obtenir_statistiques(self) -> dict:
        """
        Calcule toutes les statistiques de la classe.

        Returns:
            dict: Dictionnaire contenant toutes les statistiques
        """
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
        """Affiche les statistiques de la classe de manière formatée."""
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
        """Affiche la liste complète des étudiants avec leurs informations."""
        if not self._etudiants:
            print("\n⚠️  La liste des étudiants est vide.")
            return

        print("\n" + "=" * 80)
        print(f"LISTE DES ÉTUDIANTS - {self.nom_classe}")
        print("=" * 80)

        # Tri alphabétique par nom puis prénom
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
    """
    Gère l'interface en ligne de commande pour interagir avec la classe.
    Séparation des responsabilités : UI séparée de la logique métier.
    """

    def __init__(self, classe: Classe):
        """
        Initialise l'interface avec une classe à gérer.

        Args:
            classe: Instance de Classe à gérer
        """
        self.classe = classe

    def saisir_notes(self) -> List[float]:
        """
        Gère la saisie interactive des notes.

        Returns:
            List[float]: Liste des notes saisies
        """
        notes = []
        print("\n--- Saisie des notes ---")
        print("Entrez les notes (entre 0 et 20), tapez 'f' pour finir")

        while True:
            try:
                saisie = input("Note : ").strip().lower()

                if saisie == 'f':
                    break

                note = float(saisie)

                # Validation via les constantes de la classe Etudiant
                if not (Etudiant.NOTE_MIN <= note <= Etudiant.NOTE_MAX):
                    print(f"❌ La note doit être entre {Etudiant.NOTE_MIN} et {Etudiant.NOTE_MAX}")
                    continue

                notes.append(note)
                print(f"✅ Note {note} ajoutée")

            except ValueError:
                print("❌ Veuillez entrer un nombre valide")

        return notes

    def ajouter_etudiant_interactif(self) -> None:
        """Gère l'ajout interactif d'un étudiant."""
        print("\n" + "=" * 50)
        print("AJOUTER UN NOUVEL ÉTUDIANT")
        print("=" * 50)

        try:
            # Saisie des informations
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

            # Vérification de l'unicité du matricule
            if self.classe.matricule_existe(matricule):
                print(f"❌ Le matricule {matricule.upper()} existe déjà")
                return

            # Création de l'étudiant
            etudiant = Etudiant(nom, prenom, matricule)

            # Saisie des notes
            notes = self.saisir_notes()
            for note in notes:
                etudiant.ajouter_note(note)

            # Ajout à la classe
            if self.classe.ajouter_etudiant(etudiant):
                print(f"\n✅ Étudiant {etudiant} ajouté avec succès !")
                if not notes:
                    print("⚠️  Attention : aucune note n'a été saisie")
            else:
                print("❌ Erreur lors de l'ajout de l'étudiant")

        except Exception as e:
            print(f"❌ Erreur : {e}")

    def modifier_etudiant_interactif(self) -> None:
        """Gère la modification interactive d'un étudiant."""
        print("\n" + "=" * 50)
        print("MODIFIER UN ÉTUDIANT")
        print("=" * 50)

        matricule = input("Matricule de l'étudiant à modifier : ").strip()
        etudiant = self.classe.chercher_etudiant(matricule)

        if not etudiant:
            print(f"❌ Aucun étudiant trouvé avec le matricule {matricule}")
            return

        # Affichage des informations actuelles
        print("\n--- Informations actuelles ---")
        etudiant.afficher_info()

        # Modification du nom
        nouveau_nom = input(f"\nNouveau nom [{etudiant.nom}] (Entrée pour conserver) : ").strip()
        if nouveau_nom:
            etudiant.nom = nouveau_nom.capitalize()

        # Modification du prénom
        nouveau_prenom = input(f"Nouveau prénom [{etudiant.prenom}] (Entrée pour conserver) : ").strip()
        if nouveau_prenom:
            etudiant.prenom = nouveau_prenom.capitalize()

        # Modification des notes
        choix = input("\nModifier les notes ? (o/n) : ").strip().lower()
        if choix in ['o', 'oui']:
            etudiant.vider_notes()
            notes = self.saisir_notes()
            for note in notes:
                etudiant.ajouter_note(note)

        print(f"\n✅ Étudiant {etudiant} modifié avec succès !")
        etudiant.afficher_info()

    def supprimer_etudiant_interactif(self) -> None:
        """Gère la suppression interactive d'un étudiant."""
        print("\n" + "=" * 50)
        print("SUPPRIMER UN ÉTUDIANT")
        print("=" * 50)

        matricule = input("Matricule de l'étudiant à supprimer : ").strip()
        etudiant = self.classe.chercher_etudiant(matricule)

        if not etudiant:
            print(f"❌ Aucun étudiant trouvé avec le matricule {matricule}")
            return

        # Confirmation
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
        """Affiche le menu principal."""
        print("\n" + "=" * 60)
        print("SYSTÈME DE GESTION DES ÉTUDIANTS")
        print("=" * 60)
        print("1. Ajouter un étudiant")
        print("2. Modifier un étudiant")
        print("3. Supprimer un étudiant")
        print("4. Afficher un étudiant")
        print("5. Afficher tous les étudiants")
        print("6. Afficher les statistiques")
        print("q. Quitter")
        print("=" * 60)

    def executer(self) -> None:
        """Boucle principale de l'interface utilisateur."""
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

            elif choix == 'q':
                print("\n👋 Au revoir !")
                break

            else:
                print("❌ Choix invalide, veuillez réessayer")


# =================================================================
# POINT D'ENTRÉE DU PROGRAMME
# =================================================================
def main():
    """Fonction principale pour démarrer l'application."""
    # Création de la classe
    ma_classe = Classe("Terminale S1")

    # Ajout d'étudiants de test
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

    # Lancement de l'interface
    interface = InterfaceGestion(ma_classe)
    interface.executer()


if __name__ == "__main__":
    main()