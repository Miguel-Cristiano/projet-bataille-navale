from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin


def test_init():
    grille = Grille(5, 8)
    assert isinstance(grille, Grille)
    assert grille.lignes == 5
    assert grille.colonnes == 8
    assert grille.vide == "∿"
    assert grille.grille == ["∿"] * 40


def test_contient():
    grille = Grille(2, 3)
    assert grille.contient(0, 0)
    assert grille.contient(1, 2)
    assert not grille.contient(-1, 0)
    assert not grille.contient(0, -1)
    assert not grille.contient(2, 0)
    assert not grille.contient(0, 3)


def test_tirer():
    grille = Grille(2, 3)
    assert grille.tirer(1, 1)
    assert grille.grille == ["∿", "∿", "∿", "∿", "x", "∿"]
    assert grille.tirer(0, 0, "💣")
    assert grille.grille[0] == "💣"
    avant = grille.grille.copy()
    assert not grille.tirer(-1, 0)
    assert not grille.tirer(0, 3)
    assert grille.grille == avant


def test_str():
    grille = Grille(5, 8)
    assert str(grille) == "\n".join(["∿" * 8] * 5)
    grille.tirer(2, 3)
    assert str(grille) == "∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿\n∿∿∿x∿∿∿∿\n∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿"


def test_ajoute():
    grille = Grille(2, 3)
    bateau = Bateau(1, 0, longueur=2)
    assert grille.peut_ajouter(bateau)
    assert grille.ajoute(bateau)
    assert grille.grille == ["∿", "∿", "∿", "⛵", "⛵", "∿"]


def test_ajoute_depassement():
    for bateau in [Bateau(1, 0, 2, True), Bateau(1, 0, 4, True),
                   Bateau(0, 2, 2), Bateau(-1, 0), Bateau(0, -1)]:
        grille = Grille(2, 3)
        assert not grille.peut_ajouter(bateau)
        assert not grille.ajoute(bateau)
        assert grille.grille == ["∿"] * 6


def test_ajoute_chevauchement():
    grille = Grille(3, 4)
    grille.ajoute(Bateau(1, 1, 2))
    avant = grille.grille.copy()
    assert not grille.ajoute(Bateau(0, 2, 3, True))
    assert grille.grille == avant
    assert grille.ajoute(Bateau(2, 1, 2))


def test_ajoute_types():
    types = [PorteAvion, Croiseur, Torpilleur, SousMarin]
    marques = ["🚢", "⛴", "🚣", "🐟"]
    longueurs = [4, 3, 2, 2]
    for i in range(4):
        grille = Grille(5, 5)
        assert grille.ajoute(types[i](1, 0))
        assert grille.grille.count(marques[i]) == longueurs[i]
