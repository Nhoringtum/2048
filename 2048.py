import os
import time
import random
import tools

def GetCoo(length: int) -> list[tuple[int, int]]:
    coordinates: list[tuple[int, int]] = []

    for row in range(length):
        for col in range(length):
            coordinates.append((row, col))

    return coordinates

def GetGrid(length: int) -> list[list[str]]:
    grid: list[list[str]] = []
    i: int = 0
    while i < length:
        line: list[str] = []
        j: int = 0
        while j < length:
            line.append("0")
            j += 1

        grid.append(line)
        i += 1

    return grid

def RandomSpawn(grid: list[list[str]], GRID_LENGTH: int, PROBA: int):


    while True:
        row = random.randint(0, GRID_LENGTH - 1)
        col = random.randint(0, GRID_LENGTH - 1)
        
        if grid[row][col] == "0":
            n = random.randint(0, 10)
            if n < PROBA:
                n = "4"
            else:
                n = "2"      
            grid[row][col] = n
            break

def Init() -> tuple:
    GRID_LENGTH: int = tools.ask_int()
    PROBA: int = tools.ask_proba()
    grid: list[list[str]] = GetGrid(GRID_LENGTH)
    coordinate: list[tuple[int, int]] = GetCoo(GRID_LENGTH)

    for i in range(GRID_LENGTH):
        print(grid[i])

    for _ in range(2):
        RandomSpawn(grid, GRID_LENGTH, PROBA)

    time.sleep(2.0)
    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(GRID_LENGTH):
        print(grid[i])


    return grid, PROBA, GRID_LENGTH

grid, proba, grid_length = Init()

def refresh_grid(grid):
    for row in grid:
        print(" ".join(row))

while True:
    key: str = tools.AskInput()
    if key == "Z": # HAUT
        for col in range(len(grid[0])):
            for row in range(1, len(grid)):
                if grid[row][col] != '0':
                    new_row = row - 1
                    while new_row >= 0 and grid[new_row][col] == '0':
                        new_row -= 1
                    new_row += 1
                    if new_row != row:
                        grid[new_row][col] = grid[row][col]
                        grid[row][col] = '0'

    elif key == "S": # BAS
        for col in range(len(grid[0])):
            for row in range(len(grid) - 2, -1, -1):
                if grid[row][col] != '0':
                    new_row = row + 1
                    while new_row < len(grid) and grid[new_row][col] == '0':
                        new_row += 1
                    new_row -= 1
                    if new_row != row:
                        grid[new_row][col] = grid[row][col]
                        grid[row][col] = '0'

    if key == "Q": # GAUCHE
        for row in range(len(grid)):
            for col in range(1, len(grid[row])):
                if grid[row][col] != '0':
                    new_col = col - 1
                    while new_col >= 0 and grid[row][new_col] == '0':
                        new_col -= 1
                    new_col += 1
                    if new_col != col:
                        grid[row][new_col] = grid[row][col]
                        grid[row][col] = '0'

    elif key == "D": # DROITE
        for row in range(len(grid)):
            for col in range(len(grid[row]) - 2, -1, -1):
                if grid[row][col] != '0':
                    new_col = col + 1
                    while new_col < len(grid[row]) and grid[row][new_col] == '0':
                        new_col += 1
                    new_col -= 1
                    if new_col != col:
                        grid[row][new_col] = grid[row][col]
                        grid[row][col] = '0'
    refresh_grid(grid)



