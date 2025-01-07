import numpy as np

frame = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]])

def compute_number_neighbors(paded_frame, index_line, index_column):
    """
    Cette fonction prend en entrée la matrice avec bordure et
    renvoie le nombre de cellules voisines vivantes.
    """
    return np.sum(paded_frame[index_line-1:index_line+2, index_column-1:index_column+2]) - paded_frame[index_line, index_column]

def compute_next_frame(frame):
    """
    Cette fonction prend en entrée une frame et calcule la frame suivante
    à partir des règles du jeu de la vie
    """
    paded_frame = np.pad(frame, 1, mode="constant")
    new_frame = frame.copy()

    for i in range(1, paded_frame.shape[0] - 1):
        for j in range(1, paded_frame.shape[1] - 1):
            num_neighbors = compute_number_neighbors(paded_frame, i, j)
            if paded_frame[i, j] == 1:
                if num_neighbors < 2 or num_neighbors > 3:
                    new_frame[i-1, j-1] = 0  # Meurt
            else:
                if num_neighbors == 3:
                    new_frame[i-1, j-1] = 1  # Prend vie

    return new_frame

iterations = 10  # Nombre de frames à afficher
for _ in range(iterations):
    print("\nFrame suivante :")
    for line in frame:
        print(' '.join(map(str, line)))
    frame = compute_next_frame(frame)
