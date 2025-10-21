# ============================================================================
# tests/test_classe.py
# ============================================================================
TEST_CLASSE = """
Tests unitaires pour ClasseService
"""
import unittest
import os
from models.etudiant import Etudiant
from services.classe_service import ClasseService
from config.settings import DATA_PATH


class TestClasseService(unittest.TestCase):
    """Tests pour ClasseService"""

    def setUp(self):
        """Initialisation avant chaque test"""
        self.classe = ClasseService("Test Classe")

        # Supprimer le fichier de test s'il existe
        if os.path.exists(DATA_PATH):
            os.remove(DATA_PATH)

    def tearDown(self):
        """Nettoyage après chaque test"""
        if os.path.exists(DATA_PATH):
            os.remove(DATA_PATH)

    def test_creation_classe(self):
        """Test de la création d'une classe"""
        self.assertEqual(self.classe.nom_classe, "Test Classe")
        self.assertEqual(self.classe.nombre_etudiants, 0)

    def test_ajout_etudiant(self):
        """Test d'ajout d'un étudiant"""
        etudiant = Etudiant("Dupont", "Jean", "E001")
        self.assertTrue(self.classe.ajouter_etudiant(etudiant))
        self.assertEqual(self.classe.nombre_etudiants, 1)

    def test_ajout_etudiant_doublon(self):
        """Test d'ajout d'un étudiant avec matricule existant"""
        etudiant1 = Etudiant("Dupont", "Jean", "E001")
        etudiant2 = Etudiant("Martin", "Paul", "E001")

        self.classe.ajouter_etudiant(etudiant1)
        self.assertFalse(self.classe.ajouter_etudiant(etudiant2))
        self.assertEqual(self.classe.nombre_etudiants, 1)

    def test_matricule_existe(self):
        """Test de vérification d'existence de matricule"""
        etudiant = Etudiant("Dupont", "Jean", "E001")
        self.classe.ajouter_etudiant(etudiant)

        self.assertTrue(self.classe.matricule_existe("E001"))
        self.assertTrue(self.classe.matricule_existe("e001"))  # Test insensible à la casse
        self.assertFalse(self.classe.matricule_existe("E999"))

    def test_chercher_etudiant(self):
        """Test de recherche d'étudiant"""
        etudiant = Etudiant("Dupont", "Jean", "E001")
        self.classe.ajouter_etudiant(etudiant)

        trouve = self.classe.chercher_etudiant("E001")
        self.assertIsNotNone(trouve)
        self.assertEqual(trouve.matricule, "E001")

    def test_chercher_etudiant_inexistant(self):
        """Test de recherche d'un étudiant inexistant"""
        resultat = self.classe.chercher_etudiant("E999")
        self.assertIsNone(resultat)

    def test_suppression_etudiant(self):
        """Test de suppression d'un étudiant"""
        etudiant = Etudiant("Dupont", "Jean", "E001")
        self.classe.ajouter_etudiant(etudiant)

        self.assertTrue(self.classe.supprimer_etudiant("E001"))
        self.assertEqual(self.classe.nombre_etudiants, 0)

    def test_calcul_moyenne_classe(self):
        """Test du calcul de moyenne de classe"""
        etudiant1 = Etudiant("Dupont", "Jean", "E001")
        etudiant1.ajouter_note(10)

        etudiant2 = Etudiant("Martin", "Paul", "E002")
        etudiant2.ajouter_note(20)

        self.classe.ajouter_etudiant(etudiant1)
        self.classe.ajouter_etudiant(etudiant2)

        self.assertEqual(self.classe.calculer_moyenne_classe(), 15.0)

    def test_moyenne_classe_vide(self):
        """Test de moyenne d'une classe vide"""
        self.assertEqual(self.classe.calculer_moyenne_classe(), 0.0)

    def test_meilleur_etudiant(self):
        """Test de recherche du meilleur étudiant"""
        etudiant1 = Etudiant("Dupont", "Jean", "E001")
        etudiant1.ajouter_note(10)

        etudiant2 = Etudiant("Martin", "Paul", "E002")
        etudiant2.ajouter_note(18)

        self.classe.ajouter_etudiant(etudiant1)
        self.classe.ajouter_etudiant(etudiant2)

        meilleur = self.classe.obtenir_meilleur_etudiant()
        self.assertEqual(meilleur.matricule, "E002")

    def test_taux_reussite(self):
        """Test du calcul du taux de réussite"""
        etudiant1 = Etudiant("Dupont", "Jean", "E001")
        etudiant1.ajouter_note(12)

        etudiant2 = Etudiant("Martin", "Paul", "E002")
        etudiant2.ajouter_note(8)

        etudiant3 = Etudiant("Durand", "Marie", "E003")
        etudiant3.ajouter_note(15)

        self.classe.ajouter_etudiant(etudiant1)
        self.classe.ajouter_etudiant(etudiant2)
        self.classe.ajouter_etudiant(etudiant3)

        # 2 admis sur 3 = 66.67%
        self.assertAlmostEqual(self.classe.calculer_taux_reussite(), 66.67, places=2)

    def test_statistiques(self):
        """Test de génération des statistiques"""
        etudiant = Etudiant("Dupont", "Jean", "E001")
        etudiant.ajouter_note(15)
        self.classe.ajouter_etudiant(etudiant)

        stats = self.classe.obtenir_statistiques()

        self.assertEqual(stats['nombre_etudiants'], 1)
        self.assertEqual(stats['nombre_admis'], 1)
        self.assertEqual(stats['nombre_refuses'], 0)
        self.assertIsNotNone(stats['meilleur_etudiant'])


if __name__ == '__main__':
    unittest.main()
