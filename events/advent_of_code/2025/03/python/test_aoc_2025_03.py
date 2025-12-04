from aoc_2025_03 import parse_input, part1, part2

TEST_INPUT = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

PARSED_EXAMPLE = [
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1],
    [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9],
    [2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8],
    [8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1],
]


def test_parse_input() -> None:
    assert parse_input(TEST_INPUT) == PARSED_EXAMPLE


def test_part1() -> None:
    assert part1(PARSED_EXAMPLE) == 357


def test_part2() -> None:
    assert part2(PARSED_EXAMPLE) == 3121910778619
