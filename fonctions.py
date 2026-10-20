import random

from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin
from grille import Grille


def placements_possibles(grille, type_bateau):
    bateaux = []
    for ligne in range(grille.lignes):
        for colonne in range(grille.colonnes):
            for vertical in [False, True]:
                bateau = type_bateau(ligne, colonne, vertical)
                if grille.peut_ajouter(bateau):
                    bateaux.append(bateau)
    return bateaux


def créer_partie():
    grille = Grille(8, 10)
    affichage = Grille(8, 10)
    bateaux = []
    for type_bateau in [PorteAvion, Croiseur, Torpilleur, SousMarin]:
        possibilités = placements_possibles(grille, type_bateau)
        bateau = random.choice(possibilités)
        grille.ajoute(bateau)
        bateaux.append(bateau)
    return grille, affichage, bateaux


def tirer(grille, affichage, bateaux, ligne, colonne):
    if not grille.contient(ligne, colonne):
        return "Cette case n'est pas dans la grille"
    indice = ligne * grille.colonnes + colonne
    if grille.grille[indice] == "x":
        return "Tu as déjà tiré sur cette case"
    grille.tirer(ligne, colonne)
    for bateau in bateaux:
        if (ligne, colonne) in bateau.positions():
            affichage.tirer(ligne, colonne, "💣")
            if bateau.coulé(grille):
                for l, c in bateau.positions():
                    affichage.tirer(l, c, bateau.marque)
                return bateau.nom + " coulé "
            return "touché "
    affichage.tirer(ligne, colonne)
    return "À l'eau "


def terminé(grille, bateaux):
    for bateau in bateaux:
        if not bateau.coulé(grille):
            return False
    return True


def texte_grille(grille):
    texte = "    "
    for colonne in range(grille.colonnes):
        texte += str(colonne) + "  "
    for ligne in range(grille.lignes):
        texte += "\n" + str(ligne) + "   "
        for colonne in range(grille.colonnes):
            texte += grille.grille[ligne * grille.colonnes + colonne] + "  "
    return texte
