from grille import Grille
from fonctions import texte_grille


if __name__ == "__main__":
    grille = Grille(5, 8)
    while True:
        print(texte_grille(grille))
        ligne = int(input("Ligne : "))
        colonne = int(input("Colonne : "))
        grille.tirer(ligne, colonne)
