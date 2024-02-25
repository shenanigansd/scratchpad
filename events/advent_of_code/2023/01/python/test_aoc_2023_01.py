import pytest
from aoc_2023_01 import find_first_and_last_number_in_text


@pytest.mark.parametrize(
    ("text", "first", "last", "text_contains_spelled_words"),
    [
        # part 1
        ("1abc2", 1, 2, False),
        ("pqr3stu8vwx", 3, 8, False),
        ("a1b2c3d4e5f", 1, 5, False),
        ("treb7uchet", 7, 7, False),
        # part 2
        ("two1nine", 2, 9, True),
        ("eightwothree", 8, 3, True),
        ("abcone2threexyz", 1, 3, True),
        ("xtwone3four", 2, 4, True),
        ("4nineeightseven2", 4, 2, True),
        ("zoneight234", 1, 4, True),
        ("7pqrstsixteen", 7, 6, True),
    ],
)
def test_find_numbers_in_text(
    text: str,
    first: int,
    last: int,
    text_contains_spelled_words: bool,  # noqa: FBT001
) -> None:
    assert find_first_and_last_number_in_text(text, text_contains_spelled_words) == (
        first,
        last,
    )
