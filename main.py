import numpy as np

def creer_grille(taille=7):
    """Crée une grille de dimension (taille x taille) avec des zéros."""
    return np.zeros((taille, taille), dtype=int)

def afficher_grille(grille):
    """Affiche la grille."""
    for ligne in grille:
        print(' '.join(map(str, ligne)))

if __name__ == "__main__":
    grille = creer_grille()
    print("Grille initiale 7x7 :")
    afficher_grille(grille)
