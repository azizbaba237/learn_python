import json
import os
from models.compte_bancaire import CompteBancaire


class FileManager:
    '''Gère la lecture et l'écriture des fichiers JSON'''

    @staticmethod
    def charger_comptes(fichier):
        '''Charge les comptes depuis un fichier JSON'''
        comptes = []
        try:
            if os.path.exists(fichier):
                with open(fichier, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for numero_compte, infos in data.items():
                        compte = CompteBancaire(
                            infos['titulaire'],
                            infos['numero_compte'],
                            float(infos['solde'])
                        )
                        comptes.append(compte)
                print(f"✔ {len(comptes)} compte(s) chargé(s)")
            else:
                print("⚠ Aucun fichier de données trouvé. Nouveau départ.")
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"❌ Erreur de chargement : {e}")
        return comptes

    @staticmethod
    def sauvegarder_comptes(fichier, comptes):
        '''Sauvegarde les comptes dans un fichier JSON'''
        try:
            # Créer le répertoire si nécessaire
            os.makedirs(os.path.dirname(fichier), exist_ok=True)

            data = {}
            for compte in comptes:
                data[compte.get_numero_compte()] = compte.to_dict()

            with open(fichier, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"❌ Erreur de sauvegarde : {e}")
            return False