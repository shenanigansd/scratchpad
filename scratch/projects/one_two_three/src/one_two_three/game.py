from random import choice

GAME_OPTIONS = dict[str, set[str]]


def check_win(user_selection: str, computer_selection: str, options: GAME_OPTIONS) -> bool:
    return computer_selection in options[user_selection]
