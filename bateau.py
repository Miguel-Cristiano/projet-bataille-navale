class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = "⛵"
        self.nom = "Bateau"

    def positions(self):
        positions = []
        for i in range(self.longueur):
            if self.vertical:
                positions.append((self.ligne + i, self.colonne))
            else:
                positions.append((self.ligne, self.colonne + i))
        return positions

    def chevauche(self, autre):
        for position in self.positions():
            if position in autre.positions():
                return True
        return False

    def coulé(self, grille):
        for ligne, colonne in self.positions():
            if not grille.contient(ligne, colonne):
                return False
            if grille.grille[ligne * grille.colonnes + colonne] != "x":
                return False
        return True


class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 4, vertical)
        self.marque = "🚢"
        self.nom = "Porte-avion"


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 3, vertical)
        self.marque = "⛴"
        self.nom = "Croiseur"


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
        self.marque = "🚣"
        self.nom = "Torpilleur"


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
        self.marque = "🐟"
        self.nom = "Sous-marin"
