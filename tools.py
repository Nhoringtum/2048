PlayKey = ["Z", "Q", "S", "D"]

def ask_int() -> int:
    while True:
        value: str = input("Taille de la grille (Original = 4x4) : ")

        if value.isdigit():
            return int(value)

        print("pas un nombre")

def ask_proba() -> int:
    while True:
        value: str = input("Probabilité d'un spawn de 4 (0 - 10) (Original = 1): ")

        if value.isdigit():
            value_int = int(value)
            if 0 <= value_int <= 10:
                return value_int

        print("Erreur: Veuillez entrer un nombre entre 0 et 10.")

def AskInput() -> str:
    while True:
        value: str = input("Jouer (Z Q S D) = ")

        if value in PlayKey:
            return str(value)

        print("Veuillez rentré Z Q S D")

