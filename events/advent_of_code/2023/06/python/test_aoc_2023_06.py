import pytest
from aoc_2023_06 import Paper, Race

RAW_PAPER = """
Time:      7  15   30
Distance:  9  40  200
"""


def test_can_parse_paper() -> None:
    assert Paper.from_text(RAW_PAPER) == Paper(
        races=[
            Race(time_allowed=7, record_distance=9),
            Race(time_allowed=15, record_distance=40),
            Race(time_allowed=30, record_distance=200),
        ],
    )


@pytest.mark.parametrize(
    ("race", "win_counts"),
    [
        (Race(time_allowed=7, record_distance=9), 4),
        (Race(time_allowed=15, record_distance=40), 8),
        (Race(time_allowed=30, record_distance=200), 9),
        (Race(time_allowed=71530, record_distance=940200), 71503),
    ],
)
def test_race_win_counts(race: Race, win_counts: int) -> None:
    assert race.count_possible_wins() == win_counts
