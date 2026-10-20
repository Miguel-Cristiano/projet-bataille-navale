from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin
from grille import Grille


def test_init():
    bateau = Bateau(2, 3)
    assert bateau.ligne == 2
    assert bateau.colonne == 3
    assert bateau.longueur == 1
    assert bateau.vertical is False
    assert bateau.marque == "⛵"


def test_positions():
    assert Bateau(2, 3).positions() == [(2, 3)]
    assert Bateau(2, 3, 3).positions() == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, 3, True).positions() == [(2, 3), (3, 3), (4, 3)]


def test_chevauche():
    bateau = Bateau(2, 3, 3)
    autre = Bateau(1, 4, 3, True)
    assert bateau.chevauche(autre)
    assert autre.chevauche(bateau)
    assert not bateau.chevauche(Bateau(0, 0, 2))
    assert not bateau.chevauche(Bateau(2, 6, 2))


def test_coulé():
    grille = Grille(4, 5)
    bateau = Bateau(1, 1, 2)
    grille.ajoute(bateau)
    assert not bateau.coulé(grille)
    grille.tirer(1, 1)
    assert not bateau.coulé(grille)
    grille.tirer(1, 2)
    assert bateau.coulé(grille)
    assert not Bateau(4, 0).coulé(grille)


def test_types():
    types = [PorteAvion, Croiseur, Torpilleur, SousMarin]
    longueurs = [4, 3, 2, 2]
    marques = ["🚢", "⛴", "🚣", "🐟"]
    for i in range(4):
        bateau = types[i](1, 2, True)
        assert isinstance(bateau, Bateau)
        assert bateau.longueur == longueurs[i]
        assert bateau.marque == marques[i]
        assert bateau.vertical is True
        assert bateau.positions()[-1] == (longueurs[i], 2)
        assert types[i](0, 0).vertical is False
