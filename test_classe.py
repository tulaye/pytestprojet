from classe import Classe
from etudiant import Etudiant
import pytest

class TestClasse:

    def test_add_etudiant(self):
    #arrange
        classe =Classe("M1Miage", "Master")
        etudiant = Etudiant("Wade","Mbaye",22,"")
        nb_etudiants_initial = len(classe.etudiants)
    #act
        classe.add_etudiant(etudiant)
    #Assert
        assert len(classe.etudiants) == nb_etudiants_initial + 1

    def test_remove_etudiant(self):
        classe =Classe("M1Miage", "Master")
        nb_etudiants_initial = len(classe.etudiants)
        e1 = Etudiant("GUEYE","Mbaye",22,"")
        e2 = Etudiant("Paye","Mbaye",22,"")
    #act
        classe.add_etudiant(e1)
        classe.add_etudiant(e2)
        classe.remove_etudiant(e2)
    #Assert
        assert len(classe.etudiants)-nb_etudiants_initial == 1

    def test_etudiant_not_in_classe(self):
    #arrange
      classe = Classe("M1Miage", "Master")
      etudiant = Etudiant("Wade","Mbaye",22,"")
    #Act & Assert
      with pytest.raises(ValueError,match="L'étudiant n'est pas dans la classe"):
            classe.remove_etudiant(etudiant)
