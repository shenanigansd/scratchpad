from script_day02 import Action, _get_score


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
