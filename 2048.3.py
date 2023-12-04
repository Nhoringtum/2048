import os
import time
import random
import tools
import numpy


def GetGrid(length: int) -> list[list[str]]:
    grille: list[list[str]] = []
    i: int = 0
    while i < length:
        line: list[str] = []
        j: int = 0
        while j < length:
            line.append("")
            j += 1

        grille.append(line)
        i += 1

    return grille

def SpawnTiles(grid, length):
    dropRate: list[float] = [0.9, 0.1]
    tiles: list[int] = [2, 4]
    randomTiles: float = random.random()
    randomX: int = random.randint(0, length-1)
    randomY: int = random.randint(0, length-1)
    if randomTiles <= dropRate[0]:
        grid[randomX][randomY] = tiles[0]
    else:
        grid[randomX][randomY] = tiles[1]

GRID_LENGTH: int = tools.ask_int()
grid: list[list[str]] = GetGrid(GRID_LENGTH)
SpawnTiles(grid, GRID_LENGTH)


i: int = 0
while i < GRID_LENGTH:
    print(grid[i])
    i += 1

time.sleep(2.0)
os.system('cls')