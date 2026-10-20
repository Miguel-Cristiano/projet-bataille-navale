from bateau import Bateau


if __name__ == "__main__":
    b1 = Bateau(2, 3, longueur=3)
    b2 = Bateau(1, 4, longueur=3, vertical=True)
    b3 = Bateau(0, 0, longueur=2)

    print("Bateau 1 :", b1.positions())
    print("Bateau 2 :", b2.positions())
    print("Chevauchement attendu : True. Résultat :", b1.chevauche(b2))
    print("Bateau 3 :", b3.positions())
    print("Chevauchement attendu : False. Résultat :", b1.chevauche(b3))
