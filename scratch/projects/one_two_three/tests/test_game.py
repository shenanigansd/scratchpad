from one_two_three.game import check_win

SAMPLE_DATA = {
    "rock": {"scissors"},
    "paper": {"rock"},
    "scissors": {"paper"},
}


def test_it() -> None:
    assert check_win("rock", "scissors", SAMPLE_DATA) is True
    assert check_win("scissors", "rock", SAMPLE_DATA) is False
