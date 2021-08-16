from typing import List


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


def check_winner_all(player_team: str, surface: List[List[str]]) -> bool:
    '''
    >>> check_winner_all("X", [["X", "X", "X"], [".", ".", "."], [".", ".", "."]])
    True
    >>> check_winner_all("X", [[".", ".", "."], [".", ".", "."], [".", ".", "."]])
    False
    '''
    if check_winner_horizontal(player_team, surface) or check_winner_vertical(player_team, surface) or \
            check_winner_diagonal_waning(player_team, surface) or check_winner_diagonal_increase(player_team, surface):
        return True
    return False


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


def main():
    surface = generate_surface()
    player_team = "X"
    while not check_winner_all(player_team, surface) and not fullness_field(surface):
        show_surface(surface)
        print(1)
        remind(player_team)
        x, y = map(int, input(">> "))
        if not checking_for_a_cell_for_players(surface, x, y):
            change_elements(x, y, surface, player_team)
            if not check_winner_all(player_team, surface):
                player_team = switch_player(player_team)
            else:
                print("Player", player_team, " win !", sep=' ')
        else:
            while checking_for_a_cell_for_players(surface, x, y):
                print("the values of the already occupied cell are entered !")
                print("enter the correct value !")
                x, y = map(int, input(">> "))
                if not checking_for_a_cell_for_players(surface, x, y):
                    change_elements(x, y, surface, player_team)
                    show_surface(surface)
                    player_team = switch_player(player_team)
    if fullness_field(surface):
        print("Draw !")


if __name__ == "__main__":
    main()

