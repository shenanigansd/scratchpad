from enum import IntEnum


class Action(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


victories: dict[Action, Action] = {
    Action.Scissors: Action.Paper,
    Action.Paper: Action.Rock,
    Action.Rock: Action.Scissors,
}

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
    return sum(_get_score(*actions) for actions in values)


def part_two(values: list[tuple[Action, str]]) -> int:
    score = 0
    for opponent_action, needed_result in values:
        if needed_result == "X":
            user_action=victories[opponent_action]
        elif needed_result == "y":
            pass
        elif needed_result == "Z":
            user_action=victories[opponent_action]
    return score


if __name__ == '__main__':
    with open("../../../input.txt") as file:
        part_one_values: list[tuple[Action, Action]] = []
        part_two_values: list[tuple[Action, str]] = []
        for line in file.readlines():
            action_one, action_two = line.split()
            part_one_values.append((input_keys[action_two], input_keys[action_one]))
            part_two_values.append((input_keys[action_one], action_two))
    print(part_one(values=part_one_values))
    print(part_two(values=part_two_values))


def test_get_score():
    assert _get_score(Action.Rock, Action.Rock) == 4
    assert _get_score(Action.Rock, Action.Paper) == 1
    assert _get_score(Action.Rock, Action.Scissors) == 7

    assert _get_score(Action.Paper, Action.Rock) == 8
    assert _get_score(Action.Paper, Action.Paper) == 5
    assert _get_score(Action.Paper, Action.Scissors) == 2

    assert _get_score(Action.Scissors, Action.Rock) == 3
    assert _get_score(Action.Scissors, Action.Paper) == 9
    assert _get_score(Action.Scissors, Action.Scissors) == 6
