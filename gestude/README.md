# Système de Gestion d'Étudiants

## 📋 Description

Application Python complète pour gérer une classe d'étudiants avec leurs notes et résultats.
Architecture modulaire suivant les principes SOLID.

## 🏗️ Architecture

```
student_management/
├── config/              # Configuration
├── models/              # Modèles de données
├── services/            # Logique métier
├── ui/                  # Interface utilisateur
├── utils/               # Utilitaires
├── data/                # Fichiers de données
├── tests/               # Tests unitaires
└── main.py              # Point d'entrée
```

## 🚀 Installation

1. Cloner le projet
2. Aucune dépendance externe requise (Python 3.8+)
3. Lancer : `python main.py`

## 💡 Fonctionnalités

- ✅ Ajouter/Modifier/Supprimer des étudiants
- ✅ Gérer les notes (validation automatique)
- ✅ Calculer moyennes et statistiques
- ✅ Persistance des données (JSON)
- ✅ Interface CLI intuitive
- ✅ Tests unitaires complets

## 🧪 Tests

```bash
# Tous les tests
python -m unittest discover tests

# Test spécifique
python -m unittest tests.test_etudiant
```

## 📖 Utilisation

```python
from services.classe_service import ClasseService
from models.etudiant import Etudiant

# Créer une classe
classe = ClasseService("Terminale S1")

# Ajouter un étudiant
etudiant = Etudiant("Dupont", "Jean", "E001")
etudiant.ajouter_note(15)
classe.ajouter_etudiant(etudiant)

# Sauvegarder
classe.sauvegarder_etudiants()
```

## 🎯 Principes Appliqués

- **SRP** : Une classe = une responsabilité
- **OCP** : Ouvert à l'extension, fermé à la modification
- **DRY** : Don't Repeat Yourself
- **Encapsulation** : Attributs privés avec properties
- **Validation** : Contrôles stricts des données

## 📝 Licence

Projet éducatif - Libre d'utilisation
