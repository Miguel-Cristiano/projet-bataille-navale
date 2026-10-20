from bateau import Torpilleur
from grille import Grille


if __name__ == "__main__":
    grille = Grille(3, 5)
    bateau = Torpilleur(1, 1)
    grille.ajoute(bateau)
    print("Bateau placé :")
    print(grille)
    grille.tirer(1, 1)
    print("Après le premier tir :")
    print(grille)
    print("Coulé :", bateau.coulé(grille))
    grille.tirer(1, 2)
    print("Après le deuxième tir :")
    print(grille)
    print("Coulé :", bateau.coulé(grille))
