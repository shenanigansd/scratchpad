import pytest
from aoc_2024_01 import parse_input, part1, part2

TEST_INPUT = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

def test_parse_input() -> None:
    assert parse_input(TEST_INPUT) == ([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9])

def test_part1() -> None:
    assert part1(*parse_input(TEST_INPUT)) == 11

def test_part2() -> None:
    assert part2(*parse_input(TEST_INPUT)) == 31
