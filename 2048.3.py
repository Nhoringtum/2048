import os
import time
import random
import tools
# Recap de truc à faire : finir le systeme avec la liste available (la créer selon la taille du tableau, supprimer les index disponibles à chaque spawn et chaque mouvement)
# faire en sorte de décaler les tuiles dans la direction demandé du joueur mais en prenant en compte si l'index existe. Puis prog la fusion des tuiles (se passe avant le décalage)
def GetGrid(length: int) -> list[list[str]]:
    grid: list[list[str]] = []
    i: int = 0
    while i < length:
        line: list[str] = []
        j: int = 0
        while j < length:
            line.append("")
            j += 1

        grid.append(line)
        i += 1

    return grid


# available: list[tuple[int, int]]

# [
#    (0,0),
#    (0,1),
#    (0,2),
#    (3,3),
# ]

# available_index: int = random.randint(0,3)

# available_coordinate: tuple[int, int] = available[available_index]

# del available[available_index]

# available.remove(available_coordinate)

def SpawnTiles(grid, length, x, y):
    dropRate: list[float] = [x, y]
    tiles: list[int] = [2, 4]
    randomTiles: float = random.random()
    randomX: int = random.randint(0, length - 1)
    randomY: int = random.randint(0, length - 1)
    if randomTiles <= dropRate[0]:
        grid[randomX][randomY] = tiles[0]
    else:
        grid[randomX][randomY] = tiles[1]


keyAllowed: list[str] = ["z", "q", "s", "d"]


print("Taille de la grille : ")
GRID_LENGTH: int = tools.ask_int()
print("Proba pour 2")
proba_2: float = tools.ask_proba()
print("Proba pour 4")
proba_4: float = tools.ask_proba()
while True:
    grid: list[list[str]] = GetGrid(GRID_LENGTH)
    SpawnTiles(grid, GRID_LENGTH, proba_2, proba_4)
    i: int = 0
    while i < GRID_LENGTH:
        print(grid[i])
        i += 1
    print("Entrez une direction avec Z haut, Q gauche, S bas et D droite")
    key: str = tools.ask_input(keyAllowed)
    print(keyAllowed)
    print(key)
    if key == "Z":
        print(key)
    # time.sleep(2.0)
    # os.system('cls')
