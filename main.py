from fonctions import créer_partie, texte_grille, tirer, terminé


if __name__ == "__main__":
    grille, affichage, bateaux = créer_partie()
    coups = 0
    print("Bataille navale : trouve les quatre bateaux !")
    print("Lignes de 0 à 7, colonnes de 0 à 9.")
    print(texte_grille(affichage))

    while not terminé(grille, bateaux):
        ligne = int(input("Ligne : "))
        colonne = int(input("Colonne : "))
        if grille.contient(ligne, colonne):
            indice = ligne * grille.colonnes + colonne
            if grille.grille[indice] != "x":
                coups += 1
        print(tirer(grille, affichage, bateaux, ligne, colonne))
        print(texte_grille(affichage))

    print("Tous les bateaux sont coulés en", coups, "coups !")
