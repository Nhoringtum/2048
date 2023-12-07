import random
import copy
import os
import tools

Authorized_answer: list[str] = ["z", "q", "s", "d"]
winningValue: int = 2048

# Fonction pour afficher le tableau de jeu
def displayBoard():
    # Partie grâce à laquelle on pourra plus bas moduler la taille d'affichage du tableau en fonction de la taille des
    # nombres
    largest: int = board[0][0]
    element: int
    for row in board:
        for element in row:
            if element > largest:
                largest = element

    numSpaces: int = len(str(largest))

    # Affichage du tableau
    for row in board:
        currentRow: str = "|"
        for element in row:
            if element == 0:
                currentRow += " " * numSpaces + "|"
            else:
                currentRow += (" " * (numSpaces - len(str(element)))) + str(element) + "|"

        print(currentRow)
    print()


# Fonction pour fusionner une ligne vers la gauche
def mergeOneRowL(row) -> list[int]:
    j: int
    i: int
    for j in range(boardSize - 1):
        for i in range(boardSize - 1, 0, -1):
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0

    for i in range(boardSize - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0

    for i in range(boardSize - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row


# Fonction pour fusionner le tableau vers la gauche
def mergeLeft(currentBoard) -> list[[int]]:
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])

    return currentBoard


# Fonction pour inverser une ligne
def reverse(row) -> list[int]:
    new: list = []
    for i in range(boardSize - 1, -1, -1):
        new.append(row[i])
    return new


# Fonction pour fusionner le tableau vers la droite
def mergeRight(currentBoard) -> list[[int]]:
    for i in range(boardSize):
        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])

    return currentBoard


# Fonction pour transposer le tableau
def transpose(currentBoard) -> list[[int]]:
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp: tuple[int, int] = currentBoard[j][i]
                currentBoard[j][i] = currentBoard[i][j]
                currentBoard[i][j] = temp
    return currentBoard


# Fonction pour fusionner le tableau vers le haut
def mergeUp(currentBoard) -> list[[int]]:
    currentBoard = transpose(currentBoard)
    currentBoard = mergeLeft(currentBoard)
    currentBoard = transpose(currentBoard)

    return currentBoard


# Fonction pour fusionner le tableau vers le bas
def mergeDown(currentBoard) -> list[[int]]:
    currentBoard = transpose(currentBoard)
    currentBoard = mergeRight(currentBoard)
    currentBoard = transpose(currentBoard)

    return currentBoard


# Fonction pour choisir une nouvelle valeur (2 ou 4)
def pickNewValue() -> int:
    if random.randint(1, 8) == 1:
        return 4
    else:
        return 2


# Fonction pour ajouter une nouvelle valeur au tableau
def addNewValue():
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)

    while not board[rowNum][colNum] == 0:
        rowNum = random.randint(0, boardSize - 1)
        colNum = random.randint(0, boardSize - 1)

    board[rowNum][colNum] = pickNewValue()


# Fonction pour vérifier si le joueur a gagné
def won() -> bool:
    for row in board:
        if winningValue in row:
            return True
    return False


# Fonction pour vérifier s'il n'y a plus de mouvements possibles
def noMoves() -> bool:
    tempBoard1: list[list[int]] = copy.deepcopy(board)
    tempBoard2: list[list[int]] = copy.deepcopy(board)

    tempBoard1 = mergeDown(tempBoard1)
    if tempBoard1 == tempBoard2:
        tempBoard1 = mergeUp(tempBoard1)
        if tempBoard1 == tempBoard2:
            tempBoard1 = mergeLeft(tempBoard1)
            if tempBoard1 == tempBoard2:
                tempBoard1 = mergeRight(tempBoard1)
                if tempBoard1 == tempBoard2:
                    return True
    return False

print("Bienvenue au jeu 2048, le but est d'atteindre une tuile de 2048. Pour ce faire, vous devez fusionner les tuiles en les bougeant de chaques côtés. Elles verront leur valeur doubler. Attention 1 tuile apparait à chaque coup. Bon jeu !")

# Taille du tableau
boardSize: int = tools.ask_int()

# Initialisation du tableau
board: list[list[int]] = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    board.append(row)

# Placement de deux valeurs aléatoires au début du jeu
numNeeded: int = 2
while numNeeded > 0:
    rowNum: int = random.randint(0, boardSize - 1)
    colNum: int = random.randint(0, boardSize - 1)

    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = pickNewValue()
        numNeeded -= 1

# Affichage du tableau initial
displayBoard()

# Variable pour indiquer si le jeu est terminé
gameOver: bool = False

# Boucle principale du jeu
while not gameOver:

    # Demande du mouvement au joueur
    print("Z pour haut, Q pour gauche, S pour bas, D pour droite : ")
    move: str = tools.ask_input(Authorized_answer)

    # Validation du mouvement
    validInput: bool = True

    # Création d'une copie temporaire du tableau
    tempBoard: list[list[int]] = copy.deepcopy(board)

    # Mouvement joueur
    if move == "z":
        board = mergeUp(board)
    elif move == "q":
        board = mergeLeft(board)
    elif move == "s":
        board = mergeDown(board)
    elif move == "d":
        board = mergeRight(board)
    else:
        validInput = False

    # Gestion du cas d'entrée invalide
    if not validInput:
        print("Vous avez entré une commande erronnée, veuillez recommencer")
    else:
        # Vérification des changements dans le tableau
        if board == tempBoard:
            print("Aucun coups valables dans cette direction")
        else:
            # Effacement de l'écran (Windows seulement, ajustez pour d'autres systèmes)
            os.system('cls')
            # Vérification de la victoire
            if won():
                displayBoard()
                print("Gagné")
                gameOver = True
            else:
                # Ajout d'une nouvelle valeur et affichage du tableau
                addNewValue()
                displayBoard()
                # Vérification s'il n'y a plus de mouvements possibles
                if noMoves():
                    print("perdu, plus de mouvements")
                    gameOver = True
