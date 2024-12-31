import pytest
import sys
import os

CHEMIN_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHEMIN_TEST = CHEMIN_BASE + "\\src\\"

sys.path.append(CHEMIN_TEST)


from gestion_chevaux import lister_genre
from gestion_chevaux import lister_statut
from gestion_chevaux import lister_tous_chevaux



def test_lister_genre():
    resultat = lister_genre()
    assert len(resultat) == 2
    assert resultat[0] == {'genre_id': 1, 'genre': 'Hongre'}
    assert resultat[1] == {'genre_id': 2, 'genre': 'Jument'}


def test_lister_statut():
    resultat = lister_statut()
    assert len(resultat) == 2
    assert resultat[0] == {'statut_id': 1, 'etat': 'Actif'}
    assert resultat[1] == {'statut_id': 2, 'etat': 'En retraite'}


def test_lister_tous_chevaux():
    resultat = lister_tous_chevaux()
    assert len(resultat) == 18
    print(resultat[0] )
    assert resultat[0] == {'ID': 1, 'NOM': "Écuyer d'Or", 'GENRE': 'Hongre', 'STATUT': 'Actif'}
    assert resultat[17] == {'ID': 18, 'NOM': "Douce Mélodie", 'GENRE': 'Jument', 'STATUT': 'Actif'}

if __name__ == "__main__":
    pytest.main()