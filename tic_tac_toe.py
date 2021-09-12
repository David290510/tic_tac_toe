from typing import List
import os


def change_elements(x: int, y: int, surface: List[List[str]], plaer_team: str) -> List[List[str]]:
    surface[x][y] = plaer_team
    return surface


def switch_player(player_team: str) -> str:
    '''
    >>> switch_player("X")
    'O'
    >>> switch_player("O")
    'X'
    '''
    if player_team == "X":
        return "O"
    return "X"


def generate_surface() -> List[List[str]]:
    return [["."] * 3 for _ in range(3)]


def show_surface(surface: List[List[str]]) -> None:
    for i in surface:
        print(" ".join(i))


def remind(player_team: str) -> None:
    if player_team == "X":
        print("Player X your turn!")
    else:
        print("Player O your turn!")


def check_winner_horizontal(player_team: str, surface: List[List[str]]) -> bool:
    for i in range(3):
        if surface[i] == [player_team] * 3:
            return True
    return False


def check_winner_vertical(player_team: str, surface: List[List[str]]) -> bool:
    for i in range(3):
        if [surface[j][i] for j in range(3)] == [player_team] * 3:
            return True
    return False


def check_winner_diagonal_waning(player_team: str, surface: List[List[str]]) -> bool:
    '''
    >>> check_winner_diagonal_waning("X", [["X", "O", "O"], [".", "X", "."], [".", ".", "X"]])
    True
    >>> check_winner_diagonal_waning("O", [["O", "X", "X"], [".", "O", "."], ["X", ".", "O"]])
    True
    >>> check_winner_diagonal_waning("X", [["X", "O", "O"], [".", ".", "."], [".", ".", "X"]])
    False
    '''
    count = 0
    for i in range(len(surface)):
        for j in range(len(surface[i])):
            if i == j and surface[i][j] == player_team:
                count += 1
            if count == 3:
                return True
    return False


def check_winner_diagonal_increase(player_team: str, surface: List[List[str]]) -> bool:
    '''
    >>> check_winner_diagonal_increase("X", [[".", ".", "X"], [".", "X", "O"], ["X", "O", "."]])
    True
    >>> check_winner_diagonal_increase("X", [[".", ".", "X"], ["X", "O", "O"], ["X", "O", "O"]])
    False
    '''
    if [surface[0][2], surface[1][1], surface[2][0]] == [player_team] * 3:
        return True
    return False


def fullness_field(surface: List[List[str]]) -> bool:
    '''
    >>> fullness_field([["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]])
    True
    >>> fullness_field([["X", ".", "X"], ["X", "O", "X"], ["X", "O", "X"]])
    False
    >>> fullness_field([[".", ".", "."], [".", ".", "."], [".", ".", "."]])
    False
    '''
    for i in range(3):
        if surface[i].count(".") > 0:
            return False
    return True


def check_winner_all(surface: List[List[str]]) -> str:
    '''
    >>> check_winner_all([["X", "X", "X"], [".", ".", "."], [".", ".", "."]])
    'X'
    >>> check_winner_all([[".", ".", "."], [".", ".", "."], [".", ".", "."]])
    ''
    '''
    for player_team in "XO":
        if check_winner_horizontal(player_team, surface) or check_winner_vertical(player_team, surface) or \
                check_winner_diagonal_waning(player_team, surface) or check_winner_diagonal_increase(player_team, surface):
            return player_team
    return ''


def checking_for_a_cell_for_players(surface: List[List[str]], x: int, y: int):
    '''
    >>> checking_for_a_cell_for_players([["X", ".", "."], ["X", ".", "."], ["X", ".", "."]], 0, 0)
    True
    >>> checking_for_a_cell_for_players([["X", ".", "."], ["X", ".", "."], ["X", ".", "."]], 1, 1)
    False
    '''
    if surface[x][y] == "X" or surface[x][y] == "O":
        return True
    else:
        return False


def clean():
    os.system('cls')


def checking_for_incorrect_input(x: int, y: int) -> bool:
    '''
    >>> checking_for_incorrect_input(10, 0)
    True
    >>> checking_for_incorrect_input(1, 1)
    False
    >>> checking_for_incorrect_input(0, 2)
    False
    '''
    if 0 < x > 2 or 0 < y > 2:
        return True
    return False


def save(surface: List[List[str]], player_team: str) -> None:
    save_file = open("save.txt", "w")
    for i in range(len(surface)):
        save_file.write(" ".join(surface[i]))
        save_file.write("\n")
    save_file.write(player_team)
    save_file.close()


def load():
    save_file = open("save.txt", "r")
    surface = [save_file.readline().split() for _ in range(3)]
    player_team = save_file.readline()
    return player_team, surface


def show(surface: List[List[str]], player_team: str) -> None:
    clean()
    show_surface(surface)
    remind(player_team)


def handle_command(command: str, surface: List[List[str]], player_team: str) -> str:
    """

    :param command:
    :param surface:
    :param player_team:
    :return: actual player_team for next turn
    """
    if command == "save":
        save(surface, player_team)
        return player_team
    if command == "load":
        player_team, surface[:] = load()
        return player_team
    x, y = map(int, command.split())
    while checking_for_incorrect_input(x, y) or checking_for_a_cell_for_players(surface, x, y):
        if checking_for_incorrect_input(x, y):
            print("Enter the correct coordinates !")
        else:
            print("the values of the already occupied cell are entered !")
            print("enter the correct value !")
        x, y = map(int, input(">> ").split())
    change_elements(x, y, surface, player_team)
    return switch_player(player_team)


def main():
    surface = generate_surface()
    player_team = "X"
    while not check_winner_all(surface) and not fullness_field(surface):
        show(surface, player_team)
        command = input(">> ")
        player_team = handle_command(command, surface, player_team)
    winner = check_winner_all(surface)
    show_surface(surface)
    if winner != '':
        print("Player", winner, " win !", sep=' ')
    else:
        print("Draw !")


if __name__ == "__main__":
    main()
