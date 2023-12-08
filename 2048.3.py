# 2048 de Mathis Rota
import os
import time
import random
import tools

winningValue: int = 2048

COLOR_MAP = {
    0: "\033[48;2;205;193;180m",
    2: "\033[48;2;238;228;218m",
    4: "\033[48;2;237;224;200m",
    8: "\033[48;2;242;177;121m",
    16: "\033[48;2;245;149;99m",
    32: "\033[48;2;246;124;95m",
    64: "\033[48;2;246;94;59m",
    128: "\033[48;2;237;207;114m",
    256: "\033[48;2;237;204;97m",
    512: "\033[48;2;237;200;80m",
    1024: "\033[48;2;237;197;63m",
    2048: "\033[48;2;237;194;46m",
}

# Tableau invisible qui défini les coordonnées des cases (row, col) de la grille de jeu
def GetCoo(length: int) -> list[tuple[int, int]]:
    coordinates: list[tuple[int, int]] = []

    for row in range(length):
        for col in range(length):
            coordinates.append((row, col))

    return coordinates

# Génère une grille de jeu
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

# Spawn des tuiles
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
# Check  if Win
def won(grid) -> bool:
    for row in grid:
        for cell in row:
            if int(cell) == winningValue:
                return True
    return False

# Check if no moves
# 2048 de Mathis Rota
import os
import time
import random
import tools

winningValue: int = 2048

COLOR_MAP = {
    0: "\033[48;2;205;193;180m",
    2: "\033[48;2;238;228;218m",
    4: "\033[48;2;237;224;200m",
    8: "\033[48;2;242;177;121m",
    16: "\033[48;2;245;149;99m",
    32: "\033[48;2;246;124;95m",
    64: "\033[48;2;246;94;59m",
    128: "\033[48;2;237;207;114m",
    256: "\033[48;2;237;204;97m",
    512: "\033[48;2;237;200;80m",
    1024: "\033[48;2;237;197;63m",
    2048: "\033[48;2;237;194;46m",
}

# Tableau invisible qui défini les coordonnées des cases (row, col) de la grille de jeu
def GetCoo(length: int) -> list[tuple[int, int]]:
    coordinates: list[tuple[int, int]] = []

    for row in range(length):
        for col in range(length):
            coordinates.append((row, col))

    return coordinates

# Génère une grille de jeu
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

# Spawn des tuiles
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
# Check  if Win
def won(grid) -> bool:
    for row in grid:
        for cell in row:
            if int(cell) == winningValue:
                return True
    return False

# Check if no moves
def noMoves(grid) -> bool:
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '0':
                return False

            # Vérification des cases voisines pour les mouvements possibles
            if (col < len(grid[row]) - 1 and grid[row][col] == grid[row][col + 1]) or \
                    (col > 0 and grid[row][col] == grid[row][col - 1]) or \
                    (row < len(grid) - 1 and grid[row][col] == grid[row + 1][col]) or \
                    (row > 0 and grid[row][col] == grid[row - 1][col]):
                return False

    return True

# Initiation de la grille de jeu
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

# Refresh la grille
def refresh_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        for cell in row:
            cell_value = int(cell)
            color = COLOR_MAP.get(cell_value, "\033[0m")
            print(f"{color}{cell_value:<5}\033[0m", end=" ")
        print()


grid, proba, grid_length = Init()

# Avant la boucle principale, initialisation de merged_tiles
merged_tiles = GetGrid(grid_length)

#Code du Jeu
while True:
    key: str = tools.AskInput()
    if key == "Z": # HAUT
        for col in range(len(grid[0])):
            for row in range(1, len(grid)): # Lis tout les lignes et colonne
                if grid[row][col] != '0': # Si la case n'est pas vide (Prend tout les tuiles != de 0)
                    new_row = row - 1 # On déplace la case vers le haut
                    while new_row >= 0: # Tant qu'on ne dépasse pas la grille
                        if grid[new_row][col] == '0': # Si la case est vide
                            grid[new_row][col] = grid[new_row + 1][col] # Déplace une case vers le haut en affectant la valeur de la case actuelle à la case au-dessus d'elle.
                            grid[new_row + 1][col] = '0' # La case redevien vide apres le déplacement vers le haut  
                            new_row -= 1 # On déplace la case vers le haut
                        elif grid[new_row][col] == grid[new_row + 1][col]: # Si la case potentielle est égale à la case au-dessus d'elle
                            merged_value = int(grid[new_row][col]) + int(grid[new_row + 1][col]) # On additionne les valeurs des cases
                            grid[new_row][col] = str(merged_value) # On affecte la valeur additionnée à la case potentielle
                            grid[new_row + 1][col] = '0' # La case redevien vide apres le déplacement vers le haut
                            merged_tiles[new_row][col] = True # Marquer la tuile comme fusionnée
                            break # On sort de la boucle
                        else:
                            break

# Logique similaire pour les 3 autres touches

    elif key == "S": # BAS
        for col in range(len(grid[0])):
            for row in range(len(grid) - 2, -1, -1):
                if grid[row][col] != '0':
                    new_row = row + 1
                    while new_row < len(grid):
                        if grid[new_row][col] == '0':
                            grid[new_row][col] = grid[new_row - 1][col]
                            grid[new_row - 1][col] = '0'
                            new_row += 1
                        elif grid[new_row][col] == grid[new_row - 1][col]:
                            merged_value = int(grid[new_row][col]) + int(grid[new_row - 1][col])
                            grid[new_row][col] = str(merged_value)
                            grid[new_row - 1][col] = '0'
                            merged_tiles[new_row][col] = True
                            break
                        else:
                            break



    elif key == "Q":  # GAUCHE
        for row in range(len(grid)):
            for col in range(1, len(grid[row])):
                if grid[row][col] != '0':
                    new_col = col - 1
                    while new_col >= 0:
                        if grid[row][new_col] == '0':
                            grid[row][new_col] = grid[row][new_col + 1]
                            grid[row][new_col + 1] = '0'
                            new_col -= 1
                        elif grid[row][new_col] == grid[row][new_col + 1]:
                            merged_value = int(grid[row][new_col]) + int(grid[row][new_col + 1])
                            grid[row][new_col] = str(merged_value)
                            grid[row][new_col + 1] = '0'
                            merged_tiles[row][new_col] = True
                            break
                        else:
                            break


    elif key == "D":  # DROITE
        for row in range(len(grid)):
            for col in range(len(grid[row]) - 2, -1, -1):
                if grid[row][col] != '0':
                    new_col = col + 1
                    while new_col < len(grid[row]):
                        if grid[row][new_col] == '0':
                            grid[row][new_col] = grid[row][new_col - 1]
                            grid[row][new_col - 1] = '0'
                            new_col += 1
                        elif grid[row][new_col] == grid[row][new_col - 1]:
                            merged_value = int(grid[row][new_col]) + int(grid[row][new_col - 1])
                            grid[row][new_col] = str(merged_value)
                            grid[row][new_col - 1] = '0'
                            merged_tiles[row][new_col] = True
                            break
                        else:
                            break


    if noMoves(grid):
        refresh_grid(grid)
        print("Perdu!")
        break
        
    if won(grid):
        refresh_grid(grid)
        print("Gagné!")
        break

    RandomSpawn(grid, grid_length ,proba)
    
    refresh_grid(grid)





# Initiation de la grille de jeu
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

# Refresh la grille
def refresh_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        for cell in row:
            cell_value = int(cell)
            color = COLOR_MAP.get(cell_value, "\033[0m")
            print(f"{color}{cell_value:<5}\033[0m", end=" ")
        print()


grid, proba, grid_length = Init()

# Avant la boucle principale, initialisation de merged_tiles
merged_tiles = GetGrid(grid_length)

#Code du Jeu
while True:
    key: str = tools.AskInput()
    if key == "Z": # HAUT
        for col in range(len(grid[0])):
            for row in range(1, len(grid)): # Lis tout les lignes et colonne
                if grid[row][col] != '0': # Si la case n'est pas vide (Prend tout les tuiles != de 0)
                    new_row = row - 1 # On déplace la case vers le haut
                    while new_row >= 0: # Tant qu'on ne dépasse pas la grille
                        if grid[new_row][col] == '0': # Si la case est vide
                            grid[new_row][col] = grid[new_row + 1][col] # Déplace une case vers le haut en affectant la valeur de la case actuelle à la case au-dessus d'elle.
                            grid[new_row + 1][col] = '0' # La case redevien vide apres le déplacement vers le haut  
                            new_row -= 1 # On déplace la case vers le haut
                        elif grid[new_row][col] == grid[new_row + 1][col]: # Si la case potentielle est égale à la case au-dessus d'elle
                            merged_value = int(grid[new_row][col]) + int(grid[new_row + 1][col]) # On additionne les valeurs des cases
                            grid[new_row][col] = str(merged_value) # On affecte la valeur additionnée à la case potentielle
                            grid[new_row + 1][col] = '0' # La case redevien vide apres le déplacement vers le haut
                            merged_tiles[new_row][col] = True # Marquer la tuile comme fusionnée
                            break # On sort de la boucle
                        else:
                            break

# Logique similaire pour les 3 autres touches

    elif key == "S": # BAS
        for col in range(len(grid[0])):
            for row in range(len(grid) - 2, -1, -1):
                if grid[row][col] != '0':
                    new_row = row + 1
                    while new_row < len(grid):
                        if grid[new_row][col] == '0':
                            grid[new_row][col] = grid[new_row - 1][col]
                            grid[new_row - 1][col] = '0'
                            new_row += 1
                        elif grid[new_row][col] == grid[new_row - 1][col]:
                            merged_value = int(grid[new_row][col]) + int(grid[new_row - 1][col])
                            grid[new_row][col] = str(merged_value)
                            grid[new_row - 1][col] = '0'
                            merged_tiles[new_row][col] = True
                            break
                        else:
                            break



    elif key == "Q":  # GAUCHE
        for row in range(len(grid)):
            for col in range(1, len(grid[row])):
                if grid[row][col] != '0':
                    new_col = col - 1
                    while new_col >= 0:
                        if grid[row][new_col] == '0':
                            grid[row][new_col] = grid[row][new_col + 1]
                            grid[row][new_col + 1] = '0'
                            new_col -= 1
                        elif grid[row][new_col] == grid[row][new_col + 1]:
                            merged_value = int(grid[row][new_col]) + int(grid[row][new_col + 1])
                            grid[row][new_col] = str(merged_value)
                            grid[row][new_col + 1] = '0'
                            merged_tiles[row][new_col] = True
                            break
                        else:
                            break


    elif key == "D":  # DROITE
        for row in range(len(grid)):
            for col in range(len(grid[row]) - 2, -1, -1):
                if grid[row][col] != '0':
                    new_col = col + 1
                    while new_col < len(grid[row]):
                        if grid[row][new_col] == '0':
                            grid[row][new_col] = grid[row][new_col - 1]
                            grid[row][new_col - 1] = '0'
                            new_col += 1
                        elif grid[row][new_col] == grid[row][new_col - 1]:
                            merged_value = int(grid[row][new_col]) + int(grid[row][new_col - 1])
                            grid[row][new_col] = str(merged_value)
                            grid[row][new_col - 1] = '0'
                            merged_tiles[row][new_col] = True
                            break
                        else:
                            break


    if noMoves(grid):
        refresh_grid(grid)
        print("Perdu!")
        break
        
    if won(grid):
        refresh_grid(grid)
        print("Gagné!")
        break

    RandomSpawn(grid, grid_length ,proba)
    
    refresh_grid(grid)



