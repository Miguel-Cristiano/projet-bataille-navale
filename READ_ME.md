Projet bataille navale

Le but est de trouver et de couler quatre bateaux sur une grille de 8 lignes et 10 colonnes. Les bateaux sont placés au hasard sans se chevaucher.

Les fichiers :

- grille.py contient la classe Grille.
- bateau.py contient la classe Bateau et les quatre types de bateaux.
- fonctions.py contient les fonctions utilisées par le jeu.
- main.py permet de jouer.
- story_grille.py et story_bateau.py reprennent les deux user stories du cours.
- main_fonctionnalité.py montre un exemple de bateau touché puis coulé.
- test_grille.py, test_bateau.py et test_fonctions.py contiennent les tests.
- UML.md contient les diagrammes des classes.

Pour lancer le projet depuis le dossier projet-bataille-navale :

python main.py

On entre une ligne de 0 à 7, puis une colonne de 0 à 9. Une bombe indique un bateau touché. Quand il est coulé, sa marque apparaît sur la grille. À la fin, le programme affiche le nombre de coups joués.

Pour lancer les tests depuis le même dossier :

python -m pytest
