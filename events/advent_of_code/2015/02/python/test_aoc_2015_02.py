import pytest
from aoc_2015_02 import part_one, part_two


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
def test_part_one(text: str, result: int) -> None:
    assert part_one(text) == result


@pytest.mark.parametrize(
    ("text", "result"),
    [
        (")", 1),
        ("()())", 5),
    ],
)
def test_part_two(text: str, result: int) -> None:
    assert part_two(text) == result
