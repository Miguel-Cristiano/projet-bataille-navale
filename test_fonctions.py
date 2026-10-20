from bateau import Torpilleur
from grille import Grille
from fonctions import (placements_possibles, créer_partie, tirer, terminé,
                       texte_grille)


def test_placements_possibles():
    grille = Grille(2, 3)
    possibilités = placements_possibles(grille, Torpilleur)
    assert len(possibilités) == 7
    for bateau in possibilités:
        assert grille.peut_ajouter(bateau)
    grille.ajoute(Torpilleur(0, 0))
    possibilités = placements_possibles(grille, Torpilleur)
    assert len(possibilités) == 3
    assert placements_possibles(Grille(1, 1), Torpilleur) == []


def test_créer_partie():
    grille, affichage, bateaux = créer_partie()
    assert grille.lignes == 8
    assert grille.colonnes == 10
    assert len(bateaux) == 4
    assert affichage.grille == ["∿"] * 80
    positions = []
    for bateau in bateaux:
        for ligne, colonne in bateau.positions():
            assert grille.contient(ligne, colonne)
            assert (ligne, colonne) not in positions
            positions.append((ligne, colonne))
            assert grille.grille[ligne * 10 + colonne] == bateau.marque
    assert len(positions) == 11


def test_tirer_et_terminé():
    grille = Grille(3, 4)
    affichage = Grille(3, 4)
    bateau = Torpilleur(1, 1)
    bateaux = [bateau]
    grille.ajoute(bateau)
    assert not terminé(grille, bateaux)
    assert tirer(grille, affichage, bateaux, 0, 0) == "À l'eau "
    assert affichage.grille[0] == "x"
    assert tirer(grille, affichage, bateaux, 1, 1) == "touché "
    assert affichage.grille[5] == "💣"
    assert not terminé(grille, bateaux)
    assert tirer(grille, affichage, bateaux, 1, 2) == "Torpilleur coulé "
    assert affichage.grille[5:7] == ["🚣", "🚣"]
    assert bateau.coulé(grille)
    assert terminé(grille, bateaux)
    avant = affichage.grille.copy()
    assert tirer(grille, affichage, bateaux, 1, 1) == "Tu as déjà tiré sur cette case"
    assert tirer(grille, affichage, bateaux, -1, 0) == "Cette case n'est pas dans la grille"
    assert affichage.grille == avant


def test_texte_grille():
    grille = Grille(2, 3)
    grille.tirer(1, 2)
    assert texte_grille(grille) == "    0  1  2  \n0   ∿  ∿  ∿  \n1   ∿  ∿  x  "


def test_partie_complete():
    grille, affichage, bateaux = créer_partie()
    assert not terminé(grille, bateaux)
    for bateau in bateaux:
        for ligne, colonne in bateau.positions():
            tirer(grille, affichage, bateaux, ligne, colonne)
        assert bateau.coulé(grille)
        for ligne, colonne in bateau.positions():
            assert affichage.grille[ligne * grille.colonnes + colonne] == bateau.marque
    assert terminé(grille, bateaux)
