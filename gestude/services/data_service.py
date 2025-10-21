# ============================================================================
# services/data_service.py
# ============================================================================
DATA_SERVICE = """
Service de gestion de la persistance des données (JSON)
"""
import json
import os
from typing import Dict, List
from models.etudiant import Etudiant
from config.settings import DATA_PATH, DATA_DIR, ENCODING


class DataService:
    """Gère la sauvegarde et le chargement des données"""

    @staticmethod
    def assurer_dossier_data() -> None:
        """Crée le dossier data s'il n'existe pas"""
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

    @staticmethod
    def charger_etudiants() -> List[Etudiant]:
        """
        Charge les étudiants depuis le fichier JSON.

        Returns:
            List[Etudiant]: Liste des étudiants chargés
        """
        DataService.assurer_dossier_data()

        if not os.path.exists(DATA_PATH):
            return []

        try:
            with open(DATA_PATH, 'r', encoding=ENCODING) as fichier:
                data = json.load(fichier)
                etudiants = []

                for matricule, info in data.items():
                    etudiant = Etudiant.from_dict(matricule, info)
                    etudiants.append(etudiant)

                return etudiants

        except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
            print(f"❌ Erreur de chargement : {e}")
            return []
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")
            return []

    @staticmethod
    def sauvegarder_etudiants(etudiants: List[Etudiant]) -> bool:
        """
        Sauvegarde les étudiants dans le fichier JSON.

        Args:
            etudiants: Liste des étudiants à sauvegarder

        Returns:
            bool: True si succès
        """
        DataService.assurer_dossier_data()

        try:
            data = {}
            for etudiant in etudiants:
                data[etudiant.matricule] = etudiant.to_dict()

            with open(DATA_PATH, 'w', encoding=ENCODING) as fichier:
                json.dump(data, fichier, indent=4, ensure_ascii=False)

            return True

        except Exception as e:
            print(f"❌ Erreur de sauvegarde : {e}")
            return False