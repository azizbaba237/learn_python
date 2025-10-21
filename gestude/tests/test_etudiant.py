# ============================================================================
# tests/test_etudiant.py
# ============================================================================
TEST_ETUDIANT = """
Tests unitaires pour la classe Etudiant
"""
import unittest
from models.etudiant import Etudiant


class TestEtudiant(unittest.TestCase):
    """Tests pour la classe Etudiant"""

    def setUp(self):
        """Initialisation avant chaque test"""
        self.etudiant = Etudiant("Dupont", "Jean", "E001")

    def test_creation_etudiant(self):
        """Test de la création d'un étudiant"""
        self.assertEqual(self.etudiant.nom, "Dupont")
        self.assertEqual(self.etudiant.prenom, "Jean")
        self.assertEqual(self.etudiant.matricule, "E001")
        self.assertEqual(len(self.etudiant.notes), 0)

    def test_normalisation_donnees(self):
        """Test de la normalisation des données"""
        etudiant = Etudiant("  dupont  ", "  jean  ", "  e001  ")
        self.assertEqual(etudiant.nom, "Dupont")
        self.assertEqual(etudiant.prenom, "Jean")
        self.assertEqual(etudiant.matricule, "E001")

    def test_matricule_vide(self):
        """Test avec un matricule vide"""
        with self.assertRaises(ValueError):
            Etudiant("Dupont", "Jean", "")

    def test_ajout_note_valide(self):
        """Test d'ajout d'une note valide"""
        self.assertTrue(self.etudiant.ajouter_note(15.5))
        self.assertEqual(len(self.etudiant.notes), 1)
        self.assertEqual(self.etudiant.notes[0], 15.5)

    def test_ajout_note_invalide(self):
        """Test d'ajout d'une note invalide"""
        with self.assertRaises(ValueError):
            self.etudiant.ajouter_note(25)

        with self.assertRaises(ValueError):
            self.etudiant.ajouter_note(-5)

    def test_calcul_moyenne(self):
        """Test du calcul de moyenne"""
        self.etudiant.ajouter_note(10)
        self.etudiant.ajouter_note(15)
        self.etudiant.ajouter_note(20)
        self.assertEqual(self.etudiant.calculer_moyenne(), 15.0)

    def test_moyenne_sans_notes(self):
        """Test de moyenne sans notes"""
        self.assertEqual(self.etudiant.calculer_moyenne(), 0.0)

    def test_est_admis(self):
        """Test de la vérification d'admission"""
        self.etudiant.ajouter_note(12)
        self.etudiant.ajouter_note(14)
        self.assertTrue(self.etudiant.est_admis())

    def test_est_refuse(self):
        """Test de la vérification de refus"""
        self.etudiant.ajouter_note(5)
        self.etudiant.ajouter_note(7)
        self.assertFalse(self.etudiant.est_admis())

    def test_vider_notes(self):
        """Test de la suppression des notes"""
        self.etudiant.ajouter_note(15)
        self.etudiant.ajouter_note(18)
        self.etudiant.vider_notes()
        self.assertEqual(len(self.etudiant.notes), 0)

    def test_to_dict(self):
        """Test de la conversion en dictionnaire"""
        self.etudiant.ajouter_note(15)
        data = self.etudiant.to_dict()

        self.assertEqual(data['nom'], "Dupont")
        self.assertEqual(data['prenom'], "Jean")
        self.assertEqual(data['notes'], [15])

    def test_from_dict(self):
        """Test de la création depuis un dictionnaire"""
        data = {
            'nom': 'Dupont',
            'prenom': 'Jean',
            'notes': [15, 18, 12]
        }
        etudiant = Etudiant.from_dict("E001", data)

        self.assertEqual(etudiant.matricule, "E001")
        self.assertEqual(etudiant.nom, "Dupont")
        self.assertEqual(len(etudiant.notes), 3)

    def test_get_info(self):
        """Test de récupération des informations"""
        self.etudiant.ajouter_note(15)
        info = self.etudiant.get_info()

        self.assertIn('matricule', info)
        self.assertIn('nom', info)
        self.assertIn('moyenne', info)
        self.assertIn('decision', info)


if __name__ == '__main__':
    unittest.main()
