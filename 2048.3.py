import os
import time
import random
import tools
# Recap de truc à faire : finir le systeme avec la liste available (supprimer les index disponibles à chaque mouvement)
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

#grid: list[list[str]] = \
#[
 #   ["","","",""],
 #   ["","","",""],
#    ["","","",""],
#    ["","","",""],
#]



def GetAvailableTiles(grid: list[list[str]]) -> list[tuple[int, int]]:
    available_tiles: list[tuple[int, int]] = []
    
    i: int = 0
    while i < len(grid):
        j: int = 0
        while j < len(grid[i]):
            if(grid[i][j] == ""):
                available_tiles.append((i, j))
            j = j + 1
        i = i + 1

    return available_tiles 


# available.remove(available_coordinate)

def SpawnTiles(grid, length, x, y) -> tuple[int, int, list[tuple[int,int]]]:
    available_tiles: list[tuple[int, int]] = GetAvailableTiles(grid)

    random_index = random.randint(0, len(available_tiles) - 1)

    i, j = available_tiles[random_index]

    dropRate: list[float] = [x, y]
    tiles: list[int] = [2, 4]
    randomTiles: float = random.random()
    if randomTiles <= dropRate[0]:
        grid[i][j] = tiles[0]
        return i, j, available_tiles
    else:
        grid[i][j] = tiles[1]
        return i, j, available_tiles

def MoveTiles(available_tiles: list[tuple[int,int]], grid: list[list[str]], input: str):
    available_tiles
    if input == "z":
        if available_tiles == []:
            print("ok")
            print(SpawnX, SpawnY)
            #grid[SpawnX][SpawnY] = [""]
        print(input)
    elif input == "q":
        print(input)
    elif input == "s":
        print(input)
    elif input == "d":
        print(input)


keyAllowed: list[str] = ["z", "q", "s", "d"]



def PlayGame():
    print("Taille de la grille : ")
    GRID_LENGTH: int = tools.ask_int()
    print("Proba pour 2")
    proba_2: float = tools.ask_proba()
    print("Proba pour 4")
    proba_4: float = tools.ask_proba()
    grid: list[list[str]] = GetGrid(GRID_LENGTH)

    while True:
        print("ahhhhhhh")
    #   available: list[tuple[int,int]] = AvailableGrid(grid)
        SpawnX, SpawnY, available_tiles = SpawnTiles(grid, GRID_LENGTH, proba_2, proba_4)
        i: int = 0
        while i < GRID_LENGTH:
            print(grid[i])
            i += 1
        print("Entrez une direction avec Z haut, Q gauche, S bas et D droite")
        key: str = tools.ask_input(keyAllowed)
        MoveTiles(available_tiles, grid, key)
            
        # time.sleep(2.0)
        # os.system('cls')

PlayGame()
