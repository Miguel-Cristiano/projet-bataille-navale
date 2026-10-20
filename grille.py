class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.vide = "∿"
        self.grille = [self.vide] * (lignes * colonnes)

    def contient(self, ligne, colonne):
        return 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes

    def tirer(self, ligne, colonne, touche="x"):
        if not self.contient(ligne, colonne):
            return False
        self.grille[ligne * self.colonnes + colonne] = touche
        return True

    def __str__(self):
        texte = ""
        for ligne in range(self.lignes):
            for colonne in range(self.colonnes):
                texte += self.grille[ligne * self.colonnes + colonne]
            if ligne < self.lignes - 1:
                texte += "\n"
        return texte

    def peut_ajouter(self, bateau):
        for ligne, colonne in bateau.positions():
            if not self.contient(ligne, colonne):
                return False
            if self.grille[ligne * self.colonnes + colonne] != self.vide:
                return False
        return True

    def ajoute(self, bateau):
        if not self.peut_ajouter(bateau):
            return False
        for ligne, colonne in bateau.positions():
            self.grille[ligne * self.colonnes + colonne] = bateau.marque
        return True
