import pytest
from aoc_2015_01 import find_final_floor, find_when_santa_enters_basement


@pytest.mark.parametrize(
    ("text", "result"),
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_find_final_floor(text: str, result: int) -> None:
    assert find_final_floor(text) == result


@pytest.mark.parametrize(
    ("text", "result"),
    [
        (")", 1),
        ("()())", 5),
    ],
)
def test_find_when_santa_enters_basement(text: str, result: int) -> None:
    assert find_when_santa_enters_basement(text) == result
