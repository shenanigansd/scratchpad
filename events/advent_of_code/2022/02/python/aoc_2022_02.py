from enum import IntEnum
from itertools import starmap


class Action(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


victories: dict[Action, Action] = {
    Action.Scissors: Action.Paper,
    Action.Paper: Action.Rock,
    Action.Rock: Action.Scissors,
}

opponent_victories = {value: key for key, value in victories.items()}

input_keys: dict[str, Action] = {
    "A": Action.Rock,
    "B": Action.Paper,
    "C": Action.Scissors,
    "X": Action.Rock,
    "Y": Action.Paper,
    "Z": Action.Scissors,
}


def _get_score(user_action: Action, computer_action: Action) -> int:
    score = int(user_action)

    if computer_action == victories[user_action]:
        score += 6
    elif user_action == computer_action:
        score += 3

    return score


def part_one(values: list[tuple[Action, Action]]) -> int:
    return sum(starmap(_get_score, values))


def part_two(values: list[tuple[Action, str]]) -> int:
    score = 0
    for opponent_action, needed_result in values:
        if needed_result == "X":
            user_action = victories[opponent_action]
        elif needed_result == "Y":
            user_action = opponent_action
        elif needed_result == "Z":
            user_action = opponent_victories[opponent_action]
        else:
            msg = f"{needed_result=}"
            raise ValueError(msg)
        score += _get_score(user_action, opponent_action)
    return score


if __name__ == "__main__":
    with open("../input.txt", encoding="locale") as file:
        part_one_values: list[tuple[Action, Action]] = []
        part_two_values: list[tuple[Action, str]] = []
        for line in file:
            action_one, action_two = line.split()
            part_one_values.append((input_keys[action_two], input_keys[action_one]))
            part_two_values.append((input_keys[action_one], action_two))
    print(part_one(values=part_one_values))
    print(part_two(values=part_two_values))
