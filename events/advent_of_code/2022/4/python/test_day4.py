import pytest

from script_day4 import _contains_any, _overlaps, _range_parser


@pytest.mark.parametrize(
    "value,result",
    [
        ("2-4,6-8", False),
        ("2-3,4-5", False),
        ("5-7,7-9", False),
        ("2-8,3-7", True),
        ("6-6,4-6", True),
        ("2-6,4-8", False),
    ],
)
def test_part_one(value: str, result: bool):
    first, second = value.split(",")
    first, second = set(_range_parser(first)), set(_range_parser(second))
    assert _overlaps(first, second) == result


@pytest.mark.parametrize(
    "value,result",
    [
        ("2-4,6-8", False),
        ("2-3,4-5", False),
        ("5-7,7-9", True),
        ("2-8,3-7", True),
        ("6-6,4-6", True),
        ("2-6,4-8", True),
    ],
)
def test_part_two(value: str, result: bool):
    first, second = value.split(",")
    first, second = set(_range_parser(first)), set(_range_parser(second))
    assert _contains_any(first, second) == result
